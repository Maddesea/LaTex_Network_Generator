#!/usr/bin/env python3
"""
Network Diagram Generator - Python Integration Bridge
Converts various network formats to LaTeX diagram code

Supports:
- NetworkX graphs
- JSON network definitions
- GraphML files
- Nmap XML output
- CSV node/edge lists
"""

import json
import csv
import sys
from typing import Dict, List, Tuple
from pathlib import Path

try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    print("Warning: NetworkX not available. Install with: pip install networkx")

try:
    import xml.etree.ElementTree as ET
    HAS_XML = True
except ImportError:
    HAS_XML = False


class LatexNetworkGenerator:
    """Generate LaTeX network diagram code from various sources"""

    def __init__(self):
        self.nodes = []
        self.connections = []
        self.subnets = {}

    def from_json(self, json_file: str) -> str:
        """Load network from JSON file

        Format:
        {
            "nodes": [
                {"id": "web1", "ip": "192.168.1.10", "x": 0, "y": 0, "label": "Web Server", "type": "server"}
            ],
            "connections": [
                {"source": "web1", "target": "db1", "label": "SQL", "type": "encrypted"}
            ]
        }
        """
        with open(json_file) as f:
            data = json.load(f)

        latex_code = []
        latex_code.append("% Auto-generated from JSON")
        latex_code.append("\\begin{tikzpicture}[scale=1.0, transform shape, font=\\sffamily]\n")

        # Generate nodes
        for node in data.get('nodes', []):
            node_type = node.get('type', 'server')
            cmd = self._get_node_command(node_type)
            latex_code.append(f"    \\{cmd}{{{node['id']}}}{{{node['ip']}}}{{{node['x']}}}{{{node['y']}}}{{{node['label']}}}")

        latex_code.append("")

        # Generate connections
        for conn in data.get('connections', []):
            conn_type = conn.get('type', 'normal')
            cmd = self._get_connection_command(conn_type)
            latex_code.append(f"    \\{cmd}{{{conn['source']}}}{{{conn['target']}}}{{{conn.get('label', '')}}}")

        latex_code.append("\n\\end{tikzpicture}")
        return "\n".join(latex_code)

    def from_networkx(self, G: 'nx.Graph', layout_algorithm: str = 'spring') -> str:
        """Convert NetworkX graph to LaTeX

        Args:
            G: NetworkX graph
            layout_algorithm: 'spring', 'circular', 'kamada_kawai', 'spectral'
        """
        if not HAS_NETWORKX:
            raise ImportError("NetworkX required. Install with: pip install networkx")

        # Calculate layout
        if layout_algorithm == 'spring':
            pos = nx.spring_layout(G, scale=10)
        elif layout_algorithm == 'circular':
            pos = nx.circular_layout(G, scale=10)
        elif layout_algorithm == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(G, scale=10)
        elif layout_algorithm == 'spectral':
            pos = nx.spectral_layout(G, scale=10)
        else:
            pos = nx.spring_layout(G, scale=10)

        latex_code = []
        latex_code.append(f"% Auto-generated from NetworkX ({layout_algorithm} layout)")
        latex_code.append("\\begin{tikzpicture}[scale=1.0, transform shape, font=\\sffamily]\n")

        # Generate nodes
        for node in G.nodes():
            x, y = pos[node]
            node_data = G.nodes[node]
            ip = node_data.get('ip', '0.0.0.0')
            label = node_data.get('label', str(node))
            node_type = node_data.get('type', 'server')

            cmd = self._get_node_command(node_type)
            latex_code.append(f"    \\{cmd}{{{node}}}{{{ip}}}{{{x:.2f}}}{{{y:.2f}}}{{{label}}}")

        latex_code.append("")

        # Generate edges
        for source, target in G.edges():
            edge_data = G[source][target]
            label = edge_data.get('label', '')
            edge_type = edge_data.get('type', 'normal')

            cmd = self._get_connection_command(edge_type)
            latex_code.append(f"    \\{cmd}{{{source}}}{{{target}}}{{{label}}}")

        latex_code.append("\n\\end{tikzpicture}")
        return "\n".join(latex_code)

    def from_csv(self, nodes_csv: str, connections_csv: str) -> str:
        """Load network from CSV files

        nodes.csv format:
        id,ip,x,y,label,type
        web1,192.168.1.10,0,0,Web Server,server

        connections.csv format:
        source,target,label,type
        web1,db1,SQL,encrypted
        """
        latex_code = []
        latex_code.append("% Auto-generated from CSV")
        latex_code.append("\\begin{tikzpicture}[scale=1.0, transform shape, font=\\sffamily]\n")

        # Load and generate nodes
        with open(nodes_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                cmd = self._get_node_command(row.get('type', 'server'))
                latex_code.append(
                    f"    \\{cmd}{{{row['id']}}}{{{row['ip']}}}{{{row['x']}}}{{{row['y']}}}{{{row['label']}}}"
                )

        latex_code.append("")

        # Load and generate connections
        with open(connections_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                cmd = self._get_connection_command(row.get('type', 'normal'))
                latex_code.append(
                    f"    \\{cmd}{{{row['source']}}}{{{row['target']}}}{{{row.get('label', '')}}}"
                )

        latex_code.append("\n\\end{tikzpicture}")
        return "\n".join(latex_code)

    def from_nmap_xml(self, nmap_file: str) -> str:
        """Convert Nmap XML scan to network diagram

        Creates nodes for each discovered host with open ports
        """
        if not HAS_XML:
            raise ImportError("XML parsing not available")

        tree = ET.parse(nmap_file)
        root = tree.getroot()

        latex_code = []
        latex_code.append("% Auto-generated from Nmap scan")
        latex_code.append("\\begin{tikzpicture}[scale=1.0, transform shape, font=\\sffamily]\n")

        hosts = []
        for i, host in enumerate(root.findall('.//host')):
            # Get IP address
            addr = host.find('.//address[@addrtype="ipv4"]')
            if addr is None:
                continue
            ip = addr.get('addr')

            # Get hostname if available
            hostname = host.find('.//hostname')
            label = hostname.get('name') if hostname is not None else ip

            # Check for open ports
            ports = host.findall('.//port[@protocol="tcp"]/state[@state="open"]')
            num_ports = len(ports)

            # Position in grid
            x = (i % 4) * 5
            y = -(i // 4) * 3

            # Determine node type based on open ports
            node_type = 'server' if num_ports > 0 else 'client'

            latex_code.append(f"    \\createServer{{{ip.replace('.', '_')}}}{{{ip}}}{{{x}}}{{{y}}}{{{label}}}")
            hosts.append((ip, num_ports))

        latex_code.append("\n\\end{tikzpicture}")
        latex_code.append(f"\n% Discovered {len(hosts)} hosts")
        return "\n".join(latex_code)

    def to_graphviz_dot(self, output_file: str):
        """Export to GraphViz DOT format for external layout calculation"""
        dot_code = ["digraph network {"]
        dot_code.append("    rankdir=TB;")
        dot_code.append("    node [shape=box];")

        for node in self.nodes:
            dot_code.append(f"    {node['id']} [label=\"{node['label']}\"];")

        for conn in self.connections:
            dot_code.append(f"    {conn['source']} -> {conn['target']};")

        dot_code.append("}")

        with open(output_file, 'w') as f:
            f.write("\n".join(dot_code))

    def _get_node_command(self, node_type: str) -> str:
        """Map node type to LaTeX command"""
        mapping = {
            'server': 'createServer',
            'client': 'createClient',
            'router': 'createRouter',
            'firewall': 'createFirewall',
            'switch': 'createSwitch',
            'cloud': 'createCloud',
            'attacker': 'createAttacker',
        }
        return mapping.get(node_type, 'createServer')

    def _get_connection_command(self, conn_type: str) -> str:
        """Map connection type to LaTeX command"""
        mapping = {
            'normal': 'drawConnection',
            'encrypted': 'drawEncryptedConnection',
            'bidirectional': 'drawBidirectional',
            'suspicious': 'drawSuspiciousConnection',
            'attack': 'drawAttackConnection',
        }
        return mapping.get(conn_type, 'drawConnection')


def auto_layout_with_networkx(input_json: str, output_tex: str, algorithm: str = 'spring'):
    """Use NetworkX to calculate optimal layout positions"""
    if not HAS_NETWORKX:
        print("Error: NetworkX required for auto-layout")
        return

    # Load JSON
    with open(input_json) as f:
        data = json.load(f)

    # Create NetworkX graph
    G = nx.Graph()

    for node in data['nodes']:
        G.add_node(node['id'], **node)

    for conn in data['connections']:
        G.add_edge(conn['source'], conn['target'], **conn)

    # Generate LaTeX with calculated positions
    gen = LatexNetworkGenerator()
    latex_code = gen.from_networkx(G, algorithm)

    with open(output_tex, 'w') as f:
        f.write(latex_code)

    print(f"Generated {output_tex} with {algorithm} layout")


def main():
    """Command-line interface"""
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 latex_bridge.py json input.json output.tex")
        print("  python3 latex_bridge.py csv nodes.csv connections.csv output.tex")
        print("  python3 latex_bridge.py nmap scan.xml output.tex")
        print("  python3 latex_bridge.py auto-layout input.json output.tex [algorithm]")
        print("")
        print("Algorithms: spring, circular, kamada_kawai, spectral")
        return

    command = sys.argv[1]
    gen = LatexNetworkGenerator()

    if command == 'json':
        latex_code = gen.from_json(sys.argv[2])
        with open(sys.argv[3], 'w') as f:
            f.write(latex_code)
        print(f"Generated {sys.argv[3]} from JSON")

    elif command == 'csv':
        latex_code = gen.from_csv(sys.argv[2], sys.argv[3])
        with open(sys.argv[4], 'w') as f:
            f.write(latex_code)
        print(f"Generated {sys.argv[4]} from CSV")

    elif command == 'nmap':
        latex_code = gen.from_nmap_xml(sys.argv[2])
        with open(sys.argv[3], 'w') as f:
            f.write(latex_code)
        print(f"Generated {sys.argv[3]} from Nmap XML")

    elif command == 'auto-layout':
        algorithm = sys.argv[4] if len(sys.argv) > 4 else 'spring'
        auto_layout_with_networkx(sys.argv[2], sys.argv[3], algorithm)

    else:
        print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()
