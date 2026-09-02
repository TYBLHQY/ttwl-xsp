---
title: "3.4 积分定理（位力定理）"
type: chapter
chapter: "3.4"
source: "向守平《天体物理概论》（彩色修订版，中国科学技术大学出版社 2008，ISBN 978-7-312-02170-1）（MinerU vlm+OCR 提取）"
status: active
---

### 3.4 积分定理(位力定理)

第 2 章中我们讨论了多粒子系统能量的位力定理。现在我们再就恒星的能量做一讨论。联立上一节中恒星的质量方程与静力学平衡方程，得

$$
4 \pi r ^ {2} \mathrm{d} P = - \frac {G m (r)}{r ^ {2}} \mathrm{d} m\tag{3.83}
$$

两边同乘 $r$ ，并对整个恒星积分：

$$
\int_ {0} ^ {R} 4 \pi r ^ {3} \mathrm{d} P = - \int_ {0} ^ {M} \frac {G m (r)}{r} \mathrm{d} m\tag{3.84}
$$

等号左边分部积分后，上式变成

$$
(4 \pi r ^ {3} P) \mid_ {0} ^ {r = R} - 3 \int_ {0} ^ {R} 4 \pi r ^ {2} P \mathrm{d} r = - \int_ {0} ^ {M} \frac {G m (r)}{r} \mathrm{d} m\tag{3.85}
$$

注意到 r = R 时 P = 0，故(3.85)左边第一项的结果为零，方程化为

$$
3 \int_ {0} ^ {R} \frac {4 \pi \rho r ^ {2}}{\rho} P \mathrm{d} r = 3 \int_ {0} ^ {M} \frac {P}{\rho} \mathrm{d} m = \int_ {0} ^ {M} \frac {G m (r)}{r} \mathrm{d} m\tag{3.86}
$$

再利用热力学关系

$$
P = (\gamma - 1) \varepsilon , \quad \frac {P}{\rho} = (\gamma - 1) \frac {\varepsilon}{\rho}\tag{3.87}
$$

其中， $\gamma$ 是多方指数， $\varepsilon$ 是单位体积恒星物质的内能。不难看出，(3.86)第二个等号的左边有

$$
\int_ {0} ^ {M} \frac {P}{\rho} \mathrm{d} m = \int_ {0} ^ {M} (\gamma - 1) \frac {\varepsilon}{\rho} \mathrm{d} m = (\gamma - 1) U\tag{3.88}
$$

这里 U 为恒星的总内能(提示: $\varepsilon/\rho$ 相当于单位质量的内能, 故对 m 积分得出总的内能); 相应地, (3.86) 第二个等号的右边有

$$
\int_ {0} ^ {M} \frac {G m (r)}{r} \mathrm{d} m = - V\tag{3.89}
$$

显然 $V$ 就是整个恒星的自引力势能。因此，(3.86)最后给出

$$
3 (\gamma - 1) U + V = 0\tag{3.90}
$$

这就是恒星的总内能(相当于粒子系统的总动能)和引力势能所满足的位力定理。利用这一定理,可以得到恒星的总能量是

$$
E = U + V = - (3 \gamma - 4) U = \frac {3 \gamma - 4}{3 (\gamma - 1)} V\tag{3.91}
$$

因为一个稳定的引力束缚系统必有 E<0，故上式要求 $\gamma>4/3$ ，恒星才能有稳定的结构。 $\gamma\leqslant4/3$ 意味着 $E\geqslant0$ ，此时恒星的结构不稳定（例如上一节（3.76）所示的相对论性简并气体的情况）。还有一个特例是 $\gamma=1$ ，由（3.90）看到，此时无论 U（或 E）取为何值，V 总为零。一个自引力势能总为零的系统，是不会形成任何束缚态结构的。

根据位力定理我们可以得到一个重要的结论: 恒星是一个负热容系统。这是由于, 当恒星以光度 $L = -dE/dt > 0$ 辐射能量时, 总能量减少, 即 $dE/dt < 0$ 。根

据位力定理有

$$
E = - (3 \gamma - 4) U\tag{3.92}
$$

因而

$$
\frac {\mathrm{d} E}{\mathrm{d} t} <   0 \Rightarrow \frac {\mathrm{d} U}{\mathrm{d} t} > 0 (\text {温度升高})\tag{3.93}
$$

恒星的能量由于辐射而失去一部分，但温度却上升了，即表现出负的比热。这是典型的负热容系统，是有引力介入时的热力学特征。此时由(3.90)有

$$
\frac {\mathrm{d} V}{\mathrm{d} t} <   0 (\text {收缩})\tag{3.94}
$$

可见内能的增加以及辐射的能量，都来源于收缩时减少的引力能。普通恒星一般由非相对论性气体构成，其物态方程相应于 $\gamma = 5 / 3$ ，此时(3.92)化为

$$
E = - U\tag{3.95}
$$

位力定理(3.90)也随之化为

$$
2 U + V = 0\tag{3.96}
$$

这与第2章中多粒子系统位力定理的形式完全相同(见式(2.40))。在这一情况下,我们有下面的关系

$$
L = - \frac {\mathrm{d} E}{\mathrm{d} t} = \frac {\mathrm{d} U}{\mathrm{d} t} = - \frac {1}{2} \frac {\mathrm{d} V}{\mathrm{d} t}\tag{3.97}
$$

即减少的引力能一半变成了内能，另一半变成了辐射能。

