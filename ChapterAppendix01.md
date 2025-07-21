
# 随机过程的基本概念

随机过程（stochastic process）
: 随机过程就是指一族随机变量 $\{X(t),t\in \mathcal{T}\}$ ，其中 $t$ 是参数，该参数属于某个指标集 $\mathcal{T}$ ，称 $\mathcal{T}$ 为参数集。

```{admonition} Remark

- 当 $\mathcal{T} = \{1,2,\cdots\}$ 时，也称随机过程为随机序列。
- 随机变量是样本点的函数。 $X(t)$ 是随 $t$ 和 $\omega \in \Omega$ 而变化的，也可以记作 $X(t,\omega)$ 。

- 固定 $\omega_0$ ， $X(t,\omega_0)$ 是 $t$ 的函数；
- 固定 $t_0$ ， $X(t_0,\omega)$ 是一个随机变量。

- 随机过程在时刻 $t$ 取的值称为过程所处的状态，状态的全体称为状态空间。
- 根据状态空间可分为连续状态和离散状态；
- 根据参数集 $\mathcal{T}$ ，当 $\mathcal{T}$ 为有限集或可列集时，该随机过程称为离散参数过程；否则称为连续参数过程；
- 当 $\mathbf{t}$ 是高维向量时，则称 $X(\mathbf{t})$ 是随机场。

```

类似于随机变量的分布函数的定义，以下我们给出随机过程的分布定义。

一维分布
: 对于随机过程 $\{N(t),t\in \mathcal{T}\}$ ，称

$$
F_t(x) = P(X(t)\leq x)
$$

为过程的一维分布。

有限维分布族
: 对于任意 $t_1,t_2,\cdots,t_n \in \mathcal{T}$ ，称

$$
F_{t_1,t_2,\cdots,t_n}(x_1,x_2,\cdots,x_n) = P(X(t_1)\leq x_1,X(t_2)\leq x_2,\cdots,X(t_n)\leq x_n)
$$

为过程的有限维分布族。

随机过程的有限维分布族就是过程 $\{X(t),t\in\mathcal{T}\}$ 中任意 $n$ 个随机变量的联合分布，其满足对称性和相容性。

`````{prf:property}

- （对称性）过程的有限维分布族与变量 $X(t_1),\cdots,X(t_n)$ 的排序无关，即对 $\{1,\cdots,n\}$ 的任一置换 $(i_1,\cdots,i_n)$ 有

$$
F_{t_{i_1},\cdots,t_{i_n}}(x_{i_1},\cdots,x_{i_n}) = F_{t_1,\cdots,t_n}(x_1,\cdots,x_n).
$$

- (相容性）高维分布的边际分布与相应的低维分布一致，即对任意 $m< n$ ，有

$$
F_{t_1,\cdots,t_{m},t_{m+1},\cdots,t_{n}}(x_1,\cdots,x_m,\infty,\cdots,\infty) = F_{t_1,\cdots,t_m}(x_1,\cdots,x_m).
$$

`````

除了对过程分布的定义，我们也可以定义过程的数字特征。

- 称过程的期望 $E(X(t))$ 为过程的均值函数，记作 $\mu_{X}(t)$ ；
- 称 $\text{Var}(X(t))$ 为过程的方差函数；
- 称 $E(X(t_1)X(t_2))$ 为过程的自相关函数，记为 $r_{X}(t_1,t_2)$ ；
- 称 $\text{Cov}(X(t_1),X(t_2)) = E((X(t_1)-\mu_{X}(t_1))(X(t_2)-\mu_{X}(t_2)))$ 为协方差函数，记为 $R_{X}(t_1,t_2)$ ；

``````{prf:theorem}
协方差函数是非负定的，即对任何 $t_1,t_2,\cdots,t_n \in \mathcal{T}$ 及任意实数 $b_1,b_2,\cdots,b_n$ ，恒有

$$
\sum_{i=1}^n \sum_{j=1}^n b_ib_j R_{X}(t_i,t_j) \geq 0
$$

``````

严平稳
: 如果随机过程 $X(t)$ 满足对任意的 $t_1,t_2,\cdots,t_n\in \mathcal{T}$ 和任意 $h$ 有

$$
(X(t_1+h), \cdots,X(t_n+h)) \overset{d}{=} (X(t_1),\cdots,X(t_n))
$$

则称该过程为严平稳的。

宽平稳
: 如果随机过程 $X(t)$ 的所有二阶矩存在并有 $E(X(t))=m$ 及协方差函数 $R_X(t,s)$ 只与时间差 $t-s$ 有关，则称该过程为宽平稳的或二阶矩平稳的。

平稳独立增量的过程
: 如果对任意的 $t_1<t_2<\cdots<t_n,t_1,\cdots,t_n\in \mathcal{T}$ ，随机变量 $X(t_2)-X(t_1),X(t_3)-X(t_2),\cdots,X(t_n)-X(t_{n-1})$ 是相互独立的，则称 $X(t)$ 为独立增量过程。如果进一步有对任意的 $t_1,t_2$ ，

$$
X(t_1+h) - X(t_1) \overset{d}{=} X(t_2+h) - X(t_2)
$$

则称 $X(t)$ 为平稳独立增量的过程。