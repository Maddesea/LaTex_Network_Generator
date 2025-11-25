#!/usr/bin/env python3
"""
network_stats.py - Generate statistics and reports from network data

This script analyzes network CSV/JSON files and generates useful
statistics and reports about the network topology.

Usage:
    python3 network_stats.py nodes.csv connections.csv
    python3 network_stats.py --all
    python3 network_stats.py --latex nodes.csv connections.csv
"""

import sys
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

# ANSI color codes
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
RED = '\033[0;31m'
NC = '\033[0m'

class NetworkStats:
    """Analyze network topology data"""

    def __init__(self):
        self.nodes = []
        self.connections = []
        self.threats = []

    def load_nodes_csv(self, filepath):
        """Load nodes from CSV"""
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.nodes = list(reader)

    def load_connections_csv(self, filepath):
        """Load connections from CSV"""
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.connections = list(reader)

    def load_threats_csv(self, filepath):
        """Load threats from CSV"""
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.threats = list(reader)

    def analyze_nodes(self):
        """Analyze node statistics"""
        print(f"\n{BLUE}{'='*60}{NC}")
        print(f"{BLUE}NODE STATISTICS{NC}")
        print(f"{BLUE}{'='*60}{NC}\n")

        total_nodes = len(self.nodes)
        print(f"{CYAN}Total Nodes: {total_nodes}{NC}\n")

        # Node types
        node_types = Counter(node.get('type', '').strip() for node in self.nodes)
        print(f"{GREEN}Node Types:{NC}")
        for node_type, count in sorted(node_types.items()):
            percentage = (count / total_nodes * 100) if total_nodes > 0 else 0
            print(f"  {node_type:15} {count:4} ({percentage:5.1f}%)")

        # IP address analysis
        print(f"\n{GREEN}IP Address Distribution:{NC}")
        subnets = defaultdict(int)
        for node in self.nodes:
            ip = node.get('ip', '').strip()
            if ip:
                # Extract /24 subnet
                parts = ip.split('.')
                if len(parts) >= 3:
                    subnet = '.'.join(parts[:3]) + '.0/24'
                    subnets[subnet] += 1

        for subnet, count in sorted(subnets.items(), key=lambda x: x[1], reverse=True):
            print(f"  {subnet:20} {count:4} nodes")

        # Check for missing IPs
        nodes_without_ip = sum(1 for node in self.nodes if not node.get('ip', '').strip())
        if nodes_without_ip > 0:
            print(f"\n{YELLOW}  ⚠ {nodes_without_ip} nodes without IP address{NC}")

    def analyze_connections(self):
        """Analyze connection statistics"""
        print(f"\n{BLUE}{'='*60}{NC}")
        print(f"{BLUE}CONNECTION STATISTICS{NC}")
        print(f"{BLUE}{'='*60}{NC}\n")

        total_connections = len(self.connections)
        print(f"{CYAN}Total Connections: {total_connections}{NC}\n")

        # Connection types
        conn_types = Counter(conn.get('type', 'normal').strip() or 'normal'
                            for conn in self.connections)
        print(f"{GREEN}Connection Types:{NC}")
        for conn_type, count in sorted(conn_types.items()):
            percentage = (count / total_connections * 100) if total_connections > 0 else 0
            print(f"  {conn_type:15} {count:4} ({percentage:5.1f}%)")

        # Most connected nodes
        print(f"\n{GREEN}Most Connected Nodes:{NC}")
        node_connections = defaultdict(int)
        for conn in self.connections:
            source = conn.get('source', '').strip()
            dest = conn.get('destination', '').strip()
            if source:
                node_connections[source] += 1
            if dest:
                node_connections[dest] += 1

        # Top 10 most connected
        top_connected = sorted(node_connections.items(), key=lambda x: x[1], reverse=True)[:10]
        for node_id, conn_count in top_connected:
            print(f"  {node_id:20} {conn_count:4} connections")

        # Isolated nodes (no connections)
        if self.nodes:
            all_node_ids = {node.get('id', '').strip() for node in self.nodes}
            connected_node_ids = set(node_connections.keys())
            isolated = all_node_ids - connected_node_ids
            if isolated:
                print(f"\n{YELLOW}  ⚠ {len(isolated)} isolated nodes (no connections):{NC}")
                for node_id in sorted(isolated)[:10]:  # Show first 10
                    print(f"    - {node_id}")
                if len(isolated) > 10:
                    print(f"    ... and {len(isolated) - 10} more")

    def analyze_threats(self):
        """Analyze threat statistics"""
        print(f"\n{BLUE}{'='*60}{NC}")
        print(f"{BLUE}THREAT STATISTICS{NC}")
        print(f"{BLUE}{'='*60}{NC}\n")

        if not self.threats:
            print(f"{YELLOW}No threat data loaded{NC}")
            return

        total_threats = len(self.threats)
        print(f"{CYAN}Total Threats: {total_threats}{NC}\n")

        # Threat types
        threat_types = Counter(threat.get('type', '').strip() for threat in self.threats)
        print(f"{GREEN}Threat Types:{NC}")
        for threat_type, count in sorted(threat_types.items()):
            percentage = (count / total_threats * 100) if total_threats > 0 else 0
            print(f"  {threat_type:15} {count:4} ({percentage:5.1f}%)")

        # Severity distribution
        print(f"\n{GREEN}Severity Distribution:{NC}")
        severity_ranges = {
            'Critical (9.0-10.0)': 0,
            'High (7.0-8.9)': 0,
            'Medium (4.0-6.9)': 0,
            'Low (0.1-3.9)': 0,
            'Info (0.0)': 0
        }

        for threat in self.threats:
            try:
                severity = float(threat.get('severity', '0').strip())
                if severity >= 9.0:
                    severity_ranges['Critical (9.0-10.0)'] += 1
                elif severity >= 7.0:
                    severity_ranges['High (7.0-8.9)'] += 1
                elif severity >= 4.0:
                    severity_ranges['Medium (4.0-6.9)'] += 1
                elif severity > 0:
                    severity_ranges['Low (0.1-3.9)'] += 1
                else:
                    severity_ranges['Info (0.0)'] += 1
            except ValueError:
                pass

        for severity_range, count in severity_ranges.items():
            if count > 0:
                percentage = (count / total_threats * 100) if total_threats > 0 else 0
                print(f"  {severity_range:25} {count:4} ({percentage:5.1f}%)")

        # Most vulnerable nodes
        print(f"\n{GREEN}Most Vulnerable Nodes:{NC}")
        node_threats = Counter(threat.get('target', '').strip() for threat in self.threats)
        top_vulnerable = sorted(node_threats.items(), key=lambda x: x[1], reverse=True)[:10]
        for node_id, threat_count in top_vulnerable:
            print(f"  {node_id:20} {threat_count:4} threats")

    def generate_latex_summary(self):
        """Generate LaTeX code for summary statistics"""
        print(f"\n{BLUE}{'='*60}{NC}")
        print(f"{BLUE}LATEX SUMMARY CODE{NC}")
        print(f"{BLUE}{'='*60}{NC}\n")

        print("% Network Statistics Summary")
        print("% Copy this into your LaTeX document")
        print("")
        print("\\node[draw=black!20, fill=white, rounded corners=3pt, anchor=north west] at (-10,9) {")
        print("    \\tiny\\bfseries Network Statistics \\\\[2pt]")
        print("    \\begin{tabular}{lr}")
        print(f"        Total Nodes: & {len(self.nodes)} \\\\")
        print(f"        Total Connections: & {len(self.connections)} \\\\")

        if self.threats:
            print(f"        Total Threats: & {len(self.threats)} \\\\")

            # Count critical threats
            critical = 0
            for t in self.threats:
                try:
                    if float(t.get('severity', '0')) >= 9.0:
                        critical += 1
                except ValueError:
                    pass  # Skip non-numeric severity values
            if critical > 0:
                print(f"        Critical Threats: & {critical} \\\\")

        print("    \\end{tabular}")
        print("};")

    def print_summary(self):
        """Print complete analysis"""
        self.analyze_nodes()
        self.analyze_connections()
        self.analyze_threats()

def main():
    """Main statistics function"""
    if len(sys.argv) < 2:
        print("Usage: python3 network_stats.py <files...> [options]")
        print("")
        print("Examples:")
        print("  python3 network_stats.py nodes.csv connections.csv")
        print("  python3 network_stats.py nodes.csv connections.csv threats.csv")
        print("  python3 network_stats.py --all")
        print("  python3 network_stats.py --all --latex")
        print("")
        print("Options:")
        print("  --latex    Generate LaTeX code for statistics summary")
        sys.exit(1)

    stats = NetworkStats()
    generate_latex = '--latex' in sys.argv

    # Handle --all flag
    if '--all' in sys.argv:
        files_to_load = [
            ('nodes.csv', stats.load_nodes_csv),
            ('connections.csv', stats.load_connections_csv),
            ('threats.csv', stats.load_threats_csv),
        ]

        for filepath, load_func in files_to_load:
            if Path(filepath).exists():
                try:
                    load_func(filepath)
                    print(f"{GREEN}✓ Loaded: {filepath}{NC}")
                except Exception as e:
                    print(f"{YELLOW}⚠ Error loading {filepath}: {e}{NC}")
            else:
                print(f"{YELLOW}⚠ Skipping {filepath} (not found){NC}")
    else:
        # Load specified files
        for filepath in sys.argv[1:]:
            if filepath.startswith('--'):
                continue

            if not Path(filepath).exists():
                print(f"{RED}✗ File not found: {filepath}{NC}")
                continue

            try:
                if 'node' in filepath.lower():
                    stats.load_nodes_csv(filepath)
                    print(f"{GREEN}✓ Loaded nodes: {filepath}{NC}")
                elif 'connection' in filepath.lower():
                    stats.load_connections_csv(filepath)
                    print(f"{GREEN}✓ Loaded connections: {filepath}{NC}")
                elif 'threat' in filepath.lower():
                    stats.load_threats_csv(filepath)
                    print(f"{GREEN}✓ Loaded threats: {filepath}{NC}")
                else:
                    print(f"{YELLOW}⚠ Unknown file type, trying as nodes: {filepath}{NC}")
                    stats.load_nodes_csv(filepath)
            except Exception as e:
                print(f"{RED}✗ Error loading {filepath}: {e}{NC}")

    # Generate analysis
    stats.print_summary()

    if generate_latex:
        stats.generate_latex_summary()

    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{GREEN}✓ Analysis complete{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

if __name__ == '__main__':
    main()
