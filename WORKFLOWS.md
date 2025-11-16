# Real-World Workflows

This document demonstrates practical workflows for using the Network Diagram Generator in real-world scenarios.

## Table of Contents

1. [Security Assessment Workflow](#security-assessment-workflow)
2. [Network Documentation Workflow](#network-documentation-workflow)
3. [Compliance Reporting Workflow](#compliance-reporting-workflow)
4. [Incident Response Workflow](#incident-response-workflow)
5. [Change Management Workflow](#change-management-workflow)
6. [Automated Monitoring Integration](#automated-monitoring-integration)

---

## Security Assessment Workflow

### Scenario
You're performing a security assessment of a client's network. You need to discover the network, identify vulnerabilities, and create a comprehensive report with visual diagrams.

### Steps

#### 1. Network Discovery with Nmap

```bash
# Scan the target network
nmap -sV -O 192.168.1.0/24 -oX network_scan.xml

# Convert to diagram format
./network_diagram_tool.sh nmap network_scan.xml discovered_network

# Result: discovered_network.pdf with all discovered hosts
```

#### 2. Vulnerability Scanning with Nessus

```bash
# After running Nessus scan, export as .nessus file
# Then generate vulnerability diagram
./network_diagram_tool.sh nessus scan_results.nessus vulnerability_report

# Result: vulnerability_report.pdf with threat indicators
```

#### 3. Combine Discovery and Vulnerabilities

```latex
% security_assessment.tex
\documentclass[tikz,border=10pt]{standalone}
\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{threat_indicators}
\input{data_import}

\begin{document}
    % Merge network discovery with vulnerability data
    \mergeNetworkData{network_scan.json}{vulnerability_data.json}

    \begin{tikzpicture}[scale=1.0, transform shape, font=\sffamily]
        \renderNetworkNodes
        \renderConnections

        % Show only critical vulnerabilities
        \filterVulnerabilitiesByCVSS{9.0}{vulnerability_data.json}

        \node[font=\Large, anchor=north, text=red!80] at (0,12) {
            \textbf{SECURITY ASSESSMENT REPORT}
        };
    \end{tikzpicture}
\end{document}
```

#### 4. Generate Executive Summary

```bash
# Compile the report
lualatex security_assessment.tex

# Export to formats for stakeholders
./network_diagram_tool.sh export combined_data.json

# Share: security_assessment.pdf (for executives)
#        combined_data.graphml (for security team analysis)
```

---

## Network Documentation Workflow

### Scenario
You need to create and maintain up-to-date documentation for your organization's network infrastructure.

### Steps

#### 1. Create Initial Network Data

```bash
# Use quickstart to create project
./quickstart.sh
# Choose "Enterprise" template
# Project name: "corporate_network"

cd corporate_network
```

#### 2. Customize Network Topology

```json
// Edit corporate_network.json
{
  "nodes": [
    {
      "id": "datacenter_fw",
      "type": "firewall",
      "ip": "10.0.0.1",
      "x": 0,
      "y": 10,
      "label": "Datacenter Firewall\n(Palo Alto PA-5220)"
    },
    // ... add your actual infrastructure
  ],
  "connections": [
    // ... define your connections
  ]
}
```

#### 3. Generate Multiple Views

```latex
% overview.tex - High-level overview
\renewcommand{\renderNetworkNodes}{
    % Show only infrastructure devices
    \filterNodesByType{firewall}{corporate_network.json}
    \filterNodesByType{router}{corporate_network.json}
    \filterNodesByType{switch}{corporate_network.json}
}
```

```latex
% dmz_detail.tex - Detailed DMZ view
\renewcommand{\renderNetworkNodes}{
    % Show only DMZ subnet
    \filterNodesBySubnet{192.168.10}{corporate_network.json}
}
```

#### 4. Automate Updates

```bash
# Create update script
cat > update_docs.sh <<'EOF'
#!/bin/bash
# Update network documentation

echo "Building network documentation..."

# Build all views
lualatex overview.tex
lualatex dmz_detail.tex
lualatex internal_detail.tex
lualatex database_tier.tex

# Combine into documentation package
pdftk overview.pdf dmz_detail.pdf internal_detail.pdf database_tier.pdf \
      cat output complete_network_docs.pdf

echo "Documentation updated: complete_network_docs.pdf"
EOF

chmod +x update_docs.sh
./update_docs.sh
```

---

## Compliance Reporting Workflow

### Scenario
Generate network diagrams for PCI-DSS, HIPAA, or SOC 2 compliance audits.

### Steps

#### 1. Create Compliance-Focused Diagram

```latex
% pci_dss_network.tex
\documentclass[tikz,border=10pt]{standalone}
\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{threat_indicators}
\input{data_import}

\begin{document}
    \importJSON{network.json}

    \begin{tikzpicture}[scale=1.2, transform shape, font=\sffamily]
        \renderNetworkNodes
        \renderConnections

        % Highlight PCI-DSS cardholder data environment
        \begin{scope}[on background layer]
            \node[
                draw=red,
                ultra thick,
                fill=red!5,
                fit=(payment_gateway) (cc_database) (app_server),
                inner sep=20pt,
                label=above:{\Large\textbf{PCI-DSS CDE}}
            ] (cde) {};
        \end{scope}

        % Show compliance requirements
        \node[anchor=north west, align=left, font=\small] at (-12,12) {
            \textbf{PCI-DSS Requirements:} \\
            ✓ Firewall between CDE and internet \\
            ✓ Encrypted connections to database \\
            ✓ Network segmentation \\
            ✓ Restricted access controls
        };
    \end{tikzpicture}
\end{document}
```

#### 2. Generate Data Flow Diagrams

```bash
# Show only encrypted connections (compliance requirement)
cat > show_encrypted_only.tex <<'EOF'
\renewcommand{\renderConnections}{
    \directlua{
        local file = io.open("network.json", "r")
        local content = file:read("*all")
        file:close()
        local data = json.decode(content)

        for i, conn in ipairs(data.connections) do
            if conn.type == "encrypted" then
                convertJSONToConnections({connections = {conn}})
            end
        end
    }
}
EOF
```

---

## Incident Response Workflow

### Scenario
During a security incident, quickly visualize the affected network segment and attack path.

### Steps

#### 1. Identify Compromised Systems

```json
// incident_affected_systems.json
{
  "nodes": [
    {"id": "patient_db", "type": "server", "ip": "10.1.5.20",
     "x": 0, "y": 0, "label": "Patient DB (COMPROMISED)"}
  ],
  "threats": [
    {"target": "patient_db", "type": "malware",
     "cve": "", "severity": 10.0, "description": "Ransomware Detected"}
  ]
}
```

#### 2. Visualize Attack Path

```latex
% incident_visualization.tex
\documentclass[tikz,border=10pt]{standalone}
\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{threat_indicators}
\input{data_import}

\begin{document}
    \importJSON{network.json}

    \begin{tikzpicture}[scale=1.0, transform shape, font=\sffamily]
        \renderNetworkNodes
        \renderConnections

        % Highlight attack path
        \draw[attack conn, ultra thick]
            (internet) -- (firewall) node[midway,right] {1. Initial Access};
        \draw[attack conn, ultra thick]
            (firewall) -- (web_server) node[midway,right] {2. Web Shell};
        \draw[attack conn, ultra thick]
            (web_server) -- (app_server) node[midway,right] {3. Lateral Movement};
        \draw[attack conn, ultra thick]
            (app_server) -- (patient_db) node[midway,right] {4. Data Exfiltration};

        % Mark compromised systems
        \visualizeMalware{web_server}{Web Shell}
        \visualizeMalware{app_server}{Credential Dumping}
        \visualizeMalware{patient_db}{Ransomware}

        \node[font=\Large, text=red, anchor=north] at (0,10) {
            \textbf{INCIDENT \#2024-11-16-001}
        };
    \end{tikzpicture}
\end{document}
```

#### 3. Generate Incident Timeline

```bash
# Create timeline diagram showing progression
lualatex incident_visualization.tex

# Export for incident report
./network_diagram_tool.sh export incident_data.json

# Share with IR team
scp incident_visualization.pdf ir-team@soc.company.com:/reports/
```

---

## Change Management Workflow

### Scenario
Document network changes before and after for change management approval.

### Steps

#### 1. Capture Current State

```bash
# Before change
cp production_network.json network_before_change.json

# Generate "before" diagram
./network_diagram_tool.sh nmap before_scan.xml network_before
```

#### 2. Plan Changes

```json
// Modify network_after_change.json with planned changes
{
  "nodes": [
    // Add new firewall
    {"id": "dmz_fw_new", "type": "firewall", "ip": "192.168.5.1",
     "x": 2, "y": 4, "label": "NEW: DMZ Firewall"},
    // existing nodes...
  ]
}
```

#### 3. Generate Comparison

```latex
% change_comparison.tex
\documentclass{article}
\usepackage{tikz}
\usepackage{graphicx}
\input{styles_config}
\input{node_definitions}
\input{network_layout}
\input{connection_renderer}
\input{threat_indicators}
\input{data_import}

\begin{document}

\section*{Network Change Request \#2024-042}

\subsection*{Current State}
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{network_before.pdf}
\caption{Current Production Network}
\end{figure}

\subsection*{Proposed State}
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{network_after.pdf}
\caption{Network After Change Implementation}
\end{figure}

\subsection*{Changes Summary}
\begin{itemize}
\item Add new DMZ firewall for enhanced security
\item Reconfigure routing to isolate DMZ
\item Update firewall rules
\end{itemize}

\end{document}
```

---

## Automated Monitoring Integration

### Scenario
Automatically generate updated network diagrams from monitoring systems.

### Steps

#### 1. Export from Monitoring System

```bash
# Example: Export from Nagios/Zabbix
# (This is pseudo-code, adapt to your monitoring system)

curl -X GET "https://monitoring.company.com/api/hosts" \
    -H "Authorization: Bearer $API_TOKEN" \
    -o hosts_export.json
```

#### 2. Transform to Network Diagram Format

```python
#!/usr/bin/env python3
# monitoring_to_network.py

import json
import requests

# Fetch monitoring data
def fetch_monitoring_data():
    # Replace with your monitoring system API
    response = requests.get(
        "https://monitoring.company.com/api/hosts",
        headers={"Authorization": f"Bearer {API_TOKEN}"}
    )
    return response.json()

# Convert to network diagram format
def convert_to_network_format(monitoring_data):
    network = {"nodes": [], "connections": []}

    for host in monitoring_data['hosts']:
        node = {
            "id": host['hostname'],
            "type": detect_type(host),
            "ip": host['ip'],
            "x": host.get('x', 0),
            "y": host.get('y', 0),
            "label": host['hostname']
        }

        # Add status indicator
        if host['status'] != 'UP':
            network.setdefault('threats', []).append({
                "target": host['hostname'],
                "type": "outage",
                "severity": 8.0,
                "description": f"Host {host['status']}"
            })

        network['nodes'].append(node)

    return network

# Save to file
def main():
    data = fetch_monitoring_data()
    network = convert_to_network_format(data)

    with open('live_network.json', 'w') as f:
        json.dump(network, f, indent=2)

    print("Generated: live_network.json")

if __name__ == '__main__':
    main()
```

#### 3. Automate Daily Updates

```bash
# cron job: Run daily at 2 AM
# 0 2 * * * /path/to/update_network_diagram.sh

cat > update_network_diagram.sh <<'EOF'
#!/bin/bash

cd /opt/network_diagrams

# Fetch latest monitoring data
python3 monitoring_to_network.py

# Generate updated diagram
lualatex -interaction=nonstopmode live_network.tex

# Copy to web server
cp live_network.pdf /var/www/html/network_docs/

# Send notification
echo "Network diagram updated: $(date)" | \
    mail -s "Daily Network Diagram Update" ops-team@company.com

EOF

chmod +x update_network_diagram.sh
```

---

## Tips for All Workflows

### 1. Version Control

Always keep your network data in version control:

```bash
git init
git add *.json *.tex
git commit -m "Initial network documentation"
git tag -a v1.0 -m "Production network baseline"
```

### 2. Automation

Use Make for consistent builds:

```makefile
all: overview.pdf dmz.pdf internal.pdf

%.pdf: %.tex network.json
	lualatex $<

.PHONY: clean
clean:
	rm -f *.aux *.log *.pdf
```

### 3. Documentation

Keep a CHANGELOG.md:

```markdown
# Network Changes Log

## 2024-11-16
- Added new DMZ firewall
- Reconfigured routing tables
- Updated firewall rules

## 2024-11-10
- Removed decommissioned servers
- Added new database replica
```

### 4. Security

Never commit sensitive data:

```bash
# .gitignore
*_prod.json
*_sensitive.json
credentials/
*.env
```

---

## Need Help?

- Check the main [README.md](README.md) for feature documentation
- See [examples/README.md](examples/README.md) for format details
- Review [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
- Check [TODO_TRACKER.md](TODO_TRACKER.md) for upcoming features

