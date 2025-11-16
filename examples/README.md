# Data Import Examples

This directory contains example data files demonstrating the various import formats supported by the Network Diagram Generator.

## Available Formats

### 1. JSON Format

**File:** `example_network.json`

**Usage:**
```latex
\importJSON{examples/example_network.json}
```

**Features:**
- Comprehensive network topology definition
- Nodes with type, IP, position, and labels
- Connections with various types (normal, encrypted, attack, etc.)
- Threat indicators with CVE scores

### 2. YAML Format

**File:** `example_network.yaml`

**Usage:**
```latex
\importYAML{examples/example_network.yaml}
```

**Features:**
- Human-readable alternative to JSON
- Supports comments
- Same structure as JSON but more readable
- Ideal for version-controlled network documentation

### 3. CSV Format

**Files:**
- `nodes.csv` - Network nodes/devices
- `connections.csv` - Network connections
- `threats.csv` - Security threats and vulnerabilities

**Usage:**
```latex
\renewcommand{\renderNetworkNodes}{
    \importNodesFromCSV{examples/nodes.csv}
}

\renewcommand{\renderConnections}{
    \importConnectionsFromCSV{examples/connections.csv}
}

\renewcommand{\renderThreats}{
    \importThreatsFromCSV{examples/threats.csv}
}
```

**CSV Schemas:**

**nodes.csv:**
```
id,type,ip,x,y,label
```
- **id:** Unique identifier for the node
- **type:** firewall, router, switch, server, client, cloud
- **ip:** IP address
- **x, y:** Position coordinates
- **label:** Display name

**connections.csv:**
```
source,dest,type,label
```
- **source:** Source node ID
- **dest:** Destination node ID
- **type:** normal, encrypted, attack, suspicious, bidirectional
- **label:** Optional label for the connection

**threats.csv:**
```
target,type,severity,cve,description
```
- **target:** Target node ID
- **type:** vulnerability, malware
- **severity:** CVSS score (0-10)
- **cve:** CVE identifier (if applicable)
- **description:** Threat description

### 4. Nmap XML Format

**File:** `example_nmap.xml`

**Usage:**
```latex
\importNmapXML{examples/example_nmap.xml}
```

**Features:**
- Automatically imports network discovery results
- Extracts: hosts, open ports, services, OS detection
- Auto-generates node positions in grid layout
- Creates server nodes with detected services

**How to generate Nmap XML:**
```bash
# Scan network and save to XML
nmap -sV -O 192.168.1.0/24 -oX scan_results.xml

# Import into your diagram
\importNmapXML{scan_results.xml}
```

## Complete Example

Here's a complete LaTeX document using JSON import:

```latex
\documentclass[tikz,border=10pt]{standalone}

\usepackage{tikz}
\usepackage{ifthen}
\usepackage{xcolor}
\usepackage{calc}

\usetikzlibrary{
    positioning,
    shapes.geometric,
    shapes.multipart,
    arrows.meta,
    decorations.pathmorphing,
    decorations.markings,
    backgrounds,
    fit,
    calc,
    shadows.blur,
    patterns,
    fadings
}

\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{threat_indicators}
\input{data_import}

\begin{document}
    % Import network topology from JSON
    \importJSON{examples/example_network.json}

    \begin{tikzpicture}[scale=1.0, transform shape, font=\sffamily]
        % Render imported network
        \renderNetworkNodes
        \renderConnections
        \renderThreats
    \end{tikzpicture}
\end{document}
```

## Compilation

**Important:** The data import module requires **LuaLaTeX** for JSON, YAML, and Nmap XML parsing.

```bash
# Compile with LuaLaTeX
lualatex network_diagram_generator.tex

# Or use the compile script
./compile.sh
```

## Creating Your Own Data Files

### JSON Template

```json
{
  "nodes": [
    {
      "id": "unique_id",
      "type": "server|firewall|router|switch|client|cloud",
      "ip": "192.168.1.1",
      "x": 0,
      "y": 0,
      "label": "Display Name",
      "ports": [80, 443]
    }
  ],
  "connections": [
    {
      "source": "source_node_id",
      "dest": "dest_node_id",
      "type": "normal|encrypted|attack|suspicious|bidirectional",
      "label": "Optional Label"
    }
  ],
  "threats": [
    {
      "target": "node_id",
      "type": "vulnerability|malware",
      "cve": "CVE-2024-1234",
      "severity": 9.8,
      "description": "Description"
    }
  ]
}
```

### YAML Template

```yaml
nodes:
  - id: unique_id
    type: server
    ip: 192.168.1.1
    x: 0
    y: 0
    label: Display Name
    ports: [80, 443]

connections:
  - source: source_node_id
    dest: dest_node_id
    type: normal
    label: Optional Label

threats:
  - target: node_id
    type: vulnerability
    cve: CVE-2024-1234
    severity: 9.8
    description: Description
```

## Tips

1. **Positioning:** Use a consistent grid for x and y coordinates (e.g., increment by 2 or 3)
2. **Node IDs:** Use descriptive IDs like `fw1`, `web_server1`, `db_primary`
3. **IP Addresses:** Use realistic IP ranges for different zones
4. **Labels:** Keep labels concise for better readability
5. **Types:** Choose appropriate node types for accurate visualization

## Validation

To validate your JSON files before importing:

```latex
\validateJSONFile{examples/my_network.json}
```

This will check for syntax errors and report any issues.

## Utility Scripts

### Network Data Converter (Python)

**File:** `convert_network_data.py`

A Python script to convert between different network data formats. Supports:
- Nmap XML → JSON/YAML/CSV
- Nessus XML → JSON/YAML/CSV
- JSON ↔ YAML ↔ CSV

**Usage:**
```bash
# Convert Nmap scan to JSON
python convert_network_data.py nmap_scan.xml network.json

# Convert JSON to YAML
python convert_network_data.py network.json network.yaml

# Convert Nessus scan to JSON
python convert_network_data.py scan_results.nessus network.json

# Convert JSON to CSV (creates nodes.csv and connections.csv)
python convert_network_data.py network.json nodes.csv
```

**Requirements:**
```bash
# Optional: for YAML support
pip install pyyaml
```

**Features:**
- Automatic connection generation for imported scans
- Preserves all network metadata
- Handles vulnerability data from Nessus
- Batch conversion support

### Nessus Integration

**File:** `example_nessus.nessus`

Example Nessus vulnerability scan results showing:
- Critical vulnerabilities (CVSS 9.0+)
- High severity issues (CVSS 7.0-8.9)
- Medium severity issues (CVSS 4.0-6.9)
- CVE identifiers and descriptions

**Usage in LaTeX:**
```latex
\importNessusXML{examples/example_nessus.nessus}
```

This will automatically:
- Create nodes for all vulnerable hosts
- Mark vulnerabilities with CVSS scores >= 7.0
- Add threat badges (critical, high, medium, low)
- Position nodes in grid layout

## Demonstration Files

### JSON Import Demo

**File:** `json_import_demo.tex`

A complete working example demonstrating JSON import:

```bash
# Compile with LuaLaTeX
cd examples/
lualatex json_import_demo.tex
```

This demo:
- Imports network topology from `example_network.json`
- Automatically renders all nodes and connections
- Adds legend and metadata
- Produces a complete network diagram

## Advanced Features

### Export to Other Tools

Export your network diagrams to work with other visualization tools:

```latex
% Export to Gephi/Cytoscape (GraphML)
\importJSON{examples/example_network.json}
\exportToGraphML{output.graphml}{examples/example_network.json}

% Export to GraphViz (DOT)
\exportToDOT{output.dot}{examples/example_network.json}
```

Then visualize with:
```bash
# GraphViz
dot -Tpng output.dot -o network.png

# Or open in Gephi/Cytoscape for interactive exploration
```

### Batch Processing

Process multiple network scans:

```bash
#!/bin/bash
# Convert all Nmap scans to JSON
for scan in scans/*.xml; do
    python convert_network_data.py "$scan" "json/${scan%.xml}.json"
done

# Generate diagrams from all JSON files
for json in json/*.json; do
    basename=$(basename "$json" .json)
    lualatex -jobname="$basename" "\input{json_import_demo.tex}"
done
```

### Combining Multiple Data Sources

Merge data from different sources:

```latex
\renewcommand{\renderNetworkNodes}{
    % Load base topology from Nmap
    \loadJSONNodes{nmap_data.json}

    % Add manual nodes
    \createFirewall{fw1}{192.168.1.1}{0}{8}{Main Firewall}
}

\renewcommand{\renderConnections}{
    % Load connections from CSV
    \importConnectionsFromCSV{examples/connections.csv}
}

\renewcommand{\renderThreats}{
    % Load vulnerabilities from CSV
    \importThreatsFromCSV{examples/threats.csv}
}
```

## Troubleshooting

**Issue:** "JSON file not found"
- **Solution:** Check the file path is correct relative to your main .tex file
- **Solution:** Use absolute paths if necessary

**Issue:** "Failed to parse JSON"
- **Solution:** Validate JSON syntax using online tools like JSONLint
- **Solution:** Check for trailing commas, which are not valid in JSON

**Issue:** "Nodes not rendering"
- **Solution:** Ensure node IDs are unique
- **Solution:** Check that x,y coordinates are within reasonable ranges
- **Solution:** Verify node types are valid (server, firewall, router, etc.)

**Issue:** "Compilation errors with CSV"
- **Solution:** Ensure CSV files have proper headers
- **Solution:** Check for extra spaces or special characters
- **Solution:** Make sure all required columns are present

## Next Steps

1. Try compiling the example files to see the results
2. Modify the examples to match your network
3. Create your own data files from scratch
4. Integrate with network scanning tools (Nmap, Nessus)
5. Automate diagram generation from live network data

For more information, see the main [README.md](../README.md) and [ARCHITECTURE.md](../ARCHITECTURE.md).
