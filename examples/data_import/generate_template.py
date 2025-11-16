#!/usr/bin/env python3
"""
generate_template.py - Generate CSV templates for network diagrams

This script generates template CSV files that can be filled in with
your network data. It creates properly formatted files with headers
and example rows.

Usage:
    python3 generate_template.py nodes
    python3 generate_template.py connections
    python3 generate_template.py threats
    python3 generate_template.py --all
    python3 generate_template.py --all --auto-position
"""

import sys
import csv
from pathlib import Path

# ANSI color codes
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'

def generate_nodes_template(auto_position=False):
    """Generate nodes CSV template"""
    if auto_position:
        filename = 'nodes_template_auto.csv'
        headers = ['id', 'type', 'ip', 'label']
        example_rows = [
            ['fw1', 'firewall', '192.168.1.1', 'Edge Firewall'],
            ['rtr1', 'router', '192.168.1.2', 'Core Router'],
            ['web1', 'server', '192.168.10.10', 'Web Server'],
            ['web2', 'server', '192.168.10.11', 'Web Server 2'],
            ['app1', 'server', '192.168.20.10', 'App Server'],
            ['db1', 'server', '192.168.30.10', 'Database'],
            ['ws1', 'client', '192.168.100.50', 'Workstation 1'],
            ['ws2', 'client', '192.168.100.51', 'Workstation 2'],
        ]
    else:
        filename = 'nodes_template.csv'
        headers = ['id', 'type', 'ip', 'x', 'y', 'label']
        example_rows = [
            ['fw1', 'firewall', '192.168.1.1', '0', '5', 'Edge Firewall'],
            ['rtr1', 'router', '192.168.1.2', '-3', '3', 'Core Router'],
            ['web1', 'server', '192.168.10.10', '-3', '1', 'Web Server'],
            ['web2', 'server', '192.168.10.11', '3', '1', 'Web Server 2'],
            ['app1', 'server', '192.168.20.10', '-4', '-3', 'App Server'],
            ['db1', 'server', '192.168.30.10', '4', '-3', 'Database'],
            ['ws1', 'client', '192.168.100.50', '-6', '-5', 'Workstation 1'],
            ['ws2', 'client', '192.168.100.51', '0', '-5', 'Workstation 2'],
        ]

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(example_rows)

    print(f"{GREEN}✓ Created: {filename}{NC}")
    print(f"{BLUE}  Headers: {', '.join(headers)}{NC}")
    print(f"{BLUE}  Example rows: {len(example_rows)}{NC}")

    if auto_position:
        print(f"{YELLOW}  Usage: \\importNodesAutoPositioned{{{filename}}}{NC}")
    else:
        print(f"{YELLOW}  Usage: \\importNodesFromCSV{{{filename}}}{NC}")

def generate_connections_template():
    """Generate connections CSV template"""
    filename = 'connections_template.csv'
    headers = ['source', 'destination', 'label', 'type']

    example_rows = [
        ['fw1', 'rtr1', '', 'normal'],
        ['rtr1', 'web1', '', 'normal'],
        ['rtr1', 'web2', '', 'normal'],
        ['web1', 'app1', 'HTTPS', 'encrypted'],
        ['web2', 'app1', 'HTTPS', 'encrypted'],
        ['app1', 'db1', 'TLS 1.3', 'encrypted'],
        ['ws1', 'web1', '', 'bidirectional'],
        ['ws2', 'web1', '', 'bidirectional'],
    ]

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(example_rows)

    print(f"{GREEN}✓ Created: {filename}{NC}")
    print(f"{BLUE}  Headers: {', '.join(headers)}{NC}")
    print(f"{BLUE}  Example rows: {len(example_rows)}{NC}")
    print(f"{YELLOW}  Usage: \\importConnectionsFromCSV{{{filename}}}{NC}")
    print(f"{BLUE}  Valid types: normal, encrypted, attack, suspicious, bidirectional{NC}")

def generate_threats_template():
    """Generate threats CSV template"""
    filename = 'threats_template.csv'
    headers = ['target', 'type', 'severity', 'cve', 'description']

    example_rows = [
        ['web1', 'vulnerability', '9.8', 'CVE-2024-1234', 'SQL Injection vulnerability'],
        ['web1', 'vulnerability', '7.5', 'CVE-2024-5678', 'XSS vulnerability'],
        ['db1', 'vulnerability', '8.9', 'CVE-2024-9999', 'Authentication bypass'],
        ['ws2', 'malware', '8.5', 'N/A', 'Ransomware detected'],
        ['fw1', 'vulnerability', '6.5', 'CVE-2024-1111', 'Configuration weakness'],
    ]

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(example_rows)

    print(f"{GREEN}✓ Created: {filename}{NC}")
    print(f"{BLUE}  Headers: {', '.join(headers)}{NC}")
    print(f"{BLUE}  Example rows: {len(example_rows)}{NC}")
    print(f"{YELLOW}  Usage: \\importThreatsFromCSV{{{filename}}}{NC}")
    print(f"{BLUE}  Valid types: vulnerability, malware{NC}")
    print(f"{BLUE}  Severity: CVSS score 0-10{NC}")

def generate_network_json_template():
    """Generate JSON network template"""
    filename = 'network_template.json'

    template = """{
  "network": {
    "name": "My Network",
    "version": "1.0",
    "description": "Network topology description"
  },
  "nodes": [
    {
      "id": "fw1",
      "type": "firewall",
      "ip": "192.168.1.1",
      "position": {"x": 0, "y": 5},
      "label": "Edge Firewall",
      "properties": {
        "vendor": "Cisco",
        "model": "ASA 5506-X"
      }
    },
    {
      "id": "web1",
      "type": "server",
      "ip": "192.168.10.10",
      "position": {"x": -3, "y": 1},
      "label": "Web Server",
      "ports": ["80", "443"],
      "services": ["nginx"]
    },
    {
      "id": "db1",
      "type": "server",
      "ip": "192.168.30.10",
      "position": {"x": 4, "y": -3},
      "label": "Database Server",
      "ports": ["3306"],
      "services": ["mysql"]
    }
  ],
  "connections": [
    {
      "source": "fw1",
      "destination": "web1",
      "type": "normal",
      "protocol": "TCP"
    },
    {
      "source": "web1",
      "destination": "db1",
      "type": "encrypted",
      "label": "TLS 1.3",
      "protocol": "TCP"
    }
  ],
  "threats": [
    {
      "target": "web1",
      "type": "vulnerability",
      "severity": 9.8,
      "cve": "CVE-2024-1234",
      "description": "SQL Injection vulnerability"
    }
  ]
}
"""

    with open(filename, 'w') as f:
        f.write(template)

    print(f"{GREEN}✓ Created: {filename}{NC}")
    print(f"{YELLOW}  Usage (requires LuaLaTeX): \\importNetworkFromJSON{{{filename}}}{NC}")

def main():
    """Main template generation function"""
    if len(sys.argv) < 2:
        print("Usage: python3 generate_template.py <type> [options]")
        print("")
        print("Types:")
        print("  nodes              Generate nodes CSV template")
        print("  connections        Generate connections CSV template")
        print("  threats            Generate threats CSV template")
        print("  json               Generate JSON network template")
        print("  --all              Generate all templates")
        print("")
        print("Options:")
        print("  --auto-position    Generate auto-positioning template (nodes only)")
        print("")
        print("Examples:")
        print("  python3 generate_template.py nodes")
        print("  python3 generate_template.py nodes --auto-position")
        print("  python3 generate_template.py --all")
        sys.exit(1)

    template_type = sys.argv[1]
    auto_position = '--auto-position' in sys.argv

    print(f"{BLUE}{'='*60}{NC}")
    print(f"{BLUE}Network Diagram Template Generator{NC}")
    print(f"{BLUE}{'='*60}{NC}")
    print("")

    if template_type == 'nodes':
        generate_nodes_template(auto_position)
    elif template_type == 'connections':
        generate_connections_template()
    elif template_type == 'threats':
        generate_threats_template()
    elif template_type == 'json':
        generate_network_json_template()
    elif template_type == '--all':
        generate_nodes_template(auto_position=False)
        print("")
        generate_nodes_template(auto_position=True)
        print("")
        generate_connections_template()
        print("")
        generate_threats_template()
        print("")
        generate_network_json_template()
        print("")
        print(f"{GREEN}✓ All templates generated!{NC}")
        print(f"{BLUE}Edit the template files and import them into your LaTeX document{NC}")
    else:
        print(f"{YELLOW}Unknown template type: {template_type}{NC}")
        print(f"{YELLOW}Valid types: nodes, connections, threats, json, --all{NC}")
        sys.exit(1)

    print("")
    print(f"{BLUE}{'='*60}{NC}")
    print(f"{GREEN}✓ Template generation complete{NC}")
    print(f"{BLUE}{'='*60}{NC}")
    print("")
    print(f"{YELLOW}Next steps:{NC}")
    print(f"{YELLOW}1. Edit the template file(s) with your network data{NC}")
    print(f"{YELLOW}2. Validate: python3 validate_data.py <filename>{NC}")
    print(f"{YELLOW}3. Import into your LaTeX document{NC}")

if __name__ == '__main__':
    main()
