  # Network Diagram Templates

This directory contains ready-to-use templates for common network diagram scenarios. Each template is fully documented and can be customized for your specific needs.

## Available Templates

### 1. **template_basic_network.tex** - Simple Network Diagram
**Use Case:** General purpose network documentation

**Includes:**
- 3-tier architecture (Web → App → Database)
- Internet connection through firewall
- Basic encrypted connections
- Clean, minimal design

**Best For:**
- Learning the system
- Simple infrastructure documentation
- Quick proof-of-concept diagrams

**Compile:**
```bash
pdflatex template_basic_network.tex
```

---

### 2. **template_attack_scenario.tex** - Cyber Attack Visualization
**Use Case:** Incident response, threat analysis, security training

**Includes:**
- Attacker node and attack vectors
- Vulnerability markers (CVSS scores)
- MITRE ATT&CK technique badges
- IOC indicators (malicious IPs)
- Kill chain progression tracker
- Incident status dashboard

**Customization Points:**
- Update CVE numbers and scores
- Modify MITRE ATT&CK techniques (T-codes)
- Change attacker origin and tactics
- Adjust kill chain stage

**Best For:**
- Post-incident reports
- Threat modeling exercises
- Security awareness training
- Red team exercise documentation

**Compile:**
```bash
pdflatex template_attack_scenario.tex
```

---

### 3. **template_compliance_report.tex** - Compliance Dashboard
**Use Case:** Audit reports, compliance documentation, security assessments

**Includes:**
- NIST Cybersecurity Framework dashboard
- CIS Controls v8 compliance tracking
- Security control inventory (EDR, WAF, patches, backups)
- Network segmentation boundaries
- Zero Trust indicators
- Multi-framework comparison
- Defense-in-depth layers

**Customization Points:**
- Update compliance scores in dashboard commands
- Modify security control statuses
- Adjust framework selection (NIST, CIS, PCI-DSS, ISO 27001)
- Change audit dates and statuses

**Best For:**
- Quarterly compliance reports
- Audit preparation materials
- Board-level security presentations
- Certification documentation (PCI-DSS, ISO 27001, SOC 2)

**Compile:**
```bash
pdflatex template_compliance_report.tex
```

---

### 4. **template_soc_monitoring.tex** - SOC Operations Dashboard
**Use Case:** Security operations, real-time monitoring, SOC reporting

**Includes:**
- SIEM integration visualization
- IDS/IPS alert tracking
- Active threat indicators
- IOC dashboard
- Incident tracking system
- Security metrics (MTTD, MTTR)
- Monitoring coverage analysis
- Active alerts summary box

**Customization Points:**
- Update event counts and alert numbers
- Modify incident IDs and statuses
- Adjust monitoring coverage percentages
- Change SIEM platform name and statistics

**Best For:**
- Daily SOC reports
- Shift handoff documentation
- Security metrics dashboards
- Executive security summaries

**Compile:**
```bash
pdflatex template_soc_monitoring.tex
```

---

## How to Use Templates

### Step 1: Copy Template
```bash
cp templates/template_basic_network.tex my_network.tex
```

### Step 2: Customize Content
Open `my_network.tex` in your editor and look for:
- `% CUSTOMIZE` comments - these mark areas to modify
- `[PLACEHOLDER]` text - replace with your values
- `XXX.XXX.XXX.XXX` - replace with real IP addresses
- `YYYY-MM-DD` - replace with actual dates

### Step 3: Modify Network Topology
- Add/remove nodes using `\createServer`, `\createClient`, etc.
- Adjust node positions (x, y coordinates)
- Update connections between nodes
- Modify labels and text

### Step 4: Update Threat Intelligence (if applicable)
- Change CVE numbers to real vulnerabilities
- Update MITRE ATT&CK technique IDs
- Modify CVSS scores
- Adjust compliance percentages

### Step 5: Compile
```bash
pdflatex my_network.tex
```

### Step 6: Iterate
- Review the PDF output
- Make adjustments to positions, labels, or content
- Recompile until satisfied

---

## Template Customization Guide

### Common Modifications

#### Changing Colors/Theme
Add after `\input{styles_config}`:
```latex
\loadColorScheme{dark}  % or colorblind, highcontrast, grayscale, etc.
```

#### Adjusting Diagram Size
Modify the scale parameter:
```latex
\begin{tikzpicture}[scale=0.8, transform shape, font=\sffamily]
%                          ↑ Change this (0.5 to 2.0)
```

#### Adding More Nodes
Follow the pattern:
```latex
\createServer{uniqueID}{x}{y}{Display Name}
```

#### Repositioning Elements
- Increase X → moves right
- Decrease X → moves left
- Increase Y → moves up
- Decrease Y → moves down

Grid spacing: Usually 3-4 units between nodes works well.

---

## Template Combinations

You can combine elements from multiple templates:

**Example:** Attack scenario + Compliance controls
1. Start with `template_attack_scenario.tex`
2. Add compliance dashboards from `template_compliance_report.tex`
3. Result: Attack scenario with compliance impact analysis

**Example:** SOC monitoring + Specific incident
1. Start with `template_soc_monitoring.tex`
2. Add attack chains from `template_attack_scenario.tex`
3. Result: Real-time SOC view of active incident

---

## Best Practices

1. **Start Simple:** Begin with the basic template, then add complexity
2. **Use Meaningful IDs:** Name nodes descriptively (web1, db_prod, fw_dmz)
3. **Test Often:** Compile after every major change
4. **Comment Your Code:** Use `%` comments to document custom changes
5. **Version Control:** Keep templates in git for easy rollback
6. **Modular Approach:** Break large networks into multiple diagrams

---

## Troubleshooting

### Problem: Nodes Overlap
**Solution:** Increase spacing between coordinates
```latex
% Before: nodes at (0,0) and (1,0)
% After:  nodes at (0,0) and (4,0)
```

### Problem: Compilation Errors
**Solution:** Check that all required .tex files are in the same directory:
- styles_config.tex
- node_definitions.tex
- network_layout.tex
- connection_renderer.tex
- threat_indicators.tex

### Problem: Missing Features
**Solution:** Ensure you're using the latest modules. Some templates require features from threat_indicators.tex that may not be in older versions.

### Problem: Text Overflow
**Solution:** Reduce font size or abbreviate labels
```latex
\node[font=\tiny] ...  % or \scriptsize, \footnotesize
```

---

## Contributing Templates

Have a useful template to share? Consider adding:
- Template file (.tex)
- Description in this README
- Example output (optional: .pdf or .png)
- List of customization points

---

## Template Matrix

| Template | Complexity | Use Case | Key Features | Time to Customize |
|----------|------------|----------|--------------|-------------------|
| basic_network | Low | Documentation | Clean, minimal | 5-10 min |
| attack_scenario | Medium | Incident response | Threats, MITRE ATT&CK | 15-30 min |
| compliance_report | Medium-High | Audits | Dashboards, metrics | 20-40 min |
| soc_monitoring | High | Operations | Real-time, alerts | 30-60 min |

---

**Need help?** See the main [README.md](../README.md) or [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) for complete command documentation.
