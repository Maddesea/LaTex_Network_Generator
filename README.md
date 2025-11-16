# LaTeX Network Diagram Generator

A professional, scalable network diagram generation system using LaTeX/TikZ, designed for cybersecurity visualization, network documentation, and threat analysis.

## Features

✅ **Professional Styling** - Publication-quality diagrams exceeding draw.io/Visio standards
✅ **Modular Architecture** - Separated concerns for parallel development
✅ **Scalable Output** - Support for A0 through A4 and custom page sizes
✅ **Threat Visualization** - Built-in security threat and attack indicators
✅ **Multiple Layout Algorithms** - Tiered, circular, grid, and force-directed options
✅ **Rich Connection Types** - Encrypted, suspicious, attack, and bidirectional connections
✅ **Security Zones** - Visual subnet and security boundary representations
✅ **Data Import/Export** - JSON, YAML, CSV, and Nmap XML support (NEW!)
✅ **TeXLive 2024/2025 Compatible** - Uses stable, widely-supported packages

## Quick Start

### Prerequisites

```bash
# Install TeXLive (Ubuntu/Debian)
sudo apt-get install texlive-full

# Or install TeXLive (Fedora/RHEL)
sudo dnf install texlive-scheme-full

# Verify installation
pdflatex --version
```

### Compile Example Diagram

```bash
pdflatex network_diagram_generator.tex
```

This generates `network_diagram_generator.pdf` with the example network.

## File Structure

```
network_diagram_generator.tex  # Main entry point
├── styles_config.tex          # Visual styling and color schemes
├── node_definitions.tex       # Network asset rendering
├── network_layout.tex         # Layout algorithms and positioning
├── connection_renderer.tex    # Connection drawing and flows
├── threat_indicators.tex      # Security threat visualization
├── data_import.tex            # Data import/export system (NEW!)
├── network_data.tex           # Actual network topology data
└── examples/                  # Example data files (NEW!)
    ├── example_network.json   # JSON format example
    ├── example_network.yaml   # YAML format example
    ├── nodes.csv              # CSV nodes example
    ├── connections.csv        # CSV connections example
    ├── threats.csv            # CSV threats example
    ├── example_nmap.xml       # Nmap XML example
    └── README.md              # Examples documentation
```

## Creating Your Own Diagrams

### 1. Basic Network

Edit `network_data.tex` and replace the `renderNetworkNodes` section:

```latex
\renewcommand{\renderNetworkNodes}{
    % Create your nodes
    \createServer{srv1}{192.168.1.10}{0}{0}{Web Server}
    \createClient{pc1}{192.168.1.100}{-5}{-3}{Workstation}
    \createFirewall{fw1}{192.168.1.1}{0}{3}{Firewall}
}
```

### 2. Add Connections

```latex
\renewcommand{\renderConnections}{
    \drawConnection{fw1}{srv1}{HTTP}
    \drawBidirectional{srv1}{pc1}{HTTPS}
}
```

### 3. Add Threat Indicators

```latex
\renewcommand{\renderThreats}{
    \markVulnerability{srv1}{CVE-2024-1234}{9.8}
    \drawAttackConnection{attacker1}{srv1}{SQL Injection}
}
```

### 4. Set Page Size

In `network_diagram_generator.tex`:

```latex
\renewcommand{\pageSize}{a3}  % Options: a4, a3, a2, a1, a0, letter
\setPageSize{\pageSize}
```

## Available Node Types

| Command | Description | Example |
|---------|-------------|---------|
| `\createServer` | Server/host | `\createServer{srv1}{192.168.1.10}{0}{0}{Web Server}` |
| `\createClient` | Workstation/client | `\createClient{pc1}{192.168.1.100}{-5}{-3}{Desktop}` |
| `\createRouter` | Network router | `\createRouter{r1}{192.168.1.1}{0}{5}{Core Router}` |
| `\createFirewall` | Firewall | `\createFirewall{fw1}{10.0.0.1}{0}{3}{Edge FW}` |
| `\createSwitch` | Network switch | `\createSwitch{sw1}{192.168.1.2}{-3}{-3}{Access SW}` |
| `\createCloud` | Cloud/Internet | `\createCloud{inet}{0}{8}{Internet}` |
| `\createAttacker` | Threat actor | `\createAttacker{bad1}{1.2.3.4}{-6}{8}{Attacker}` |

## Available Connection Types

| Command | Description | Visual Style |
|---------|-------------|--------------|
| `\drawConnection` | Normal connection | Solid line with arrow |
| `\drawEncryptedConnection` | Encrypted/VPN | Green with dots |
| `\drawSuspiciousConnection` | Suspicious traffic | Orange dashed |
| `\drawAttackConnection` | Active attack | Red thick line |
| `\drawBidirectional` | Two-way traffic | Arrows on both ends |

## Threat Visualization

```latex
% Mark vulnerability
\markVulnerability{node_name}{CVE-2024-1234}{9.8}

% Show DDoS attack
\visualizeDDoS{attacker1,attacker2,attacker3}{target_server}{critical}

% Show SQL injection
\visualizeSQLi{attacker}{database_server}

% Mark compromised node
\visualizeMalware{node_name}{Ransomware}

% Show data exfiltration
\visualizeExfiltration{source_node}{attacker_node}{500MB}
```

## Security Zones

```latex
% Draw subnet boundary
\drawSubnet{dmz}{routerOrange}{(node1) (node2) (node3)}{DMZ Network}

% Draw security zone with trust level
\drawSecurityZone{internal}{clientGreen}
    {(node1) (node2)}
    {Internal Network}
    {High Trust}
```

## Advanced Features

### Custom Colors

Edit `styles_config.tex`:

```latex
\definecolor{myCustomBlue}{RGB}{30, 144, 255}
```

### Multi-Part Nodes with Ports

```latex
\createServerWithPorts{web1}{192.168.1.10}{0}{0}{Web Server}{80,443,8080}
```

### Curved Connections

```latex
\drawCurvedConnection{node1}{node2}{30}{Label}  % 30 degree bend
```

## Data Import/Export (NEW!)

The system now supports importing network topologies from multiple data formats, eliminating the need to manually code network diagrams.

### Supported Import Formats

#### 1. JSON Import

**Requires:** LuaLaTeX

Import complete network topologies from JSON files:

```latex
% In your main .tex file
\importJSON{examples/example_network.json}
```

**JSON Schema:**
```json
{
  "nodes": [
    {
      "id": "node1",
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
      "source": "node1",
      "dest": "node2",
      "type": "normal|encrypted|attack|suspicious|bidirectional",
      "label": "Optional Label"
    }
  ],
  "threats": [
    {
      "target": "node1",
      "type": "vulnerability|malware",
      "cve": "CVE-2024-1234",
      "severity": 9.8
    }
  ]
}
```

#### 2. YAML Import

**Requires:** LuaLaTeX

Human-readable alternative to JSON with comment support:

```latex
\importYAML{examples/example_network.yaml}
```

#### 3. CSV Bulk Import

Import network data from CSV spreadsheets:

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
- `nodes.csv`: `id,type,ip,x,y,label`
- `connections.csv`: `source,dest,type,label`
- `threats.csv`: `target,type,severity,cve,description`

#### 4. Nmap XML Parser

**Requires:** LuaLaTeX

Automatically import network discovery results from Nmap scans:

```latex
\importNmapXML{scan_results.xml}
```

**Generate Nmap XML:**
```bash
nmap -sV -O 192.168.1.0/24 -oX scan_results.xml
```

This will automatically:
- Create nodes for discovered hosts
- Add open port information
- Use hostnames as labels
- Arrange nodes in a grid layout

#### 5. Nessus XML Parser

**Requires:** LuaLaTeX

Import vulnerability scan results from Nessus:

```latex
\importNessusXML{scan_results.nessus}
```

This will automatically:
- Create nodes for vulnerable hosts
- Mark critical vulnerabilities (CVSS >= 7.0)
- Add threat badges based on severity
- Include CVE identifiers

### Export Formats

Export your network diagrams to other tools:

```latex
% Export to GraphML (for Gephi, Cytoscape)
\exportToGraphML{output.graphml}{network_data}

% Export to DOT format (for GraphViz)
\exportToDOT{output.dot}{network_data}
```

### Compilation for Data Import

**Important:** JSON, YAML, and Nmap XML parsing require LuaLaTeX:

```bash
# Compile with LuaLaTeX
lualatex network_diagram_generator.tex

# Or update compile.sh to use lualatex
./compile.sh
```

### Example Files

See the `examples/` directory for complete working examples:
- `example_network.json` - JSON format example
- `example_network.yaml` - YAML format example
- `nodes.csv`, `connections.csv`, `threats.csv` - CSV format examples
- `example_nmap.xml` - Nmap XML format example
- `example_nessus.nessus` - Nessus vulnerability scan example
- `json_import_demo.tex` - Complete demo using JSON import
- `convert_network_data.py` - Python conversion utility
- `README.md` - Detailed usage guide

### Automation Tools

**Shell Scripts:**
- `network_diagram_tool.sh` - Automation suite for common workflows (NEW!)
- `quickstart.sh` - Project template generator (NEW!)

**Usage:**
```bash
# Auto-generate diagram from Nmap scan
./network_diagram_tool.sh nmap scan.xml my_network

# Generate vulnerability report from Nessus
./network_diagram_tool.sh nessus scan.nessus vuln_report

# Batch process all scans in a directory
./network_diagram_tool.sh batch ./scans ./output

# Create a new project from template
./quickstart.sh
```

### Advanced Features (NEW!)

**Data Filtering:**
```latex
% Filter by subnet
\filterNodesBySubnet{192.168.1}{network.json}

% Filter by type
\filterNodesByType{server}{network.json}

% Show only critical vulnerabilities
\filterVulnerabilitiesByCVSS{7.0}{threats.json}

% Exclude certain types
\excludeNodesByType{client}{network.json}
```

**Data Transformation:**
```latex
% Auto-layout by subnet grouping
\autoLayoutBySubnet{network.json}

% Scale node positions
\scaleNodePositions{1.5}{network.json}

% Merge multiple data sources
\mergeNetworkData{network1.json}{network2.json}
```

See [WORKFLOWS.md](WORKFLOWS.md) for complete real-world usage examples.

## Parallel Development Guide

This system is designed for **multiple agents/developers** to work simultaneously on different components:

### Agent 1: Styles & Aesthetics (`styles_config.tex`)
**Priority TODOs:**
- [ ] Custom color scheme support via config file
- [ ] Colorblind-friendly alternative palettes
- [ ] Dark mode theme support
- [ ] Gradient fills for premium look
- [ ] Icon/image support inside nodes
- [ ] Badge/label support for OS type and status

### Agent 2: Node System (`node_definitions.tex`)
**Priority TODOs:**
- [ ] Hash map for O(1) node lookup by IP
- [ ] Node grouping/clustering support
- [ ] Database server nodes with cylinder shape
- [ ] Load balancer nodes with special indicators
- [ ] Virtual machine nested appearance
- [ ] Container/Docker nodes with stacked appearance
- [ ] CVE vulnerability badges with scoring
- [ ] Auto-validation of IP addresses

### Agent 3: Layout Engine (`network_layout.tex`)
**Priority TODOs:**
- [ ] Implement tiered layout algorithm for N-tier architectures
- [ ] Force-directed graph layout integration
- [ ] Auto-layout algorithm to prevent overlapping nodes
- [ ] Subnet-based clustering and grouping
- [ ] Auto-grouping nodes by IP subnet
- [ ] Multi-page diagram support for large networks
- [ ] Grid layout for data center visualization

### Agent 4: Connections (`connection_renderer.tex`)
**Priority TODOs:**
- [ ] Automatic path finding to avoid node overlaps
- [ ] Bandwidth indicators (line thickness based on traffic)
- [ ] Animated flow direction indicators
- [ ] Connection bundling for high-density areas
- [ ] Edge routing algorithms (orthogonal, polyline)
- [ ] Protocol/port labels on connections
- [ ] Connection aggregation (show "10 connections" vs 10 lines)

### Agent 5: Threat Intelligence (`threat_indicators.tex`)
**Priority TODOs:**
- [ ] CVSS score integration and visualization
- [ ] MITRE ATT&CK framework mapping
- [ ] IOC (Indicators of Compromise) visualization
- [ ] Attack kill chain progression display
- [ ] Threat actor attribution with confidence levels
- [ ] Real-time threat feed integration
- [ ] Security compliance dashboard (NIST, CIS, PCI-DSS)

### Agent 6: Data Import/Export ✅ HIGH PRIORITY COMPLETE + MEDIUM PRIORITY COMPLETE
**High Priority TODOs:**
- [✅] JSON/YAML parser for network data input
- [✅] CSV import for bulk node creation
- [✅] Nmap XML output parser
- [✅] Export to GraphML/DOT format

**Medium Priority TODOs:**
- [✅] Nessus scan result integration
- [✅] Complete GraphML/DOT export implementation
- [✅] Python data conversion utility
- [ ] Database connectivity for live network data
- [ ] REST API for dynamic diagram generation

## Performance Optimization

For large networks (100+ nodes):

1. **Use connection filtering:**
   ```latex
   \filterConnectionsByType{attacks}  % Show only attack connections
   ```

2. **Enable multi-page mode:**
   ```latex
   \layoutMultiPage{subnet_based}
   ```

3. **Adjust detail level:**
   ```latex
   \setDetailLevel{low}  % Hide port labels, reduce decorations
   ```

## Compilation Options

### High-Quality PDF
```bash
pdflatex -interaction=nonstopmode network_diagram_generator.tex
```

### SVG Output (requires dvisvgm)
```bash
pdflatex network_diagram_generator.tex
pdf2svg network_diagram_generator.pdf network_diagram_generator.svg
```

### PNG Output (requires ImageMagick)
```bash
pdflatex network_diagram_generator.tex
convert -density 300 network_diagram_generator.pdf -quality 100 network_diagram.png
```

## Troubleshooting

### "Undefined control sequence" errors
- Ensure all module files are in the same directory
- Verify TeXLive installation includes TikZ libraries

### Overlapping nodes
- Increase `\nodeSpacing` in `network_layout.tex`
- Use manual positioning or auto-layout algorithms

### Long compilation times
- Reduce shadow effects in large diagrams
- Disable background grid
- Use simplified connection styles

## Contributing

This is a modular system designed for enhancement. Each TODO block represents a clear development task. Submit pull requests for individual modules to avoid conflicts.

## License

Free for personal and commercial use. Attribution appreciated.

## Version History

- **v1.0 (Foundation)** - Initial modular architecture with core features
- **v1.1** - Data import/export system (JSON, YAML, CSV, Nmap XML)
- **v1.2** - Nessus integration, complete export functions, Python utilities
- **v1.3 (Current)** - Advanced filtering, transformation, automation tools
- **v2.0 (Planned)** - Auto-layout algorithms and intelligent positioning
- **v3.0 (Planned)** - SIEM integration and real-time threat feeds

## Contact & Support

For questions, bug reports, or feature requests, check the TODO blocks in each module file for priority enhancements.

---

**Built for cybersecurity professionals who demand professional-quality network documentation.**
