# Troubleshooting Guide

Complete troubleshooting reference for common issues and their solutions.

## Table of Contents

1. [Compilation Errors](#compilation-errors)
2. [Visual Issues](#visual-issues)
3. [Performance Problems](#performance-problems)
4. [Feature-Specific Issues](#feature-specific-issues)
5. [Environment Issues](#environment-issues)

---

## Compilation Errors

### Error: "Undefined control sequence"

**Symptoms:**
```
! Undefined control sequence.
l.15 \useColorblindSafe
```

**Causes:**
- Missing `\input{styles_config.tex}`
- Wrong file path to styles_config.tex
- Styles file not in expected location

**Solutions:**

1. **Add the input command:**
```latex
\usetikzlibrary{shapes, arrows, shadows, decorations.markings, patterns}
\input{styles_config.tex}  % ← Add this line
```

2. **Check file path:**
```latex
% If in examples/ or templates/ directory:
\input{../styles_config.tex}

% If in main directory:
\input{styles_config.tex}
```

3. **Verify file exists:**
```bash
ls -l styles_config.tex
# Should show the file
```

---

### Error: "File `tikz.sty' not found"

**Symptoms:**
```
! LaTeX Error: File `tikz.sty' not found.
```

**Cause:** TikZ package not installed

**Solutions:**

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
# or at minimum:
sudo apt-get install texlive-latex-base texlive-latex-extra
```

**Fedora/RHEL:**
```bash
sudo dnf install texlive-scheme-full
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows:**
- Install [MiKTeX](https://miktex.org/) or [TeXLive](https://www.tug.org/texlive/)
- Run MiKTeX Package Manager and install `tikz`

---

### Error: "I do not know the key '/tikz/gradient server'"

**Symptoms:**
```
Package tikz Error: I do not know the key '/tikz/gradient server'
```

**Causes:**
- Outdated styles_config.tex
- File not properly loaded
- Typo in style name

**Solutions:**

1. **Verify you have the latest version:**
```bash
grep "gradient server" styles_config.tex
# Should return matches
```

2. **Check for typos:**
```latex
% Correct:
\node[gradient server] ...

% Wrong:
\node[gradiant server] ...  % Typo
\node[gradient-server] ...   % Wrong format
```

3. **Ensure styles_config.tex is loaded:**
```latex
\input{styles_config.tex}
```

---

### Error: "! Dimension too large"

**Symptoms:**
```
! Dimension too large.
```

**Causes:**
- Coordinates too far apart
- Scale too large
- Too many nested nodes

**Solutions:**

1. **Reduce coordinates:**
```latex
% Instead of:
\node[server] at (1000,1000) {...}

% Use:
\node[server] at (10,10) {...}
```

2. **Adjust scale:**
```latex
% Instead of:
\begin{tikzpicture}[scale=10]

% Use:
\begin{tikzpicture}[scale=1.0]
```

3. **Simplify complex diagrams:**
- Break into multiple pages
- Use simpler styles
- Reduce number of decorations

---

### Error: Pattern color not found

**Symptoms:**
```
! Package xcolor Error: Undefined color `serverBlue!40'.
```

**Cause:** Color not defined before use

**Solution:**

Ensure styles_config.tex is loaded **before** using any styles:
```latex
\documentclass{standalone}
\usepackage{tikz}
\usepackage{xcolor}
\usetikzlibrary{...}
\input{styles_config.tex}  % ← Must be here
\begin{document}
```

---

## Visual Issues

### Nodes Overlap

**Symptoms:** Nodes appear on top of each other

**Solutions:**

1. **Increase spacing:**
```latex
% Before:
\node[server] (srv1) at (0,0) {Server 1};
\node[server] (srv2) at (1,0) {Server 2};

% After:
\node[server] (srv1) at (0,0) {Server 1};
\node[server] (srv2) at (4,0) {Server 2};  % Increased from 1 to 4
```

2. **Scale down:**
```latex
\begin{tikzpicture}[scale=0.7]  % Reduce scale
```

3. **Reduce node size:**
```latex
\node[server, minimum width=2cm, minimum height=1cm] ...
```

---

### Connections Not Visible

**Symptoms:** Drawn connections don't appear

**Causes:**
- Wrong node IDs
- Nodes not yet defined
- Connection behind nodes
- Connection color same as background

**Solutions:**

1. **Verify node IDs match:**
```latex
\node[server] (web) at (0,0) {Web};
\node[server] (db) at (3,0) {DB};
\draw[normal conn] (web) -- (db);  % IDs must match exactly
                    ↑        ↑
```

2. **Define nodes before connections:**
```latex
% Correct order:
\node[server] (srv1) ...
\node[server] (srv2) ...
\draw[normal conn] (srv1) -- (srv2);  % After nodes

% Wrong:
\draw[normal conn] (srv1) -- (srv2);  % Before nodes defined
\node[server] (srv1) ...
```

3. **Change connection color:**
```latex
\draw[red, line width=2pt] (node1) -- (node2);  % Test with visible color
```

---

### Badges Not Showing

**Symptoms:** Pin badges don't appear on nodes

**Solutions:**

1. **Check badge syntax:**
```latex
% Correct:
\node[server, pin={[badge linux]45:Linux}] ...
                   ↑badge style  ↑angle ↑text

% Wrong:
\node[server, badge linux] ...  % Missing pin={}
```

2. **Adjust angle:**
```latex
% Try different angles:
pin={[badge linux]45:Linux}   % Top right
pin={[badge linux]135:Linux}  % Top left
pin={[badge linux]90:Linux}   % Top center
```

3. **Increase pin distance:**
```latex
\tikzset{
    pin distance=1cm  % Increase if badges too close
}
```

---

### Gradients Appear as Solid Colors

**Symptoms:** Gradient styles show as flat colors

**Causes:**
- Using `latex` instead of `pdflatex`
- Old PDF viewer
- PostScript output

**Solutions:**

1. **Use pdflatex:**
```bash
# Correct:
pdflatex diagram.tex

# Wrong:
latex diagram.tex
```

2. **Update PDF viewer** - Old viewers may not support gradients

3. **Test with different viewer:**
```bash
# Linux:
evince diagram.pdf

# macOS:
open diagram.pdf

# Windows:
start diagram.pdf
```

---

### Colors Look Wrong

**Symptoms:** Colors don't match documentation

**Cause:** Wrong color scheme loaded

**Solutions:**

1. **Check which scheme is active:**
```latex
% Make sure only ONE is uncommented:
\useDefaultColors        % ← Active
% \useColorblindSafe
% \useDarkMode
```

2. **Reload color scheme:**
```latex
\loadColorScheme{colorblind}  % Explicitly load
```

3. **Verify color files exist:**
```bash
ls color_schemes/
# Should show: default.colorscheme, dark.colorscheme, etc.
```

---

## Performance Problems

### Slow Compilation

**Symptoms:** Takes >30 seconds to compile

**Causes:**
- Too many nodes (100+)
- Complex shadows
- Many gradients
- High-resolution images

**Solutions:**

1. **Disable shadows:**
```latex
% Instead of:
\node[gradient server] ...  % Has shadows

% Use:
\node[server, draw, fill=serverBlue!20] ...  % No shadows
```

2. **Use simpler styles:**
```latex
% Instead of:
\node[metallic server] ...  % Complex

% Use:
\node[server] ...  % Simple
```

3. **Reduce decorations:**
```latex
% Instead of:
\draw[encrypted conn] ...  % Has decorations

% Use:
\draw[normal conn] ...  % Simple line
```

4. **Compile with draft mode:**
```bash
pdflatex -draftmode diagram.tex
```

---

### Out of Memory

**Symptoms:**
```
! TeX capacity exceeded, sorry [main memory size=...]
```

**Solutions:**

1. **Increase memory:**

Create/edit `texmf.cnf`:
```
main_memory = 12000000
```

2. **Split into multiple files:**
```latex
% diagram_part1.tex
\input{styles_config.tex}
\begin{document}
% First half of diagram
\end{document}

% diagram_part2.tex
\input{styles_config.tex}
\begin{document}
% Second half of diagram
\end{document}
```

3. **Simplify diagram:**
- Use connection aggregation
- Reduce node detail
- Remove unnecessary elements

---

## Feature-Specific Issues

### Patterns Not Showing

**Symptoms:** Pattern fills appear solid

**Cause:** Pattern library not loaded

**Solution:**

Add patterns to library list:
```latex
\usetikzlibrary{shapes, arrows, shadows, decorations.markings, patterns}
                                                                  ↑ Add this
```

---

### Icons Too Small/Large

**Symptoms:** Built-in icons wrong size

**Solutions:**

1. **Icons are drawn at 0.5 scale by default**

To resize, edit the icon commands in styles_config.tex:
```latex
\newcommand{\serverIcon}[1][0.4cm]{%
    \begin{tikzpicture}[scale=0.7, ...]  % Change scale here
        ...
    \end{tikzpicture}%
}
```

2. **For external images, adjust width:**
```latex
\nodeIcon{2cm}{icons/server.png}  % Increase from 1cm to 2cm
```

---

### VPN Tunnel Style Not Working

**Symptoms:**
```
! Package tikz Error: I do not know the key '/tikz/vpn tunnel'
```

**Cause:** Using older version of styles_config.tex

**Solution:** Update to version 2.0+ which includes advanced connection styles

---

### Topology Templates Not Working

**Symptoms:**
```
! Undefined control sequence.
l.50 \threeTierTemplate
```

**Cause:** Feature requires v2.0+ of styles_config.tex

**Solution:**

1. **Check version:**
```bash
grep "NETWORK TOPOLOGY TEMPLATES" styles_config.tex
# Should return a match
```

2. **Update to latest version**

---

### Beamer Animations Don't Work

**Symptoms:** All nodes appear at once in Beamer

**Cause:** Missing `<slide>` syntax

**Solution:**

Use Beamer overlay syntax:
```latex
\node<1->[server] (srv1) ...  % Appears on slide 1+
\node<2->[server] (srv2) ...  % Appears on slide 2+
\draw<3->[attack conn] ...     % Appears on slide 3+
```

---

## Environment Issues

### Different Output on Different Machines

**Symptoms:** PDF looks different on another computer

**Causes:**
- Different TeXLive versions
- Different fonts installed
- Different PDF viewers

**Solutions:**

1. **Use same TeXLive version:**
```bash
pdflatex --version
# Compare versions
```

2. **Embed fonts:**
```bash
pdflatex -output-format=pdf diagram.tex
```

3. **Use standalone package:**
```latex
\documentclass[border=5mm]{standalone}  % Ensures consistency
```

---

### Permission Denied Errors

**Symptoms:**
```
! I can't write on file `diagram.pdf'.
```

**Causes:**
- PDF open in viewer
- No write permissions
- File locked

**Solutions:**

1. **Close PDF viewer** before recompiling

2. **Check permissions:**
```bash
ls -l diagram.pdf
chmod 644 diagram.pdf
```

3. **Use different output name:**
```bash
pdflatex -jobname=diagram2 diagram.tex
```

---

### Compilation Works but PDF Won't Open

**Symptoms:** pdflatex succeeds but PDF corrupted

**Solutions:**

1. **Check for errors in log:**
```bash
grep -i error diagram.log
```

2. **Try different PDF tool:**
```bash
pdftex diagram.tex
# or
lualatex diagram.tex
```

3. **Check disk space:**
```bash
df -h .
```

---

## Quick Diagnostics

### Run This Checklist

1. **TeXLive installed?**
```bash
pdflatex --version
```

2. **TikZ available?**
```bash
kpsewhich tikz.sty
```

3. **Files in place?**
```bash
ls styles_config.tex color_schemes/
```

4. **Simple test compiles?**
```latex
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
\node {Test};
\end{tikzpicture}
\end{document}
```

5. **Styles load?**
```latex
\documentclass{standalone}
\usepackage{tikz}
\input{styles_config.tex}
\begin{document}
\useDefaultColors
\begin{tikzpicture}
\node[server] {Test};
\end{tikzpicture}
\end{document}
```

---

## Getting More Help

1. **Check documentation:**
   - STYLING_GUIDE.md
   - QUICK_REFERENCE_STYLING.md
   - examples/README.md

2. **Look at examples:**
   - examples/ directory has 9 working examples
   - Compare your code to working examples

3. **Validate setup:**
   - Compile examples/99_feature_validation.tex
   - Should test all 60+ features

4. **Check version:**
   - Ensure you have v2.0+
   - See CHANGELOG.md for version history

---

## Common Solutions Summary

| Problem | Quick Fix |
|---------|-----------|
| Undefined control sequence | Add `\input{styles_config.tex}` |
| Missing tikz.sty | Install texlive-full |
| Nodes overlap | Increase coordinate spacing |
| Gradients flat | Use `pdflatex` not `latex` |
| Slow compilation | Remove shadows and gradients |
| Badges not showing | Fix pin syntax: `pin={[badge linux]45:Linux}` |
| Patterns not working | Add `patterns` to \usetikzlibrary |
| Colors wrong | Check color scheme (only one active) |

---

**Still stuck? Check the examples directory for working code to compare against!**
