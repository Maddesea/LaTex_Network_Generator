# Integration Guide - External Tools & Advanced Features

This guide covers integration with external tools, animation support, color schemes, and network analysis features.

---

## Table of Contents

1. [Python Integration](#python-integration)
2. [Color Schemes](#color-schemes)
3. [Beamer Animations](#beamer-animations)
4. [Network Statistics](#network-statistics)
5. [External Tool Workflow](#external-tool-workflow)

---

## Python Integration

### Overview

The `latex_bridge.py` script converts various network formats to LaTeX diagram code.

### Supported Formats

1. **JSON** - Custom network definition
2. **NetworkX Graphs** - Python graph objects
3. **CSV** - Node and connection lists
4. **Nmap XML** - Network scan results
5. **GraphML** - Graph Markup Language

### Installation

```bash
# Install Python dependencies
pip install networkx

# Optional: For Nmap integration
sudo apt-get install nmap

# Optional: For GraphViz integration
sudo apt-get install graphviz
```

### Usage

#### 1. JSON to LaTeX

**Input: network.json**
```json
{
    "nodes": [
        {"id": "web1", "ip": "192.168.1.10", "x": 0, "y": 0, "label": "Web Server", "type": "server"},
        {"id": "db1", "ip": "10.0.1.20", "x": 0, "y": -5, "label": "Database", "type": "server"}
    ],
    "connections": [
        {"source": "web1", "target": "db1", "label": "SQL", "type": "encrypted"}
    ]
}
```

**Convert:**
```bash
python3 latex_bridge.py json network.json output.tex
```

**Output: output.tex**
```latex
% Auto-generated from JSON
\begin{tikzpicture}[scale=1.0, transform shape, font=\sffamily]

    \createServer{web1}{192.168.1.10}{0}{0}{Web Server}
    \createServer{db1}{10.0.1.20}{0}{-5}{Database}

    \drawEncryptedConnection{web1}{db1}{SQL}

\end{tikzpicture}
```

#### 2. CSV to LaTeX

**nodes.csv:**
```csv
id,ip,x,y,label,type
web1,192.168.1.10,0,0,Web Server,server
web2,192.168.1.11,4,0,Web Server 2,server
lb1,192.168.1.5,2,3,Load Balancer,router
```

**connections.csv:**
```csv
source,target,label,type
lb1,web1,HTTP,normal
lb1,web2,HTTP,normal
```

**Convert:**
```bash
python3 latex_bridge.py csv nodes.csv connections.csv output.tex
```

#### 3. Auto-Layout with NetworkX

Use NetworkX to calculate optimal positions automatically:

```bash
# Spring layout (force-directed)
python3 latex_bridge.py auto-layout network.json output.tex spring

# Circular layout
python3 latex_bridge.py auto-layout network.json output.tex circular

# Kamada-Kawai layout
python3 latex_bridge.py auto-layout network.json output.tex kamada_kawai

# Spectral layout
python3 latex_bridge.py auto-layout network.json output.tex spectral
```

#### 4. Nmap Scan to Diagram

```bash
# Scan network
nmap -oX scan.xml 192.168.1.0/24

# Convert to diagram
python3 latex_bridge.py nmap scan.xml network.tex
```

### Python API Usage

```python
from latex_bridge import LatexNetworkGenerator
import networkx as nx

# Create NetworkX graph
G = nx.Graph()
G.add_node("web1", ip="192.168.1.10", label="Web Server", type="server")
G.add_node("db1", ip="10.0.1.20", label="Database", type="server")
G.add_edge("web1", "db1", label="SQL", type="encrypted")

# Generate LaTeX code
gen = LatexNetworkGenerator()
latex_code = gen.from_networkx(G, layout_algorithm='spring')

# Write to file
with open('output.tex', 'w') as f:
    f.write(latex_code)
```

---

## Color Schemes

### Available Schemes

The `color_schemes.tex` module provides 10 professional color palettes:

1. **default** - Bright, vibrant colors (current)
2. **dark** - Dark mode compatible
3. **colorblind** - Deuteranopia/Protanopia safe
4. **monochrome** - Grayscale for B&W printing
5. **high-contrast** - Maximum accessibility
6. **pastel** - Soft, professional look
7. **corporate** - Professional blue/gray
8. **neon** - Vibrant, eye-catching
9. **earth** - Natural, warm tones
10. **ocean** - Cool blue/green palette

### Usage

```latex
% In your main .tex file, add:
\input{color_schemes}

% Load a scheme
\loadColorScheme{colorblind}

% Or set a complete theme
\setDiagramTheme{dark}  % Includes color scheme + background
```

### Color Scheme Examples

**Colorblind-Friendly:**
```latex
\loadColorScheme{colorblind}
\createServer{srv1}{192.168.1.10}{0}{0}{Server}
% Uses blue-orange palette safe for red-green colorblindness
```

**Dark Mode:**
```latex
\setDiagramTheme{dark}
% Sets dark background + bright colors
```

**Print:**
```latex
\setDiagramTheme{print}
% High contrast, optimized for printing
```

### Custom Color Utilities

```latex
% Lighten a color
\lightenColor{serverBlue}{50}{lightBlue}

% Darken a color
\darkenColor{serverBlue}{30}{darkBlue}

% Blend two colors
\blendColors{serverBlue}{clientGreen}{50}{blendedColor}
```

---

## Beamer Animations

### Setup

```latex
\documentclass{beamer}
\usepackage{tikz}
% ... other packages ...

\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{beamer_animations}  % Add this!

\begin{document}

\begin{frame}{Network Topology}
    \enableAnimations  % Enable animation support
    % Your animated diagram here
\end{frame}

\end{document}
```

### Progressive Reveal

```latex
% Reveal nodes one at a time
\only<1->{
    \createServer{web1}{192.168.1.10}{0}{0}{Web Server}
}
\only<2->{
    \createServer{db1}{10.0.1.20}{0}{-5}{Database}
}
\only<3->{
    \drawEncryptedConnection{web1}{db1}{SQL}
}
```

### Highlight Nodes

```latex
% Normal view (slide 1)
\only<1->{
    \createServer{target}{192.168.1.10}{0}{0}{Target Server}
}

% Highlighted (slide 2)
\highlightNode<2>{target}
```

### Attack Scenario Animation

```latex
% Slide 1: Normal network
\only<1>{
    \createServer{web}{192.168.1.10}{0}{0}{Web Server}
    \createAttacker{hacker}{8.8.8.8}{-5}{5}{Attacker}
}

% Slide 2: Show attack
\only<2->{
    \draw[attack, very thick, ->] (hacker) -- (web);
}

% Slide 3: Compromise
\only<3->{
    \node[fill=red!30] at (web) {COMPROMISED};
}

% Slide 4: Mitigation
\only<4->{
    \createFirewall{fw}{192.168.1.1}{-2}{2}{Firewall};
    \node[fill=green!30] {Threat Blocked};
}
```

### Data Flow Animation

```latex
% Animate packets flowing
\animateDataFlow<2->{source}{target}{Data Transfer}

% Pulsing active connection
\pulsingConnection<3->{web}{db}
```

### Kill Chain Progression

```latex
\begin{frame}{Cyber Kill Chain}
    \animateKillChain
    % Shows each phase on separate slide
\end{frame}
```

---

## Network Statistics

### Setup

```latex
\input{network_statistics}

% Enable counters
\begin{tikzpicture}
    % Count nodes as you create them
    \createServer{web1}{...}{...}{...}{Web}
    \countServer  % Increment server counter

    \createClient{pc1}{...}{...}{...}{Client}
    \countClient  % Increment client counter

    \drawConnection{web1}{pc1}{HTTP}
    \countConnection  % Increment connection counter
\end{tikzpicture}
```

### Statistics Dashboard

```latex
% Draw complete statistics panel
\drawStatisticsDashboard{10}{-10}
% Shows: node counts, topology metrics, security score
```

### Individual Metrics

```latex
% Calculate network density
\calcNetworkDensity{\density}
\node at (0, 0) {Network Density: \pgfmathprintnumber{\density}\%};

% Calculate security score (0-100)
\calcSecurityScore{\score}
\node at (0, -1) {Security: \pgfmathprintnumber{\score}/100};

% Calculate avg connections per node
\calcAvgConnectionsPerNode{\avg}
\node at (0, -2) {Avg Connections: \pgfmathprintnumber{\avg}};
```

### Visualizations

**Node Type Pie Chart:**
```latex
\drawNodeTypePie{0}{0}{2}  % x, y, radius
% Shows distribution of server/client/router/firewall
```

**Security Gauge:**
```latex
\drawSecurityGauge{0}{0}{1.5}{75}  % x, y, radius, score
% Visual arc gauge (green/yellow/red)
```

**Connection Heatmap:**
```latex
\drawConnectionHeatmap{0}{0}{5}{1}  % x, y, width, height
% Shows network density gradient
```

### Export Statistics

```latex
% Export to CSV file
\exportStatistics{network_stats.csv}
% Creates: total_nodes,total_connections,density,security_score,...
```

---

## External Tool Workflow

### Complete Workflow Example

#### 1. Scan Network with Nmap

```bash
nmap -sV -oX network_scan.xml 192.168.1.0/24
```

#### 2. Convert to JSON (manual or with Python)

**network.json:**
```json
{
    "nodes": [
        {"id": "host1", "ip": "192.168.1.10", "x": 0, "y": 0, "label": "Web Server", "type": "server"},
        {"id": "host2", "ip": "192.168.1.20", "x": 4, "y": 0, "label": "Database", "type": "server"}
    ],
    "connections": [
        {"source": "host1", "target": "host2", "label": "MySQL", "type": "encrypted"}
    ]
}
```

#### 3. Auto-Layout with NetworkX

```bash
python3 latex_bridge.py auto-layout network.json network.tex kamada_kawai
```

#### 4. Incorporate into Main Diagram

**main.tex:**
```latex
\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\usepackage{xstring}

\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{color_schemes}
\input{network_statistics}

\begin{document}
\begin{tikzpicture}

% Load color scheme
\loadColorScheme{colorblind}

% Include auto-generated content
\input{network}  % network.tex from Python

% Add statistics
\drawStatisticsDashboard{10}{-8}

\end{tikzpicture}
\end{document}
```

#### 5. Compile

```bash
make main
# or
pdflatex main.tex
```

### GraphViz Integration

Export to DOT format for external layout calculation:

```python
from latex_bridge import LatexNetworkGenerator

gen = LatexNetworkGenerator()
# ... add nodes and connections ...
gen.to_graphviz_dot('network.dot')
```

```bash
# Calculate layout with GraphViz
dot -Tplain network.dot -o positions.txt

# Parse positions and generate LaTeX
# (custom script needed)
```

---

## Advanced Integration Patterns

### 1. Dynamic Diagram Generation

**Python script: generate_network.py**
```python
#!/usr/bin/env python3
import json
import subprocess

# Fetch live network data (e.g., from API, database)
network_data = fetch_network_topology()

# Save as JSON
with open('network.json', 'w') as f:
    json.dump(network_data, f)

# Convert to LaTeX
subprocess.run(['python3', 'latex_bridge.py', 'auto-layout',
                'network.json', 'network.tex', 'spring'])

# Compile diagram
subprocess.run(['pdflatex', 'main.tex'])

print("Diagram generated: main.pdf")
```

### 2. Continuous Integration

**GitHub Actions workflow:**
```yaml
name: Generate Network Diagrams

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install LaTeX
        run: sudo apt-get install texlive-latex-extra
      - name: Install Python deps
        run: pip install networkx
      - name: Generate diagrams
        run: make all-formats
      - name: Upload PDFs
        uses: actions/upload-artifact@v2
        with:
          name: diagrams
          path: '*.pdf'
```

### 3. Monitoring Integration

Connect to monitoring systems:

```python
import requests
from latex_bridge import LatexNetworkGenerator

# Fetch from Nagios/Zabbix/Prometheus
response = requests.get('http://monitoring/api/topology')
data = response.json()

# Generate diagram
gen = LatexNetworkGenerator()
# ... process data ...
latex_code = gen.from_json('topology.json')

# Auto-compile every hour via cron
```

---

## Tips & Best Practices

### Color Schemes

1. **Accessibility:** Use `colorblind` scheme for presentations
2. **Printing:** Use `monochrome` or `high-contrast`
3. **Dark rooms:** Use `dark` theme for projectors
4. **Corporate:** Use `corporate` for professional documents

### Animations

1. **Timing:** Keep animations under 10 slides per concept
2. **Purpose:** Only animate to show progression, not decoration
3. **Simplicity:** Fewer animations = clearer message
4. **Export:** Use `-shell-escape` if animations need compilation tricks

### Statistics

1. **Count Everything:** Use all counter functions
2. **Update Live:** Recalculate metrics on each compile
3. **Export:** Save statistics for trending over time
4. **Visualize:** Use dashboards for executive summaries

### Python Integration

1. **Automate:** Use cron jobs for regular updates
2. **Validate:** Check JSON schema before conversion
3. **Version:** Keep network.json in version control
4. **Document:** Add comments to Python scripts

---

## Troubleshooting

### Issue: Python script fails

**Solution:**
```bash
# Check Python version (needs 3.6+)
python3 --version

# Install dependencies
pip install networkx

# Run with verbose errors
python3 latex_bridge.py json network.json output.tex 2>&1 | tee errors.log
```

### Issue: Colors don't change

**Solution:**
```latex
% Ensure color scheme is loaded BEFORE creating nodes
\loadColorScheme{dark}

% Then create nodes
\createServer{...}
```

### Issue: Animations don't work

**Solution:**
```latex
% Must use beamer document class
\documentclass{beamer}

% Call enableAnimations
\enableAnimations
```

### Issue: Statistics show zero

**Solution:**
```latex
% Must call counter functions
\createServer{srv1}{...}
\countServer  % Don't forget this!
```

---

## Examples

See these files for complete examples:
- `example_comprehensive_showcase.tex` - Statistics dashboard
- `example_tiered_layout.tex` - Color schemes
- Sample Beamer presentation (create with animations)

---

**For more help:** Check the FEATURE_CATALOG.md for complete command reference.
