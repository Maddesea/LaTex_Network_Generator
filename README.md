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

### Specialized Network Appliances (NEW!)

| Command | Description | Visual |
|---------|-------------|--------|
| `\createProxy` | Proxy server | Purple rectangle |
| `\createProxyWithType` | Proxy with type | Shows forward/reverse |
| `\createVPN` | VPN endpoint | Trapezium shape in green |
| `\createVPNWithProtocol` | VPN with protocol | Shows IPSec/OpenVPN/etc. |
| `\createDNS` | DNS server | Ellipse shape |
| `\createDNSWithZone` | DNS with zone info | Shows domain zones |

### Node Status System (NEW!)

| Command | Description | Status Types |
|---------|-------------|--------------|
| `\addNodeStatus` | Add status indicator | online, offline, degraded, maintenance |
| `\addNodeStatusWithLabel` | Status with label | Colored badge with text |
| `\createServerWithStatus` | Server with status | Combined creation command |

**Status Colors:**
- **Online**: Green dot (operational)
- **Offline**: Gray dot (unavailable)
- **Degraded**: Orange dot (performance issues)
- **Maintenance**: Blue dot (scheduled downtime)

### OS Badge System (NEW!)

| Command | Description | Supported OS |
|---------|-------------|--------------|
| `\addOSBadge` | Add OS badge | windows, linux, macos, unix, bsd |
| `\createServerWithOS` | Server with OS | Creates server + OS badge |
| `\createServerWithStatusAndOS` | Server with status & OS | All-in-one command |

**Example:**
```latex
\createServerWithStatusAndOS{web1}{192.168.1.10}{0}{0}{Web Server}{online}{linux}
```

### Service/Port Badge System (NEW!)

| Command | Description | Supported Services |
|---------|-------------|-------------------|
| `\addServiceBadge` | Add service badge | http, https, ssh, rdp, ftp, smtp, dns, sql |

**Common Services with Ports:**
- HTTP:80, HTTPS:443, SSH:22, RDP:3389, FTP:21, SMTP:25, DNS:53, SQL:3306

### Security & Compliance (NEW!)

| Command | Description | Options |
|---------|-------------|---------|
| `\addSecurityPosture` | Security level | high, medium, low, critical |
| `\addComplianceBadge` | Compliance standard | pci, hipaa, sox, iso27001, gdpr |

## Available Connection Types

### Basic Connections

| Command | Description | Visual Style |
|---------|-------------|--------------|
| `\drawConnection` | Normal connection | Solid line with arrow |
| `\drawEncryptedConnection` | Encrypted/VPN | Green with dots |
| `\drawSuspiciousConnection` | Suspicious traffic | Orange dashed |
| `\drawAttackConnection` | Active attack | Red thick line |
| `\drawBidirectional` | Two-way traffic | Arrows on both ends |

### Advanced Routing (NEW!)

**Bezier & Curved Paths:**
```latex
% Bezier curve with control points
\drawBezierConnection{srv1}{pc1}{2}{4}{6}{3}{Custom Route}

% Smart curved connection (avoids obstacles)
\drawSmartConnection{srv1}{pc1}{obstacle_node}{Routed}

% S-curve (smooth transition)
\drawSCurveConnection{srv1}{pc1}{3}{Data Flow}

% Loop connection (node to itself)
\drawLoopConnection{router1}{90}{2}{Loopback}
```

**Orthogonal Routing (Right Angles):**
```latex
% Orthogonal via point
\drawOrthogonalConnection{srv1}{pc1}{(4,2)}{Route}

% Horizontal then vertical
\drawOrthogonalHV{srv1}{pc1}{Connection}

% Vertical then horizontal
\drawOrthogonalVH{srv1}{pc1}{Connection}

% Manhattan routing with obstacle avoidance
\drawManhattanPath{srv1}{pc1}{up}{Route}  % Options: up, down, left, right
```

**Multi-Segment Paths:**
```latex
% Path through multiple waypoints
\drawPathThroughWaypoints{srv1}{(2,3) (4,5) (6,4)}{pc1}{Complex Route}

% Routed connection with midpoint
\drawRoutedConnection{srv1}{pc1}{5}{3}{Mid-Route}
```

### Bandwidth Visualization (NEW!)

```latex
% Log-scale bandwidth visualization
\drawConnectionWithBandwidthLog{srv1}{pc1}{100}{High BW}

% Bandwidth with utilization percentage (color-coded)
\drawConnectionWithUtilization{srv1}{pc1}{450}{1000}{Link}
% Green < 50%, yellow < 80%, red >= 80%

% Congestion indicators
\drawConnectionWithCongestion{srv1}{pc1}{high}{Congested Link}
% Levels: none, low, medium, high, critical

% Bundled connections (multiple connections shown as one)
\drawBundledConnection{srv1}{pc1}{15}{Aggregate}  % Shows "15 connections"
```

### Protocol-Specific Connections (NEW!)

```latex
% Protocol shortcuts with auto-styling
\drawHTTPConnection{web1}{client1}{Web Traffic}
\drawHTTPSConnection{web1}{client1}{Secure Web}
\drawSSHConnection{srv1}{admin1}{Remote Access}
\drawDNSConnection{dns1}{client1}{Lookup}
\drawSQLConnection{app1}{db1}{Database Query}

% Multi-protocol connection
\drawMultiProtocolConnection{srv1}{pc1}{HTTP,HTTPS,SSH}{Multi-Service}

% Custom protocol with color
\drawCustomProtocolConnection{srv1}{pc1}{RDP}{3389}{firewallRed}{Remote Desktop}
```

### Advanced Connection Features (NEW!)

**Specialized Connection Types:**
```latex
% VPN tunnel
\drawVPNTunnel{office1}{office2}{IPSec}

% Wireless connection
\drawWirelessConnection{ap1}{mobile1}{Corp-WiFi}

% Fiber optic (with light effect)
\drawFiberConnection{dc1}{dc2}{10Gbps}

% Serial/legacy connection
\drawSerialConnection{plc1}{scada1}{9600}

% Satellite link
\drawSatelliteLink{ship1}{base1}{500}  % 500ms latency

% Cross-connect/direct
\drawCrossConnect{srv1}{srv2}{Direct Link}
```

**Connection Health & QoS:**
```latex
% Health-based coloring
\drawConnectionHealth{srv1}{pc1}{good}{Link}      % Green
\drawConnectionHealth{srv1}{pc1}{degraded}{Link}  % Yellow
\drawConnectionHealth{srv1}{pc1}{poor}{Link}      % Orange
\drawConnectionHealth{srv1}{pc1}{down}{Link}      % Red

% QoS priority indicators
\drawConnectionWithQoS{srv1}{pc1}{critical}{Priority Traffic}
% Levels: critical, high, normal, low

% SLA monitoring
\drawConnectionWithSLA{srv1}{pc1}{99.95}{99.9}{Uplink}  % Uptime vs target

% Multi-metric labels
\drawConnectionMetrics{srv1}{pc1}{100}{5}{0.1}{2}
% Bandwidth, latency, packet loss, jitter
```

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

## Layout Algorithms (NEW!)

The system now includes comprehensive layout algorithms for automatic node positioning:

### Tiered/Layered Layouts

Perfect for N-tier architectures (web, app, database tiers):

```latex
% Setup horizontal tiered layout
\setupNTierLayout{horizontal}{3}  % 3-tier architecture

% Place nodes in tiers
\placeInTierH{web1}{0}{0}{2}  % tier 0, position 0, 2 nodes total in tier
\placeInTierH{web2}{0}{1}{2}  % tier 0, position 1
\placeInTierH{app1}{1}{0}{1}  % tier 1, single node
\placeInTierH{db1}{2}{0}{1}   % tier 2, single node

% Or use vertical layout
\setupNTierLayout{vertical}{4}
```

**Available Commands:**
- `\layoutTieredHorizontal{tier_count}{base_x}{base_y}{tier_spacing}{node_spacing}`
- `\layoutTieredVertical{tier_count}{base_x}{base_y}{tier_spacing}{node_spacing}`
- `\placeInTierH{node_id}{tier_num}{position}{total_in_tier}`
- `\placeInTierV{node_id}{tier_num}{position}{total_in_tier}`
- `\calculateTierSpacing{max_nodes}{min_spacing}{max_spacing}`

### Circular/Hub-and-Spoke Layouts

Ideal for star topologies and hub-centric networks:

```latex
% Setup circular layout: center at (0,0), radius 5, 8 nodes, start at 90°
\layoutCircularAuto{0}{0}{5}{8}{90}

% Place nodes around circle
\placeInCircle{node1}{0}  % position 0
\placeInCircle{node2}{1}  % position 1
% ... continues for all nodes

% Multi-ring layout (concentric circles)
\layoutMultiRing{0}{0}{3}{3}{2}  % 3 rings, base radius 3, increment 2
\placeInRing{inner1}{0}{0}{4}    % ring 0, position 0, 4 nodes in ring
\placeInRing{outer1}{2}{0}{8}    % ring 2, position 0, 8 nodes in ring

% Arc layout (partial circle)
\layoutArc{0}{0}{5}{6}{0}{180}   % center, radius, count, start angle, end angle
\placeInArc{node1}{0}
```

**Available Commands:**
- `\layoutCircularAuto{center_x}{center_y}{radius}{node_count}{start_angle}`
- `\placeInCircle{node_id}{position_index}`
- `\layoutMultiRing{center_x}{center_y}{ring_count}{base_radius}{radius_increment}`
- `\placeInRing{node_id}{ring_number}{position_in_ring}{total_in_ring}`
- `\layoutArc{center_x}{center_y}{radius}{node_count}{start_angle}{end_angle}`
- `\calculateCircularRadius{node_count}{min_node_spacing}`

### Grid Layouts

Perfect for data centers and server farms:

```latex
% Regular grid: base (0,0), 4 rows, 5 cols, spacing 3x4
\layoutGridAuto{0}{0}{4}{5}{3}{4}

% Place servers in grid
\placeInGrid{srv1}{0}{0}  % row 0, col 0
\placeInGrid{srv2}{0}{1}  % row 0, col 1

% Irregular grid (varying columns per row, auto-centered)
\layoutIrregularGrid{0}{0}{3}{4}
\placeInIrregularGrid{node1}{0}{0}{3}  % row 0, pos 0, 3 nodes in row
\placeInIrregularGrid{node2}{1}{0}{5}  % row 1, pos 0, 5 nodes in row

% Server rack layout (vertical stacking)
\layoutServerRack{0}{0}{42}{1}  % 42U rack, 1 unit height
\placeInRack{blade1}{5}   % rack unit 5
\placeInRack{blade2}{10}  % rack unit 10
```

**Available Commands:**
- `\layoutGridAuto{base_x}{base_y}{rows}{cols}{row_spacing}{col_spacing}`
- `\placeInGrid{node_id}{row}{col}`
- `\calculateGridDimensions{node_count}` - auto-calculates optimal rows/cols
- `\layoutIrregularGrid{base_x}{base_y}{row_spacing}{col_spacing}`
- `\placeInIrregularGrid{node_id}{row}{col}{total_in_row}`
- `\layoutServerRack{base_x}{base_y}{rack_units}{unit_height}`

### Tree Layouts

For hierarchical networks:

```latex
% Tree layout: root at (0,5), 3 levels, spacing 3x2
\layoutTreeAuto{0}{5}{3}{3}{2}

% Place nodes
\placeInTree{root}{0}{0}{1}     % level 0, position 0, 1 node in level
\placeInTree{child1}{1}{0}{3}   % level 1, position 0, 3 nodes in level
\placeInTree{child2}{1}{1}{3}
\placeInTree{child3}{1}{2}{3}

% Inverted tree (root at bottom)
\layoutInvertedTree{0}{-5}{3}{3}{2}
\placeInInvertedTree{root}{0}{0}{1}

% Calculate optimal spacing for tree
\calculateTreeSpacing{2}{4}{1.5}  % binary tree, depth 4, min spacing 1.5
```

**Available Commands:**
- `\layoutTreeAuto{root_x}{root_y}{levels}{level_spacing}{node_spacing}`
- `\placeInTree{node_id}{level}{position_in_level}{total_in_level}`
- `\layoutBinaryTree{root_x}{root_y}{depth}{h_spacing}{v_spacing}`
- `\layoutInvertedTree{root_x}{root_y}{levels}{level_spacing}{node_spacing}`
- `\calculateTreeSpacing{branching_factor}{depth}{min_spacing}`

### Collision Detection & Avoidance (NEW!)

Prevent overlapping nodes automatically:

```latex
% Register node dimensions for collision checking
\registerNodeBounds{srv1}{2.5}{1.5}  % width, height
\registerNodeBounds{srv2}{2.5}{1.5}

% Check if two nodes would overlap
\checkNodeOverlap{srv1}{0}{0}{srv2}{1}{1}  % sets \nodesoverlap to 1 or 0

% Calculate safe distance between nodes
\calculateSafeDistance{2.5}{1.5}{2.5}{1.5}{0.5}  % widths, heights, padding

% Adjust position to avoid collision
\avoidCollision{node1}{2}{2}{3}{3}  % sets \adjustedx, \adjustedy

% Snap to grid
\snapToGrid{2.3}{3.7}{1.0}  % snaps to nearest 1.0 unit, sets \snappedx, \snappedy

% Magnetic alignment
\magneticAlign{2.1}{3.0}{2.0}{3.0}{0.2}  % snaps if within 0.2 threshold
```

**Available Commands:**
- `\registerNodeBounds{node_id}{width}{height}`
- `\checkNodeOverlap{node1_id}{x1}{y1}{node2_id}{x2}{y2}`
- `\calculateSafeDistance{w1}{h1}{w2}{h2}{padding}`
- `\avoidCollision{node_id}{current_x}{current_y}{obstacle_x}{obstacle_y}`
- `\snapToGrid{x}{y}{grid_size}`
- `\magneticAlign{x}{y}{ref_x}{ref_y}{threshold}`

### Distribution Algorithms

Evenly space nodes across areas:

```latex
% Distribute 5 nodes along a line
\distributeAlongLine{5}{0}{0}{10}{5}  % count, start_x, start_y, end_x, end_y
\getDistributedPosition{0}  % sets \distx, \disty for position 0
\getDistributedPosition{1}  % position 1

% Distribute nodes in rectangular area
\distributeInArea{12}{0}{0}{10}{8}  % 12 nodes in area (0,0) to (10,8)
\getAreaPosition{0}   % sets \areax, \areay
\getAreaPosition{5}
```

### Subnet-Based Auto-Grouping (NEW!)

Automatically group nodes by IP subnet:

```latex
% Extract subnet from IP
\extractSubnet24{192.168.1.10}  % sets \subnetid to "192.168.1"
\extractSubnet16{10.0.1.5}      % sets \subnet16id to "10.0"

% Register node in subnet
\addNodeToSubnet{srv1}{192.168.1.10}{24}  % /24 subnet

% Get subnet color based on trust level
\getSubnetColor{192.168.1}  % sets \subnetcolor (green for private IPs)

% Draw subnet with auto-calculated trust level
\drawAutoSubnet{192.168.1.0}{(srv1) (srv2) (srv3)}

% Draw DMZ
\drawDMZ{dmz1}{(web1) (web2)}{Public Web Servers}

% Draw VLAN
\drawVLAN{100}{(node1) (node2)}{serverBlue}

% Draw trust boundary
\drawTrustBoundary{fw1.east}{dmz1.west}

% Draw geographic region
\drawRegion{us-east}{(srv1) (srv2)}{US East Region}{azureBlue}
```

**Available Commands:**
- `\extractSubnet24{ip_address}` - extracts /24 subnet
- `\extractSubnet16{ip_address}` - extracts /16 subnet
- `\addNodeToSubnet{node_id}{ip_address}{subnet_mask}`
- `\getSubnetColor{subnet_id}` - auto-assigns color by trust level
- `\drawAutoSubnet{subnet_cidr}{nodes}`
- `\drawDMZ{name}{nodes}{label}`
- `\drawVLAN{vlan_id}{nodes}{color}`
- `\drawTrustBoundary{start_coord}{end_coord}`
- `\drawRegion{name}{nodes}{region_label}{color}`

### Background Grids (NEW!)

Visual aids for layout:

```latex
% Simple configurable grid
\drawConfigurableGrid{1}{gray!20}{0.3pt}{-10}{-10}{10}{10}

% Graph paper style (major/minor grid)
\drawGraphPaperGrid{5}{1}{(-10,-10) grid (10,10)}

% Polar grid (for circular layouts)
\drawPolarGrid{0}{0}{8}{4}{12}  % center, radius, radial_steps, angular_steps

% Hexagonal grid
\drawHexGrid{0}{0}{1}{10}{10}   % origin, hex_size, rows, cols
```

### Dynamic Optimization (NEW!)

Auto-adjust layouts based on complexity:

```latex
% Calculate diagram complexity (0-100)
\calculateComplexity{25}{50}  % 25 nodes, 50 connections, sets \complexityscore

% Auto-adjust spacing
\autoAdjustSpacing{75}{3.5}    % complexity 75, base spacing 3.5, sets \adjustedspacing

% Calculate optimal bounds
\calculateDiagramBounds{30}{grid}  % 30 nodes, grid layout, sets \diagramwidth/height

% Scale to fit page
\scaleDiagramToPage{21}{29.7}{30}{40}  % page WxH, diagram WxH, sets \pagescale

% Optimize for output medium
\optimizeForPrint   % Thicker lines, larger fonts
\optimizeForScreen  % Lighter lines, smaller fonts

% Compact/expanded modes
\enableCompactMode{0.7}    % Reduce all spacing by 30%
\enableExpandedMode{1.3}   % Increase all spacing by 30%
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
**Completed:**
- [x] Tiered layout algorithm for N-tier architectures (horizontal/vertical)
- [x] Circular/hub-and-spoke layout with multi-ring support
- [x] Grid layout algorithms (regular, irregular, server rack)
- [x] Tree layout algorithms (standard, binary, inverted)
- [x] Collision detection and avoidance system
- [x] Subnet-based auto-grouping with IP parsing
- [x] Snap-to-grid and magnetic alignment
- [x] Distribution algorithms (line, area)
- [x] DMZ, VLAN, and trust boundary visualization
- [x] Geographic region grouping
- [x] Background grid systems (cartesian, polar, hexagonal)
- [x] Dynamic optimization and complexity scoring
- [x] Compact/expanded layout modes

**Remaining TODOs:**
- [ ] Force-directed graph layout integration (requires external tools)
- [ ] Multi-page diagram support for large networks
- [ ] Bezier curve auto-routing for connections
- [ ] Advanced path-finding algorithms (A*, Dijkstra)
- [ ] Grid layout for data center visualization

### Agent 4: Connections (`connection_renderer.tex`)
**Completed:**
- [x] Advanced connection routing (Bezier, smart curved, S-curves, loops)
- [x] Orthogonal routing (right angles, Manhattan paths)
- [x] Multi-segment paths through waypoints
- [x] Connection bundling for high-density areas
- [x] Bandwidth visualization with log-scale line thickness
- [x] Bandwidth utilization percentage with color coding
- [x] Congestion indicators (5 levels)
- [x] Protocol-specific connections (HTTP, HTTPS, SSH, DNS, SQL)
- [x] Multi-protocol connection labels
- [x] Custom protocol connections with colors
- [x] Connection health indicators (good/degraded/poor/down)
- [x] QoS priority visualization
- [x] SLA monitoring displays
- [x] Multi-metric connection labels
- [x] Specialized connections (VPN, wireless, fiber, serial, satellite)

**Remaining TODOs:**
- [ ] Animated flow direction indicators (requires animation package)
- [ ] A* or Dijkstra pathfinding for complex obstacle avoidance
- [ ] Interactive connection highlighting

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
