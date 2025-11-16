# Network Diagram Examples

This directory contains practical examples demonstrating the advanced layout features of the LaTeX Network Diagram Generator.

## Available Examples

### 1. example_tiered_layout.tex
**Demonstrates:** Tiered layout with circular sub-layout

**Features shown:**
- 4-tier architecture (External → Perimeter → Application → Data)
- Automatic tier positioning with `\calcTierPosition`
- Circular layout for web server cluster
- Subnet auto-grouping with `\drawAutoSubnet`
- IP-based trust-level coloring (RFC 1918)

**Use case:** Web application architecture, N-tier systems

**Compile:**
```bash
pdflatex example_tiered_layout.tex
```

---

### 2. example_datacenter_grid.tex
**Demonstrates:** Grid layout for data center visualization

**Features shown:**
- Grid layout with `\layoutGrid` and `\calcGridPosition`
- Server rack visualization with 42U racks
- Blade server enclosures
- Hot/cold aisle representation (future)
- Network redundancy with dual core switches

**Use case:** Data center floor plans, server farms

**Compile:**
```bash
pdflatex example_datacenter_grid.tex
```

---

### 3. example_hub_spoke.tex
**Demonstrates:** Hub-and-spoke topology with concentric circles

**Features shown:**
- Central hub router
- Inner ring: 4 regional routers
- Outer ring: 8 branch offices
- Circular layout with `\positionOnCircle`
- Multi-level hierarchy
- VPN connectivity

**Use case:** WAN networks, regional office networks, CDN topologies

**Compile:**
```bash
pdflatex example_hub_spoke.tex
```

---

### 4. example_comprehensive_showcase.tex
**Demonstrates:** ALL advanced features in one diagram

**Features shown:**
- **Layout algorithms:** Tiered, circular, grid, HA pairs
- **Background elements:** Dot pattern, security zones
- **Collision avoidance:** Smart positioning
- **Subnet grouping:** Auto-colored by trust level
- **Advanced positioning:** Interpolation, rotation, mirroring
- **HA configuration:** Firewall pair, database replication
- **Load balancing:** Round-robin to app tier
- **Threat indicators:** Vulnerability badges, attack visualization
- **Annotations:** Complex connections, legends, statistics
- **Optimization:** Display mode set for print output

**Use case:** Enterprise security architecture, comprehensive network documentation

**Compile:**
```bash
pdflatex example_comprehensive_showcase.tex
```

---

## Quick Start

1. **Choose an example** based on your needs
2. **Copy and modify** the example file
3. **Compile** using pdflatex or the compile script:
   ```bash
   ./compile.sh pdf example_tiered_layout
   ```

## Customization Tips

### Changing Node Positions
```latex
% Modify tier spacing
\calcTierPosition{tier}{position}{total}{resultX}{resultY}

% Adjust grid spacing
\calcGridPosition{row}{col}{rowSpacing}{colSpacing}{startX}{startY}{resultX}{resultY}
```

### Adjusting Colors
```latex
% Change subnet colors (edit in styles_config.tex)
\definecolor{myBlue}{RGB}{30, 144, 255}

% Or use inline
fill=myBlue!30, draw=myBlue!80
```

### Scaling Diagrams
```latex
% In the tikzpicture environment
\begin{tikzpicture}[scale=0.8, transform shape, font=\sffamily]

% Or use output size optimization
\setOutputSize{a3}  % a4, a3, a2, letter, screen
```

## Common Modifications

### Add More Nodes to Tiered Layout
```latex
% Add a 5th node to tier 2
\calcTierPosition{2}{4}{5}{\newX}{\newY}  % position 4 of 5
\createServer{newserver}{10.0.0.50}{\newX}{\newY}{New Server}
```

### Change Circular Layout Radius
```latex
% Increase/decrease radius
\pgfmathsetmacro{\dmzRadius}{4.0}  % was 2.5
```

### Modify Grid Density
```latex
% Change row/column spacing
\calcGridPosition{\row}{\col}{4}{4}{startX}{startY}{x}{y}  % 4cm spacing
```

## Combining Features

You can mix and match layout algorithms in one diagram:

```latex
% Tiered layout for main structure
\layoutTiered{4}{vertical}{6cm}

% Circular layout within tier 2
\positionOnCircle{centerX}{centerY}{radius}{angle}{result}

% Grid layout within tier 3
\calcGridPosition{row}{col}{spacing}{spacing}{x}{y}{result_x}{result_y}
```

## Performance Tips

1. **For large diagrams (50+ nodes):**
   - Use multi-page layout: `\layoutMultiPage{50}{20}{2}`
   - Enable overview mode: `\setOverviewMode{true}`
   - Reduce shadow effects

2. **For complex connections:**
   - Use collision avoidance: `\avoidCollision{...}`
   - Enable curved connections: `\drawCurvedConnection{...}`

3. **For print output:**
   - Set display mode: `\setDisplayMode{print}`
   - Use appropriate output size: `\setOutputSize{a3}`

## Troubleshooting

### Nodes Overlapping
- Increase spacing in layout commands
- Use collision detection: `\checkNodeCollision{...}`
- Enable magnetic alignment: `\magneticAlign{...}`

### Compilation Errors
- Ensure all `.tex` modules are in the same directory
- Check for missing packages: `xstring`, `tikz`, `calc`
- Verify node names don't have special characters

### Connections Not Showing
- Verify node names match exactly
- Check if nodes are on the same page (for multi-page)
- Ensure `connection_renderer.tex` is included

## Next Steps

1. **Explore LAYOUT_ENGINE_GUIDE.md** for detailed API documentation
2. **Check QUICK_REFERENCE.md** for command syntax
3. **Review TODO_TRACKER.md** for planned features
4. **Modify examples** to match your specific network topology

## Contributing

Have a useful example? Consider contributing:
1. Create a well-documented example file
2. Add description to this README
3. Test compilation
4. Submit via pull request

## License

These examples are part of the LaTeX Network Diagram Generator project.
Free to use, modify, and distribute.

---

**Need help?** Check the main README.md or consult LAYOUT_ENGINE_GUIDE.md for comprehensive documentation.
