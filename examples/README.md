# Network Diagram Generator - Examples

This directory contains example files demonstrating all the styling features of the Network Diagram Generator.

## Quick Start

```bash
# Linux/Mac
./compile_all.sh

# Windows
compile_all.bat

# Single file
pdflatex 01_basic_network_colorschemes.tex
```

## Example Files

### 01_basic_network_colorschemes.tex
**Demonstrates:** Color scheme system
- Shows how to use different color palettes
- Uses colorblind-safe colors
- Basic network topology with legend

**Features:**
- `\useColorblindSafe` command
- Standard node types (router, switch, server, client)
- Normal and encrypted connections
- Basic legend

---

### 02_enterprise_gradients.tex
**Demonstrates:** Gradient and premium styling
- Enterprise data center architecture
- Multiple gradient styles

**Features:**
- `gradient server`, `gradient firewall` styles
- `metallic router` for core infrastructure
- `radial server` for databases
- `glass node` for cloud services
- Bidirectional connections with labels

---

### 03_security_with_badges.tex
**Demonstrates:** Icons and badge system
- Security visualization with status indicators
- OS type badges
- Built-in TikZ icons

**Features:**
- `\serverIcon`, `\databaseIcon`, `\laptopIcon`
- OS badges: Windows, Linux, macOS
- Status badges: online, warning, critical
- Attack connections
- Security status dashboard

---

### 04_multicloud_architecture.tex
**Demonstrates:** Multi-cloud infrastructure
- Complex topology with multiple cloud providers
- Glass effects for cloud resources

**Features:**
- `\useHighContrast` color scheme
- Cloud provider zones (AWS, Azure, GCP)
- Glass node styling
- Mobile device icons (`\phoneIcon`)
- Cross-cloud connections

---

### 05_accessibility_patterns.tex
**Demonstrates:** Pattern-based accessibility
- Patterns for colorblind users
- Works in black & white printing
- Pattern types for different node categories

**Features:**
- `pattern server`, `pattern client`, `pattern router`
- `pattern database`, `pattern firewall`, `pattern critical`
- Monochrome color scheme
- Pattern legend with explanations

---

### 06_beamer_presentation.tex
**Demonstrates:** Beamer animations
- Progressive reveal in presentations
- Attack scenario storytelling
- Slide-by-slide progression

**Features:**
- Beamer `\visible<>` integration
- Animated attack progression
- Status badge changes across slides
- Alert nodes for emphasis
- Multi-frame attack narrative

**Compile with:** `pdflatex` or `lualatex`

---

### 07_complete_demo.tex
**Demonstrates:** All features combined
- Comprehensive network diagram
- Every styling feature in one diagram

**Features:**
- All gradient types (vertical, radial, metallic, glass)
- All icon types
- All badge types (OS + status)
- All connection types
- Pattern fills
- Multiple legends
- Data flow animations
- Security dashboard
- Layer-based network architecture

---

### 08_advanced_features_demo.tex
**Demonstrates:** Advanced connection styles and annotations
- All new connection types from v2.0
- Network zone boundaries
- Topology templates

**Features:**
- 10+ connection styles (VPN, wireless, fiber, satellite, etc.)
- Bandwidth indicators (low, medium, high, congested)
- Network zones (DMZ, internal, trusted, external)
- Callout annotations (info, warning, critical, success)
- Hub-and-spoke and mesh topology templates
- Metadata and statistics boxes
- Comprehensive legend with new connection types

---

### 99_feature_validation.tex
**Demonstrates:** Complete feature test suite
- Validation of all 60+ features
- Ensures compilation compatibility

**Features:**
- Tests all color schemes (5 types)
- Tests all node styles (15+ variants)
- Tests all connection types (15+ styles)
- Tests all icons and badges
- Tests annotations and zones
- Comprehensive checklist
- Auto-validation report

**Purpose:** Use this file to verify your LaTeX environment supports all features.

---

## Compilation Scripts

### compile_all.sh (Linux/Mac)
Automated compilation script for all examples.

**Usage:**
```bash
chmod +x compile_all.sh
./compile_all.sh           # Uses pdflatex
./compile_all.sh lualatex  # Uses lualatex
```

**Features:**
- Compiles all examples automatically
- Two-pass compilation for references
- Error reporting with log files
- Success/failure summary
- Auto-cleanup of auxiliary files

### compile_all.bat (Windows)
Windows batch version of compilation script.

**Usage:**
```cmd
compile_all.bat           REM Uses pdflatex
compile_all.bat lualatex  REM Uses lualatex
```

---

## Compiling Examples

### Standard Compilation
```bash
cd examples
pdflatex 01_basic_network_colorschemes.tex
```

### For LuaLaTeX (recommended for complex diagrams)
```bash
lualatex 07_complete_demo.tex
```

### For Beamer Presentations
```bash
pdflatex 06_beamer_presentation.tex
# Run twice for proper TOC and references
pdflatex 06_beamer_presentation.tex
```

### Batch Compile All Examples (Linux/Mac)
```bash
for file in *.tex; do pdflatex "$file"; done
```

### Batch Compile All Examples (Windows)
```cmd
for %f in (*.tex) do pdflatex "%f"
```

## Requirements

All examples require:
- TeXLive 2020 or newer (2024 recommended)
- TikZ package with libraries: shapes, arrows, shadows, decorations.markings, patterns
- xcolor package
- ifthen package

## Customization Guide

### Changing Color Schemes
In any example, replace the color scheme command:
```latex
% Original
\useColorblindSafe

% Try these alternatives
\useDefaultColors
\useDarkMode
\useMonochrome
\useHighContrast
```

### Swapping Node Styles
Change node styles to experiment:
```latex
% Original
\node[server] (web) at (0,0) {Web Server};

% Try these variants
\node[gradient server] (web) at (0,0) {Web Server};
\node[metallic server] (web) at (0,0) {Web Server};
\node[pattern server] (web) at (0,0) {Web Server};
\node[icon server] (web) at (0,0) {Web Server};
```

### Adding More Badges
Combine multiple badges on one node:
```latex
\node[server,
      pin={[badge windows]45:Win},
      pin={[badge online]135:●},
      pin={[badge warning]225:⚠}
     ] (srv) at (0,0) {Server};
```

## Troubleshooting

### Compilation Errors

**Error:** `! LaTeX Error: File 'tikz.sty' not found.`
- **Solution:** Install TeXLive or MiKTeX with full package set

**Error:** `! Package tikz Error: I do not know the key '/tikz/gradient server'`
- **Solution:** Ensure `\input{../styles_config.tex}` is present and path is correct

**Error:** Patterns not showing
- **Solution:** Add `\usetikzlibrary{patterns}` if not already loaded

**Error:** Gradients rendering as solid colors
- **Solution:** Use `pdflatex` or `lualatex`, not `latex` + `dvips`

### Visual Issues

**Issue:** Diagrams too large/small
- **Solution:** Adjust the `scale` parameter in `\begin{tikzpicture}[scale=X]`

**Issue:** Badges overlapping
- **Solution:** Adjust pin angles (0-360°) or use xshift/yshift

**Issue:** Colors look wrong
- **Solution:** Check which color scheme is loaded, try `\useDefaultColors`

## Creating Your Own Examples

1. Copy one of the existing examples
2. Modify the network topology
3. Experiment with different styles
4. Add appropriate legends
5. Document your changes

Template structure:
```latex
\documentclass[border=5mm]{standalone}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{ifthen}
\usetikzlibrary{shapes, arrows, shadows, decorations.markings, patterns}

\input{../styles_config.tex}

\begin{document}
% Optional: Choose color scheme
\useDefaultColors

\begin{tikzpicture}[scale=1.0]
    % Your diagram here
\end{tikzpicture}

\end{document}
```

## Learn More

- Main documentation: `../STYLING_GUIDE.md`
- Style reference: `../styles_config.tex`
- Project overview: `../README.md`
- Architecture: `../ARCHITECTURE.md`

## Contributing Examples

If you create interesting network diagrams, consider contributing them:
1. Add descriptive comments
2. Use clear naming for nodes
3. Include a legend
4. Add documentation in this README
5. Submit via pull request
