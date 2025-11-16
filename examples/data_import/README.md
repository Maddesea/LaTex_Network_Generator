# Data Import Examples

This directory contains examples demonstrating the **Agent 6: Data Import/Export** functionality.

## Overview

The `data_import.tex` module provides functionality to import network topology data from various formats:

- **CSV** - Simple, spreadsheet-compatible format
- **JSON** - Machine-readable structured data
- **YAML** - Human-readable configuration format
- **Nmap XML** - Network discovery scan results

## Files in This Directory

### Example Data Files

1. **nodes.csv** - Network device definitions
2. **connections.csv** - Network connections between devices
3. **threats.csv** - Security threats and vulnerabilities
4. **network.json** - Complete network definition in JSON format
5. **network.yaml** - Complete network definition in YAML format
6. **nmap-scan.xml** - Sample Nmap scan results

### Example LaTeX Files

1. **example_csv_import.tex** - Demonstrates CSV import functionality
2. **example_nmap_import.tex** - Demonstrates Nmap XML import functionality

## Usage

### CSV Import

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

## Future Enhancements

Coming soon:

- **Auto-layout** - Automatic node positioning from imported data
- **Subnet detection** - Automatic grouping by IP address ranges
- **Nessus integration** - Import vulnerability scan results
- **Database connectivity** - Query network data from SQL databases
- **REST API** - Generate diagrams via HTTP endpoints

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
