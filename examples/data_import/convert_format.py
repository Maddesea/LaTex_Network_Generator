#!/usr/bin/env python3
"""
convert_format.py - Convert between network data formats

This script converts network data between different formats:
- CSV to JSON
- JSON to CSV
- Nmap XML to CSV
- CSV to GraphML (for Gephi/Cytoscape)

Usage:
    python3 convert_format.py nodes.csv --to json
    python3 convert_format.py network.json --to csv
    python3 convert_format.py nmap-scan.xml --to csv
    python3 convert_format.py nodes.csv connections.csv --to graphml
"""

import sys
import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path
import html

# ANSI color codes
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
RED = '\033[0;31m'
NC = '\033[0m'

class FormatConverter:
    """Convert between network data formats"""

    def __init__(self):
        self.nodes = []
        self.connections = []
        self.threats = []

    def csv_to_json(self, nodes_file, connections_file=None, threats_file=None, output_file='network.json'):
        """Convert CSV files to JSON"""
        data = {
            "network": {
                "name": "Imported Network",
                "version": "1.0"
            },
            "nodes": [],
            "connections": [],
            "threats": []
        }

        # Load nodes
        with open(nodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                node = {
                    "id": row.get('id', '').strip(),
                    "type": row.get('type', '').strip(),
                    "ip": row.get('ip', '').strip(),
                    "label": row.get('label', '').strip()
                }

                # Add position if available
                if 'x' in row and 'y' in row:
                    try:
                        node["position"] = {
                            "x": float(row['x']),
                            "y": float(row['y'])
                        }
                    except ValueError:
                        pass

                data["nodes"].append(node)

        # Load connections if provided
        if connections_file and Path(connections_file).exists():
            with open(connections_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    conn = {
                        "source": row.get('source', '').strip(),
                        "destination": row.get('destination', '').strip()
                    }

                    if row.get('type'):
                        conn["type"] = row.get('type', '').strip()
                    if row.get('label'):
                        conn["label"] = row.get('label', '').strip()

                    data["connections"].append(conn)

        # Load threats if provided
        if threats_file and Path(threats_file).exists():
            with open(threats_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    threat = {
                        "target": row.get('target', '').strip(),
                        "type": row.get('type', '').strip()
                    }

                    if row.get('severity'):
                        try:
                            threat["severity"] = float(row.get('severity'))
                        except ValueError:
                            threat["severity"] = row.get('severity', '').strip()

                    if row.get('cve'):
                        threat["cve"] = row.get('cve', '').strip()
                    if row.get('description'):
                        threat["description"] = row.get('description', '').strip()

                    data["threats"].append(threat)

        # Write JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        print(f"{GREEN}✓ Converted to JSON: {output_file}{NC}")
        print(f"{BLUE}  Nodes: {len(data['nodes'])}{NC}")
        print(f"{BLUE}  Connections: {len(data['connections'])}{NC}")
        print(f"{BLUE}  Threats: {len(data['threats'])}{NC}")

    def json_to_csv(self, json_file):
        """Convert JSON to CSV files"""
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract nodes
        nodes = data.get('nodes', [])
        if data.get('network', {}).get('nodes'):
            nodes = data['network']['nodes']

        if nodes:
            with open('nodes_from_json.csv', 'w', newline='', encoding='utf-8') as f:
                has_position = any('position' in node for node in nodes)

                if has_position:
                    fieldnames = ['id', 'type', 'ip', 'x', 'y', 'label']
                else:
                    fieldnames = ['id', 'type', 'ip', 'label']

                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for node in nodes:
                    row = {
                        'id': node.get('id', ''),
                        'type': node.get('type', ''),
                        'ip': node.get('ip', ''),
                        'label': node.get('label', '')
                    }

                    if has_position and 'position' in node:
                        row['x'] = node['position'].get('x', 0)
                        row['y'] = node['position'].get('y', 0)

                    writer.writerow(row)

            print(f"{GREEN}✓ Created: nodes_from_json.csv ({len(nodes)} nodes){NC}")

        # Extract connections
        connections = data.get('connections', [])
        if data.get('network', {}).get('connections'):
            connections = data['network']['connections']

        if connections:
            with open('connections_from_json.csv', 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['source', 'destination', 'label', 'type']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for conn in connections:
                    writer.writerow({
                        'source': conn.get('source', ''),
                        'destination': conn.get('destination', ''),
                        'label': conn.get('label', ''),
                        'type': conn.get('type', '')
                    })

            print(f"{GREEN}✓ Created: connections_from_json.csv ({len(connections)} connections){NC}")

        # Extract threats
        threats = data.get('threats', [])
        if data.get('network', {}).get('threats'):
            threats = data['network']['threats']

        if threats:
            with open('threats_from_json.csv', 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['target', 'type', 'severity', 'cve', 'description']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for threat in threats:
                    writer.writerow({
                        'target': threat.get('target', ''),
                        'type': threat.get('type', ''),
                        'severity': threat.get('severity', ''),
                        'cve': threat.get('cve', ''),
                        'description': threat.get('description', '')
                    })

            print(f"{GREEN}✓ Created: threats_from_json.csv ({len(threats)} threats){NC}")

    def nmap_to_csv(self, nmap_file):
        """Convert Nmap XML to CSV"""
        tree = ET.parse(nmap_file)
        root = tree.getroot()

        nodes = []
        node_id = 1

        for host in root.findall('.//host'):
            # Get IP address
            addr_elem = host.find('.//address[@addrtype="ipv4"]')
            if addr_elem is None:
                continue

            ip = addr_elem.get('addr')

            # Get hostname
            hostname_elem = host.find('.//hostname')
            if hostname_elem is not None:
                label = hostname_elem.get('name')
            else:
                label = f"Host-{node_id}"

            # Get open ports
            ports = []
            for port in host.findall('.//port'):
                state = port.find('state')
                if state is not None and state.get('state') == 'open':
                    ports.append(port.get('portid'))

            nodes.append({
                'id': f"nmap_{node_id}",
                'type': 'server',
                'ip': ip,
                'label': label,
                'ports': ','.join(ports) if ports else ''
            })

            node_id += 1

        # Write CSV
        with open('nodes_from_nmap.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'type', 'ip', 'label', 'ports']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(nodes)

        print(f"{GREEN}✓ Converted Nmap XML to CSV: nodes_from_nmap.csv{NC}")
        print(f"{BLUE}  Discovered {len(nodes)} hosts{NC}")

    def csv_to_graphml(self, nodes_file, connections_file, output_file='network.graphml'):
        """Convert CSV to GraphML format"""
        # Read nodes
        nodes = []
        with open(nodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            nodes = list(reader)

        # Read connections
        connections = []
        if Path(connections_file).exists():
            with open(connections_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                connections = list(reader)

        # Generate GraphML
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n')
            f.write('  <key id="label" for="node" attr.name="label" attr.type="string"/>\n')
            f.write('  <key id="type" for="node" attr.name="type" attr.type="string"/>\n')
            f.write('  <key id="ip" for="node" attr.name="ip" attr.type="string"/>\n')
            f.write('  <graph id="network" edgedefault="directed">\n')

            # Write nodes
            for node in nodes:
                node_id = html.escape(node.get('id', '').strip())
                node_label = html.escape(node.get('label', ''))
                node_type = html.escape(node.get('type', ''))
                node_ip = html.escape(node.get('ip', ''))
                f.write(f'    <node id="{node_id}">\n')
                f.write(f'      <data key="label">{node_label}</data>\n')
                f.write(f'      <data key="type">{node_type}</data>\n')
                f.write(f'      <data key="ip">{node_ip}</data>\n')
                f.write(f'    </node>\n')

            # Write edges
            edge_id = 0
            for conn in connections:
                source = html.escape(conn.get('source', '').strip())
                dest = html.escape(conn.get('destination', '').strip())
                f.write(f'    <edge id="e{edge_id}" source="{source}" target="{dest}"/>\n')
                edge_id += 1

            f.write('  </graph>\n')
            f.write('</graphml>\n')

        print(f"{GREEN}✓ Converted to GraphML: {output_file}{NC}")
        print(f"{BLUE}  Nodes: {len(nodes)}{NC}")
        print(f"{BLUE}  Edges: {len(connections)}{NC}")
        print(f"{BLUE}  Can be imported into Gephi or Cytoscape{NC}")

def main():
    """Main conversion function"""
    if len(sys.argv) < 3:
        print("Usage: python3 convert_format.py <input_file> --to <format> [additional_files]")
        print("")
        print("Examples:")
        print("  python3 convert_format.py nodes.csv --to json")
        print("  python3 convert_format.py nodes.csv connections.csv --to json")
        print("  python3 convert_format.py network.json --to csv")
        print("  python3 convert_format.py nmap-scan.xml --to csv")
        print("  python3 convert_format.py nodes.csv connections.csv --to graphml")
        print("")
        print("Supported conversions:")
        print("  CSV → JSON")
        print("  JSON → CSV")
        print("  Nmap XML → CSV")
        print("  CSV → GraphML")
        sys.exit(1)

    converter = FormatConverter()

    # Parse arguments
    if '--to' not in sys.argv:
        print(f"{RED}Error: --to flag required{NC}")
        sys.exit(1)

    to_index = sys.argv.index('--to')
    if to_index + 1 >= len(sys.argv):
        print(f"{RED}Error: output format not specified{NC}")
        sys.exit(1)

    output_format = sys.argv[to_index + 1].lower()
    input_files = sys.argv[1:to_index]

    print(f"{BLUE}{'='*60}{NC}")
    print(f"{BLUE}Network Data Format Converter{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

    try:
        if output_format == 'json':
            nodes_file = input_files[0]
            connections_file = input_files[1] if len(input_files) > 1 else None
            threats_file = input_files[2] if len(input_files) > 2 else None
            converter.csv_to_json(nodes_file, connections_file, threats_file)

        elif output_format == 'csv':
            input_file = input_files[0]
            if input_file.endswith('.json'):
                converter.json_to_csv(input_file)
            elif input_file.endswith('.xml'):
                converter.nmap_to_csv(input_file)
            else:
                print(f"{RED}Unknown input format for CSV conversion{NC}")
                sys.exit(1)

        elif output_format == 'graphml':
            if len(input_files) < 2:
                print(f"{RED}GraphML conversion requires nodes.csv and connections.csv{NC}")
                sys.exit(1)
            converter.csv_to_graphml(input_files[0], input_files[1])

        else:
            print(f"{RED}Unknown output format: {output_format}{NC}")
            sys.exit(1)

        print(f"\n{GREEN}✓ Conversion complete{NC}\n")

    except FileNotFoundError as e:
        print(f"{RED}Error: {e}{NC}")
        sys.exit(1)
    except Exception as e:
        print(f"{RED}Conversion error: {e}{NC}")
        sys.exit(1)

if __name__ == '__main__':
    main()
