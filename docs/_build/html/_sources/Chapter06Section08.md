# 习题

1.  `计算题` 设随机变量 $X$ 的密度函数为

    $$ p(x) = \begin{cases}
    a + bx^2, & 0\leq x\leq 1\
    0, & \text{其他}.
    \end{cases}
    $$

    如果 $E(X) = 2/3$ ,求 $a$ 和 $b$ 。

2.  `计算题` 设随机变量 $X$ 的分布函数为

    $$
    F(x) = 1- e^{-x^2},x > 0
    $$

    试求 $E(X)$ 和 $\text{Var}(X)$ 。

3.  `计算题` 设随机变量 $X \sim U(a,b)$ ，对 $k = 1,2,3,4$ ，求：
    - $\mu_k = E(X^k)$ 与 $\upsilon_k = E(X - E(X))^k$ ；
    - 偏度系数和峰度系数。

4.  `计算题` 设随机变量 $X$ 服从双参数韦布尔分布，其分布函数为

    $$
    F(x) = 1-\exp \left \{-\left (\frac{x}{\eta} \right )^m \right \}, x>0,
    $$

    其中 $\eta > 0,m > 0$ 。试求：
    - 该分布的 $p$ 分位数 $x_p$ 的表达式；
    - 当 $m = 1.5,\eta = 1000$ 时的 $x_{0.1},x_{0.5},x_{0.8}$ 的值。

5.  `自主练习` 请根据常见分布的分布列或密度函数，计算其期望和方差。

```{list-table} 常见分布的分布列（密度函数）及其期望与方差
:header-rows: 1
:name: tab-common-distributions
* - 分布
  - 分布列/密度函数
  - 期望
  - 方差
* - 二项分布 $b(n,p)$
  - $P(X=x) = \frac{n!}{x!(n-x)!} p^x (1-p)^{n-x}, x = 0,1, \cdots,n$
  - $np$
  - $np(1-p)$
* - 泊松分布 $P(\lambda)$
  - $P(X=x) = \frac{\lambda^x}{x!} e^{-\lambda }, x = 0,1, \cdots$
  - $\lambda$
  - $\lambda$
* - 负二项分布 $Nb(r,p)$
  - $P(X=x) = \frac{(x-1)!}{(r-1)!(x-r)!} (1-p)^{x-r}p^r, x = r,r+1, \cdots$
  - $\frac{r}{p}$
  - $\frac{r(1-p)}{p^2}$
* - 正态分布 $N(\mu,\sigma^2)$
  - $p(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\{-\frac{(x-\mu)^2}{2\sigma^2}\}, -\infty <x <\infty$
  - $\mu$
  - $\sigma^2$
* - 均匀分布 $U(a,b)$
  - $p(x) = \frac{1}{b-a}, a<x<b$
  - $\frac{a+b}{2}$
  - $\frac{(b-a)^2}{12}$
* - 伽马分布 $Ga(\alpha,\lambda)$
  - $p(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha -1} \exp\{-\lambda x\}, x \geq 0$
  - $\frac{\alpha}{\lambda}$
  - $\frac{\alpha}{\lambda^2}$
* - 贝塔分布 $Be(a,b)$
  - $p(x) = \frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)} x^{a-1} (1-x)^{b-1}, 0<x<1$
  - $\frac{a}{a+b}$
  - $\frac{ab}{(a+b)^2(a+b+1)}$
```