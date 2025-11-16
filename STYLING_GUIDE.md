# Network Diagram Generator - Styling Guide

This guide covers all the new visual styling features added to the Network Diagram Generator.

## Table of Contents
1. [Color Schemes](#color-schemes)
2. [Gradient Fills](#gradient-fills)
3. [Icons and Images](#icons-and-images)
4. [Badges and Labels](#badges-and-labels)

---

## Color Schemes

The system now supports multiple color schemes that can be loaded dynamically.

### Available Color Schemes

1. **default** - Standard vibrant colors
2. **dark** - Optimized for dark backgrounds
3. **colorblind** - Accessible for all types of color vision deficiency
4. **monochrome** - Grayscale for black & white printing
5. **high-contrast** - Maximum contrast for accessibility

### Usage

#### Load a Color Scheme
```latex
\loadColorScheme{colorblind}
```

#### Set Theme (Dark/Light)
```latex
\setTheme{dark}  % Loads dark color scheme and sets dark background
\setTheme{light} % Loads default colors and light background
```

#### Convenience Commands
```latex
\useDefaultColors    % Load default color scheme
\useDarkMode        % Enable dark mode
\useLightMode       % Enable light mode
\useColorblindSafe  % Load colorblind-friendly palette
\useMonochrome      % Load grayscale palette
\useHighContrast    % Load high-contrast palette
```

### Creating Custom Color Schemes

Create a new file in `color_schemes/` directory with the `.colorscheme` extension:

```latex
% custom.colorscheme
\definecolor{serverBlue}{RGB}{100,150,200}
\definecolor{clientGreen}{RGB}{80,180,120}
% ... define all required colors
```

Then load it with:
```latex
\loadColorScheme{custom}
```

#### Required Color Names
- **Network Assets**: serverBlue, clientGreen, routerOrange, firewallRed, switchPurple, cloudGray
- **Threats**: threatCritical, threatHigh, threatMedium, threatLow, threatInfo
- **Connections**: connNormal, connEncrypted, connSuspicious, connMalicious
- **Background**: bgLight, bgDark

---

## Gradient Fills

Add professional gradient effects to your network diagrams.

### Gradient Node Styles

#### Vertical Gradients (Top to Bottom)
```latex
\node[gradient server] at (0,0) {Web Server};
\node[gradient client] at (2,0) {Laptop};
\node[gradient router] at (4,0) {Router};
\node[gradient firewall] at (6,0) {Firewall};
\node[gradient switch] at (8,0) {Switch};
```

#### Radial Gradients
```latex
\node[radial server] at (0,0) {Database};
\node[radial critical] at (2,0) {Compromised Host};
```

#### Metallic/Glossy Effects
```latex
\node[metallic server] at (0,0) {Enterprise Server};
\node[metallic router] at (3,0) {Core Router};
```

#### Glass Effect (Modern UI)
```latex
\node[glass node] at (0,0) {Cloud Service};
```

### Example
```latex
\begin{tikzpicture}
    % Use gradient styles for a premium look
    \node[gradient server] at (0,3) {Production\\Server};
    \node[gradient client] at (-3,0) {Admin\\Workstation};
    \node[metallic router] at (0,0) {Core\\Router};

    \draw[encrypted conn] (-3,0) -- (0,0);
    \draw[normal conn] (0,0) -- (0,3);
\end{tikzpicture}
```

---

## Icons and Images

Add visual icons to your network nodes for better clarity.

### Built-in TikZ Icons

The following icon commands are available:

```latex
\serverIcon      % Server rack icon
\laptopIcon      % Laptop computer icon
\phoneIcon       % Mobile phone icon
\routerIcon      % Router with antennas
\databaseIcon    % Database cylinder
\cloudIcon       % Cloud shape
```

### Using Icons in Nodes

#### Method 1: Icon Node Styles
```latex
\node[icon server] at (0,0) {Web Server};
\node[icon client] at (2,0) {Laptop};
\node[icon router] at (4,0) {Router};
\node[icon database] at (6,0) {Database};
```

#### Method 2: Inline Icons
```latex
\node[server] at (0,0) {\serverIcon\ Web Server};
\node[client] at (2,0) {\laptopIcon\ User PC};
```

### External Images

For custom images, place them in an `icons/` directory:

```latex
\node[server] at (0,0) {\nodeIcon{1cm}{icons/custom-server.png}\\Web Server};
```

### Example
```latex
\begin{tikzpicture}
    % Nodes with built-in icons
    \node[icon server] (web) at (0,3) {Web Server\\192.168.1.10};
    \node[icon database] (db) at (3,3) {Database\\192.168.1.20};
    \node[icon client] (pc) at (0,0) {Client PC\\192.168.1.100};

    \draw[encrypted conn] (pc) -- (web);
    \draw[encrypted conn] (web) -- (db);
\end{tikzpicture}
```

---

## Badges and Labels

Add OS type and status indicators to your nodes.

### OS Badges

```latex
\node[badge windows] {Win};   % Blue Windows badge
\node[badge linux] {Linux};   % Orange Linux badge
\node[badge macos] {Mac};     % Black macOS badge
```

### Status Badges

```latex
\node[badge online] {●};      % Green online indicator
\node[badge offline] {●};     % Red offline indicator
\node[badge warning] {⚠};    % Yellow warning
\node[badge critical] {!};    % Red critical alert
```

### Adding Badges to Nodes

#### Using Pin
```latex
\node[server, pin={[badge windows]45:Win}] at (0,0) {Server};
\node[client, pin={[badge online]90:●}] at (2,0) {Workstation};
```

#### Using Corner Badge Styles
```latex
\node[server, top right badge={badge windows, text=Win}] at (0,0) {Server};
\node[client, top left badge={badge linux, text=Linux}] at (3,0) {Client};
```

#### Multiple Badges
```latex
% OS badge + Status badge
\node[server,
      pin={[badge windows]60:Win},
      pin={[badge online]120:●}
     ] at (0,0) {Web Server};
```

### Complete Example
```latex
\begin{tikzpicture}
    % Windows server with online status
    \node[gradient server,
          pin={[badge windows]45:Win},
          pin={[badge online]135:●}
         ] (web) at (0,3) {Web Server\\192.168.1.10};

    % Linux database with warning status
    \node[gradient server,
          pin={[badge linux]45:Linux},
          pin={[badge warning]135:⚠}
         ] (db) at (4,3) {Database\\192.168.1.20};

    % Windows client with online status
    \node[gradient client,
          pin={[badge windows]315:Win},
          pin={[badge online]225:●}
         ] (client) at (2,0) {Admin PC\\192.168.1.100};

    \draw[encrypted conn] (client) -- (web);
    \draw[encrypted conn] (web) -- (db);
\end{tikzpicture}
```

---

## Complete Example: Putting It All Together

```latex
\documentclass{standalone}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{ifthen}

\usetikzlibrary{shapes, arrows, shadows, decorations.markings, patterns}

\input{styles_config.tex}

\begin{document}

% Use colorblind-safe palette
\useColorblindSafe

\begin{tikzpicture}[scale=1.2]

    % Title
    \node[font=\Large\bfseries] at (2,5) {Enterprise Network};

    % Internet cloud
    \node[cloud, icon] (internet) at (2,4) {\cloudIcon\ Internet};

    % Firewall with gradient
    \node[gradient firewall,
          pin={[badge online]90:●}
         ] (fw) at (2,2.5) {Firewall\\10.0.0.1};

    % Core router with metallic effect
    \node[metallic router,
          pin={[badge online]90:●}
         ] (router) at (2,1) {Core Router\\10.0.0.254};

    % Web server with Windows badge
    \node[gradient server,
          pin={[badge windows]45:Win},
          pin={[badge online]135:●}
         ] (web) at (0,0) {\serverIcon\\Web Server\\10.0.1.10};

    % Database with Linux badge
    \node[gradient server,
          pin={[badge linux]45:Linux},
          pin={[badge online]135:●}
         ] (db) at (2,0) {\databaseIcon\\Database\\10.0.1.20};

    % Client with macOS badge
    \node[gradient client,
          pin={[badge macos]315:Mac},
          pin={[badge warning]225:⚠}
         ] (client) at (4,0) {\laptopIcon\\Laptop\\10.0.2.50};

    % Connections
    \draw[normal conn] (internet) -- (fw);
    \draw[encrypted conn] (fw) -- (router);
    \draw[encrypted conn] (router) -- (web);
    \draw[encrypted conn] (router) -- (db);
    \draw[suspicious conn] (router) -- (client);

\end{tikzpicture}

\end{document}
```

---

## Tips and Best Practices

1. **Color Schemes**: Choose the appropriate color scheme for your audience
   - Use `colorblind` for presentations and publications
   - Use `high-contrast` for projection screens
   - Use `monochrome` for printed documentation

2. **Gradients**: Don't overuse gradients
   - Mix gradient and flat styles for visual hierarchy
   - Use metallic styles for critical infrastructure
   - Use glass styles for cloud/virtual services

3. **Icons**: Keep icons consistent
   - Use built-in TikZ icons for consistency
   - Only use external images when necessary
   - Scale icons appropriately for node size

4. **Badges**: Be selective with badges
   - Only show relevant information
   - Limit to 2-3 badges per node
   - Use status badges to highlight issues

5. **Performance**: For large diagrams
   - Prefer flat colors over gradients
   - Minimize shadow effects
   - Use simpler icon styles

---

## Troubleshooting

### Colors Not Loading
- Ensure the `.colorscheme` file is in the `color_schemes/` directory
- Check that all required color names are defined
- Verify the file uses proper LaTeX syntax

### Gradients Not Rendering
- Ensure your PDF viewer supports shading
- Try compiling with `pdflatex` instead of `latex`
- Check TikZ version (requires TikZ 3.0+)

### Icons Not Displaying
- Verify the icon command is correctly spelled
- Check that TikZ libraries are loaded
- For external images, verify the file path

### Badges Positioning Wrong
- Adjust pin angles (0-360 degrees)
- Use xshift/yshift for fine-tuning
- Try different corner badge styles

---

## Future Enhancements

Coming soon:
- Font Awesome icon integration
- SVG icon support
- Animated status badges for Beamer presentations
- Custom badge templates
- More gradient presets
