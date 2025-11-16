# LaTeX Network Diagram Generator

A professional, scalable network diagram generation system using LaTeX/TikZ, designed for cybersecurity visualization, network documentation, and threat analysis.

## Features

✅ **Professional Styling** - Publication-quality diagrams exceeding draw.io/Visio standards
✅ **Modular Architecture** - Separated concerns for parallel development
✅ **60+ Node Types** - Servers, databases, cloud, mobile, IoT, storage, security appliances
✅ **Pre-built Templates** - Instant 3-tier, DMZ, cloud hybrid, microservices, IoT architectures
✅ **Bulk Creation Utilities** - Generate rows, grids, and star topologies automatically
✅ **Advanced Visualizations** - Resource metrics, security status, OS badges, subnet boundaries
✅ **Scalable Output** - Support for A0 through A4 and custom page sizes
✅ **Rich Connection Types** - Encrypted, suspicious, attack, and bidirectional connections
✅ **TeXLive 2024/2025 Compatible** - Uses stable, widely-supported packages
### 🎨 **Visual Styling (60+ Features)**

#### Color Schemes & Accessibility
✅ **5 Color Schemes** - default, dark, colorblind-safe, monochrome, high-contrast
✅ **Colorblind Accessibility** - Research-based palettes for all vision types
✅ **Pattern Fills** - 6 pattern styles for B&W printing and accessibility
✅ **Dark Mode** - Full dark theme with optimized colors

#### Node Styles (20+ Variants)
✅ **Basic Styles** - server, client, router, firewall, switch, cloud, attacker
✅ **Gradient Effects** - vertical, radial, metallic, and glass gradients
✅ **Pattern Styles** - 6 accessibility patterns (vertical lines, horizontal, grid, dots, crosshatch)
✅ **Style Templates** - corporate, security, modern cloud, minimal, presentation

#### Icons & Badges
✅ **6 Built-in Icons** - server, laptop, phone, router, database, cloud
✅ **OS Badges** - Windows, Linux, macOS indicators
✅ **Status Badges** - online, offline, warning, critical alerts
✅ **Multiple Badges** - Support for 2-3 badges per node

### 🔗 **Connections (18+ Types)**

#### Basic & Secure
✅ **Standard Types** - normal, encrypted, suspicious, attack, bidirectional
✅ **Bandwidth Indicators** - 5 levels (low, medium, high, very high, congested)
✅ **Flow Animations** - Animated data flow with markers

#### Special Connection Types
✅ **VPN Tunnels** - Dashed tube effect for VPN links
✅ **Wireless** - Wave pattern for WiFi connections
✅ **Fiber Optic** - Light beam effect for fiber
✅ **Satellite Links** - Space-themed connections
✅ **Blocked Connections** - Firewall blocks
✅ **Load Balanced** - Dual-line load balancer connections
✅ **Curved Paths** - Bezier curves for complex topologies

### 📝 **Annotations & Metadata**

✅ **Callout Boxes** - info, warning, critical, success, note styles
✅ **Network Zones** - DMZ, internal, trusted, external boundaries
✅ **Metadata Boxes** - Diagram info, author, version tracking
✅ **Statistics Dashboards** - Network stats with live counts
✅ **Protocol Labels** - Inline protocol and port labeling

### 🎯 **Topology Templates**

✅ **3-Tier Architecture** - Auto-generates web/app/data tiers
✅ **Hub-and-Spoke** - Parameterized hub topology
✅ **Full Mesh** - Automatic mesh network creation

### 🎬 **Presentation Support**

✅ **Beamer Integration** - Progressive reveal animations
✅ **Slide Builds** - Step-by-step network evolution
✅ **Alert Styles** - Highlight critical systems
✅ **Opacity Control** - Dim/reveal for emphasis

### 🛠️ **Developer Tools**

✅ **9 Example Files** - Complete working examples
✅ **Compilation Scripts** - Automated build for Linux/Mac/Windows
✅ **Feature Validation** - 60+ feature test suite
✅ **Quick Reference** - 1-page command reference
✅ **Comprehensive Docs** - 1,000+ lines of documentation

### 🏗️ **Architecture**

✅ **Modular Design** - Separated concerns for parallel development
✅ **Scalable Output** - Support for A0 through A4 and custom sizes
✅ **Threat Visualization** - Security threat and attack indicators
✅ **TeXLive Compatible** - Works with TeXLive 2020-2025

## New in Version 2.0 🎉

**Agent 1: Styles & Visual Design - NOW COMPLETE!**

The styling system has been massively enhanced with 60+ new features:

### Quick Examples

```latex
% Use colorblind-safe palette
\useColorblindSafe

% Create gradient server with badges
\node[gradient server,
      pin={[badge linux]45:Linux},
      pin={[badge online]135:●}
     ] (web) at (0,0) {
     \serverIcon\\
     Web Server\\
     192.168.1.10
};

% Draw VPN connection with label
\draw[vpn tunnel] (siteA) -- (siteB)
     node[midway, above] {IPSec};

% Add network zone
\node[dmz zone, fit=(fw)(web)(mail)] {};

% Use topology template
\threeTierTemplate{w1}{w2}{w3}{a1}{a2}{a3}{d1}{d2}{d3}
```

### See It In Action

Check out the `examples/` directory for 9 complete working examples:
- Color schemes and accessibility
- Enterprise gradients and effects
- Security visualization with badges
- Multi-cloud architectures
- Beamer presentations
- Complete feature demonstrations

Run `./examples/compile_all.sh` to build all examples!

---

### 🆕 Advanced Analysis Features (v1.2)

✅ **Network Validation** - Automated IP conflict detection, port conflict checking, and connectivity validation
✅ **Auto-Documentation** - Generate network inventories, service catalogs, and topology descriptions automatically
✅ **Diagram Comparison** - Version diff visualization, change tracking, and configuration drift detection
✅ **Security Assessment** - Vulnerability scoring, attack surface analysis, threat modeling, and compliance gap analysis
✅ **Health Monitoring** - Real-time network health scoring (0-100) with automated issue detection
✅ **Security Dashboard** - Comprehensive security metrics dashboard with visual indicators

## Quick Start

**⚡ New to the project? Check out [QUICKSTART.md](QUICKSTART.md) for a 5-minute tutorial!**

### Prerequisites

```bash
# Install TeXLive (Ubuntu/Debian)
sudo apt-get install texlive-full

# Or install TeXLive (Fedora/RHEL)
sudo dnf install texlive-scheme-full

# Verify installation
pdflatex --version
```

### Option 1: Use Pre-built Templates (Fastest!)

```latex
% In your .tex file
\input{topology_templates}

% Create instant architectures:
\createThreeTierApp{myapp}{192.168}                   % 3-tier web app
\createSecureDMZ{corp}{203.0.113}{10.0.0}{192.168.1}  % DMZ with security
\createHybridCloud{hybrid}{172.16.0}{aws}             % Cloud hybrid
\createMicroservices{api}{10.100}                     % Microservices
\createSmartHome{home}{192.168.50}                    % IoT smart home
```

### Option 2: Compile Example Diagrams

```bash
# Basic example
pdflatex network_diagram_generator.tex

# Advanced features (45+ nodes, all types)
pdflatex example_complete_network.tex

# Templates demonstration
pdflatex example_templates.tex
```

### Option 3: Bulk Creation Utilities

```latex
% Create 5 web servers automatically
\createNodeRow{server}{web}{192.168.10}{3}{5}{Web Server}

% Create 3x3 grid of servers
\createNodeGrid{server}{node}{192.168.20}{0}{0}{3}{3}

% Create star topology (1 switch, 8 clients)
\createStarTopology{office}{switch}{client}{192.168.1}{8}
```

## File Structure

```
network_diagram_generator.tex  # Main entry point
├── styles_config.tex          # Visual styling and color schemes (20+ styles)
├── node_definitions.tex       # Network asset rendering (60+ node types)
├── topology_templates.tex     # Pre-built architecture templates (NEW!)
├── network_layout.tex         # Layout algorithms and positioning
├── connection_renderer.tex    # Connection drawing and flows
├── threat_indicators.tex      # Security threat visualization
├── network_data.tex           # Actual network topology data
├── QUICKSTART.md              # 5-minute tutorial (NEW!)
├── example_complete_network.tex   # Comprehensive 45+ node example
├── example_advanced_nodes.tex     # Advanced features demo
├── example_templates.tex      # Template usage examples (NEW!)
└── example_advanced_analysis.tex  # Advanced analysis demo (NEW!)
```

## Advanced Features Usage

### Network Validation & Health Monitoring

```latex
% Register IPs for conflict detection
\registerIPAddress{web1}{192.168.1.10}
\registerIPAddress{web2}{192.168.1.10}  % Detects duplicate!

% Register ports for conflict checking
\registerNodePort{web1}{192.168.1.10}{80}{nginx}

% Generate validation report
\generateValidationReport{-9}{-5}

% Display network health score (0-100)
\displayNetworkHealth{8}{6}
```

### Auto-Documentation

```latex
% Generate network inventory
\generateNetworkInventory{0}{9}{Network Inventory}

% Create service catalog
\generateServiceCatalog{-9}{5}

% Generate topology description
\generateTopologyDescription{0}{0}{Production Network}

% Export summary card
\generateNetworkSummaryCard{0}{9}{My Network}
```

### Diagram Comparison & Version Tracking

```latex
% Register nodes in version 1
\registerNodeV1{web1}{192.168.1.10}{WebServer}{server}

% Register nodes in version 2
\registerNodeV2{web1}{192.168.1.20}{WebServer}{server}  % IP changed!

% Compare and highlight changes
\compareNode{web1}{\result}
\highlightModifiedNode{web1}

% Generate comparison report
\generateVersionComparison{0}{0}{v1.0}{v2.0}
```

### Security Assessment

```latex
% Register vulnerabilities
\registerVulnerability{web1}{CVE-2024-1234}{critical}{9.8}

% Register exposed services
\registerExposedService{web1}{443}{HTTPS}{public}

% Generate security reports
\generateVulnerabilityReport{0}{0}
\visualizeAttackSurface{0}{5}
\generateSecurityDashboard{0}{9}

% Add security badges to nodes
\addVulnerabilityBadge{web1}{3}{critical}
\markInternetExposed{web1}
```

### Complete Analysis Example

See `example_advanced_analysis.tex` for a full demonstration including:
- IP conflict detection
- Vulnerability tracking
- Security assessment
- Auto-generated documentation
- Health monitoring dashboard

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

### Basic Node Types

| Command | Description | Example |
|---------|-------------|---------|
| `\createServer` | Server/host | `\createServer{srv1}{192.168.1.10}{0}{0}{Web Server}` |
| `\createClient` | Workstation/client | `\createClient{pc1}{192.168.1.100}{-5}{-3}{Desktop}` |
| `\createRouter` | Network router | `\createRouter{r1}{192.168.1.1}{0}{5}{Core Router}` |
| `\createFirewall` | Firewall | `\createFirewall{fw1}{10.0.0.1}{0}{3}{Edge FW}` |
| `\createSwitch` | Network switch | `\createSwitch{sw1}{192.168.1.2}{-3}{-3}{Access SW}` |
| `\createCloud` | Cloud/Internet | `\createCloud{inet}{0}{8}{Internet}` |
| `\createAttacker` | Threat actor | `\createAttacker{bad1}{1.2.3.4}{-6}{8}{Attacker}` |

### Database Nodes (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createDatabase` | Basic database server | Cylinder shape, teal color |
| `\createDatabasePrimary` | Primary database | Bold cylinder with "PRIMARY" label |
| `\createDatabaseReplica` | Replica database | Light cylinder with "REPLICA" label |
| `\createDatabaseCluster` | Database cluster | Double-border cylinder with "CLUSTER" label |

**Example:**
```latex
\createDatabasePrimary{db1}{10.0.3.10}{0}{0}{PostgreSQL-Primary}
\createDatabaseReplica{db2}{10.0.3.11}{2}{0}{PostgreSQL-Replica}
```

### Load Balancer Nodes (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createLoadBalancer` | Basic load balancer | Trapezium shape, cyan color |
| `\createLoadBalancerActive` | Active LB with algorithm | Bold with algorithm display |
| `\createLoadBalancerPassive` | Standby/passive LB | Dashed border with "STANDBY" |

**Example:**
```latex
\createLoadBalancerActive{lb1}{10.0.4.10}{0}{0}{LB-Primary}{round-robin}
\createLoadBalancerPassive{lb2}{10.0.4.11}{2}{0}{LB-Standby}
\addLoadDistribution{lb1}{web1,web2,web3}
```

### Virtual Machine Nodes (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createVM` | Virtual machine | Double-border with host info |
| `\createHypervisor` | VM host/hypervisor | Large double-border box |
| `\createVMWithResources` | VM with CPU/RAM/Disk | Shows resource allocation |

**Example:**
```latex
\createHypervisor{esxi1}{10.0.0.10}{0}{5}{ESXi-01}{3}
\createVM{vm1}{10.0.1.10}{0}{3}{Web-VM}{esxi1}
\createVMWithResources{vm2}{10.0.1.11}{2}{3}{App-VM}{4vCPU}{8GB}{50GB}
```

### Container/Docker Nodes (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createContainer` | Docker container | Stacked appearance with image name |
| `\createPod` | Kubernetes pod | Dashed border with namespace |
| `\createContainerWithPorts` | Container with ports | Shows port mappings |

**Example:**
```latex
\createContainer{nginx1}{10.0.2.100}{0}{0}{nginx}{nginx:latest}
\createPod{pod1}{10.0.2.200}{2}{0}{web-pod}{production}
\createContainerWithPorts{api1}{10.0.2.101}{4}{0}{api}{3000:3000}
```

### Multi-Part Nodes (NEW!)

| Command | Description | Use Case |
|---------|-------------|----------|
| `\createDetailedServer` | Three-section node | Hostname, services, status |
| `\createNodeWithServices` | Service details | Shows ports and services |
| `\createNodeWithMetrics` | Resource metrics | CPU/Memory/Disk usage bars |
| `\createSecurityNode` | Security status | Vulnerability count, CVSS score |

**Example:**
```latex
% Node with resource metrics (CPU: 45%, Memory: 62%, Disk: 38%)
\createNodeWithMetrics{srv1}{192.168.1.10}{0}{0}{AppServer}{45}{62}{38}

% Security-focused node
\createSecurityNode{srv2}{192.168.1.20}{2}{0}{WebServer}{3}{6.5}{warning}
```

### Mobile and IoT Devices (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createMobilePhone` | Mobile phone | Tall rectangle with screen indicator |
| `\createTablet` | Tablet device | Wider rectangle |
| `\createLaptop` | Laptop computer | Client node with hinge indicator |
| `\createIoTDevice` | IoT device | Diamond shape |
| `\createSensor` | Sensor node | Circle shape |
| `\createSmartDevice` | Smart home device | Diamond with status |

**Example:**
```latex
\createMobilePhone{phone1}{192.168.60.101}{0}{0}{CEO-iPhone}{iOS 17}
\createLaptop{laptop1}{192.168.60.100}{2}{0}{Sales-Laptop}{john.doe}
\createIoTDevice{iot1}{192.168.70.10}{4}{0}{Smart-Thermostat}{HVAC}
\createSensor{sensor1}{192.168.70.11}{6}{0}{Temp-01}{Temperature}
```

### Cloud Provider Nodes (NEW!)

| Command | Description | Provider |
|---------|-------------|----------|
| `\createAWSNode` | AWS cloud service | Amazon Web Services |
| `\createAzureNode` | Azure cloud service | Microsoft Azure |
| `\createGCPNode` | GCP cloud service | Google Cloud Platform |

**Example:**
```latex
\createAWSNode{aws1}{0}{5}{AWS Cloud}{EC2, S3, RDS}
\createAzureNode{azure1}{3}{5}{Azure Cloud}{VMs, Blob Storage}
\createGCPNode{gcp1}{6}{5}{GCP Cloud}{Compute Engine}
```

### Network Appliances (NEW!)

| Command | Description | Use Case |
|---------|-------------|----------|
| `\createIPS` | IPS/IDS node | Intrusion Prevention/Detection |
| `\createProxy` | Proxy server | Forward/Reverse proxy |
| `\createWAF` | Web Application Firewall | Web security |
| `\createWirelessAP` | Wireless Access Point | WiFi with signal indicators |

**Example:**
```latex
\createIPS{ips1}{203.0.113.30}{0}{0}{IPS-01}{IPS Mode}
\createProxy{proxy1}{192.168.50.10}{2}{0}{Squid Proxy}{HTTP/HTTPS}
\createWAF{waf1}{203.0.113.10}{4}{0}{WAF-01}{OWASP Core}
\createWirelessAP{wap1}{192.168.60.1}{6}{0}{WAP-01}{CorpWiFi}
```

### Storage Nodes (NEW!)

| Command | Description | Storage Type |
|---------|-------------|--------------|
| `\createStorage` | Generic storage | Tape shape |
| `\createNAS` | Network Attached Storage | NFS/SMB protocols |
| `\createSAN` | Storage Area Network | iSCSI/FC protocols |

**Example:**
```latex
\createNAS{nas1}{192.168.40.10}{0}{0}{NAS-01}{50TB}{NFS/SMB}
\createSAN{san1}{192.168.40.20}{2}{0}{SAN-01}{100TB}{iSCSI}
\createStorage{backup1}{192.168.40.30}{4}{0}{Backup}{500TB}
```

### OS Badges and Status Indicators (NEW!)

```latex
% Add OS badge to any node
\addOSBadge{srv1}{ubuntu}
\addOSBadge{web1}{windows}
\addOSBadge{laptop1}{macos}

% Supported OS: windows, linux, macos, android, ios, ubuntu, redhat, centos

% Add status indicator
\addStatusIndicator{srv1}{online}
\addStatusIndicator{srv2}{degraded}
\addStatusIndicator{srv3}{offline}
% Status options: online, offline, degraded, maintenance
```

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
## Node Grouping and Clustering (NEW!)

### Cluster Boundaries
```latex
% Create cluster around nodes
\createCluster{webcluster}{Web Tier}{(srv1)(srv2)(srv3)}{0}{0}

% Create HA pair
\createHAPair{hapair}{HA Pair}{(lb1)}{(lb2)}

% Create server rack
\createRack{rack1}{Rack A}{(srv1)(srv2)(srv3)}{0}{0}
```

### Subnet Boundary Visualization (NEW!)

```latex
% Create subnet boundary with trust level
\createSubnet{subnet1}{Internal Network}{192.168.1.0/24}{(srv1)(srv2)(srv3)}{high}
% Trust levels: high (green), medium (yellow), low (red)

% Create DMZ boundary
\createDMZ{dmz}{DMZ Zone}{(web1)(lb1)(waf1)}
```

### IP Address Utilities (NEW!)

```latex
% Validate IP addresses
\validateIPv4{192.168.1.10}{\result}  % Returns 1 if valid
\validateIPv6{2001:db8::1}{\result}   % Returns 1 if valid
\validateIP{192.168.1.10}{\result}    % Returns 4 for IPv4, 6 for IPv6

% Extract subnet
\extractSubnet{192.168.1.100}{\subnet}  % Returns 192.168.1.0

% Extract subnet with variable CIDR
\extractSubnetCIDR{192.168.1.100}{16}{\subnet}  % Returns 192.168.0.0
% Supports /8, /16, /24

% Check if IPs in same subnet
\sameSubnet{192.168.1.10}{192.168.1.20}{\result}  % Returns 1 if same

% Check if IP is private
\isPrivateIP{192.168.1.10}{\result}  % Returns 1 for private, 0 for public
% Detects: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16

% Format CIDR notation
\formatCIDR{192.168.1.0}{24}{\cidr}  % Returns 192.168.1.0/24
```

### Hash Map for Node Lookup (NEW!)
```latex
% Register nodes in hash map for fast lookup
\registerNode{srv1}{192.168.1.10}{WebServer}

% Lookup by IP
\getNodeByIP{192.168.1.10}{\nodeid}

% Lookup by hostname
\getNodeByHostname{WebServer}{\nodeid}

% Extended registration with metadata
\registerNodeExtended{srv1}{192.168.1.10}{WebServer}{server}{Ubuntu 22.04}{online}

% Store additional metadata
\setNodeServices{srv1}{HTTP, HTTPS, SSH}
\setNodeSecurity{srv1}{3}{6.5}{PCI-DSS}
\assignNodeToCluster{srv1}{webcluster}
\setNodeParent{vm1}{hypervisor1}
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

### Agent 1: Styles & Aesthetics (`styles_config.tex`) ✅ **COMPLETE**
**Status:** ALL tasks completed + enhanced beyond scope

Implemented Features:
- ✅ Custom color scheme loader with 5 presets
- ✅ Colorblind-friendly alternative palettes (research-based)
- ✅ Dark mode theme support with full integration
- ✅ Gradient fills (vertical, radial, metallic, glass)
- ✅ Icon/image support (6 built-in TikZ icons + external)
- ✅ Badge/label support (OS + status indicators)
- ✅ Pattern fills for B&W printing (6 types)
- ✅ Beamer animation support
- ✅ Style template system
- ✅ Enhanced legend system
- ✅ Advanced connection styles (18+ types)
- ✅ Annotation callouts and zone boundaries
- ✅ Topology templates (3-tier, hub-spoke, mesh)
- ✅ Compilation scripts and validation suite

**Documentation:** STYLING_GUIDE.md, QUICK_REFERENCE_STYLING.md
**Examples:** 9 complete working examples in `examples/`

### Agent 2: Node System (`node_definitions.tex`)
**✅ ALL HIGH & MEDIUM PRIORITY FEATURES COMPLETED! (100%)**

**Core Systems:**
- [x] Hash map for O(1) node lookup by IP, hostname, and node ID
- [x] Extended hash map with metadata storage (OS, services, security)
- [x] IP address validation and formatting (IPv4, IPv6, CIDR)
- [x] Enhanced IP utilities (private IP detection, variable CIDR, subnet extraction)
- [x] Node grouping/clustering support (clusters, HA pairs, racks, subnets)

**Database & Infrastructure:**
- [x] Database server nodes with cylinder shape (primary, replica, cluster)
- [x] Load balancer nodes with special indicators (active/passive, algorithms)
- [x] Virtual machine nodes with nested appearance and hypervisors
- [x] Container/Docker nodes with stacked appearance and Kubernetes pods
- [x] Storage nodes (NAS, SAN, generic storage with capacity)

**Security & Monitoring:**
- [x] Multi-part nodes for detailed information display
- [x] Security-focused nodes with vulnerability counts and CVSS scores
- [x] Resource utilization nodes with CPU/Memory/Disk bars
- [x] Network appliances (IPS/IDS, Proxy, WAF)
- [x] OS badges for operating system identification
- [x] Status indicators (online, offline, degraded, maintenance)

**Mobile, IoT & Cloud:**
- [x] Mobile device nodes (phones, tablets, laptops)
- [x] IoT device nodes (sensors, smart devices)
- [x] Cloud provider-specific nodes (AWS, Azure, GCP)
- [x] Wireless access points with signal indicators

**Visualization Enhancements:**
- [x] Subnet boundary visualization with trust levels
- [x] DMZ (Demilitarized Zone) boundaries
- [x] Server rack visualization

**Low Priority Remaining:**
- [ ] Auto-arrange nodes within clusters (would require complex graph algorithms)
- [ ] Icon/image support inside nodes (requires external graphics)

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

## Documentation

📚 **Comprehensive Documentation:**
- **STYLING_GUIDE.md** - Complete styling reference (700+ lines)
- **QUICK_REFERENCE_STYLING.md** - 1-page quick reference
- **ARCHITECTURE.md** - System architecture details
- **TODO_TRACKER.md** - Development roadmap
- **examples/README.md** - Example documentation

## Version History

- **v2.0 (Current)** - Complete Agent 1 styling system with 60+ features
  - 5 color schemes with accessibility support
  - 20+ node style variants
  - 18+ connection types
  - Pattern fills for colorblind users
  - Beamer presentation support
  - Topology templates
  - Advanced annotations
  - Compilation tools

- **v1.0 (Foundation)** - Initial modular architecture with core features
- **v1.1 (Current)** - Enhanced node system with VMs, containers, databases, load balancers, clustering, IP validation, and hash map lookups
- **v1.2 (Planned)** - Auto-layout algorithms and data import
- **v2.0 (Planned)** - SIEM integration and real-time threat feeds
  - Basic node types and connections
  - Threat visualization
  - Security zones

- **v1.1 (Planned)** - Auto-layout algorithms and data import
- **v3.0 (Planned)** - SIEM integration and real-time threat feeds

## Contact & Support

For questions, bug reports, or feature requests, check the TODO blocks in each module file for priority enhancements.

---

**Built for cybersecurity professionals who demand professional-quality network documentation.**
