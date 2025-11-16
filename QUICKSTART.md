# LaTeX Network Diagram Generator - Quick Start Guide

This guide will get you creating professional network diagrams in 5 minutes!

## 🚀 5-Minute Quick Start

### Step 1: Create Your First Diagram (30 seconds)

```latex
% my_network.tex
\renewcommand{\renderNetworkNodes}{
    % Create a simple 3-node network
    \createServer{web1}{192.168.1.10}{-3}{3}{Web Server}
    \createDatabase{db1}{192.168.1.20}{0}{0}{Database}
    \createClient{pc1}{192.168.1.100}{3}{-3}{Workstation}
}

\renewcommand{\renderConnections}{
    \draw[encrypted conn] (web1) -- (db1);
    \draw[normal conn] (pc1) -- (web1);
}
```

### Step 2: Compile (10 seconds)

```bash
pdflatex network_diagram_generator.tex
```

### Step 3: View Result

Open `network_diagram_generator.pdf` - you now have a professional network diagram!

---

## 📋 Common Use Cases

### Use Case 1: Web Application Architecture (2 minutes)

**Goal:** Document a 3-tier web application

```latex
% Option A: Use the template (fastest!)
\input{topology_templates}
\createThreeTierApp{prod}{192.168}
\drawTemplateLegend{3-Tier Architecture}

% Option B: Manual creation (more control)
\createLoadBalancerActive{lb1}{192.168.10.10}{0}{6}{Load Balancer}{round-robin}
\createNodeWithMetrics{web1}{192.168.20.10}{-3}{3}{Web-01}{45}{60}{35}
\createNodeWithMetrics{web2}{192.168.20.11}{0}{3}{Web-02}{50}{65}{38}
\createNodeWithMetrics{web3}{192.168.20.12}{3}{3}{Web-03}{42}{58}{33}
\createServer{app1}{192.168.30.10}{0}{0}{App Server}
\createDatabasePrimary{db1}{192.168.40.10}{0}{-3}{DB Primary}
```

### Use Case 2: Security Assessment Diagram (3 minutes)

**Goal:** Show DMZ, firewalls, and security zones

```latex
\input{topology_templates}
\createSecureDMZ{corp}{203.0.113}{10.0.0}{192.168.1}
\drawTemplateLegend{Secure DMZ}
```

### Use Case 3: IoT Smart Home (2 minutes)

```latex
\input{topology_templates}
\createSmartHome{home}{192.168.50}
\drawTemplateLegend{Smart Home IoT}
```

### Use Case 4: Cloud Hybrid Architecture (3 minutes)

```latex
\input{topology_templates}
\createHybridCloud{hybrid}{172.16.0}{aws}
\drawTemplateLegend{Hybrid Cloud}
```

---

## 🎨 Customization Examples

### Add OS Badges and Status

```latex
\createServer{web1}{192.168.1.10}{0}{0}{Web Server}
\addOSBadge{web1}{ubuntu}
\addStatusIndicator{web1}{online}
\addVersionInfo{web1}{2.4.51}
\addUptime{web1}{127}
```

### Create Bulk Nodes

```latex
% Create 5 web servers in a row
\createNodeRow{server}{web}{192.168.10}{3}{5}{Web Server}

% Create a 3x3 grid of servers
\createNodeGrid{server}{node}{192.168.20}{0}{0}{3}{3}

% Create star topology (1 router, 8 clients)
\createStarTopology{office}{router}{client}{192.168.1}{8}
```

### Use Node Templates

```latex
% Pre-configured stacks
\createWebServerStack{web1}{192.168.1.10}{0}{3}
\createAppServerStack{app1}{192.168.1.20}{0}{0}
\createMonitoringServer{mon1}{192.168.1.30}{0}{-3}
\createLogServer{log1}{192.168.1.40}{3}{-3}
\createDomainController{dc1}{192.168.1.5}{-3}{3}
```

### Group Nodes into Subnets

```latex
\createServer{web1}{192.168.10.10}{-3}{0}{Web-01}
\createServer{web2}{192.168.10.11}{0}{0}{Web-02}
\createServer{web3}{192.168.10.12}{3}{0}{Web-03}

\begin{scope}[on background layer]
    \createSubnet{webnet}{Web Tier}{192.168.10.0/24}{(web1)(web2)(web3)}{high}
\end{scope}
```

---

## 🔧 All Available Node Types

### Infrastructure
```latex
\createServer{name}{ip}{x}{y}{label}
\createRouter{name}{ip}{x}{y}{label}
\createSwitch{name}{ip}{x}{y}{label}
\createFirewall{name}{ip}{x}{y}{label}
```

### Databases
```latex
\createDatabase{name}{ip}{x}{y}{label}
\createDatabasePrimary{name}{ip}{x}{y}{label}
\createDatabaseReplica{name}{ip}{x}{y}{label}
\createDatabaseCluster{name}{ip}{x}{y}{label}
```

### Load Balancers
```latex
\createLoadBalancer{name}{ip}{x}{y}{label}
\createLoadBalancerActive{name}{ip}{x}{y}{label}{algorithm}
\createLoadBalancerPassive{name}{ip}{x}{y}{label}
```

### Virtualization
```latex
\createVM{name}{ip}{x}{y}{label}{hypervisor}
\createHypervisor{name}{ip}{x}{y}{label}{vmcount}
\createVMWithResources{name}{ip}{x}{y}{label}{cpu}{ram}{disk}
```

### Containers
```latex
\createContainer{name}{ip}{x}{y}{label}{image}
\createPod{name}{ip}{x}{y}{label}{namespace}
\createContainerWithPorts{name}{ip}{x}{y}{label}{ports}
```

### Cloud
```latex
\createAWSNode{name}{x}{y}{label}{service}
\createAzureNode{name}{x}{y}{label}{service}
\createGCPNode{name}{x}{y}{label}{service}
```

### Security Appliances
```latex
\createIPS{name}{ip}{x}{y}{label}{mode}
\createWAF{name}{ip}{x}{y}{label}{ruleset}
\createProxy{name}{ip}{x}{y}{label}{type}
```

### Storage
```latex
\createNAS{name}{ip}{x}{y}{label}{capacity}{protocol}
\createSAN{name}{ip}{x}{y}{label}{capacity}{protocol}
\createStorage{name}{ip}{x}{y}{label}{capacity}
```

### Mobile & IoT
```latex
\createMobilePhone{name}{ip}{x}{y}{label}{os}
\createTablet{name}{ip}{x}{y}{label}{os}
\createLaptop{name}{ip}{x}{y}{label}{user}
\createIoTDevice{name}{ip}{x}{y}{label}{type}
\createSensor{name}{ip}{x}{y}{label}{sensortype}
\createWirelessAP{name}{ip}{x}{y}{label}{ssid}
```

### Advanced Nodes
```latex
\createNodeWithMetrics{name}{ip}{x}{y}{hostname}{cpu}{mem}{disk}
\createNodeWithServices{name}{ip}{x}{y}{hostname}{ports}{services}
\createSecurityNode{name}{ip}{x}{y}{hostname}{vulns}{cvss}{status}
```

---

## 🔗 Connection Types

```latex
% Basic connections
\draw[normal conn] (node1) -- (node2);
\draw[encrypted conn] (node1) -- (node2);
\draw[suspicious conn] (node1) -- (node2);
\draw[attack conn] (node1) -- (node2);
\draw[bidirectional] (node1) -- (node2);

% With labels
\labelConnection{node1}{node2}{HTTPS}
\drawConnectionWithPorts{web1}{db1}{443}{5432}

% Highlight critical path
\highlightPath{client,firewall,web,app,database}
```

---

## 💡 Pro Tips

### Tip 1: Start with Templates
```latex
\input{topology_templates}
\createThreeTierApp{myapp}{192.168}
% Then customize from there
```

### Tip 2: Use Meaningful Names
```latex
% Good - descriptive names
\createServer{web_prod_01}{192.168.1.10}{0}{0}{Production Web 01}

% Avoid - generic names
\createServer{s1}{192.168.1.10}{0}{0}{Server}
```

### Tip 3: Consistent IP Addressing
```latex
% Use logical IP blocks
% 192.168.10.x - Web tier
% 192.168.20.x - App tier
% 192.168.30.x - Database tier
```

### Tip 4: Layer Your Diagrams
```latex
% Background elements first
\begin{scope}[on background layer]
    \createSubnet{...}
    \createCluster{...}
\end{scope}

% Then nodes
\createServer{...}

% Then connections
\draw[normal conn] ...
```

### Tip 5: Add Documentation
```latex
\diagramTitle{Production Network}{Last Updated: \today}
\drawTemplateLegend{Architecture Type}
\addComplianceBadge{8}{8}{pci}
```

---

## 📊 Complete Example

```latex
% complete_example.tex
\input{topology_templates}

\begin{tikzpicture}
    % Title
    \diagramTitle{Production Web Application}{3-Tier Architecture with HA}

    % DMZ Layer
    \createFirewall{fw1}{203.0.113.1}{0}{8}{Edge Firewall}
    \createWAF{waf1}{203.0.113.10}{0}{6}{WAF-01}{OWASP}

    % Load Balancers (HA Pair)
    \createLoadBalancerActive{lb1}{192.168.10.10}{-2}{4}{LB-Primary}{round-robin}
    \createLoadBalancerPassive{lb2}{192.168.10.11}{2}{4}{LB-Standby}

    % Web Tier (3 servers with metrics)
    \createNodeWithMetrics{web1}{192.168.20.10}{-4}{2}{Web-01}{45}{60}{35}
    \createNodeWithMetrics{web2}{192.168.20.11}{0}{2}{Web-02}{50}{65}{38}
    \createNodeWithMetrics{web3}{192.168.20.12}{4}{2}{Web-03}{42}{58}{33}

    % Add OS badges and status
    \addOSBadge{web1}{ubuntu}
    \addOSBadge{web2}{ubuntu}
    \addOSBadge{web3}{ubuntu}
    \addStatusIndicator{web1}{online}
    \addStatusIndicator{web2}{online}
    \addStatusIndicator{web3}{online}

    % App Tier (using templates)
    \createAppServerStack{app1}{192.168.30.10}{0}{0}

    % Database Tier (Master-Slave)
    \createDBMasterSlave{db}{192.168.40.10}{192.168.40.11}{-2}

    % Storage
    \createNAS{nas1}{192.168.50.10}{0}{-5}{Storage}{100TB}{NFS}

    % Connections
    \draw[encrypted conn] (fw1) -- (waf1);
    \draw[encrypted conn] (waf1) -- (lb1);
    \draw[normal conn] (lb1) -- (web1);
    \draw[normal conn] (lb1) -- (web2);
    \draw[normal conn] (lb1) -- (web3);
    \draw[encrypted conn] (web1) -- (app1);
    \draw[encrypted conn] (web2) -- (app1);
    \draw[encrypted conn] (web3) -- (app1);
    \draw[encrypted conn] (app1) -- (db_master);
    \draw[normal conn] (app1) -- (nas1);

    % Subnets
    \begin{scope}[on background layer]
        \createSubnet{webnet}{Web Tier}{192.168.20.0/24}{(web1)(web2)(web3)}{high}
        \createSubnet{appnet}{App Tier}{192.168.30.0/24}{(app1)}{high}
        \createHAPair{lbha}{LB HA Pair}{(lb1)}{(lb2)}
    \end{scope}

    % Legend and Compliance
    \drawTemplateLegend{3-Tier HA Architecture}
    \addComplianceBadge{8}{8}{pci}
\end{tikzpicture}
```

---

## 🆘 Common Issues & Solutions

### Issue: Nodes Overlapping
```latex
% Solution: Adjust spacing or use auto-layout
\createNodeRow{server}{web}{192.168.1}{3}{5}{Web}  % Auto-spaces
```

### Issue: Can't See All Nodes
```latex
% Solution: Adjust page size
\renewcommand{\pageSize}{a3}  % Or a2, a1, a0
\setPageSize{\pageSize}
```

### Issue: Connection Lines Crossing
```latex
% Solution: Use bend
\draw[normal conn, bend left=20] (node1) -- (node2);
\draw[encrypted conn, bend right=15] (node3) -- (node4);
```

---

## 📚 Next Steps

1. **Explore Templates**: Check `topology_templates.tex` for ready-to-use architectures
2. **Browse Examples**: Look at `example_complete_network.tex` for inspiration
3. **Read Full Docs**: See `README.md` for comprehensive documentation
4. **Customize**: Create your own node templates and topology patterns!

---

**Happy Diagramming! 🎉**

For issues or questions, check the TODO blocks in each module or consult the full README.md
