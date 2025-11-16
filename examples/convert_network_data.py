#!/usr/bin/env python3
"""
Network Data Converter
Converts between different network diagram data formats
Supports: JSON, YAML, CSV, Nmap XML, Nessus XML

Usage:
    python convert_network_data.py input.json output.yaml
    python convert_network_data.py nodes.csv output.json
    python convert_network_data.py nmap_scan.xml output.json
"""

import json
import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    print("Warning: PyYAML not installed. YAML support disabled.")
    print("Install with: pip install pyyaml")


class NetworkDataConverter:
    """Convert between different network diagram data formats"""

    def __init__(self):
        self.nodes = []
        self.connections = []
        self.threats = []

    def load_json(self, filename):
        """Load data from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.nodes = data.get('nodes', [])
            self.connections = data.get('connections', [])
            self.threats = data.get('threats', [])
        print(f"Loaded {len(self.nodes)} nodes, {len(self.connections)} connections from JSON")

    def load_yaml(self, filename):
        """Load data from YAML file"""
        if not YAML_AVAILABLE:
            raise ImportError("PyYAML is required for YAML support")

        with open(filename, 'r') as f:
            data = yaml.safe_load(f)
            self.nodes = data.get('nodes', [])
            self.connections = data.get('connections', [])
            self.threats = data.get('threats', [])
        print(f"Loaded {len(self.nodes)} nodes, {len(self.connections)} connections from YAML")

    def load_csv_nodes(self, filename):
        """Load nodes from CSV file"""
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            self.nodes = []
            for row in reader:
                node = {
                    'id': row['id'],
                    'type': row['type'],
                    'ip': row['ip'],
                    'x': float(row['x']),
                    'y': float(row['y']),
                    'label': row['label']
                }
                if 'ports' in row and row['ports']:
                    node['ports'] = [int(p) for p in row['ports'].split(',')]
                self.nodes.append(node)
        print(f"Loaded {len(self.nodes)} nodes from CSV")

    def load_csv_connections(self, filename):
        """Load connections from CSV file"""
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            self.connections = []
            for row in reader:
                conn = {
                    'source': row['source'],
                    'dest': row['dest'],
                    'type': row['type'],
                    'label': row.get('label', '')
                }
                self.connections.append(conn)
        print(f"Loaded {len(self.connections)} connections from CSV")

    def load_nmap_xml(self, filename):
        """Load data from Nmap XML file"""
        tree = ET.parse(filename)
        root = tree.getroot()

        self.nodes = []
        x, y = 0, 0
        nodes_per_row = 4

        for i, host in enumerate(root.findall('.//host')):
            # Get IP address
            addr = host.find('.//address[@addrtype="ipv4"]')
            if addr is None:
                continue

            ip = addr.get('addr')

            # Get hostname
            hostname_elem = host.find('.//hostname')
            hostname = hostname_elem.get('name') if hostname_elem is not None else ip

            # Get open ports
            ports = []
            for port in host.findall('.//port'):
                state = port.find('state')
                if state is not None and state.get('state') == 'open':
                    ports.append(int(port.get('portid')))

            # Calculate position
            x = (i % nodes_per_row) * 3
            y = -(i // nodes_per_row) * 2

            node = {
                'id': f"nmap_host{i+1}",
                'type': 'server',
                'ip': ip,
                'x': x,
                'y': y,
                'label': hostname
            }

            if ports:
                node['ports'] = ports[:6]  # Limit to 6 ports

            self.nodes.append(node)

        print(f"Loaded {len(self.nodes)} hosts from Nmap XML")

    def load_nessus_xml(self, filename):
        """Load data from Nessus .nessus XML file"""
        tree = ET.parse(filename)
        root = tree.getroot()

        self.nodes = []
        self.threats = []
        x, y = 0, 0
        nodes_per_row = 4

        for i, host in enumerate(root.findall('.//ReportHost')):
            # Get hostname and IP
            hostname = host.get('name')

            # Get IP from properties
            ip_elem = host.find('.//tag[@name="host-ip"]')
            ip = ip_elem.text if ip_elem is not None else hostname

            # Calculate position
            x = (i % nodes_per_row) * 3
            y = -(i // nodes_per_row) * 2

            node = {
                'id': f"nessus_host{i+1}",
                'type': 'server',
                'ip': ip,
                'x': x,
                'y': y,
                'label': hostname
            }

            self.nodes.append(node)

            # Extract vulnerabilities
            for item in host.findall('.//ReportItem'):
                severity = int(item.get('severity', 0))

                if severity >= 2:  # Medium or higher
                    cvss_elem = item.find('cvss3_base_score')
                    if cvss_elem is None:
                        cvss_elem = item.find('cvss_base_score')

                    cve_elem = item.find('cve')

                    if cvss_elem is not None and cve_elem is not None:
                        threat = {
                            'target': node['id'],
                            'type': 'vulnerability',
                            'cve': cve_elem.text,
                            'severity': float(cvss_elem.text),
                            'description': item.get('pluginName', '')
                        }
                        self.threats.append(threat)

        print(f"Loaded {len(self.nodes)} hosts and {len(self.threats)} vulnerabilities from Nessus XML")

    def save_json(self, filename):
        """Save data to JSON file"""
        data = {
            'nodes': self.nodes,
            'connections': self.connections
        }
        if self.threats:
            data['threats'] = self.threats

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Saved to JSON: {filename}")

    def save_yaml(self, filename):
        """Save data to YAML file"""
        if not YAML_AVAILABLE:
            raise ImportError("PyYAML is required for YAML support")

        data = {
            'nodes': self.nodes,
            'connections': self.connections
        }
        if self.threats:
            data['threats'] = self.threats

        with open(filename, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        print(f"Saved to YAML: {filename}")

    def save_csv_nodes(self, filename):
        """Save nodes to CSV file"""
        if not self.nodes:
            print("No nodes to save")
            return

        with open(filename, 'w', newline='') as f:
            fieldnames = ['id', 'type', 'ip', 'x', 'y', 'label', 'ports']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for node in self.nodes:
                row = {
                    'id': node.get('id', ''),
                    'type': node.get('type', 'server'),
                    'ip': node.get('ip', ''),
                    'x': node.get('x', 0),
                    'y': node.get('y', 0),
                    'label': node.get('label', ''),
                    'ports': ','.join(map(str, node.get('ports', [])))
                }
                writer.writerow(row)
        print(f"Saved nodes to CSV: {filename}")

    def save_csv_connections(self, filename):
        """Save connections to CSV file"""
        if not self.connections:
            print("No connections to save")
            return

        with open(filename, 'w', newline='') as f:
            fieldnames = ['source', 'dest', 'type', 'label']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for conn in self.connections:
                writer.writerow(conn)
        print(f"Saved connections to CSV: {filename}")

    def auto_generate_connections(self):
        """Auto-generate basic connections based on node types"""
        if len(self.nodes) < 2:
            print("Need at least 2 nodes to generate connections")
            return

        self.connections = []

        # Find routers and firewalls
        routers = [n for n in self.nodes if n['type'] == 'router']
        firewalls = [n for n in self.nodes if n['type'] == 'firewall']
        servers = [n for n in self.nodes if n['type'] == 'server']
        clients = [n for n in self.nodes if n['type'] == 'client']

        # Connect firewalls to routers
        for fw in firewalls:
            if routers:
                self.connections.append({
                    'source': fw['id'],
                    'dest': routers[0]['id'],
                    'type': 'normal',
                    'label': ''
                })

        # Connect routers to servers
        for router in routers:
            for server in servers:
                self.connections.append({
                    'source': router['id'],
                    'dest': server['id'],
                    'type': 'normal',
                    'label': ''
                })

        # Connect servers to clients
        if servers and clients:
            for client in clients:
                self.connections.append({
                    'source': servers[0]['id'],
                    'dest': client['id'],
                    'type': 'bidirectional',
                    'label': ''
                })

        print(f"Generated {len(self.connections)} connections")


def main():
    if len(sys.argv) < 3:
        print("Usage: python convert_network_data.py <input_file> <output_file>")
        print()
        print("Supported formats:")
        print("  - JSON (.json)")
        print("  - YAML (.yaml, .yml)")
        print("  - CSV (.csv) - separate files for nodes/connections")
        print("  - Nmap XML (.xml)")
        print("  - Nessus XML (.nessus)")
        print()
        print("Examples:")
        print("  python convert_network_data.py nmap_scan.xml network.json")
        print("  python convert_network_data.py network.json network.yaml")
        print("  python convert_network_data.py network.json nodes.csv")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    converter = NetworkDataConverter()

    # Load input file
    input_ext = input_file.suffix.lower()

    if input_ext == '.json':
        converter.load_json(input_file)
    elif input_ext in ['.yaml', '.yml']:
        converter.load_yaml(input_file)
    elif input_ext == '.csv':
        # Assume nodes CSV, look for connections CSV
        converter.load_csv_nodes(input_file)
        conn_file = input_file.parent / f"connections{input_ext}"
        if conn_file.exists():
            converter.load_csv_connections(conn_file)
        else:
            print("Generating basic connections...")
            converter.auto_generate_connections()
    elif input_ext == '.xml':
        converter.load_nmap_xml(input_file)
        converter.auto_generate_connections()
    elif input_ext == '.nessus':
        converter.load_nessus_xml(input_file)
        converter.auto_generate_connections()
    else:
        print(f"Error: Unsupported input format: {input_ext}")
        sys.exit(1)

    # Save output file
    output_ext = output_file.suffix.lower()

    if output_ext == '.json':
        converter.save_json(output_file)
    elif output_ext in ['.yaml', '.yml']:
        converter.save_yaml(output_file)
    elif output_ext == '.csv':
        converter.save_csv_nodes(output_file)
        conn_file = output_file.parent / f"connections{output_ext}"
        converter.save_csv_connections(conn_file)
    else:
        print(f"Error: Unsupported output format: {output_ext}")
        sys.exit(1)

    print()
    print("Conversion complete!")
    print(f"  Nodes: {len(converter.nodes)}")
    print(f"  Connections: {len(converter.connections)}")
    print(f"  Threats: {len(converter.threats)}")


if __name__ == '__main__':
    main()
