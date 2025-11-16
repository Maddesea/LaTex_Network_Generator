# Quick Reference Card - Network Diagram Generator

## Essential Commands (Copy-Paste Ready)

### Node Creation
```latex
% Servers
\createServer{srv1}{192.168.1.10}{0}{0}{Web Server}

% Clients
\createClient{pc1}{192.168.1.100}{-5}{-3}{Workstation}

% Network Devices
\createRouter{rtr1}{10.0.0.1}{0}{5}{Core Router}
\createFirewall{fw1}{10.0.0.2}{0}{3}{Edge Firewall}
\createSwitch{sw1}{192.168.1.1}{-3}{-3}{Access Switch}

% Cloud/Internet
\createCloud{internet}{0}{8}{Internet}

% Attackers
\createAttacker{bad1}{203.0.113.45}{-6}{8}{Threat Actor}
```

### Connections
```latex
% Basic
\drawConnection{node1}{node2}{HTTP}

% Encrypted
\drawEncryptedConnection{node1}{node2}{TLS 1.3}

% Bidirectional
\drawBidirectional{node1}{node2}{SMB}

% Suspicious
\drawSuspiciousConnection{node1}{node2}{Unusual Port}

% Attack
\drawAttackConnection{attacker1}{server1}{SQL Injection}

% Curved (to avoid overlap)
\drawCurvedConnection{node1}{node2}{30}{Label}
```

### Threats & Vulnerabilities
```latex
% Basic vulnerability
\markVulnerability{server1}{CVE-2024-1234}{9.8}

% CVSS vulnerability with detailed scoring
\markVulnerabilityCVSS{server1}{CVE-2024-1234}{9.8}{9.5}{8.7}

% CVSS score meter
\drawCVSSMeter{0}{0}{9.8}{Critical Vuln}

% Compact CVSS badge
\cvssBadge{server1}{9.8}

% DDoS attack
\visualizeDDoS{attacker1,attacker2}{target}{critical}

% SQL injection
\visualizeSQLi{attacker1}{database1}

% Malware infection
\visualizeMalware{workstation1}{Ransomware}

% Data exfiltration
\visualizeExfiltration{server1}{attacker1}{500MB}

% Active exploit correlation
\correlateVulnExploit{srv1}{CVE-2024-1234}{9.8}{yes}{Metasploit}
```

### MITRE ATT&CK & Kill Chain
```latex
% ATT&CK technique badge
\attackTechnique{node}{credential-access}{T1110}{Brute Force}

% Kill chain progression
\drawKillChain{-8}{-5}{3}  % Stage 3 of 7

% Compact kill chain bar
\drawKillChainCompact{0}{0}{5}

% ATT&CK matrix legend
\drawAttackMatrix{12}{8}

% TTP profile
\drawTTPProfile{0}{0}{APT29}

% Attack timeline
\drawAttackTimeline{-5}{3}

% Multi-stage attack chain
\drawAttackChain{stage1}{stage2}{stage3}{stage4}
```

### IOC & Threat Intelligence
```latex
% Enhanced IOC marker
\markIOCEnhanced{node}{malicious-ip}{192.0.2.1}{85}{3}

% Malicious IP with geolocation
\markMaliciousIP{node}{192.0.2.1}{Russia}{92}

% File hash IOC
\markFileHashIOC{node}{SHA256}{a1b2c3d4...}{WannaCry}

% C2 server marker
\markC2Server{node}{evil.badguys.com}{APT28}

% IOC dashboard
\drawIOCDashboard{10}{5}

% Threat intelligence summary
\drawThreatSummary{-8}{8}
```

### Threat Actor Attribution
```latex
% Detailed threat actor profile
\drawThreatActorProfile{0}{5}{APT28}{87}{Operation Ghost}{Espionage}

% Actor comparison
\drawActorComparison{10}{5}

% Campaign tracking
\drawCampaignTracker{0}{0}{SolarStorm}{2025-01-01}{Fortune 500}

% Actor origin marker
\markThreatActorOrigin{node}{APT29}{Russia}{yes}

% Link victims to actor
\linkToThreatActor{attacker}{srv1,srv2,srv3}
```

### Quick Threat Scenarios
```latex
% Ransomware attack
\scenarioRansomware{pc1}{pc2,pc3,srv1}{$50,000 BTC}

% APT infiltration
\scenarioAPT{srv1}{attacker1}{database1}{APT29}{SolarStorm}

% DDoS attack
\scenarioDDoS{attacker1,attacker2,attacker3}{webserver}

% Infection spread
\drawInfectionSpread{patient_zero}{srv1,srv2,srv3}
```

### Security Compliance
```latex
% NIST CSF
\drawNISTCompliance{0}{5}{85}{90}{78}{82}{75}

% CIS Controls v8
\drawCISCompliance{8}{5}{14}{28}{12}

% PCI-DSS
\drawPCIDSSCompliance{0}{0}{12}

% General framework
\drawComplianceScorecard{0}{3}{ISO 27001}{78}{partial}

% Security metrics
\drawSecurityMetrics{10}{8}{12}{24}{15}{8}

% Control effectiveness
\drawControlEffectiveness{0}{0}{Firewall}{92}

% Multi-framework comparison
\drawComplianceComparison{12}{8}

% Security coverage
\drawCoverageHeatmap{0}{5}
```

### Security Status & Dashboards
```latex
% Overall security status
\drawSecurityStatus{0}{8}{75}

% Risk prioritization
\drawRiskPriority{10}{8}{3}{12}{25}{8}

% Incident response status
\drawIncidentStatus{10}{5}{INC-2025-001}{investigating}{Critical}

% Security posture dashboard
\drawSecurityDashboard{10}{8}
```

### Security Zones
```latex
% Basic subnet
\drawSubnet{dmz}{routerOrange}{(node1) (node2) (node3)}{DMZ Network}

% Security zone with trust level
\drawSecurityZone{internal}{clientGreen}
    {(srv1) (srv2) (pc1)}
    {Internal Network}
    {High Trust}
```

### Annotations
```latex
% Add note to node
\annotateNode{server1}{Production}{above}

% Add metadata
\addNodeMetadata{server1}{Ubuntu 22.04}

% Threat indicator
\drawThreatIndicator{-5}{5}{critical}{Breach Detected}
```

## Complete Minimal Example

```latex
\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\usepackage{xcolor}
\usetikzlibrary{positioning,shapes.geometric,arrows.meta,shadows.blur}

\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{threat_indicators}

\begin{document}
\begin{tikzpicture}[scale=1.0, transform shape, font=\sffamily]
    
    % Create nodes
    \createFirewall{fw1}{10.0.0.1}{0}{3}{Firewall}
    \createServer{web1}{192.168.1.10}{0}{0}{Web Server}
    \createAttacker{bad1}{1.2.3.4}{-5}{5}{Attacker}
    
    % Connect them
    \drawConnection{fw1}{web1}{HTTPS}
    \drawAttackConnection{bad1}{fw1}{Port Scan}
    
    % Add threats
    \markVulnerability{web1}{CVE-2024-0001}{8.5}
    \addThreatBadge{web1}{high}
    
\end{tikzpicture}
\end{document}
```

## Page Size Configuration

```latex
% In main .tex file, before \begin{document}:
\renewcommand{\pageSize}{a3}  % Options: a4, a3, a2, a1, a0, letter
\setPageSize{\pageSize}
```

## Color Customization

```latex
% In styles_config.tex or in main file:
\definecolor{myColor}{RGB}{30, 144, 255}

% Use in node:
\tikzset{
    custom server/.style={
        base node,
        fill=myColor!20,
        draw=myColor!80
    }
}
```

## Compilation

```bash
# Simple PDF
pdflatex network_diagram_generator.tex

# Using script (recommended)
./compile.sh pdf     # PDF output
./compile.sh svg     # PDF + SVG
./compile.sh png     # PDF + PNG
./compile.sh all     # All formats
./compile.sh clean   # Remove all outputs
```

## Common Positioning Patterns

```latex
% Grid Layout
\createServer{s1}{IP}{0}{0}{Server 1}
\createServer{s2}{IP}{4}{0}{Server 2}
\createServer{s3}{IP}{0}{-3}{Server 3}
\createServer{s4}{IP}{4}{-3}{Server 4}

% Tiered (Web → App → DB)
\createServer{web1}{IP}{0}{6}{Web}
\createServer{app1}{IP}{0}{3}{App}
\createServer{db1}{IP}{0}{0}{Database}

% Hub and Spoke
\createRouter{hub}{IP}{0}{0}{Core}
\createClient{spoke1}{IP}{-4}{0}{PC1}
\createClient{spoke2}{IP}{0}{4}{PC2}
\createClient{spoke3}{IP}{4}{0}{PC3}
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Undefined control sequence | Ensure all .tex modules are in same directory |
| Overlapping nodes | Increase spacing or adjust x,y coordinates |
| Missing arrows | Check TikZ arrows.meta library is loaded |
| Colors not working | Verify xcolor package is loaded |
| Compilation takes too long | Reduce shadows, simplify connections |

## Coordinate System

```
        y
        ↑
        |
   (0,5)|
        |
        |
  ------+-------- x →
 (-5,0) |(5,0)
        |
        |
   (0,-5)
```

Positive x = right, Positive y = up

## Tips & Tricks

1. **Start Simple**: Create 2-3 nodes first, test compile, then add more
2. **Use Comments**: Mark sections with `% SECTION NAME` for organization
3. **Version Control**: Save working versions before major changes
4. **Incremental Build**: Add nodes/connections/threats in stages
5. **Test Often**: Compile after every major change
6. **Spacing**: Leave extra space between nodes (adjust later)
7. **Color Coding**: Use consistent colors for same device types
8. **Labels**: Keep short, use abbreviations when needed

## Node Types Quick Reference

| Type | Command | Shape | Common Use |
|------|---------|-------|------------|
| Server | `\createServer` | Rectangle | Web, App, DB servers |
| Client | `\createClient` | Rectangle | Workstations, laptops |
| Router | `\createRouter` | Trapezoid | Network routing |
| Firewall | `\createFirewall` | Patterned rect | Security boundary |
| Switch | `\createSwitch` | Thin rect | Network switching |
| Cloud | `\createCloud` | Cloud shape | Internet, cloud services |
| Attacker | `\createAttacker` | Star | Threat actors |

## Connection Types Quick Reference

| Type | Style | Use Case |
|------|-------|----------|
| Normal | Solid arrow | Regular traffic |
| Encrypted | Dotted green | HTTPS, VPN, SSH |
| Suspicious | Dashed orange | Anomalous traffic |
| Attack | Thick red | Active attacks |
| Bidirectional | Double arrow | Two-way communication |

## Save This File!

Keep this reference handy when creating diagrams. It contains the most commonly used commands and patterns.
