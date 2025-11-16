# Getting Started with Network Diagram Generator

Welcome! This guide will help you create your first network diagram in under 5 minutes.

## Prerequisites

### Install LaTeX

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install texlive-full
```

#### Fedora/RHEL
```bash
sudo dnf install texlive-scheme-full
```

#### macOS (with Homebrew)
```bash
brew install --cask mactex
```

#### Windows
1. Download [MiKTeX](https://miktex.org/download) or [TeXLive](https://www.tug.org/texlive/)
2. Run the installer
3. Add to PATH during installation

### Verify Installation

```bash
pdflatex --version
```

You should see version information. If not, LaTeX isn't installed correctly.

## Quick Start (3 Steps)

### Step 1: Choose a Template

Navigate to the `templates/` directory:

```bash
cd templates
ls
```

You'll see:
- `basic_network.tex` - Simple network (recommended for beginners)
- `enterprise_datacenter.tex` - 3-tier architecture
- `security_incident.tex` - Security visualization

### Step 2: Compile

```bash
pdflatex basic_network.tex
```

This creates `basic_network.pdf` - open it to see your first diagram!

### Step 3: Customize

Open `basic_network.tex` in your favorite editor:

```bash
nano basic_network.tex
# or
code basic_network.tex  # VSCode
# or
vim basic_network.tex
```

Try changing:

1. **The title:**
```latex
\node[font=\Large\bfseries] at (3,6) {My Network Diagram};
                                      ↑ Change this
```

2. **A server name:**
```latex
\node[server] (web) at (0,2) {Web Server\\192.168.1.10};
                              ↑ Change this
```

3. **The color scheme:**
```latex
% Change from:
\useDefaultColors

% To:
\useColorblindSafe
```

Save and recompile:
```bash
pdflatex basic_network.tex
```

## Your First Custom Diagram

Let's create a simple home network from scratch:

### 1. Create a New File

```bash
cd ..  # Go to main directory
nano my_home_network.tex
```

### 2. Copy This Template

```latex
\documentclass[border=5mm]{standalone}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{ifthen}

\usetikzlibrary{shapes, arrows, shadows, decorations.markings, patterns}

\input{styles_config.tex}

\begin{document}

\useDefaultColors

\begin{tikzpicture}[scale=1.0]

    % Title
    \node[font=\Large\bfseries] at (3,5) {My Home Network};

    % Internet
    \node[cloud] (internet) at (3,4) {Internet};

    % Router
    \node[router] (router) at (3,2.5) {Home Router\\192.168.1.1};

    % Devices
    \node[client] (laptop) at (0,1) {\laptopIcon\\Laptop};
    \node[client] (phone) at (3,1) {\phoneIcon\\Phone};
    \node[server] (nas) at (6,1) {NAS\\Storage};

    % Connections
    \draw[normal conn] (internet) -- (router);
    \draw[wireless] (router) -- (laptop);
    \draw[wireless] (router) -- (phone);
    \draw[normal conn] (router) -- (nas);

\end{tikzpicture}

\end{document}
```

### 3. Compile

```bash
pdflatex my_home_network.tex
```

### 4. View

Open `my_home_network.pdf` - you just created your first custom diagram!

## Understanding the Structure

### Basic Anatomy

```latex
\documentclass[border=5mm]{standalone}  % Document type
\usepackage{tikz}                        % Graphics package
\input{styles_config.tex}                % Load styling

\begin{document}
\useDefaultColors                         % Choose color scheme

\begin{tikzpicture}[scale=1.0]           % Start diagram

    % YOUR DIAGRAM GOES HERE
    % 1. Create nodes
    % 2. Draw connections
    % 3. Add labels/legends

\end{tikzpicture}
\end{document}
```

### Creating Nodes

**Pattern:**
```latex
\node[STYLE] (ID) at (X,Y) {LABEL};
```

**Example:**
```latex
\node[server] (web) at (0,0) {Web Server};
       ↑       ↑      ↑        ↑
      style    ID   position  label
```

**Styles you can use:**
- `server`, `client`, `router`, `firewall`, `switch`, `cloud`, `attacker`
- `gradient server`, `metallic server`, `glass node`
- `pattern server`, `pattern client` (for accessibility)

### Drawing Connections

**Pattern:**
```latex
\draw[STYLE] (FROM_ID) -- (TO_ID);
```

**Example:**
```latex
\draw[encrypted conn] (server1) -- (server2);
       ↑               ↑           ↑
     style         from node    to node
```

**Styles you can use:**
- `normal conn`, `encrypted conn`, `suspicious conn`, `attack conn`
- `vpn tunnel`, `wireless`, `fiber optic`
- `bw high`, `bw low` (bandwidth indicators)

## Next Steps

### Add More Features

#### Add Badges
```latex
\node[server,
      pin={[badge linux]45:Linux}
     ] (srv) at (0,0) {My Server};
```

#### Add Icons
```latex
\node[server] (srv) at (0,0) {
    \serverIcon\\
    My Server\\
    192.168.1.10
};
```

#### Add Zones
```latex
% First create your nodes
\node[server] (srv1) at (0,0) {Server 1};
\node[server] (srv2) at (2,0) {Server 2};

% Then add a zone around them
\node[dmz zone, fit=(srv1)(srv2)] {};
```

#### Add Labels to Connections
```latex
\draw[encrypted conn] (node1) -- (node2)
    node[midway, above] {HTTPS:443};
```

### Explore Examples

Check out the `examples/` directory:

```bash
cd examples
./compile_all.sh
```

This compiles all 9 examples. Study the `.tex` files to learn more techniques.

### Read the Documentation

- **QUICK_REFERENCE_STYLING.md** - Quick command lookup
- **STYLING_GUIDE.md** - Complete feature guide
- **templates/README.md** - Template documentation

## Common Tasks

### Change Colors

```latex
% At the top of your diagram:
\useDefaultColors      % Vibrant colors
\useColorblindSafe     % Accessible colors
\useDarkMode          % Dark theme
\useMonochrome        % Grayscale
\useHighContrast      % Max contrast
```

### Scale Your Diagram

```latex
\begin{tikzpicture}[scale=1.5]  % 1.5x larger
\begin{tikzpicture}[scale=0.8]  % 0.8x smaller
```

### Add a Legend

```latex
\node[legend box, anchor=north west] at (0,5) {
    \begin{tabular}{ll}
        \textbf{Legend} \\[2pt]
        \legendServer \\
        \legendClient \\
        \legendNormalConn \\
        \legendEncryptedConn \\
    \end{tabular}
};
```

### Add a Title

```latex
\node[font=\Huge\bfseries] at (5,8) {My Diagram Title};
\node[font=\large, text=gray] at (5,7.4) {Subtitle or Description};
```

## Troubleshooting

### "Undefined control sequence" error

**Problem:** Missing `\input{styles_config.tex}`

**Solution:** Add this line after `\usetikzlibrary{...}`:
```latex
\input{styles_config.tex}
```

### Nodes overlap

**Solution 1:** Increase spacing between nodes
```latex
\node[server] (srv1) at (0,0) {Server 1};
\node[server] (srv2) at (4,0) {Server 2};
                        ↑ Increase this number
```

**Solution 2:** Scale down
```latex
\begin{tikzpicture}[scale=0.8]
```

### Compilation is slow

**Solution:** Remove shadows on nodes:
```latex
% Instead of:
\node[gradient server] ...

% Use:
\node[server] ...
```

### Can't find color scheme file

**Solution:** Make sure you're compiling from the correct directory:
```bash
# If in examples/ or templates/
\input{../styles_config.tex}  % Go up one directory

# If in main directory
\input{styles_config.tex}      # Same directory
```

## Tips for Success

1. **Start simple** - Use `basic_network.tex` template
2. **Compile often** - Test after each change
3. **One feature at a time** - Don't add everything at once
4. **Study examples** - The `examples/` folder has working code
5. **Use comments** - Document your diagram with `% comments`
6. **Save versions** - Keep working versions as backups

## Getting Help

1. **Quick Reference**: See `QUICK_REFERENCE_STYLING.md`
2. **Examples**: Check `examples/` directory
3. **Full Documentation**: Read `STYLING_GUIDE.md`
4. **Templates**: Use `templates/` as starting points

## What's Next?

Once you're comfortable with basics:

1. **Try different color schemes** - Experiment with `\useDarkMode`, `\useColorblindSafe`
2. **Add gradients** - Use `gradient server` instead of `server`
3. **Include badges** - Add OS and status indicators
4. **Create zones** - Group nodes with network boundaries
5. **Build presentations** - Use Beamer with example 06

## Congratulations! 🎉

You've learned the basics of creating network diagrams with LaTeX!

Keep experimenting and refer to the documentation as you add more advanced features.

Happy diagramming! 🚀
