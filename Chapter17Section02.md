# 三种分布的构造方式
在本讲中，首先我们介绍三种“新”的分布，这些分布都来自于用于估计和检验任务中常见的统计量。与之前学习思路不同，这些分布并不是来自于伯努利实验，也并不是通过数学推导而得的。这些分布是构造出来的，我们需要关注于这三个分布的构造方式。
## 卡方分布
在第 6 讲中，我们已经证明了一个命题：标准正态分布 $X\sim N(0,1)$ ，则 $X^2 \sim Ga(1/2,1/2)$ 。我们将 $Ga(1/2,1/2)$ 命名为卡方分布 $\chi^2(1)$ 。另外，在第 9 讲中，我们也已经证明了一个命题：伽马分布具有可加性。于是，如果 $Y_1,Y_2,\cdots,Y_n$ 独立同分布于 $Ga(1/2,1/2)$ ，那么

$$
\sum_{i=1}^n Y_i \sim Ga(n/2,1/2).
$$

我们将 $Ga(n/2,1/2)$ 命名为自由度为 $n$ 的卡方分布，即 $\chi^2(n)$ 。于是，我们可以有以下定义。

设 $X_1,X_2,\cdots,X_n$ 独立同分布于标准正态分布 $N(0,1)$ ，则称

$$
\chi^2 = X_1^2 + X_2^2 + \cdots + X_n^2 = \sum_{i=1}^n X_i^2
$$

的分布为自由度为 $n$ 的 $\chi^2$ 分布，记为 $\chi^2 \sim \chi^2(n)$ 。

根据伽马分布的期望和方差公式，我们知道，如果 $\chi^2 \sim \chi^2(n)$ ，那么

$$
\begin{eqnarray*}
E(\chi^2) &=& n\\
\text{Var}(\chi^2) &=& 2n
\end{eqnarray*}
$$

以下两个分布是建立在卡方分布之上。
## $F$ 分布

 $F$ 分布
: 设随机变量 $X_{1}\sim \chi^{2}(m),X_{2}\sim \chi^{2}(n)$ ，且 $X_{1}$ 与 $X_{2}$ 独立，则称

$$F=\frac{X_{1} /m }{X_{2}/n}$$

的分布是自由度为 $m$ 与 $n$ 的 $F$ 分布，记为 $F(m,n)$ 。其中， $m$ 为分子自由度， $n$ 为分母自由度。

```{admonition} Remark

- 根据增补变换法，可以推导 $F$ 的密度函数为

$$
p_F(y) = \frac{\Gamma\left(\frac{m+n}{2}\right) \left(\frac{m}{n}\right)^{\frac{m}{2}} }{\Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right)} y^{\frac{m}{2}-1} \left(1+\frac{m}{n}y\right)^{-\frac{m+n}{2}}, y>0.
$$

- 通过图像绘制， $F$ 分布是一个偏态分布。
- 易证：若 $F \sim F(m,n)$ ，则 $1/F \sim F(n,m)$ ；
- $F$ 分布分布数的性质。若 $F_{\alpha}(m,n)$ 为自由度为 $m$ 和 $n$ 的 $F$ 分布分位数。于是，若存在一个随机变量 $F \sim F(m,n)$ ，则 $1/F$ 也是一个 $F$ 分布随机变量，其自由度分别为 $n$ 和 $m$ 。所以，

$$
\alpha = P\left(\frac{1}{F}\leq F_{\alpha}(n,m)\right)
= P\left(F \geq \frac{1}{F_{\alpha}(n,m)}\right),
$$

从而

$$
P\left( F \leq \frac{1}{F_{\alpha}(n,m)}\right) =1-\alpha.
$$

因此，

$$
F_{1-\alpha} (m,n) = \frac{1}{F_{\alpha}(n,m)}.
$$

```

## $t$ 分布

$t$ 分布
: 设随机变量 $X_1$ 与 $X_2$ 独立且 $X_1\sim N(0,1),X_2\sim \chi^2(n)$ ，则称

$$t=\frac{X_{1}}{\sqrt{X_{2}/n } } $$

的分布为自由度为 $n$ 的 $t$ 分布，记为 $t\sim t(n)$ 。

```{admonition} Remark

- 根据增补变换法，可以推导 $t$ 的密度函数为

$$
p_t(y) = \frac{\Gamma\left(\frac{n+1}{2} \right)}{\sqrt{n\pi}\Gamma\left(\frac{n}{2}\right)} \left(1 + \frac{y^2}{n}\right)^{-\frac{n+1}{2}}, -\infty < y < \infty.
$$

- $t$ 分布的密度函数 vs 标准正态分布的密度函数。

- $t$ 分布的密度函数和标准正态分布的密度函数均为偶函数，形状类似。
- 特别当 $n$ 比较小时，尾部概率比标准正态分布的大一些。

```