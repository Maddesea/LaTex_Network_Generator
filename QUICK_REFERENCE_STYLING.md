# Network Diagram Generator - Quick Styling Reference

## Color Schemes

```latex
\useDefaultColors        % Vibrant default colors
\useDarkMode            % Dark background theme
\useLightMode           % Light background theme
\useColorblindSafe      % Accessible for all vision types
\useMonochrome          % Grayscale for B&W printing
\useHighContrast        % Maximum contrast
```

## Node Styles

### Basic Styles
```latex
\node[server] {...};
\node[client] {...};
\node[router] {...};
\node[firewall] {...};
\node[switch] {...};
\node[cloud] {...};
\node[attacker] {...};
```

### Gradient Styles
```latex
\node[gradient server] {...};
\node[gradient client] {...};
\node[gradient router] {...};
\node[gradient firewall] {...};
\node[metallic server] {...};
\node[radial server] {...};
\node[glass node] {...};
```

### Pattern Styles (Accessibility)
```latex
\node[pattern server] {...};     % Vertical lines
\node[pattern client] {...};     % Horizontal lines
\node[pattern router] {...};     % Grid
\node[pattern database] {...};   % Dots
\node[pattern firewall] {...};   % Crosshatch
\node[pattern critical] {...};   % NE lines
```

### Template Styles
```latex
\node[corporate] {...};          % Professional gradient
\node[security] {...};           % Threat emphasis
\node[modern cloud] {...};       % Glass cloud style
\node[minimal] {...};            % Clean simple
\node[presentation] {...};       % Large high-visibility
```

## Icons

### Built-in TikZ Icons
```latex
\serverIcon    \laptopIcon    \phoneIcon
\routerIcon    \databaseIcon  \cloudIcon
```

### Icon Node Styles
```latex
\node[icon server] {...};
\node[icon client] {...};
\node[icon router] {...};
\node[icon database] {...};
```

### External Images
```latex
\node {\nodeIcon{1cm}{icons/custom.png}};
```

## Badges

### OS Badges
```latex
pin={[badge windows]45:Win}
pin={[badge linux]45:Linux}
pin={[badge macos]45:Mac}
```

### Status Badges
```latex
pin={[badge online]90:●}
pin={[badge offline]90:●}
pin={[badge warning]90:⚠}
pin={[badge critical]90:!}
```

### Multiple Badges
```latex
\node[server,
      pin={[badge windows]45:Win},
      pin={[badge online]135:●}
     ] {...};
```

## Connections

### Basic Connections
```latex
\draw[normal conn] (A) -- (B);
\draw[encrypted conn] (A) -- (B);
\draw[suspicious conn] (A) -- (B);
\draw[attack conn] (A) -- (B);
\draw[bidirectional] (A) -- (B);
```

### Bandwidth Styles
```latex
\draw[bw low] (A) -- (B);        % 1-10 Mbps
\draw[bw medium] (A) -- (B);     % 10-100 Mbps
\draw[bw high] (A) -- (B);       % 100-1000 Mbps
\draw[bw very high] (A) -- (B);  % 1+ Gbps
\draw[bw congested] (A) -- (B);  % Congested
```

### Special Connection Types
```latex
\draw[vpn tunnel] (A) -- (B);
\draw[wireless] (A) -- (B);
\draw[fiber optic] (A) -- (B);
\draw[satellite link] (A) -- (B);
\draw[blocked conn] (A) -- (B);
\draw[load balanced] (A) -- (B);
```

### Curved Connections
```latex
\draw[curve conn] (A) -- (B);        % Smooth curve
\draw[curve sharp] (A) -- (B);       % Sharp curve
\draw[curve reverse] (A) -- (B);     % Reverse curve
```

### Flow Animations
```latex
\draw[data flow] (A) -- (B);
\draw[flow animation] (A) -- (B);
```

### Connection with Label
```latex
\draw[normal conn] (A) -- (B)
     node[midway, above] {HTTPS:443};
```

## Annotations

### Callout Boxes
```latex
\node[info callout] {...};
\node[warning callout] {...};
\node[critical callout] {...};
\node[success callout] {...};
\node[note box] {...};
```

### Network Zones
```latex
\node[dmz zone, fit=(node1)(node2)] {};
\node[internal zone, fit=(node3)(node4)] {};
\node[trusted zone, fit=(node5)] {};
\node[external zone, fit=(node6)] {};
```

### Metadata
```latex
\diagramMetadata{Title}{Author}{Date}{v1.0}{south east}
\networkStats{12}{5}{7}{18}{2}{north west}
```

## Legends

### Quick Legends
```latex
\basicLegend
\connectionLegend
\statusLegend
```

### Legend Styles
```latex
\node[legend box] {...};
\node[legend compact] {...};
\node[legend large] {...};
\node[legend transparent] {...};
```

### Legend Items
```latex
\legendServer
\legendClient
\legendRouter
\legendFirewall
\legendNormalConn
\legendEncryptedConn
\legendOnline
\legendWarning
\legendCritical
```

## Beamer Animations

### Progressive Reveals
```latex
\node<1->[server] (s1) {...};    % Appears on slide 1+
\node<2->[client] (c1) {...};    % Appears on slide 2+
\draw<3->[attack conn] (c1) -- (s1);  % Appears on slide 3+
```

### Animation Styles
```latex
\node[pulse node] {...};
\node[alert node] {...};
\node[dim] {...};
\node[reveal] {...};
```

## Topology Templates

### 3-Tier Architecture
```latex
\threeTierTemplate{w1}{w2}{w3}{a1}{a2}{a3}{d1}{d2}{d3}
```

### Hub-and-Spoke
```latex
\hubSpokeTemplate{hub}{6}{3cm}{metallic router}{gradient client}
```

### Full Mesh
```latex
\meshTemplate{5}{3cm}{gradient server}
```

## Common Patterns

### Complete Node Example
```latex
\node[gradient server,
      pin={[badge linux]45:Linux},
      pin={[badge online]135:●}
     ] (web) at (0,0) {
     \serverIcon\\
     Web Server\\
     192.168.1.10
};
```

### Labeled Connection
```latex
\draw[encrypted conn] (A) -- (B)
     node[midway, above, font=\tiny, fill=white] {HTTPS:443};
```

### Network Zone with Nodes
```latex
\begin{scope}
    \node[internal zone, fit=(n1)(n2)(n3),
          label=above:Internal Network] {};
    \node[gradient server] (n1) at (0,0) {...};
    \node[gradient server] (n2) at (2,0) {...};
    \node[gradient client] (n3) at (1,-2) {...};
\end{scope}
```

### Security Dashboard
```latex
\node[rectangle, draw=red, fill=red!10, rounded corners] {
    \begin{tabular}{ll}
        \multicolumn{2}{l}{\textbf{Security Status}} \\
        \legendOnline & 10 \\
        \legendWarning & 2 \\
        \legendCritical & 1 \\
    \end{tabular}
};
```

## Tips

1. **Start with color scheme**: Choose early based on audience
2. **Use patterns for accessibility**: Combine with colorblind palette
3. **Limit badges**: 2-3 per node maximum
4. **Gradient moderation**: Mix with flat styles for hierarchy
5. **Label connections**: Use `midway` positioning
6. **Layer your diagram**: Background zones, then nodes, then connections
7. **Test compilation**: Use `pdflatex` for best gradient rendering

## File Structure

```
your-diagram.tex
├─ \documentclass{standalone}
├─ \usepackage{tikz, xcolor, ifthen}
├─ \usetikzlibrary{shapes, arrows, shadows, decorations.markings, patterns}
├─ \input{styles_config.tex}
├─ \begin{document}
│  ├─ \useColorblindSafe  % Choose color scheme
│  ├─ \begin{tikzpicture}
│  │  ├─ Nodes
│  │  ├─ Connections
│  │  └─ Legends/Annotations
│  └─ \end{tikzpicture}
└─ \end{document}
```

## Examples Directory

See `examples/` for complete working examples:
- `01_basic_network_colorschemes.tex` - Color scheme demo
- `02_enterprise_gradients.tex` - Gradient effects
- `03_security_with_badges.tex` - Icons and badges
- `04_multicloud_architecture.tex` - Multi-cloud
- `05_accessibility_patterns.tex` - Pattern fills
- `06_beamer_presentation.tex` - Animated presentation
- `07_complete_demo.tex` - All features combined

## Compilation

```bash
# Linux/Mac
cd examples
./compile_all.sh

# Windows
cd examples
compile_all.bat

# Single file
pdflatex your-diagram.tex
```

---

For complete documentation, see `STYLING_GUIDE.md`
