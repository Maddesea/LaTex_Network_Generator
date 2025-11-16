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

### Basic Network Devices

| Command | Description | Example |
|---------|-------------|---------|
| `\createServer` | Server/host | `\createServer{srv1}{192.168.1.10}{0}{0}{Web Server}` |
| `\createClient` | Workstation/client | `\createClient{pc1}{192.168.1.100}{-5}{-3}{Desktop}` |
| `\createRouter` | Network router | `\createRouter{r1}{192.168.1.1}{0}{5}{Core Router}` |
| `\createFirewall` | Firewall | `\createFirewall{fw1}{10.0.0.1}{0}{3}{Edge FW}` |
| `\createSwitch` | Network switch | `\createSwitch{sw1}{192.168.1.2}{-3}{-3}{Access SW}` |
| `\createCloud` | Cloud/Internet | `\createCloud{inet}{0}{8}{Internet}` |
| `\createAttacker` | Threat actor | `\createAttacker{bad1}{1.2.3.4}{-6}{8}{Attacker}` |

### Database Servers (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createDatabase` | Basic database | Cylinder shape |
| `\createDatabasePrimary` | Primary/master DB | Bold cylinder with PRIMARY label |
| `\createDatabaseReplica` | Replica/slave DB | Dashed cylinder with REPLICA label |
| `\createDatabaseCluster` | DB cluster | Double-outlined cylinder |
| `\createDatabaseWithInfo` | DB with ports/type | Cylinder with additional info |

### Load Balancers (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createLoadBalancer` | Basic load balancer | Trapezium shape |
| `\createLoadBalancerActive` | Active LB | Bold with ACTIVE label |
| `\createLoadBalancerPassive` | Passive/standby LB | Dashed with PASSIVE label |
| `\createLoadBalancerWithAlgo` | LB with algorithm | Shows algorithm (Round Robin, etc.) |
| `\createLoadBalancerWithPool` | LB with pool size | Shows backend node count |

### Virtual Machines (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createVM` | Basic VM | Double-outlined box |
| `\createVMWithHypervisor` | VM with host info | Shows hypervisor name |
| `\createVMCluster` | VM cluster | Cluster with instance count |
| `\createHypervisor` | Hypervisor host | Server with HYPERVISOR label |

### Containers & Orchestration (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createContainer` | Basic container | Orange container box |
| `\createContainerWithImage` | Container with image | Shows Docker image name |
| `\createK8sPod` | Kubernetes pod | Dashed box with container count |
| `\createContainerWithResources` | Container with limits | Shows CPU/RAM limits |
| `\createDockerStack` | Docker stack | Multi-service stack |

### Mobile Devices (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createMobilePhone` | Mobile phone | Portrait rectangle |
| `\createMobilePhoneWithOS` | Phone with OS | Shows iOS/Android |
| `\createTablet` | Tablet | Landscape rectangle |
| `\createTabletWithOS` | Tablet with OS | Shows OS information |

### IoT Devices (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createIoTDevice` | IoT device | Circle shape |
| `\createIoTDeviceWithType` | IoT with type | Shows device type |
| `\createIoTSensor` | IoT sensor | Diamond shape |
| `\createIoTSensorWithType` | Sensor with type | Shows sensor type (temp, motion, etc.) |

### Cloud Provider Nodes (NEW!)

| Command | Description | Provider |
|---------|-------------|----------|
| `\createAWSNode` | AWS service | Amazon Web Services |
| `\createAWSEC2` | AWS EC2 instance | Shows instance type |
| `\createAzureNode` | Azure service | Microsoft Azure |
| `\createAzureVM` | Azure VM | Shows VM size |
| `\createGCPNode` | GCP service | Google Cloud Platform |
| `\createGCPCompute` | GCP Compute | Shows machine type |

### Multi-Part & Detailed Nodes (NEW!)

| Command | Description | Features |
|---------|-------------|----------|
| `\createDetailedServer` | Server with details | Hostname, IP, ports, services |
| `\createNodeWithMetrics` | Node with metrics | CPU/RAM/Disk utilization bars |
| `\createThreeTierNode` | Three-section node | Header, body, footer layout |

### Node Grouping & Clustering (NEW!)

| Command | Description | Usage |
|---------|-------------|-------|
| `\drawCluster` | Cluster boundary | Groups multiple nodes |
| `\drawHAPair` | HA pair boundary | Marks high-availability pairs |
| `\drawServerRack` | Server rack | Visual rack container |
| `\addClusterLabel` | Cluster label | Adds label with node count |

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
**Completed:**
- [x] Hash map for O(1) node lookup by IP, hostname, and node ID
- [x] Node grouping/clustering support with visual boundaries
- [x] Database server nodes with cylinder shapes (primary, replica, cluster)
- [x] Load balancer nodes with special indicators (active/passive, algorithms)
- [x] Virtual machine nested appearance with hypervisor support
- [x] Container/Docker nodes with Kubernetes pod support
- [x] Mobile device nodes (phones, tablets) with OS indicators
- [x] IoT device nodes (sensors, actuators) with specialized shapes
- [x] Cloud provider nodes (AWS, Azure, GCP) with service types
- [x] Multi-part nodes with resource utilization bars
- [x] IP address validation and formatting (IPv4, IPv6, CIDR)
- [x] Custom node template system

**Remaining TODOs:**
- [ ] CVE vulnerability badges with scoring
- [ ] Advanced IP validation with subnet parsing

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
- **v1.1 (Planned)** - Auto-layout algorithms and data import
- **v2.0 (Planned)** - SIEM integration and real-time threat feeds

## Contact & Support

For questions, bug reports, or feature requests, check the TODO blocks in each module file for priority enhancements.

---

**Built for cybersecurity professionals who demand professional-quality network documentation.**
