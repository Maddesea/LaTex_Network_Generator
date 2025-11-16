# Data Import Examples

This directory contains examples demonstrating the **Agent 6: Data Import/Export** functionality.

## Overview

The `data_import.tex` module provides functionality to import network topology data from various formats:

- **CSV** - Simple, spreadsheet-compatible format (with auto-positioning support!)
- **JSON** - Machine-readable structured data
- **YAML** - Human-readable configuration format
- **Nmap XML** - Network discovery scan results
- **Nessus XML** - Vulnerability assessment reports (NEW!)
- **Auto-Positioning** - Automatic grid layout without manual coordinates (NEW!)
- **Subnet Detection** - Automatic grouping by IP address ranges (NEW!)

## Files in This Directory

### Example Data Files

1. **nodes.csv** - Network device definitions (with x,y coordinates)
2. **nodes-simple.csv** - Simplified format for auto-positioning (no coordinates!)
3. **connections.csv** - Network connections between devices
4. **threats.csv** - Security threats and vulnerabilities
5. **network.json** - Complete network definition in JSON format
6. **network.yaml** - Complete network definition in YAML format
7. **nmap-scan.xml** - Sample Nmap network discovery scan
8. **nessus-scan.nessus** - Sample Nessus vulnerability assessment (NEW!)

### Example LaTeX Files

1. **example_csv_import.tex** - Basic CSV import functionality
2. **example_nmap_import.tex** - Nmap network discovery import
3. **example_nessus_import.tex** - Nessus vulnerability scan import (NEW!)
4. **example_auto_positioning.tex** - Auto-positioning without coordinates (NEW!)
5. **example_advanced_integration.tex** - Mixing CSV + manual + analysis (NEW!)

## Usage

### 🆕 Auto-Positioning (No Coordinates Required!)

The easiest way to get started! Just specify node type and IP address:

**nodes-simple.csv format:**
```csv
id,type,ip,label
web1,server,192.168.10.10,Web Server
db1,server,192.168.20.10,Database
```

**In your LaTeX file:**
```latex
\input{data_import.tex}

\importNodesAutoPositioned{nodes-simple.csv}
```

Nodes are automatically arranged in a grid layout. Perfect for:
- Quick prototypes
- Rapid network documentation
- When exact positioning doesn't matter
- Large bulk imports

**Compile with:**
```bash
pdflatex example_auto_positioning.tex
```

### CSV Import (Traditional with Coordinates)

The CSV format is the simplest and most compatible with spreadsheet tools like Excel, Google Sheets, or LibreOffice Calc.

**nodes.csv format:**
```csv
id,type,ip,x,y,label
fw1,firewall,192.168.1.1,0,5,Edge Firewall
web1,server,192.168.10.10,-3,1,Web Server
```

**connections.csv format:**
```csv
source,destination,label,type
fw1,rtr1,,normal
web1,fw2,HTTPS,encrypted
```

**threats.csv format:**
```csv
target,type,severity,cve,description
web1,vulnerability,9.8,CVE-2024-1234,SQL Injection vulnerability
```

**In your LaTeX file:**
```latex
\input{data_import.tex}

% Import all network data from CSV files
\importNetworkFromCSV{nodes.csv}{connections.csv}{threats.csv}

% Or import individually
\importNodesFromCSV{nodes.csv}
\importConnectionsFromCSV{connections.csv}
\importThreatsFromCSV{threats.csv}
```

**Compile with:**
```bash
pdflatex example_csv_import.tex
```

### JSON Import

JSON format provides a structured, machine-readable format suitable for automated tools and APIs.

**Requires:** LuaLaTeX

**In your LaTeX file:**
```latex
\input{data_import.tex}

\importNetworkFromJSON{network.json}
```

**Compile with:**
```bash
lualatex your_document.tex
```

### YAML Import

YAML format is more human-readable than JSON and supports comments, making it ideal for manual editing.

**Requires:** LuaLaTeX

**In your LaTeX file:**
```latex
\input{data_import.tex}

\importNetworkFromYAML{network.yaml}
```

**Compile with:**
```bash
lualatex your_document.tex
```

### Nmap XML Import

Import network discovery data directly from Nmap scan results.

**Requires:** LuaLaTeX

**Generate Nmap scan:**
```bash
nmap -sV -O 192.168.1.0/24 -oX nmap-scan.xml
```

**In your LaTeX file:**
```latex
\input{data_import.tex}

\importNmapXML{nmap-scan.xml}
```

**Compile with:**
```bash
lualatex example_nmap_import.tex
```

### 🆕 Nessus Vulnerability Scan Import

Import vulnerability assessment data from Nessus scans to visualize security posture.

**Requires:** LuaLaTeX

**Export Nessus scan:**
1. In Nessus UI, go to Scans
2. Select your scan
3. Click "Export" and choose ".nessus" format (XML)

**In your LaTeX file:**
```latex
\input{data_import.tex}

\importNessusXML{nessus-scan.nessus}
```

**Features:**
- Extracts all discovered hosts with IP addresses
- Parses vulnerability severity levels
- Displays CVE IDs and CVSS scores
- Shows vulnerability counts: (C/H/M) format
- Auto-assigns threat badges (Critical/High/Medium)
- Creates risk-appropriate node styling

**Compile with:**
```bash
lualatex example_nessus_import.tex
```

**Perfect for:**
- Vulnerability assessment reports
- Security audit documentation
- Risk visualization dashboards
- Compliance reporting (PCI-DSS, HIPAA, etc.)

## Compiling the Examples

### Prerequisites

- **pdflatex** or **lualatex** (from TeX Live or MiKTeX)
- All module files from the parent directory

### CSV Example

```bash
cd examples/data_import
pdflatex example_csv_import.tex
```

### Nmap Example

```bash
cd examples/data_import
lualatex example_nmap_import.tex
```

## Supported Node Types

The CSV import supports the following node types:

- `server` - Generic server
- `client` - Client workstation
- `router` - Network router
- `firewall` - Firewall device
- `switch` - Network switch
- `attacker` - Threat actor

## Supported Connection Types

The CSV import supports the following connection types:

- `normal` - Standard connection
- `encrypted` - Encrypted connection (e.g., TLS, VPN)
- `attack` - Attack connection
- `suspicious` - Suspicious connection
- `bidirectional` - Two-way connection

## Tips and Best Practices

1. **Use absolute or relative paths** - Ensure CSV/JSON/YAML/XML files are accessible from your LaTeX document directory

2. **Validate your data** - Check that:
   - Node IDs are unique
   - Connection endpoints reference existing nodes
   - IP addresses are valid
   - Coordinates don't cause overlapping nodes

3. **Start simple** - Begin with a small dataset and gradually add more nodes

4. **Use spreadsheets for CSV** - Excel or Google Sheets can help manage large node lists

5. **Version control** - Keep your data files in version control alongside your LaTeX files

6. **Combine approaches** - Use CSV for bulk data and manual LaTeX commands for fine-tuning

## Advanced Features

### Subnet Auto-Detection (LuaTeX)

Automatically group nodes by IP subnet and generate security zones:

```latex
% After importing nodes
\autoGenerateSubnetZones
```

This command:
- Analyzes all imported node IP addresses
- Groups nodes by /24 subnets
- Automatically creates security zone boundaries
- Color-codes based on private/public IP ranges
- Labels zones with subnet CIDR notation

### Hybrid Manual + Import Workflow

Mix imported data with manual commands for maximum flexibility:

```latex
% Import bulk nodes from CSV
\importNodesFromCSV{nodes.csv}

% Add special nodes manually
\createAttacker{hacker}{1.2.3.4}{-8}{8}{APT Group}

% Import connections
\importConnectionsFromCSV{connections.csv}

% Add attack overlays
\drawAttackConnection{hacker}{fw1}{Port Scan}
```

See `example_advanced_integration.tex` for a complete example.

## New in Version 1.1

✅ **Auto-positioning algorithm** - No more manual coordinates!
✅ **Nessus scan integration** - Vulnerability assessment imports
✅ **IP subnet detection** - Automatic network segmentation
✅ **Enhanced validation** - IPv4 format checking
✅ **Connection inference** - Smart topology suggestions from port data

## Future Enhancements

Coming in future versions:

- **Database connectivity** - Query network data from SQL databases
- **REST API** - Generate diagrams via HTTP endpoints
- **Force-directed layout** - Organic auto-positioning based on connections
- **Enhanced JSON/YAML** - Full library support (lunajson/lyaml)
- **SIEM integration** - Import from Splunk, ELK, etc.

## Troubleshooting

### "File not found" errors

- Ensure file paths are correct (relative to the .tex file)
- Use forward slashes (/) even on Windows
- Check file permissions

### "Package luatex required" warnings

- Install LuaLaTeX if not available
- For CSV import, pdflatex is sufficient
- JSON/YAML/Nmap require lualatex

### Nodes overlap

- Adjust x,y coordinates in CSV/JSON/YAML files
- Use auto-layout features (coming soon)
- Increase spacing between nodes

### Missing connections

- Verify source and destination node IDs exist
- Check for typos in node references
- Ensure CSV format is correct (comma-separated)

## Getting Help

- Check the main README.md for general usage
- See ARCHITECTURE.md for system design details
- Review QUICK_REFERENCE.md for command syntax
- Open an issue on GitHub for bugs or feature requests

## Contributing

Found a bug or have an enhancement idea?

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

**Agent 6: Data Import/Export**
High Priority: ✅ JSON, YAML, CSV, Nmap XML parsers implemented
Medium Priority: 🔄 Nessus, GraphML export (coming soon)
Low Priority: 📋 SIEM integration, database connectivity (planned)
