# 数学术语中英对照表（Glossary）

> 本表是本仓库全部翻译的**术语基准**。译者在翻译任何条目前，请先查此表；表中有「裁决」标注的词按裁决译法执行。
> 译法参考全国科学技术名词审定委员会审定名词及主流数学文献惯例。

---

## 一、通用高频词（跨学科）

| 英文 | 中文 | 备注 / 裁决 |
|---|---|---|
| conjecture | 猜想 | 「XX conjecture」一律译「XX 猜想」 |
| counterexample | 反例 | |
| proof / proof sketch | 证明 / 证明思路 | |
| result family | 成果族 | 上游将相关手稿归为一「family」，本仓库译「成果族」 |
| manuscript | 手稿 | 不译「论文」（未经同行评审） |
| bound / lower bound / upper bound | 界 / 下界 / 上界 | 「sharp bound」→「最优界」 |
| sharp / optimal | 最优的 / 最优的 | sharp 优先译「最优」，指达到极端情形时译「达到极值」 |
| asymptotic | 渐近 | |
| uniform / uniformly | 一致 / 一致地 | 如 uniform bound → 一致界 |
| explicit | 显式 | |
| effective | 有效 | 指给出可计算常数时 |
| finite / infinite | 有限 / 无限 | |
| finitely generated | 有限生成 | |
| classification | 分类 | |
| rigidity | 刚性 | |
| stability | 稳定性 | |
| universality | 普适性 | 概率/物理语境 |
| threshold | 阈值 | 随机图语境亦作「阈值」 |
| exponent | 指数 | |
| entropy | 熵 | |
| approximation | 近似 | |
| algorithm / decidable | 算法 / 可判定 | |
| smooth | 光滑 | |
| singularity | 奇点 | |
| local / global | 局部 / 整体 | |
| mixing | 混合 | 遍历论语境 |
| gap | 间隙 / 缺口 | 谱间隙 →「谱隙」 |
| distribution | 分布 | |
| density (one) | 密度（为一） | |
| corank | 余秩 | |
| formalization | 形式化 | Lean 形式化 = 用 Lean 证明助手验证 |
| zero-free (region/half-plane) | 无零点（区域/半平面） | **裁决**：不译「零自由」 |
| embedding | 嵌入 | |
| refinement | 加细 | |
| realization | 实现(matrix) 不译 | 一般语境译「实现」；Galois 表示语境保留不译按惯例 |
| reduction (of an abelian variety) | 约化 | 「good reduction」→「好约化」 |

## 二、数论（Number theory）

| 英文 | 中文 |
|---|---|
| Riemann zeta function | 黎曼 ζ 函数 |
| Dirichlet *L*-function | 狄利克雷 *L* 函数 |
| Hecke *L*-function | 赫克 *L* 函数 |
| quasi-Riemann hypothesis | 准黎曼猜想 |
| zero-free half-plane | 无零点半平面 |
| Landau–Siegel zero | 兰道–西格尔零点 |
| elliptic curve | 椭圆曲线 |
| Birch–Swinnerton-Dyer (BSD) formula | BSD 公式（Birch–Swinnerton-Dyer 公式） |
| Mordell–Weil rank | Mordell–Weil 秩 |
| Selmer group | 塞尔默群（Selmer 群） |
| Tate–Shafarevich group | Tate–Shafarevich 群（沙法列维奇–泰特群） |
| quadratic twist | 二次扭曲 |
| isogeny | 同源 |
| Hilbert's tenth problem | 希尔伯特第十问题 |
| Diophantine (equation/problem) | 丢番图（方程/问题） |
| arithmetic progression | 等差数列 |
| multiplicative function | 乘性函数 |
| irrationality exponent | 无理性指数 |
| modular form | 模形式 |
| partition | 分拆（整数分拆） |
| prime gap | 素数间隙 |
| circle method | 圆法 |

## 三、代数与表示论（Algebra / Group theory / Operator algebras）

| 英文 | 中文 |
|---|---|
| abelian variety | 阿贝尔簇 |
| Hodge class / Hodge conjecture | Hodge 类 / Hodge 猜想（霍奇猜想） |
| algebraic cycle | 代数闭链 |
| crystalline (cohomology) | 晶状（上同调） |
| Galois representation | 伽罗瓦表示 |
| Kaplansky (direct-finiteness) conjecture | Kaplansky（直有限性）猜想 |
| free group factor | 自由群因子 |
| von Neumann algebra | 冯·诺依曼代数 |
| C*-algebra | C* 代数 |
| operator algebra | 算子代数 |
| representation | 表示 |
| module | 模 |
| Lie algebra | 李代数 |
| simple group | 单群 |
| word problem | 字问题 |
| residual finiteness | 剩余有限性 |

## 四、几何与拓扑

| 英文 | 中文 |
|---|---|
| Kähler (manifold/metric) | Kähler（流形/度量）（凯勒） |
| Calabi–Yau | Calabi–Yau（卡拉比–丘） |
| minimal surface | 极小曲面 |
| mean curvature | 平均曲率 |
| Ricci curvature / flow | Ricci 曲率 / Ricci 流（里奇曲率/里奇流） |
| scalar curvature | 数量曲率 |
| sectional curvature | 截面曲率 |
| nonnegative curvature | 非负曲率 |
| geodesic | 测地线 |
| isoperimetric (inequality/problem) | 等周（不等式/问题） |
| Cartan–Hadamard conjecture | 卡当–阿达马猜想（Cartan–Hadamard 猜想） |
| CAT(0) space | CAT(0) 空间（保留记号） |
| filling (integral filling) | 填充（积分填充） |
| current (integral current) | 积分流（积分电流）— geometric measure theory 语境译「积分流」 |
| Hausdorff dimension | 豪斯多夫维数 |
| Kakeya (conjecture/set) | 挂谷（猜想/集合） |
| Besicovitch set | 贝西科维奇集 |
| manifold | 流形 |
| 3-manifold | 三维流形 |
| knot / link | 纽结 / 链环 |
| homotopy / homology | 同伦 / 同调 |
| hyperbolic (space/group) | 双曲（空间/群） |
| cover / covering | 覆盖 |
| triangulation | 三角剖分 |
| planar graph | 平面图 |

## 五、分析（Real and complex analysis / Functional analysis / PDE）

| 英文 | 中文 |
|---|---|
| harmonic analysis | 调和分析 |
| Fourier transform | 傅里叶变换 |
| restriction (problem/theory) | 限制（问题/理论） |
| decoupling | 解耦 |
| oscillatory integral | 振荡积分 |
| maximal function | 极大函数 |
| singular integral | 奇异积分 |
| Lipschitz (function/constant) | Lipschitz（函数/常数）（利普希茨） |
| Sobolev (space/inequality) | Sobolev（空间/不等式）（索博列夫） |
| Banach space | 巴拿赫空间 |
| Hilbert space | 希尔伯特空间 |
| Navier–Stokes (equations) | 纳维–斯托克斯（方程） |
| Euler equations | 欧拉方程 |
| Vlasov–Maxwell (system) | Vlasov–Maxwell（方程组）（弗拉索夫–麦克斯韦） |
| mild solution | 温和解 |
| blow-up | 爆破 |
| well-posedness | 适定性 |
| regularity | 正则性 |
| weak solution | 弱解 |
| energy estimate | 能量估计 |

## 六、概率与统计力学（Probability / Statistical mechanics）

| 英文 | 中文 |
|---|---|
| random walk | 随机游走 |
| Brownian motion | 布朗运动 |
| percolation | 渗流 |
| Gaussian (process/free field) | 高斯（过程/自由场） |
| concentration (inequality) | 集中（不等式） |
| Ising model | 伊辛模型（Ising 模型） |
| spin glass | 自旋玻璃 |
| Mézard–Parisi formula | Mézard–Parisi 公式 |
| Heisenberg ferromagnet | 海森堡铁磁体 |
| spontaneous magnetization | 自发磁化 |
| first-passage percolation | 首达渗流 |
| KPZ (universality) | KPZ（普适性） |
| Dyson Brownian motion | 戴森布朗运动 |
| invariant measure | 不变测度 |
| ergodic (theory) | 遍历（理论） |
| mixing | 混合 |
| large deviations | 大偏差 |
| martingale | 鞅 |

## 七、组合与图论（Combinatorics）

| 英文 | 中文 |
|---|---|
| Ramsey (theory/number) | 拉姆齐（理论/数）（Ramsey） |
| Szemerédi (regularity) | Szemerédi（正则性）（塞迈雷迪） |
| arithmetic combinatorics | 加法组合 |
| extremal (graph theory) | 极值（图论） |
| hypergraph | 超图 |
| design | 设计（组合设计） |
| packing / covering | 填装 / 覆盖 |
| chromatic number | 色数 |
| independence number | 独立数 |
| expander (graph/mixing) | 扩展图（扩张图）/ 扩展混合 |
| quasirandom | 拟随机 |
| progression-free | 无等差数列的 |
| sum-free | 无和集的 |
| Sidon set | Sidon 集（西顿集） |
| corner / polygon (free) | 角 / 多边形（无……的） |

## 八、理论计算机科学（Theoretical computer science）

| 英文 | 中文 |
|---|---|
| NP-hardness / NP-hard | NP 难度 / NP 难的 |
| Unique Games conjecture | 唯一游戏猜想（Unique Games 猜想） |
| semidefinite programming (SDP) | 半定规划 |
| approximation ratio | 近似比 |
| matrix multiplication exponent | 矩阵乘法指数 |
| dual exponent | 对偶指数 |
| communication complexity | 通信复杂度 |
| circuit complexity | 电路复杂度 |
| data structure | 数据结构 |
| dynamic (graph) algorithm | 动态（图）算法 |
| streaming algorithm | 流式算法 |
| property testing | 性质测试 |
| PCP (theorem) | PCP（定理） |
| hard(ness of approximation) | 难解性（近似难解性） |
| quantum (query/complexity) | 量子（查询/复杂度） |

## 九、动力系统与数学物理（Dynamical systems / Math physics）

| 英文 | 中文 |
|---|---|
| ergodic theory | 遍历理论 |
| billiard | 台球系统（billiard） |
| Anosov (flow/diffeomorphism) | Anosov（流/微分同胚） |
| hyperbolicity | 双曲性 |
| invariant (measure/set) | 不变（测度/集） |
| quantum (chaos/spectrum) | 量子（混沌/谱） |
| spectral gap | 谱隙 |
| scattering | 散射 |
| soliton | 孤子 |

## 十、人名译法裁决

**人名保留原文不译**：Kähler, Sobolev, Lipschitz, Ramsey, Szemerédi, Anosov, Kaplansky, Selmer, Mordell, CAT(0), KPZ, Mézard–Parisi, Vlasov 等无通行审定译名或译名不统一的，保留原文。
**采用通行译名**：黎曼、狄利克雷、赫克、椭圆、丢番图、纳维–斯托克斯、欧拉、傅里叶、巴拿赫、希尔伯特、豪斯多夫、挂谷、贝西科维奇、伊辛、海森堡、戴森、拉姆齐、渗流、遍历。
**特殊裁决**：
- 「zero-free」一律译「无零点」；
- 「sharp」一律译「最优」（不译「锐利」）；
- 「manuscript」一律译「手稿」（不译「论文」）；
- 「result family」一律译「成果族」；
- 积分流语境的「current」译「积分流」（geometric measure theory）。
