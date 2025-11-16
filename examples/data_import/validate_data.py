#!/usr/bin/env python3
"""
validate_data.py - Data validation tool for network diagram imports

This script validates CSV, JSON, and YAML files before importing them
into the network diagram generator. It checks for:
- Proper file format
- Required fields
- Valid IP addresses
- Unique node IDs
- Valid connection endpoints
- Data consistency

Usage:
    python3 validate_data.py nodes.csv
    python3 validate_data.py network.json
    python3 validate_data.py --all
"""

import sys
import csv
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set

# ANSI color codes
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

class NetworkDataValidator:
    """Validates network diagram data files"""

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.node_ids = set()

    def validate_ipv4(self, ip: str) -> bool:
        """Validate IPv4 address format"""
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
        match = re.match(pattern, ip)
        if not match:
            return False

        # Check each octet is in range 0-255
        for octet in match.groups():
            if int(octet) > 255:
                return False

        return True

    def validate_node_type(self, node_type: str) -> bool:
        """Validate node type"""
        valid_types = [
            'server', 'client', 'router', 'firewall',
            'switch', 'cloud', 'attacker'
        ]
        return node_type.lower() in valid_types

    def validate_connection_type(self, conn_type: str) -> bool:
        """Validate connection type"""
        if not conn_type:  # Empty is OK (defaults to normal)
            return True
        valid_types = [
            'normal', 'encrypted', 'attack',
            'suspicious', 'bidirectional'
        ]
        return conn_type.lower() in valid_types

    def validate_nodes_csv(self, filepath: str) -> bool:
        """Validate nodes CSV file"""
        print(f"\n{BLUE}Validating nodes CSV: {filepath}{NC}")

        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)

                # Check required headers
                required_headers = ['id', 'type', 'ip', 'label']
                optional_headers = ['x', 'y']

                if not reader.fieldnames:
                    self.errors.append("No headers found in CSV file")
                    return False

                # Check for required headers
                missing_headers = set(required_headers) - set(reader.fieldnames)
                if missing_headers:
                    self.errors.append(f"Missing required headers: {missing_headers}")
                    return False

                # Determine if coordinates are provided
                has_coordinates = 'x' in reader.fieldnames and 'y' in reader.fieldnames

                if has_coordinates:
                    print(f"{GREEN}✓ CSV format: nodes with coordinates{NC}")
                else:
                    print(f"{YELLOW}⚠ CSV format: nodes without coordinates (use \\importNodesAutoPositioned){NC}")

                # Validate each row
                line_num = 2  # Start at 2 (header is line 1)
                for row in reader:
                    # Check node ID
                    node_id = row.get('id', '').strip()
                    if not node_id:
                        self.errors.append(f"Line {line_num}: Empty node ID")
                    elif node_id in self.node_ids:
                        self.errors.append(f"Line {line_num}: Duplicate node ID '{node_id}'")
                    else:
                        self.node_ids.add(node_id)

                    # Check node type
                    node_type = row.get('type', '').strip()
                    if not self.validate_node_type(node_type):
                        self.errors.append(
                            f"Line {line_num}: Invalid node type '{node_type}'"
                        )

                    # Check IP address
                    ip = row.get('ip', '').strip()
                    if ip and not self.validate_ipv4(ip):
                        self.errors.append(
                            f"Line {line_num}: Invalid IP address '{ip}'"
                        )

                    # Check coordinates if present
                    if has_coordinates:
                        try:
                            x = float(row.get('x', 0))
                            y = float(row.get('y', 0))
                        except ValueError as e:
                            self.errors.append(
                                f"Line {line_num}: Invalid coordinates (x={row.get('x')}, y={row.get('y')})"
                            )

                    # Check label
                    label = row.get('label', '').strip()
                    if not label:
                        self.warnings.append(
                            f"Line {line_num}: Empty label for node '{node_id}'"
                        )

                    line_num += 1

                print(f"{GREEN}✓ Processed {line_num - 2} nodes{NC}")
                return len(self.errors) == 0

        except FileNotFoundError:
            self.errors.append(f"File not found: {filepath}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading CSV: {str(e)}")
            return False

    def validate_connections_csv(self, filepath: str) -> bool:
        """Validate connections CSV file"""
        print(f"\n{BLUE}Validating connections CSV: {filepath}{NC}")

        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)

                # Check required headers
                required_headers = ['source', 'destination']
                optional_headers = ['label', 'type']

                if not reader.fieldnames:
                    self.errors.append("No headers found in CSV file")
                    return False

                # Check for required headers
                missing_headers = set(required_headers) - set(reader.fieldnames)
                if missing_headers:
                    self.errors.append(f"Missing required headers: {missing_headers}")
                    return False

                # Validate each row
                line_num = 2
                connection_count = 0
                for row in reader:
                    source = row.get('source', '').strip()
                    destination = row.get('destination', '').strip()

                    # Check source and destination
                    if not source:
                        self.errors.append(f"Line {line_num}: Empty source")
                    if not destination:
                        self.errors.append(f"Line {line_num}: Empty destination")

                    # Warn if nodes not found (only if nodes were validated first)
                    if self.node_ids:
                        if source and source not in self.node_ids:
                            self.warnings.append(
                                f"Line {line_num}: Source node '{source}' not found in nodes file"
                            )
                        if destination and destination not in self.node_ids:
                            self.warnings.append(
                                f"Line {line_num}: Destination node '{destination}' not found in nodes file"
                            )

                    # Check connection type
                    conn_type = row.get('type', '').strip()
                    if conn_type and not self.validate_connection_type(conn_type):
                        self.errors.append(
                            f"Line {line_num}: Invalid connection type '{conn_type}'"
                        )

                    line_num += 1
                    connection_count += 1

                print(f"{GREEN}✓ Processed {connection_count} connections{NC}")
                return len(self.errors) == 0

        except FileNotFoundError:
            self.errors.append(f"File not found: {filepath}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading CSV: {str(e)}")
            return False

    def validate_threats_csv(self, filepath: str) -> bool:
        """Validate threats CSV file"""
        print(f"\n{BLUE}Validating threats CSV: {filepath}{NC}")

        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)

                # Check required headers
                required_headers = ['target', 'type', 'severity']

                if not reader.fieldnames:
                    self.errors.append("No headers found in CSV file")
                    return False

                # Check for required headers
                missing_headers = set(required_headers) - set(reader.fieldnames)
                if missing_headers:
                    self.errors.append(f"Missing required headers: {missing_headers}")
                    return False

                # Validate each row
                line_num = 2
                threat_count = 0
                for row in reader:
                    target = row.get('target', '').strip()

                    # Check target exists
                    if not target:
                        self.errors.append(f"Line {line_num}: Empty target")
                    elif self.node_ids and target not in self.node_ids:
                        self.warnings.append(
                            f"Line {line_num}: Target node '{target}' not found in nodes file"
                        )

                    # Check severity (if it's a number, should be 0-10)
                    severity = row.get('severity', '').strip()
                    try:
                        sev_val = float(severity)
                        if sev_val < 0 or sev_val > 10:
                            self.warnings.append(
                                f"Line {line_num}: Severity {sev_val} outside typical CVSS range (0-10)"
                            )
                    except ValueError:
                        pass  # Non-numeric severity is OK

                    line_num += 1
                    threat_count += 1

                print(f"{GREEN}✓ Processed {threat_count} threats{NC}")
                return len(self.errors) == 0

        except FileNotFoundError:
            self.errors.append(f"File not found: {filepath}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading CSV: {str(e)}")
            return False

    def validate_json(self, filepath: str) -> bool:
        """Validate JSON network file"""
        print(f"\n{BLUE}Validating JSON: {filepath}{NC}")

        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            # Check basic structure
            if 'nodes' in data or 'network' in data:
                print(f"{GREEN}✓ Valid JSON structure{NC}")
            else:
                self.warnings.append("JSON file missing 'nodes' or 'network' key")

            # TODO: Add more detailed JSON validation

            return len(self.errors) == 0

        except FileNotFoundError:
            self.errors.append(f"File not found: {filepath}")
            return False
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {str(e)}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading JSON: {str(e)}")
            return False

    def print_summary(self):
        """Print validation summary"""
        print(f"\n{BLUE}{'='*50}{NC}")
        print(f"{BLUE}Validation Summary{NC}")
        print(f"{BLUE}{'='*50}{NC}")

        if self.errors:
            print(f"\n{RED}Errors: {len(self.errors)}{NC}")
            for error in self.errors:
                print(f"{RED}  ✗ {error}{NC}")

        if self.warnings:
            print(f"\n{YELLOW}Warnings: {len(self.warnings)}{NC}")
            for warning in self.warnings:
                print(f"{YELLOW}  ⚠ {warning}{NC}")

        if not self.errors and not self.warnings:
            print(f"\n{GREEN}✓ All checks passed!{NC}")
            print(f"{GREEN}✓ Data is ready to import{NC}")
        elif not self.errors:
            print(f"\n{GREEN}✓ No errors found (warnings can be ignored){NC}")
            print(f"{GREEN}✓ Data should import successfully{NC}")
        else:
            print(f"\n{RED}✗ Validation failed{NC}")
            print(f"{RED}✗ Please fix errors before importing{NC}")

def main():
    """Main validation function"""
    if len(sys.argv) < 2:
        print("Usage: python3 validate_data.py <file> [additional_files...]")
        print("       python3 validate_data.py --all")
        print("")
        print("Examples:")
        print("  python3 validate_data.py nodes.csv")
        print("  python3 validate_data.py nodes.csv connections.csv threats.csv")
        print("  python3 validate_data.py network.json")
        print("  python3 validate_data.py --all  # Validate all CSV files")
        sys.exit(1)

    validator = NetworkDataValidator()

    # Handle --all flag
    if sys.argv[1] == '--all':
        files_to_validate = [
            ('nodes.csv', validator.validate_nodes_csv),
            ('connections.csv', validator.validate_connections_csv),
            ('threats.csv', validator.validate_threats_csv),
        ]

        print(f"{BLUE}{'='*50}{NC}")
        print(f"{BLUE}Validating all CSV files{NC}")
        print(f"{BLUE}{'='*50}{NC}")

        all_valid = True
        for filepath, validate_func in files_to_validate:
            if Path(filepath).exists():
                if not validate_func(filepath):
                    all_valid = False
            else:
                print(f"{YELLOW}⚠ Skipping {filepath} (not found){NC}")

        validator.print_summary()
        sys.exit(0 if all_valid else 1)

    # Validate individual files
    all_valid = True
    for filepath in sys.argv[1:]:
        path = Path(filepath)

        if not path.exists():
            print(f"{RED}✗ File not found: {filepath}{NC}")
            all_valid = False
            continue

        # Determine file type and validate
        if filepath.endswith('.csv'):
            if 'node' in filepath.lower():
                if not validator.validate_nodes_csv(filepath):
                    all_valid = False
            elif 'connection' in filepath.lower():
                if not validator.validate_connections_csv(filepath):
                    all_valid = False
            elif 'threat' in filepath.lower():
                if not validator.validate_threats_csv(filepath):
                    all_valid = False
            else:
                # Try to auto-detect based on headers
                print(f"{YELLOW}⚠ Could not auto-detect CSV type, trying nodes format{NC}")
                if not validator.validate_nodes_csv(filepath):
                    all_valid = False

        elif filepath.endswith('.json'):
            if not validator.validate_json(filepath):
                all_valid = False
        else:
            print(f"{YELLOW}⚠ Unknown file type: {filepath}{NC}")

    validator.print_summary()
    sys.exit(0 if all_valid else 1)

if __name__ == '__main__':
    main()
