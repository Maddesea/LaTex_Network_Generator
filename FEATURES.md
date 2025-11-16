# Complete Feature Catalog - LaTeX Network Diagram Generator

This document catalogs all 60+ threat intelligence and visualization commands available in the system.

---

## Table of Contents

1. [CVSS Vulnerability Scoring](#cvss-vulnerability-scoring) (5 commands)
2. [MITRE ATT&CK Framework](#mitre-attck-framework) (7 commands)
3. [IOC & Threat Intelligence](#ioc--threat-intelligence) (9 commands)
4. [Kill Chain & Attack Progression](#kill-chain--attack-progression) (7 commands)
5. [Threat Actor Attribution](#threat-actor-attribution) (6 commands)
6. [Security Compliance](#security-compliance) (9 commands)
7. [Defensive Controls (Blue Team)](#defensive-controls-blue-team) (12 commands)
8. [Risk Analysis](#risk-analysis) (2 commands)
9. [Quick Threat Scenarios](#quick-threat-scenarios) (4 commands)
10. [Visual Indicators & Helpers](#visual-indicators--helpers) (8 commands)
11. [Color Schemes](#color-schemes) (7 themes)

---

## CVSS Vulnerability Scoring

### 1. `\markVulnerability{node}{CVE-ID}{score}`
**Purpose:** Basic vulnerability marker with CVE number and score
**Example:** `\markVulnerability{server1}{CVE-2024-1234}{9.8}`
**Output:** Red badge with CVE number and CRITICAL rating

### 2. `\markVulnerabilityCVSS{node}{CVE-ID}{base}{temporal}{environmental}`
**Purpose:** Enhanced vulnerability with full CVSS v3.1 scoring breakdown
**Example:** `\markVulnerabilityCVSS{server1}{CVE-2024-1234}{9.8}{9.5}{9.2}`
**Output:** Detailed box showing base, temporal, and environmental scores
**Color:** Auto-selects based on severity (Critical=red, High=orange, etc.)

### 3. `\drawCVSSMeter{x}{y}{score}{label}`
**Purpose:** Visual gauge/meter showing CVSS score
**Example:** `\drawCVSSMeter{10}{5}{9.8}{Web Server Vulnerability}`
**Output:** Horizontal progress bar with color gradient (green → red)
**Use Case:** Dashboard summary, executive presentations

### 4. `\drawCVSSBreakdown{x}{y}{base}{temporal}{env}{exploitability}{impact}`
**Purpose:** Detailed CVSS score table with all metrics
**Example:** `\drawCVSSBreakdown{0}{0}{9.8}{8.5}{9.2}{9.5}{8.7}`
**Output:** Professional table with all CVSS v3.1 components
**Use Case:** Technical reports, detailed analysis

### 5. `\cvssBadge{node}{score}`
**Purpose:** Compact CVSS score badge on node corner
**Example:** `\cvssBadge{server1}{7.5}`
**Output:** Small colored circle with score (HIGH/7.5)
**Use Case:** Minimalist diagrams, high node density

**Severity Thresholds:**
- 9.0-10.0: CRITICAL (dark red)
- 7.0-8.9: HIGH (orange-red)
- 4.0-6.9: MEDIUM (orange)
- 0.1-3.9: LOW (yellow)
- 0.0: NONE (blue)

---

## MITRE ATT&CK Framework

### 1. `\attackTechnique{node}{tactic}{technique-id}{description}`
**Purpose:** Display MITRE ATT&CK technique badge on node
**Example:** `\attackTechnique{server1}{credential-access}{T1110}{Brute Force}`
**Output:** Colored badge with T-code and name
**Tactics:** 12 color-coded tactics (see list below)

**Available Tactics:**
| Tactic | Color | Example T-Code |
|--------|-------|----------------|
| `reconnaissance` | Purple | T1595 |
| `initial-access` | Red-Purple | T1190 |
| `execution` | Red | T1059 |
| `persistence` | Red-Orange | T1053 |
| `privilege-escalation` | Orange | T1068 |
| `defense-evasion` | Yellow-Orange | T1055 |
| `credential-access` | Yellow | T1110 |
| `discovery` | Yellow-Green | T1083 |
| `lateral-movement` | Green | T1021 |
| `collection` | Blue-Green | T1005 |
| `command-and-control` | Blue | T1071 |
| `exfiltration` | Blue-Purple | T1041 |
| `impact` | Dark Purple | T1486 |

### 2. `\drawAttackMatrix{x}{y}`
**Purpose:** Legend showing all MITRE ATT&CK tactics with colors
**Example:** `\drawAttackMatrix{12}{8}`
**Output:** Compact legend of 12 tactics
**Use Case:** Diagram legend, reference guide

### 3. `\drawTTPProfile{x}{y}{actor-name}`
**Purpose:** TTP (Tactics, Techniques, Procedures) profile for threat actor
**Example:** `\drawTTPProfile{0}{5}{APT29}`
**Output:** Box listing common TTPs used by specified actor
**Use Case:** Threat actor analysis, attribution reports

### 4. `\drawAttackWithTechnique{source}{target}{T-code}{label}`
**Purpose:** Attack connection with MITRE technique label
**Example:** `\drawAttackWithTechnique{attacker}{server}{T1566.001}{Spearphishing}`
**Output:** Red attack arrow with technique badge
**Use Case:** Showing specific attack techniques on connections

### 5. `\drawAttackTimeline{x}{y}`
**Purpose:** Timeline of attack progression with timestamps
**Example:** `\drawAttackTimeline{10}{5}`
**Output:** Timeline bar with stages and timestamps
**Use Case:** Incident reports, temporal analysis

### 6. `\drawAttackChain{stage1}{stage2}{stage3}{stage4}`
**Purpose:** Multi-stage attack progression between nodes
**Example:** `\drawAttackChain{email}{workstation}{server}{database}`
**Output:** Connected nodes showing attack path
**Use Case:** Visualizing lateral movement and attack flow

### 7. `\correlateVulnExploit{node}{CVE}{score}{is-exploited}{exploit-name}`
**Purpose:** Link vulnerability to active exploit
**Example:** `\correlateVulnExploit{srv1}{CVE-2024-1234}{9.8}{yes}{Metasploit}`
**Output:** Vuln marker + exploit availability badge
**Use Case:** Risk prioritization, urgent patching

---

## IOC & Threat Intelligence

### 1. `\markIOCEnhanced{node}{type}{value}{reputation}{age-days}`
**Purpose:** Enhanced IOC marker with reputation score and age
**Example:** `\markIOCEnhanced{server}{malicious-ip}{192.0.2.1}{85}{3}`
**Output:** Badge with IOC type, value, reputation %, and age
**Reputation:** 0-100 (higher = more malicious)

### 2. `\markMaliciousIP{node}{ip-address}{country}{confidence}`
**Purpose:** IP-specific IOC with geolocation
**Example:** `\markMaliciousIP{attacker}{45.123.45.67}{Russia}{92}`
**Output:** IP badge with country flag emoji and confidence %
**Use Case:** Attribution, geolocation analysis

### 3. `\markFileHashIOC{node}{hash-type}{hash}{malware-name}`
**Purpose:** File hash IOC indicator
**Example:** `\markFileHashIOC{pc1}{SHA256}{a1b2c3d4e5f6...}{WannaCry}`
**Output:** Hash type + truncated hash + malware family
**Hash Types:** MD5, SHA1, SHA256, SHA512

### 4. `\markC2Server{node}{domain}{actor}`
**Purpose:** Command & Control server marker
**Example:** `\markC2Server{attacker}{evil.badactor.net}{APT29}`
**Output:** C2 badge with domain and associated threat actor
**Use Case:** Attribution, infrastructure tracking

### 5. `\drawIOCDashboard{x}{y}`
**Purpose:** IOC summary dashboard
**Example:** `\drawIOCDashboard{10}{5}`
**Output:** Box showing total IOCs by type (IPs, domains, hashes, URLs)
**Includes:** Counts, last update time, threat feed status

### 6. `\drawThreatFeedStatus{x}{y}{feed-name}{status}`
**Purpose:** Threat intelligence feed status indicator
**Example:** `\drawThreatFeedStatus{0}{0}{VirusTotal}{active}`
**Output:** Feed name with active/inactive status
**Status:** active, inactive, error, stale

### 7. `\drawIOCList{x}{y}`
**Purpose:** Comprehensive table of all IOCs in diagram
**Example:** `\drawIOCList{12}{8}`
**Output:** Formatted table with type, value, confidence
**Use Case:** Appendix, reference section

### 8. `\drawReputationScore{x}{y}{score}{entity}`
**Purpose:** Reputation meter for domain/IP
**Example:** `\drawReputationScore{0}{0}{75}{suspicious.domain.com}`
**Output:** Progress bar showing reputation (0=safe, 100=malicious)
**Use Case:** Risk assessment, triage

### 9. `\drawThreatSummary{x}{y}{count}`
**Purpose:** Overall threat summary dashboard
**Example:** `\drawThreatSummary{-8}{8}{0}`
**Output:** Summary of threats, vulnerabilities, IOCs detected
**Use Case:** Executive summary, overview

---

## Kill Chain & Attack Progression

### 1. `\drawKillChain{x}{y}{current-stage}`
**Purpose:** 7-stage Lockheed Martin Cyber Kill Chain
**Example:** `\drawKillChain{-8}{-5}{3}` (stage 3 = Delivery)
**Stages:** 0=Recon, 1=Weaponize, 2=Deliver, 3=Exploit, 4=Install, 5=C2, 6=Actions
**Output:** Horizontal bar with current stage highlighted
**Use Case:** Incident progression tracking

### 2. `\drawKillChainCompact{x}{y}{stage}`
**Purpose:** Compact kill chain progress bar
**Example:** `\drawKillChainCompact{0}{0}{5}`
**Output:** Smaller version suitable for dashboards
**Use Case:** Space-constrained diagrams

### 3. `\drawKillChainDetails{x}{y}{stage}`
**Purpose:** Detailed explanation of specific kill chain stage
**Example:** `\drawKillChainDetails{0}{5}{3}`
**Output:** Box with stage description and indicators
**Use Case:** Training materials, detailed analysis

### 4. `\drawAttackTimeline{x}{y}`
**Purpose:** Temporal attack progression
**Example:** `\drawAttackTimeline{10}{5}`
**Output:** Timeline with timestamps of each attack stage
**Use Case:** Incident forensics, temporal correlation

### 5. `\drawAttackPath{x}{y}`
**Purpose:** Tree visualization of attack paths
**Example:** `\drawAttackPath{12}{8}`
**Output:** Branching tree showing multiple attack vectors
**Use Case:** Complex attack scenarios

### 6. `\drawInfectionSpread{patient-zero}{victim-list}`
**Purpose:** Visualize malware/ransomware spread
**Example:** `\drawInfectionSpread{pc1}{pc2,pc3,server1}`
**Output:** Radiating infection lines from patient zero
**Use Case:** Ransomware outbreaks, worm propagation

### 7. `\drawAttackChain{node1}{node2}{node3}{node4}`
**Purpose:** Sequential attack chain between nodes
**Example:** `\drawAttackChain{email}{pc}{server}{db}`
**Output:** Curved arrows showing attack progression
**Use Case:** Lateral movement visualization

---

## Threat Actor Attribution

### 1. `\drawThreatActorProfile{x}{y}{name}{confidence}{campaign}{motivation}`
**Purpose:** Detailed threat actor dossier
**Example:** `\drawThreatActorProfile{0}{5}{APT29}{92}{SolarStorm}{Espionage}`
**Output:** Profile box with actor details, confidence %, campaign, motivation
**Confidence:** 0-100%

### 2. `\drawActorComparison{x}{y}`
**Purpose:** Compare multiple threat actors
**Example:** `\drawActorComparison{10}{5}`
**Output:** Table comparing tactics, tools, targets
**Use Case:** Threat landscape analysis

### 3. `\drawCampaignTracker{x}{y}{name}{start-date}{targets}`
**Purpose:** Track specific threat campaign
**Example:** `\drawCampaignTracker{0}{0}{SolarStorm}{2025-01-01}{Fortune 500}`
**Output:** Campaign timeline and target profile
**Use Case:** Long-term threat tracking

### 4. `\markThreatActorOrigin{node}{name}{country}{state-sponsored}`
**Purpose:** Mark threat actor with origin attribution
**Example:** `\markThreatActorOrigin{attacker}{APT29}{Russia}{yes}`
**Output:** Badge with actor name, origin, state-sponsored flag
**Use Case:** Geopolitical attribution

### 5. `\linkToThreatActor{attacker-node}{victim-nodes}`
**Purpose:** Draw connections from actor to all victims
**Example:** `\linkToThreatActor{apt28}{srv1,srv2,srv3}`
**Output:** Multiple attack arrows from actor to victims
**Use Case:** Campaign victim visualization

### 6. `\citeThreatIntel{x}{y}{source}{date}`
**Purpose:** Citation for threat intelligence source
**Example:** `\citeThreatIntel{0}{-8}{MISP}{2025-01-16}`
**Output:** Citation box with source and date
**Use Case:** Attribution credibility, documentation

---

## Security Compliance

### 1. `\drawNISTCompliance{x}{y}{ID%}{PR%}{DE%}{RS%}{RC%}`
**Purpose:** NIST Cybersecurity Framework 5 functions dashboard
**Example:** `\drawNISTCompliance{0}{5}{85}{90}{78}{82}{75}`
**Functions:** Identify, Protect, Detect, Respond, Recover
**Output:** Bar chart with % completion for each function
**Use Case:** NIST CSF compliance reporting

### 2. `\drawCISCompliance{x}{y}{IG1}{IG2}{IG3}`
**Purpose:** CIS Controls v8 implementation tracker
**Example:** `\drawCISCompliance{8}{5}{18}{35}{15}`
**Parameters:** Number of controls implemented per Implementation Group
**Output:** Progress bars for IG1 (18 max), IG2 (35 max), IG3 (20 max)
**Use Case:** CIS Controls assessment

### 3. `\drawPCIDSSCompliance{x}{y}{compliant-requirements}`
**Purpose:** PCI-DSS compliance status
**Example:** `\drawPCIDSSCompliance{0}{0}{12}`
**Parameters:** Number of compliant requirements (out of 12)
**Output:** Checklist of 12 PCI-DSS requirements
**Use Case:** Payment card security compliance

### 4. `\drawComplianceScorecard{x}{y}{framework}{score}{status}`
**Purpose:** General framework scorecard
**Example:** `\drawComplianceScorecard{0}{3}{ISO 27001}{78}{partial}`
**Status:** compliant, partial, non-compliant
**Use Case:** Any compliance framework (ISO 27001, SOC 2, HIPAA, etc.)

### 5. `\drawSecurityMetrics{x}{y}{critical}{high}{incidents}{mttr}`
**Purpose:** Security metrics dashboard
**Example:** `\drawSecurityMetrics{10}{8}{2}{5}{18}{22}`
**Metrics:** Critical vulns, High vulns, Incidents this month, MTTR (minutes)
**Output:** Box with key security KPIs
**Use Case:** Executive dashboards, SOC reports

### 6. `\drawControlEffectiveness{x}{y}{control-name}{effectiveness%}`
**Purpose:** Measure specific control effectiveness
**Example:** `\drawControlEffectiveness{0}{0}{Firewall}{92}`
**Output:** Progress bar showing control effectiveness
**Use Case:** Control assessment, audit evidence

### 7. `\drawComplianceComparison{x}{y}`
**Purpose:** Multi-framework comparison table
**Example:** `\drawComplianceComparison{12}{8}`
**Output:** Table comparing NIST, CIS, PCI-DSS, ISO 27001 scores
**Use Case:** Holistic compliance view

### 8. `\drawCoverageHeatmap{x}{y}`
**Purpose:** Security control coverage heatmap
**Example:** `\drawCoverageHeatmap{0}{5}`
**Output:** Grid showing coverage across categories
**Use Case:** Gap analysis, coverage visualization

### 9. `\drawSecurityStatus{x}{y}{overall-score%}`
**Purpose:** Overall security posture dashboard
**Example:** `\drawSecurityStatus{10}{8}{85}`
**Output:** Gauge showing overall security score with status
**Status:** <60=Poor, 60-75=Fair, 75-85=Good, >85=Excellent
**Use Case:** Executive summary, board presentations

---

## Defensive Controls (Blue Team)

### 1. `\markSecurityControl{node}{control-type}{status}`
**Purpose:** Mark active security control on node
**Example:** `\markSecurityControl{firewall}{Firewall}{active}`
**Status:** active, inactive, degraded
**Output:** Shield badge with control name

### 2. `\markIDS{node}{ids-name}{alert-count}`
**Purpose:** IDS/IPS monitoring indicator
**Example:** `\markIDS{router}{Snort}{12}`
**Output:** Badge showing IDS name and alert count
**Color:** Green (0 alerts), Orange (1-10), Red (>10)

### 3. `\markWAF{node}{waf-name}{blocked-requests}`
**Purpose:** Web Application Firewall status
**Example:** `\markWAF{webserver}{ModSecurity}{247}`
**Output:** WAF badge with blocked request count
**Use Case:** Web security monitoring

### 4. `\markEDR{node}{edr-product}{protection-status}`
**Purpose:** Endpoint Detection & Response status
**Example:** `\markEDR{workstation}{CrowdStrike}{protected}`
**Status:** protected, vulnerable, updating
**Output:** Shield icon with EDR product name

### 5. `\drawSegmentBoundary{x1}{y1}{width}{height}{label}`
**Purpose:** Network segmentation boundary box
**Example:** `\drawSegmentBoundary{-5}{-2}{10}{5}{DMZ}`
**Output:** Dashed colored box around nodes
**Use Case:** Show security zones, VLANs, trust boundaries

### 6. `\markSIEM{x}{y}{siem-name}{events-per-hour}`
**Purpose:** SIEM integration status
**Example:** `\markSIEM{-10}{8}{Splunk}{5000}`
**Output:** SIEM badge with event ingestion rate
**Use Case:** SOC monitoring, log aggregation

### 7. `\drawDefenseLayers{x}{y}`
**Purpose:** Defense-in-depth layer visualization
**Example:** `\drawDefenseLayers{12}{8}`
**Output:** Concentric circles showing security layers
**Layers:** Perimeter, Network, Host, Application, Data
**Use Case:** Architecture diagrams, defense posture

### 8. `\markHoneypot{node}{honeypot-type}`
**Purpose:** Mark node as honeypot/decoy
**Example:** `\markHoneypot{fake_ssh}{SSH Honeypot}`
**Output:** Honeypot icon with type
**Use Case:** Deception technology visualization

### 9. `\drawMonitoringCoverage{x}{y}{coverage%}`
**Purpose:** Monitoring coverage meter
**Example:** `\drawMonitoringCoverage{10}{5}{92}`
**Output:** Progress bar showing network monitoring coverage
**Use Case:** SOC dashboards, coverage gaps

### 10. `\markPatchStatus{node}{days-behind}{last-patch-date}`
**Purpose:** System patch status
**Example:** `\markPatchStatus{server}{3}{2025-01-10}`
**Output:** Badge showing patch age
**Color:** Green (0 days), Yellow (1-7), Orange (8-30), Red (>30)

### 11. `\markBackupStatus{node}{last-backup-date}{status}`
**Purpose:** Backup status indicator
**Example:** `\markBackupStatus{database}{2025-01-15}{current}`
**Status:** current, stale, failed, none
**Output:** Backup icon with date and status

### 12. `\markZeroTrust{node}{enabled}`
**Purpose:** Zero Trust architecture indicator
**Example:** `\markZeroTrust{server}{yes}`
**Output:** Badge indicating Zero Trust enforcement
**Use Case:** Zero Trust deployment visualization

---

## Risk Analysis

### 1. `\drawRiskMatrix{x}{y}`
**Purpose:** 5x5 Risk matrix (likelihood × impact)
**Example:** `\drawRiskMatrix{10}{8}`
**Output:** Grid showing risk levels (green/yellow/orange/red)
**Use Case:** Risk assessment, prioritization

### 2. `\calculateRiskScore{threat%}{vuln%}{asset%}{control%}`
**Purpose:** Calculate weighted risk score
**Example:** `\calculateRiskScore{80}{90}{95}{75}`
**Formula:** Threat(30%) + Vuln(30%) + Asset(25%) - Controls(15%)
**Output:** Numeric risk score (0-100)
**Use Case:** Automated risk calculation, prioritization

---

## Quick Threat Scenarios

### 1. `\scenarioRansomware{patient-zero}{victims}{ransom}`
**Purpose:** Complete ransomware outbreak scenario
**Example:** `\scenarioRansomware{pc1}{pc2,pc3,srv1}{3 BTC}`
**Output:** Infection spread + ransom demand + recovery info
**Includes:** Malware markers, encryption status, ransom note

### 2. `\scenarioAPT{entry-point}{attacker}{target}{actor}{campaign}`
**Purpose:** APT intrusion scenario
**Example:** `\scenarioAPT{srv1}{apt29}{database}{APT29}{SolarStorm}`
**Output:** Full attack chain with attribution and TTPs
**Includes:** Kill chain, MITRE techniques, IOCs

### 3. `\scenarioDDoS{attackers}{target}`
**Purpose:** DDoS attack visualization
**Example:** `\scenarioDDoS{bot1,bot2,bot3}{webserver}`
**Output:** Multiple attack vectors converging on target
**Includes:** Traffic volume, attack type, mitigation status

### 4. `\drawIncidentStatus{x}{y}{incident-id}{status}{severity}`
**Purpose:** Incident response tracking box
**Example:** `\drawIncidentStatus{10}{5}{INC-2025-042}{investigating}{Critical}`
**Status:** new, investigating, containment, remediation, closed
**Severity:** Low, Medium, High, Critical
**Output:** Formatted incident tracker

---

## Visual Indicators & Helpers

### 1. `\visualizeDDoS{attackers}{target}{severity}`
**Purpose:** DDoS attack visual
**Example:** `\visualizeDDoS{bot1,bot2,bot3}{srv1}{critical}`
**Output:** Multiple thick red arrows to target

### 2. `\visualizeSQLi{attacker}{database}`
**Purpose:** SQL injection attack visual
**Example:** `\visualizeSQLi{hacker}{db1}`
**Output:** Attack arrow with SQLi label

### 3. `\visualizeMalware{node}{malware-name}`
**Purpose:** Malware infection indicator
**Example:** `\visualizeMalware{pc1}{WannaCry}`
**Output:** Skull icon + malware name on node

### 4. `\visualizeExfiltration{source}{destination}{data-size}`
**Purpose:** Data exfiltration visualization
**Example:** `\visualizeExfiltration{server}{attacker}{500MB}`
**Output:** Thick outbound arrow with data volume

### 5. `\addThreatBadge{node}{severity}`
**Purpose:** Simple threat severity badge
**Example:** `\addThreatBadge{server}{high}`
**Severity:** critical, high, medium, low, info
**Output:** Colored circle in corner of node

### 6. `\annotateNode{node}{text}{position}`
**Purpose:** Add annotation to node
**Example:** `\annotateNode{server1}{Production}{above}`
**Position:** above, below, left, right
**Output:** Text label at specified position

### 7. `\addNodeMetadata{node}{text}`
**Purpose:** Add metadata below node
**Example:** `\addNodeMetadata{server1}{Ubuntu 22.04}`
**Output:** Small text under node

### 8. `\drawThreatIndicator{x}{y}{severity}{message}`
**Purpose:** Standalone threat warning box
**Example:** `\drawThreatIndicator{0}{5}{critical}{Breach Detected!}`
**Output:** Attention-grabbing alert box
**Use Case:** Major warnings, breach notifications

---

## Color Schemes

The system includes 7 professional color themes:

### 1. **Light Mode** (default)
**Use:** General purpose, bright colors
**Activation:** No command needed (default)

### 2. **Dark Mode**
**Use:** Night viewing, extended sessions
**Activation:** `\loadColorScheme{dark}`
**Features:** Muted backgrounds, bright accents

### 3. **Colorblind-Friendly**
**Use:** Accessibility (deuteranopia/protanopia safe)
**Activation:** `\loadColorScheme{colorblind}`
**Features:** Scientifically verified distinguishable colors

### 4. **High Contrast**
**Use:** Visual impairment, WCAG AAA compliant
**Activation:** `\loadColorScheme{highcontrast}`
**Features:** Maximum contrast ratios

### 5. **Grayscale**
**Use:** Black & white printing
**Activation:** `\loadColorScheme{grayscale}`
**Features:** Distinguishable shades of gray

### 6. **Cyberpunk**
**Use:** Presentations, demos
**Activation:** `\loadColorScheme{cyberpunk}`
**Features:** Neon colors, futuristic aesthetic

### 7. **Solarized**
**Use:** Developer preference
**Activation:** `\loadColorScheme{solarized}`
**Features:** Balanced contrast, professional look

---

## Feature Statistics

- **Total Commands:** 60+
- **Threat Intelligence:** 38 commands
- **Defensive Controls:** 12 commands
- **Compliance:** 9 commands
- **Color Themes:** 7 schemes
- **MITRE ATT&CK:** 12 tactics supported
- **Compliance Frameworks:** 5+ frameworks
- **IOC Types:** 4 types (IP, domain, hash, URL)
- **Kill Chain Stages:** 7 stages (Lockheed Martin model)

---

## Quick Command Index

**Most Used Commands:**
1. `\markVulnerabilityCVSS` - Vulnerability with full CVSS scoring
2. `\attackTechnique` - MITRE ATT&CK technique badge
3. `\markMaliciousIP` - IP IOC with geolocation
4. `\drawKillChain` - Kill chain progression
5. `\markEDR` - Endpoint protection status
6. `\drawNISTCompliance` - NIST CSF dashboard
7. `\drawSecurityStatus` - Overall security posture
8. `\scenarioRansomware` - Quick ransomware scenario

**Most Complex Commands:**
1. `\drawThreatActorProfile` - Complete actor dossier
2. `\drawComplianceComparison` - Multi-framework comparison
3. `\scenarioAPT` - Full APT scenario with attribution
4. `\drawAttackTimeline` - Temporal attack analysis
5. `\drawThreatSummary` - Comprehensive threat overview

---

**See also:**
- [README.md](README.md) - Main documentation
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Copy-paste command examples
- [templates/](templates/) - Ready-to-use diagram templates
- [examples/](.) - example_*.tex files for demonstrations

---

*Last Updated: 2025-01-16*
*Version: 2.0 (Agent 5 Enhancements Complete)*
