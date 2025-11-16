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
└── network_data.tex           # Actual network topology data
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

### Basic Threat Indicators

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

### CVSS Score Visualization ✨ NEW

```latex
% Display comprehensive CVSS score breakdown
\drawCVSSScore{x}{y}{CVE-2024-1234}{9.8}{9.5}{8.7}{CVSS:3.1/AV:N/AC:L...}

% Add CVSS badge to node
\cvssbadge{node_name}{CVE-2024-1234}{9.8}

% Show detailed CVSS metrics breakdown
\drawCVSSMetrics{x}{y}{Network}{Low}{None}{None}{Unchanged}{High}{High}{High}
```

### MITRE ATT&CK Framework ✨ NEW

```latex
% Display MITRE ATT&CK technique
\drawMITREAttack{x}{y}{T1566}{Phishing}{Initial Access}

% Add MITRE badge to compromised node
\mitrebadge{node_name}{T1566}

% Show MITRE ATT&CK kill chain progression
\drawMITREKillChain{x}{y}{3}  % Currently at stage 3 (Execution)

% Map technique to tactic on node
\mapTechniqueToTactic{node_name}{T1078}{Valid Accounts}

% Display multiple techniques for complex attack
\drawMITRETTP{x}{y}{APT Attack}{T1566 Phishing \\ T1059 Command Execution \\ T1547 Persistence}
```

### IOC (Indicators of Compromise) ✨ NEW

```latex
% Mark generic IOC with reputation score
\markIOC{node_name}{IP}{1.2.3.4}{95}  % 95/100 reputation (malicious)

% Display malicious IP address
\markMaliciousIP{node_name}{1.2.3.4}{95}{VirusTotal}

% Display malicious domain
\markMaliciousDomain{node_name}{evil.com}{87}{C2}

% Show malware file hash
\markMalwareHash{x,y}{SHA256}{a1b2c3d4...}{45}  % 45 AV detections

% Display IOC age/freshness
\markIOCFreshness{node_name}{3}{FRESH}  % 3 days old

% Comprehensive IOC dashboard
\drawIOCDashboard{x}{y}{12}{8}{5}{25}  % 12 IPs, 8 domains, 5 hashes, 25 total

% Threat feed integration indicator
\markThreatFeed{x}{y}{AlienVault OTX}{2024-01-15}{47}
```

### Attack Kill Chain Progression ✨ NEW

```latex
% Show Cyber Kill Chain (Lockheed Martin) with current stage
\drawKillChain{x}{y}{4}{defenses}  % Currently at stage 4 (Exploitation)

% Display defensive gaps analysis
\drawDefensiveGaps{x}{y}{1,2,3}{4,5,6,7}  % Protected: 1-3, Vulnerable: 4-7

% NIST Cybersecurity Framework coverage
\drawNISTMapping{x}{y}{85}{70}{60}{50}{40}  % Identify/Protect/Detect/Respond/Recover

% Attack timeline visualization
\drawAttackTimeline{x}{y}{2024-01-15 14:32}{2024-01-15 16:45}{Initial phishing \\ Payload executed \\ C2 established}

% Visualize attack path through network
\drawAttackPath{attacker}{web_server}{database}{4}  % Stage 4
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
**Completed Features:**
- [x] CVSS score integration and visualization ✅
- [x] MITRE ATT&CK framework mapping ✅
- [x] IOC (Indicators of Compromise) visualization ✅
- [x] Attack kill chain progression display ✅

**Remaining TODOs:**
- [ ] Threat actor attribution with confidence levels
- [ ] Real-time threat feed integration
- [ ] Security compliance dashboard (NIST, CIS, PCI-DSS)
- [ ] Vulnerability database integration

### Agent 6: Data Import/Export
**Priority TODOs:**
- [ ] JSON/YAML parser for network data input
- [ ] CSV import for bulk node creation
- [ ] Nmap XML output parser
- [ ] Nessus scan result integration
- [ ] Export to GraphML/DOT format
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
- **v1.1 (Current)** - Enhanced threat intelligence module with:
  - CVSS score visualization (base, temporal, environmental scores)
  - MITRE ATT&CK framework mapping with kill chain progression
  - IOC visualization (malicious IPs, domains, file hashes)
  - Cyber Kill Chain progression tracking
  - NIST Cybersecurity Framework mapping
  - Attack timeline and path visualization
- **v1.2 (Planned)** - Auto-layout algorithms and data import
- **v2.0 (Planned)** - SIEM integration and real-time threat feeds

## Contact & Support

For questions, bug reports, or feature requests, check the TODO blocks in each module file for priority enhancements.

---

**Built for cybersecurity professionals who demand professional-quality network documentation.**
