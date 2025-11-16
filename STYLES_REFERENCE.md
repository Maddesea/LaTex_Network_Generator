# Complete Styles Reference Guide

This comprehensive reference covers ALL styling features available in the LaTeX Network Diagram Generator.

## Table of Contents
- [Color Schemes](#color-schemes)
- [Style Presets](#style-presets)
- [Node Styles](#node-styles)
- [Connection Styles](#connection-styles)
- [Visual Effects](#visual-effects)
- [Badge System](#badge-system)
- [Legend System](#legend-system)
- [Positioning Helpers](#positioning-helpers)
- [Templates](#templates)
- [Quick Reference](#quick-reference)

---

## Color Schemes

### Available Schemes
```latex
\loadColorScheme{standard}      % Default vibrant colors
\loadColorScheme{dark}          % Dark theme with bright accents
\loadColorScheme{colorblind}    % Deuteranopia/protanopia safe
\loadColorScheme{tritanopia}    % Tritanopia safe
\loadColorScheme{monochrome}    % Grayscale for printing
\loadColorScheme{high-contrast} % Maximum accessibility
```

### Theme Support
```latex
\setTheme{light}  % Light background (default)
\setTheme{dark}   % Dark background
```

---

## Style Presets

Apply complete styling configurations with one command:

```latex
\loadCorporatePreset      % Professional monochrome
\loadSecurityPreset       % High contrast, threat-focused
\loadPresentationPreset   % High visibility with glows
\loadAccessiblePreset     % Colorblind-safe with patterns
\loadDarkPreset          % Dark mode with neon effects
```

**Quick Setup:**
```latex
\setupDiagram{corporate}     % Same as \loadCorporatePreset
\setupDiagram{security}      % Same as \loadSecurityPreset
\setupDiagram{presentation}  % Same as \loadPresentationPreset
\setupDiagram{accessible}    % Same as \loadAccessiblePreset
\setupDiagram{dark}          % Same as \loadDarkPreset
```

---

## Node Styles

### Standard Nodes
```latex
server            % Basic server
client            % Basic client/workstation
router            % Router (trapezium shape)
firewall          % Firewall (patterned rectangle)
switch            % Network switch
cloud             % Cloud/Internet (cloud shape)
attacker          % Threat actor (star shape)
```

### Premium Nodes (with Gradients)
```latex
server premium
client premium
router premium
firewall premium
switch premium
cloud premium
```

### Colorblind-Safe Nodes (with Patterns)
```latex
server colorblind
client colorblind
router colorblind
firewall colorblind
switch colorblind
```

### Advanced Specialized Nodes
```latex
database cluster      % Multi-cylinder database
load balancer node    % Diamond-shaped load balancer
cloud service         % Enhanced cloud with shimmer
container node        % Docker/container with separators
vm node              % Virtual machine (nested boxes)
iot device           % IoT device (hexagon)
mobile device        % Mobile phone (portrait rectangle)
```

### Multi-Part Nodes
```latex
% Detailed server: hostname | IP | ports
\detailedServer{name}{x}{y}{hostname}{IP}{ports}

% Detailed client: hostname | IP | OS
\detailedClient{name}{x}{y}{hostname}{IP}{OS}
```

### Quick Node Creation
```latex
% Premium styled nodes with glow in one command
\quickServer{name}{x}{y}{label}
\quickClient{name}{x}{y}{label}
\quickRouter{name}{x}{y}{label}
\quickFirewall{name}{x}{y}{label}
```

---

## Connection Styles

### Basic Connections
```latex
normal conn         % Standard connection
encrypted conn      % Encrypted/VPN (green with dots)
suspicious conn     % Suspicious traffic (orange dashed)
attack conn         % Active attack (thick red)
bidirectional       % Two-way arrows
```

### Bandwidth-Aware Connections
```latex
bandwidth low       % Thin line (0.5pt)
bandwidth medium    % Medium line (1.5pt)
bandwidth high      % Thick line (3pt)
bandwidth ultra     % Very thick line (5pt)
```

### Congestion Indicators
```latex
congestion normal    % Green (< 50% utilization)
congestion warning   % Yellow (50-80% utilization)
congestion critical  % Red (> 80% utilization)
```

### Specialized Connections
```latex
vpn tunnel     % Thick dashed with encryption indicators
fiber optic    % Light beam effect (cyan with white core)
wireless       % Wave pattern (purple wavy line)
satellite      % Dashed with satellite markers
load balanced  % Double/parallel lines (HA connections)
```

### Connection Helpers
```latex
% Labeled connection with auto-positioned label
\labeledConnection{from}{to}{style}{label}

% Bandwidth connection with automatic congestion coloring
\bandwidthConnection{from}{to}{utilization%}{label}
```

---

## Visual Effects

### Glow Effects
```latex
glow                % Soft shadow glow
strong glow=color   % Intense colored glow
shimmer=color       % Subtle glow variation
neon=color          % Neon tube effect
```

### Border Effects
```latex
double border=color  % Emphasis double border
dashed shadow=color  % Dashed outline with shadow
raised 3d           % 3D raised appearance
```

### Alert Effects
```latex
flash alert  % Intense red glow for critical alerts
```

### Zone Styles
```latex
danger zone      % Red dashed boundary (high risk)
safe zone        % Green dotted boundary (secure)
quarantine zone  % Yellow patterned boundary (isolated)
```

---

## Badge System

### OS Badges
```latex
windows badge  % Blue Windows badge
linux badge    % Orange Linux badge
macos badge    % Gray macOS badge
```

### Status Badges
```latex
online badge    % Green checkmark
offline badge   % Gray minus
warning badge   % Yellow exclamation
critical badge  % Red X
```

### Security Level Badges
```latex
security high    % Green high security
security medium  % Yellow medium security
security low     % Red low security
```

### Service Type Badges
```latex
web service badge       % Blue web service
database service badge  % Purple database
api service badge       % Orange API
ssh service badge       % Gray SSH
```

### CVE Severity Badges
```latex
cve critical  % Red critical vulnerability
cve high      % Orange high severity
cve medium    % Yellow medium severity
cve low       % Green low severity
```

### Badge Positioning
```latex
% Add single badge
\nodeBadge{node-name}{badge-style}{position}{text}

% Positions: north east, north west, south east, south west

% Add multiple badges at once
\addBadges{node}{os-badge}{status-badge}

% Add service badge
\addService{node}{service-type}{port}

% Add CVE badge
\addCVE{node}{CVE-ID}{severity}{score}

% Stack multiple badges
\stackBadges{node}{position}{badge1}{badge2}

% Custom colored badge
\customBadge{node}{position}{color}{text}

% Numeric indicator badge
\numericBadge{node}{position}{number}{color}
```

---

## Legend System

### Manual Legend Creation
```latex
% Add items to legend
\addLegendItem{style}{label}

% Render the legend
\renderLegend{x}{y}{title}
```

### Quick Legend Presets
```latex
\addStandardLegend     % Add all standard node types
\addConnectionLegend   % Add all connection types
\addThreatLegend       % Add threat severity levels
```

### Example
```latex
\addStandardLegend
\addConnectionLegend
\renderLegend{10}{5}{Legend}
```

---

## Positioning Helpers

### Grid Layout
```latex
% Create grid of nodes
\nodeGrid{base-name}{rows}{cols}{spacing}{style}

% Calculate grid position
\gridPosition{row}{col}{spacing}
```

### Row/Column Layout
```latex
% Create horizontal row
\nodeRow{base-name}{y}{count}{spacing}{style}{label-prefix}

% Create vertical column
\nodeColumn{base-name}{x}{count}{spacing}{style}{label-prefix}
```

### Circular Layout
```latex
% Calculate circular position
\circularPosition{index}{total}{radius}
```

### Example
```latex
% Create 3x4 grid of servers
\nodeGrid{srv}{3}{4}{3}{server premium}

% Create row of 5 web servers
\nodeRow{web}{0}{5}{3}{server premium}{Web-}

% Create column of 4 clients
\nodeColumn{pc}{0}{4}{3}{client premium}{PC-}
```

---

## Templates

### Three-Tier Architecture
```latex
% Create complete 3-tier setup with one command
\threeTierSetup{x-spacing}{y-spacing}
```

### DMZ Architecture
```latex
% Create complete DMZ architecture
\dmzTemplate
```

### Color Scheme Cycling
```latex
% Cycle through all color schemes (useful for multi-diagram documents)
\nextColorScheme
```

---

## Quick Reference

### Minimal Example
```latex
\setupDiagram{presentation}

\quickServer{web}{0}{0}{Web Server}
\quickClient{pc}{4}{0}{Client}
\addBadges{web}{linux badge}{online badge}

\draw[encrypted conn] (pc) -- (web);
```

### Production Example
```latex
\loadColorScheme{standard}

\detailedServer{web1}{0}{0}{web-prod-01}{192.168.1.10}{80, 443}
\addService{web1}{web}{:443}
\addCVE{web1}{CVE-2024-1234}{critical}{9.8}
\nodeBadge{web1}{linux badge}{north east}{L}
\nodeBadge{web1}{online badge}{north west}{\checkmark}
```

### Enterprise Example
```latex
\setupDiagram{corporate}

% Three-tier architecture
\threeTierSetup{4}{3}

% Add load balancer
\node[load balancer node] (lb) at (4,2) {LB};
\foreach \i in {1,2,3} {
    \draw[load balanced] (lb) -- (web-\i);
    \addBadges{web-\i}{linux badge}{online badge}
}

% Add legend
\addStandardLegend
\renderLegend{8}{2}{Legend}
```

---

## Beamer Animation Support

### Overlay-Aware Nodes
```latex
\createOverlayNode{1-}{server premium}{(0,0)}{srv}{Web Server}
\createOverlayNode{2-}{client premium}{(4,0)}{pc}{Client}
```

### Progressive Reveal
```latex
\revealConnection{3-}{encrypted conn}{pc}{srv}
```

### Animation Effects
```latex
pulse           % Pulsing opacity/scale
fade in         % Smooth fade-in
highlight pulse % Border pulsing
```

---

## Complete Feature Count

- **Color Schemes**: 6
- **Style Presets**: 5
- **Node Types**: 20+
- **Connection Styles**: 15+
- **Visual Effects**: 10+
- **Badge Types**: 15+
- **Helper Macros**: 25+
- **Total Commands**: 60+

---

## Tips & Best Practices

1. **Start Simple**: Use `\setupDiagram{preset}` to get started quickly
2. **Use Quick Macros**: `\quickServer` is faster than manually styling
3. **Leverage Templates**: `\threeTierSetup` saves hours of positioning
4. **Add Legends**: `\addStandardLegend` makes diagrams self-documenting
5. **Consider Accessibility**: Use `\loadAccessiblePreset` for colorblind users
6. **Stack Information**: Combine badges, CVEs, and services for detail
7. **Auto-Position**: Use `\nodeRow`, `\nodeGrid` for consistent layouts
8. **Label Connections**: Use `\labeledConnection` for clarity

---

**All features are production-ready and fully backward compatible!**
