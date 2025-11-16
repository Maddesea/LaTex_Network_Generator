# System Architecture - Module Relationships

## Visual Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                   network_diagram_generator.tex                     │
│                        (Main Entry Point)                           │
│                                                                     │
│  • Document setup                                                   │
│  • Package loading                                                  │
│  • Module orchestration                                             │
│  • Main rendering command                                           │
└───────┬─────────────────────────────────────────────────────────────┘
        │
        │ \input
        │
        ├──────────────────────────────────────────────────────────┐
        │                                                          │
        ├─────────────────────┐                                    │
        │                     │                                    │
┌───────▼────────┐    ┌──────▼──────────┐    ┌──────────▼────────┐  │
│                │    │                 │    │                   │  │
│ styles_config  │───▶│ node_definitions│───▶│ network_layout    │  │
│     .tex       │    │      .tex       │    │      .tex         │  │
│                │    │                 │    │                   │  │
│ • Colors       │    │ • Node commands │    │ • Auto-layout     │  │
│ • Node styles  │    │ • Rendering     │    │ • Subnet grouping │  │
│ • Conn styles  │    │ • Annotations   │    │ • Multi-page      │  │
│ • Page config  │    │ • Metadata      │    │ • Positioning     │  │
│                │    │                 │    │                   │  │
└────────────────┘    └─────────────────┘    └───────────────────┘  │
                                                                     │
        │                                                            │
        │                                                            │
┌───────▼────────┐    ┌──────────────────┐    ┌────────────▼──────┐│
│                │    │                  │    │                   ││
│  connection_   │───▶│ threat_indicators│◀───│  network_data     ││
│   renderer.tex │    │       .tex       │    │       .tex        ││
│                │    │                  │    │                   ││
│ • Draw conns   │    │ • Attacks        │    │ • YOUR NETWORK    ││
│ • Flow viz     │    │ • Vulnerabilities│    │ • Nodes           ││
│ • Protocols    │    │ • IOCs           │    │ • Connections     ││
│ • Routing      │    │ • MITRE ATT&CK   │    │ • Threats         ││
│                │    │                  │    │ • Zones           ││
└────────────────┘    └──────────────────┘    └───────────────────┘│
                                                                     │
        │                                                            │
        │                                                            │
        └────────────────────────────────────────────────────────────┘
                              │
                              │ pdflatex
                              ▼
                    ┌───────────────────┐
                    │  Output PDF/SVG   │
                    │  Professional     │
                    │  Network Diagram  │
                    └───────────────────┘
```

## Module Dependencies

### styles_config.tex (No dependencies)
- Foundation module
- Loaded first
- Provides colors and styles for all other modules

### node_definitions.tex (Depends on: styles_config.tex)
- Uses colors from styles_config
- Uses node styles from styles_config
- Provides node creation commands

### network_layout.tex (Depends on: node_definitions.tex)
- Uses node commands to arrange network
- Provides positioning algorithms
- Handles subnet grouping

### connection_renderer.tex (Depends on: styles_config.tex, node_definitions.tex)
- Uses connection styles from styles_config
- Connects nodes defined by node_definitions
- Provides flow visualization

### threat_indicators.tex (Depends on: styles_config.tex, node_definitions.tex)
- Uses threat colors from styles_config
- Annotates nodes from node_definitions
- Provides security visualization

### network_data.tex (Depends on: ALL above modules)
- Uses commands from all modules
- Defines actual network topology
- **This is where YOU put YOUR network**

## Data Flow

```
User Edit               Module Processing              Output
─────────               ─────────────────              ──────

network_data.tex  ──▶  Main file loads    ──▶  PDF with:
                       all modules              • Styled nodes
Your network:                                   • Connected topology
• Nodes            ──▶  Node commands     ──▶  • Security zones
• Connections           create shapes           • Threat indicators
• Threats               apply styles            • Professional look
• Zones                 route connections
                        render threats
```

## Rendering Pipeline

```
Step 1: Load Styles
─────────────────────
styles_config.tex provides:
  ├─ Color palette
  ├─ Node visual styles
  ├─ Connection styles
  └─ Page configuration

Step 2: Define Node Commands
─────────────────────────────
node_definitions.tex creates:
  ├─ \createServer{...}
  ├─ \createClient{...}
  ├─ \createFirewall{...}
  └─ etc.

Step 3: Setup Layout
────────────────────
network_layout.tex provides:
  ├─ Positioning helpers
  ├─ Zone drawing
  └─ Layout algorithms

Step 4: Connection Tools
─────────────────────────
connection_renderer.tex creates:
  ├─ \drawConnection{...}
  ├─ \drawAttackConnection{...}
  └─ Flow visualization

Step 5: Threat Visualization
─────────────────────────────
threat_indicators.tex provides:
  ├─ \visualizeDDoS{...}
  ├─ \markVulnerability{...}
  └─ Attack indicators

Step 6: Your Network Data
──────────────────────────
network_data.tex calls:
  ├─ renderNetworkNodes()
  ├─ renderConnections()
  ├─ renderThreats()
  └─ drawLegend()

Step 7: Compile
───────────────
pdflatex processes:
  ├─ Loads all modules
  ├─ Executes commands
  ├─ Renders TikZ graphics
  └─ Generates PDF
```

## Parallel Development Strategy

```
                    ┌─────────────────┐
                    │   Main System   │
                    │   (v1.0 Core)   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        │                    │                    │
┌───────▼──────┐    ┌────────▼───────┐   ┌───────▼──────┐
│              │    │                │   │              │
│  Agent 1-2   │    │   Agent 3-4    │   │  Agent 5-6   │
│              │    │                │   │              │
│ Styles &     │    │ Layout &       │   │ Threats &    │
│ Nodes        │    │ Connections    │   │ Data Import  │
│              │    │                │   │              │
│ TODO: 40     │    │ TODO: 35       │   │ TODO: 30     │
│ items        │    │ items          │   │ items        │
└──────────────┘    └────────────────┘   └──────────────┘
        │                    │                    │
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  Enhanced System│
                    │  (v2.0 Future)  │
                    └─────────────────┘
```

## Communication Between Modules

### Direct Dependencies (Must load in order)
1. styles_config.tex  (first - provides foundation)
2. node_definitions.tex (uses styles)
3. network_layout.tex (uses nodes)
4. connection_renderer.tex (uses styles & nodes)
5. threat_indicators.tex (uses styles & nodes)
6. network_data.tex (last - uses everything)

### API Contracts (Function Signatures)

**styles_config.tex exports:**
- Colors: `\definecolor{name}{RGB}{r,g,b}`
- Styles: TikZ style definitions
- Page config: `\setPageSize{size}`

**node_definitions.tex exports:**
- `\createServer{id}{ip}{x}{y}{label}`
- `\createClient{id}{ip}{x}{y}{label}`
- `\createFirewall{id}{ip}{x}{y}{label}`
- etc.

**network_layout.tex exports:**
- `\drawSubnet{name}{color}{nodes}{label}`
- `\drawSecurityZone{name}{color}{nodes}{label}{trust}`
- Auto-layout algorithms (future)

**connection_renderer.tex exports:**
- `\drawConnection{from}{to}{label}`
- `\drawEncryptedConnection{from}{to}{protocol}`
- `\drawAttackConnection{from}{to}{type}`

**threat_indicators.tex exports:**
- `\markVulnerability{node}{cve}{score}`
- `\visualizeDDoS{attackers}{target}{severity}`
- `\addThreatBadge{node}{level}`

**network_data.tex uses:**
- ALL commands from above modules
- Defines: `\renderNetworkNodes`, `\renderConnections`, `\renderThreats`

## Extension Points

### Adding New Node Types
Edit: `node_definitions.tex`
Add: `\newcommand{\createYourNode}[5]{...}`
Uses: Styles from `styles_config.tex`

### Adding New Connection Types
Edit: `connection_renderer.tex`
Add: `\newcommand{\drawYourConnection}[3]{...}`
Uses: Styles from `styles_config.tex`

### Adding New Threat Indicators
Edit: `threat_indicators.tex`
Add: `\newcommand{\visualizeYourAttack}[3]{...}`
Uses: Colors and styles from `styles_config.tex`

### Adding New Color Schemes
Edit: `styles_config.tex`
Add: Colors and update style definitions
No other files need changes!

### Adding New Layout Algorithms
Edit: `network_layout.tex`
Add: `\layoutYourAlgorithm{...}`
Uses: Node commands from `node_definitions.tex`

## Testing Strategy

```
Unit Testing:
├─ Test each module independently
│  ├─ Load only styles_config → compile
│  ├─ Load styles + nodes → compile
│  └─ Load all modules → compile
│
Integration Testing:
├─ Test module combinations
│  ├─ Styles + Nodes + Network Data
│  ├─ Connections + Threats
│  └─ Full system
│
Regression Testing:
└─ Compare PDFs after changes
   ├─ Visual diff
   └─ Byte-level comparison
```

## Build Process

```
Input Files          Compiler           Output
───────────          ────────           ──────

network_diagram_     pdflatex           network_diagram_
generator.tex    ──▶ (LaTeX)       ──▶  generator.pdf
   │                 │  │  │
   ├─ styles_config  │  │  │           Optional:
   ├─ node_defs      │  │  └─▶ dvisvgm  ├─ .svg
   ├─ network_layout │  │               └─ .png
   ├─ connection_    │  └─▶ aux files
   ├─ threat_        │      (cleaned)
   └─ network_data   │
                     │
                compile.sh automates this
```

This architecture enables true parallel development while maintaining clean separation of concerns!
