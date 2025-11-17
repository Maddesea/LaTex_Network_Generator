# Agent 3 Quick Reference Guide

## Essential Safety Functions

### Safe Mathematical Operations
```latex
% Safe division with fallback
\safeDivide{10}{0}{999}{\result}  % Returns 999 if divisor is 0

% Safe square root (handles negative inputs)
\safeSqrt{-5}{\result}  % Returns 0

% Safe modulo
\safeMod{7}{0}{\result}  % Protects against division by zero
```

### Value Validation
```latex
% Clamp value to range
\clampValue{150}{0}{100}{\result}  % Returns 100

% Check if two values are close
\isNearValue{5.0}{5.001}{0.01}  % Returns 1 (true)

% Validate coordinates
\validateCoordinate{10}{20}{1000}  % Returns 1 if valid
```

## Layout Optimization

### Smart Spacing
```latex
% Automatically calculate optimal spacing
\calculateSmartSpacing{50}{120}{100}{1.0}
% Parameters: nodes, connections, area, complexity_weight
% Sets \nodeSpacing and \layerSpacing automatically
```

### Auto-Fix Layout Issues
```latex
% Fix overlaps, balance, and optimize
\autoFixLayout{true}  % true = aggressive fixes
\autoFixLayout{false} % false = conservative fixes
```

### Detect Optimal Layout Type
```latex
\detectOptimalLayout{25}{60}
% Returns: grid, tree, circular, force, or tiered
% Stored in \recommendedlayout
```

## Collision Handling

### Quick Collision Detection
```latex
% Check if two nodes collide
\checkNodeCollision{node1}{node2}
\ifnodecollision
    % Collision detected
\else
    % No collision
\fi
```

### Collision Resolution
```latex
% Resolve all collisions iteratively
\resolveCollisionsIterative{10}{0.8}
% Parameters: max_iterations, learning_rate

% Quick fix for single node
\quickFixNodeCollision{node1}{auto}{2cm}
% Directions: auto, up, down, left, right

% Ensure minimum clearance
\ensureClearance{node1}{2cm}{5}
% Parameters: node, min_distance, max_iterations
```

## Geometric Calculations

### Distance and Angle
```latex
% Calculate distance between nodes
\calculateNodeDistance{node1}{node2}{\distance}
% Result in cm

% Calculate angle from node1 to node2
\calculateAngle{node1}{node2}{\angle}
% Result in degrees
```

### Positioning Helpers
```latex
% Position node equidistant from three anchors
\positionEquidistant{newnode}{anchor1}{anchor2}{anchor3}

% Find optimal position near reference nodes
\findOptimalPosition{ref_nodes}{3cm}

% Balance edge lengths
\balanceEdgeLengths{node}{connected_nodes}
```

## Layout Templates

### Quick Setup Presets
```latex
% Enterprise network best practices
\applyEnterpriseBestPractices

% Microservices architecture
\applyMicroservicesLayout

% IoT network with many devices
\applyIoTLayout{100}  % 100 devices
```

## Layout Quality

### Measure Quality
```latex
% Get aesthetic score (0-100)
\calculateAestheticScore{50}{120}
% Parameters: node_count, connection_count

% Count edge crossings
\countEdgeCrossings

% Check diagram balance
\calculateDiagramBalance

% Measure spacing uniformity
\measureSpacingUniformity
```

### Optimization
```latex
% Optimize spacing distribution
\optimizeSpacing

% Reduce edge crossings
\reduceCrossings{5}  % max 5 swaps

% Snap to grid
\snapAllNodesToGrid{1cm}
```

## Caching and Performance

### Layout Caching
```latex
% Save current layout
\cacheLayout{mylayout}

% Restore saved layout
\restoreLayout{mylayout}

% Incremental update (faster)
\updateLayoutIncremental{changed_nodes}
```

## Debugging and Diagnostics

### Diagnostic Tools
```latex
% Generate comprehensive report
\generateDiagnosticReport
% Outputs to console

% Enable visual debugging
\enableDebugOverlay
% Shows coordinate system and bounding box

% Profile performance
\profileLayoutPerformance
% Estimates compilation complexity

% Validate configuration
\validateLayoutConfiguration
% Checks all parameters
```

## Common Use Cases

### Case 1: Complex Network with Overlaps
```latex
% Problem: 100 nodes, many overlapping
\calculateSmartSpacing{100}{250}{200}{1.2}
\autoFixLayout{true}
\generateDiagnosticReport
```

### Case 2: Perfect Enterprise Layout
```latex
% One-command professional layout
\applyEnterpriseBestPractices
\autoFixLayout{false}
```

### Case 3: Custom Layout with Safety
```latex
% Manual layout with safety checks
\safeDivide{\nodecount}{\tiercount}{1}{\nodespertier}
\clampValue{\spacing}{1cm}{10cm}{\safespacing}
\ensureClearance{newnode}{2cm}{10}
```

### Case 4: Troubleshooting Layout Issues
```latex
% Debug mode
\enableDebugMode
\enableDebugOverlay
\generateDiagnosticReport
\profileLayoutPerformance
```

### Case 5: IoT Network with 200 Devices
```latex
% Optimized for many nodes
\applyIoTLayout{200}
\calculateSmartSpacing{200}{400}{300}{0.8}
\optimizePerformance{200}
```

## Error Prevention

### Before (Error-Prone)
```latex
% Dangerous: Can crash
\pgfmathsetmacro{\result}{#1 / #2}
\pgfmathsetmacro{\angle}{360 / (#3 - 1)}
```

### After (Safe)
```latex
% Safe: Always works
\safeDivide{#1}{#2}{0}{\result}
\pgfmathsetmacro{\divisor}{max(#3 - 1, 1)}
\pgfmathsetmacro{\angle}{360 / \divisor}
```

## Performance Tips

1. **Use caching for large diagrams**:
   ```latex
   \cacheLayout{main}
   % ... make changes ...
   \updateLayoutIncremental{changed_nodes}
   ```

2. **Optimize for your node count**:
   ```latex
   \pgfmathparse{#nodes > 100 ? 1 : 0}
   \ifnum\pgfmathresult=1
       \optimizePerformance{#nodes}
   \fi
   ```

3. **Use appropriate layout type**:
   ```latex
   \detectOptimalLayout{#nodes}{#connections}
   % Use \recommendedlayout result
   ```

## Best Practices

✅ **DO**:
- Always use safety functions for calculations
- Validate inputs before processing
- Use smart spacing for automatic optimization
- Apply appropriate layout presets
- Run diagnostics on complex layouts
- Cache layouts for reuse

❌ **DON'T**:
- Divide without checking for zero
- Skip input validation
- Use hard-coded spacing for all cases
- Ignore collision warnings
- Forget to validate coordinates

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Nodes overlapping | `\autoFixLayout{true}` |
| Spacing too tight | `\calculateSmartSpacing{...}` |
| Division by zero | Use `\safeDivide{...}` |
| Layout looks poor | `\applyEnterpriseBestPractices` |
| Slow compilation | `\cacheLayout{...}` + `\updateLayoutIncremental{...}` |
| Can't find issue | `\generateDiagnosticReport` |
| Need debugging info | `\enableDebugOverlay` |

## Function Categories

- **Safety**: 6 functions
- **Layout Optimization**: 5 functions
- **Collision**: 4 functions
- **Geometric**: 4 functions
- **Quality Metrics**: 4 functions
- **Auto-fix**: 4 functions
- **Caching**: 3 functions
- **Positioning**: 4 functions
- **Templates**: 3 functions
- **Debugging**: 4 functions
- **Validation**: 1 comprehensive function

**Total: 42 utility functions**

---

**Quick Start**: For most users, just use:
```latex
\applyEnterpriseBestPractices
\calculateSmartSpacing{nodes}{connections}{area}{1.0}
\autoFixLayout{false}
```

For detailed examples, see `test_agent3_improvements.tex`.

For complete documentation, see `AGENT3_IMPROVEMENTS_V2.md`.
