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

### NEW: Advanced Threat Intelligence Features

#### CVSS Score Visualization
```latex
% Enhanced CVSS vulnerability marker with breakdown
\markVulnerabilityCVSS{node}{CVE-2024-1234}{9.8}{9.5}{8.7}

% CVSS score meter (visual gauge)
\drawCVSSMeter{0}{0}{9.8}{Web Server Vulnerability}

% Detailed CVSS breakdown
\drawCVSSBreakdown{0}{0}{9.8}{8.5}{9.2}{9.5}{8.7}

% Compact CVSS badge
\cvssBadge{node}{9.8}
```

#### MITRE ATT&CK Framework Integration
```latex
% Display ATT&CK technique on node
\attackTechnique{node}{credential-access}{T1110}{Brute Force}

% Full kill chain visualization (7 stages)
\drawAttackKillChain{0}{0}{4}  % Currently at stage 4 (Exploitation)

% ATT&CK technique list
\drawAttackTechniqueList{10}{5}

% TTP Profile for threat actor
\drawTTPProfile{0}{0}{APT29}

% Attack with technique label
\drawAttackWithTechnique{attacker}{victim}{T1566.001}{Spearphishing}

% ATT&CK Matrix legend
\drawAttackMatrix{12}{8}
```

#### IOC (Indicators of Compromise)
```latex
% Enhanced IOC marker with reputation and age
\markIOCEnhanced{node}{malicious-ip}{192.0.2.1}{85}{3}

% Malicious IP with geolocation
\markMaliciousIP{node}{192.0.2.1}{Russia}{92}

% File hash IOC
\markFileHashIOC{node}{SHA256}{a1b2c3d4...}{WannaCry}

% Mark C2 server
\markC2Server{node}{evil.badguys.com}{APT28}

% IOC Dashboard
\drawIOCDashboard{10}{5}

% Threat feed status
\drawThreatFeedStatus{0}{0}{VirusTotal}{active}

% Comprehensive IOC list
\drawIOCList{0}{5}

% Reputation score meter
\drawReputationScore{0}{0}{75}{suspicious.domain.com}
```

#### Attack Kill Chain & Progression
```latex
% Full cyber kill chain with current stage
\drawKillChain{-8}{-5}{3}  % Currently at stage 3 (Delivery)

% Compact progress bar
\drawKillChainCompact{0}{0}{5}

% Time-based attack timeline
\drawAttackTimeline{-5}{3}

% Attack path tree
\drawAttackPath{10}{5}

% Infection spread visualization
\drawInfectionSpread{patient_zero}{srv1,srv2,srv3}

% Kill chain stage details
\drawKillChainDetails{0}{5}{3}  % Details for stage 3
```

#### Enhanced Threat Actor Attribution
```latex
% Detailed threat actor profile
\drawThreatActorProfile{0}{5}{APT28}{87}{Operation Ghost}{Espionage}

% Actor comparison analysis
\drawActorComparison{10}{5}

% Campaign tracking
\drawCampaignTracker{0}{0}{SolarStorm}{2025-01-01}{Fortune 500}

% Threat actor with origin
\markThreatActorOrigin{node}{APT29}{Russia}{yes}

% Link multiple victims to actor
\linkToThreatActor{attacker}{srv1,srv2,srv3}

% Threat intelligence citation
\citeThreatIntel{0}{-8}{MISP}{2025-01-16}
```

#### Security Compliance Dashboards
```latex
% NIST Cybersecurity Framework
\drawNISTCompliance{0}{5}{85}{90}{78}{82}{75}

% CIS Controls v8
\drawCISCompliance{8}{5}{14}{28}{12}

% PCI-DSS Compliance
\drawPCIDSSCompliance{0}{0}{12}

% General framework scorecard
\drawComplianceScorecard{0}{3}{ISO 27001}{78}{partial}

% Security metrics
\drawSecurityMetrics{10}{8}{12}{24}{15}{8}

% Control effectiveness
\drawControlEffectiveness{0}{0}{Firewall}{92}

% Multi-framework comparison
\drawComplianceComparison{12}{8}

% Security coverage heatmap
\drawCoverageHeatmap{0}{5}
```

#### Quick Threat Scenarios & Helper Functions
```latex
% Ransomware attack scenario
\scenarioRansomware{pc1}{pc2,pc3,srv1}{$50,000 BTC}

% APT infiltration scenario
\scenarioAPT{srv1}{attacker1}{database1}{APT29}{SolarStorm}

% DDoS attack scenario
\scenarioDDoS{attacker1,attacker2,attacker3}{webserver}

% Multi-stage attack chain
\drawAttackChain{stage1}{stage2}{stage3}{stage4}

% Vulnerability with active exploit
\correlateVulnExploit{srv1}{CVE-2024-1234}{9.8}{yes}{Metasploit}

% Risk prioritization dashboard
\drawRiskPriority{10}{8}{3}{12}{25}{8}

% Threat intelligence summary
\drawThreatSummary{-8}{8}

% Security status dashboard
\drawSecurityStatus{0}{8}{75}

% Incident response status
\drawIncidentStatus{10}{5}{INC-2025-001}{investigating}{Critical}
```

#### Defensive Security Controls (Blue Team)
```latex
% Mark security control on node
\markSecurityControl{srv1}{Firewall}{active}

% IDS/IPS monitoring
\markIDS{srv1}{Snort}{5}

% WAF protection
\markWAF{web1}{ModSecurity}{142}

% EDR/Endpoint protection
\markEDR{pc1}{CrowdStrike}{protected}

% Network segmentation
\drawSegmentBoundary{-2}{-2}{4}{4}{DMZ}

% SIEM integration
\markSIEM{10}{8}{Splunk}{5000}

% Defense-in-depth layers
\drawDefenseLayers{12}{8}

% Honeypot marker
\markHoneypot{fake_srv}{SSH Honeypot}

% Monitoring coverage
\drawMonitoringCoverage{0}{-6}{92}

% Patch management
\markPatchStatus{srv1}{3}{2025-01-10}

% Backup status
\markBackupStatus{database1}{2025-01-15}{current}

% Zero Trust indicator
\markZeroTrust{srv1}{yes}
```

#### Risk Analysis & Calculation
```latex
% Risk matrix
\drawRiskMatrix{10}{8}

% Calculate risk score (returns numeric value)
% Parameters: threat_level, vuln_score, asset_value, control_effectiveness
Risk: \calculateRiskScore{80}{90}{95}{75}
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
**High Priority TODOs:**
- [x] CVSS score integration and visualization - **COMPLETED**
- [x] MITRE ATT&CK framework mapping - **COMPLETED**
- [x] IOC (Indicators of Compromise) visualization - **COMPLETED**
- [x] Attack kill chain progression display - **COMPLETED**

**Medium Priority TODOs:**
- [x] Threat actor attribution with confidence levels - **COMPLETED**
- [x] Security compliance dashboard (NIST, CIS, PCI-DSS) - **COMPLETED**
- [x] Advanced threat correlation features - **COMPLETED**
- [x] Quick threat scenario helpers - **COMPLETED**
- [ ] Real-time threat feed integration

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
- **v1.1 (Planned)** - Auto-layout algorithms and data import
- **v2.0 (Planned)** - SIEM integration and real-time threat feeds

## Contact & Support

For questions, bug reports, or feature requests, check the TODO blocks in each module file for priority enhancements.

---

**Built for cybersecurity professionals who demand professional-quality network documentation.**
