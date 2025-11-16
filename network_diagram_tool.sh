#!/usr/bin/env bash
#
# Network Diagram Automation Suite
# Automates common workflows for network diagram generation
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXAMPLES_DIR="$PROJECT_DIR/examples"

# Helper functions
print_header() {
    echo -e "${BLUE}=== $1 ===${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}! $1${NC}"
}

# Function: Generate network diagram from Nmap scan
nmap_to_diagram() {
    local nmap_file="$1"
    local output_name="${2:-network_diagram}"

    print_header "Converting Nmap scan to network diagram"

    if [ ! -f "$nmap_file" ]; then
        print_error "Nmap file not found: $nmap_file"
        return 1
    fi

    # Convert Nmap to JSON
    print_warning "Converting Nmap XML to JSON..."
    python3 "$EXAMPLES_DIR/convert_network_data.py" "$nmap_file" "${output_name}.json"

    # Generate LaTeX diagram
    print_warning "Generating LaTeX diagram..."
    cat > "${output_name}.tex" <<EOF
\\documentclass[tikz,border=10pt]{standalone}
\\usepackage{tikz}
\\usepackage{ifthen}
\\usepackage{xcolor}
\\usepackage{calc}

\\usetikzlibrary{
    positioning, shapes.geometric, shapes.multipart,
    arrows.meta, decorations.pathmorphing, decorations.markings,
    backgrounds, fit, calc, shadows.blur, patterns, fadings
}

\\input{styles_config}
\\input{node_definitions}
\\input{network_layout}
\\input{connection_renderer}
\\input{threat_indicators}
\\input{data_import}

\\begin{document}
    \\importJSON{${output_name}.json}

    \\begin{tikzpicture}[scale=1.0, transform shape, font=\\sffamily]
        \\renderNetworkNodes
        \\renderConnections

        \\node[font=\\tiny, anchor=south east, text=black!60] at (10,-10) {
            Generated from Nmap scan \\\\
            \\today
        };
    \\end{tikzpicture}
\\end{document}
EOF

    # Compile diagram
    print_warning "Compiling diagram with LuaLaTeX..."
    cd "$PROJECT_DIR"
    lualatex -interaction=nonstopmode "${output_name}.tex" > /dev/null 2>&1

    if [ -f "${output_name}.pdf" ]; then
        print_success "Diagram generated: ${output_name}.pdf"
        print_success "JSON data saved: ${output_name}.json"
    else
        print_error "LaTeX compilation failed!"
        return 1
    fi
}

# Function: Generate diagram from Nessus scan
nessus_to_diagram() {
    local nessus_file="$1"
    local output_name="${2:-vulnerability_report}"

    print_header "Converting Nessus scan to vulnerability diagram"

    if [ ! -f "$nessus_file" ]; then
        print_error "Nessus file not found: $nessus_file"
        return 1
    fi

    # Convert Nessus to JSON
    print_warning "Converting Nessus XML to JSON..."
    python3 "$EXAMPLES_DIR/convert_network_data.py" "$nessus_file" "${output_name}.json"

    # Generate LaTeX diagram
    print_warning "Generating vulnerability diagram..."
    cat > "${output_name}.tex" <<EOF
\\documentclass[tikz,border=10pt]{standalone}
\\usepackage{tikz}
\\usepackage{ifthen}
\\usepackage{xcolor}
\\usepackage{calc}

\\usetikzlibrary{
    positioning, shapes.geometric, shapes.multipart,
    arrows.meta, decorations.pathmorphing, decorations.markings,
    backgrounds, fit, calc, shadows.blur, patterns, fadings
}

\\input{styles_config}
\\input{node_definitions}
\\input{network_layout}
\\input{connection_renderer}
\\input{threat_indicators}
\\input{data_import}

\\begin{document}
    \\importJSON{${output_name}.json}

    \\begin{tikzpicture}[scale=1.0, transform shape, font=\\sffamily]
        \\renderNetworkNodes
        \\renderConnections

        % Filter for high-severity vulnerabilities only
        \\filterVulnerabilitiesByCVSS{7.0}{${output_name}.json}

        \\node[font=\\small, anchor=north west, text=red!80] at (-10,10) {
            \\textbf{VULNERABILITY REPORT} \\\\
            High \& Critical Findings Only
        };

        \\node[font=\\tiny, anchor=south east, text=black!60] at (10,-10) {
            Generated from Nessus scan \\\\
            \\today
        };
    \\end{tikzpicture}
\\end{document}
EOF

    # Compile diagram
    print_warning "Compiling vulnerability report..."
    cd "$PROJECT_DIR"
    lualatex -interaction=nonstopmode "${output_name}.tex" > /dev/null 2>&1

    if [ -f "${output_name}.pdf" ]; then
        print_success "Vulnerability diagram generated: ${output_name}.pdf"
    else
        print_error "LaTeX compilation failed!"
        return 1
    fi
}

# Function: Batch process multiple scans
batch_process() {
    local scan_dir="$1"
    local output_dir="${2:-./diagrams}"

    print_header "Batch processing network scans"

    if [ ! -d "$scan_dir" ]; then
        print_error "Scan directory not found: $scan_dir"
        return 1
    fi

    mkdir -p "$output_dir"

    local count=0
    # Process Nmap scans
    for nmap_file in "$scan_dir"/*.xml; do
        [ -e "$nmap_file" ] || continue
        local basename=$(basename "$nmap_file" .xml)
        print_warning "Processing: $basename"
        nmap_to_diagram "$nmap_file" "$output_dir/$basename"
        ((count++))
    done

    # Process Nessus scans
    for nessus_file in "$scan_dir"/*.nessus; do
        [ -e "$nessus_file" ] || continue
        local basename=$(basename "$nessus_file" .nessus)
        print_warning "Processing: $basename"
        nessus_to_diagram "$nessus_file" "$output_dir/${basename}_vulns"
        ((count++))
    done

    print_success "Batch processed $count scan files"
    print_success "Output directory: $output_dir"
}

# Function: Merge multiple network data files
merge_networks() {
    print_header "Merging multiple network data files"

    local output_file="$1"
    shift
    local files=("$@")

    if [ ${#files[@]} -lt 2 ]; then
        print_error "Need at least 2 files to merge"
        return 1
    fi

    print_warning "Merging ${#files[@]} files..."

    # Use Python to merge
    python3 << EOF
import json
import sys

merged = {"nodes": [], "connections": [], "threats": []}

for filename in ${files[@]}:
    with open(filename, 'r') as f:
        data = json.load(f)
        if 'nodes' in data:
            merged['nodes'].extend(data['nodes'])
        if 'connections' in data:
            merged['connections'].extend(data['connections'])
        if 'threats' in data:
            merged['threats'].extend(data['threats'])

with open('$output_file', 'w') as f:
    json.dump(merged, f, indent=2)

print(f"Merged {len(merged['nodes'])} nodes, {len(merged['connections'])} connections")
EOF

    print_success "Merged data saved to: $output_file"
}

# Function: Export to multiple formats
export_diagram() {
    local json_file="$1"
    local basename="${json_file%.json}"

    print_header "Exporting diagram to multiple formats"

    if [ ! -f "$json_file" ]; then
        print_error "JSON file not found: $json_file"
        return 1
    fi

    # Create export LaTeX file
    cat > "${basename}_export.tex" <<EOF
\\documentclass{article}
\\usepackage{luacode}
\\input{data_import}

\\begin{document}
\\exportToGraphML{${basename}.graphml}{$json_file}
\\exportToDOT{${basename}.dot}{$json_file}
\\end{document}
EOF

    lualatex "${basename}_export.tex" > /dev/null 2>&1

    # Export to PNG using GraphViz
    if [ -f "${basename}.dot" ]; then
        if command -v dot &> /dev/null; then
            dot -Tpng "${basename}.dot" -o "${basename}.png"
            print_success "PNG exported: ${basename}.png"
        fi

        if command -v dot &> /dev/null; then
            dot -Tsvg "${basename}.dot" -o "${basename}.svg"
            print_success "SVG exported: ${basename}.svg"
        fi
    fi

    [ -f "${basename}.graphml" ] && print_success "GraphML exported: ${basename}.graphml"
    [ -f "${basename}.dot" ] && print_success "DOT exported: ${basename}.dot"

    # Cleanup
    rm -f "${basename}_export.tex" "${basename}_export.aux" "${basename}_export.log"
}

# Function: Show help
show_help() {
    cat << EOF
Network Diagram Automation Suite

Usage: $0 <command> [options]

Commands:
    nmap <file.xml> [output_name]
        Generate diagram from Nmap scan

    nessus <file.nessus> [output_name]
        Generate vulnerability diagram from Nessus scan

    batch <scan_directory> [output_directory]
        Batch process all scans in directory

    merge <output.json> <file1.json> <file2.json> ...
        Merge multiple network data files

    export <file.json>
        Export diagram to multiple formats (GraphML, DOT, PNG, SVG)

    help
        Show this help message

Examples:
    # Generate diagram from Nmap scan
    $0 nmap scan_results.xml my_network

    # Generate vulnerability report from Nessus
    $0 nessus scan.nessus vuln_report

    # Batch process all scans
    $0 batch ./scans ./output_diagrams

    # Merge two networks
    $0 merge combined.json network1.json network2.json

    # Export to all formats
    $0 export network.json

Requirements:
    - LuaLaTeX
    - Python 3
    - GraphViz (optional, for PNG/SVG export)

EOF
}

# Main command dispatcher
main() {
    if [ $# -eq 0 ]; then
        show_help
        exit 0
    fi

    local command="$1"
    shift

    case "$command" in
        nmap)
            nmap_to_diagram "$@"
            ;;
        nessus)
            nessus_to_diagram "$@"
            ;;
        batch)
            batch_process "$@"
            ;;
        merge)
            merge_networks "$@"
            ;;
        export)
            export_diagram "$@"
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            print_error "Unknown command: $command"
            echo
            show_help
            exit 1
            ;;
    esac
}

main "$@"
