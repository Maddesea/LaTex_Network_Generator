# Layout Engine Usage Guide

This guide demonstrates how to use the advanced layout features implemented in `network_layout.tex`.

## Table of Contents
1. [Tiered Layout](#tiered-layout)
2. [Circular Layout](#circular-layout)
3. [Grid Layout](#grid-layout)
4. [Tree Layout](#tree-layout)
5. [Force-Directed Layout](#force-directed-layout)
6. [Subnet Auto-Grouping](#subnet-auto-grouping)
7. [Collision Detection](#collision-detection)
8. [Multi-Page Diagrams](#multi-page-diagrams)
9. [Dynamic Optimization](#dynamic-optimization)
10. [Zoom and Detail Levels](#zoom-and-detail-levels)

---

## Tiered Layout

Perfect for N-tier architectures (web applications, enterprise systems).

### Basic Usage
```latex
% Configure 4-tier layout
\layoutTiered{4}{vertical}{7cm}

% Calculate position for a web server (tier 2, position 1 of 3)
\calcTierPosition{2}{1}{3}{\webX}{\webY}
\node[server] at (\webX, \webY) {Web Server 1};
```

### Auto-Assignment by Node Type
```latex
% Automatically assign nodes to tiers based on type
\assignNodeTier{firewall}    % → Tier 1
\assignNodeTier{web}          % → Tier 2
\assignNodeTier{database}     % → Tier 3

% Supported types: external, firewall, dmz, web, app, application, database, data, backend
```

### Optimal Spacing Calculation
```latex
% Calculate optimal spacing based on node count
\calcOptimalTierSpacing{15}{\optimalSpacing}
% Result: spacing scaled based on 15 nodes (5cm - 10cm range)
```

---

## Circular Layout

Ideal for hub-and-spoke networks, star topologies.

### Simple Circular Layout
```latex
% Position 8 nodes in a circle
\layoutCircular{0}{0}{5}{8}{0}  % center (0,0), radius 5, 8 nodes, start at 0°

% Position individual nodes
\calcCircularAngle{0}{8}{0}{\angleA}
\positionOnCircle{0}{0}{5}{\angleA}{nodeA}
\node[server] at (nodeA) {Server A};
```

### Optimal Radius Calculation
```latex
% Calculate optimal radius for 12 nodes with 2cm minimum spacing
\calcOptimalRadius{12}{2}{\radius}
% Result: radius = (12 * 2) / (2π) ≈ 3.82 cm
```

### Concentric Circles
```latex
% Create multiple concentric rings
\layoutConcentricCircles{0}{0}{4}{3}{6}  % 3 circles, 6 nodes each
% Inner circle: radius 4
% Middle circle: radius 6
% Outer circle: radius 8
```

### Arc-Based Positioning
```latex
% Position nodes on a partial arc (180° arc from 0° to 180°)
\positionOnArc{0}{0}{5}{0}{180}{0.25}{node1}  % 25% along arc
\positionOnArc{0}{0}{5}{0}{180}{0.75}{node2}  % 75% along arc
```

---

## Grid Layout

Perfect for data centers, server farms.

### Regular Grid
```latex
% 4x6 grid starting at (0,0) with 3cm spacing
\layoutGrid{0}{0}{3}{3}{4}{6}

% Calculate position for server at row 2, column 3
\calcGridPosition{2}{3}{3}{3}{0}{0}{\srvX}{\srvY}
\node[server] at (\srvX cm, \srvY cm) {Server 2-3};
```

### Auto-Calculate Grid Dimensions
```latex
% Calculate grid for 24 nodes with 1.5 aspect ratio (wider)
\calcGridDimensions{24}{1.5}{\rows}{\cols}
% Result: 4 rows × 6 columns
```

### Server Rack Visualization
```latex
% Draw a 42U server rack
\drawServerRack{rack1}{0}{0}{2}{8}{42}{Rack A}
% Parameters: name, x, y, width, height, rack units, label
```

### Blade Server Enclosure
```latex
% Draw blade enclosure with 16 blades
\drawBladeEnclosure{blade1}{5}{3}{16}{Blade Chassis 1}
% Shows individual blade slots in a compact view
```

---

## Tree Layout

For hierarchical networks, organizational structures.

### Binary Tree
```latex
% Configure tree layout
\layoutTree{0}{0}{4}{3}{false}  % root at (0,0), inverted=false

% Position left and right children
\calcBinaryTreePosition{1}{1}{0}{0}{2}{\leftX}{\leftY}   % left child
\calcBinaryTreePosition{1}{0}{0}{0}{2}{\rightX}{\rightY} % right child
```

### N-ary Tree (Any Branching Factor)
```latex
% Position 5 children under a parent node
\foreach \i in {0,...,4} {
    \calcNaryTreePosition{0}{0}{\i}{5}{2}{\childX}{\childY}
    \node[server] at (\childX, \childY) {Child \i};
}
```

### Inverted Tree (Root at Bottom)
```latex
\layoutTree{0}{0}{4}{3}{true}  % inverted=true
% Tree grows upward from root
```

### Tree Balancing
```latex
% Calculate center of subtree for balanced positioning
\calcSubtreeCenter{-5}{5}{\centerX}
% Centers parent above children at x=-5 and x=5
```

---

## Force-Directed Layout

Physics-based organic layouts.

### Fruchterman-Reingold Algorithm
```latex
% Initialize force-directed layout
\layoutForceDirected{20}{100}{15}{15}  % 20 nodes, 100 iterations, 15×15 area

% Calculate repulsive force between two nodes
\calcRepulsiveForce{0}{0}{3}{4}{2}{\fx}{\fy}
% Nodes at (0,0) and (3,4), spring constant k=2

% Calculate attractive force (for connected nodes)
\calcAttractiveForce{0}{0}{3}{4}{2}{\fx}{\fy}
```

### External Tool Integration
```latex
% Export positions for GraphViz/networkx processing
\exportPositionsForExternal{positions.csv}

% Import calculated positions
\importPositionsFromExternal{optimized_positions.csv}
```

---

## Subnet Auto-Grouping

Automatically group nodes by IP subnet with color-coding.

### IP Address Parsing
```latex
% Parse IP address into octets
\parseIPAddress{192.168.1.100}{\octA}{\octB}{\octC}{\octD}
% Result: octA=192, octB=168, octC=1, octD=100
```

### Subnet Calculation
```latex
% Calculate subnet ID from IP and CIDR
\calcSubnetID{192.168.1.100}{24}{\subnetID}
% Result: 192.168.1.0/24

\calcSubnetID{10.50.30.15}{16}{\subnetID}
% Result: 10.50.0.0/16
```

### Auto-Colored Subnet Boundaries
```latex
% Draw subnet with automatic trust-level coloring
\drawAutoSubnet{192.168.1.0/24}{(web1)(web2)(web3)}{DMZ Web Servers}
% Private IP (192.168.x.x) → Green (high trust)
% Public IP → Red (low trust)
```

### Nested Subnets (VLAN Support)
```latex
% Draw overlapping subnets
\drawNestedSubnet{10.0.0.0/8}{10.50.0.0/16}{(srv1)(srv2)}{Finance VLAN}
```

### Private IP Detection
```latex
% Check if IP is private (RFC 1918)
\isPrivateIP{192.168.1.1}{\result}  % Result: 1 (private)
\isPrivateIP{8.8.8.8}{\result}      % Result: 0 (public)
```

---

## Collision Detection

Prevent overlapping nodes automatically.

### Check for Collisions
```latex
% Check if two nodes collide
\checkNodeCollision{0}{0}{2}{2}{1}{1}{\collision}
% Nodes at (0,0) and (2,2) with radii 1 and 1
% Result: 1 if collision, 0 if safe
```

### Auto-Avoid Collisions
```latex
% Adjust position to avoid collision
\avoidCollision{0}{0}{1}{1}{\newX}{\newY}
% Moves from (0,0) away from collision at (1,1)
```

### Snap to Grid
```latex
% Snap position to 1cm grid
\snapToGrid{3.7}{5.2}{1}{\gridX}{\gridY}
% Result: (4, 5)
```

### Magnetic Alignment
```latex
% Align to nearby node if within threshold
\magneticAlign{3.8}{5.1}{4}{5}{0.5}{\alignedX}{\alignedY}
% If within 0.5cm, snaps to (4, 5)
```

### Even Distribution
```latex
% Distribute 12 nodes in 10×8 area
\distributeNodesInArea{12}{10}{8}{0}{0}
% Calculates optimal grid: 4 cols × 3 rows
```

---

## Multi-Page Diagrams

For very large networks that don't fit on one page.

### Basic Multi-Page Setup
```latex
% Configure 50 nodes, 20 per page
\layoutMultiPage{50}{20}{2}  % overlap margin = 2cm

% Calculate which page a node belongs to
\calcNodePage{35}{20}{\pageNum}  % Result: page 2
```

### Cross-Page References
```latex
% Draw reference to another page
\drawPageReference{5}{10}{3}{Database Cluster}{to}
% Arrow pointing TO page 3

\drawPageReference{5}{10}{1}{From Firewall}{from}
% Arrow FROM page 1
```

### Page Navigation
```latex
% Draw page map/navigator
\drawOverviewPage{5}{2}  % 5 total pages, currently on page 2
% Shows thumbnail nav with current page highlighted
```

### Page Headers
```latex
% Add header with navigation
\drawPageHeader{2}{5}{Corporate Network Topology}
% Page 2 of 5, with prev/next indicators
```

### Global Coordinates Across Pages
```latex
% Store coordinate for use across pages
\createGlobalCoordinate{mainRouter}{0}{0}

% Retrieve on different page
\useGlobalCoordinate{mainRouter}{\x}{\y}
```

---

## Dynamic Optimization

Automatically optimize layouts based on complexity.

### Complexity Scoring
```latex
% Calculate complexity score (0-100)
\calcComplexityScore{50}{120}{\score}
% 50 nodes, 120 connections → score ≈ 55
```

### Auto-Adjust Spacing
```latex
% Increase spacing for complex diagrams
\autoAdjustSpacing{75}{3}{\newSpacing}
% Complexity 75 → scales 3cm to ~4.1cm
```

### Density-Based Optimization
```latex
% Optimize based on node density
\optimizeLayout{100}{20}{15}
% 100 nodes in 20×15 area → calculates optimal scaling
```

### Display Mode Optimization
```latex
% Optimize for print
\setDisplayMode{print}  % Thicker lines, larger fonts

% Optimize for screen
\setDisplayMode{screen}  % Thinner lines, smaller fonts
```

### Responsive Output Sizes
```latex
% Set output size
\setOutputSize{a3}     % A3 paper (29.7×42 cm)
\setOutputSize{letter} % US Letter
\setOutputSize{screen} % 16:9 aspect ratio
```

---

## Zoom and Detail Levels

Control level of detail based on zoom level.

### Set Zoom Level
```latex
% Normal zoom
\setZoomLevel{1.0}

% 2x zoom (show more detail)
\setZoomLevel{2.0}

% Zoom out (less detail)
\setZoomLevel{0.5}
```

### Conditional Detail Rendering
```latex
% Show detail only if zoomed in enough
\shouldShowDetail{1.5}{1.0}{\showIt}
\ifnum\showIt=1
    \node[font=\tiny] at (0,-0.5) {Detailed info: 192.168.1.100:443};
\fi
```

### Overview Mode
```latex
% Simplified view for overviews
\setOverviewMode{true}
% Hides: detailed labels, port numbers, complex styling
```

### Detail Mode
```latex
% Full detail view
\setDetailMode{1.5}  % Sets zoom to 1.5x and enables all details
```

### Adaptive Rendering
```latex
% Render different details at different zoom levels
\renderAdaptiveDetail{1.2}{node}
% showBasic=1 (zoom ≥ 0.5)
% showMedium=1 (zoom ≥ 1.0)
% showFull=0 (zoom < 1.5)
```

---

## Complete Example: Enterprise Network

```latex
\begin{tikzpicture}

% Set output for A3 paper
\setOutputSize{a3}

% Use 4-tier layout
\layoutTiered{4}{vertical}{6cm}

% Tier 0: Internet
\calcTierPosition{0}{0}{1}{6}{4}{\internetX}{\internetY}
\node[cloud, fill=red!20] at (\internetX, \internetY) {Internet};

% Tier 1: Perimeter (2 firewalls)
\calcTierPosition{1}{0}{2}{6}{4}{\fw1X}{\fw1Y}
\calcTierPosition{1}{1}{2}{6}{4}{\fw2X}{\fw2Y}
\node[firewall] (fw1) at (\fw1X, \fw1Y) {Firewall 1};
\node[firewall] (fw2) at (\fw2X, \fw2Y) {Firewall 2};

% Tier 2: Web servers in circular layout
\layoutCircular{\fw1X}{\fw1Y - 6}{3}{4}{0}
\foreach \i in {0,...,3} {
    \calcCircularAngle{\i}{4}{0}{\angle}
    \positionOnCircle{\fw1X}{\fw1Y - 6}{3}{\angle}{web\i}
    \node[server] at (web\i) {Web \i};
}

% Tier 3: Database cluster
\calcTierPosition{3}{0}{2}{6}{4}{\db1X}{\db1Y}
\calcTierPosition{3}{1}{2}{6}{4}{\db2X}{\db2Y}
\node[database] (db1) at (\db1X, \db1Y) {DB Primary};
\node[database] (db2) at (\db2X, \db2Y) {DB Replica};

% Auto-group web servers by subnet
\drawAutoSubnet{192.168.10.0/24}{(web0)(web1)(web2)(web3)}{DMZ Web Tier}

% Auto-group databases by subnet
\drawAutoSubnet{10.50.20.0/24}{(db1)(db2)}{Secure DB Tier}

% Add page navigation (page 1 of 3)
\drawPageHeader{1}{3}{Enterprise Network Architecture}

\end{tikzpicture}
```

---

## Tips and Best Practices

1. **Start Simple**: Use basic layouts first, then add complexity
2. **Test Spacing**: Adjust `\nodeSpacing` and `\layerSpacing` for your specific diagram
3. **Use Auto-Grouping**: Let subnet auto-grouping color-code security zones
4. **Multi-Page for Scale**: Use multi-page layout for networks > 30 nodes
5. **Optimize for Output**: Set display mode and output size early
6. **Preview at Scale**: Test print output at actual size before finalizing

---

## Troubleshooting

### Nodes Overlapping
```latex
% Increase minimum spacing
\setlength{\minNodeSpacing}{4cm}

% Use collision avoidance
\avoidCollision{x1}{y1}{x2}{y2}{\newX}{\newY}
```

### Layout Too Cramped
```latex
% Calculate optimal spacing
\calcOptimalTierSpacing{node_count}{\spacing}

% Or manually increase
\setlength{\layerSpacing}{8cm}
```

### Subnet Colors Wrong
```latex
% Check IP address format
\parseIPAddress{192.168.1.100}{\a}{\b}{\c}{\d}
% Verify: \a=192, \b=168, \c=1, \d=100

% Manually set color if needed
\drawSubnet{mynet}{blue}{(nodes)}{Custom Subnet}
```

---

For more examples, see the `examples/` directory (coming soon).
