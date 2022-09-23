<style type="text/css">
    ol ol { list-style-type: lower-alpha; }
</style>

$\gdef\unit#1{\,\text{#1}}$

# Lecture 1 Problems

1. The equation $$ d_{end-to-end} = N \frac{L}{R} $$ Where $L$ is the length of each packet, $N$ is the number of links, and $R$ is the transmission speed of each link can be generalized for $P$ packets as $$ d_{end-to-end} = (N + P - 1) \frac{L}{R} $$  Here, $\frac{L}{R}$ is the transmission delay of each link. Links transport 1 packet at a time, and there are $N - 1$ switches between each link.

2. &nbsp;
    1. The network can support 16 simultaneous connections: 4 connections between each of the 4 hosts.
    2. There can be 8 simultaneous connections between host A and C: 4 routing through B and another 4 routing through D.
    3. Yes, we can route 4 connections between A and C as well as B and D:

    ```mermaid
    flowchart LR
        A((A)) === B((B)) === C((C)) === D((D)) === A((A))
        B((B)) === C((C)) === D((D)) === A((A)) === B((B))
        C((C)) -.- D((D)) -.- A((A)) -.- B((B)) -.- C((C))
        D((D)) -.- A((A)) -.- B((B)) -.- C((C)) -.- D((D))

        subgraph Legend
            subgraph Connection 1
                direction LR
                A1((A)) -.- B1((B))
            end
            subgraph Connection 2
                direction LR
                A2((A)) === B2((B))
            end
        end
    ```

3. &nbsp;
    1. $d_{prop} = \frac{m}{s}$
    2. $d_{trans} = \frac{L}{R}$
    3. $d_{end-to-end} = d_{prop} + d_{trans}$
    4. $x_{last} = (t-d_{trans})s$, so at time $t = d_{trans}$, $x_{last} = 0$. In other words, the last bit of the packet is still just about to leave $A$.
    5. $x_{first} = ts$. At time $t = d_{trans}$, $x_{first} = d_{trans}s$. If $d_{prop} > d_{trans}$, then it follows that $x_{first} < m$ (because $s = \frac{m}{d_{prop}}$, so $x_{first} = d_{trans} \frac{m}{d_{prop}}$), meaning the first bit of the packet has yet to reach $B$.
    6. If instead $d_{prop} < d_{trans}$, then it follows that $x_{first} > m$, meaning the first bit of the packet has reached $B$.
    $\
    \gdef\s{2.5 \cdot 10^8 \unit{m/s}}\
    \gdef\L{120 \unit{bits}}\
    \gdef\R{56 \unit{kbps}}\
    $
    7. If $s = \s$, $L = \L$, $R = \R$, and $d_{prop} = d_{trans}$ then
        $$
            \begin{split}
            \frac{m}{s} &= \frac{L}{R}\\
            &\Downarrow\\
            m &= s \frac{L}{R}\\
            &= (\s) \frac{\L}{\R}\\
            &\approx 535 \unit{m}\\
            \end{split}
        $$

4. If $N = \text{number of packets}$, $L = \text{length of each packet in bits}$, and $R = \text{transmission rate in bps}$, then
    1. $$
        \begin{split}
        d_{avg\,queue} &= \frac{\sum_{i=0}^{N - 1} i \frac{L}{R}}{N}\\
        &= \frac{(N - 1)L}{2R}
        \end{split}
    $$
    2. If $N$ packets arrive to the link every $\frac{LN}{R}$ seconds, then the average queuing delay is still $\frac{(N - 1)L}{2R}$, since the next burst of packets arrives right as the previous burst is done.

5. $\gdef\m{20\,000 \unit{km}}
    \gdef\R{2 \unit{Mbps}}
    \gdef\s{2.5 \cdot 10^8 \unit{m/s}}
    \gdef\bxd{160 \unit{kb}}$ If $m = \m$, $R = \R$, and $s = \s$, then
    1. The bandwidth-delay product
        $$
        \begin{split}
        R \cdot d_{prop} &= R \frac{m}{s}\\
        &= \R \cdot \frac{\m}{\s}\\
        &= \bxd
        \end{split}
        $$
    
    2. The maximum number of bits in the link at any given must be $\bxd$ (the number of bits the link can transmit in $d_{prop}$ seconds).

    3. The **bandwidth-delay product** must be the maximum number of bits that can fit in a given link at any given time.

    4. $w = \frac{m}{\bxd} = \frac{\m}{\bxd} = 125 \unit{meters per bit}$. This would make each bit longer than a football field.

    5. $w = \frac{m}{R \frac{m}{s}} = \frac{s}{R}$

6. $\gdef\m{35\,786 \unit{km}}
    \gdef\R{10 \unit{Mbps}}
    \gdef\s{2.4 \cdot 10^8 \unit{m/s}}
    \gdef\D{0.15 \unit{s}}
    \gdef\bxd{150 \unit{Mb}}$ If $R = \R$, $s = \s$, and $m = \text{distance from geostationary satellite to surface} = \m$, then
    1. $d_{prop} = \frac{m}{s} = \frac{\m}{\s} \approx \D$

    2. The bandwidth-delay product $R \cdot d_{prop} = \R \cdot \D = \bxd$.

    3. $$
        \begin{split}
        d_{end-to-end} &= d_{trans} + d_{prop}\\
        &= \frac{x}{R} + d_{prop}\\
        x &= R(d_{end-to-end} - d_{prop})\\
        &= \R \cdot (60 \unit{s} - \D)\\
        &= 450 \unit{Mb}
        \end{split}
    $$