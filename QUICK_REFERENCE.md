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
% Mark vulnerability
\markVulnerability{server1}{CVE-2024-1234}{9.8}

% Add threat badge
\addThreatBadge{server1}{critical}  % critical, high, medium, low, info

% DDoS attack
\visualizeDDoS{attacker1,attacker2}{target}{critical}

% SQL injection
\visualizeSQLi{attacker1}{database1}

% Malware infection
\visualizeMalware{workstation1}{Ransomware}

% Data exfiltration
\visualizeExfiltration{server1}{attacker1}{500MB}
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
