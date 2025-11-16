#!/usr/bin/env bash
#
# Network Diagram Quick Start Generator
# Creates a new network diagram project with templates
#

set -e

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_header() {
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║    Network Diagram Generator - Quick Start                  ║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}→ $1${NC}"
}

# Generate a basic network template
generate_basic_template() {
    local project_name="$1"

    cat > "${project_name}.json" <<'EOF'
{
  "nodes": [
    {
      "id": "internet",
      "type": "cloud",
      "ip": "0.0.0.0",
      "x": 0,
      "y": 8,
      "label": "Internet"
    },
    {
      "id": "firewall1",
      "type": "firewall",
      "ip": "203.0.113.1",
      "x": 0,
      "y": 6,
      "label": "Edge Firewall"
    },
    {
      "id": "router1",
      "type": "router",
      "ip": "192.168.1.1",
      "x": 0,
      "y": 4,
      "label": "Core Router"
    },
    {
      "id": "server1",
      "type": "server",
      "ip": "192.168.1.10",
      "x": -3,
      "y": 2,
      "label": "Web Server",
      "ports": [80, 443]
    },
    {
      "id": "server2",
      "type": "server",
      "ip": "192.168.1.20",
      "x": 3,
      "y": 2,
      "label": "Database Server",
      "ports": [3306, 5432]
    }
  ],
  "connections": [
    {
      "source": "internet",
      "dest": "firewall1",
      "type": "normal",
      "label": ""
    },
    {
      "source": "firewall1",
      "dest": "router1",
      "type": "normal",
      "label": ""
    },
    {
      "source": "router1",
      "dest": "server1",
      "type": "normal",
      "label": ""
    },
    {
      "source": "router1",
      "dest": "server2",
      "type": "encrypted",
      "label": "TLS 1.3"
    },
    {
      "source": "server1",
      "dest": "server2",
      "type": "encrypted",
      "label": "Database Connection"
    }
  ]
}
EOF

    print_success "Created: ${project_name}.json"
}

# Generate enterprise template
generate_enterprise_template() {
    local project_name="$1"

    cat > "${project_name}.json" <<'EOF'
{
  "nodes": [
    {
      "id": "internet",
      "type": "cloud",
      "ip": "0.0.0.0",
      "x": 0,
      "y": 10,
      "label": "Internet"
    },
    {
      "id": "edge_fw",
      "type": "firewall",
      "ip": "203.0.113.1",
      "x": 0,
      "y": 8,
      "label": "Edge Firewall"
    },
    {
      "id": "dmz_switch",
      "type": "switch",
      "ip": "192.168.10.1",
      "x": 0,
      "y": 6,
      "label": "DMZ Switch"
    },
    {
      "id": "web1",
      "type": "server",
      "ip": "192.168.10.10",
      "x": -4,
      "y": 4,
      "label": "Web Server 1",
      "ports": [80, 443]
    },
    {
      "id": "web2",
      "type": "server",
      "ip": "192.168.10.11",
      "x": -2,
      "y": 4,
      "label": "Web Server 2",
      "ports": [80, 443]
    },
    {
      "id": "lb1",
      "type": "router",
      "ip": "192.168.10.5",
      "x": 0,
      "y": 4,
      "label": "Load Balancer"
    },
    {
      "id": "mail1",
      "type": "server",
      "ip": "192.168.10.20",
      "x": 2,
      "y": 4,
      "label": "Mail Server",
      "ports": [25, 587, 993]
    },
    {
      "id": "dns1",
      "type": "server",
      "ip": "192.168.10.30",
      "x": 4,
      "y": 4,
      "label": "DNS Server",
      "ports": [53]
    },
    {
      "id": "internal_fw",
      "type": "firewall",
      "ip": "192.168.1.1",
      "x": 0,
      "y": 2,
      "label": "Internal Firewall"
    },
    {
      "id": "core_switch",
      "type": "switch",
      "ip": "192.168.100.1",
      "x": 0,
      "y": 0,
      "label": "Core Switch"
    },
    {
      "id": "app1",
      "type": "server",
      "ip": "192.168.100.10",
      "x": -3,
      "y": -2,
      "label": "App Server 1"
    },
    {
      "id": "app2",
      "type": "server",
      "ip": "192.168.100.11",
      "x": 0,
      "y": -2,
      "label": "App Server 2"
    },
    {
      "id": "db_primary",
      "type": "server",
      "ip": "192.168.200.10",
      "x": 3,
      "y": -2,
      "label": "DB Primary",
      "ports": [3306]
    },
    {
      "id": "db_replica",
      "type": "server",
      "ip": "192.168.200.11",
      "x": 5,
      "y": -2,
      "label": "DB Replica",
      "ports": [3306]
    }
  ],
  "connections": [
    {"source": "internet", "dest": "edge_fw", "type": "normal", "label": ""},
    {"source": "edge_fw", "dest": "dmz_switch", "type": "normal", "label": ""},
    {"source": "dmz_switch", "dest": "lb1", "type": "normal", "label": ""},
    {"source": "lb1", "dest": "web1", "type": "normal", "label": ""},
    {"source": "lb1", "dest": "web2", "type": "normal", "label": ""},
    {"source": "dmz_switch", "dest": "mail1", "type": "normal", "label": ""},
    {"source": "dmz_switch", "dest": "dns1", "type": "normal", "label": ""},
    {"source": "dmz_switch", "dest": "internal_fw", "type": "normal", "label": ""},
    {"source": "internal_fw", "dest": "core_switch", "type": "normal", "label": ""},
    {"source": "core_switch", "dest": "app1", "type": "normal", "label": ""},
    {"source": "core_switch", "dest": "app2", "type": "normal", "label": ""},
    {"source": "core_switch", "dest": "db_primary", "type": "encrypted", "label": "TLS"},
    {"source": "app1", "dest": "db_primary", "type": "encrypted", "label": "SQL/TLS"},
    {"source": "app2", "dest": "db_primary", "type": "encrypted", "label": "SQL/TLS"},
    {"source": "db_primary", "dest": "db_replica", "type": "normal", "label": "Replication"}
  ]
}
EOF

    print_success "Created: ${project_name}.json (Enterprise template)"
}

# Generate LaTeX file
generate_latex_file() {
    local project_name="$1"

    cat > "${project_name}.tex" <<EOF
% ${project_name}.tex
% Auto-generated by quickstart.sh

\\documentclass[tikz,border=10pt]{standalone}

% Core packages
\\usepackage{tikz}
\\usepackage{ifthen}
\\usepackage{xcolor}
\\usepackage{calc}

% TikZ libraries
\\usetikzlibrary{
    positioning,
    shapes.geometric,
    shapes.multipart,
    arrows.meta,
    decorations.pathmorphing,
    decorations.markings,
    backgrounds,
    fit,
    calc,
    shadows.blur,
    patterns,
    fadings
}

% Import modular components
\\input{styles_config}
\\input{node_definitions}
\\input{network_layout}
\\input{connection_renderer}
\\input{threat_indicators}
\\input{data_import}

\\begin{document}
    % Import network topology from JSON
    \\importJSON{${project_name}.json}

    \\begin{tikzpicture}[
        scale=1.0,
        transform shape,
        font=\\sffamily
    ]
        % Render the imported network
        \\renderNetworkNodes
        \\renderConnections

        % Optional: Add legend
        \\node[legend box, anchor=south west] at (-10,-12) {
            \\small\\bfseries Legend \\\\[2pt]
            \\begin{tabular}{ll}
                \\tikz\\draw[normal conn] (0,0) -- (0.5,0); & Normal \\\\
                \\tikz\\draw[encrypted conn] (0,0) -- (0.5,0); & Encrypted \\\\
            \\end{tabular}
        };

        % Optional: Add metadata
        \\node[font=\\tiny, anchor=south east, text=black!60] at (10,-12) {
            ${project_name} \\\\
            Generated: \\today
        };

    \\end{tikzpicture}
\\end{document}
EOF

    print_success "Created: ${project_name}.tex"
}

# Generate Makefile
generate_makefile() {
    local project_name="$1"

    cat > "Makefile" <<EOF
# Makefile for ${project_name}

.PHONY: all clean view

all: ${project_name}.pdf

${project_name}.pdf: ${project_name}.tex ${project_name}.json
	lualatex ${project_name}.tex
	lualatex ${project_name}.tex

clean:
	rm -f *.aux *.log *.out *.toc
	rm -f ${project_name}.pdf

view: ${project_name}.pdf
	@if command -v xdg-open > /dev/null; then \\
		xdg-open ${project_name}.pdf; \\
	elif command -v open > /dev/null; then \\
		open ${project_name}.pdf; \\
	else \\
		echo "Please open ${project_name}.pdf manually"; \\
	fi

export: ${project_name}.json
	@echo "Exporting to multiple formats..."
	python3 ../examples/convert_network_data.py ${project_name}.json ${project_name}.yaml
	@echo "✓ Exported to YAML"

help:
	@echo "Available targets:"
	@echo "  make        - Build the diagram PDF"
	@echo "  make clean  - Remove build artifacts"
	@echo "  make view   - Open the PDF"
	@echo "  make export - Export to other formats"
EOF

    print_success "Created: Makefile"
}

# Generate README
generate_readme() {
    local project_name="$1"

    cat > "README.md" <<EOF
# ${project_name}

Network diagram project generated by the LaTeX Network Diagram Generator.

## Quick Start

\`\`\`bash
# Build the diagram
make

# View the PDF
make view

# Clean build artifacts
make clean
\`\`\`

## Files

- **${project_name}.json** - Network topology data
- **${project_name}.tex** - LaTeX diagram source
- **Makefile** - Build automation

## Editing

### Modify Network Topology

Edit \`${project_name}.json\` to change:
- Nodes (servers, firewalls, routers, etc.)
- Connections between nodes
- IP addresses and labels

### Compile

\`\`\`bash
lualatex ${project_name}.tex
\`\`\`

Or use the Makefile:

\`\`\`bash
make
\`\`\`

## Export to Other Formats

\`\`\`bash
# Export to YAML
python3 ../examples/convert_network_data.py ${project_name}.json ${project_name}.yaml

# Export to GraphML (for Gephi)
# (Add export commands in LaTeX file)
\`\`\`

## Documentation

See the main project README for full documentation:
- JSON schema reference
- Available node types
- Connection types
- Advanced features

## Requirements

- LuaLaTeX
- Python 3 (for data conversion)
- Make (optional, but recommended)

EOF

    print_success "Created: README.md"
}

# Main function
main() {
    print_header

    echo "Welcome to the Network Diagram Quick Start Generator!"
    echo
    echo "This tool will create a new network diagram project with templates."
    echo

    # Get project name
    read -p "Enter project name (e.g., my_network): " project_name

    if [ -z "$project_name" ]; then
        echo "Error: Project name cannot be empty"
        exit 1
    fi

    # Create project directory
    mkdir -p "$project_name"
    cd "$project_name"

    print_info "Creating project in: $(pwd)"
    echo

    # Ask for template type
    echo "Select a template:"
    echo "  1) Basic (Simple network with firewall, router, servers)"
    echo "  2) Enterprise (Multi-tier with DMZ, load balancer, databases)"
    echo "  3) Empty (Start from scratch)"
    echo
    read -p "Choose template [1-3]: " template_choice

    case "$template_choice" in
        1)
            generate_basic_template "$project_name"
            ;;
        2)
            generate_enterprise_template "$project_name"
            ;;
        3)
            echo '{"nodes": [], "connections": []}' > "${project_name}.json"
            print_success "Created: ${project_name}.json (empty template)"
            ;;
        *)
            echo "Invalid choice. Using basic template."
            generate_basic_template "$project_name"
            ;;
    esac

    # Generate supporting files
    generate_latex_file "$project_name"
    generate_makefile "$project_name"
    generate_readme "$project_name"

    echo
    print_success "Project created successfully!"
    echo
    echo "Next steps:"
    echo "  cd $project_name"
    echo "  make              # Build the diagram"
    echo "  make view         # View the PDF"
    echo
    echo "Edit ${project_name}.json to customize your network diagram."
    echo
}

main "$@"
