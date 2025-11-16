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

### Agent 1: Styles & Aesthetics (`styles_config.tex`)
**Priority TODOs:**
- [ ] Custom color scheme support via config file
- [ ] Colorblind-friendly alternative palettes
- [ ] Dark mode theme support
- [ ] Gradient fills for premium look
- [ ] Icon/image support inside nodes
- [ ] Badge/label support for OS type and status

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
**Priority TODOs:**
- [ ] CVSS score integration and visualization
- [ ] MITRE ATT&CK framework mapping
- [ ] IOC (Indicators of Compromise) visualization
- [ ] Attack kill chain progression display
- [ ] Threat actor attribution with confidence levels
- [ ] Real-time threat feed integration
- [ ] Security compliance dashboard (NIST, CIS, PCI-DSS)

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
- **v1.1 (Current)** - Enhanced node system with VMs, containers, databases, load balancers, clustering, IP validation, and hash map lookups
- **v1.2 (Planned)** - Auto-layout algorithms and data import
- **v2.0 (Planned)** - SIEM integration and real-time threat feeds

## Contact & Support

For questions, bug reports, or feature requests, check the TODO blocks in each module file for priority enhancements.

---

**Built for cybersecurity professionals who demand professional-quality network documentation.**
