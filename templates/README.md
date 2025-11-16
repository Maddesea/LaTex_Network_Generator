# Network Diagram Templates

Ready-to-use templates for common network diagram scenarios. Copy, modify, and compile!

## Available Templates

### 1. basic_network.tex
**Perfect for**: First-time users, simple networks, learning the system

**Features:**
- Simple network topology
- Internet → Firewall → Servers → Clients
- Basic and encrypted connections
- Legend included
- Commented for easy modification

**Nodes:** 7 (1 cloud, 1 firewall, 2 servers, 3 clients)
**Complexity:** ⭐ Beginner

**Usage:**
```bash
cd templates
pdflatex basic_network.tex
```

### 2. enterprise_datacenter.tex
**Perfect for**: Data centers, 3-tier architectures, professional documentation

**Features:**
- 3-tier architecture (Web/App/Data)
- Gradient node styles
- OS and status badges
- Metadata and statistics boxes
- Network zone organization
- Database replication

**Nodes:** 11 (3 web, 3 app, 2 database, 3 tiers)
**Complexity:** ⭐⭐⭐ Advanced

**Usage:**
```bash
cd templates
pdflatex enterprise_datacenter.tex
```

**Customization:** Edit the node counts in each tier (currently 3-3-2).

### 3. security_incident.tex
**Perfect for**: Incident reports, security analysis, threat visualization

**Features:**
- Attack visualization
- Threat actor representation
- Compromised node indicators
- Attack path highlighting
- Incident details callout
- Security status dashboard
- Response checklist

**Nodes:** 5 (1 attacker, 1 firewall, 2 servers, 1 client)
**Complexity:** ⭐⭐ Intermediate

**Usage:**
```bash
cd templates
pdflatex security_incident.tex
```

**Customization:** Modify attack type, CVE details, and response actions.

## How to Use Templates

### Method 1: Copy and Modify

```bash
# Copy template to your project
cp templates/basic_network.tex my_network.tex

# Edit the file
nano my_network.tex

# Compile
pdflatex my_network.tex
```

### Method 2: Direct Compilation

```bash
cd templates
pdflatex basic_network.tex
# Output: basic_network.pdf
```

## Customization Guide

### Change Color Scheme

In the template file, find and uncomment:

```latex
% \useDefaultColors        % Default vibrant colors
\useColorblindSafe       % ← Currently active
% \useDarkMode            % Dark background
% \useMonochrome          % Grayscale
% \useHighContrast        % Maximum contrast
```

### Add More Nodes

Copy existing node definitions:

```latex
% Copy this pattern:
\node[gradient server,
      pin={[badge linux]45:Linux},
      pin={[badge online]135:●}
     ] (server1) at (x,y) {\serverIcon\\Server Name\\IP};
```

**Key parts to change:**
- `(server1)` - Unique node ID
- `at (x,y)` - Position coordinates
- `Server Name` - Display name
- `IP` - IP address

### Add Connections

```latex
% Normal connection
\draw[normal conn] (node1) -- (node2);

% Encrypted connection
\draw[encrypted conn] (node1) -- (node2);

% Attack connection
\draw[attack conn] (attacker) -- (target);

% VPN tunnel
\draw[vpn tunnel] (siteA) -- (siteB);

% With label
\draw[encrypted conn] (node1) -- (node2)
    node[midway, above] {HTTPS:443};
```

### Change Node Styles

Replace the style keyword:

```latex
% Basic → Gradient
\node[server] ... → \node[gradient server] ...

% Basic → Pattern (accessibility)
\node[server] ... → \node[pattern server] ...

% Basic → Metallic
\node[server] ... → \node[metallic server] ...
```

### Add Badges

```latex
% Single badge
\node[server, pin={[badge linux]45:Linux}] ...

% Multiple badges (OS + Status)
\node[server,
      pin={[badge linux]45:Linux},
      pin={[badge online]135:●}
     ] ...
```

**Badge positions:**
- `45` - Top right
- `135` - Top left
- `225` - Bottom left
- `315` - Bottom right
- `90` - Top center

### Add Icons

```latex
% Include icon in node text
\node[server] {\serverIcon\\Server Name};

% Available icons:
\serverIcon    \laptopIcon    \phoneIcon
\routerIcon    \databaseIcon  \cloudIcon
```

## Template Comparison

| Feature | Basic | Enterprise | Security |
|---------|-------|------------|----------|
| Difficulty | ⭐ | ⭐⭐⭐ | ⭐⭐ |
| Nodes | 7 | 11 | 5 |
| Gradients | ❌ | ✅ | ✅ |
| Badges | ❌ | ✅ | ✅ |
| Icons | ❌ | ✅ | ✅ |
| Zones | ❌ | ✅ | ❌ |
| Metadata | ❌ | ✅ | ✅ |
| Animations | ❌ | ❌ | ❌ |
| Best for | Learning | Production | Reports |

## Creating Your Own Template

1. **Start with basic_network.tex**
2. **Add your nodes** (copy/paste/modify existing nodes)
3. **Connect nodes** (add \draw commands)
4. **Style it** (change colors, add badges, etc.)
5. **Add metadata** (title, legend, statistics)
6. **Test compile** (pdflatex your_template.tex)
7. **Save as template** (for reuse)

## Quick Modifications

### Change Title
```latex
\node[font=\Huge\bfseries] at (4,10) {Your Title Here};
```

### Change Scale
```latex
\begin{tikzpicture}[scale=1.5]  % Increase to 1.5x
```

### Change Position
```latex
\node[server] (srv) at (3,5) {...};
%                      ↑  ↑
%                      x  y coordinates
```

### Add Network Zone
```latex
\node[dmz zone, fit=(node1)(node2)(node3)] {};
% Creates a zone around node1, node2, and node3
```

## Troubleshooting

### Template won't compile
- Check that `styles_config.tex` is in parent directory
- Verify `\input{../styles_config.tex}` path is correct
- Ensure all TikZ libraries are loaded

### Nodes overlap
- Increase spacing: change `at (x,y)` coordinates
- Increase scale: `\begin{tikzpicture}[scale=1.2]`

### Missing features
- Update to latest version
- Check STYLING_GUIDE.md for feature documentation

## Advanced Topics

For advanced features, see:
- **STYLING_GUIDE.md** - Complete styling reference
- **QUICK_REFERENCE_STYLING.md** - Command reference
- **examples/** - 9 working examples

## Need Help?

1. Check **QUICK_REFERENCE_STYLING.md** for command syntax
2. Look at **examples/** for feature demonstrations
3. Read **STYLING_GUIDE.md** for detailed explanations
4. Review **TROUBLESHOOTING.md** for common issues

## Contributing Templates

Have a useful template? Contributions welcome!

Requirements:
- Well-commented code
- Clear purpose/use case
- Documentation in this README
- Compiles without errors
