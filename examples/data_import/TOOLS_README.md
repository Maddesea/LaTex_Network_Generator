# Data Import Tools and Utilities

This directory includes powerful command-line tools to help you work with network diagram data.

## Available Tools

### 1. **compile_examples.sh** - Example Compilation Script

Automatically compiles all example LaTeX files in this directory.

**Usage:**
```bash
./compile_examples.sh
```

**Features:**
- Detects available LaTeX engines (pdflatex, lualatex)
- Compiles all examples automatically
- Shows success/failure status for each
- Cleans up auxiliary files
- Provides compilation summary

**Requirements:**
- pdflatex (for CSV and auto-positioning examples)
- lualatex (optional, for Nmap/Nessus/JSON/YAML examples)

---

### 2. **validate_data.py** - Data Validation Tool

Validates your CSV, JSON, and YAML files before importing them into LaTeX.

**Usage:**
```bash
# Validate a single file
python3 validate_data.py nodes.csv

# Validate multiple files
python3 validate_data.py nodes.csv connections.csv threats.csv

# Validate all CSV files in directory
python3 validate_data.py --all
```

**Checks:**
- ✓ Proper file format and headers
- ✓ Required fields present
- ✓ Valid IPv4 addresses (octet range 0-255)
- ✓ Unique node IDs (no duplicates)
- ✓ Valid node types (server, client, router, etc.)
- ✓ Valid connection types (normal, encrypted, attack, etc.)
- ✓ Connection endpoints exist
- ✓ CVSS severity scores in range
- ⚠ Warns about missing optional fields
- ⚠ Warns about isolated nodes

**Output:**
- Colored terminal output (red for errors, yellow for warnings, green for success)
- Line-by-line error reporting
- Summary statistics

**Example Output:**
```
Validating nodes CSV: nodes.csv
✓ CSV format: nodes with coordinates
✓ Processed 14 nodes

Validation Summary
✓ All checks passed!
✓ Data is ready to import
```

---

### 3. **generate_template.py** - Template Generator

Creates template CSV and JSON files with proper headers and example data.

**Usage:**
```bash
# Generate nodes template with coordinates
python3 generate_template.py nodes

# Generate nodes template for auto-positioning (no coordinates)
python3 generate_template.py nodes --auto-position

# Generate connections template
python3 generate_template.py connections

# Generate threats template
python3 generate_template.py threats

# Generate JSON template
python3 generate_template.py json

# Generate all templates
python3 generate_template.py --all
```

**Generated Files:**
- `nodes_template.csv` - Full template with x,y coordinates
- `nodes_template_auto.csv` - Simplified template for auto-positioning
- `connections_template.csv` - Connection definitions
- `threats_template.csv` - Threat/vulnerability data
- `network_template.json` - Complete JSON network structure

**Features:**
- Includes helpful example data
- Shows usage commands for each template
- Lists valid values for type fields
- Pre-filled with realistic network examples

**Workflow:**
1. Generate template: `python3 generate_template.py nodes`
2. Edit template with your data
3. Validate: `python3 validate_data.py nodes_template.csv`
4. Import into LaTeX

---

### 4. **network_stats.py** - Network Statistics and Analysis

Analyzes your network data and generates useful statistics.

**Usage:**
```bash
# Analyze specific files
python3 network_stats.py nodes.csv connections.csv

# Analyze all CSV files
python3 network_stats.py --all

# Generate LaTeX summary code
python3 network_stats.py --all --latex
```

**Statistics Generated:**

**Node Analysis:**
- Total node count
- Node type distribution (servers, clients, routers, etc.)
- IP address distribution by subnet
- Nodes without IP addresses

**Connection Analysis:**
- Total connection count
- Connection type distribution (normal, encrypted, attack, etc.)
- Most connected nodes (top 10)
- Isolated nodes (no connections)

**Threat Analysis:**
- Total threat count
- Threat type distribution
- Severity distribution (Critical/High/Medium/Low)
- Most vulnerable nodes

**Example Output:**
```
NODE STATISTICS
Total Nodes: 14

Node Types:
  attacker          1 (  7.1%)
  client            3 ( 21.4%)
  firewall          2 ( 14.3%)
  router            1 (  7.1%)
  server            6 ( 42.9%)
  switch            1 (  7.1%)

IP Address Distribution:
  192.168.1.0/24         3 nodes
  192.168.10.0/24        2 nodes
  192.168.100.0/24       4 nodes
  192.168.200.0/24       2 nodes
```

**LaTeX Output (--latex flag):**
Generates ready-to-use LaTeX code for embedding statistics in your diagram:

```latex
\node[draw=black!20, fill=white, rounded corners=3pt] {
    \tiny\bfseries Network Statistics \\[2pt]
    \begin{tabular}{lr}
        Total Nodes: & 14 \\
        Total Connections: & 16 \\
        Total Threats: & 3 \\
        Critical Threats: & 2 \\
    \end{tabular}
};
```

---

### 5. **convert_format.py** - Format Conversion Utility

Convert network data between different formats.

**Usage:**
```bash
# CSV to JSON
python3 convert_format.py nodes.csv --to json
python3 convert_format.py nodes.csv connections.csv threats.csv --to json

# JSON to CSV
python3 convert_format.py network.json --to csv

# Nmap XML to CSV
python3 convert_format.py nmap-scan.xml --to csv

# CSV to GraphML (for Gephi/Cytoscape)
python3 convert_format.py nodes.csv connections.csv --to graphml
```

**Supported Conversions:**

| From | To | Output Files |
|------|-----|--------------|
| CSV | JSON | network.json |
| JSON | CSV | nodes_from_json.csv, connections_from_json.csv, threats_from_json.csv |
| Nmap XML | CSV | nodes_from_nmap.csv |
| CSV | GraphML | network.graphml |

**Use Cases:**
- **CSV → JSON**: Prepare data for LuaTeX import
- **JSON → CSV**: Edit network data in spreadsheet
- **Nmap → CSV**: Process scan results in Excel
- **CSV → GraphML**: Analyze network in Gephi or Cytoscape

**Example:**
```bash
# Convert CSV files to JSON
$ python3 convert_format.py nodes.csv connections.csv --to json

Network Data Format Converter
✓ Converted to JSON: network.json
  Nodes: 14
  Connections: 16
  Threats: 0
```

---

## Workflow Examples

### Starting from Scratch

```bash
# 1. Generate template
python3 generate_template.py nodes

# 2. Edit nodes_template.csv in Excel/LibreOffice

# 3. Validate your data
python3 validate_data.py nodes_template.csv

# 4. Analyze your network
python3 network_stats.py nodes_template.csv

# 5. Rename to nodes.csv and import into LaTeX
mv nodes_template.csv nodes.csv
```

### Working with Nmap Scans

```bash
# 1. Run Nmap scan
nmap -sV -O 192.168.1.0/24 -oX nmap-scan.xml

# 2. Convert to CSV for editing
python3 convert_format.py nmap-scan.xml --to csv

# 3. Edit nodes_from_nmap.csv to add positions/labels

# 4. Validate
python3 validate_data.py nodes_from_nmap.csv

# 5. Import into LaTeX with auto-positioning
# \importNodesAutoPositioned{nodes_from_nmap.csv}
```

### Converting Between Formats

```bash
# CSV → JSON (for LuaTeX)
python3 convert_format.py nodes.csv connections.csv --to json

# JSON → CSV (for editing)
python3 convert_format.py network.json --to csv

# CSV → GraphML (for graph analysis)
python3 convert_format.py nodes.csv connections.csv --to graphml
```

### Complete Analysis Workflow

```bash
# 1. Validate all data files
python3 validate_data.py --all

# 2. Generate statistics
python3 network_stats.py --all

# 3. Generate LaTeX summary code
python3 network_stats.py --all --latex > network_stats.tex

# 4. Compile examples
./compile_examples.sh

# 5. Convert to other formats for external analysis
python3 convert_format.py nodes.csv connections.csv --to graphml
```

---

## Requirements

### Python Scripts
- **Python 3.6+**
- Standard library only (no external dependencies!)

### Shell Scripts
- **Bash 4.0+**
- LaTeX distribution with pdflatex
- LuaLaTeX (optional, for advanced features)

---

## Tips and Tricks

### Using with Git

Add to `.gitignore`:
```
*_template.csv
*_from_*.csv
*.log
*.aux
```

Keep in Git:
```
nodes.csv
connections.csv
threats.csv
*.tex
```

### Batch Processing

Process multiple networks:
```bash
for dir in network1 network2 network3; do
    cd $dir
    python3 ../validate_data.py --all
    python3 ../network_stats.py --all > stats.txt
    cd ..
done
```

### Automation

Create a Makefile:
```makefile
.PHONY: validate compile stats

validate:
	python3 validate_data.py --all

stats:
	python3 network_stats.py --all --latex > network_stats.tex

compile: validate
	./compile_examples.sh

all: validate stats compile
```

Then just run: `make all`

---

## Troubleshooting

**Problem:** Script says "command not found"
**Solution:** Make script executable: `chmod +x script_name.sh`

**Problem:** Python script fails with import error
**Solution:** Ensure Python 3.6+ is installed: `python3 --version`

**Problem:** Validation shows encoding errors
**Solution:** Save CSV files as UTF-8 in your editor

**Problem:** Generated templates won't open
**Solution:** Check file permissions and disk space

**Problem:** Stats show too many warnings
**Solution:** Review warnings and fix data issues, or ignore if intentional

---

## Contributing

Found a bug or have a feature request? Please check the main project README for contribution guidelines.

---

**These tools make Agent 6: Data Import/Export even more powerful!**
