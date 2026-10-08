# 成果族中文目录（CONTENTS-zh）

> **722 篇手稿，372 个成果族。** 编号与上游 [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md) 一一对应，可对照阅读。
> 手稿标题保留英文并链接至上游 PDF；「Lean」表示该族附有 [Lean 形式化](https://github.com/openai/math/tree/main/lean)。

> ⚠️ 原文结果处于不同验证阶段，未经同行评审；译文以英文原文为准。基于上游 commit `adc7f12`（2026-10-06）。

## 1. 数论（Number theory，31 个族）

**001. Milne 有理性猜想与代数特化。** 证明 Milne 有理性猜想：对 $`\overline{\mathbb Q}`$ 上具有好约化的阿贝尔簇，特化 Hodge 类与补除子积在有理数上配对，且与上同调理论的选取无关。结合成果 032，对每个剩余特征 <i>p</i>，每个特化 Hodge 类同时在所有素于 <i>p</i> 的实现与晶状实现中由单个有理代数闭链表示。

&emsp;[Milne's rationality conjecture for abelian varieties](https://github.com/openai/math/blob/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/paper.pdf)

**002. 低 Selmer 余秩下的完整 BSD 公式。** 对 ℚ 上每条椭圆曲线证明完整的 Birch–Swinnerton-Dyer 首项公式，只要其完整 <i>q</i>-幂 Selmer 群对某个素数 <i>q</i> 的余秩为 0 或 1，并包括 Tate–Shafarevich 群的有限性。与成果 006 合起来，对 ℚ 上每条椭圆曲线的一个密度为一的二次扭曲集合给出完整 BSD 公式。

&emsp;[Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank](https://github.com/openai/math/blob/main/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/exact-bsd-low-selmer-corank.pdf)

&emsp;[The Selmer converse for elliptic curves at every prime](https://github.com/openai/math/blob/main/preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/main.pdf)

&emsp;[The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one](https://github.com/openai/math/blob/main/preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/paper.pdf)

**003. 准黎曼猜想。** 证明每个狄利克雷 <i>L</i> 函数（包括 $`\zeta(s)`$）在 $`\Re s\gt 7/8`$ 内无零点，解决准黎曼猜想。对 $`\mathbb Q(\sqrt{-3})`$ 上每个有限阶 Hecke <i>L</i> 函数，同一半平面也无零点。配套论文给出 $`\Re s\gt 11/12`$ 无零点半平面的另一证明。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/003.md)）

&emsp;[The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $`\Re s\gt 7/8`$](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)

&emsp;[The Quasi-Riemann Hypothesis (alternate 11/12 proof)](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf)

&emsp;[Uniform exclusion of Landau–Siegel zeros](https://github.com/openai/math/blob/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)

**004. ℚ 上的希尔伯特第十问题。** 证明不存在算法判定任意多个变量的整系数多项式是否有有理零点，从而对 ℚ 上的希尔伯特第十问题给出否定解答。

&emsp;[Hilbert’s tenth problem over the rational numbers](https://github.com/openai/math/blob/main/preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf)

&emsp;[A pointwise 2-converse for elliptic curves with rational two-torsion](https://github.com/openai/math/blob/main/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/paper.pdf)

**005. Catalan 常数的无理性。** 证明 Catalan 常数 $`G=\sum_{j\ge0}(-1)^j/(2j+1)^2`$ 是无理数。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/005.md)）

&emsp;[Catalan's constant is irrational](https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)

**006. Goldfeld 猜想：密度与平均解析秩。** 对 ℚ 上每条椭圆曲线的二次扭曲证明 Goldfeld 猜想：解析秩为 0 与 1 的密度各为 1/2，平均解析秩趋于 1/2。两个断言均按绝对值对带符号无平方因子扭曲参数排序。

&emsp;[Goldfeld's analytic density conjecture and the 2-converse for elliptic curves](https://github.com/openai/math/blob/main/preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026/paper.pdf)

&emsp;[The mean analytic rank of quadratic twists of elliptic curves](https://github.com/openai/math/blob/main/preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-September-23-2026/paper.pdf)

**007. 普通两点相关与修正 Elliott 猜想。** 证明普通两点 Chowla 猜想：沿固定非成比例仿射形式的刘维尔相关和有界 $`O(X/(\log X)^c)`$，其中 <i>c</i> &gt; 0 为绝对常数。更一般地，当其中一个因子对每个固定狄利克雷特征乘以 $`n^{it}`$（$`|t|\le X`$）一致非伪装（nonpretentious）时，对模长不超过 1 的复值乘性函数证明二元修正 Elliott 猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/007.md)）

&emsp;[Ordinary two-point correlations of multiplicative functions](https://github.com/openai/math/blob/main/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf)

**008. Deligne–Drinfeld 猜想。** 证明带 Ihara 括号的 rational Grothendieck–Teichmüller 李代数在权 3、5、7、… 的每个奇数权上由一个元素自由生成，解决 Deligne–Drinfeld 猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/008.md)）

&emsp;[The Deligne-Drinfeld conjecture](https://github.com/openai/math/blob/main/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/paper.pdf)

**009. 从 Milnor K 理论与伽罗瓦数据重构函数域。** 从 $`K^{\mathrm M}_1/\ell`$、$`K^{\mathrm M}_2/\ell`$ 及其乘积重构代数闭常数域上超越次数至少 2 的函数域。当 <i>ℓ</i> 异于特征时，这些数据恢复完全闭包与常数域；在等特征情形恢复原域及其命名基。还证明：在特征之外，由 abelian-by-central 的 pro-<i>ℓ</i> 伽罗瓦数据得到 Bogomolov–Pop 重构。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/009.md)）

&emsp;[Reconstruction of Function Fields from Mod-ℓ Milnor K-Theory](https://github.com/openai/math/blob/main/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf)

&emsp;[Reconstruction from Milnor K-theory modulo the characteristic](https://github.com/openai/math/blob/main/preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf)

&emsp;[The Bogomolov-Pop reconstruction theorem](https://github.com/openai/math/blob/main/preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf)

**010. 素数 2 处的无限制 pro-模性。** $`G_{\mathbb Q}`$ 的每个在有限多素数外不分歧的连续奇绝对不可约二维 2-adic 表示，出现在某个奇 tame 水平的完备 Hecke 代数中。还证明：满足这些有限性条件、在 2 处为 de Rham 且 Hodge–Tate 权互不相同的不可约奇表示在相差 Tate 扭转下经典模性，从而在无剩余限制下解决 dyadic Fontaine–Mazur 情形。

&emsp;[Unrestricted pro-modularity at the prime two](https://github.com/openai/math/blob/main/preprints/Unrestricted-pro-modularity-at-the-prime-two-October-4-2026/two-adic-promodularity.pdf)

&emsp;[The Dimension of the Two-Adic Hecke Algebra at Odd Level](https://github.com/openai/math/blob/main/preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf)

&emsp;[Fontaine–Mazur modularity at the prime 2](https://github.com/openai/math/blob/main/preprints/Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026/paper.pdf)

**011. $`p-1`$ 的素因子统计。** 证明 $`p-1`$ 的素因子（计重数）的归一化有序对数，当 <i>p</i> 均匀遍历不超过 <i>x</i> 的素数且 $`x\to\infty`$ 时联合收敛于 Poisson–Dirichlet 律 $`\mathrm{PD}(1)`$，解决 Ford–Konyagin–Luca 猜想。还证明：对每个 <i>ε</i> &gt; 0，有无穷多整数 <i>n</i> 拥有多于 $`n^{1-\varepsilon}`$ 个 totient 原像。

&emsp;[Weighted dilation graphs, smooth shifted primes and totient fibers](https://github.com/openai/math/blob/main/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf)

&emsp;[The Poisson-Dirichlet law for prime predecessors](https://github.com/openai/math/blob/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf)

&emsp;[Prime Predecessors with an Even Number of Prime Factors](https://github.com/openai/math/blob/main/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf)

**012. 相邻整数的独立最大素因子。** 解决 Erdős–Pomerance 联合 Dickman 猜想：<i>n</i> 与 $`n+1`$ 的最大素因子的对数大小在通常自然密度下渐近独立。特别地，满足 $`P^+(n)\lt P^+(n+1)`$ 的整数密度为 1/2。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/012.md)）

&emsp;[The joint Dickman law for consecutive integers](https://github.com/openai/math/blob/main/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf)

**013. Ostmann 逆哥德巴赫猜想。** 证明素数的任何有限修改都不能写成 $`A+B`$（$`A,B\subseteq\mathbb Z_{\ge0}`$ 各至少含两个元素），解决关于加法不可分解性的 Ostmann 逆哥德巴赫猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/013.md)）

&emsp;[The additive indecomposability of the primes](https://github.com/openai/math/blob/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026/paper.pdf)

**014. 限制几何 Langlands、整体 Arthur 增强 与 generic Ramanujan。** 在四个所述李论特征假设下，对 $`\overline{\mathbb F}_q`$ 上光滑射影连通曲线上的连通约化群证明限制几何 Langlands 等价。在特征 <i>p</i> &gt; 0 的任意代数闭域上，若 <i>p</i> 对群是极好的且 $`p\nmid |W_G|`$，同样结论成立。在整体函数域上，对分裂伴随绝对单例外群的 globally generic 尖表示在每个处证明 Ramanujan 性质（无特征或分歧深度限制）；对带 generic 无分歧分量的分裂伴随绝对单群的尖表示在每个无分歧处成立。在有限水平 Ramanujan–Arthur 分解假设下，为分裂连通半单群在完全有限水平出现的尖 excursion 参数构造整体 Arthur 增强，通过在整个 Weil 群（含惯性群）上的对角特化恢复给定参数。

&emsp;[Global Arthur Enhancements of Cuspidal Excursion Parameters](https://github.com/openai/math/blob/main/preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf)

&emsp;[Rationality of the Canonical Unramified Arthur Filtration](https://github.com/openai/math/blob/main/preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/paper.pdf)

&emsp;[Ramanujan-Arthur Decompositions of Cuspidal Functions at Full Finite Level](https://github.com/openai/math/blob/main/preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf)

&emsp;[Temperedness at ramified places for globally generic exceptional groups](https://github.com/openai/math/blob/main/preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf)

&emsp;[The Restricted Geometric Langlands Equivalence in Positive Characteristic](https://github.com/openai/math/blob/main/preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf)

&emsp;[Constructible tame Hecke eigensheaves in positive characteristic](https://github.com/openai/math/blob/main/preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/constructible-tame-hecke-eigensheaves-positive-characteristic.pdf)

&emsp;[Tame Hecke Eigensheaves with Several Marked Points](https://github.com/openai/math/blob/main/preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf)

&emsp;[Frobenius Structures on Tame Hecke Eigensheaves](https://github.com/openai/math/blob/main/preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/tame-hecke-frobenius.pdf)

**015. 素数、四次与六次次数下的环面束均匀分布。** 对全实域的完全体积加权环面束证明无质量逃逸的 Haar 均匀分布：固定素次数（至少 5）下的任意格与指定局部类型，本原四次域中任意阶的 Picard 束，本原六次域中极大阶理想类束。此处「本原」指没有真中间域；相应的阶或域判别式趋于无穷。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/015.md)）

&emsp;[Equidistribution of Prime-Degree Torus Packets with Arbitrary Local Type](https://github.com/openai/math/blob/main/preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/paper.pdf)

&emsp;[Equidistribution of primitive quartic torus packets for arbitrary orders](https://github.com/openai/math/blob/main/preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf)

&emsp;[Equidistribution of Primitive Sextic Torus Packets](https://github.com/openai/math/blob/main/preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/primitive-sextic-torus-packets.pdf)

**016. 阿贝尔簇中的 Zilber–Pink 与 Siegel 三重积。** 证明 $`\overline{\mathbb Q}`$ 上的阿贝尔 Zilber–Pink 猜想：每个不可约子簇相对于其最小包含扭转陪集只有有限多个极大非典型子簇。还对 $`\overline{\mathbb Q}`$ 上定义的 Hodge-generic 曲线证明 Siegel 三重积 $`\mathcal A_2`$ 中的完整曲线情形，无需边界或约化假设。

&emsp;[The abelian Zilber–Pink conjecture](https://github.com/openai/math/blob/main/preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/paper.pdf)

&emsp;[The E×CM component of Zilber–Pink for curves in A2](https://github.com/openai/math/blob/main/preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf)

&emsp;[Quaternionic division points on curves in the Siegel threefold](https://github.com/openai/math/blob/main/preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/paper.pdf)

&emsp;[Elliptic squares and Zilber–Pink for curves in A2](https://github.com/openai/math/blob/main/preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf)

**017. π 的无理性指数为 2。** 证明 <i>π</i> 的无理性指数恰为 2：对每个 <i>ε</i> &gt; 0 与所有足够大的分母 <i>q</i>，每个有理数 $`p/q`$ 满足 $`|\pi-p/q|\ge q^{-2-\varepsilon}`$。由此还证明 Flint–Hills 级数 $`\sum_{n\ge1}1/(n^3\sin^2 n)`$（角以弧度计）收敛。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/017.md)）

&emsp;[The irrationality exponent of pi is 2](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf)

**018. 整体域上的 Margulis–Platonov 猜想。** 对每个整体域（包括特征 2 的函数域）证明 Margulis–Platonov 猜想：对 <i>k</i> 上绝对几乎单单连通代数群 <i>G</i>，$`G(k)`$ 的每个非中心抽象正规子群是其非迷向非阿基米德局部群的有限积中某个开正规子群的原像。

&emsp;[The Margulis–Platonov conjecture over global function fields](https://github.com/openai/math/blob/main/preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/margulis-platonov-global-function-fields.pdf)

&emsp;[The Margulis–Platonov conjecture over number fields](https://github.com/openai/math/blob/main/preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/paper.pdf)

**019. 局部 <i>p</i>-adic 截面猜想与整体推论。** 证明 ℚ<sub><i>p</i></sub> 的有限扩张上亏格至少 2 的光滑真几何连通曲线上，有理点与其完整算术 étale 基本群的截面共轭类一一对应。还对亏格至少 2 的模曲线 $`X_0(N)`$ 与 $`X_1(N)`$ 证明 ℚ 上的 Grothendieck 截面猜想。

&emsp;[Étale covers with a prescribed exterior sheet](https://github.com/openai/math/blob/main/preprints/Etale-covers-with-a-prescribed-exterior-sheet-September-24-2026/main.pdf)

&emsp;[The p-adic section conjecture](https://github.com/openai/math/blob/main/preprints/The-p-adic-section-conjecture-September-24-2026/main.pdf)

**020. 无平方因子四次 数与无高次幂多项式取值。** 对没有固定素数平方因子的不可约整系数四次多项式证明无平方因子取值猜想：其正整数上的无平方因子取值具有预言的正 Euler 积密度。更一般地，在必要的局部条件下，对次数 4 到 8 的不可约整系数多项式建立 $`(d-2)`$-次幂自由密度；结合 Browning 的更高次定理，这覆盖每个 <i>d</i> ≥ 4。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/020.md)）

&emsp;[Squarefree values of quartics and power-free values of polynomials](https://github.com/openai/math/blob/main/preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf)

**021. Jacobsthal 函数的二次界。** 回答 Jacobsthal 的二次界问题：每个含 $`Ck^2`$ 个连续整数的区间必含一个与任一给定的、至多有 <i>k</i> 个不同素因子的正整数互素的整数，其中 <i>C</i> 为绝对常数。该界对素数集合与区间位置一致，并去掉了经典的对数损失。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/021.md)）

&emsp;[A quadratic bound for Jacobsthal's function](https://github.com/openai/math/blob/main/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf)

**022. 弱非齐次 Duffin–Schaeffer 猜想。** 证明：对每个实平移 <i>γ</i> 与有限值函数 $`\psi:\mathbb N\to[0,\infty)`$，若 $`\sum_q\phi(q)\psi(q)/q`$ 发散，则对几乎每个 <i>x</i>，存在无穷多 <i>q</i> 使 $`\|qx-\gamma\|\lt \psi(q)`$。此处 <i>ϕ</i> 为 Euler 函数，范数为到最近整数的距离。分子无限制；不需要 <i>γ</i> 的单调性或丢番图条件。

&emsp;[The Weak Inhomogeneous Duffin–Schaeffer Conjecture](https://github.com/openai/math/blob/main/preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/paper.pdf)

**023. 三次 Gauss 和的 Patterson 一阶矩。** 无条件证明 Patterson 一阶矩渐近的全部本原素数形式：范数不超过 <i>X</i> 的本原 Eisenstein 素数上的归一化三次 Gauss 和（包括两个共轭）具有显式正主项，阶为 $`X^{5/6}/\log X`$。每个固定非零素角的 Fourier 模都是更低阶的。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/023.md)）

&emsp;[An unconditional first moment for cubic Gauss sums](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf)

**024. totient 取值个数的渐近公式。** 给出不超过 <i>x</i> 的不同 totient 取值个数 $`V(x)`$ 的渐近等价，含由收敛算术近似确定的正有界相位因子。特别地，对每个固定 <i>c</i> &gt; 0 有 $`V(cx)/V(x)\to c`$，回答 Erdős 与 Hall 的尺度问题。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/024.md)）

&emsp;[An asymptotic formula for the number of totients](https://github.com/openai/math/blob/main/preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf)

**025. 短埃及分数。** 每个满足 $`1\le a\lt b`$ 的有理数 $`a/b`$ 都是 $`O(\log\log b)`$ 个互不相同的正单位分数之和。最坏情形的最小项数具有相同阶，解决 Erdős 关于短埃及分数的猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/025.md)）

&emsp;[Short Egyptian fractions](https://github.com/openai/math/blob/main/preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf)

**026. 大素数间隙的正下密度。** 对每个固定 <i>C</i> &gt; 0，在素数的每个足够大的初始段中，正比比例的相邻素数间隙超过 $`C\log p_n`$。该比例可依赖于 <i>C</i>。由此，$`p_n/n`$ 递增的下标具有正下密度，回答 Erdős 与 Prachar 的问题。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/026.md)）

&emsp;[Positive lower density of large prime gaps](https://github.com/openai/math/blob/main/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf)

**027. 曲线特征簇上的潜在整密度。** 解决 Litt 整密度问题的行列式为 1 的曲线情形。对每条光滑连通复代数曲线与每个秩，整数点在其 SL<sub><i>r</i></sub> 特征簇在某个数域的完整整数环上的每个分支中成为 Zariski 稠密。允许指定拟单幂边界共轭类，包括非半单类。

&emsp;[Integral points on character varieties of curves](https://github.com/openai/math/blob/main/preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf)

**028. Gauss 素数图的一致有界分支。** 证明 Gauss 壕沟猜想：不存在步长一致有界的无穷游走穿过互不相同的 Gauss 素数。更强地，对每个距离界 <i>D</i>，将距离不超过 <i>D</i> 的 Gauss 素数相连的图具有一致有界的有限分支大小（只依赖 <i>D</i>），包括坐标轴上的素数。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/028.md)）

&emsp;[Bounded-Step Walks on Gaussian Primes](https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf)

**029. 每个容许整数底的本原根。** 对每个既非 −1 又非平方数的整数 <i>a</i>，证明 Artin 本原根猜想的无穷性断言。对每个这样的底，在每个足够大的区间 $`(x,2x)`$ 中至少有 $`c_a x/(\log x)^2`$ 个素数以 <i>a</i> 为本原根，其中 $`c_a\gt 0`$。

&emsp;[Primitive roots for every admissible integer base](https://github.com/openai/math/blob/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf)

&emsp;[Simultaneous primitive roots: a conditional lower bound for prime bases](https://github.com/openai/math/blob/main/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/simultaneous-primitive-roots-conditional-lower-bound-prime-bases.pdf)

**030. 虚二次域上椭圆曲线的模性。** 证明虚二次域上椭圆曲线的模性猜想：每个虚二次域上的椭圆曲线都是模的，且在每个处局部参数匹配。

&emsp;[Modularity of elliptic curves over imaginary quadratic fields](https://github.com/openai/math/blob/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/paper.pdf)

**031. Galois 群开同态的 Uchida 猜想。** 证明 Uchida 猜想：数域的（可能无限的）可解闭 Galois 扩张的 Galois 群之间的每个连续开同态，都来自唯一一个反向的等变域嵌入。不需要对核的限制，也不需要单独的分圆相容性假设。

&emsp;[Open Homomorphisms of Global Solvably Closed Galois Groups](https://github.com/openai/math/blob/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/open-homomorphisms-solvably-closed-galois-groups.pdf)

---

## 2. 代数与复几何（Algebraic and complex geometry，36 个族）

**032. 所有射影 K3 曲面的 Hodge 与 Kuga–Satake 结果。** 对每个维数与余维数，证明每个复 CM 阿贝尔簇的有理 Hodge 猜想。通过 Milne 的定理，这也给出有限域上所有阿贝尔簇的 Tate 猜想以及每 种特征下阿贝尔簇的 Hodge 标准猜想。配套结果证明射影复 K3 曲面任意乘积的有理 Hodge 猜想，以及每个此类曲面的 Kuga–Satake 对应的代数性。

&emsp;[The rational Hodge conjecture for products of K3 surfaces](https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/hodge-conjecture-products-k3.pdf)

&emsp;[Algebraicity of Kuga–Satake Correspondences for K3 Surfaces](https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026/manuscript.pdf)

&emsp;[The rational Hodge conjecture for CM abelian varieties](https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026/paper.pdf)

&emsp;[Algebraic Kuga–Satake correspondences and Hodge conjectures on a K3 quadratic locus](https://github.com/openai/math/blob/main/preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf)

&emsp;[Weil classes and Hodge classes on abelian powers](https://github.com/openai/math/blob/main/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-September-30-2026/paper.pdf)

&emsp;[Abelian covers, Gale correspondences, and the Hodge conjecture for powers](https://github.com/openai/math/blob/main/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026/paper.pdf)

&emsp;[Algebraicity of Weil classes on split abelian eightfolds](https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/paper.pdf)

&emsp;[A Conditional Reduction for Algebraic Kuga–Satake Correspondences](https://github.com/openai/math/blob/main/preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/paper.pdf)

**033. Iitaka 次可加性、变差与对数可加性。** 对带理性简单法向交叉边界的光滑 Fujiki 类 $`\mathcal C`$ 流形证明 Campana 轨形 Iitaka 次可加性猜想。对连通纤维为一般纤维 <i>F</i> 且 $`\bar\kappa(V)\ge0`$ 的光滑复拟射影簇的射影纤维化 $`f:U\to V`$，证明 Popa 不等式 $`\bar\kappa(U)\ge\kappa(F)+\max\{\bar\kappa(V),\mathop{\mathrm{Var}}\nolimits (f)\}`$，其中变差度量整个几何一般纤维。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/033.md)）

&emsp;[Orbifold and logarithmic Iitaka subadditivity](https://github.com/openai/math/blob/main/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/paper.pdf)

&emsp;[Logarithmic Kodaira dimension and whole-fiber variation](https://github.com/openai/math/blob/main/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/paper.pdf)

&emsp;[The reverse logarithmic Kodaira inequality and additivity](https://github.com/openai/math/blob/main/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf)

&emsp;[Projective Hodge lines and ordinary Iitaka subadditivity](https://github.com/openai/math/blob/main/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/paper.pdf)

&emsp;[B-semiampleness for compact log-smooth Kähler fibrations](https://github.com/openai/math/blob/main/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/paper.pdf)

**034. 对数 Iitaka 次可加性下的紧 Kähler 空间对数丰度。** 利用对数 Iitaka 次可加性，证明每个维数下带有效有理边界的法向紧 Kähler 对数典范对的对数丰度：解析 nef 的 ℚ-Cartier 伴随是半丰沛的。还证明特征零代数闭域上的射影对数丰度，以及该背景下非负 Kodaira 维数光滑射影簇的有效 Iitaka 纤维化猜想。另一结果对这类域上连通射影半对数典范对数 Calabi–Yau 对，在固定维数与固定有限有理边界系数集下解决有限有理系数指标猜想，指标一致有界且与分支数无关。

&emsp;[Log abundance for compact Kähler spaces under logarithmic Iitaka subadditivity](https://github.com/openai/math/blob/main/preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-4-2026/main.pdf)

&emsp;[Uniform indices for semi-log-canonical log Calabi–Yau pairs](https://github.com/openai/math/blob/main/preprints/Uniform-indices-for-semi-log-canonical-log-Calabi-Yau-pairs-October-5-2026/uniform-slc-index.pdf)

&emsp;[Conditional good minimal models for compact Kähler fourfolds](https://github.com/openai/math/blob/main/preprints/Conditional-good-minimal-models-for-compact-Kahler-fourfolds-October-5-2026/paper.pdf)

&emsp;[Log abundance in characteristic zero](https://github.com/openai/math/blob/main/preprints/Log-abundance-in-characteristic-zero-September-24-2026/paper.pdf)

&emsp;[Minimal metrics and interior injectivity for nef adjoints](https://github.com/openai/math/blob/main/preprints/Minimal-metrics-and-interior-injectivity-for-nef-adjoints-September-27-2026/paper.pdf)

&emsp;[Fourfold nonvanishing by minimal metrics and moving jets](https://github.com/openai/math/blob/main/preprints/Fourfold-nonvanishing-by-minimal-metrics-and-moving-jets-September-27-2026/paper.pdf)

&emsp;[Lifting sections from the reduced support of an adjoint](https://github.com/openai/math/blob/main/preprints/Lifting-sections-from-the-reduced-support-of-an-adjoint-September-27-2026/paper.pdf)

&emsp;[Schnell fiber spaces and good canonical models](https://github.com/openai/math/blob/main/preprints/Schnell-fiber-spaces-and-good-canonical-models-September-24-2026/paper.pdf)

&emsp;[Uniform log Iitaka fibrations and bounded moduli denominators](https://github.com/openai/math/blob/main/preprints/Uniform-log-Iitaka-fibrations-and-bounded-moduli-denominators-October-4-2026/uniform-log-iitaka.pdf)

&emsp;[Uniform Pluricanonical Iitaka Fibrations](https://github.com/openai/math/blob/main/preprints/Uniform-Pluricanonical-Iitaka-Fibrations-October-3-2026/paper.pdf)

&emsp;[Relative denominators and effective systems for log Calabi-Yau fibrations](https://github.com/openai/math/blob/main/preprints/Relative-denominators-and-effective-systems-for-log-Calabi-Yau-fibrations-September-27-2026/paper.pdf)

&emsp;[Arithmetic Stein-degree bounds for log Calabi–Yau pairs](https://github.com/openai/math/blob/main/preprints/Arithmetic-Stein-degree-bounds-for-log-Calabi-Yau-pairs-September-25-2026/paper.pdf)

&emsp;[Uniform effective log Iitaka fibrations for fourfolds](https://github.com/openai/math/blob/main/preprints/Uniform-effective-log-Iitaka-fibrations-for-fourfolds-September-26-2026/paper.pdf)

&emsp;[Abundance after nonvanishing for compact Kähler fourfolds](https://github.com/openai/math/blob/main/preprints/Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026/paper.pdf)

**035. 数值维数 1 的对数典范三维簇丰度。** 对代数闭域上特征 <i>p</i> &gt; 3 的射影对数典范三维簇对，当有效边界有理且 ℚ-Cartier 伴随是数值维数 1 的 nef 除子时，证明对数丰度。伴随是半丰沛的，且不要求原簇是 terminal 或 ℚ-因子分解的。

&emsp;[Log abundance in numerical dimension one for threefolds in positive characteristic](https://github.com/openai/math/blob/main/preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/paper.pdf)

&emsp;[Abundance in numerical dimension one for terminal threefolds in positive characteristic](https://github.com/openai/math/blob/main/preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/paper.pdf)

**036. 数值半丰沛性与广义极小模型。** 对代数闭特征零域上的射影 klt 有理对与光滑紧 Kähler 有理 klt 简单法向交叉对（后者用 Bott–Chern 上同调），证明伴随 $`K_X+B+M`$（$`K_X+B`$ 伪有效、<i>M</i> nef 有理）的数值半丰沛性。另外，此类域上的射影广义对数典范有理对在伪有效伴随时有极小模型，否则有 Mori 纤维空间，均固定 nef b-数据。

&emsp;[Numerical semiampleness of nef adjoint classes on compact Kähler manifolds](https://github.com/openai/math/blob/main/preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-4-2026/numerical-generalized-abundance.pdf)

&emsp;[Numerical Semiampleness of Nef Adjoint Divisors](https://github.com/openai/math/blob/main/preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/paper.pdf)

&emsp;[Minimal models and Mori fibre spaces for generalized log canonical Q-pairs](https://github.com/openai/math/blob/main/preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/paper.pdf)

&emsp;[Minimal models in numerical dimension one](https://github.com/openai/math/blob/main/preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/paper.pdf)

**037. 普通双点奇点的体积间隙。** 证明普通双点体积间隙猜想：每个维数 <i>n</i> ≥ 2、边界为零的奇异复代数 klt 芽，其归一化体积至多为 $`2(n-1)^n`$。等号恰在解析普通双点处成立。

&emsp;[The ordinary-double-point gap in every dimension](https://github.com/openai/math/blob/main/preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/paper.pdf)

&emsp;[The normalized-volume gap in dimension four](https://github.com/openai/math/blob/main/preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/paper.pdf)

**038. Fujita 丰沛性猜想。** 在每个维数的最优界处证明 Fujita 丰沛性猜想：对维数 <i>n</i> 的光滑射影复簇 <i>X</i> 与丰沛线丛 <i>L</i>，伴随 $`K_X+mL`$ 对每个整数 $`m\ge n+1`$ 整体生成。

&emsp;[Fujita's freeness conjecture](https://github.com/openai/math/blob/main/preprints/Fujitas-freeness-conjecture-September-23-2026/Fujitas-freeness-conjecture-September-23-2026.pdf)

**039. Nagata 猜想与极大 Seshadri 常数。** 对过 <i>r</i> ≥ 10 个非常一般复点、次数为 <i>d</i> 的每个非零有效平面曲线（重数 <i>m</i><sub><i>i</i></sub> 任意），证明 Nagata 严格不等式 $`\sum_i m_i\lt d\sqrt r`$。还对每个维数 <i>n</i> ≥ 2 的光滑极化射影簇与所有足够大的 <i>r</i>，证明极大多点 Seshadri 常数 $`(L^n/r)^{1/n}`$：在 ℂ 上非常一般的点处，以及在正特征任意代数闭域上的几何一般元组处。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/039.md)）

&emsp;[Nagata's conjecture for plane curves](https://github.com/openai/math/blob/main/preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/main.pdf)

&emsp;[Maximal Seshadri constants on arbitrary polarized surfaces](https://github.com/openai/math/blob/main/preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/main.pdf)

&emsp;[Maximal Multipoint Seshadri Constants in Higher Dimensions](https://github.com/openai/math/blob/main/preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/main.pdf)

&emsp;[Maximal multipoint Seshadri constants in positive characteristic](https://github.com/openai/math/blob/main/preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/seshadri-positive-characteristic.pdf)

**040. 复曲面的 Bloch 猜想。** 证明 Bloch 猜想：对每个满足 $`p_g(S)=0`$ 的光滑连通射影复曲面 <i>S</i>，整次数零零闭链上的 Albanese 映射 $`\mathrm{CH}_0(S)^0\to\mathrm{Alb}(S)(\mathbb C)`$ 是同构。这结合了新的 $`p_g=q=0`$ 定理与 Bloch–Kas–Lieberman 经典定理。

&emsp;[Bloch’s conjecture for surfaces with p_g=0](https://github.com/openai/math/blob/main/preprints/Blochs-Conjecture-for-Surfaces-with-pg-equals-q-equals-0-September-24-2026/paper.pdf)

**041. 超 Kähler SYZ 与射影空间底。** 证明强超 Kähler SYZ 猜想：紧不可约全纯辛 Kähler 流形上每个具有非零 nef 迷向第一 Chern 类的全纯线丛是半丰沛的。还证明：每个带法向射影底的射影拉格朗日纤维化，其底是射影空间，在每个维数与形变类型下成立。

&emsp;[Projective-space bases of Lagrangian fibrations](https://github.com/openai/math/blob/main/preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/main.pdf)

&emsp;[The strong hyperkähler SYZ conjecture](https://github.com/openai/math/blob/main/preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/main.pdf)

**042. 极小紧复曲面的 Oka 分类：Kodaira 维数零与 VII 类。** 证明每个复 K3 曲面都是 Oka 的，包括非射影曲面。更一般地，Kodaira 维数为零的每个连通极小紧复曲面都是 Oka 的；VII 类的连通极小紧复曲面是 Oka 的当且仅当它是 Hopf 或 Enoki 曲面。

&emsp;[Every complex K3 surface is Oka](https://github.com/openai/math/blob/main/preprints/Every-complex-K3-surface-is-Oka-September-23-2026/paper.pdf)

**043. 固定行列式 SL<sub><i>n</i></sub> 模空间的 <i>P</i> = <i>W</i>。** 对亏格至少 2 的光滑射影复曲线上的复合秩光滑互素固定行列式无迹 Higgs 模空间及其特征簇，在整个有理上同调上证明 $`P_k=W_{2k}=W_{2k+1}`$。这包括变体上同调；结合已知的素数秩定理，在互素的每个秩建立固定行列式 <i>P</i> = <i>W</i> 猜想。

&emsp;[P=W in composite rank for fixed determinant](https://github.com/openai/math/blob/main/preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026.pdf)

**044. 等变上同调 Hikita 猜想。** 对每个有限箭图（含环与多重箭）、任意维数与框架向量及交换 flavor 环面，证明等变上同调 Hikita 对应。当每个半稳定点都稳定且规范作用自由时，Nakajima 簇的等变上同调典范地等于其 flavor 形变 Coulomb 分支的概形论共特征不动点的坐标环。

&emsp;[The equivariant cohomological Hikita conjecture for arbitrary quivers](https://github.com/openai/math/blob/main/preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/main.pdf)

**046. 二维及大基本群的 Shafarevich 反例。** 构造一个具有大基本群的光滑射影复四重簇，其万有覆盖不含正维数紧解析子簇，但既非 Stein 也非全纯凸。另一个光滑射影复曲面已经否定二维下无限制的 Shafarevich 全纯凸性。

&emsp;[A projective fourfold with large fundamental group and non-Stein universal cover](https://github.com/openai/math/blob/main/preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/large-fundamental-group-non-stein.pdf)

&emsp;[A surface counterexample to Shafarevich holomorphic convexity](https://github.com/openai/math/blob/main/preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/paper.pdf)

**047. 复数上的 Zariski 消去与仿射纤维化。** 构造整复仿射四重簇 $`X\not\cong\mathbb A^4`$ 满足 $`X\times\mathbb A^1\cong\mathbb A^5`$，否定 ℂ 上四维的仿射空间消去。还否定 Dolgachev–Weisfeiler 仿射纤维化猜想：光滑满射 $`X\to\mathbb A^1`$ 与 $`\mathbb A^5\to\mathbb A^2`$ 的每个剩余域纤维都同构于仿射三维空间，但不是 Zariski 局部平凡的。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/047.md)）

&emsp;[An explicit failure of complex affine-space cancellation](https://github.com/openai/math/blob/main/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf)

**048. Lipman–Zariski 的特征零反例。** 构造一个秩 2 切层自由的光滑奇异法向仿射复曲面，否定特征零的 Lipman–Zariski 猜想。

&emsp;[A singular normal affine surface with free tangent sheaf](https://github.com/openai/math/blob/main/preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/paper.pdf)

**049. 四变量的稳定坐标反例。** 构造一个四个复变量的多项式，它不是坐标，但添上一个变量后成为坐标，否定四变量的稳定坐标猜想。它的每根纤维都是仿射三维空间，但其嵌入均不可拉直，从而即使所有纤维都是仿射空间，也否定 Abhyankar–Sathaye 猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/049.md)）

&emsp;[A stable coordinate that is not a coordinate in four variables](https://github.com/openai/math/blob/main/preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf)

&emsp;[An explicit noncoordinate polynomial with affine three-space zero fibre](https://github.com/openai/math/blob/main/preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf)

**050. Griffiths 正性猜想的反例。** 在 $`\mathbb P^1\times\mathbb P^1`$ 上构造不具有严格 Griffiths 正曲率光滑 Hermite 度量的丰沛秩 2 丛，在二次曲面上就否定 Griffiths 正性猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/050.md)）

&emsp;[Ample rank-two bundles on the quadric surface without Griffiths-positive metrics](https://github.com/openai/math/blob/main/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf)

**051. Kobayashi 典型丰沛性猜想。** 每个没有非常数整曲线的正复维数紧连通 Kähler 流形都有丰沛典型丛，因而是射影的。这证明了光滑紧 Kähler 情形下的 Kobayashi 典型丰沛性猜想。

&emsp;[Canonical ampleness of compact hyperbolic Kähler manifolds](https://github.com/openai/math/blob/main/preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/canonical-ampleness.pdf)

**052. 切层分裂与乘积分解。** 紧 Kähler 流形切丛分裂为两个可积全纯子丛时，其万有覆盖诱导出相容的乘积分解，证明 Beauville 分裂猜想的双因子形式。在光滑有理连通射影流形上，两个因子自动可积，从而建立 Höring 猜想及相应的乘积分解。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/052.md)）

&emsp;[Universal-cover splitting for compact Kähler manifolds](https://github.com/openai/math/blob/main/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf)

&emsp;[Integrability of split tangent bundles on rationally connected manifolds](https://github.com/openai/math/blob/main/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/main.pdf)

**053. Chow 环中 Pixton 完备性的反例。** 在带标记稳定曲线模空间上构造一条重言关系：它在有理 Chow 环中为零（因而在有理上同调中也为零），但落在 Pixton 原始关系张成之外。这否定了其原始完备性猜想的 Chow 形式与有理上同调形式。

&emsp;[A high-arity counterexample to Pixton completeness in Chow](https://github.com/openai/math/blob/main/preprints/A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026/paper.pdf)

**054. 带 Hodge 理论与范畴 K3 关联的无理三次四重簇。** 对每个足够大的容许 Hassett 判别式，非常一般的光滑复三次四重簇是无理的，尽管它同时具有无扭曲的几何 K3 范畴与整 Hodge 理论 K3 关联。这否定 Kuznetsov 有理性猜想及「关联 K3」判据对有理性的充分性；判别式阈值非有效。

&emsp;[Irrational cubic fourfolds with geometric K3 categories](https://github.com/openai/math/blob/main/preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026.pdf)

**055. 三维簇上的 Gepner 对称与大体积稳定性。** 对每个光滑复五次三维簇证明 Toda 的 Gepner 猜想，构造具有指定相位移动 2/5 的数值 Bridgeland 稳定性条件。还对每个典范丛平凡的光滑射影复三维簇，在所有足够大体积处构造数值 Bridgeland 稳定性条件，中心电荷恰为普通的与平方根 Todd 的。

&emsp;[A Gepner stability condition on every smooth quintic threefold](https://github.com/openai/math/blob/main/preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/paper.pdf)

&emsp;[Prescribed large-volume charges on threefolds with trivial canonical bundle](https://github.com/openai/math/blob/main/preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/paper.pdf)

**056. 射影与 Kähler 四重簇极小模型程序的终止。** 证明全局 Weil ℚ-因子分解的紧 Kähler 四重簇上，每个已有的广义对数典范翻转序列都终止（有理边界、固定有理解析 nef b-数据、带指定丰沛符号的射影小翻转图表）。还证明特征零下带理边界的射影对数典范四重簇的任意允许极小模型程序的终止。

&emsp;[Termination of generalized log canonical flips on compact Kähler fourfolds](https://github.com/openai/math/blob/main/preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-5-2026/termination-generalized-lc-kahler-fourfolds.pdf)

&emsp;[Termination of generalized-canonical flips on compact Kähler fourfolds](https://github.com/openai/math/blob/main/preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-5-2026/termination-generalized-terminal-flips-compact-kahler-fourfolds.pdf)

&emsp;[Termination for projective log canonical fourfolds with rational boundary](https://github.com/openai/math/blob/main/preprints/Termination-for-projective-log-canonical-fourfolds-with-rational-boundary-September-24-2026/paper.pdf)

&emsp;[Finite ordinary minimal model programs on compact Kähler fourfolds](https://github.com/openai/math/blob/main/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-5-2026/paper.pdf)

&emsp;[Finite ordinary minimal model programs on compact Kähler fourfolds](https://github.com/openai/math/blob/main/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026/paper.pdf)

**057. 特殊复簇的基本群与根轨形。** 证明 Campana 交换性猜想：特殊紧 Kähler 流形具有几乎交换的基本群。利用该定理，对沿一个非空光滑连通除子取二阶根轨形的光滑射影复四重簇，在所述微分线丛特殊意义下建立同一结论。对光滑特殊复拟射影簇，证明其基本群的每个有限维复线性表示都有类至多 2 的几乎幂零像。

&emsp;[The abelianity conjecture for special compact Kähler manifolds](https://github.com/openai/math/blob/main/preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/paper.pdf)

&emsp;[Two-step monodromy of special quasi-projective varieties](https://github.com/openai/math/blob/main/preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/paper.pdf)

&emsp;[A conditional abelianity theorem for special fourfold pairs with a half-weight divisor](https://github.com/openai/math/blob/main/preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/main.pdf)

**058. 半代数万有覆盖与有界域。** 证明 Kollár–Pardon 猜想：连通法向射影复簇的半代数万有覆盖恰为乘积 $`D\times\mathbb C^m\times F`$，其中 <i>D</i> 为有界对称域，<i>F</i> 单连通、法向且射影。万有覆盖拟射影当且仅当没有有界对称因子。特别地，被 ℂⁿ 覆盖的光滑射影簇有被某阿贝尔簇有限 étale 覆盖的有限 étale 覆盖。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/058.md)）

&emsp;[Semialgebraic universal covers of normal projective varieties](https://github.com/openai/math/blob/main/preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/paper.pdf)

&emsp;[Symmetry of semialgebraic bounded domains with compact quotient](https://github.com/openai/math/blob/main/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/paper.pdf)

**059. Zariski 重数猜想的反例。** 构造环境同胚但重数不同的约化全纯超曲面芽，否定 Zariski 重数猜想。例子包括 ℂ⁴ 中具有孤立临界点、重数分别为 4 与 5 的超曲面。

&emsp;[Ambiently homeomorphic isolated hypersurfaces of multiplicities two and three](https://github.com/openai/math/blob/main/preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/paper.pdf)

&emsp;[Ambiently homeomorphic isolated hypersurface germs in ℂ⁴ with multiplicities four and five](https://github.com/openai/math/blob/main/preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/paper.pdf)

**060. 整体球壳猜想。** 每个 $`b_2\gt 0`$ 的 VII 类连通极小紧复曲面都含一个整体球壳，证明正 <i>b</i>₂ 整体球壳猜想。球壳是标准三维球面在 $`\mathbb C^2\setminus\{0\}`$ 中的全纯嵌入邻域，其补连通。

&emsp;[Global Spherical Shells on Minimal Surfaces of Class VII](https://github.com/openai/math/blob/main/preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/paper.pdf)

**062. 射影接触分类与 LeBrun–Salamon 猜想。** 证明 LeBrun–Salamon 猜想：实维数至少 8 的闭连通正四元数 Kähler 流形都与某个紧对称 Wolf 空间位似。还证明接触 Fano 齐性，并分类复维数至少 3 的光滑连通复射影接触流形：$`b_2=1`$ 者是带典范接触结构的伴随簇，$`b_2\ge2`$ 者的底流形为 $`\mathbb P(T^*Z)`$（<i>Z</i> 为光滑射影簇）。

&emsp;[Contact Fano manifolds and the LeBrun–Salamon conjecture](https://github.com/openai/math/blob/main/preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/paper.pdf)

**063. 广义 Mukai 猜想。** 证明广义 Mukai 猜想：维数 <i>n</i>、Picard 数 <i>ρ</i>、伪指标 <i>ι</i> 的正维数光滑复射影 Fano 流形满足 $`\rho(\iota-1)\le n`$，等号恰在 $`(\mathbb P^{\iota-1})^\rho`$ 处成立。伪指标指有理曲线的最小反典范次数。

&emsp;[The generalized Mukai conjecture](https://github.com/openai/math/blob/main/preprints/The-Generalized-Mukai-Conjecture-September-24-2026/article.pdf)

**064. μ-常值曲面奇点的拓扑平凡性。** 对 ℂ³ 中具有常数 Milnor 数的孤立超曲面奇点的每个全索单参数族，证明拓扑右平凡性，解决 μ-常值问题的曲面情形。缩小参数圆盘与代表元后，环境同胚可取为联合连续、固定原点截口且保持定义函数。

&emsp;[Topological triviality of mu-constant families of surface singularities](https://github.com/openai/math/blob/main/preprints/Topological-triviality-of-mu-constant-families-of-surface-singularities-September-24-2026/main.pdf)

**065. 完全交与射影丛塔的 Virasoro 约束。** 对复射影空间中的光滑完全交，在任意亏格与曲线类、任意上同调插入下证明完整的普通未既约下降 Virasoro 猜想。约束还从任何满足它的光滑射影复底传递到秩至少 2 的代数向量丛的射影化，从而传递到射影丛塔。

&emsp;[Virasoro Constraints under Projectivization](https://github.com/openai/math/blob/main/preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/virasoro-constraints-under-projectivization.pdf)

&emsp;[Virasoro Constraints for Projective Complete Intersections](https://github.com/openai/math/blob/main/preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/article.pdf)

**066. Fano 收缩的有界 klt 补。** 对带 nef 反对数典范除子的 <i>ε</i>-lc 复 Fano 型对，证明 Shokurov 有界 klt 补猜想的有限有理系数形式。对任意代数闭特征零域上的 <i>ε</i>-lc Fano 收缩，在每个底点附近给出 klt 补，指标只由维数与正有理 <i>ε</i> 界定。

&emsp;[Bounded klt complements for Fano contractions](https://github.com/openai/math/blob/main/preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/Bounded-klt-complements-for-Fano-contractions-September-25-2026.pdf)

&emsp;[Uniform Cartier sections for Fano type contractions](https://github.com/openai/math/blob/main/preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf)

**067. 六维的 Campana–Peternell 猜想。** 在复维数 6 证明 Campana–Peternell 猜想：每个带 nef 切丛的光滑连通复射影 Fano 六重簇是有理齐性的。

&emsp;[The Campana–Peternell conjecture in dimension six](https://github.com/openai/math/blob/main/preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/main.pdf)

**068. 每个维数的反典范非消失性。** 若 <i>X</i> 是光滑连通复射影簇且 $`-K_X`$ 允许一个曲率非负的光滑 Hermite 度量，则存在 <i>m</i> &gt; 0 使 $`H^0(X,-mK_X)\ne0`$。即在任意维数，光滑半正性迫使反典范丛的某个正幂有非零截口。

&emsp;[Anticanonical nonvanishing from smooth semipositivity](https://github.com/openai/math/blob/main/preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/main.pdf)

&emsp;[Invariant anticanonical indices and conversion of twisted differentials](https://github.com/openai/math/blob/main/preprints/Invariant-anticanonical-indices-and-conversion-of-twisted-differentials-September-26-2026/main.pdf)

&emsp;[Bounded anticanonical metrics on klt pairs and torus quotients](https://github.com/openai/math/blob/main/preprints/Bounded-anticanonical-metrics-on-klt-pairs-and-torus-quotients-September-26-2026/main.pdf)

&emsp;[Cohomological transfer and equivariant anticanonical sections](https://github.com/openai/math/blob/main/preprints/Cohomological-transfer-and-equivariant-anticanonical-sections-September-26-2026/main.pdf)

&emsp;[Metric descent and rank-preserving contractions](https://github.com/openai/math/blob/main/preprints/Metric-descent-and-rank-preserving-contractions-September-26-2026/main.pdf)

&emsp;[Integrable metrics and effectivity with controlled boundary](https://github.com/openai/math/blob/main/preprints/Integrable-metrics-and-effectivity-with-controlled-boundary-September-26-2026/main.pdf)

&emsp;[Exact orders and invariant anticanonical linear systems](https://github.com/openai/math/blob/main/preprints/Exact-orders-and-invariant-anticanonical-linear-systems-September-26-2026/main.pdf)

**069. 无理水平的整体量子几何 Langlands。** 对每个连通单复代数群、每条光滑射影连通复曲线、每个移位水平 $`c\in\mathbb C\setminus\mathbb Q`$，证明无分歧 de Rham 量子几何 Langlands 等价：识别群与其 Langlands 对偶的扭曲 <i>D</i>-模的完整导出范畴，保留所有整体形式与连通分支。

&emsp;[Global quantum geometric Langlands at irrational level](https://github.com/openai/math/blob/main/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf)

---

## 3. 实与复分析（Real and complex analysis，16 个族）

**071. Koebe 圆域猜想。** 解决 Koebe 圆域猜想的存在性部分：黎曼球面上的每个域共形等价于一个补分支均为圆盘或点的域。还证明带共形可去边界的圆域是刚性的——到另一圆域的每个共形等价都是 Möbius 变换，建立 He–Schramm 猜想的这一方向。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/071.md)）

&emsp;[Removable Boundaries and Rigidity of Circle Domains](https://github.com/openai/math/blob/main/preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/paper.pdf)

&emsp;[Koebe's Circle-Domain Conjecture](https://github.com/openai/math/blob/main/preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/paper.pdf)

**072. Brennan 猜想与积分均值谱。** 证明 Brennan 猜想：对从单连通平面域到圆盘的每个共形双射 <i>φ</i>，$`|\phi'|^s`$ 在 $`4/3\lt s\lt 4`$ 上面积可积。锐利 universal 积分均值恒等式为：对 <i>t</i> ≤ −2，$`B_{\mathcal S}(t)=|t|-1`$。对有界单叶函数的严格界 $`B_b(-1)\lt 1/4`$ 否定 Kraetzer 预测在该参数处的值。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/072.md)）

&emsp;[Brennan's conjecture and sharp inverse-square integral means](https://github.com/openai/math/blob/main/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf)

&emsp;[A strict inverse-first-power bound for univalent functions](https://github.com/openai/math/blob/main/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf)

**073. Falconer 距离猜想。** 在维数 2 与 3 解决 Falconer 距离猜想：若 $`E\subset\mathbb R^d`$ 为豪斯多夫维数大于 <i>d</i>/2 的紧集，则其确定的欧氏距离集具有正勒贝格测度。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/073.md)）

&emsp;[The Falconer distance conjecture in all dimensions](https://github.com/openai/math/blob/main/preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf)

**074. 三维与四维的挂谷问题。** 解决三维挂谷极大算子猜想与四维豪斯多夫维数猜想。三维：半径 <i>δ</i> 细管的极大算子以范数 $`O_\varepsilon(\delta^{-\varepsilon})`$ 映 $`L^3(\mathbb R^3)`$ 到 $`L^3(S^2)`$（每个 <i>ε</i> &gt; 0）。四维：每个在所有方向含单位线段的集合豪斯多夫维数为 4。

&emsp;[The Kakeya maximal conjecture in three dimensions](https://github.com/openai/math/blob/main/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/paper.pdf)

&emsp;[Every four-dimensional Kakeya set has full Hausdorff dimension](https://github.com/openai/math/blob/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/paper.pdf)

**075. $`L\log L`$ 傅里叶收敛猜想。** 证明 $`L\log L(\mathbb T)`$ 中每个复值函数的普通对称傅里叶部分和沿完整序列几乎处处收敛。解决 $`L\log L`$ 尺度上的经典充分性猜想。

&emsp;[Almost-everywhere Fourier convergence in L log L](https://github.com/openai/math/blob/main/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf)

**076. 实超平坦 Littlewood 多项式与无界二进制优值因子。** 构造 <i>N</i> 个连续系数取自 $`\{-1,1\}`$ 的多项式，其模在整单位圆上一致为 $`(1+o(1))\sqrt N`$，对每个足够大的长度 <i>N</i>。即实 Littlewood 多项式可以超平坦，包括在实端点处。其二进制优值因子趋于无穷，否定 Turyn 的有界优值因子猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/076.md)）

&emsp;[Ultraflat real Littlewood polynomials](https://github.com/openai/math/blob/main/preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/ultraflat-real-littlewood-polynomials.pdf)

&emsp;[Nearly minimal maxima and positive minima of Littlewood polynomials](https://github.com/openai/math/blob/main/preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/littlewood-lower-envelope.pdf)

&emsp;[Asymptotically minimal maxima of real Littlewood polynomials](https://github.com/openai/math/blob/main/preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/paper.pdf)

**077. 正曲率曲面的傅里叶限制。** 证明三维正曲率曲面的对角傅里叶延拓猜想。对每个紧光滑正曲率曲面 $`\Sigma\subset\mathbb R^3`$（含带边曲面），对每个 <i>p</i> &gt; 3，延拓算子从 $`L^p(\Sigma)`$ 到 $`L^p(\mathbb R^3)`$ 有界。

&emsp;[Elliptic capacity propagation and Fourier restriction to the sphere](https://github.com/openai/math/blob/main/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf)

&emsp;[Diagonal Fourier extension for positively curved surfaces in three dimensions](https://github.com/openai/math/blob/main/preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026.pdf)

**078. 三维 Bochner–Riesz 猜想。** 在严格范围内解决三维 Bochner–Riesz 猜想：只要 $`\delta\gt \max\{3|1/p-1/2|-1/2,0\}`$，阶 <i>δ</i> 的 Bochner–Riesz 乘子在所有 $`1\le p\le\infty`$ 的 $`L^p(\mathbb R^3)`$ 上有界。

&emsp;[Bochner–Riesz multipliers in three dimensions](https://github.com/openai/math/blob/main/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf)

**079. 三维局部光滑化。** 解决 Sogge 的三维欧氏波动方程局部光滑化猜想：估计在整个严格范围 $`2\lt p\lt \infty`$ 成立，Sobolev 正则性高于 $`\max\{0,1-3/p\}`$。特别地，临界 <i>L</i>³ 估计带任意正 Sobolev 损失成立。

&emsp;[Critical local smoothing for the three-dimensional wave equation](https://github.com/openai/math/blob/main/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf)

**080. 薛定谔收敛的精确 Sobolev 端点。** 对每个 $`f\in H^{n/(2(n+1))}(\mathbb R^n)`$ 与每个维数 <i>n</i> ≥ 2，证明 $`e^{it\Delta}f\to f`$ 当 $`t\downarrow0`$ 时几乎处处收敛。达到 Carleson 薛定谔收敛问题的锐利 Sobolev 等式情形，包括平面端点 <i>H</i>^(1/3)。

&emsp;[Endpoint convergence for the planar Schrodinger equation](https://github.com/openai/math/blob/main/preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/paper.pdf)

&emsp;[Endpoint pointwise convergence for the Schrodinger equation in higher dimensions](https://github.com/openai/math/blob/main/preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/paper.pdf)

**081. 高余维 Riesz 变换与可求长性。** 解决余下的高余维 Riesz 变换可求长性问题：对 <i>d</i> ≥ 4 与 $`2\le n\le d-2`$，ℝ<sup>d</sup> 上的 <i>n</i>-Ahlfors–David 正则 Radon 测度，只要其 <i>n</i> 维 Riesz 变换在所有正向硬截断上一致 <i>L</i>² 有界，就是一致 <i>n</i>-可求长的。可求长性界只依赖维数、正则性与算子界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/081.md)）

&emsp;[Riesz transforms and uniform rectifiability in higher codimension](https://github.com/openai/math/blob/main/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf)

**082. 三角希尔伯特变换的环变差与二进绝对界。** 对每个 <i>r</i> &gt; 2，证明从复 $`L^3(\mathbb R^2)\times L^3(\mathbb R^2)`$ 到 $`L^{3/2}(\mathbb R^2)`$ 的极大与环 <i>r</i>-变差界。极大估计控制两个硬截断端点，给出几乎处处收敛与范数收敛。与第三个输入配对后，在对称点 $`L^3\times L^3\times L^3`$ 解决三角希尔伯特变换估计。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/082.md)）

&emsp;[Annular variation of the triangular Hilbert transform at the symmetric point](https://github.com/openai/math/blob/main/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/annular-variation.pdf)

&emsp;[An L³ bound for the dyadic triangular Hilbert form](https://github.com/openai/math/blob/main/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/dyadic-triangular-hilbert.pdf)

&emsp;[The maximal triangular Hilbert transform at the symmetric point](https://github.com/openai/math/blob/main/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf)

**083. 沿 Lipschitz 方向的希尔伯特变换。** 对沿任意 Lipschitz 单位向量场的平面希尔伯特变换，在积分长度不超过其倒数 Lipschitz 常数绝对倍数的范围内，证明一致强 <i>L</i>² 界。该估计对内截断一致，并给出 <i>L</i>² 有界的主值算子，在这个短尺度上建立 Stein 弱型猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/083.md)）

&emsp;[A uniform Hilbert transform estimate for Lipschitz directions](https://github.com/openai/math/blob/main/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf)

**084. Erdős 相似性猜想的几何情形。** 对每个固定 $`q\in(0,1)`$，构造测度任意接近 1 的 [0,1] 紧子集，不含 $`\{q^n:n\ge1\}`$ 的平移与非平凡伸缩拷贝（伸缩可取两种符号）。对每个比率解决 Erdős 相似性猜想的等比数列情形。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/084.md)）

&emsp;[The geometric case of the Erdős similarity conjecture](https://github.com/openai/math/blob/main/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/geometric-erdos-similarity.pdf)

&emsp;[The dyadic case of the Erdős similarity conjecture](https://github.com/openai/math/blob/main/preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/paper.pdf)

**085. 中心圆盘平均的端点 Sobolev 正则性。** 解决 Hajłasz–Onninen 极大函数正则性问题的平面中心圆盘情形。对每个实 $`f\in W^{1,1}(\mathbb R^2)`$，中心圆盘极大函数满足 $`\|\nabla Mf\|_1\le C\|\nabla f\|_1`$（绝对常数），局部属于 $`W^{1,1}`$ 且具有整体可积弱梯度。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/085.md)）

&emsp;[An Endpoint Gradient Bound for the Centered Disk Maximal Operator](https://github.com/openai/math/blob/main/preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/article.pdf)

**086. 三线性希尔伯特变换的 <i>L</i>³ 界。** 证明带移位 $`x-t`$、$`x-2t`$、$`x-3t`$ 的主值三线性希尔伯特变换从 $`L^3(\mathbb R)^3`$ 到 $`L^1(\mathbb R)`$ 有界。解决标准猜想中斜率 1、2、3 的 <i>L</i>³ 指数情形。

&emsp;[An <i>L</i><sup>3</sup> bound for the trilinear Hilbert transform](https://github.com/openai/math/blob/main/preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/paper.pdf)

---

## 4. 凸几何与度量几何（Convex and metric geometry，15 个族）

**087. Mahler 猜想、函数不等式与极坐标乘积辛宽度。** 在每个维数解决对称与非对称几何 Mahler 猜想：体积积的最小化子分别是 Hanner 多面体与单纯形，所有等号情形均已分类。相应的锐利函数 Mahler 不等式同样成立。对 <i>n</i> ≥ 2，维数 2n 的每个对称极坐标乘积 $`K\times K^\circ`$ 的 Gromov 宽度为 4。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/087.md)）

&emsp;[The symmetric Mahler conjecture and its equality cases](https://github.com/openai/math/blob/main/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf)

&emsp;[The Mahler Conjecture for General Convex Bodies](https://github.com/openai/math/blob/main/preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/paper.pdf)

&emsp;[Symplectic Balls in Symmetric Polar Products](https://github.com/openai/math/blob/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/paper.pdf)

**088. 锐利投影体不等式与单纯形最大化的反例。** 在其余维数 <i>n</i> ≥ 4 证明 Petty 投影体积猜想：椭球在固定体积下唯一最小化投影体体积。还建立完整的 Lutwak–Petty 投影不等式。与之相对，单纯形的乘积在归一化投影体体积上以指数因子超过 Brannen 提出的单纯形最大值（每个足够大的维数）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/088.md)）

&emsp;[Petty’s projection-volume conjecture in dimensions at least four](https://github.com/openai/math/blob/main/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf)

&emsp;[A product counterexample to the simplex maximum for projection-body volume](https://github.com/openai/math/blob/main/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf)

**089. 平面图与有界树宽图的有界失真 <i>L</i>₁ 嵌入。** 解决 Gupta–Newman–Rabinovich–Sinclair 猜想的平面与有界树宽情形。任意正边长的有限连通图最短路度量嵌入实 <i>L</i>₁：平面图具有普适失真，有界树宽图失真只依赖树宽。相应多商品流–割间隙一致有界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/089.md)）

&emsp;[Planar Graph Metrics Embed into L1 with Constant Distortion](https://github.com/openai/math/blob/main/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf)

&emsp;[L1 Embeddings of Graphs of Bounded Treewidth](https://github.com/openai/math/blob/main/preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf)

**090. 三角格最优性、长程 Riesz 与库仑能量、球面对数能量。** 证明在中心圆盘密度 1 的局部有限平面构形中，三角格最小化每个非负完全单调势（距离平方的函数）的每粒子能量下极限。它还最小化 $`0\lt s\lt 2`$ 的单位背景重整化 Riesz 能量与库仑能量，解决 Sandier–Serfaty 猜想与 Brauchart–Hardin–Saff 关于最优球面对数能量线性项的二维猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/090.md)）

&emsp;[An atomic certificate for triangular-lattice universal optimality](https://github.com/openai/math/blob/main/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf)

&emsp;[Universal optimality of the triangular lattice](https://github.com/openai/math/blob/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/paper.pdf)

&emsp;[A sharp Fourier certificate for planar circle packing](https://github.com/openai/math/blob/main/preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/paper.pdf)

&emsp;[Triangular minimality for planar Coulomb renormalized energy](https://github.com/openai/math/blob/main/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf)

**091. 对数与 <i>L</i><sub>p</sub> Brunn–Minkowski 不等式与 B-猜想。** 在每个维数对中心对称凸体证明对数 Brunn–Minkowski 不等式，并对所有偶对数凹 Radon 测度证明标量伸缩 B-猜想。对勒贝格体积，还在整个 $`0\lt p\lt 1`$ 证明满维中心对称凸体的加性 <i>L</i><sub>p</sub> Brunn–Minkowski 不等式。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/091.md)）

&emsp;[The logarithmic Brunn–Minkowski conjecture](https://github.com/openai/math/blob/main/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf)

**092. 凸体覆盖密度的最优阶。** 确定最坏情形覆盖密度的最优阶为 $`\Theta(n\log n)`$，对格覆盖与无限制平移覆盖同时成立。ℝⁿ（<i>n</i> ≥ 2）中每个凸体都有密度至多 $`Cn\log n`$ 的格覆盖；每个足够大维数中的中心对称例子即使无格限制也至少需要 $`cn\log n`$（绝对常数 $`c,C\gt 0`$）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/092.md)）

&emsp;[A single-lattice covering bound of order n log n](https://github.com/openai/math/blob/main/preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/paper.pdf)

&emsp;[Translative covering densities of order n log n](https://github.com/openai/math/blob/main/preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/paper.pdf)

**093. 次高斯对数凹测度的维数无关对数 Sobolev 不等式。** 对线性边际一致次高斯的中心化对数凹密度证明维数无关的对数 Sobolev 不等式，常数由线性次高斯参数平方的普适倍数界定。

&emsp;[A dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures](https://github.com/openai/math/blob/main/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf)

**094. <i>L</i><sub>p</sub> 中的次多项式维数约化。** 对每个固定 $`1\lt p\lt \infty`$ 与失真 <i>D</i> &gt; 1，实 <i>L</i><sub>p</sub> 的每个 <i>n</i> 点子集以失真至多 <i>D</i>、维数 $`d=n^{o(1)}`$ 嵌入 $`\ell_p^d`$，回答 Naor 对 <i>p</i> ≠ 2 的次线性维数问题。与之相对，精确嵌入在 <i>p</i> ≠ 2 时需要最坏情形维数 $`\Theta(n^2)`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/094.md)）

&emsp;[Subpolynomial dimension reduction in Lp](https://github.com/openai/math/blob/main/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/paper.pdf)

**095. 无半定提升的双曲性锥。** 否定投影 Lax 猜想：某些双曲性锥不是谱面（spectrahedral）阴影。这些例子不容许任何精确的有限仿射半定提升，与辅助变量个数或所用实系数无关。这也否定「每个双曲性锥都是谱面的」广义 Lax 猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/095.md)）

&emsp;[Hyperbolicity Cones Without Semidefinite Lifts](https://github.com/openai/math/blob/main/preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/nonliftable-hyperbolicity.pdf)

&emsp;[A nonspectrahedral hyperbolicity cone](https://github.com/openai/math/blob/main/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/nonspectrahedral-hyperbolicity-cone.pdf)

&emsp;[An Exact Semidefinite Lift of a Nonspectrahedral Hyperbolicity Cone](https://github.com/openai/math/blob/main/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone.pdf)

**096. 每个维数的高斯螺旋桨猜想。** 证明任何有限可测分区的平方高斯一阶矩之和至多为 $`9/(8\pi)`$。在维数至少 2，三个角为 $`2\pi/3`$、正交延拓的平面扇形达到该界。结合独立的 Unique Games 定理，证明：在固定 <i>k</i> ≥ 3 的有理中心化半正定输入上，改进恒等目标核聚类的损失因子 $`(8\pi/9)(1-1/k)`$ 是 NP 难的。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/096.md)）

&emsp;[The Gaussian propeller bound in every dimension](https://github.com/openai/math/blob/main/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/main.pdf)

**097. 欧氏 Steinitz–Bergström 界。** 证明 ℝ<sup>d</sup> 欧氏单位球中的任何有限序列都可赋符号，使每个部分和保持在 $`C\sqrt d`$ 内，与长度无关。由此每个零和族都可重排，使不带符号的部分和满足同一界。匹配的下界给出最优阶 $`S_2(d)=\Theta(\sqrt d)`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/097.md)）

&emsp;[The Euclidean Steinitz–Bergström theorem](https://github.com/openai/math/blob/main/preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026.pdf)

**098. 双 Lipschitz 维数约化的紧反例。** 每个无限维实巴拿赫空间都含一个紧的加倍集，它不容许到任何有限维赋范空间的双 Lipschitz 嵌入。加倍常数是普适的。这否定回答 Lang–Plaut 问题，即使对希尔伯特空间的紧子集也成立。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/098.md)）

&emsp;[A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding](https://github.com/openai/math/blob/main/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf)

**099. 编辑距离失真的锐利指数尺度。** 确定长度至多 <i>d</i> 的词上的编辑距离嵌入实 <i>ℓ</i>₁ 的最小失真：$`\exp(\Theta(\sqrt{\log d\,\log\log d}))`$。插入、删除与替换的单位代价均为 1。常数对所有至少两个符号的有限字母表一致，即使字母表随 <i>d</i> 增长；二元词已迫使下界成立。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/099.md)）

&emsp;[Edit Distance in l1: Matching Bounds up to Constants in the Exponent](https://github.com/openai/math/blob/main/preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/paper.pdf)

&emsp;[Finite-Circle Obstructions, Binary Codes, and Histogram Embeddings for Edit Distance](https://github.com/openai/math/blob/main/preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf)

&emsp;[Tree Constructions for the l1 Distortion of Binary Edit Distance](https://github.com/openai/math/blob/main/preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/paper.pdf)

**100. 低于半面积界的圆柱覆盖。** 用总表面积小于正四面体最小正交投影面积一半的有限多个（带紧三角形垂直底的）圆柱覆盖整个闭正四面体。这否定 Bang 的半面积圆柱覆盖界以及更强的逐方向归一化猜想（三维）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/100.md)）

&emsp;[Finite angular cylinder covers below the half-area bound](https://github.com/openai/math/blob/main/preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026/main.pdf)

&emsp;[Finite cylinder approximation of ruled sets](https://github.com/openai/math/blob/main/preprints/Finite-cylinder-approximation-of-ruled-sets-September-27-2026/main.pdf)

&emsp;[Slope-field perturbations of the two-cylinder covering](https://github.com/openai/math/blob/main/preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026/main.pdf)

&emsp;[Finite triangular approximation of radial sweeps](https://github.com/openai/math/blob/main/preprints/Finite-triangular-approximation-of-radial-sweeps-September-27-2026/main.pdf)

**101. 各向同性常数的锐利单纯形猜想。** 证明单纯形在每个维数的凸体中唯一最大化各向同性常数，解决强各向同性常数猜想。还建立对数凹概率密度的锐利熵下界，等号恰在单侧指数律乘积的可逆仿射像处成立。

&emsp;[A sharp entropy bound and the simplex inequality for isotropic constants](https://github.com/openai/math/blob/main/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf)

---

## 5. 理论计算机科学（Theoretical computer science，40 个族）

**102. 唯一游戏猜想与最优近似阈值。** 证明 Khot 的唯一游戏猜想。独立的直接归约还在无权图上建立：Max-Cut 超过 Goemans–Williamson 比值的近似是 NP 难的，顶点覆盖低于因子 2 的近似是 NP 难的，Min-UnCut 与有向反馈点集的任意固定常数因子近似是 NP 难的。这些直接证明使用已有的 PCP 与 Label Cover 难度结果。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/102.md)）

&emsp;[The Unique Games Theorem](https://github.com/openai/math/blob/main/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf)

&emsp;[A Direct Proof of Optimal Max-Cut Hardness](https://github.com/openai/math/blob/main/preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper.pdf)

&emsp;[The Factor-Two Hardness Threshold for Vertex Cover](https://github.com/openai/math/blob/main/preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/paper.pdf)

&emsp;[Constant-factor hardness of Min-UnCut](https://github.com/openai/math/blob/main/preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/paper.pdf)

&emsp;[Constant-factor hardness of directed feedback vertex set](https://github.com/openai/math/blob/main/preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf)

**103. 对数空间的确切去随机化：L = RL = BPL。** 证明 $`\mathsf L=\mathsf{RL}=\mathsf{BPL}`$，解决有界错误对数空间计算的去随机化。一个有效编译器把每个以单侧或双侧错误判定语言的随机化多项式时间对数空间机，转换为带显式多项式运行时间界的确定性对数空间判定机。

&emsp;[Exact derandomization of logarithmic space: L = RL = BPL](https://github.com/openai/math/blob/main/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf)

**104. 平均收益、随机与奇偶博弈的拟多项式算法。** 对完整二进制输入长度 <i>L</i>，给出确定性算法，用 $`2^{O((\log(L+2))^2)}`$ 次位运算处理普通平均收益博弈及两个独立扩展：在普通博弈中计算精确值与最优位置策略；在回合制随机博弈中计算非负期望下确界值集；以及非负下确界平均收益与奇偶条件的联合胜出集。带符号奖励、有理概率与奇偶优先级均无限制，按二进制编码。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/104.md)）

&emsp;[Turn-Based Stochastic Mean-Payoff Games in Deterministic Quasipolynomial Time](https://github.com/openai/math/blob/main/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf)

&emsp;[Mean-payoff parity games in quasipolynomial time](https://github.com/openai/math/blob/main/preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf)

&emsp;[Deterministic quasipolynomial-time mean-payoff games](https://github.com/openai/math/blob/main/preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf)

&emsp;[Randomized quasipolynomial-time mean-payoff games](https://github.com/openai/math/blob/main/preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf)

**105. 2 对 1 博弈的完美完备性。** 以完美完备性证明 Khot 的 2 对 1 博弈猜想：对每个固定有理 $`\delta\in(0,1)`$，在显式无权实例上区分可满足博弈与最优值至多 <i>δ</i> 的博弈是 NP 难的。字母表只依赖 <i>δ</i>，且每个右侧标记在每个约束映射下恰有两个原像。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/105.md)）

&emsp;[Perfect completeness for 2-to-1 games](https://github.com/openai/math/blob/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/paper.pdf)

**106. 三可着色图染色的难度。** 用任何固定数目 <i>c</i> ≥ 3 的颜色给三可着色图染色是 NP 难的。更强地，对每个固定 $`0\lt \delta\lt 1/3`$，一个从 3SAT 出发的确定性多项式时间归约产生简单无权图：可满足情形三可着色，不可满足情形没有大小为 $`\delta n`$ 的独立集（<i>n</i> 为顶点数）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/106.md)）

&emsp;[Hardness of finding large independent sets in three-colorable graphs](https://github.com/openai/math/blob/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf)

**107. 指数至多 9/4 的矩阵乘法。** 在 ℂ 上证明 $`\omega\le9/4`$，给出方阵乘法的 $`O_\varepsilon(n^{9/4+\varepsilon})`$ 次算术运算。在特征零下，某个内维数 <i>n</i>^<i>a</i>（<i>a</i> &gt; 0.465）容许 $`n^{2+o(1)}`$ 的矩形乘法。进一步的方阵界给出：在除去有限多个正特征外 <i>ω</i> &lt; 2.258，在每个固定域上 <i>ω</i> &lt; 2.371054886006746。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/107.md)）

&emsp;[An Upper Bound of 9/4 for the Matrix Multiplication Exponent](https://github.com/openai/math/blob/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf)

&emsp;[Staggered extraction for exact matrix multiplication over every field](https://github.com/openai/math/blob/main/preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf)

&emsp;[Complex Matrix Multiplication Below 2.258 and Rectangular Bounds](https://github.com/openai/math/blob/main/preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf)

**108. 立方型积和式–行列式下界。** 证明 ℂ 上 $`n\times n`$ 积和式的 border 行列式复杂度下界 $`\Omega(n^3)`$。即使对仿射线性矩阵行列式的逐系数极限，矩阵规模也至少为 $`cn^3`$（绝对 <i>c</i> &gt; 0，所有足够大的 <i>n</i>）；因此对精确表示同样成立。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/108.md)）

&emsp;[A cubic lower bound for border determinantal complexity of the permanent](https://github.com/openai/math/blob/main/preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf)

**109. 低于 $`n\log n`$ 的整数乘法。** 在单台固定有限字母表、有限多条一维纸带的图灵机上，对每个输入长度以确定性最坏情形时间 $`O(n(\log n)^{1-\kappa})`$（$`\kappa=2^{-182}`$）精确相乘两个 <i>n</i> 位整数。这否定 Schönhage–Strassen 的 $`n\log n`$ 最优性猜想（普通多纸带位模型）。

&emsp;[Integer multiplication below n log n](https://github.com/openai/math/blob/main/preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf)

**110. 任意度量上最优阶的随机化 <i>k</i>-服务。** 在任意度量空间上建立 <i>k</i>-服务的随机化竞争比 $`O(\log^2(k+1))`$，匹配最坏情形下界的阶。一个策略可服务每个有限的无感知请求序列，包括无限无界度量。在有限有理度量上，统一实现的预处理与每请求位代价在输入长度与 $`\log(t+1)`$（第 <i>t</i> 个请求）上多项式，外加有限实例相关的附加移动常数。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/110.md)）

&emsp;[Squared-logarithmic randomized k-server on arbitrary metrics](https://github.com/openai/math/blob/main/preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026.pdf)

&emsp;[Uniform computation of the squared-logarithmic k-server bound](https://github.com/openai/math/blob/main/preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026.pdf)

**111. 对抗全能对手的单样本拟阵先知不等式。** 对每个预先已知的有限拟阵，给出分布无关的在线规则：每个元素使用一个独立样本，赚取离线最优期望值的普适常数比例。取值独立非负，期望最优值有限。即使到达序对手看到全部样本、取值与规则的整个随机种子，保证依然成立；不断言多项式时间实现。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/111.md)）

&emsp;[One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary](https://github.com/openai/math/blob/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf)

**112. 超越平方根指数的三层电路下界。** 构造确定性多项式时间中的一个语言，其 <i>n</i> 位成员函数在无界扇入 OR–AND–OR 电路中需要 $`2^{\omega(\sqrt n)}`$ 个门（每个足够大的输入长度）。这越过显式三层布尔电路下界的平方根指数阈值。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/112.md)）

&emsp;[Beyond the Square-Root Exponent for Depth-Three Boolean Circuits](https://github.com/openai/math/blob/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/main.pdf)

**113. 完美匹配的近似计数与熵。** 对任意有限简单图中完美匹配的计数给出完全多项式随机化近似方案，并精确检测零计数。还证明 Anari–Oveis Gharan–Vinzant 完美匹配熵猜想：在无环带标记多重图的每个可行边边际向量（含边界点）处，匹配律的最大熵有界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/113.md)）

&emsp;[A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs](https://github.com/openai/math/blob/main/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf)

&emsp;[Entropy and Face Dimension of the Perfect-Matching Polytope](https://github.com/openai/math/blob/main/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf)

**114. 公共整多项拟阵基的近似计数。** 对总秩相等、由精确秩值神谕提供的两个整多项拟阵，给出其公共整基计数的完全多项式随机化近似方案。容量按二进制编码，每个整向量计一次，神谕调用与神谕外的位运算在每次执行上都多项式。对由独立性神谕给出的拟阵，结果还覆盖指定基数、无限制或最大基数的公共独立集，即使秩不同。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/114.md)）

&emsp;[An FPRAS for Common Integer Polymatroid Bases with Binary Capacities](https://github.com/openai/math/blob/main/preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf)

&emsp;[Approximate counting of common bases of two matroids](https://github.com/openai/math/blob/main/preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf)

**115. 任意边际列联表的采样与计数。** 对给定行和与列和的非负整矩阵，给出期望多项式位时间的精确均匀采样与最坏情形多项式位时间的近均匀采样。维数与二进制编码的边际均无限制。还对任意单元界（含结构零）的此类表计数给出完全多项式随机化近似方案，每次执行代价多项式。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/115.md)）

&emsp;[Exact Uniform Sampling of Contingency Tables with Arbitrary Margins](https://github.com/openai/math/blob/main/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf)

&emsp;[An FPRAS for Cell-Bounded Contingency Tables](https://github.com/openai/math/blob/main/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf)

**116. 跨特征一致的黑箱非交换恒等式测试。** 对每个特征，在确定性多项式位时间内构造多项式维数的矩阵元组，检测该特征任意域上每个有界规模非零无除式非交换公式。ℚ 上的有理公式只要具有有定义的有理矩阵赋值，就也有多项式规模的击中列表。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/116.md)）

&emsp;[Uniform Matrix Hitting Points in Every Positive Characteristic](https://github.com/openai/math/blob/main/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf)

&emsp;[One Rational Matrix Hitting Point for Noncommutative Formulas](https://github.com/openai/math/blob/main/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026.pdf)

&emsp;[Polynomial Hitting Lists for Noncommutative Rational Formulas](https://github.com/openai/math/blob/main/preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf)

**117. 一致最稀割：难度与半定间隙。** 证明一致最稀割在任何固定常数因子内的近似是 NP 难的，即使容量为非负有理数、需求为单位。Goemans–Linial 半定松弛的整性间隙至少为 $`\sqrt{\log n}/(\log\log n)^3`$ 阶，逼近平方根对数上界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/117.md)）

&emsp;[Constant-factor hardness of uniform sparsest cut](https://github.com/openai/math/blob/main/preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf)

&emsp;[Near-square-root logarithmic integrality gaps for uniform sparsest cut](https://github.com/openai/math/blob/main/preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf)

**118. 装箱与无界构型 LP 间隙。** 否定 Scheithauer–Terno 修正整数进位猜想：整数装箱最优值可以比其构型线性规划值大任意大的加性常数。在任何固定加性常数内近似最优值也是 NP 难的，即使每个物品超过 1/6 且每箱至多装 5 件。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/118.md)）

&emsp;[Additive hardness and unbounded configuration gaps in bin packing](https://github.com/openai/math/blob/main/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf)

**119. Courtade–Kumar 与 Hellinger 猜想。** 证明 Courtade–Kumar 猜想：在独立均匀比特的布尔函数中，经过独立比特翻转噪声后，单个坐标保留最多互信息。更强的定理处理固定初始信息的随机化二元摘要。对每个布尔输出偏差与噪声相关，Hellinger 猜想同样得证。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/119.md)）

&emsp;[Sharp binary-information contraction on the discrete cube](https://github.com/openai/math/blob/main/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf)

&emsp;[Hellinger contraction with arbitrary Boolean output bias](https://github.com/openai/math/blob/main/preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/main.pdf)

**120. 一般图中近线性时间的精确匹配与指定度因子。** 给出随机化算法：在任何简单无向图中以 $`(n+m)^{1+o(1)}`$ 字时间找到精确最大基数匹配，成功概率至少 2/3，时间界在每条计算路径上成立。同样的保证适用于寻找带指定容许顶点度的生成子图，或判定不存在。

&emsp;[Almost-Linear-Time Maximum-Cardinality Matching in General Graphs](https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/main.pdf)

**121. 编辑距离的近线性近似。** 对每个固定有理 $`\varepsilon\in(0,1)`$，在 $`N^{1+o(1)}`$ 最坏情形期望时间内给出单位代价编辑距离的随机化 $`(1+\varepsilon)`$ 近似，成功概率至少 2/3。字符串总长 <i>N</i>，符号为多项式有界整数。这是固定精度下的渐近保证。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/121.md)）

&emsp;[An Almost-Linear Approximation Scheme for Edit Distance](https://github.com/openai/math/blob/main/preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf)

**122. 带统一解码器的定量迹重构界。** 在每个固定删除概率 $`\in(0,1)`$ 处，重构任意长度 <i>n</i> 的二元串需要 $`n^{\Omega(\log\log n)}`$ 条独立迹，排除多项式样本重构。对已知固定有理保留概率，统一解码器达到拟多项式样本与运行时间界。当删除概率至多 $`n^{-\varepsilon}`$（固定 <i>ε</i> &gt; 0）时，两个界都变成输入与参数编码的多项式。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/122.md)）

&emsp;[Uniform quasipolynomial-time trace reconstruction](https://github.com/openai/math/blob/main/preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/uniform-trace-reconstruction.pdf)

&emsp;[A latest-anchor induction with spectrally compact masks for worst-case trace reconstruction](https://github.com/openai/math/blob/main/preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/paper.pdf)

&emsp;[Quantitative lower bounds for trace reconstruction](https://github.com/openai/math/blob/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf)

**124. 三台同型机的多项式时间调度。** 解决 Garey–Johnson 三处理机单位作业调度问题：确定性多项式时间算法在三台同型并行机上最小化不可抢先单位长度作业（任意先后约束）的完工时间。对显式给定的先后图，精确判定截止期可行性并构造可行调度。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/124.md)）

&emsp;[A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](https://github.com/openai/math/blob/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf)

**125. 度量 <i>k</i>-中位数的近似阈值与恢复。** 对给定候选设施的有限有理度量 <i>k</i>-中位数，对每个固定 <i>ε</i> &gt; 0 给出确定性多项式时间 $`(1+2/e+\varepsilon)`$ 近似。假设 $`P\ne NP`$，最优下确界近似因子为 $`1+2/e`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/125.md)）

&emsp;[Single-exponential recovery and bounded-price strictness for metric k-median](https://github.com/openai/math/blob/main/preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/paper.pdf)

&emsp;[The approximation threshold for metric k-median](https://github.com/openai/math/blob/main/preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/main.pdf)

**126. 完美匹配的指数半定复杂度。** 证明完美匹配多面体的每个精确半定提升都有指数规模，否定回答 Rothvoss 的多项式规模提升问题。该界甚至对其奇割松弛矩阵在任意固定移位 $`0\lt \rho\lt 1`$ 后的正半定秩成立，允许任意实半定因子。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/126.md)）

&emsp;[Exponential PSD rank of positively shifted matching matrices](https://github.com/openai/math/blob/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/shifted-matching-psd.pdf)

**127. 多项式阈值函数的平均敏感度。** 证明均匀 <i>n</i> 维布尔立方上次数至多 <i>d</i> 的多项式阈值函数平均敏感度至多 $`8d\sqrt n`$（对 $`1\le d\le n`$ 一致）。平均敏感度计单比特翻转下输出变化的期望。这建立渐近形式的 Gotsman–Linial 猜想，允许多项式零点且 $`\mathrm{sign}(0)=1`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/127.md)）

&emsp;[Average sensitivity of polynomial threshold functions](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf)

**128. 最短公共超串的因子二近似。** 给出确定性多项式时间算法：对每个显式表示的有限字符串族，构造长度至多两倍最优值的最短公共超串。运行时间在完整编码输入长度（含符号标签）上多项式。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/128.md)）

&emsp;[A Polynomial-Time 2-Approximation for Shortest Common Superstring](https://github.com/openai/math/blob/main/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf)

**129. 双向自动机的指数状态代价。** 证明补化双向非确定有限自动机与用双向确定自动机模拟单向非确定自动机都有指数下界。后者在增长有限字母表上解决 Sakoda–Sipser 状态简洁性猜想；两个结果都排除与字母表规模无关的多项式状态界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/129.md)）

&emsp;[An exponential state lower bound for two-way nondeterministic complementation](https://github.com/openai/math/blob/main/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf)

&emsp;[An exponential two-way deterministic state lower bound for one-way liveness](https://github.com/openai/math/blob/main/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf)

**130. 低于 $`n\log n`$ 的精确傅里叶变换。** 给出确定性长度 <i>n</i> 离散傅里叶变换算法，对每个 <i>n</i> 用 $`O(n(\log n)^{1-\delta})`$ 次运算，显式 $`\delta=10^{-13}`$。模型使用精确复数算术、无限制系数与给定的单位根，计入标量准备与对数字寻址。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/130.md)）

&emsp;[An explicit power saving for the exact discrete Fourier transform](https://github.com/openai/math/blob/main/preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf)

&emsp;[Finite tensor savings and exact Fourier circuits](https://github.com/openai/math/blob/main/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf)

**131. 每个度序列的图交换快速混合。** 解决简单无向 Kannan–Tetali–Vempala 猜想：惰性边交换链对每个图化带标记度序列在 $`O(n^8)`$ 时间混合。同样的度约束图也可由几乎必然终止、期望多项式位运行时间的算法精确均匀采样。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/131.md)）

&emsp;[Polynomial mixing of the switch chain for every graphical degree sequence](https://github.com/openai/math/blob/main/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026/main.pdf)

**132. 敏感度与块敏感度的超二次分离。** 构造全布尔函数使 $`\mathrm{bs}(f)\ge s(f)^\alpha`$（固定 <i>α</i> &gt; 2），否定敏感度猜想的二次强化。$`s(f)`$ 计有影响的单比特翻转，块敏感度允许不相交比特组一起翻转。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/132.md)）

&emsp;[A superquadratic separation between sensitivity and block sensitivity](https://github.com/openai/math/blob/main/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf)

**133. Weisfeiler–Leman 加细的计算复杂度。** 在指定的顺序邻接矩阵模型中，对足够大的固定 <i>k</i>，证明联合与分离 <i>k</i> 维 Weisfeiler–Leman 等价的无条件 $`n^{\Omega(k)}`$ 确定性时间下界。以维数为输入时，联合等价在次立方图上已是 EXPTIME 完全的；判定加细是否识别一个图同样 EXPTIME 完全。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/133.md)）

&emsp;[Parity lifts and bounded-treewidth witnesses for Weisfeiler–Leman equivalence](https://github.com/openai/math/blob/main/preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf)

&emsp;[The complexity of identifying a graph by Weisfeiler–Leman refinement](https://github.com/openai/math/blob/main/preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/paper.pdf)

&emsp;[Unconditional time lower bounds for Weisfeiler–Leman equivalence](https://github.com/openai/math/blob/main/preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf)

&emsp;[Variable-dimension Weisfeiler–Leman equivalence on general and subcubic graphs](https://github.com/openai/math/blob/main/preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/paper.pdf)

**134. 广义星高至多 3。** 有限字母表上的每个正则语言都有一个至多 3 层嵌套 Kleene 星的广义正则表达式（同一字母表上允许并、连接与补）。这建立与自动机规模无关的绝对界，解决广义星高问题的均匀有界性版本。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/134.md)）

&emsp;[Finite Monoid Computations and a Uniform Generalized Star-Height Bound](https://github.com/openai/math/blob/main/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf)

&emsp;[Generalized Star Height at Most Four](https://github.com/openai/math/blob/main/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf)

&emsp;[Generalized Star Height at Most Three](https://github.com/openai/math/blob/main/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf)

**135. 迭代矩阵乘法的齐次五层下界。** 在每个特征零域上，<i>n</i> 个独立 $`n\times n`$ 变量矩阵乘积的 $`(1,1)`$ 元在齐次五层和积电路中需要 $`n^{\Theta(\sqrt n)}`$ 个门。该锐利界允许共享门与涉及全部变量的底层线性形式。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/135.md)）

&emsp;[Homogeneous depth-five lower bounds for iterated matrix multiplication](https://github.com/openai/math/blob/main/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf)

**136. PPAD 的拟线性 PCP 定理。** 解决拟线性 PCP-for-PPAD 猜想。长度 <i>N</i> 的 End-of-Line 实例归约为总长 $`N(\log N)^{O(1)}`$ 的数值电路约束，使得任何满足除固定比例外全部约束（到固定精度）的多项式编码有理赋值都产生一个端点解。这样的赋值总是存在，给出只有拟线性规模开销的鲁棒局部验证。

&emsp;[The PCP-for-PPAD conjecture: a quasilinear reduction](https://github.com/openai/math/blob/main/preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/paper.pdf)

**137. 五分之二幂空间模拟单纸带时间。** 用 $`O(T^{2/5}\log^C(T+2))`$ 空间确定固定确定性单可写纸带机至时间 <i>T</i> 的停机与有限控制结果，改进平方根指数。读写头每步至多移动一格；允许有限多个只读输入头。初始内容与 <i>T</i> 无关，内容与输入符号可 polylog 空间访问。模拟时间无限制。

&emsp;[Simulating One-Tape Time in Two-Fifths-Power Space](https://github.com/openai/math/blob/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf)

**138. $`O(2^{0.49n})`$ 时间的子集和。** 对最坏情形子集和问题给出一致的随机化经典算法：在多项式位输入上以普通 $`O(2^{0.49n})`$ 字随机存取时间运行（<i>n</i> 计整数个数）。时间界在每次执行上成立，每个输入上成功概率至少 2/3。输入可含重复正整数；机器字有 $`O(n+b)`$ 位（<i>b</i> 为最大输入位长）。

&emsp;[Subset Sum in Time $`O(2^{0.49n})`$](https://github.com/openai/math/blob/main/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf)

&emsp;[A Low-Space Algorithm for Worst-Case Subset Sum](https://github.com/openai/math/blob/main/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf)

**139. 对数凹采样的次多项式查询复杂度。** 对提供极小化子且 $`I\preceq\nabla^2V\preceq2I`$ 的 $`C^2`$ 势函数，证明在总变差 1/10 内采样只需 $`C_\varepsilon d^\varepsilon`$ 次精确值与梯度查询（每个固定 <i>ε</i> &gt; 0）。该界在每次运行上成立，查询之间的计算无限制。还存在对数下界，故此神谕模型中最优幂律指数为零。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/139.md)）

&emsp;[Subpolynomial query complexity for well-conditioned log-concave sampling](https://github.com/openai/math/blob/main/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf)

**140. 无噪声高斯回归的内存–样本下界。** 对固定 <i>A</i> &gt; 0，持留 $`Ad^2`$ 位的一遍学习器为以角误差 $`0\lt \epsilon\le1/10`$、概率 2/3 恢复单位向量，需要 $`\Omega_A(d\log(1/\epsilon))`$ 个无噪声高斯样本（大 <i>d</i> 一致于精度）。计算与随机化更新无限制，但输出只使用终态、停止指标与新鲜随机性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/140.md)）

&emsp;[Memory and precision in noiseless Gaussian regression](https://github.com/openai/math/blob/main/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf)

&emsp;[Posterior replicas and conditional information in Gaussian regression](https://github.com/openai/math/blob/main/preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/paper.pdf)

&emsp;[Localization costs and information growth for exact Gaussian observations](https://github.com/openai/math/blob/main/preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/paper.pdf)

&emsp;[Projection moments, positive cap domination, and Riesz estimates on the sphere](https://github.com/openai/math/blob/main/preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/paper.pdf)

&emsp;[Replacing Gaussian observations in memory-constrained inference](https://github.com/openai/math/blob/main/preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/paper.pdf)

&emsp;[Subsphere methods for memory-sample lower bounds in noiseless Gaussian regression](https://github.com/openai/math/blob/main/preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf)

**141. 计数层级中的存在–全称实语句。** 证明实数存在理论包含于计数层级。更一般地，存在–全称实语句的真值可在该层级的某个固定层级判定，即使其整系数多项式由算术电路给出。

&emsp;[Existential–universal real sentences in the counting hierarchy](https://github.com/openai/math/blob/main/preprints/Existential-universal-real-sentences-in-the-counting-hierarchy-October-4-2026/etr-counting-hierarchy.pdf)

**142. 素域上的确定性多项式因子分解。** 给出一致的确定性算法：在位复杂度关于 $`(n+1)\log p`$ 多项式内完全分解素域 𝔽<sub>p</sub> 上每个非零稠密 <i>n</i> 次多项式（含重数）。素数以二进制给出。不需要随机性、整数分解或本原根神谕，也不需要 GRH 假设。

&emsp;[Deterministic Polynomial Factorization over Prime Fields](https://github.com/openai/math/blob/main/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf)

---

## 6. 动力系统与遍历理论（Dynamical systems and ergodic theory，12 个族）

**143. 希尔伯特第十六问题：极限环的一致界。** 解决希尔伯特第十六问题的一致有界性断言：实平面多项式向量场的孤立周期轨道个数由只依赖次数的有限常数界定。对经典五次 Liénard 系统，精确最大值为两个极限环。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/143.md)）

&emsp;[Uniform bounds for planar polynomial limit cycles](https://github.com/openai/math/blob/main/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf)

&emsp;[Two limit cycles for quintic Liénard systems](https://github.com/openai/math/blob/main/preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf)

**144. Banach 的简单勒贝格谱问题。** 在光滑动力学的范围内解决概率保持形式的 Banach 简单勒贝格谱问题：标准体积三维环面上的光滑保体积微分同胚在其整个复均值零 <i>L</i>² 空间上具有简单勒贝格谱——一个实可观测函数的双侧迭代构成该空间的正交规范基。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/144.md)）

&emsp;[A smooth three-torus diffeomorphism with simple Lebesgue spectrum](https://github.com/openai/math/blob/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/paper.pdf)

**145. Rokhlin 的多重混合问题。** 证明每个可逆混合概率保持变换是所有有限阶的混合，解决 Rokhlin 单变换多重混合问题。只要所有成对时间间隔发散，任何有限个可测集之间的相关收敛于其测度的乘积。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/145.md)）

&emsp;[Rokhlin's multiple-mixing problem for one transformation](https://github.com/openai/math/blob/main/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf)

**146. 标准映射的正度量熵。** 证明二维环面上的标准正弦映射对每个足够大的正参数具有关于面积的正度量熵。这建立 Sinai 正参数测度猜想在原族上的成立，且结论更强：完整参数尾部。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/146.md)）

&emsp;[Positive Metric Entropy for the Standard Map at Large Parameters](https://github.com/openai/math/blob/main/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf)

**147. 近边界 Birkhoff 猜想。** 对正曲率的光滑严格凸平面台球系统解决近边界 Birkhoff 猜想：只要一个完整擦掠环被逐条不变的本质曲线连续叶状化，该台球就是椭圆。由光滑闭凸焦散线组成的连续物理领圈同样充分。

&emsp;[Continuous Phase Foliations Create Analytic Caustic Collars](https://github.com/openai/math/blob/main/preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/paper.pdf)

&emsp;[Rigidity of Smooth Billiards with a Continuous Caustic Collar](https://github.com/openai/math/blob/main/preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/paper.pdf)

**148. 自相似测度的熵率维数公式。** 对直线上由有限多个压缩相似生成的每个自相似测度，证明 $`\dim_{\mathrm H}\mu=\min\{1,h_{\mathrm{RW}}/\chi\}`$，其中 $`h_{\mathrm{RW}}`$ 是随机复合映射的熵率、<i>χ</i> 是平均对数压缩率。这无需分离假设解决熵率维数猜想，允许精确重叠与不等压缩比。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/148.md)）

&emsp;[The entropy-rate dimension formula for self-similar measures on the line](https://github.com/openai/math/blob/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/main.pdf)

**149. 弱可逆质量作用系统的类内持久性。** 对每个带固定正常数率常数的有限弱可逆质量作用系统证明持久性猜想。每个正化学计量相容类（即使无界）都有公共的紧凸前向不变吸收集。因此该类中所有正轨道最终共享正的下浓度界与有限的上浓度界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/149.md)）

&emsp;[Uniform Permanence in Weakly Reversible Mass-Action Systems](https://github.com/openai/math/blob/main/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf)

&emsp;[Boundedness and persistence of weakly reversible mass-action systems](https://github.com/openai/math/blob/main/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf)

**150. 带无理角的三角台球的弱混合。** 证明每个至少有一个角相对 <i>π</i> 无理的非退化欧氏三角形中，台球流关于归一化面积乘均匀方向是弱混合的。这把遍历性强化到整个无理角类，不需要一般性或丢番图限制。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/150.md)）

&emsp;[Weak mixing of triangular billiards with an irrational angle](https://github.com/openai/math/blob/main/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf)

&emsp;[Ergodicity of triangular billiards with an irrational angle](https://github.com/openai/math/blob/main/preprints/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026.pdf)

**151. 熵猜想的 <i>C</i>¹ 反例。** 构造紧光滑流形上的非可逆 <i>C</i>¹ 自映射，其拓扑熵为零但在第二同调上特征值为 2。这否定一般 <i>C</i>¹ 自映射的同调熵下界：同调增长不必迫使正的轨道复杂度。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/151.md)）

&emsp;[A C^1 Counterexample to the Entropy Conjecture](https://github.com/openai/math/blob/main/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/article.pdf)

**152. 零熵不保证光滑正体积模型。** 构造标准非原子概率空间上的零熵遍历可逆变换，它不测度共轭于任何在紧有限维流形上保持严格正光滑概率密度的 $`C^\infty`$ 微分同胚。一个例子排除所有有限维数。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/152.md)）

&emsp;[A zero-entropy system without a smooth positive-volume model](https://github.com/openai/math/blob/main/preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/paper.pdf)

**153. Bernoulli 卷积的算术分类与非 Pisot 奇异性。** 对每个 $`\lambda\in(0,1)`$，用显式的代数单位有限集与无穷单向逼近条件分类无偏 Bernoulli 卷积的奇异与绝对连续情形。还证明在 $`(1,2)`$ 中每个四次 Salem 数的倒数处奇异性，给出超越倒数 Pisot 参数的例子。

&emsp;[Arithmetic classification and non-Pisot singularity for Bernoulli convolutions](https://github.com/openai/math/blob/main/preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/paper.pdf)

**154. 混合变换的逐点多重遍历平均。** 对可逆混合概率保持变换，证明每个有限长度的相邻多重遍历平均的几乎处处收敛。对每组有界函数，沿所有正平均长度，极限是其积分的乘积。不需要混合速率或概率空间标准性假设。

&emsp;[Pointwise Multiple Ergodic Averages for Mixing Transformations](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/multiple-ergodic-averages.pdf)

&emsp;[Pointwise convergence of fourfold ergodic averages for mixing transformations](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/fourfold-ergodic-averages.pdf)

&emsp;[Triple ergodic averages with distinct integer slopes](https://github.com/openai/math/blob/main/preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/triple-ergodic-distinct-slopes.pdf)

&emsp;[Pointwise convergence of triple ergodic averages for mixing transformations](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/pointwise-triple-ergodic-averages-mixing-transformations.pdf)

---

## 7. 组合数学（Combinatorics，37 个族）

**155. 三维周期铺砌的反例。** 构造 ℤ³ 中的有限平移铺块：它能铺满空间但不容许完全周期铺砌，在最小可能的格维数否定周期铺砌猜想。其单位立方加厚给出 ℝ³ 中的同样反例，即使允许任意实平移向量。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/155.md)）

&emsp;[A translational tile with no fully periodic tiling in dimension three](https://github.com/openai/math/blob/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/paper.pdf)

**156. Borsuk 猜想在九维失效。** 构造 ℝ⁹ 的紧子集，不能被十个直径严格更小的集合覆盖，在九维就否定 Borsuk 覆盖断言。例子由 ℝ⁴ 中直线的一秩正交投影子组成，配 Frobenius 度量。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/156.md)）

&emsp;[A nine-dimensional counterexample to Borsuk's covering assertion](https://github.com/openai/math/blob/main/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf)

**157. 图染色、团子式与 Colin de Verdière 不变量。** 否定 Hadwiger 猜想甚至其分数染色形式：独立数至多 2 的任意大有限简单图满足 $`\chi_f(G)\gt h(G)`$（$`h(G)`$ 为最大团子式阶）。还否定分数 Colin de Verdière 色数界 $`\chi_f(G)\le\mu(G)+1`$。正向地，每个有限非空图满足 $`\chi_{\mathrm{list}}(G)\le C h(G)`$（普适常数 <i>C</i>）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/157.md)）

&emsp;[A counterexample to Hadwiger's conjecture](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf)

&emsp;[A counterexample to the Colin de Verdière chromatic conjecture](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/paper.pdf)

&emsp;[A linear list-coloring bound in terms of the Hadwiger number](https://github.com/openai/math/blob/main/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf)

**158. 欧氏平面不能用五种颜色染色。** 证明欧氏平面的每个五染色都有距离为 1 的单色点对，对颜色类无任何限制。这推进 Hadwiger–Nelson 问题：与经典七染色结合，平面的色数只剩 6 与 7 两种可能。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/158.md)）

&emsp;[The Euclidean plane is not five-colorable](https://github.com/openai/math/blob/main/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf)

**159. Erdős 倒数和猜想与拟多项式 Szemerédi 界。** 证明 Erdős 猜想：倒数和发散的正整数集包含任意有限长度的等差数列。定量地，对每个固定 <i>k</i> ≥ 3，$`\{1,\ldots,N\}`$ 中无非常 <i>k</i> 项数列的子集大小至多 $`C_kN\exp[-c_k(\log N)^{\varepsilon_k}]`$（常数只依赖 <i>k</i>）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/159.md)）

&emsp;[Quasipolynomial Bounds for Arithmetic Progressions](https://github.com/openai/math/blob/main/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf)

**160. 超指数的 van der Waerden 数。** 解决 Erdős 关于 van der Waerden 数超指数增长的问题。若 $`W_r(k)`$ 是迫使每个 <i>r</i>-染色出现单色 <i>k</i> 项数列的最小区间长度，则 $`W_r(k)\gt k^{ck\lfloor\log_2 r\rfloor}`$（绝对 <i>c</i> &gt; 0，所有 <i>r</i> ≥ 2 与足够大 <i>k</i>，对 <i>r</i> 一致）。特别地，对每个固定 <i>r</i> 有 $`W_r(k)^{1/k}\to\infty`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/160.md)）

&emsp;[Quantitative Superexponential Bounds for van der Waerden Numbers](https://github.com/openai/math/blob/main/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf)

**161. Sidorenko 猜想与强制猜想的反例。** 用 35 顶点 66 边的连通二部模式否定 Sidorenko 猜想：该模式出现频率低于同边密度随机图。同一模式还否定 Skokan–Thoma 强制猜想：匹配其密度与常值图子的边密度不必迫使拟随机性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/161.md)）

&emsp;[A counterexample to Sidorenko's conjecture](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf)

**162. Ryser 覆盖猜想的反例。** 构造相交的 $`(q+1)`$ 部、$`(q+1)`$ 均匀超图，其覆盖数为 $`q+1`$ 而非预测的 <i>q</i>（每个足够大的素数 <i>q</i>），否定 Ryser 覆盖猜想。扩域上的独立构造还否定 Gyárfás 单色树覆盖猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/162.md)）

&emsp;[Balanced counterexamples to Ryser's conjecture at prime orders](https://github.com/openai/math/blob/main/preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/paper.pdf)

&emsp;[A counterexample to Ryser's covering conjecture](https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/paper.pdf)

**164. Hindman 有限和与有限积猜想。** 证明 Hindman 有限和与有限积猜想：正整数的每个有限染色都包含任意指定有限大小的集合，其非空子集和与非空子集积同色。

&emsp;[Monochromatic finite sums and products in the positive integers](https://github.com/openai/math/blob/main/preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/paper.pdf)

**165. Harary–Hill 与 Zarankiewicz 交叉数公式。** 在 Zarankiewicz 表述下解决 Harary–Hill 猜想与 Turán 砖厂问题，确定每个完全图与完全二部图的交叉数。结果证明经典画法在所有边弧连续的平面画法中的最优性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/165.md)）

&emsp;[The crossing number of complete graphs](https://github.com/openai/math/blob/main/preprints/The-crossing-number-of-complete-graphs-September-23-2026/paper.pdf)

&emsp;[The crossing number of complete bipartite graphs](https://github.com/openai/math/blob/main/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/paper.pdf)

**166. 高维 Erdős 不同距离猜想。** 对每个固定 <i>d</i> ≥ 3，ℝ<sup>d</sup> 中任意 <i>n</i> ≥ 2 个不同点至少确定 $`c_dn^{2/d}`$ 个不同距离（$`c_d\gt 0`$ 只依赖维数）。这与整数格的阶匹配，以常数因子界解决高维 Erdős 不同距离猜想。

&emsp;[The higher-dimensional Erdős distinct-distances conjecture](https://github.com/openai/math/blob/main/preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/paper.pdf)

**167. 平面不同距离与单位距离界。** 证明弱钉扎 Erdős 距离猜想：对每个固定 <i>ε</i> &gt; 0，任意 <i>n</i> 点平面集中除 $`o(n)`$ 个点外，至少确定 $`n^{1-\varepsilon}`$ 个不同非零距离。配套定理把单位距离对数界为 $`O(n^{4/3-\delta})`$（绝对 <i>δ</i> &gt; 0）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/167.md)）

&emsp;[The weak pinned planar distance theorem](https://github.com/openai/math/blob/main/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf)

&emsp;[A power saving for planar unit distances](https://github.com/openai/math/blob/main/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf)

**168. Kazhdan–Lusztig 多项式的组合不变性。** 解决完整的组合不变性猜想：任意 Coxeter 系统中同构的 Bruhat 区间具有相同的等参数 Kazhdan–Lusztig 多项式。即区间的抽象序决定多项式，即使跨不同 Coxeter 系统也如此。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/168.md)）

&emsp;[Combinatorial invariance of Kazhdan–Lusztig polynomials](https://github.com/openai/math/blob/main/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/paper.pdf)

**169. Shareshian–Wachs 初等正性。** 解决 Shareshian–Wachs 猜想的初等正性部分：每个自然单位区间图的染色拟对称函数的初等基系数都在 $`\mathbb N[q]`$ 中。系数显式计数被描述的置换，给出正性的组合解释。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/169.md)）

&emsp;[Elementary positivity of chromatic quasisymmetric functions](https://github.com/openai/math/blob/main/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/paper.pdf)

**170. 非对角 Ramsey 数的锐利对数指数。** 对每个固定整数 <i>s</i> ≥ 5，证明 $`r(s,t)=t^{s-1}/(\log t)^{s-2+o(1)}`$（$`t\to\infty`$），确定对数指数并在该尺度匹配经典上界。此处 $`r(s,t)`$ 是迫使出现 <i>s</i>-团或 <i>t</i> 顶点独立集的最少顶点数。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/170.md)）

&emsp;[The sharp logarithmic exponent of r(5,t)](https://github.com/openai/math/blob/main/preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/paper.pdf)

&emsp;[Sharp logarithmic exponents for fixed off-diagonal Ramsey numbers](https://github.com/openai/math/blob/main/preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/paper.pdf)

**171. 超立方 Ramsey 猜想。** 解决 Burr–Erdős 超立方 Ramsey 猜想：<i>n</i> 维立方体的二色 Ramsey 数为 $`\Theta(2^n)`$。即每个以普适常数倍立方体顶点数为顶点数的完全图的每个红蓝染色，都含单色立方体拷贝。

&emsp;[The hypercube Ramsey number has linear order](https://github.com/openai/math/blob/main/preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/paper.pdf)

**172. 有限欧氏 Ramsey 构形的分类。** 分类在足够高维欧氏空间的每个有限染色中、以原尺度单色出现的有限点构形。刻画是坐标域上的代数条件。还否定 Leader–Russell–Walters 猜想（每个这样的构形都是某个有限传递集的子集）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/172.md)）

&emsp;[A classification of finite Euclidean Ramsey configurations](https://github.com/openai/math/blob/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf)

**173. Seymour 第二邻域猜想。** 证明 Seymour 第二邻域猜想：每个非空有限有向图都有这样的顶点——其有向距离恰为 2 的顶点数不少于有向距离为 1 的顶点数。有向图除禁自环与成对反向边外任意。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/173.md)）

&emsp;[A proof of Seymour’s second-neighborhood conjecture](https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf)

**174. 强细生成树的确定性构造。** 构造性解决强细树猜想。每个至少两顶点的有限无环 <i>k</i>-边连通多重图都有生成树：对每个割，其含边比例至多为普适的 $`C/k`$。这样的树可在多项式时间确定性找到，即使并行边重数按二进制编码。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/174.md)）

&emsp;[The strong thin tree conjecture](https://github.com/openai/math/blob/main/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf)

&emsp;[A polynomial-time construction of strong thin trees](https://github.com/openai/math/blob/main/preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/paper.pdf)

**175. Talagrand 期望阈值、离散凸性与图分解。** 证明整数与分数期望阈值至多相差普适因子，解决 Talagrand 离散凸性猜想。应用证明 Ascoli–He–Park–Talagrand 图分解猜想：每个图的边分成普适有界数目的固定类，每类的容含阈值至多为原图整数期望阈值的普适常数倍。各类的嵌入不必在共享顶点上一致。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/175.md)）

&emsp;[Graph Decompositions at the Integral Expectation Threshold](https://github.com/openai/math/blob/main/preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/graph-threshold-decompositions.pdf)

&emsp;[Integral and fractional expectation thresholds are equivalent](https://github.com/openai/math/blob/main/preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/paper.pdf)

&emsp;[Talagrand’s discrete-convexity conjecture](https://github.com/openai/math/blob/main/preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/paper.pdf)

**176. 带边计数的第二 Kahn–Kalai 猜想。** 证明第二 Kahn–Kalai 猜想：对每个有 <i>h</i> ≥ 1 条边、至多 <i>n</i> 个顶点的有限简单图 <i>H</i>，其在 $`G(n,p)`$ 中的出现阈值至多 $`C p_{\mathrm E}(n,H)(1+\log_2 h)`$（普适 <i>C</i>）。$`p_{\mathrm E}`$ 是使 <i>H</i> 的每个子图期望拷贝数至少 1/2 的最小密度。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/176.md)）

&emsp;[The second Kahn–Kalai conjecture](https://github.com/openai/math/blob/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf)

**177. 有界度余边界扩张图。** 对每个 <i>d</i> ≥ 3，构造任意大的有限 <i>d</i> 维单纯复形：顶点度一致有界，且在 <i>d</i> 以下每个维度有一致 𝔽₂ 余边界扩张。与已知的图及二维情形结合，这建立每个正维数此类扩张图的存在性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/177.md)）

&emsp;[Bounded-degree coboundary expanders in every dimension](https://github.com/openai/math/blob/main/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/paper.pdf)

**178. 每个固定度的确定性非二部 Ramanujan 图。** 对每个固定 <i>d</i> ≥ 3，在每个足够大的偶数 <i>n</i> 顶点上构造简单 <i>d</i>-正则非二部 Ramanujan 图，其每个非常数邻接特征值严格位于 $`\pm2\sqrt{d-1}`$ 之间。确定性算法以多项式位时间输出完整邻接表，指数依赖 <i>d</i>。

&emsp;[Deterministic nonbipartite Ramanujan graphs in every fixed degree](https://github.com/openai/math/blob/main/preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/paper.pdf)

**179. 循环 Hadamard 与 Barker 序列猜想。** 证明实循环 Hadamard 矩阵恰在阶 1 与 4 存在，解决循环 Hadamard 猜想。结合经典 Barker 序列结果，非平凡非周期自相关幅值至多 1 的二元序列在 <i>n</i> &gt; 1 时存在当且仅当 $`n\in\{2,3,4,5,7,11,13\}`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/179.md)）

&emsp;[The circulant Hadamard conjecture](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf)

**180. Barnette 哈密顿圈猜想。** 证明每个有限简单三次二部平面 3-顶点连通图都有哈密顿圈，解决 Barnette 猜想。等价地，有限简单三次 3-顶点连通二部 Pfaffian 图中的每条三边路径都在某个哈密顿圈上。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/180.md)）

&emsp;[Paired states and Hamiltonian cycles in cubic bipartite planar graphs](https://github.com/openai/math/blob/main/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf)

**181. Erdős–Gallai 圈分解猜想。** 证明 <i>n</i> 个顶点的有限简单无向图的边可以分成至多 $`Cn`$ 个简单圈与单边（绝对常数 <i>C</i>）。这解决 Erdős–Gallai 圈分解猜想，即使对稠密图也给出线性界的块数。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/181.md)）

&emsp;[A linear cycle-and-edge decomposition of every graph](https://github.com/openai/math/blob/main/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/main.pdf)

**182. 相交多项式差与素数变元的幂节省。** 对每个固定次数 <i>k</i> ≥ 2、首项系数为正的相交整多项式 <i>h</i>，证明避开非零值 <i>h(1),h(2),…</i> 作为差的 $`\{1,\ldots,N\}`$ 子集大小为 $`O_h(N^{1-c_k})`$（$`c_k\gt 0`$ 只依赖次数）。此处「相交」指对每个模都有根。对素数变元，当 <i>h</i> 对每个模有单位根时也有幂节省，指数可依赖 <i>h</i>。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/182.md)）

&emsp;[A power saving for intersective polynomial differences with an exponent depending only on the degree](https://github.com/openai/math/blob/main/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/power-saving-intersective-polynomial-differences.pdf)

&emsp;[A Power Saving for Polynomial Differences at Prime Arguments](https://github.com/openai/math/blob/main/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf)

&emsp;[A power saving for square-difference-free sets](https://github.com/openai/math/blob/main/preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf)

**183. 平面平分线与 <i>k</i>-集的幂节省。** 对无三点共线的集合把平面平分线界改进到 $`O(n^{4/3-\varepsilon})`$（绝对 <i>ε</i> &gt; 0）。更一般地，无三点共线的 <i>n</i> 点集有 $`O(n(k+1)^{1/3-\varepsilon_0})`$ 个严格可分的 <i>k</i>-子集（$`1\le k\le n/2`$，绝对 $`\varepsilon_0\gt 0`$）。常数与正指数非定量。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/183.md)）

&emsp;[A power saving for planar halving lines](https://github.com/openai/math/blob/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf)

**184. 带固定禁用子图的对应染色。** 以对应染色形式证明 Alon–Krivelevich–Sudakov 染色猜想：避免任何固定子图 <i>F</i> 的图在最大度 <i>Δ</i> 足够大时只需 $`O_F(\Delta/\log\Delta)`$ 种颜色。还证明 Ajtai–Erdős–Komlós–Szemerédi 独立性猜想：对固定 <i>r</i> ≥ 4，每个平均度 <i>d</i> ≥ 2 的 <i>n</i> 顶点 <i>K</i><sub>r</sub>-自由图有大小 $`\Omega_r(n\log d/d)`$ 的独立集。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/184.md)）

&emsp;[Correspondence coloring graphs with a forbidden clique](https://github.com/openai/math/blob/main/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf)

&emsp;[A logarithmic independence bound for clique-free graphs](https://github.com/openai/math/blob/main/preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/paper.pdf)

**185. 无穷拟阵交与装填/覆盖的反例。** 用可数无穷底集上两个自对偶分拆拟阵，在 ZFC 内否定无限制的无穷拟阵交与装填/覆盖猜想。同样的例子否定回答 Joó 的分拆拟阵问题。它们既非有限也非余有限，因此 Nash-Williams 原始有限性猜想不在结果范围内。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/185.md)）

&emsp;[A Counterexample to the Infinite Matroid Packing/Covering Conjecture](https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf)

**186. 图与超图性质的一致影响与锐利阈值。** 证明图与固定均匀性超图的 Friedgut–Kalai 阈值宽度猜想。对固定 $`0\lt \varepsilon\lt 1/2`$，每个非平凡递增重标记不变性质从概率 <i>ε</i> 越过到 $`1-\varepsilon`$ 的宽度：图为 $`O((\log n)^{-2})`$，<i>r</i>-均匀超图为 $`O_r((\log n)^{-r/(r-1)})`$（<i>r</i> ≥ 3）。超图影响界也适用于非单调性质。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/186.md)）

&emsp;[A uniform influence bound for hypergraph properties](https://github.com/openai/math/blob/main/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf)

&emsp;[A Sharp Threshold Bound for Monotone Graph Properties](https://github.com/openai/math/blob/main/preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf)

**187. 21 步拿下 Snaky。** 解决 Snaky 成就问题：在初始为空的无穷方格板上，maker 可在 21 步内强制拿下六格 Snaky 形。maker 先行，每回合各占一格，平移、旋转与翻转均算胜。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/187.md)）

&emsp;[Snaky in 21 Maker moves](https://github.com/openai/math/blob/main/preprints/Snaky-in-21-Maker-moves-September-25-2026/article.pdf)

**188. 随机三角形删除的锐利终末边缘。** 从 <i>n</i> 个顶点的完全图出发，反复删除均匀选取的剩余三角形。终末边数渐近于 $`n^{3/2}/(2\sqrt2)`$，按 <i>n</i>^(3/2) 归一化后均方收敛。这证明 Joos–Kühn 锐利常数猜想的三角形情形。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/188.md)）

&emsp;[The sharp terminal leave in random triangle removal](https://github.com/openai/math/blob/main/preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026.pdf)

**189. 圈–团 Ramsey 数。** 证明 Erdős–Faudree–Rousseau–Schelp 猜想：$`R(C_m,K_n)=(m-1)(n-1)+1`$ 对每个 $`m\ge n\ge3`$ 成立（除 $`R(C_3,K_3)=6`$）。这是每个完全图红蓝染色中迫使红色 <i>m</i>-圈或蓝色 <i>n</i>-团的精确阈值。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/189.md)）

&emsp;[Cycle--clique Ramsey numbers](https://github.com/openai/math/blob/main/preprints/Cycle-clique-Ramsey-numbers-September-25-2026/Cycle-clique-Ramsey-numbers-September-25-2026.pdf)

**190. 有序二元矩阵的多项式删除失效。** 用一个固定的 $`66\times66`$ 0–1 模式否定多项式有序二元矩阵删除。矩阵可能需要许多比特改动才能变成无模式状态，而其拷贝密度小于每个关于该距离提出的多项式界。拷贝保持行列顺序并匹配 0 与 1。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/190.md)）

&emsp;[Polynomial removal fails for ordered binary matrices](https://github.com/openai/math/blob/main/preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/paper.pdf)

**191. Heilbronn 三角形下界的幂改进。** 对每个足够大的 <i>n</i>，构造单位正方形内 <i>n</i> 个点，使每个三角形面积至少 $`n^{-2+c}`$（绝对 <i>c</i> &gt; 0）。这否定 Heilbronn 三角形问题中猜测的近乎 <i>n</i>^(−2) 上界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/191.md)）

&emsp;[A power improvement in the Heilbronn triangle lower bound](https://github.com/openai/math/blob/main/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026/main.pdf)

**192. 布尔函数以任意因子违反平方根次数界。** 否定连接布尔函数线性傅里叶系数与其多项式次数的平方根界。对每个 <i>C</i> &gt; 0，存在符号值布尔函数 <i>f</i> 使 $`\sum_i\widehat f(\{i\})\gt C\sqrt{\deg(f)}`$。即其与单个输入比特的总带符号相关可超过该界任意因子。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/192.md)）

&emsp;[Unbounded Violations of the Square-Root Degree Bound](https://github.com/openai/math/blob/main/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf)

---

## 8. 代数（Algebra，18 个族）

**193. Serre 交重数猜想。** 对任意正则局部环上非零有限生成模证明 Serre 交重数 $`\chi^R(M,N)`$ 的严格正性，条件为 $`M\otimes_R N`$ 有限长且 $`\dim M+\dim N=\dim R`$。这解决正性猜想，包括分歧混合特征情形。

&emsp;[Positivity of Serre's Intersection Multiplicity](https://github.com/openai/math/blob/main/preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/paper.pdf)

**194. Lech 重数猜想。** 对每个非零 Noether 局部环的平坦局部同态证明 $`e(R)\le e(S)`$（<i>e</i> 为 Hilbert–Samuel 重数）。在每个维数与每个特征下解决 Lech 猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/194.md)）

&emsp;[Lech's multiplicity conjecture](https://github.com/openai/math/blob/main/preprints/Lechs-multiplicity-conjecture-September-23-2026/paper.pdf)

**195. 小 Cohen–Macaulay 模猜想的反例。** 构造 ℂ 上三维完备 Noether 法向局部域，它没有任何非零有限生成极大 Cohen–Macaulay 模。ℂ 上本质有限型的三维局部域具有同样性质，否定小 Cohen–Macaulay 模猜想的整域形式。

&emsp;[A Complete Local Domain without a Small Cohen–Macaulay Module](https://github.com/openai/math/blob/main/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/paper.pdf)

**196. Kaplansky 零因子猜想的反例。** 构造有限表现无挠群 <i>G</i>，其群代数 $`\mathbb F_2[G]`$ 有非零零因子，否定 Kaplansky 零因子猜想。该群有有限二维分类空间。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/196.md)）

&emsp;[A Torsion-Free Group Algebra with Zero Divisors](https://github.com/openai/math/blob/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf)

**197. 非直有限的无挠群代数。** 构造有限表现无挠非 sofic 群，其 𝔽₂ 上群代数非直有限，即使在无挠时也否定 Kaplansky 猜想。配套例子在所有构形上给出单而非满的细胞自动机，驳斥 Gottschalk 满射性猜想。另一反例是整群环矩阵：在有理群环上可逆，但 Fuglede–Kadison 行列式严格介于 0 与 1 之间，否定无限制的行列式猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/197.md)）

&emsp;[A Torsion-Free Group Algebra That Is Not Directly Finite](https://github.com/openai/math/blob/main/preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/direct-finiteness.pdf)

&emsp;[A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two](https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf)

&emsp;[A Counterexample to the Group-Ring Determinant Conjecture](https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf)

&emsp;[A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Odd Characteristic](https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf)

**198. 有限维数有限性的反例。** 构造有限维复代数，其有限维模的有限投射维数无界。这否定小有限维数猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/198.md)）

&emsp;[An algebra of infinite little finitistic dimension](https://github.com/openai/math/blob/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/paper.pdf)

**199. Auslander–Reiten、Tachikawa 及相关同调猜想的反例。** 在特征二有理函数域上构造有限维代数，否定 Auslander–Reiten 猜想、Gorenstein 投射猜想与 Tachikawa 第二猜想。相关的自同态代数还否定经典、广义与强 Nakayama 猜想、Auslander–Gorenstein 猜想与 Wakamatsu 倾斜猜想。反例在基域的任何扩张下持续存在。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/199.md)）

&emsp;[An explicit counterexample to the Auslander-Reiten conjecture](https://github.com/openai/math/blob/main/preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/paper.pdf)

&emsp;[A counterexample to Tachikawa's second conjecture](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf)

**200. Eisenbud–Green–Harris 与 lex-plus-powers。** 在每个特征零域上证明 Eisenbud–Green–Harris 与 lex-plus-powers 猜想。任何包含正则序列（任意长度、次数至少 2）的分次理想，都容许具有相同 Hilbert 函数、分次 Betti 数不更小的 lex-plus-powers 理想。

&emsp;[The Artinian Lex-Plus-Powers Betti Theorem](https://github.com/openai/math/blob/main/preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/paper.pdf)

&emsp;[Commuting Division-Coefficient Forms and the Artinian Eisenbud--Green--Harris Conjecture](https://github.com/openai/math/blob/main/preprints/Commuting-Division-Coefficient-Forms-and-the-Artinian-Eisenbud-Green-Harris-Conjecture-September-23-2026/paper.pdf)

**201. Kurosh 可除环问题的反例。** 构造可数特征零可除环：在其中心上代数、由中心上两个元素生成，但在中心上维数无穷。这否定回答 Kurosh 关于局部有限性的可除环问题。

&emsp;[A Counterexample to Kurosh’s Division-Ring Problem](https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-Kuroshs-Division-Ring-Problem-September-23-2026/paper.pdf)

**202. 分块 Alperin 权猜想。** 对每个素数与每个有限群证明数值分块 Alperin 权猜想：块中不可约 Brauer 特征数等于其权共轭类数。

&emsp;[The Blockwise Alperin Weight Conjecture](https://github.com/openai/math/blob/main/preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/paper.pdf)

**203. 域与完全混合特征 DVR 上的 Donovan 猜想。** 证明 Donovan 猜想：在每个固定代数闭特征 <i>p</i> 域上，亏度群阶有界的有限群块只有有限多个 Morita 等价类（每个素数 <i>p</i>）。还证明在每个剩余域代数闭的完全混合特征离散赋值环上的整形式。

&emsp;[Donovan's Conjecture over Algebraically Closed Fields](https://github.com/openai/math/blob/main/preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/main.pdf)

&emsp;[Integral Donovan Finiteness over Witt Vectors](https://github.com/openai/math/blob/main/preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/main.pdf)

**204. 偶旋量群的张量饱和。** 对 $`\mathop{\mathrm{Spin}}\nolimits(2n)`$（<i>n</i> ≥ 2）证明饱和因子为 1：对和落在根格中的三个支配整权，任意公共正整放大处的非负不变已经给出原权处的非负不变。这解决单线饱和猜想的 <i>D</i> 型部分。

&emsp;[Tensor saturation for even spin groups](https://github.com/openai/math/blob/main/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026.pdf)

**205. Saxl 猜想与泛张量平方。** 证明 Saxl 猜想：每个阶梯表示的张量平方包含对应对称群的每个不可约复表示。更一般地，$`n\notin\{2,4,9\}`$ 的每个 <i>S</i><sub>n</sub> 都有不可约表示，其张量平方包含所有不可约表示。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/205.md)）

&emsp;[Universal Tensor Squares for Symmetric Groups](https://github.com/openai/math/blob/main/preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/main.pdf)

&emsp;[A Cyclic Polytabloid Proof of Saxl's Conjecture](https://github.com/openai/math/blob/main/preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/paper.pdf)

**206. 有限格表示与不可判定性。** 有些有限格不是任何有限代数的同余格，否定回答有限格表示问题。此外，没有算法判定有限格是否有这样的表示，或它是否是有限群的满子群区间。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/206.md)）

&emsp;[Finite congruence lattices: characterization and undecidability](https://github.com/openai/math/blob/main/preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/paper.pdf)

&emsp;[A negative solution to the finite lattice representation problem](https://github.com/openai/math/blob/main/preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/paper.pdf)

**207. 所有离散群的 <i>ℓ</i>¹-Bass 猜想。** 对每个离散群证明 <i>ℓ</i>¹-Bass 猜想：$`\ell^1(G)`$ 上幂等矩阵的 Hattori–Stallings 迹支撑在有限多个有限阶共轭类上。代数配套结果证明积分 Bass 迹猜想与无挠群上 Kaplansky 幂等猜想（在每个交换含幺特征零整域上）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/207.md)）

&emsp;[The ℓ¹-Bass Conjecture for Discrete Groups](https://github.com/openai/math/blob/main/preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/l1-bass-conjecture.pdf)

&emsp;[The Bass trace conjecture and the characteristic-zero Kaplansky idempotent conjecture](https://github.com/openai/math/blob/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf)

**208. 有限对称张量范畴与 Verlinde 塔。** 证明特征 <i>p</i> &gt; 0 代数闭域 <i>k</i> 上每个有限对称张量范畴都容许到更高 Verlinde 范畴 $`\mathrm{Ver}_{p^n}`$ 的 <i>k</i>-线性正合忠实强对称幺半群纤维函子。层级可依赖范畴，定理包括特征二，解决 Benson–Etingof–Ostrik 猜想的有限情形。

&emsp;[Fiber functors for finite symmetric tensor categories in positive characteristic](https://github.com/openai/math/blob/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/paper.pdf)

**209. Gersten 猜想的整反例。** 否定 3 与 5 次的无限制整 Gersten 单射性。两个显式的二维分歧正则局部环（混合特征 (0,5)）有非零整 <i>K</i>-理论类，在分式域上为零。

&emsp;[An integral counterexample to Gersten's conjecture](https://github.com/openai/math/blob/main/preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026.pdf)

&emsp;[An integral degree-three Gersten counterexample](https://github.com/openai/math/blob/main/preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/paper.pdf)

**210. 六次幂的 Foulkes 猜想与二次稳定化。** 证明 Foulkes 猜想第六情形：对每个 <i>b</i> ≥ 6 与有限维复 <i>V</i>，$`\mathrm{Sym}^6(\mathrm{Sym}^bV)`$ 等变嵌入 $`\mathrm{Sym}^b(\mathrm{Sym}^6V)`$。更一般地，典范乘法映射 $`\mathrm{Sym}^b(\mathrm{Sym}^aV)\to\mathrm{Sym}^a(\mathrm{Sym}^bV)`$ 在 <i>a</i> ≥ 2、$`b\ge a(a-1)`$ 时满射，给出维数无关的二次稳定化。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/210.md)）

&emsp;[Foulkes' conjecture for the sixth symmetric power](https://github.com/openai/math/blob/main/preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/main.pdf)

&emsp;[Quadratic stabilization of the canonical Foulkes--Howe map](https://github.com/openai/math/blob/main/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/paper.pdf)

---

## 9. 概率与统计力学（Probability and statistical mechanics，29 个族）

**211. 随机平面地图的几何相图、扩散与谱。** 临界 Fortuin–Kasteleyn 平面地图在 $`0\lt q\le4`$ 时收敛到刘维尔量子引力球面、<i>q</i> &gt; 4 时收敛到布朗连续随机树，建立面–树几何相变。对 FK–Ising 与生成树加权地图，平稳随机游走收敛到极限球面上的刘维尔布朗运动。FK–Ising 谱结果还给出特征值与热迹的收敛（以所述布朗/LQG 输入为前提）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/211.md)）

&emsp;[Random Walks on Critical FK–Ising Maps and Liouville Brownian Motion](https://github.com/openai/math/blob/main/preprints/Random-Walks-on-Critical-FK-Ising-Maps-and-Liouville-Brownian-Motion-October-5-2026/fk-ising-walk-limit.pdf)

&emsp;[Spectral convergence for critical FK–Ising planar maps](https://github.com/openai/math/blob/main/preprints/Spectral-convergence-for-critical-FK-Ising-planar-maps-October-5-2026/spectral-convergence-critical-fk-ising-planar-maps.pdf)

&emsp;[A Linear Clock for Random Walk on Tree-Weighted Planar Maps](https://github.com/openai/math/blob/main/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/linear-clock-random-walk-tree-weighted-planar-maps.pdf)

&emsp;[Canonical conformal limits of subcritical FK planar maps](https://github.com/openai/math/blob/main/preprints/Canonical-conformal-limits-of-subcritical-FK-planar-maps-September-24-2026/main.pdf)

&emsp;[The critical Liouville quantum sphere and geometric limits of FK maps at q=4](https://github.com/openai/math/blob/main/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/main.pdf)

&emsp;[Metric-measure limits of subcritical FK and spanning-tree planar maps](https://github.com/openai/math/blob/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/main.pdf)

&emsp;[Brownian continuum random tree limits of finite Fortuin–Kasteleyn maps above four](https://github.com/openai/math/blob/main/preprints/Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026/main.pdf)

**212. 平面首达渗流的几何与双测地线的不存在性。** 证明：对 iid 非负非原子边权（四个权的最小值二阶矩有限），平面首达渗流没有双无穷测地线。指数权下极限形状严格凸且边界 $`C^1`$。对每个正形状与速率的 Gamma 律同样可微。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/212.md)）

&emsp;[No bigeodesics in planar first-passage percolation](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf)

&emsp;[Strict convexity and differentiability of the planar exponential first-passage limit shape](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf)

**213. 每个拟传递图上的临界渗流。** 解决 Benjamini–Schramm 临界性猜想在边渗流的情形：对每个 $`p_c\lt 1`$ 的无限连通局部有限拟传递图，临界概率下几乎必然没有无穷分支。该族还对 ℤ³ 的最近邻边渗流与点渗流建立同一结论。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/213.md)）

&emsp;[Critical bond and site percolation on the cubic lattice](https://github.com/openai/math/blob/main/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf)

&emsp;[No percolation at criticality on quasi-transitive graphs](https://github.com/openai/math/blob/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf)

**214. Benjamini–Schramm 非唯一性猜想。** 对每个无限连通局部有限非amenable拟传递图证明 Bernoulli 边渗流的 $`p_c\lt p_u`$，解决 Benjamini–Schramm 非唯一性猜想。即存在非空概率区间使无穷分支有无穷多个。更强的算子界还建立临界三角形条件。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/214.md)）

&emsp;[Nonuniqueness of percolation on nonamenable quasi-transitive graphs](https://github.com/openai/math/blob/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf)

**215. 规范 O(3) 连续极限与精确 O(4) 质量渐近。** 构造二维最近邻 O(3) 模型的规范连续极限：非高斯局部相对论性理论，唯一真空、正质量隙。对方格 O(4) 模型，确定完整转移隙的精确首项渐近 $`m_{\mathrm{lat}}(\beta)\sim32e^{\pi/4-1/2}\sqrt\beta\,e^{-\pi\beta}`$。该族还对 <i>n</i> ≥ 3 的二维最近邻 O(<i>n</i>) 模型在每个正温度证明自旋相关指数衰减。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/215.md)）

&emsp;[The canonical massive continuum limit of the two-dimensional O(3) model](https://github.com/openai/math/blob/main/preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/massive-continuum-o3.pdf)

&emsp;[An Isolated Particle Pole for the Two-Dimensional O(3) Spin Field](https://github.com/openai/math/blob/main/preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/o3-particle-pole.pdf)

&emsp;[Exact mass asymptotics for the two-dimensional O(4) lattice model](https://github.com/openai/math/blob/main/preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/exact-mass-o4.pdf)

&emsp;[Sharp mass bounds for the two-dimensional O(4) model](https://github.com/openai/math/blob/main/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf)

&emsp;[Exponential decay in two-dimensional classical O(n) models](https://github.com/openai/math/blob/main/preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf)

**216. 临界与近临界 XY 标度与 BKT 普适性。** 对方格最近邻余弦 XY 模型，证明临界轴向相关 $`C_{\beta_c}(r)\sim Ar^{-1/4}(\log r)^{1/8}`$ 与 Berezinskii–Kosterlitz–Thouless 本性奇点 $`\sqrt{\beta_c-\beta}\log\xi(\beta)\to B`$（自由盒热力学极限后 $`A,B\gt 0`$）。对含最近邻的有限方对称相互作用，离散高斯高度在整个粗糙相（含其阈值）沿几何环面尺寸收敛到高斯场。临界中心磁化与自旋场结论保留所述高度、重整化与场输入假设。

&emsp;[The critical logarithmic correction for the planar XY model](https://github.com/openai/math/blob/main/preprints/The-critical-logarithmic-correction-for-the-planar-XY-model-October-5-2026/paper.pdf)

&emsp;[Critical Center Magnetization in the Planar XY Model](https://github.com/openai/math/blob/main/preprints/Critical-Center-Magnetization-in-the-Planar-XY-Model-October-5-2026/paper.pdf)

&emsp;[The Critical Spin Field of the Planar XY Model](https://github.com/openai/math/blob/main/preprints/The-Critical-Spin-Field-of-the-Planar-XY-Model-October-5-2026/paper.pdf)

&emsp;[Essential Singularity of the Correlation Length in the Planar XY Model](https://github.com/openai/math/blob/main/preprints/Essential-Singularity-of-the-Correlation-Length-in-the-Planar-XY-Model-October-5-2026/paper.pdf)

&emsp;[The critical correlation exponent of the planar XY model](https://github.com/openai/math/blob/main/preprints/The-critical-correlation-exponent-of-the-planar-XY-model-September-24-2026/paper.pdf)

&emsp;[BKT universality for height and planar spin fields](https://github.com/openai/math/blob/main/preprints/BKT-universality-for-height-and-planar-spin-fields-September-24-2026/paper.pdf)

**217. 低温 Sherrington–Kirkpatrick 涨落律。** 对每个固定逆温度 <i>β</i> &gt; 1，确定零场高斯 SK 对数配分函数的涨落尺度与极限律。方差渐近于 $`c_\beta n^{1/3}`$（$`c_\beta\gt 0`$），确证预测的 <i>n</i>^(1/6) 标准差尺度。精确中心化与标准化给出完整序列收敛到唯一刻画的非退化律。

&emsp;[The low-temperature Sherrington–Kirkpatrick free-energy limiting law](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026.pdf)

&emsp;[The low-temperature Sherrington–Kirkpatrick fluctuation scale](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026.pdf)

**218. 弱相互作用与随机键 Ising 模型的共形普适性。** 方格 Ising 模型的弱有限程方对称偶多自旋扰动保持临界体自旋与能量极限；弱方对称轮廓相互作用还给出弦状 SLE₃ 界面极限。取足够弱的 iid 键无序（固定有界非退化均值零律）时，临界自旋界面在环境概率下收敛到同一律。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/218.md)）

&emsp;[Quenched SLE₃ limits for general weak random-bond Ising models](https://github.com/openai/math/blob/main/preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/general-weak-random-bond-ising.pdf)

&emsp;[Quenched SLE₃ Universality for the Weak Random-Bond Ising Model](https://github.com/openai/math/blob/main/preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/quenched-sle3-weak-random-bond-ising.pdf)

&emsp;[Logarithmic Relative Fluctuations in the Weakly Disordered Planar Ising Model](https://github.com/openai/math/blob/main/preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/critical-relative-second-moment-weak-random-bond-ising.pdf)

&emsp;[Conformal universality of bulk Ising correlations under weak interactions](https://github.com/openai/math/blob/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/paper.pdf)

&emsp;[SLE3 universality for weak finite-range Ising interactions](https://github.com/openai/math/blob/main/preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026/paper.pdf)

&emsp;[Buffered comparison and stopping-band resolution in critical Ising](https://github.com/openai/math/blob/main/preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/paper.pdf)

**219. 弱 Anderson 无序正则图的 GOE 体普适性。** 对每个固定度 <i>d</i> ≥ 3，均匀随机 <i>d</i>-正则简单图的体邻接特征值点过程收敛到高斯正交系综律，包括三次图。在干净谱边内部的紧频带内，同样固定能量普适性在足够弱的固定 iid 均匀对角无序下保持。

&emsp;[Fixed-energy universality for weak Anderson disorder on random regular graphs](https://github.com/openai/math/blob/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/fixed-energy-universality-weak-anderson-disorder-random-regular-graphs.pdf)

&emsp;[GOE bulk universality for fixed-degree random regular graphs](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/paper.pdf)

**220. 超出 iid 环境与 iid 弹道性的方向 0–1 律。** 在 ℤ<sup>d</sup>（<i>d</i> ≥ 3），对 iid 严格椭圆最近邻环境，以及一致椭圆下的平稳遍历有限程相依环境，方向逃逸概率为 0 或 1。在 <i>d</i> ≥ 2 的 iid 一致椭圆环境中，几乎必然方向暂态蕴含在该方向有正投影的确定性极限速度，解决弹道性猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/220.md)）

&emsp;[A directional zero–one law for finite-range-dependent random environments](https://github.com/openai/math/blob/main/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/directional-zero-one-finite-range.pdf)

&emsp;[A directional zero–one law under strict ellipticity](https://github.com/openai/math/blob/main/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf)

&emsp;[Directional transience implies ballisticity](https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf)

**221. 稀释自旋玻璃的 Mézard–Parisi 公式。** 对满足 Panchenko–Talagrand 分解与正性假设的泊松稀释偶元 Ising 模型（只需一阶矩可积），证明 Mézard–Parisi 层次腔公式。极限自由能等于有限深度层次试验律的下确界。这包括 Viana–Bray 模型、对称稀释偶自旋模型与加权的软偶 <i>K</i>-可满足性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/221.md)）

&emsp;[The Mézard–Parisi formula for diluted spin glasses](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf)

**222. 感知机自由能与微观堵塞指数。** 确定有界 Borel 对数势的高斯 Ising 感知机与有界连续势的高斯球面感知机在每个正图案密度下的有限温度变分自由能。球面扩展处理双正交不变无序（极限奇异值分布紧、无离群值）。在裕度 −1 处，二次罚球面模型有锐利可行性阈值与极限间隙与力律（系统规模、零温度、临界密度依次取极限）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/222.md)）

&emsp;[The free energy of the Ising random perceptron](https://github.com/openai/math/blob/main/preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/The-free-energy-of-the-Ising-random-perceptron-September-24-2026.pdf)

&emsp;[Microscopic jamming in the negative spherical perceptron](https://github.com/openai/math/blob/main/preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026.pdf)

&emsp;[The spherical perceptron with bi-orthogonally invariant disorder](https://github.com/openai/math/blob/main/preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026.pdf)

&emsp;[The free energy of the spherical random perceptron](https://github.com/openai/math/blob/main/preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/The-free-energy-of-the-spherical-random-perceptron-September-24-2026.pdf)

**223. 随机簇界面：临界、无序、热与自然时间标度。** 证明临界方格随机簇界面的弦状 SLE<sub>κ</sub> 极限（$`0\lt q\le4`$，$`\kappa=4\pi/\arccos(-\sqrt q/2)`$）：<i>q</i> ≥ 1 时允许有界 Jordan 域，<i>q</i> &lt; 1 时允许光滑 Jordan 域（在所述标记边界逼近下）。$`1\le q\le4`$ 时完整嵌套平面环收敛到 CLE<sub>κ</sub>。

&emsp;[Square-lattice FK interfaces and nested loops for 1 <= q < 4](https://github.com/openai/math/blob/main/preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/paper.pdf)

&emsp;[Self-dual random-cluster interfaces below one](https://github.com/openai/math/blob/main/preprints/Self-dual-random-cluster-interfaces-below-one-September-23-2026/paper.pdf)

&emsp;[Quenched SLE Universality for Weakly Disordered FK–Ising Interfaces](https://github.com/openai/math/blob/main/preprints/Quenched-SLE-Universality-for-Weakly-Disordered-FK-Ising-Interfaces-October-5-2026/quenched-fk-ising.pdf)

&emsp;[Thermal FK–Ising interfaces and massive SLE](https://github.com/openai/math/blob/main/preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/paper.pdf)

&emsp;[Natural Occupation Measures for Critical Square-Lattice FK Interfaces](https://github.com/openai/math/blob/main/preprints/Natural-Occupation-Measures-for-Critical-Square-Lattice-FK-Interfaces-October-5-2026/natural-occupation-measures-critical-square-lattice-fk-interfaces.pdf)

&emsp;[Conformal Limits of Critical Square-Lattice Random-Cluster Interfaces](https://github.com/openai/math/blob/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/paper.pdf)

**224. 泊松–Voronoi 渗流的临界与淬火近临界普适性。** 对每个有界 Jordan 四边形中的退火临界泊松–Voronoi 穿越概率证明 Cardy 公式。以各模型自身期望单位方格关键计数归一化后，有理多边形四边形的条件联合近临界穿越阈值律在环境概率下收敛到三角格参考律。这建立穿越阈值的淬火近临界普适性。

&emsp;[From critical crossings to quenched near-critical universality in Voronoi percolation](https://github.com/openai/math/blob/main/preprints/From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026/critical-crossings-quenched-near-critical-universality-voronoi-percolation.pdf)

&emsp;[A Pivotal Amplitude for Voronoi Percolation from Cardy's Formula](https://github.com/openai/math/blob/main/preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026/voronoi-pivotal-amplitude.pdf)

&emsp;[Cardy’s formula for critical Poisson–Voronoi percolation](https://github.com/openai/math/blob/main/preprints/Cardys-formula-for-critical-Poisson-Voronoi-percolation-September-23-2026/paper.pdf)

**225. 平衡六顶点区域全程的高斯自由场极限。** 平衡方格六顶点高度场（$`a=b=1`$、$`0\lt c\le2`$）收敛到高斯自由场，包括端点 <i>c</i> = 2。平面态由平衡环面极限定义。对单位高度增量与 Green 核 $`-(2\pi)^{-1}\log|x-y|`$，精确方差乘子为 $`1/\arcsin(c/2)`$。

&emsp;[The Gaussian free field limit of the balanced six-vertex model with variance multiplier 1/arcsin(c/2)](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026.pdf)

**226. 双二聚体环系综收敛到 CLE₄。** 解决双二聚体标度极限猜想的半平面 Temperleyan 形式：Temperleyan 方格上两个独立二聚体覆盖形成的完整环系综收敛到嵌套 CLE₄。收敛把每个宏观环匹配为无参数曲线，把环可观测量的收敛升级为环本身的收敛。

&emsp;[The curve scaling limit of half-plane double dimers](https://github.com/openai/math/blob/main/preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/paper.pdf)

**227. 临界 SK 自相关过程与跨越温度转变的动力学。** 对每自旋速率一的零场高斯 SK 热浴动力学证明：固定 $`0\le\beta\lt 1`$ 时 $`\log n`$ 尺度上的最坏起点截断；<i>β</i> = 1 时混合时间 $`n^{2/3+o(1)}`$；<i>β</i> &gt; 1 时从 Gibbs 采样固定起点出发的拉伸指数混合（在对无序的概率下）。临界处，重标化的平稳与淬火自相关过程对高斯与 Rademacher 无序有普适随机极限；淬火极限松弛到平稳极限。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/227.md)）

&emsp;[Universality of critical quench autocorrelations in the Sherrington–Kirkpatrick model](https://github.com/openai/math/blob/main/preprints/Universality-of-critical-quench-autocorrelations-in-the-Sherrington-Kirkpatrick-model-October-5-2026/main.pdf)

&emsp;[Functional universality of critical SK autocorrelations](https://github.com/openai/math/blob/main/preprints/Functional-universality-of-critical-SK-autocorrelations-October-5-2026/critical-sk-autocorrelations.pdf)

&emsp;[A spectral gap throughout the high-temperature Sherrington–Kirkpatrick phase](https://github.com/openai/math/blob/main/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/main.pdf)

&emsp;[Cutoff throughout the high-temperature Sherrington–Kirkpatrick phase](https://github.com/openai/math/blob/main/preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/paper.pdf)

&emsp;[Critical slowing down in the Sherrington–Kirkpatrick model](https://github.com/openai/math/blob/main/preprints/Critical-slowing-down-in-the-Sherrington-Kirkpatrick-model-September-24-2026/paper.pdf)

&emsp;[Stretched-exponential barriers for typical SK initial states](https://github.com/openai/math/blob/main/preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/paper.pdf)

&emsp;[A typical-start upper bound for low-temperature SK Glauber dynamics](https://github.com/openai/math/blob/main/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/paper.pdf)

&emsp;[Critical mixing in the Sherrington–Kirkpatrick model](https://github.com/openai/math/blob/main/preprints/Critical-mixing-in-the-Sherrington-Kirkpatrick-model-September-25-2026/paper.pdf)

**228. 径向对势的连续相变。** 对三维经典粒子构造稳定的距离依赖对相互作用，具有一级相变：正则自由能在一个开密度区间内的某个逆温度处导数跳跃。一个势有发散排斥核；另一个有界连续、带可积幂律尾部，实现 Simon 连续问题所寻求的相变类型。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/228.md)）

&emsp;[A continuum temperature singularity for a radial pair potential](https://github.com/openai/math/blob/main/preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/paper.pdf)

&emsp;[A radial continuum phase transition with algebraic decay](https://github.com/openai/math/blob/main/preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/paper.pdf)

**229. 精确三态与四态重构阈值及四态树容量。** 对正则树（<i>d</i> ≥ 2）与观测泊松树（均值 <i>d</i> &gt; 1 与 <i>d</i> &gt; 0）上的三态对称与四态铁磁广播，证明精确重构阈值 $`d\lambda^2\gt 1`$（等号处不可重构），泊松优势在不以存活为条件下平均。三态定理允许 <i>λ</i> 的两个符号，并给出对称三社区随机块模型的精确弱恢复阈值。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/229.md)）

&emsp;[The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model](https://github.com/openai/math/blob/main/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf)

&emsp;[A Capacity Criterion for Four-State Potts Reconstruction on Trees](https://github.com/openai/math/blob/main/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf)

&emsp;[The exact reconstruction threshold for the three-state symmetric channel](https://github.com/openai/math/blob/main/preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/paper.pdf)

**230. SLE 的精确豪斯多夫规范。** 解决 Schramm 关于弦状 SLE<sub>κ</sub>（$`0\lt \kappa\lt 8`$）的豪斯多夫测度问题。显式规范 $`r^d(\log\log(1/r))^{(2-d)/2}`$（$`d=1+\kappa/8`$）对每段迹 $`\gamma([s,t])`$（$`0\lt s\lt t\lt \infty`$）几乎必然给出正有限测度，对每个有界圆盘中的迹给出有限期望测度。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/230.md)）

&emsp;[An exact Hausdorff gauge for SLE](https://github.com/openai/math/blob/main/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/An-exact-Hausdorff-gauge-for-SLE-September-25-2026.pdf)

&emsp;[An explicit exact Hausdorff gauge for SLE](https://github.com/openai/math/blob/main/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026.pdf)

**231. 自由均匀生成森林是 IID 的因子。** 在每个无限连通局部有限简单无权图上，自由均匀生成森林是独立顶点标记的因子（由一个无根的等变同构规则）。每个可数群上的平移不变强 Rayleigh 二值过程（包括带 Hermite 正压缩核的不变行列式过程）也是 IID 的因子。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/231.md)）

&emsp;[The free uniform spanning forest is a factor of IID](https://github.com/openai/math/blob/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026.pdf)

**232. 三角格 Lipschitz 高斯场与界面。** 证明三角格高度模型在有界光滑单连通域上的高斯自由场极限：增量 $`0,\pm2`$ 的均匀奇高度与边界值 $`\pm1`$ 的双弧情形，以及由固定 $`x\in[1/\sqrt2,1]`$ 加权的零边界整 Lipschitz 高度。均匀实 Lipschitz 高度也收敛到高斯场；在调好的对边界振幅处，其界面收敛到弦状 SLE₄，建立 Schramm 的实场/界面预测。

&emsp;[Gaussian free-field limits of weighted integer Lipschitz heights](https://github.com/openai/math/blob/main/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-September-25-2026/paper.pdf)

&emsp;[The Gaussian free field limit of integer Lipschitz heights with two-arc boundary data](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-September-25-2026/paper.pdf)

&emsp;[Uniform real Lipschitz surfaces on the triangular lattice](https://github.com/openai/math/blob/main/preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-September-25-2026/paper.pdf)

**233. Ashkin–Teller 临界线的联合电流极限。** 识别整个临界线（含四态 Potts 端点）上 Ashkin–Teller 高度与两个完整电流簇集合的联合标度极限。在有界 Jordan 域、容许格逼近与 wired 自由对偶边界下，高度收敛到预测的高斯自由场，簇收敛到同一场的典范递归集合，保留每个嵌套深度。

&emsp;[The joint scaling limit of critical Ashkin-Teller currents](https://github.com/openai/math/blob/main/preprints/The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-September-25-2026/main.pdf)

**234. 正交不变 Ising 自旋玻璃的全温度压强。** 对正交不变 Ising 自旋玻璃在每个固定温度的极限压强给出精确变分公式（几乎必然与期望同时成立）。耦合矩阵是确定谱（收敛到紧支撑律）的 Haar 随机旋转，极值特征值收敛到其支撑端点。零场基态能量作为温度趋于零的推论。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/234.md)）

&emsp;[All-temperature pressure for orthogonally invariant Ising spin glasses](https://github.com/openai/math/blob/main/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/paper.pdf)

**235. 极限随机 SAT 阈值、锐利方差与可计算性。** 对以带放回采样的独立均匀带号恰当子句构成的随机 <i>k</i>-SAT，证明每个固定 <i>k</i> ≥ 3 的有限正极限阈值与命中时间方差 $`\Theta_k(n)`$，以及 3-SAT 阈值的可计算性。我们确认 Gaia Carenini 在其同期公开的 ECCC TR26-229 中对阈值存在性猜想的优先解决（2026-10-05 公开）；本族提供另一证明以及更锐利的方差与可计算性结果。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/235.md)）

&emsp;[A Limiting Satisfiability Threshold for Every Fixed Clause Size](https://github.com/openai/math/blob/main/preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/article.pdf)

&emsp;[Linear Variance of the Random 3-SAT Hitting Time](https://github.com/openai/math/blob/main/preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/linear-variance-of-the-random-3-sat-hitting-time.pdf)

&emsp;[Variance of the Random k-SAT Hitting Time](https://github.com/openai/math/blob/main/preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/article.pdf)

&emsp;[Computing the Random 3-SAT Threshold](https://github.com/openai/math/blob/main/preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf)

**236. 树上自由 Ising 自旋的精确 IID 因子阈值。** 确定无穷 <i>d</i>-正则树上零场铁磁 Ising 自由态何时是独立顶点标记的因子：恰在 $`\tanh\beta\le(d-1)^{-1/2}`$（含等号，<i>d</i> ≥ 3、<i>β</i> ≥ 0）。构造无根，且对每个固定树自同构几乎必然等变，解决 Lyons 问题铁磁情形。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/236.md)）

&emsp;[The sharp factor-of-IID threshold for the free Ising model on regular trees](https://github.com/openai/math/blob/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/article.pdf)

**237. 蜂巢自回避行走的三分之四指数。** 证明 Nienhuis 预测的三分之四指数的直径形式：均匀选取的蜂巢格上 <i>n</i> 步自回避行走的直径为 $`n^{3/4+o(1)}`$。其局部质量与覆盖数指数为 4/3。这些估计在所有足够大的固定长度、跨尺度同时成立，且以任意高的多项式概率成立。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/237.md)）

&emsp;[Radial transfer estimates and polygon length laws for honeycomb walks](https://github.com/openai/math/blob/main/preprints/Radial-transfer-estimates-and-polygon-length-laws-for-honeycomb-walks-September-26-2026/main.pdf)

&emsp;[Critical honeycomb chords with prescribed boundary endpoints](https://github.com/openai/math/blob/main/preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/main.pdf)

&emsp;[Cylinder loop weights and planar nesting](https://github.com/openai/math/blob/main/preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/main.pdf)

&emsp;[Mass and covering exponents for fixed-length honeycomb walks](https://github.com/openai/math/blob/main/preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026/main.pdf)

&emsp;[Signed cylinder propagation and marked polygons on the honeycomb lattice](https://github.com/openai/math/blob/main/preprints/Signed-cylinder-propagation-and-marked-polygons-on-the-honeycomb-lattice-September-26-2026/main.pdf)

&emsp;[Cylinder amplitudes and logarithmic bridge-length windows on the honeycomb lattice](https://github.com/openai/math/blob/main/preprints/Cylinder-amplitudes-and-logarithmic-bridge-length-windows-on-the-honeycomb-lattice-September-26-2026/main.pdf)

&emsp;[Marked polygon correlations and one-arc bounds](https://github.com/openai/math/blob/main/preprints/Marked-polygon-correlations-and-one-arc-bounds-September-26-2026/main.pdf)

&emsp;[Disk transfer representations and confined bridge mass](https://github.com/openai/math/blob/main/preprints/Disk-transfer-representations-and-confined-bridge-mass-September-26-2026/main.pdf)

&emsp;[Polynomial vacuum representations and bridge mass for honeycomb walks](https://github.com/openai/math/blob/main/preprints/Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026/main.pdf)

&emsp;[Renewal and changes of law for critical honeycomb walks](https://github.com/openai/math/blob/main/preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/main.pdf)

&emsp;[Critical strip-crossing mass on the honeycomb lattice](https://github.com/openai/math/blob/main/preprints/Critical-strip-crossing-mass-on-the-honeycomb-lattice-September-26-2026/main.pdf)

&emsp;[Uniform marked-polygon estimates and sharp finite bridge moments](https://github.com/openai/math/blob/main/preprints/Uniform-marked-polygon-estimates-and-sharp-finite-bridge-moments-September-26-2026/main.pdf)

&emsp;[Cap-selected amplitudes and triangle chords for honeycomb walks](https://github.com/openai/math/blob/main/preprints/Cap-selected-amplitudes-and-triangle-chords-for-honeycomb-walks-September-26-2026/main.pdf)

**238. Thorp 洗牌的最优对数混合。** 证明 Thorp 洗牌在 $`\Theta(\log N)`$ 次物理洗牌内随机化 $`N=2^d`$ 张带标牌，确定其两幂牌数下的最优混合阶。收敛按全变差从最坏初始序计，针对整个排列而不仅是单个牌位。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/238.md)）

&emsp;[Optimal-order mixing of the Thorp shuffle](https://github.com/openai/math/blob/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/paper.pdf)

&emsp;[Random coordinate frames and partial permutation laws](https://github.com/openai/math/blob/main/preprints/Random-coordinate-frames-and-partial-permutation-laws-September-26-2026/main.pdf)

&emsp;[From partial permutation information to Fourier bounds](https://github.com/openai/math/blob/main/preprints/From-partial-permutation-information-to-Fourier-bounds-September-26-2026/main.pdf)

&emsp;[Conditional information under deterministic coordinate sweeps](https://github.com/openai/math/blob/main/preprints/Conditional-information-under-deterministic-coordinate-sweeps-September-26-2026/main.pdf)

&emsp;[Conditional permutations in a revealed switching environment](https://github.com/openai/math/blob/main/preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/paper.pdf)

&emsp;[Routing densities and representation contraction for Thorp sweeps](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/paper.pdf)

&emsp;[Row&#8211;column symmetry and contraction of coordinate sweeps](https://github.com/openai/math/blob/main/preprints/Row-column-symmetry-and-contraction-of-coordinate-sweeps-September-26-2026/paper.pdf)

&emsp;[Random-subspace tests and trace smoothing for coordinate sweeps](https://github.com/openai/math/blob/main/preprints/Random-subspace-tests-and-trace-smoothing-for-coordinate-sweeps-September-26-2026/paper.pdf)

&emsp;[Compatibility entropy and the spectrum of a Thorp sweep](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/paper.pdf)

&emsp;[Signed tensor densities and diagram budgets for the Thorp shuffle](https://github.com/openai/math/blob/main/preprints/Signed-tensor-densities-and-diagram-budgets-for-coordinate-sweeps-September-26-2026/paper.pdf)

&emsp;[Conditional coordinate sweeps and analytic transfer](https://github.com/openai/math/blob/main/preprints/Conditional-coordinate-sweeps-and-analytic-transfer-September-26-2026/main.pdf)

&emsp;[A strict four-row permanent inequality and permutation moments](https://github.com/openai/math/blob/main/preprints/A-strict-four-row-permanent-inequality-and-permutation-moments-September-26-2026/main.pdf)

**239. 对称随机符号矩阵的锐利奇异性速率。** 确定对角及以上独立同分布的对称随机符号矩阵的锐利指数奇异性速率。均匀符号给出 $`\Pr(\det A_n=0)=(1/2+o(1))^n`$；固定偏差 $`p\in(0,1)\setminus\{1/2\}`$ 时速率为 $`(p^2+(1-p)^2+o(1))^n`$。有偏情形下，相同行达到该速率。

&emsp;[The sharp exponential rate of singularity for symmetric Bernoulli matrices](https://github.com/openai/math/blob/main/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/symmetric-bernoulli-singularity.pdf)

&emsp;[The sharp singularity rate for biased symmetric sign matrices](https://github.com/openai/math/blob/main/preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/biased-symmetric-sign-singularity.pdf)

---

## 10. 数理逻辑（Mathematical logic，6 个族）

**240. Shelah 最终范畴性与指定阈值障碍。** 在 ZFC 中证明 Shelah 最终范畴性猜想：对每个 Löwenheim–Skolem 数的界，存在一致阈值，使抽象初等类在阈值之上一个基数处的范畴性蕴含同一尾部的所有基数处的范畴性。范畴性指给定基数下同构意义唯一。在连续统假设下，某个提出的特定 Hanf 阈值不必充分。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/240.md)）

&emsp;[A CH obstruction to a prescribed categoricity threshold](https://github.com/openai/math/blob/main/preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/paper.pdf)

&emsp;[Eventual categoricity for abstract elementary classes](https://github.com/openai/math/blob/main/preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/paper.pdf)

**241. Turing 度的刚性。** 图灵度的每个序自同构都是恒等，解决其刚性问题。即不存在保持相对可计算序的非平凡重标记。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/241.md)）

&emsp;[Rigidity of the Turing degrees](https://github.com/openai/math/blob/main/preprints/Rigidity-of-the-Turing-degrees-September-24-2026/paper.pdf)

**242. 单折丢番图表示与至多一解承诺下的不可判定性。** 自然数元组的每个递归可枚举集都有这样的丢番图表示：对每个成员恰有一个辅助解，对非成员没有。这证明单折猜想，从而证明有限折猜想。即使在至多一解承诺下，非负整数上的丢番图可解性仍不可判定。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/242.md)）

&emsp;[Single-fold Diophantine representations](https://github.com/openai/math/blob/main/preprints/Single-fold-Diophantine-representations-September-24-2026/paper.pdf)

**243. 无选择计数与多项式时间及见证选择的分离。** 确证 Blass–Gurevich–Shelah 非捕捉猜想：𝔽₃ 上线性方程组的一致性定义了无序有限结构上的多项式时间查询，带计数的无选择多项式时间无法表达。另一结果表明加入见证对称选择严格增加表达能力。两个分离都对完整计数形式化成立，允许任意有限秩的遗传有限集。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/243.md)）

&emsp;[Choiceless polynomial time with counting does not capture polynomial time](https://github.com/openai/math/blob/main/preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/paper.pdf)

&emsp;[Witnessed symmetric choice is strictly stronger than choiceless polynomial time with counting](https://github.com/openai/math/blob/main/preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/paper.pdf)

**244. 分拆原理不蕴含选择。** 假设 ZF 一致，构造一个模型：其中每个集合的满射像都可内射到该集合自身，而选择公理失效。序数索引族的选择仍成立。从 ZFC 的任何可数传递模型出发，独立构造给出具有这些性质、且不含基模型元素的新可数序列的传递对称扩张。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/244.md)）

&emsp;[The Partition Principle does not imply Choice](https://github.com/openai/math/blob/main/preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/partition-principle-without-choice.pdf)

**245. 纯型系统中弱规范化蕴含强规范化。** 对每个纯型系统证明弱规范化蕴含强规范化：若每个合法上下文中的合法表达式都有 <i>β</i>-范式，则每个 <i>β</i>-约化序列终止。这解决 <i>β</i>-Barendregt–Geuvers–Klop 猜想，包括非函数规则与开上下文。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/245.md)）

&emsp;[Weak and strong normalization in pure type systems](https://github.com/openai/math/blob/main/preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/paper.pdf)

---

## 11. 群论（Group theory，14 个族）

**246. Cannon 猜想。** 每个边界同胚于 <i>S</i>² 的词双曲群都容许核对数有限、在双曲三维空间上正常余紧的等距作用，证明 Cannon 猜想。每个无挠的此类群因此是闭双曲三维流形的基本群。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/246.md)）

&emsp;[A Modulus Proof of Cannon’s Conjecture](https://github.com/openai/math/blob/main/preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/paper.pdf)

**247. 无穷有限表现剩余有限 2-群与有限表现幂零代数。** 构造无穷有限表现剩余有限群，其所有元素都有有限 2-幂阶，即使在此类中否定回答有限表现 Burnside 问题。构造还给出无穷维有限表现幂零结合 𝔽₂ 代数与有限表现无穷维代数么单位化，对相应的幂零与 Kurosh 有限性问题给出否定答案。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/247.md)）

&emsp;[An infinite finitely presented residually finite 2-group](https://github.com/openai/math/blob/main/preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/residually-finite-torsion.pdf)

&emsp;[An infinite finitely presented periodic group](https://github.com/openai/math/blob/main/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/paper.pdf)

**248. Thompson 群 F 非顺从。** 证明 Thompson 群 <i>F</i>（区间上二进制分段线性同胚群）非顺从，解决其长期的顺从性问题。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/248.md)）

&emsp;[Thompson's group F is nonamenable](https://github.com/openai/math/blob/main/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf)

**249. 有限生成的 Eilenberg–Ganea 反例。** 构造有限生成剩余有限群：整上同调维数 2、几何维数 3，否定 Eilenberg–Ganea 猜想。它没有二维分类空间，即使允许无穷多胞腔。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/249.md)）

&emsp;[A finitely generated counterexample to the Eilenberg–Ganea conjecture](https://github.com/openai/math/blob/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026/paper.pdf)

**250. 带更高有限性的 Boone–Higman 嵌入。** 有限生成群有可判定字问题当且仅当它嵌入某个有限表现单群，证明 Boone–Higman 猜想。靶群可取 <i>F</i><sub>∞</sub> 型：每维数有限多个胞腔的分类空间。单个 <i>F</i><sub>∞</sub> 型群还可包含每个有限表现群。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/250.md)）

&emsp;[Finite algebraic envelopes and the Boone–Higman conjecture](https://github.com/openai/math/blob/main/preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf)

&emsp;[Simple F∞ overgroups of groups with decidable word problem](https://github.com/openai/math/blob/main/preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/paper.pdf)

&emsp;[A universal group of type F∞](https://github.com/openai/math/blob/main/preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf)

**251. 顺从性、可西化性与强 Ulam 稳定性。** 对所有离散群解决 Dixmier 问题：顺从性等价于每个一致有界希尔伯特空间表示都相似于一个酉表示。对可数离散群，顺从性还等价于强 Ulam 稳定性：足够精确的酉近似表示在算子范数下一致接近同一（可能无穷维）希尔伯特空间上的真表示。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/251.md)）

&emsp;[Unitarizability implies amenability for discrete groups](https://github.com/openai/math/blob/main/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf)

&emsp;[Strong Ulam Stability Characterizes Amenability](https://github.com/openai/math/blob/main/preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/strong-ulam-stability.pdf)

**252. 非剩余有限且在任何域上非线性的无挠双曲群。** 构造非剩余有限的无挠词双曲群，否定回答剩余有限性问题。一个固定的非单位元被每个交换域上的每个有限维线性表示杀死，故该群在任何此类域上非线性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/252.md)）

&emsp;[A torsion-free hyperbolic group that is not residually finite](https://github.com/openai/math/blob/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/paper.pdf)

**253. 无穷有限表现单顺从群。** 构造无穷有限表现单顺从群，回答这些性质能否同时出现的长期问题。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/253.md)）

&emsp;[An infinite finitely presented simple amenable group](https://github.com/openai/math/blob/main/preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/paper.pdf)

**254. Artin 群的分类空间与几何障碍。** 每个有限秩 Artin 群的 Salvetti 复形非球面，证明 Artin $`K(\pi,1)`$ 猜想。其抛物子群的任意交仍是抛物的，证明抛物交猜想。一个显式 Artin 群不容许在任何非空真 CAT(0) 空间上正常余紧等距作用。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/254.md)）

&emsp;[Harmonic heights and the Artin K(pi,1) conjecture](https://github.com/openai/math/blob/main/preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/paper.pdf)

&emsp;[An Artin group with no geometric CAT(0) action](https://github.com/openai/math/blob/main/preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/paper.pdf)

&emsp;[Parabolic intersections in Artin groups](https://github.com/openai/math/blob/main/preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/paper.pdf)

**255. 几乎多循环群的拟等距识别。** 证明每个拟等距于有限生成几乎多循环群的有限生成群本身几乎多循环，解决 Eskin–Fisher–Whyte 格识别猜想。等价地，拟等距于连通单连通可解李群中格的群，几乎等于某个此类李群（可能不同）中的一致格。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/255.md)）

&emsp;[Quasi-isometric recognition of virtually polycyclic groups](https://github.com/openai/math/blob/main/preprints/quasi-isometric-recognition-of-virtually-polycyclic-groups-September-24-2026/paper.pdf)

**256. 任意群上方程组的非奇异性。** 证明任意群上指数和矩阵在 ℚ 上满行秩的每个有限方程组都在扩群中有联立解，解决 Howie 猜想。系数群嵌入所给商群。配套结果证明 Kervaire 猜想：添加一个生成元与一个关系不能平凡化非平凡群。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/256.md)）

&emsp;[Nonsingular systems of equations over arbitrary groups](https://github.com/openai/math/blob/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf)

&emsp;[The Kervaire theorem for groups](https://github.com/openai/math/blob/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026/The-Kervaire-Theorem-for-Groups-September-24-2026.pdf)

**257. 无几何 CAT(0) 作用的双曲群。** 否定回答「每个词双曲群都是 CAT(0) 群」。构造一个有有限分类空间、但不容许在任何真完备 CAT(0) 空间（任何维数）上正常余紧等距作用的双曲群。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/257.md)）

&emsp;[A hyperbolic group with no geometric CAT(0) action](https://github.com/openai/math/blob/main/preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf)

**258. Gersten 猜想与单关系群的虚紧特殊化。** 证明 Gersten 猜想：每个不含 Baumslag–Solitar 子群 $`\mathrm{BS}(m,n)`$（$`m,n\ne0`$）的有限生成单关系群是词双曲的。还证明每个词双曲单关系群虚紧特殊。

&emsp;[Baumslag-Solitar-free one-relator groups are hyperbolic](https://github.com/openai/math/blob/main/preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/paper.pdf)

&emsp;[Virtual compact specialness of hyperbolic one-relator groups](https://github.com/openai/math/blob/main/preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/paper.pdf)

**259. 无固定价格的群。** 构造有限生成群，其两个本质自由概率测度保持作用的 cost 不同，否定回答一般固定价格问题。其 Bernoulli 作用的 cost 有界离开 1，而一列有限高扩张的 cost 趋于 1。

&emsp;[A group without fixed price](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/unequal-costs-rank-100-amalgam.pdf)

---

## 12. 数学物理（Mathematical physics，25 个族）

**260. 时空 Penrose 不等式：包围面积、电荷、旋转与反德西特扩展。** 在主导能量、弱未来俘获、正包围面积与所述衰减假设下，对每个空间维数 <i>n</i> ≥ 3 的光滑单端渐近平坦初值，证明锐利包围面积时空 Penrose 不等式：以最小包围面积自下界定不变 ADM 质量，在附加视界假设下有等号刚性。带电上面积界处理双层三维数据；高维纯电扩展使用匹配的中性定理。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/260.md)）

&emsp;[The spacetime Penrose inequality with charge and original-data rigidity](https://github.com/openai/math/blob/main/preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/paper.pdf)

&emsp;[A Charged Reduction of the Spacetime Penrose Inequality in Spatial Dimensions at Least Four](https://github.com/openai/math/blob/main/preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/paper.pdf)

&emsp;[Spacetime Penrose inequalities: enclosing area, charge, and rigidity](https://github.com/openai/math/blob/main/preprints/Spacetime-Penrose-inequalities-enclosing-area-charge-and-rigidity-October-5-2026/paper.pdf)

&emsp;[The Kerr–Newman Penrose Inequality for Axisymmetric Electrovacuum Exteriors](https://github.com/openai/math/blob/main/preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/paper.pdf)

&emsp;[Electromagnetic tails and the Kerr–Newman Penrose inequality](https://github.com/openai/math/blob/main/preprints/Electromagnetic-tails-and-the-Kerr-Newman-Penrose-inequality-October-5-2026/paper.pdf)

&emsp;[The nonmaximal anti-de Sitter Penrose Inequality and original-data rigidity](https://github.com/openai/math/blob/main/preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/paper.pdf)

&emsp;[The Penrose inequality for maximal asymptotically hyperbolic initial data](https://github.com/openai/math/blob/main/preprints/The-Penrose-inequality-for-maximal-asymptotically-hyperbolic-initial-data-October-5-2026/paper.pdf)

&emsp;[A local Penrose inequality for conformal perturbations of Schwarzschild–anti-de Sitter data](https://github.com/openai/math/blob/main/preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/paper.pdf)

&emsp;[The spacetime Penrose inequality and enclosing area](https://github.com/openai/math/blob/main/preprints/The-spacetime-Penrose-inequality-and-enclosing-area-September-27-2026/paper.pdf)

&emsp;[Conformal flow and the Riemannian Penrose inequality with minimizing frontiers](https://github.com/openai/math/blob/main/preprints/Conformal-flow-and-the-Riemannian-Penrose-inequality-with-minimizing-frontiers-September-27-2026/paper.pdf)

&emsp;[Equality and rigidity in the spacetime Penrose inequality](https://github.com/openai/math/blob/main/preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf)

&emsp;[Boundary graph deformations for the spacetime Penrose inequality](https://github.com/openai/math/blob/main/preprints/Boundary-graph-deformations-for-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf)

&emsp;[Area-controlled end replacement and the Bondi Penrose inequality in the CKS class](https://github.com/openai/math/blob/main/preprints/Area-controlled-end-replacement-and-the-Bondi-Penrose-inequality-in-the-CKS-class-September-27-2026/paper.pdf)

**261. Anderson 模型中的局域化与退局域化。** 解决具有独立均匀点位势的格点 Anderson 模型的预测谱对比：二维中每个正无序强度都几乎必然给出纯点谱；每个固定维数 <i>d</i> ≥ 3 中足够弱的正无序在固定开区间上给出纯绝对连续谱，且谱重非零。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/261.md)）

&emsp;[Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three](https://github.com/openai/math/blob/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf)

&emsp;[Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder](https://github.com/openai/math/blob/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf)

**262. 锐利有限矩阵 Lieb–Thirring 不等式与所有等号情形。** 对 $`1/2\lt \gamma\lt 3/2`$ 与任意满足 $`\int\mathrm{tr}(W^{\gamma+1/2})\lt\infty`$ 的有限矩阵势 $`W\ge0`$，证明一维 Lieb–Thirring 不等式的锐利形式：最优常数是标量单束缚态值，与矩阵规模无关。所有等号情形都是常值酉基下标量 sech² 孤子的直和（独立尺度与中心）与零通道。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/262.md)）

&emsp;[Equality cases in the sharp one-dimensional matrix Lieb–Thirring inequality](https://github.com/openai/math/blob/main/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf)

&emsp;[Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials](https://github.com/openai/math/blob/main/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/sharp-matrix-lieb-thirring.pdf)

&emsp;[Sharp one-dimensional Lieb–Thirring constants](https://github.com/openai/math/blob/main/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf)

**263. 电离与广义电离猜想。** 对带两个电子自旋态的完整非相对论库仑模型，证明：核数 <i>M</i>、核电荷至少 1、总电荷 <i>Z</i> 的分子至多严格束缚 $`Z+CM`$ 个电子。中性原子第一电离能与包含除期望半个电子以外全部电子的半径有普适正上下界。移除 <i>m</i> 个电子的能量代价在 $`m\to\infty`$、$`Z/m\to\infty`$ 时有 Thomas–Fermi 渐近；中性原子外半径有相应的迭代极限渐近（先取 $`Z\to\infty`$）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/263.md)）

&emsp;[Uniform excess charge for Coulomb molecules and the outer radius of neutral atoms](https://github.com/openai/math/blob/main/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf)

&emsp;[Generalized ionization energies for full Coulomb atoms](https://github.com/openai/math/blob/main/preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/paper.pdf)

&emsp;[Generalized outer-electron radii of neutral Coulomb atoms](https://github.com/openai/math/blob/main/preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/paper.pdf)

**264. 双端 Kerr 数据附近的强宇宙监督。** 证明在每个固定旋转亚极端 Kerr 桥附近的局部强宇宙监督：光滑完整双端渐近平坦真空数据的加权光滑邻域的稠密 $`G_\delta`$ 子集，其极大整体双曲发展没有未来连续非退化延拓（弱连接局部平方可积）。不施加对称性；延拓不必满足真空方程。

&emsp;[Generic Future Inextendibility with Square-Integrable Connection Near a Fixed Kerr Spacetime](https://github.com/openai/math/blob/main/preprints/Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026/paper.pdf)

&emsp;[Generic C1 Future Inextendibility Near Rotating Subextremal Kerr Spacetimes](https://github.com/openai/math/blob/main/preprints/Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026/paper.pdf)

&emsp;[Quantitative Near-Kerr Evolution and Generic C2 Future Inextendibility](https://github.com/openai/math/blob/main/preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/paper.pdf)

**265. 二维有隙系统的面积律与张量网络。** 只用一致的全系统谱隙与局部相互作用界，证明任意有限诱导方格域上有限程哈密顿量唯一基态的熵面积律。在开放 $`L\times L`$ 方块上，一致有隙最近邻基态还容许投影纠缠对态近似：键维数多项式、全局向量误差至多 <i>L</i>^(−1)。

&emsp;[A two-dimensional area law from a global spectral gap](https://github.com/openai/math/blob/main/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf)

&emsp;[Polynomial PEPS approximation of gapped square-grid ground states](https://github.com/openai/math/blob/main/preprints/Polynomial-PEPS-approximation-of-gapped-square-grid-ground-states-September-24-2026/paper.pdf)

**266. 六维恰好三个互不偏基。** 证明 $`N(6)=3`$，解决 Zauner 六维互不偏基猜想：ℂ⁶ 中存在三个这样的基，但不能有四个。排除是所述 binary64 算术与编译器条件下的完整认证计算。独立配套结果对六阶复 Hadamard 矩阵（Tao 三次等价类之外）证明 Matolcsi–Ruzsa–Weiner 傅里叶消失猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/266.md)）

&emsp;[The maximum number of mutually unbiased bases in dimension six](https://github.com/openai/math/blob/main/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf)

&emsp;[Exact Fourier certificates for complex Hadamard matrices of order six](https://github.com/openai/math/blob/main/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf)

**267. 正温度玻色–爱因斯坦凝聚与精确量子耗尽。** 证明三维硬球气体精确正则 Gibbs 态的玻色–爱因斯坦凝聚：每个固定排除距离与足够小的固定密度都容许严格正温度（与体积无关），热力学极限下凝聚分数为正。零温度下，对硬球与固定有界非负径向有限程、散射长度为正的势，证明 Bogoliubov 首项量子耗尽律（先取热力学极限再取稀薄极限）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/267.md)）

&emsp;[Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/positive-temperature-hard-spheres.pdf)

&emsp;[Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas](https://github.com/openai/math/blob/main/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/Quantum-Depletion-in-the-Dilute-Hard-Sphere-Bose-Gas.pdf)

&emsp;[Quantum Depletion for Fixed Bounded Repulsive Potentials](https://github.com/openai/math/blob/main/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/fixed-repulsion-quantum-depletion.pdf)

&emsp;[A density-uniform condensate bound for dilute Bose gases](https://github.com/openai/math/blob/main/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf)

&emsp;[Ground-state condensation in the dilute hard-sphere gas](https://github.com/openai/math/blob/main/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf)

**268. 自旋一 Haldane 隙。** 对偶周期环上的纯反铁磁 Heisenberg 链证明自旋一 Haldane 隙猜想：链增长时谱隙保持一致正。配套结果对带端点场 $`h=3/5`$ 的奇数开链建立间隙，并给出拓扑指标 −1 的边界选择无穷体积态。

&emsp;[The periodic spin-one Haldane gap](https://github.com/openai/math/blob/main/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf)

&emsp;[A boundary-field gap for the spin-one Heisenberg chain](https://github.com/openai/math/blob/main/preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/paper.pdf)

**269. 一致 Laughlin 隙与有界标量无序下的稳定性。** 对填充 1/3 的圆球面上完整 <i>V</i>₁ 相互作用证明费米子 Laughlin 谱隙猜想。唯一基态在投影到最低朗道能级的足够弱有界实标量一体势下保持一致有隙。隙与无序阈值对所有足够大粒子数与所有归一化势轮廓一致。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/269.md)）

&emsp;[Uniform Stability of the Spherical Laughlin Gap](https://github.com/openai/math/blob/main/preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/uniform-stability-spherical-laughlin-gap.pdf)

&emsp;[A Fock-space inequality and the Laughlin spectral gap](https://github.com/openai/math/blob/main/preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf)

**270. BFSS 矩阵模型的阈值与正能量束缚态。** 证明未变形相对 $`\mathrm{SU}(N)`$ BFSS 模型对每个有限 <i>N</i> ≥ 2 恰有一个可归一化零能量态，解决阈值束缚态猜想。对 $`\mathrm{SU}(2)`$，配套结果证明有无穷多个可归一化正能量本征态（能量无界），与原始 BFSS 论文在 <i>N</i> = 2 时排除额外束缚态相矛盾。

&emsp;[The unique threshold bound state of the SU(N) BFSS model](https://github.com/openai/math/blob/main/preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/paper.pdf)

&emsp;[Positive eigenvalues of the relative SU(2) BFSS Hamiltonian](https://github.com/openai/math/blob/main/preprints/Positive-eigenvalues-of-the-relative-SU-2-BFSS-Hamiltonian-October-5-2026/positive-eigenvalues-relative-su2-bfss.pdf)

**271. Bloch 律、其格修正与球面磁化律。** 对每个正量子自旋的三维量子 Heisenberg 铁磁体（允许支撑生成 ℤ³ 的非负对称有限程耦合），证明带精确系数的 Bloch $`T^{3/2}`$ 律。热力学极限先于零场导数与低温极限。该族还对每个维数 <i>d</i> ≥ 3 的最近邻模型证明自发磁化，并确定三维最近邻耦合的一阶格修正。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/271.md)）

&emsp;[Bloch's Law for Finite-Range Heisenberg Ferromagnets in Three Dimensions](https://github.com/openai/math/blob/main/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/bloch-law-heisenberg.pdf)

&emsp;[The first lattice correction to Bloch's law](https://github.com/openai/math/blob/main/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/first-lattice-correction-bloch-law.pdf)

&emsp;[The spherical magnetization law for the three-dimensional quantum Heisenberg ferromagnet](https://github.com/openai/math/blob/main/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf)

&emsp;[Spontaneous magnetization in the quantum Heisenberg ferromagnet](https://github.com/openai/math/blob/main/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf)

**272. 无可蒸馏密钥的纠缠。** 构造 $`\mathbb C^{10}\otimes\mathbb C^{10}`$ 上的纠缠态：对所述几乎必然完成的局域仪器协议，其可蒸馏密钥为零。这些协议允许联合局域处理与认证的双向公开通信，无其他共享私有资源，窃听者持有输入纯化与公开记录。$`M_{21}(\mathbb C)`$ 上平方非纠缠破坏的保迹 PPT 信道否定 Christandl 的 PPT-平方猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/272.md)）

&emsp;[Entanglement with zero distillable secret key in local dimension ten](https://github.com/openai/math/blob/main/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf)

**273. 熵光子数不等式。** 对任意有限模数中两个独立有限能玻色输入的分束器混合，证明熵光子数不等式：输出的熵光子数至少是输入的透射率加权平均。允许每个输入内的任意纠缠；乘积热输入即使熵不同也达到等号。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/273.md)）

&emsp;[The entropy photon-number inequality](https://github.com/openai/math/blob/main/preprints/The-entropy-photon-number-inequality-September-24-2026/paper.pdf)

**274. 奇偶不在 QAC⁰ 中。** 在测量输出模型中解决 Moore 奇偶性猜想：带任意单比特门、无界扇入 Toffoli 门与多项式总量子比特的常数深度量子电路，不能以任何固定正的最坏情形优势计算奇偶性。辅助比特初始为 0，测量一个输出量子比特，其余寄存器可弃置。Xu–Li 的归约给出严格多数的相同有界错误障碍。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/274.md)）

&emsp;[Product-projection localization and the QAC0 parity lower bound](https://github.com/openai/math/blob/main/preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/paper.pdf)

&emsp;[Regular trajectories, pruning and quantum parity](https://github.com/openai/math/blob/main/preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/paper.pdf)

**275. 连续库仑能量的 QMA 难度。** 证明三维电子库仑能量下确界近似（在整个自旋费米子连续空间上极小化）是 QMA 难的。确定性多项式时间归约即使只用位于不同有理位置的单位电荷核、多项式多个电子与至少为 1 的能量阈值间隔也成立。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/275.md)）

&emsp;[Continuum Coulomb hardness with binary nuclear charges](https://github.com/openai/math/blob/main/preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf)

&emsp;[QMA-hardness of continuum Coulomb energy with unit nuclear charges](https://github.com/openai/math/blob/main/preprints/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026.pdf)

**276. 广义振幅阻尼的经典容量。** 确定每个量子比特广义振幅阻尼信道（含全部阻尼与热参数）的无辅助经典容量。显式单变量优化给出容量，由带集体解码的独立二态信号系综达到。与任何有限维量子信道作张量积时，Holevo 容量、最小输出熵与正则化经典容量可加。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/276.md)）

&emsp;[Classical capacity and entropy inequalities for generalized amplitude damping](https://github.com/openai/math/blob/main/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf)

**277. 纠缠博弈的阈值重复。** 对每个有限双人单轮博弈证明指数阈值重复：若其纠缠值为 <i>v</i> &lt; 1，则 <i>k</i> 次独立重复中获胜比例至少 $`v+\delta`$ 的概率关于 <i>k</i> 指数衰减（$`0\lt \delta\lt 1-v`$）。允许任意联合有限维纠缠策略与相关的问题分布。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/277.md)）

&emsp;[Threshold parallel repetition for finite-dimensional entangled games](https://github.com/openai/math/blob/main/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/paper.pdf)

**278. Kohn–Sham 系综表示的失效。** 构造三电子库仑分子（两个相等正整电荷核），其绝对基态密度在 $`L^{3/2}(\mathbb R^3)+L^\infty(\mathbb R^3)`$ 中没有任何单个实自旋无关局域势的非相互作用基态系综表示。这否定该势类的 Kohn–Sham 系综可表示性；所需核电荷以非数值方式指定。

&emsp;[A Coulomb ground-state density without Kohn-Sham ensemble representation](https://github.com/openai/math/blob/main/preprints/A-Coulomb-Ground-State-Density-without-Kohn-Sham-Ensemble-Representation-September-25-2026/paper.pdf)

**279. 固定有限门集上的精确量子因子分解。** 给出多项式时间一致量子电路族：概率 1 输出每个整数的完整素因子分解。门数与量子比特数都在输入长度上多项式，且单个固定有限门集即可。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/279.md)）

&emsp;[Exact quantum factoring over a fixed finite gate set](https://github.com/openai/math/blob/main/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026/main.pdf)

**280. 酉顶点算子代数与共形网。** 证明强局域性猜想的强有理情形：每个单强有理复顶点算子代数生成完全有理共形网。其单模可酉化，其表示范畴作为辫化酉张量范畴与网的有限指标扇区一致。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/280.md)）

&emsp;[Strongly rational unitary vertex operator algebras and conformal nets](https://github.com/openai/math/blob/main/preprints/Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026/paper.pdf)

**281. QAOA 在热力学优先极限下达到 SK 最优。** 证明当系统规模先于电路深度趋于无穷时，QAOA 逼近高斯零场 Sherrington–Kirkpatrick 模型的基态能量。对每个精度，有限深度与独立于规模及无序的确定性角度达到所需的每自旋极限期望能量。这还给出大度随机正则图上首阶最优期望 MaxCut 值（规模先于度趋于无穷）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/281.md)）

&emsp;[QAOA attains the SK ground-state energy in the thermodynamic-first limit](https://github.com/openai/math/blob/main/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026.pdf)

&emsp;[Full support of the zero-temperature Sherrington-Kirkpatrick order parameter](https://github.com/openai/math/blob/main/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/main.pdf)

**282. 四维 QFT 中从标度对称到局部共形对称。** 在所述有界局域网与场重构假设下，对具有离散有下界有限重数标度谱、有限标度支撑与物理局域标度电流的四维酉正能量理论，证明标度对称蕴含局部共形对称。应力张量有迹无痕改进而时空电荷不变。结论针对局域 Ward 恒等式，而非整个网上的全局共形作用。

&emsp;[Scale and conformal symmetry in four-dimensional operational quantum field theory](https://github.com/openai/math/blob/main/preprints/Scale-and-conformal-symmetry-in-four-dimensional-operational-quantum-field-theory-September-26-2026/main.pdf)

**283. 从布尔神谕出发的多项式时间酉合成。** 解决常数错误 Aaronson–Kuperberg 酉合成问题：选定合适的布尔神谕后，一致多项式规模量子神谕电路在 diamond 范数误差 1/2 内逼近每个 <i>n</i>-量子比特酉信道。门、量子比特、神谕调用与查询长度都多项式有界。依赖目标的神谕可有无限制真值表；不断言其高效经典构造。

&emsp;[Polynomial-Time Unitary Synthesis from a Boolean Oracle](https://github.com/openai/math/blob/main/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/paper.pdf)

**284. 随机化与量子查询之间的最优四分之三次幂分离。** 证明全布尔函数的普适界 $`R(f)=O((1+Q(f))^4)`$ 的指数是锐利的，排除所有更小的幂并否定猜测的三次关系。<i>R</i> 与 <i>Q</i> 是错误至多 1/3 的随机化与量子最坏情形比特查询复杂度；查询之间的计算无限制。

&emsp;[A Nearly Quartic Separation Between Randomized and Quantum Query Complexity](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf)

---

## 13. 算子代数（Operator algebras，19 个族）

**285. Baum–Connes 与 Kadison–Kaplansky 的反例。** 经由有理单射性失效与装配映射满射性的独立失效，否定无系数约化 Baum–Connes 猜想。有限生成无挠例子见证单射性失效。另外，一个无挠群在其约化群 C*-代数中有非平凡投影，否定 Kadison–Kaplansky 猜想。

&emsp;[A torsion-free counterexample to reduced Baum–Connes injectivity](https://github.com/openai/math/blob/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/paper.pdf)

&emsp;[A torsion-free counterexample to the Kadison–Kaplansky projection conjecture](https://github.com/openai/math/blob/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf)

&emsp;[An irrational-trace counterexample to reduced Baum–Connes](https://github.com/openai/math/blob/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/paper.pdf)

**286. 格 von Neumann 代数的刚性与算术。** 分类特征零局部域上与性质 (T) 格可公度的 ICC 群的标量扭转群因子、与任意 ICC 群因子之间的有限指标双模。每个这样的双模都是来自有限指标子群同构与有限维射影表示的模型之有限和的直加项。分类还在所述稳定等价下恢复群、标量上循环与放大尺度。

&emsp;[Arithmeticity of twisted finite correspondences for lattices over local fields](https://github.com/openai/math/blob/main/preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/paper.pdf)

&emsp;[The arithmetic category and stable recovery of lattice factors](https://github.com/openai/math/blob/main/preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/paper.pdf)

**287. 自由群因子的同构。** 解决自由群因子同构问题：$`L(\mathbb F_2)\cong L(\mathbb F_3)`$，从而所有插值自由群因子（包括 $`L(\mathbb F_\infty)`$）彼此同构。它们共同的因子基本群为 $`\mathbb R_{\gt 0}`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/287.md)）

&emsp;[An isomorphism of the free group factors](https://github.com/openai/math/blob/main/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf)

**288. Kadison 相似性猜想。** 证明 Kadison 相似性猜想：从含幺复 C*-代数到希尔伯特空间上算子的每个有界复线性含幺代数同态，在经有界可逆算子共轭后成为 *-同态。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/288.md)）

&emsp;[Kadison's similarity theorem through uniform derivation estimates](https://github.com/openai/math/blob/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf)

**289. 强 Kadison–Kastler 稳定性及其空间边界。** 证明同一希尔伯特空间上足够接近的含幺 von Neumann 代数可由任意接近恒等的酉共轭，单位球算子范数距离有普适容差。反例表明：单侧近包含时近恒等共轭失效，且任意接近的范数可分 C*-代数不必环境酉共轭。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/289.md)）

&emsp;[Universal strong Kadison–Kastler stability](https://github.com/openai/math/blob/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf)

&emsp;[Near Inclusions of von Neumann Algebras Without Small Spatial Embeddings](https://github.com/openai/math/blob/main/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026/near-inclusions.pdf)

&emsp;[Close Separable C*-Algebras Without Spatial Conjugacy](https://github.com/openai/math/blob/main/preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/paper.pdf)

**290. 相对双中心化子与模谱恢复。** 对每个可分预对偶的 III₁ 型因子与每个忠实正规态证明 Connes 双中心化子猜想。更一般地，对每个容许忠实正规条件期望、可分预对偶的 von Neumann 代数包含 $`N\subset M`$，构造顺从带期望子代数 $`P\subset N`$ 使 $`P'\cap c(M)=N'\cap c(M)`$，解决相对双中心化子猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/290.md)）

&emsp;[Expected amenable subalgebras preserving core commutants](https://github.com/openai/math/blob/main/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf)

&emsp;[Bounded recovery for modular spectral averages](https://github.com/openai/math/blob/main/preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf)

**291. Cuntz 比较、核维数与等变 Jiang–Su 稳定性。** 对每个可数离散顺从群在单可分含幺无穷维核稳定有限、Jiang–Su 稳定的 C*-代数上的作用，证明等变 Jiang–Su 稳定性，在无迹动力学限制下解决 Szabó 猜想此情形。该族还证明含幺 Toms–Winter 猜想：在单可分含幺无穷维核情形，严格比较、有限核维数与 Jiang–Su 稳定性等价。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/291.md)）

&emsp;[Equivariant Jiang–Su Stability for Amenable Actions in the Unital Stably Finite Case](https://github.com/openai/math/blob/main/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/paper.pdf)

&emsp;[Cuntz comparison and Jiang–Su absorption](https://github.com/openai/math/blob/main/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf)

&emsp;[Nuclear dimension and Jiang–Su stability without elementary subquotients](https://github.com/openai/math/blob/main/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf)

&emsp;[Tracial projection methods and uniform property Gamma](https://github.com/openai/math/blob/main/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf)

**292. Kirchberg 的 $`\mathcal O_2`$ 范数超幂嵌入问题。** 构造显式可分含幺完全群 C*-代数：对自然数上任意自由超滤，它不能含幺嵌入任何固定非零含幺核 C*-代数的范数超幂。取目标为 $`\mathcal O_2`$ 时否定回答 Kirchberg 范数超幂嵌入问题。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/292.md)）

&emsp;[An explicit obstruction to nuclear norm-ultrapower embeddings](https://github.com/openai/math/blob/main/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026/paper.pdf)

**293. 不变投影、超不变子空间与传递代数。** 在每个无穷维可分复希尔伯特空间上构造非零范数拟幂零算子：无任何在其交换算子全体下不变的闭子空间。构造还给出超有限 II₁ 因子中无非平凡不变投影的算子。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/293.md)）

&emsp;[Invariant-projection counterexamples for every irrational rotation](https://github.com/openai/math/blob/main/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf)

&emsp;[Backward intertwiners and a transitive commutant](https://github.com/openai/math/blob/main/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf)

**294. Kaplansky 拟迹猜想与张量积稳定有限性的失效。** 构造可分含幺复 C*-代数：它容许归一化 2-拟迹，但全部非可加，否定 Kaplansky 拟迹猜想。由此，两个含幺单稳定有限 C*-代数的极小张量积可以真无穷，其中一个因子为 $`C_r^*(\mathbb F_2)`$。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/294.md)）

&emsp;[A counterexample to Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/paper.pdf)

**295. Kadison–Ringrose 上同调猜想。** 证明复 von Neumann 代数上每个次数至少 2、系数在代数自身的有界 Hochschild 上循环都有有界原函数。等价地，所有高阶有界 Hochschild 上同调群为零，解决 Kadison–Ringrose 猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/295.md)）

&emsp;[Vanishing of higher bounded Hochschild cohomology](https://github.com/openai/math/blob/main/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/paper.pdf)

**296. 有限因子的生成元问题。** 证明每个可分预对偶的 II₁ 型因子由单个算子生成（等价地由两个自伴算子生成），解决生成元问题。更强地，对每个此类因子的不可约包含 $`P\subset M`$，使 $`M=W^*(P,u)`$ 的酉 <i>u</i> 在迹 2-范数拓扑中构成稠密 <i>G</i><sub>δ</sub> 子集。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/296.md)）

&emsp;[Relative generation and the generator problem for finite factors](https://github.com/openai/math/blob/main/preprints/Relative-generation-and-the-generator-problem-for-finite-factors-September-23-2026/paper.pdf)

**297. Naimark 问题的 ZFC 反例。** 给出 Tanaka 的 ZFC 构造（含幺无穷维单复 C*-代数、忠实迹态、恰有一个非零不可约表示到酉等价）的替代。因此无额外集合论假设时无限制的紧算子刻画失效；反例不可分。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/297.md)）

&emsp;[A counterexample to Naimark's problem in ZFC](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/naimark-counterexample-zfc.pdf)

**298. 两种自由熵在两者都有限时也不同。** 构造迹 von Neumann 代数中的有界自伴元组：其微态与非微态自由熵满足 $`-\infty\lt \chi\lt \chi^*\lt \infty`$。这否定回答 Voiculescu 有限熵相等性问题：矩阵逼近与自由 Fisher 信息两种定义在两者都有限时也不同。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/298.md)）

&emsp;[A finite-entropy separation of microstates and nonmicrostates free entropy](https://github.com/openai/math/blob/main/preprints/A-finite-entropy-separation-of-microstates-and-nonmicrostates-free-entropy-September-25-2026/paper.pdf)

**299. Kirchberg–Rørdam 特征判据与无穷张量幂 Jiang–Su 稳定性。** 非零含幺可分复 C*-代数是 Jiang–Su 稳定的，当且仅当其范数中心序列代数没有特征（对每个自由超滤）。这回答 Kirchberg–Rørdam 特征问题。另外，每个无特征的此类代数的无穷极小张量幂是 Jiang–Su 稳定的，回答 Dadarlat–Toms 问题。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/299.md)）

&emsp;[The Kirchberg–Rørdam character criterion](https://github.com/openai/math/blob/main/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf)

**300. 逼近与二次强算子铺瓦化。** 证明复 von Neumann 代数的每个自伴元相对任意极大交换子代数容许强算子铺瓦化，块数 $`O(\varepsilon^{-2})`$。在强拓扑中由任意接近恒等的投影压缩后范数界成立，解决 Popa–Vaes 二次铺瓦化猜想。

&emsp;[Approximation Paving over Arbitrary Maximal Abelian Subalgebras](https://github.com/openai/math/blob/main/preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf)

&emsp;[Quadratic Strong-Operator Paving over Arbitrary Maximal Abelian Subalgebras](https://github.com/openai/math/blob/main/preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf)

**301. 迹锥与 Razak–Jacelon 稳定化。** 用扩展下半连续迹权的完整拓扑锥，分类与 Razak–Jacelon 代数及紧算子作张量后的可分核复 C*-代数。这回答 Robert 的迹锥问题，包括任意理想结构、有限与无穷子商并存的代数。

&emsp;[The trace cone classifies Razak–Jacelon stabilizations](https://github.com/openai/math/blob/main/preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf)

**302. 比较半径等于平均维数的一半。** 对无穷紧可度量化空间 <i>X</i> 的每个极小同胚 <i>h</i>，$`C(X)\rtimes_h\mathbb Z`$ 的比较半径等于 $`\tfrac12\mathrm{mdim}(X,h)`$（含无穷值）。零平均维数等价于小边界性质、Jiang–Su 稳定性与有限核维数；此时核维数至多 1。

&emsp;[Filtered products and boundary-preserving compression in complex cobordism](https://github.com/openai/math/blob/main/preprints/Filtered-products-and-boundary-preserving-compression-in-complex-cobordism-September-25-2026/paper.pdf)

&emsp;[Radius of comparison equals half the mean dimension](https://github.com/openai/math/blob/main/preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/paper.pdf)

**303. 弱纯无穷性与 Cuntz 代数吸收。** 解决 Kirchberg–Rørdam 的普通到强纯无穷性问题（复 C*-代数）。对恰当代数，每个正元的某个固定有限放大的真无穷性也已足够。因此每个具有该性质的可分核代数吸收 $`\mathcal O_\infty`$，无需含幺或单性假设。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/303.md)）

&emsp;[Weak pure infiniteness and O-infinity absorption](https://github.com/openai/math/blob/main/preprints/Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026/paper.pdf)

---

## 14. 拓扑学（Topology，18 个族）

**304. 每个维数的 Hilbert–Smith 猜想。** 每个在连通有限维拓扑流形上忠实且联合连续作用的局部紧第二可数豪斯多夫群都是李群。这证明无边界豪斯多夫第二可数流形上所有有限维数的 Hilbert–Smith 猜想。

&emsp;[The Hilbert–Smith conjecture in every finite dimension](https://github.com/openai/math/blob/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/paper.pdf)

**305. 四维圆盘嵌入与 Wall 猜想。** 无限制的四维圆盘嵌入猜想失效：带架代数对偶球面不足以获得不相交局部平坦张成圆盘。特别地，自由群 $`F_2`$ 在 Freedman–Quinn 意义下不是好的。还构造四维有限表现整 Poincaré 对偶群：有有限分类空间但不能实现为闭非球面拓扑四维流形的基本群，否定 Wall 猜想。

&emsp;[A boundary-only obstruction to four-dimensional disk embedding](https://github.com/openai/math/blob/main/preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/paper.pdf)

&emsp;[A marked tensor obstruction to four-dimensional disk embedding](https://github.com/openai/math/blob/main/preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/paper.pdf)

&emsp;[A PD4 group without an aspherical manifold model](https://github.com/openai/math/blob/main/preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/paper.pdf)

**306. 纯装饰手术猜想。** $`S^3`$ 中非平凡光滑纽结的不同 Dehn 手术斜率从不产生保定向同胚的流形，证明纯装饰手术猜想。该陈述包括子午斜率。

&emsp;[Purely cosmetic surgery on knots in the three-sphere](https://github.com/openai/math/blob/main/preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/paper.pdf)

**307. 极大粗装配的有理单射性失效。** 构造一致离散有界几何空间：其极大粗装配映射非有理单射。例子是度一致有界的有限连通图的粗不交并，核类有无穷阶。配套结果给出约化粗装配的类似失效，否定有理粗 Novikov 猜想。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/307.md)）

&emsp;[Failure of rational injectivity for maximal coarse assembly](https://github.com/openai/math/blob/main/preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/paper.pdf)

&emsp;[A counterexample to the coarse Novikov conjecture](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf)

**308. 每个高度处的有限 Smith–Toda 复形。** 对每个 <i>n</i> ≥ 0，在依赖 <i>n</i> 的素数 <i>p</i> 处构造有限 Smith–Toda 谱：Brown–Peterson 同调为 $`BP_*/(p,v_1,\ldots,v_n)`$ 带典范余模结构。因此当素数可变时 Smith–Toda 复形在每个高度存在；显式例子在 <i>p</i> = 1009 实现 $`V(4)`$。

&emsp;[Finite Smith–Toda Complexes at Varying Primes](https://github.com/openai/math/blob/main/preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/paper.pdf)

&emsp;[A finite Smith–Toda complex V(4) at the prime 1009](https://github.com/openai/math/blob/main/preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/paper.pdf)

**309. 素数三处的 Kervaire 不变量问题。** 解决奇素数 Kervaire 不变量问题在素数三处的情形：恰有指标 0、2、3 的标准类在模三 Adams 谱序列中存活，对应茎 10、106、322。每个存活检测陪集含一个恰好三阶加法的元素。

&emsp;[The Kervaire invariant problem at the prime three](https://github.com/openai/math/blob/main/preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/paper.pdf)

**310. 有理同调中的 Quillen 猜想。** 对每个有限群与每个素数证明 Quillen 猜想的有理同调形式：若 <i>G</i> 的最大正规 <i>p</i>-子群平凡，则非平凡初等交换 <i>p</i>-子群的偏集有非零增广约化有理同调，从而不可缩。

&emsp;[Rational homology and Quillen's conjecture](https://github.com/openai/math/blob/main/preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/paper.pdf)

**311. Hovey–Strickland 与 Chai 猜想。** 对有限剩余域上的 Lubin–Tate 形变环证明 Chai 不变理想猜想（每个素数与正高度 <i>n</i>）。经由 Barthel–Heard–Naumann 的蕴含，这证明 Hovey–Strickland 猜想：可对偶 $`K(n)`$-局部谱恰有 $`n+2`$ 个厚张量理想，其 Balmer 谱是 $`n+1`$ 个点的链。

&emsp;[Stabilizer orbits and thick tensor ideals of dualizable K(n)-local spectra](https://github.com/openai/math/blob/main/preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/paper.pdf)

**312. Grothendieck 同伦假设。** 在 Ara–Henry 约定下对每个 Grothendieck 余相干子证明 Grothendieck 同伦假设：这些代数对象恢复空间的同伦理论。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/312.md)）

&emsp;[The Grothendieck homotopy hypothesis via elementary expansions](https://github.com/openai/math/blob/main/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/paper.pdf)

**313. $`K(n)`$-局部球面的有限生成。** 回答 Hovey 与 Hovey–Strickland 的逐次有限性问题：$`K(n)`$-局部球面的每个同伦群都是有限生成的 ℤ<sub>p</sub>-模（每个素数、正高度与整次数）。对任何有限 <i>p</i>-局部谱作 $`K(n)`$-局部化后同样成立。

&emsp;[Finite generation for the K(n)-local sphere](https://github.com/openai/math/blob/main/preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/Finite-generation-for-the-Kn-local-sphere-September-24-2026.pdf)

**314. 循环长度与色固定点损失。** 确定有限 <i>p</i>-群 <i>G</i> 的每个子群 <i>H</i> 从几何 <i>H</i>-不动点到几何 <i>G</i>-不动点的最优色损失。在每个非负高度，损失等于从 <i>H</i> 到 <i>G</i> 带循环商的最短次正规链长度。每个商只计一次（与阶无关），有限谱见证锐利性。

&emsp;[Cyclic length and chromatic fixed-point loss](https://github.com/openai/math/blob/main/preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026.pdf)

**315. 四维 Singer 猜想。** 证明每个闭连通非球面拓扑四维流形的万有覆盖的 <i>L</i>²-Betti 数在二次以外为零。更一般地，同样结论对每个形式维数 4 的有限连通非球面整 Poincaré 复形成立，在更广类中证明四维 Singer 猜想。

&emsp;[The Singer conjecture in dimension four](https://github.com/openai/math/blob/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/paper.pdf)

**316. Curtis 猜想。** 证明 Curtis 猜想：球面的正次数模二稳定 Hurewicz 像由存在性的 Hopf 不变量一类 <i>η</i>、<i>ν</i>、<i>σ</i> 与 Kervaire 不变量一类张成。

&emsp;[The Stable Hurewicz Image of the Sphere at Two](https://github.com/openai/math/blob/main/preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/paper.pdf)

**317. 所有严格高维的 Thomason 模型结构。** 解决 Ara–Maltsiniotis 猜想：对每个 <i>n</i> ≥ 1 与 <i>n</i> = <i>ω</i>，小严格球形 <i>n</i>-范畴容许 Quillen 等价于单纯集的真组合 Thomason 模型结构。因此严格高范畴在每个所述维数建模空间的同伦理论。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/317.md)）

&emsp;[Thomason Model Structures in Every Strict Higher Dimension](https://github.com/openai/math/blob/main/preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/paper.pdf)

**318. 色分裂：滤过与反例。** 否定高度三、素数 <i>p</i> ≥ 5 的强色分裂，以及导出 <i>p</i>-完备球面在高度 <i>p</i>（<i>p</i> ≥ 5）与 $`p+1`$（<i>p</i> ≥ 7）的弱分裂。然而对 <i>n</i> ≥ 1、$`p\gt n+1`$，重叠 $`L_{n-1}L_{K(n)}S_p^\wedge`$ 容许由预测的局域化球面块组成的 $`2^n`$ 阶滤过。在高度三素数三处，即使是来自此类块的有限装配也在导出完备球面的 $`E(2)`$-局部模范畴中失效。

&emsp;[Filtered chromatic splitting at generic primes](https://github.com/openai/math/blob/main/preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/paper.pdf)

&emsp;[The height-three chromatic overlap: an explicit filtration and its attachments](https://github.com/openai/math/blob/main/preprints/The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026/paper.pdf)

&emsp;[A rational obstruction to strong chromatic splitting at height three](https://github.com/openai/math/blob/main/preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/paper.pdf)

&emsp;[Failure of finite assembly for a chromatic overlap at the prime three](https://github.com/openai/math/blob/main/preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/paper.pdf)

&emsp;[Counterexamples to weak chromatic splitting: sphere kernels and descent exponents](https://github.com/openai/math/blob/main/preprints/Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026/paper.pdf)

**319. 色高度二处有限生成的反例。** 在色高度二驳斥 Hahn–Wilson 猜想。对每个足够大素数 <i>p</i>，构造精确 fp-型二的连通 <i>p</i>-完备谱：不能由完备化的 $`\mathrm{BP}\langle2\rangle`$ 经有限多次和、移位、锥与收缩项构造。这些例子仍满足有限与望远镜局部化比较。

&emsp;[Counterexamples to the Hahn-Wilson conjecture at height two](https://github.com/openai/math/blob/main/preprints/Counterexamples-to-the-Hahn-Wilson-conjecture-at-height-two-September-26-2026/paper.pdf)

**320. 非同胚的闭非球面四维流形。** 构造同伦等价但不同胚的闭连通非球面拓扑四维流形，其基本群共同为词双曲。这否定 Borel 猜想在四维的同胚存在性形式。

&emsp;[Nonhomeomorphic closed aspherical four-manifolds with the same homotopy type](https://github.com/openai/math/blob/main/preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/paper.pdf)

**321. Wall 有限 D(2) 问题的反例。** 构造有限连通三维 CW 复形：其万有覆盖在二次以上无整同调、对每个局部系数模三次上同调为零，但没有有限二维同调模型。这否定 Wall 有限 D(2) 猜想；例子基本群无穷。

&emsp;[A Counterexample to Wall's D(2) Problem](https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/wall-d2-counterexample.pdf)

---

## 15. 泛函分析（Functional analysis，11 个族）

**322. Tingley 球面等距问题。** 解决 Tingley 问题：非零实巴拿赫空间单位球面之间的每个满射等距都唯一延拓为整个空间上的满射实线性等距。不施加维数限制，故单位球面的度量几何决定巴拿赫空间到线性等距。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/322.md)）

&emsp;[A positive solution to Tingley’s problem](https://github.com/openai/math/blob/main/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf)

**323. 可分商问题对 ZFC 的独立性。** 在可测基数一致性假设下建立：可分商问题独立于 ZFC。「每个无穷维巴拿赫空间有可分无穷维商」可以在所有实与复巴拿赫空间上成立，而连续统假设给出两个域上的反例。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/323.md)）

&emsp;[Relative independence of the separable quotient problem](https://github.com/openai/math/blob/main/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf)

**324. Lipschitz 等价的巴拿赫空间不必线性同构。** 构造全局双 Lipschitz 等价但不线性同构的可分实巴拿赫空间，否定回答可分 Lipschitz 同构问题。即双 Lipschitz 等价意义下的完整度量结构也不决定可分巴拿赫空间的线性同构类。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/324.md)）

&emsp;[Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic](https://github.com/openai/math/blob/main/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf)

&emsp;[Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0](https://github.com/openai/math/blob/main/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf)

**325. 完整 Crouzeix 猜想。** 解决完整 Crouzeix 猜想：对复希尔伯特空间上的每个有界算子 <i>A</i> 与每个有限矩阵值多项式 <i>P</i>，有 $`\lVert P[A]\rVert\le2\sup_{z\in W(A)}\lVert P(z)\rVert`$（<i>W</i>(<i>A</i>) 为数值域）。常数 2 锐利、与矩阵规模无关、在无穷维成立。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/325.md)）

&emsp;[A direct proof of the complete Crouzeix inequality](https://github.com/openai/math/blob/main/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf)

&emsp;[The complete Crouzeix theorem: optimal similarity and a common positive boundary representation](https://github.com/openai/math/blob/main/preprints/The-complete-Crouzeix-theorem-September-23-2026/paper.pdf)

**326. 逼近性质下的余型–余型猜想。** 对具有逼近性质的实巴拿赫空间解决余型–余型猜想：这样的非零空间是 <i>K</i>-凸的，当且仅当它与其对偶都有有限 Rademacher 余型（指数可不同）。等价地，这些余型假设迫使非平凡 Rademacher 型。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/326.md)）

&emsp;[The cotype–cotype conjecture under the approximation property](https://github.com/openai/math/blob/main/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/paper.pdf)

**327. Markov 型刻画超自反性。** 证明每个对某个 <i>p</i> &gt; 1 具有 Markov 型 <i>p</i> 的实巴拿赫空间都容许等价的一致凸范数，回答 Naor 重赋范问题。与已知逆命题结合，以非平凡 Markov 型刻画超自反性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/327.md)）

&emsp;[Nontrivial Markov Type Forces Superreflexivity](https://github.com/openai/math/blob/main/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf)

**328. 自反巴拿赫空间中的非扩张不动点。** 解决 Kirk 自反空间不动点问题：实自反巴拿赫空间非空有界闭凸子集的每个非扩张自映射都有不动点。结果使用原范数，不假设一致凸性。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/328.md)）

&emsp;[Fixed Points of Nonexpansive Maps in Reflexive Banach Spaces](https://github.com/openai/math/blob/main/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/paper.pdf)

**329. 度量熵对偶的反例。** 否定 Pietsch 维数无关度量熵对偶猜想。中心对称凸体违反覆盖数与其极体覆盖数之间每个提出的普适常数选择，即使覆盖体是方体。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/329.md)）

&emsp;[Counterexamples to the duality conjecture for metric entropy](https://github.com/openai/math/blob/main/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/main.pdf)

**330. Lipschitz 自由空间中有界逼近的一致离散反例。** 构造可数一致离散度量空间：其实 Lipschitz 自由巴拿赫空间有逼近性质但没有有界逼近性质，否定回答 Kalton 问题。有限秩算子在每紧集上逼近恒等，但其范数不能共享有限界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/330.md)）

&emsp;[A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces](https://github.com/openai/math/blob/main/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026/main.pdf)

**331. 自反中点凸性与菱形失真。** 构造实自反巴拿赫空间：渐近中点一致凸范数但没有等价渐近一致凸范数，把 Baudier 的分离扩展到自反空间。同一空间中深度 <i>k</i> 可数分支菱形失真至少 $`\sqrt{1+k/12}`$，故即使自反，中点一致凸性也不强制一致有界菱形失真。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/331.md)）

&emsp;[Asymptotic midpoint uniform convexity and unbounded diamond distortion in a reflexive tree space](https://github.com/openai/math/blob/main/preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/manuscript.pdf)

&emsp;[Midpoint lenses in segment spaces](https://github.com/openai/math/blob/main/preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/manuscript.pdf)

&emsp;[Distortion of countably branching diamonds from midpoint and tree energies](https://github.com/openai/math/blob/main/preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/manuscript.pdf)

&emsp;[Exact asymptotic moduli in a Daugavet subspace of L1](https://github.com/openai/math/blob/main/preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/manuscript.pdf)

&emsp;[Midpoint convexity from bounded tree potentials and path costs](https://github.com/openai/math/blob/main/preprints/Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026/manuscript.pdf)

&emsp;[Independent products in real L1: asymptotic midpoint convexity without AUC renormings](https://github.com/openai/math/blob/main/preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/manuscript.pdf)

&emsp;[Midpoint convexity from two recursive potentials](https://github.com/openai/math/blob/main/preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/manuscript.pdf)

**332. <i>ℓ</i>₁ 的度量 Markov 余型与希尔伯特空间 Lipschitz 延拓。** 证明实 <i>ℓ</i>₁ 有度量 Markov 余型二，回答 Mendel–Naor 问题。因此，从实希尔伯特空间任意子集到 <i>ℓ</i>₁ 的每个 Lipschitz 映射都以普适乘性损失延拓到全空间，解决此目标的 Ball 延拓问题。

&emsp;[Metric Markov Cotype Two of <i>ℓ</i><sub>1</sub>](https://github.com/openai/math/blob/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/l1-markov-cotype.pdf)

---

## 16. 微分几何（Differential geometry，29 个族）

**333. 曲面到 ℝ⁴ 的光滑等距浸入。** 每个闭光滑黎曼曲面都容许到 ℝ⁴ 的光滑等距浸入，解决四维等距浸入问题的闭曲面形式。这包括不可定向曲面与任意高斯曲率的度量。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/333.md)）

&emsp;[Smooth isometric immersions of closed surfaces into Euclidean four-space](https://github.com/openai/math/blob/main/preprints/Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026/paper.pdf)

**334. 无 ℝ³ 局部等距浸入的光滑曲面度量。** 构造 $`(-1,1)^2`$ 上的光滑正定度量：原点的任何邻域都不容许到 ℝ³ 的光滑等距浸入。即使缩小邻域，也否定回答无限制的光滑局部等距实现问题（曲面情形）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/334.md)）

&emsp;[A Smooth Metric with No Local Isometric Immersion into Three-Space](https://github.com/openai/math/blob/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/paper.pdf)

**335. Gromov 的单纯体积积分标量曲率界。** 对每个闭连通定向光滑 <i>n</i>-流形（<i>n</i> ≥ 3）与每个光滑度量证明 $`\int_M(\mathrm{Scal}_g^-)^{n/2}\,dV_g\ge a_n\lVert M\rVert`$（$`a_n\gt 0`$ 只依赖维数；$`\mathrm{Scal}_g^-=\max\{0,-\mathrm{Scal}_g\}`$，$`\lVert M\rVert`$ 为实单纯体积）。还证明正标量曲率下的有理性非本质性，解决 Gromov–Lawson 猜想：闭非球面流形上每个非负标量曲率度量都是平坦的。

&emsp;[An integral scalar curvature bound for real simplicial volume](https://github.com/openai/math/blob/main/preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/v126-proof.pdf)

&emsp;[Positive scalar curvature forces rational inessentiality](https://github.com/openai/math/blob/main/preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/paper.pdf)

**336. 谱标量曲率、Urysohn 宽度与宏观维数。** 每个满足二次型不等式 $`-4\Delta+\mathrm{Scal}\ge1`$ 的完备连通光滑无边界 <i>n</i>-流形（<i>n</i> ≥ 3），都容许到维数至多 <i>n</i>−2 的单纯复形的连续映射：全部纤维在原度量下直径只由 <i>n</i> 界定。这把 Gromov 宽度结论强化到谱标量曲率。闭正标量曲率流形的万有覆盖（每个 <i>n</i> ≥ 2）也有连续宏观维数至多 <i>n</i>−2。

&emsp;[Spectral scalar curvature and uniform Urysohn width](https://github.com/openai/math/blob/main/preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/main.pdf)

&emsp;[Spectral scalar curvature and Urysohn width in dimension three](https://github.com/openai/math/blob/main/preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026/spectral-urysohn-three-manifolds.pdf)

&emsp;[Positive scalar curvature and uniform codimension-two width](https://github.com/openai/math/blob/main/preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/paper.pdf)

**337. 锐利 Cartan–Hadamard 等周性与刚性。** 在每个维数证明广义 Cartan–Hadamard 等周性：截面曲率至多 <i>κ</i> ≤ 0 的完备单连通流形中，每个有限体积有限周长集都满足与等体积模型球的锐利比较。<i>κ</i> = 0 时有界正体积等号区域是欧氏球。还对任意真 CAT(0) 空间中紧支撑积分 <i>n</i>-循环（<i>n</i> ≥ 2）证明锐利欧氏填充界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/337.md)）

&emsp;[Generalized Cartan–Hadamard isoperimetry and Euclidean equality rigidity](https://github.com/openai/math/blob/main/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf)

&emsp;[Sharp integral fillings in CAT(0) spaces](https://github.com/openai/math/blob/main/preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf)

**338. Yau 单值化猜想。** 证明 Yau 单值化猜想：每个带严格正全纯双截曲率的完备连通非紧 Kähler 流形都双全纯同构于 ℂⁿ。

&emsp;[Uniformization of complete Kähler manifolds with positive bisectional curvature](https://github.com/openai/math/blob/main/preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/paper.pdf)

**339. Katok 熵刚性猜想。** 对维数至少 3、截面曲率严格为负的闭连通黎曼流形证明 Katok 熵刚性猜想：归一化刘维尔测度最大化测地流熵当且仅当度量局部对称。

&emsp;[Entropy equality and local symmetry in negative curvature](https://github.com/openai/math/blob/main/preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/paper.pdf)

**340. 近旁拉格朗日猜想的反例。** 否定无限制的近旁拉格朗日猜想。对某个足够大的偶数 <i>N</i>，构造 $`T^*(S^9\times S^{N-1})`$ 中的闭恰当嵌入拉格朗日子流形：微分同胚于底但不哈密顿同痕于零截口。

&emsp;[A counterexample to the nearby Lagrangian conjecture](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/paper.pdf)

**341. Donaldson 超辛形变猜想。** 以保持上同调形式证明 Donaldson 超辛形变猜想。闭连通定向四维流形上归一化 $`\int\omega_i\wedge\omega_j=\delta_{ij}`$ 的每个正光滑闭 2-形式三元组，都在保持全部三个上同调类的同时经过正闭三元组形变到超凯勒三元组。任何正三元组都可先经常数线性变换归一化。

&emsp;[Deforming hypersymplectic four-manifolds to hyperkähler triples](https://github.com/openai/math/blob/main/preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026/paper.pdf)

**342. Donaldson 驯服到相容猜想。** 证明 Donaldson 驯服到相容猜想：闭四维流形上被辛形式驯服的每个光滑殆复结构都容许相容辛形式。殆复结构保持固定；形式的同调类可以改变。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/342.md)）

&emsp;[Taming implies compatibility on four-manifolds](https://github.com/openai/math/blob/main/preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/paper.pdf)

**343. 高维辛球装填。** 对每个维数 $`2n\ge6`$ 的任意容量解决 Siegel–Yao 猜想：容量为 $`R_1,\ldots,R_k`$ 的有限多个闭辛球不交嵌入容量 <i>R</i> 的开球，当且仅当 $`\sum_iR_i^n\lt R^n`$ 且 $`R_i+R_j\lt R`$（每对不同 <i>i</i>、<i>j</i>）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/343.md)）

&emsp;[Symplectic Ball Packings in Higher Dimensions](https://github.com/openai/math/blob/main/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/paper.pdf)

**344. 度量 Blaschke 猜想。** 证明度量 Blaschke 猜想：正维数的每个闭连通黎曼流形，若其单射半径等于直径，则相差缩放是标准紧一秩对称空间。

&emsp;[The metric Blaschke theorem](https://github.com/openai/math/blob/main/preprints/The-metric-Blaschke-theorem-September-23-2026/paper.pdf)

**345. 黎曼球面与闭三维流形上的无穷多闭测地线。** 证明 $`S^n`$（<i>n</i> ≥ 2）上每个光滑黎曼度量都有无穷多个两两像不同的本原闭测地线。同样结论对每个容许有限光滑球面覆盖的闭流形与每个闭三维流形成立，无需可定向性或非退化性限制。

&emsp;[Infinitely many closed geodesic images on every Riemannian sphere](https://github.com/openai/math/blob/main/preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/paper.pdf)

**346. 平稳积分 varifold 的锐利奇异集界。** 证明欧氏开集中每个平稳积分 <i>m</i>-varifold 的奇异集豪斯多夫维数至多 <i>m</i>−1，在每个正维数与余维数都是锐利界。在圆球上，该族还证明几乎处处正则性：奇异集 <i>m</i> 维豪斯多夫测度为零。

&emsp;[A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold](https://github.com/openai/math/blob/main/preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/varifold-singular-dimension.pdf)

&emsp;[Almost-everywhere regularity of stationary integral varifolds](https://github.com/openai/math/blob/main/preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/paper.pdf)

**347. 稳定 Morse 与强 Arnold 不动点界的反例。** 否定非退化哈密顿不动点的稳定 Morse 下界：实维数 22 的单连通闭 Kähler 流形上，低于稳定 Morse 数的亏损无界。复二次锥面上的一个哈密顿微分同胚恰有三个不动点，少于每个光滑函数必需的四个临界点。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/347.md)）

&emsp;[Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two](https://github.com/openai/math/blob/main/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf)

&emsp;[Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number](https://github.com/openai/math/blob/main/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf)

&emsp;[Hamiltonian Fixed Points Below the Stable Morse Number](https://github.com/openai/math/blob/main/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf)

&emsp;[A nondegenerate counterexample to the Morse-number Arnold bound](https://github.com/openai/math/blob/main/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf)

&emsp;[Three fixed points on the symplectic quadric threefold](https://github.com/openai/math/blob/main/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf)

**348. 非负曲率 Einstein 分类与 <i>L</i>² 拓扑间隙。** 分类带正 Einstein 常数与非负截面曲率的闭连通 Einstein 四维流形：相差缩放，其万有黎曼覆盖是圆 <i>S</i>⁴、Fubini–Study $`\mathbb{CP}^2`$ 或等径圆球面的乘积。闭单连通非负曲率四维流形，只要其无迹 Ricci 曲率的尺度不变 <i>L</i>² 范数低于普适正常数，就微分同胚于其中之一。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/348.md)）

&emsp;[Zero-Plane Rigidity for Einstein Four-Manifolds](https://github.com/openai/math/blob/main/preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf)

&emsp;[An L² Einstein Gap for Nonnegatively Curved Four-Manifolds](https://github.com/openai/math/blob/main/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf)

&emsp;[Positively curved Einstein four-manifolds](https://github.com/openai/math/blob/main/preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf)

**349. Solomon–Yau 最小体积猜想。** 对圆球面的极小超曲面证明 Solomon–Yau 最小体积猜想：对每个 <i>m</i> ≥ 2，到单位球面 $`S^{m+1}`$ 的闭连通极小浸入若其像非全测地，则体积至少为最小极小 Clifford 乘积的体积（计覆盖重数）。

&emsp;[The Solomon–Yau least-volume theorem](https://github.com/openai/math/blob/main/preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/paper.pdf)

**350. Yau 节点界：曲面与高维。** 在每张固定光滑闭曲面上证明节点长度的锐利 $`C\sqrt\lambda`$ 上界，完成 Yau 猜想的曲面情形。上界在三维与四维对固定光滑度量失效，包括任意接近圆球的 <i>S</i>³ 度量。五维中节点测度可以比 $`\lambda^{1/2+\varepsilon_0}`$ 更快增长（固定 $`\varepsilon_0\gt 0`$），排除任意小的幂损失。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/350.md)）

&emsp;[Sharp nodal length on smooth surfaces](https://github.com/openai/math/blob/main/preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/paper.pdf)

&emsp;[Smooth counterexamples to Yau's nodal upper bound in dimensions three and four](https://github.com/openai/math/blob/main/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf)

&emsp;[Power-law violations of Yau's nodal upper bound](https://github.com/openai/math/blob/main/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf)

**351. 标量曲率与有限时间 Ricci 流奇点。** 证明闭四维流形上的光滑 Ricci 流可以在标量曲率保持一致有界的任何有限时刻之后延拓。一个高维反例在有限极大时刻标量曲率有界但全曲率无界，否定无限制的标量曲率延拓猜想。

&emsp;[A closed Ricci flow with bounded scalar curvature and finite-time curvature blowup](https://github.com/openai/math/blob/main/preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/paper.pdf)

&emsp;[Bounded scalar curvature and smooth extension of four-dimensional Ricci flow](https://github.com/openai/math/blob/main/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf)

&emsp;[Path selection and an elliptic inequality on degenerating Ricci-flat trees](https://github.com/openai/math/blob/main/preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf)

**352. Calabi 流的有限时间奇点。** 通过构造 $`\mathbb{CP}^{10}`$ 上光滑 $`U(10)`$ 不变 Kähler 度量（其流产生有限时间奇点）否定 Chen 的 Calabi 流光滑长时间存在猜想。该度量位于 Fubini–Study 类中，故失效发生在含常标量曲率度量的类中。

&emsp;[A finite-time singularity of Calabi flow on projective space](https://github.com/openai/math/blob/main/preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/paper.pdf)

**353. 到九维的仿射 Bernstein 刚性与十维光滑反例。** 证明维数 3 到 9 的每个对其诱导欧氏度量完备的光滑局部一致凸仿射极大图都是椭圆抛物面。十维中一个光滑整体非二次例子使该范围锐利。在维数 3 到 9，抛物面分类对仿射 Berwald–Blaschke 度量完备的连通开局部一致凸仿射极大超曲面同样成立。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/353.md)）

&emsp;[A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten](https://github.com/openai/math/blob/main/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026/affine-maximal-dimension-ten.pdf)

&emsp;[The affine Bernstein theorem in dimensions three through nine](https://github.com/openai/math/blob/main/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf)

**354. 立方三维环面的等周轮廓。** 确定单位立方平坦三维环面的等周轮廓并分类每个有限周长极小化子：球、最短闭测地线周围的圆管、坐标板片及其补。转变体积为 $`4\pi/81`$ 与 $`1/\pi`$，每个转变处恰有相邻两类同时极小。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/354.md)）

&emsp;[The Isoperimetric Conjecture for the Cubic Flat Three-Torus](https://github.com/openai/math/blob/main/preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/article.pdf)

**355. 首个曲面奇点处的唯一切流。** 证明 ℝ³ 中无边界光滑紧连通嵌入曲面在首个奇点时刻的切流唯一性。在每个奇点处，所有固定中心后向切流在原环境坐标下对每个负时刻作为面积测度一致，无需平均凸性或指定切模型。

&emsp;[Uniqueness of tangent flows at the first singular time of embedded surface mean-curvature flow](https://github.com/openai/math/blob/main/preprints/Tangent-flow-uniqueness-2026-09-24/paper.pdf)

**356. Gigli 对 Alexandrov 曲率的刻画。** 证明 Gigli 猜想：在每个整数维数 <i>n</i> ≥ 2，Alexandrov 曲率至少 <i>κ</i> 由满支撑 $`\mathrm{RCD}((n-1)\kappa,n)`$ 条件（参考测度 $`\mathcal H^n`$）与原全局测试类中的分布截面曲率至少 <i>κ</i> 联合刻画。RCD 条件为未约化形式。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/356.md)）

&emsp;[Gigli’s distributional curvature characterization of Alexandrov spaces](https://github.com/openai/math/blob/main/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf)

&emsp;[Weak Hessian bounds along every geodesic in RCD spaces](https://github.com/openai/math/blob/main/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf)

**357. 每个正则 RCD 点处的双 Lipschitz 坐标。** 证明非坍缩 $`\mathrm{RCD}(K,n)`$ 空间（<i>K</i> ∈ ℝ、整数 <i>n</i> ≥ 2）的每个正则点都有双 Lipschitz 同胚于 ℝⁿ 开子集的开邻域。正则性要求所有带点切空间欧氏；参考测度恰为 $`\mathcal H^n`$；图表以依赖点的有限常数比较环境距离。

&emsp;[Bi-Lipschitz Coordinates at Regular Points of Noncollapsed RCD Spaces](https://github.com/openai/math/blob/main/preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/paper.pdf)

**358. 无共轭点也无非正曲率的三维流形。** 构造闭连通可定向光滑三维流形：容许无共轭点度量但不容许非正截面曲率度量。这已在三维否定回答「第一个度量存在性质是否蕴含第二个」。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/358.md)）

&emsp;[A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric](https://github.com/openai/math/blob/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/paper.pdf)

**359. 无有界全纯坐标的负 Kähler 曲率。** 构造 ℂ³ 中的可缩域：带完备负捏 Kähler 度量但没有有界全纯坐标，否定此情形的有界域单值化。一个高维例子截面曲率至多 −1 且只有常数有界全纯函数；其曲率无下界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/359.md)）

&emsp;[A negatively pinched Kähler threefold without bounded holomorphic coordinates](https://github.com/openai/math/blob/main/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf)

&emsp;[One-sided negative sectional curvature and the holomorphic Liouville property](https://github.com/openai/math/blob/main/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/paper.pdf)

**360. 弱 MTW 曲率给出凸性与正则最优输运。** 在每个满足弱 Ma–Trudinger–Wang 曲率的闭连通黎曼流形（维数至少 2）上，所有切单射域都是凸的，解决此情形的 Villani 猜想。对上方有界且离开零的有界可测概率密度之间的平方距离输运，最优映射及其逆 Hölder 连续。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/360.md)）

&emsp;[Global Support and Convex Injectivity Domains under Weak MTW](https://github.com/openai/math/blob/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/paper.pdf)

&emsp;[Uniform Bi-Holder Transport from Weak MTW](https://github.com/openai/math/blob/main/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf)

**361. 整数次数调和维数比较的失效。** 否定 Yau 对非负 Ricci 曲率流形上整数增长调和函数提出的欧氏维数界。对每个足够大整数 <i>k</i>，ℝ³ 上一个完备光滑度量有至少 $`(k+2)^2`$ 个增长至多 <i>k</i> 的独立调和函数，超过欧氏计数 $`(k+1)^2`$。度量可依赖 <i>k</i>。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/361.md)）

&emsp;[A counterexample to integer-degree harmonic dimension comparison](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/paper.pdf)

&emsp;[A Three-Dimensional Counterexample to Integer-Degree Harmonic Dimension Comparison](https://github.com/openai/math/blob/main/preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/paper.pdf)

---

## 17. 偏微分方程（Partial differential equations，16 个族）

**362. 相对论 Vlasov–Maxwell 的整体光滑性。** 证明三维单物种相对论 Vlasov–Maxwell 系统的大数据整体存在唯一性。光滑容许初值可以任意，只要粒子密度紧支撑、电磁场能量有限且各阶导数有界；解在每个有限时间区间上保持光滑。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/362.md)）

&emsp;[Global classical solutions of the three-dimensional relativistic Vlasov–Maxwell system](https://github.com/openai/math/blob/main/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf)

**363. 硬球玻尔兹曼方程的带局部守恒非唯一性。** 从同一非负初值构造三维周期硬球玻尔兹曼方程的两个不同整体熵解：速度支撑有界，质量、能量与绝对熵有限。两者都强连续于 <i>L</i>¹ 并满足质量、动量与动能的精确局部守恒。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/363.md)）

&emsp;[Nonuniqueness with local conservation for the hard-sphere Boltzmann equation](https://github.com/openai/math/blob/main/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf)

&emsp;[Nonuniqueness for the periodic hard-sphere Boltzmann equation](https://github.com/openai/math/blob/main/preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/paper.pdf)

**364. Boltzmann 生命期上的动理学极限与涨落。** 从三维巨正则牛顿气体导出非线性玻尔兹曼方程，贯穿每个带一致高斯衰减的正则动理学区间。稳定有限程径向势可有吸引井与奇异排斥核；假设初始对排除与空间可和的高斯密度与梯度界。配套结果给出有限维硬球高斯涨落：以精确微观期望为中心、由线性涨落玻尔兹曼方程支配。

&emsp;[The Boltzmann–Grad limit for stable radial potentials on regular kinetic intervals](https://github.com/openai/math/blob/main/preprints/The-Boltzmann-Grad-limit-for-stable-radial-potentials-on-regular-kinetic-intervals-September-23-2026/paper.pdf)

&emsp;[Hard-sphere fluctuations on the regular Boltzmann lifespan](https://github.com/openai/math/blob/main/preprints/Hard-sphere-fluctuations-on-the-regular-Boltzmann-lifespan-September-23-2026/paper.pdf)

**365. 从单个边界片恢复度量与联络。** 任何非空开边界片上的零频测量，在相差固定于该片的微分同胚与规范下，确定至少三维紧连通流形上平凡厄米秩二丛的光滑度量与光滑酉联络。输入与观测使用同一片。与之相对，三维球上不同的一致正有界可测标量电导率可以有相同的全边界数据。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/365.md)）

&emsp;[Determination of a metric and a unitary connection from one boundary patch](https://github.com/openai/math/blob/main/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf)

&emsp;[Smooth anisotropic uniqueness in the Calderón problem from one boundary patch](https://github.com/openai/math/blob/main/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf)

&emsp;[Nonuniqueness for bounded measurable scalar conductivities in three dimensions](https://github.com/openai/math/blob/main/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf)

**366. 平面 Mumford–Shah 正则性猜想与局部弱 <i>L</i>⁴ 梯度界。** 解决带界保真数据的既约绝对平面 Mumford–Shah 极小化子的内部正则性猜想。局部地，闭间断集是 $`C^{1,\alpha}`$ 弧、正则裂纹尖或三弧 $`120^\circ`$ 相接；每个紧内部区域只遇到有限多个整体连通分支。

&emsp;[Interior regularity of planar Mumford–Shah minimizers](https://github.com/openai/math/blob/main/preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026.pdf)

**367. 单相 Bernoulli 问题的临界维数。** 确立 7 为第一个容许非平坦一齐次整体极小化子的维数（单相 Bernoulli 能量）。因此极小化自由边界在六维以下光滑，更高维数中奇异集维数至多 <i>n</i>−7。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/367.md)）

&emsp;[The critical dimension for one-phase Bernoulli minimizers](https://github.com/openai/math/blob/main/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf)

**368. 三维 Ball–Evans 逼近问题。** 解决三维 Ball–Evans 逼近问题：ℝ³ 中任意有界域之间的每个 $`W^{1,p}`$ 同胚（$`1\le p\lt \infty`$）都是光滑微分同胚（映到同一靶域）的强 $`W^{1,p}`$ 极限。

&emsp;[Strong diffeomorphic approximation in three dimensions for 1≤p≤2](https://github.com/openai/math/blob/main/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf)

&emsp;[Strong diffeomorphic approximation in three dimensions for p>2](https://github.com/openai/math/blob/main/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf)

**369. 单连通平面域的热点猜想。** 证明 Burdzy 单连通热点猜想的严格形式。在每张光滑有界单连通平面域上，第一正 Neumann 特征值的每个非零特征函数都没有内部临界点，故全部全局极值在边界上。允许特征值重数。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/369.md)）

&emsp;[Strict hot spots and absence of interior critical points on smooth simply connected planar domains](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf)

**370. Lane–Emden 与 Hénon–Lane–Emden 猜想。** 解决次临界 Lane–Emden 猜想及其加权 Hénon 扩展。对 <i>n</i> ≥ 2、<i>p,q</i> &gt; 0 与实 <i>A</i>、<i>B</i>，当 $`(n+A)/(p+1)+(n+B)/(q+1)\gt n-2`$ 时，方程组 $`-\Delta u=|x|^A v^p`$、$`-\Delta v=|x|^B u^q`$ 无正整体解（在原点连续、其余处经典）。无需对称性或增长假设。已知径向存在性给出 <i>n</i> ≥ 3、<i>A,B</i> &gt; −2 的精确存在判据。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/370.md)）

&emsp;[The Subcritical Hénon–Lane–Emden Conjecture](https://github.com/openai/math/blob/main/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf)

**371. 散焦薛定谔方程的稳定爆破。** 对足够大的奇非线性幂，构造 $`H^k(\mathbb T^{12})`$（<i>k</i> &gt; 8）中非空开集的初值：其标量散焦非线性薛定谔方程的解在有限时间爆破。即在此超临界情形，有限时间爆破在 Sobolev 扰动下稳定。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/371.md)）

&emsp;[Stable self-similar blowup for a supercritical defocusing Schrödinger equation on the torus](https://github.com/openai/math/blob/main/preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/paper.pdf)

**372. 光滑各向同性弹性的整体唯一性。** 证明：只要 <i>μ</i> &gt; 0 且 $`3\lambda+2\mu\gt 0`$ 在闭包上成立，完整的静态边界位移到牵引数据就确定 ℝ³ 中每个有界连通光滑域上的光滑实 Lamé 模量。不需要解析性、接近常系数或边界附近的先验知识。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/372.md)）

&emsp;[Global Uniqueness for the Smooth Isotropic Elasticity Inverse Problem](https://github.com/openai/math/blob/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf)

**373. 三边际库仑 Monge 问题的不可达性。** 最优三粒子库仑构形不必是第一个粒子的确定性函数，即使对光滑恒同空间密度。Monge 与 Kantorovich 下确界相等，但 Monge 下确界不可达。同样现象出现在每个维数至少二的每个逆幂 Riesz 指数处（各配适当密度）。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/373.md)）

&emsp;[A counterexample to the Monge ansatz for the three-marginal Coulomb cost](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/paper.pdf)

**374. Brenier 映射的锐利三分之一稳定性。** 对维数至少 2、内部非空的紧凸体上的均匀源测度 <i>ρ</i>，二次最优输运映射满足 $`\|T_\mu-T_\nu\|_{L^2(\rho)}\le C W_2(\mu,\nu)^{1/3}`$（目标在固定紧集上一致）。指数锐利，即使对三原子目标，否定 Letrouit 猜测的平方根界。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/374.md)）

&emsp;[Sharp One-Third Stability of Brenier Maps](https://github.com/openai/math/blob/main/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/article.pdf)

**375. 八维的 De Giorgi 猜想。** 在其锐利的八维端点证明 De Giorgi 猜想：$`\Delta u=u^3-u`$ 的每个沿一个方向严格递增的整体 <i>C</i>² 解 $`u:\mathbb R^8\to(-1,1)`$ 只依赖一个线性坐标。更强的定理把所有稳定整体解 $`v:\mathbb R^7\to[-1,1]`$ 分类为常值井或平面过渡，无需能量增长假设。

&emsp;[A positive resolution of De Giorgi's conjecture in dimension eight](https://github.com/openai/math/blob/main/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf)

**376. 受迫 Navier–Stokes 流中的普适计算。** 构造从静止开始在固定平坦三维域上的黏性不可压缩流：在光滑外力下执行普适计算。一个终止编译器把图灵机与输入转为外力的有限程序，使指定粒子恰在机器停机时到达固定区域。黏度固定、正且可计算。（[Lean 形式化](https://github.com/openai/math/blob/main/lean/docs/376.md)）

&emsp;[Finite Instructions and Solenoidal Shear Flows](https://github.com/openai/math/blob/main/preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/manuscript.pdf)

&emsp;[A Fixed Particle Test for Computation in a Forced Viscous Flow](https://github.com/openai/math/blob/main/preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/manuscript.pdf)

&emsp;[Universal Computation with Eventually Stationary Navier–Stokes Forcing](https://github.com/openai/math/blob/main/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf)

&emsp;[Geometric Programs for Solenoidal Forcing](https://github.com/openai/math/blob/main/preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/manuscript.pdf)

&emsp;[Prefix Instructions and Incompressible Flows](https://github.com/openai/math/blob/main/preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/manuscript.pdf)

&emsp;[Computation under Rapidly Vanishing Navier–Stokes Forcing](https://github.com/openai/math/blob/main/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf)

&emsp;[Velocity-Field Detection of Computation in Forced Navier–Stokes Flows](https://github.com/openai/math/blob/main/preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/manuscript.pdf)

&emsp;[Scalar Potentials and Slow Clocks for Forced Fluid Computation](https://github.com/openai/math/blob/main/preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/manuscript.pdf)

&emsp;[Incompressible Box Transport and Finite Computation](https://github.com/openai/math/blob/main/preprints/Incompressible-Box-Transport-and-Finite-Computation-September-27-2026/manuscript.pdf)

**377. 无穷调和函数的内部 $`C^{1,\alpha}`$ 正则性。** 证明每个维数 <i>d</i> ≥ 3 中有界无穷调和函数的一致内部 $`C^{1,\alpha_d}`$ 正则性（正指数只依赖维数）。梯度在半单位球上的上确界范数与 Hölder 半范数由单位球上振荡的维数相关常数倍界定。指数非显式。

&emsp;[Uniform Interior $`C^{1,\alpha}`$ Estimates for Infinity-Harmonic Functions](https://github.com/openai/math/blob/main/preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/interior-c1-infinity-harmonic.pdf)

---

