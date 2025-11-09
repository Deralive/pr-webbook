# 有限样本的评估方式——均方误差
在评估估计方法时，一个非常直观的想法是比较我得到的估计值与真实值之间的差异。如果差异越小，估计方法越好。而我们所得到的估计值本身是样本的函数，不仅仅依赖于函数的构造（估计方法），也依赖于样本的质量。我们采取了“平均化”的策略尽可能地消除样本所造成的影响。于是，我们构建了以下指标——均方误差。

均方误差
: 若 $\hat{\theta}$ 是参数 $\theta$ 的一个估计。称

$$
\text{MSE}(\hat{\theta}) = E(\hat{\theta}-\theta)^2
$$

为 $\hat{\theta}$ 的均方误差（Mean Squared Error, MSE）。

```{admonition} Remark
均方误差是评价点估计的最一般的标准。希望点估计的均方误差越小越好。
```

通过分解，我们可以发现

$$
\begin{eqnarray*}
\text{MSE}(\hat{\theta})&=& E(\hat{\theta}-\theta)^{2} \\
&=& E(\hat{\theta}-E(\hat{\theta})+E(\hat{\theta})-\theta)^{2} \\
&=& E(\hat{\theta}-E(\hat{\theta}))^{2}+2 E(\hat{\theta}-E(\hat{\theta})) \cdot(E(\hat{\theta})-\theta) +E(E(\hat{\theta})-\theta)^{2}
\\
&=& E(\hat{\theta}-E(\hat{\theta}))^{2} +(E(\hat{\theta})-\theta)^{2}
\end{eqnarray*}
$$

其中，最后一个等式成立，是因为交叉项 $E\left((\hat{\theta}-E(\hat{\theta})) \cdot(E(\hat{\theta})-\theta) \right)=0$ 。

```{admonition} Remark
点估计的均方误差可以分解为两个部分：

- $E(\hat{\theta}-E(\hat{\theta}))^{2}$ 可记为 $\text{Var}(\hat{\theta})$ ，表示点估计的方差；
- $(E(\hat{\theta})-\theta)^{2}$ 可记为 $\text{Bias}^2(\hat{\theta})$ ，表示点估计偏差的平方。

```

## 无偏性
估计的无偏性是最常见的性质，它是重要的，但不是必要的。

无偏性
: 设 $\theta$ 是我们待估计的参数，而 $\hat{\theta}$ 是 $\theta$ 的一个点估计。如果 $\hat{\theta}$ 满足

$$
E_{\theta} (\hat{\theta}) = \theta, \theta \in \theta.
$$

则称 $\hat{\theta}$ 是 $\theta$ 的无偏估计（Unbiased Estimate，U.E.）。

```{admonition} Remark
倘若一个点估计是无偏估计，这个点估计的偏差为零，即 $E_{\theta} (\hat{\theta}) -\theta =0$ ；而与无偏估计相对，我们统一地称不具有无偏估计的估计是有偏估计。
```

`````{prf:example}
若总体分布为一个未知分布，其分布函数记为 $F(x)$ 。设其期望为 $\mu$ ，即 $E(X) = \mu$ ，方差为 $\sigma^2$ ，即 $\text{Var}(X) =\sigma^2$ 。现有样本 $x_1,x_2,\cdots,x_n$ 。
通常，样本均值 $\bar{x}$ 是总体均值 $\mu$ 的一个估计。我们可以计算 $\bar{x}$ 的期望，即

$$
\begin{eqnarray*}
E(\bar{x}) &=& E\left( \frac{1}{n} \sum_{i=1}^{n} x_{i} \right)\\
&=& \frac{1}{n} \sum_{i=1}^{n} E\left(x_{i}\right)\\
&=&\mu.
\end{eqnarray*}
$$

于是， $\bar{x}$ 是 $\mu$ 的无偏估计。
而样本方差 $s^2 = \frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}$ 来估计总体方差。我们可以计算 $s_n^2$ 的期望，即

$$
\begin{eqnarray*}
E(s_n^2) = \frac{n-1}{n} \sigma^{2} \neq \sigma^2.
\end{eqnarray*}
$$

于是， $s_n^2$ 不是 $\sigma^2$ 的无偏估计。
因为 $E\left(s_{n}^{2}\right)=\frac{n-1}{n} \sigma^{2}$ ， $S_{n}^{2}$ 不是无偏估计。 但易于证明 $s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i-\bar{x})^2$ 是 $\sigma^2$ 的无偏估计。


```{admonition} Remark
:class: dropdown
回看样本方差 $s_n^2$ ，这个估计量的偏差为

$$
-\frac{1}{n}\sigma^2 .
$$

当样本量 $n$ 越大时， $s_n^2$ 的偏差越接近 0，而 $s_n^2$ 的期望也越接近 $\sigma^2$ 。于是，我们称 $s_n^2$ 是 $\sigma^2$ 的**渐近无偏**估计。
```
`````

```{admonition} Question
总体标准差 $\sigma$ 的无偏估计会是怎样的？样本标准差 $s$ 是 $\sigma$ 的无偏估计吗？
```

`````{prf:example}
考虑总体分布为 $N(\mu,\sigma^2)$ ， $\mu$ 和 $\sigma^2$ 均是待估参数。现有样本 $x_1,x_2,\cdots,x_n$ 。已知样本方差 $s^2$ 为

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i-\bar{x})^2.
$$

而样本标准差 $s = \sqrt{s^2}$ 。
为计算 $s$ 的期望，我们先来回顾一下 $s^2$ 的分布。我们知道在正态分布假定下，

$$
\frac{(n-1)s^2}{\sigma^2} \sim \chi^2(n-1) = Ga((n-1)/2,1/2)。
$$

因为 $s = (s^2)^{1/2}$ ，我们来看待一般的伽马分布 $Y \sim Ga(\alpha,\gamma)$ 的 $k$ 阶矩的期望。

$$
\begin{eqnarray*}
E(Y^{k}) &=& \int_{0}^{\infty} y^{k} \frac{\lambda^{\alpha}}{\Gamma(\alpha)} y^{\alpha - 1} \exp\{-\lambda y\} \text{d} y\\
&=& \int_{0}^{\infty} \frac{\lambda^{\alpha}}{\Gamma(\alpha)} y^{k+\alpha - 1} \exp\{-\lambda y\} \text{d} y\\
&=&\frac{\lambda^{\alpha}}{\Gamma(\alpha)}\frac{\Gamma(\alpha + k)} {\lambda^{\alpha +k}} \int_{0}^{\infty} \frac{\lambda^{\alpha +k}}{\Gamma(\alpha + k)} y^{k+\alpha - 1} \exp\{-\lambda y\} \text{d} y\\
&=& \frac{\Gamma(\alpha + k)}{\Gamma(\alpha)} \cdot \lambda^{-k}.
\end{eqnarray*}
$$

于是，

$$
E(s) = E\left((s^2)^{1/2}\right) = \frac{\Gamma\left(\frac{n-1}{2}+\frac{1}{2}\right)}{\Gamma(\frac{n-1}{2})} \cdot \left(\frac{1}{2}\right)^{-1/2}
$$

即

$$
\frac{\sqrt{n-1}}{\sigma} E(s) = \frac{\Gamma\left(\frac{n}{2}\right)}{\Gamma(\frac{n-1}{2})} \cdot \left(\frac{1}{2}\right)^{-1/2}
$$

因此，

$$
E(s) = \sqrt{\frac{2}{n-1}} \frac{\Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{n-1}{2}\right)} \sigma .
$$

而 $c_n = \left(\sqrt{\frac{2}{n-1}} \frac{\Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{n-1}{2}\right)}\right)^{-1}$ 就是修偏系数。当 $n$ 充分大时，这个修偏系数接近 1。于是在实际使用时，我们通常忽略这个修偏系数，直接用样本标准差来估计总体标准差。
`````

```{admonition} Remark

- $s$ 是 $\sigma$ 的有偏估计；
- $s$ 是 $\sigma$ 的渐近无偏估计；
- $c_n s$ 是 $\sigma$ 的无偏估计，但实际中我们不纠偏。

```

值得注意的是，不是所有的参数都有无偏估计。在本课程中，如果一个参数的任何估计都不是无偏的，那么称这个参数**不可估**。以下介绍一个例子，供同学们课后阅读。

`````{prf:example}
设总体为二点分布 $b(1,p),0<p<1$ 。 $x_1,x_2,\cdots,x_n$ 是样本，令参数为 $\theta = 1/p$ 。以下说明 $\theta$ 是不可估的。

首先， $T = x_1+x_2+\cdots+x_n$ 是充分统计量，则 $T\sim b(n,p)$ 。若有一个 $\hat{\theta} = \hat{\theta}(t)$ 是 $\theta$ 的无偏估计，则有

$$
E(\hat{\theta}) = \sum_{i=1}^n \begin{pmatrix}
n\\i
\end{pmatrix}
\hat{\theta}(i) p^{i}(1-p)^{n-i} = \frac{1}{p}
$$

也就是说，

$$
\sum_{i=1}^n \begin{pmatrix}
n\\i
\end{pmatrix}
\hat{\theta}(i) p^{i+1}(1-p)^{n-i} -1 =0, \quad 0 < p < 1.
$$

这是 $p$ 的 $n+1$ 次方程，最多有 $n+1$ 个实根，要使它对 $(0,1)$ 中所有的 $p$ 都成立是不可能的，故参数 $\theta = 1/p$ 是不可估的。

其次，若有某个 $h(x_1,x_2,\cdots,x_n)$ 是 $\theta$ 的无偏估计，则令 $\tilde{\theta} = E(h(x_1,x_2,\cdots,x_n)|T)$ 。由重期望公式可知，

$$
E(\tilde{\theta}) = E(E(h(x_1,x_2,\cdots,x_n)|T)) = E(h(x_1,x_2,\cdots,x_n) = \theta.
$$

这说明 $\tilde{\theta}(T)$ 是 $\theta$ 的无偏估计。因此这是不可能的。
`````

## 有效性

```{admonition} Question
对于同一个参数 $\theta$ ，无偏估计仍有很多，如何在无偏估计中进行选择？
```

设 $\hat{\theta}_1,\hat{\theta}_2$ 是 $\theta$ 的两个无偏估计。如果对任意的 $\theta\in \Theta$ 有

$$
\text{Var}(\hat{\theta}_1) \leq \text{Var}(\hat{\theta}_2),
$$

且至少有一个 $\theta \in \Theta$ 使得上述不等号严格成立，则称 $\hat{\theta}_1$ 比 $\hat{\theta}_2$ 更有效。

```{admonition} Remark
对无偏估计而言，方差越小的无偏估计越有效。
```

`````{prf:example} 
:label: ex:chap20_UE_uniform_distribution
设 $x_1,x_2,\cdots,x_n$ 是来自均匀总体 $U(0,\theta)$ 的样本，现有两个无偏估计。

- $\theta$ 的一个估计为 $\hat{\theta}_1 = \frac{n+1}{n}x_{(n)}$ 。 因为 $x_{(n)}/\theta\sim Be(n,1)$ ，所以 $E(x_{(n)}) = \frac{n}{n+1}\theta$ ，而

$$
\text{Var}(x_{(n)}) = \frac{n}{(n+1)^2 (n+2)} \theta^2.
$$

于是， $\hat{\theta}_1$ 是 $\theta$ 的无偏估计，其方差为

$$
\text{Var}(\hat{\theta}_1) = \frac{(n+1)^2}{n^2} \frac{n}{(n+1)^2 (n+2)} \theta^2 = \frac{\theta^2}{n(n+2)}.$$

- $\theta$ 的另一个估计为 $\hat{\theta}_2 = 2\bar{x}$ 。可以计算

$$
E(\hat{\theta}_2) = 2 E(\bar{x}) = 2 \cdot \frac{\theta}{2} = \theta.
$$

而

$$
\text{Var}(\hat{\theta}_2)= 4 \text{Var}(\bar{x}) = \frac{4}{n} \cdot \frac{\theta^2}{12} = \frac{\theta^2}{3n}.
$$

根据比较可知，当 $n>1$ 时， $\hat{\theta}_1$ 比 $\hat{\theta}_2$ 更有效。
`````

```{admonition} Remark
我们发现： $\hat{\theta}_1$ 是 $x_{(n)}$ 的函数，而 $x_{(n)}$ 是 $\theta$ 的充分统计量。
```

```{admonition} Question
对于任意 $\theta \in \Theta$ ，我们能否找到一致最小均方误差估计 $\hat{\theta}$ ，即

$$
\hat{\theta} = \arg\min_{\hat{\theta}} \text{MSE} (\hat{\theta})?
$$

```

```{admonition} Remark
在**无偏估计类**中，存在一致最小均方误差估计，此时一致最小均方误差估计为一致最小方差无偏估计（Uniformly Minimum Variance Unbiased Estimate, UMVUE）。对于 UMVUE 这里不再深入探讨，感兴趣的同学可以自行阅读《概率论与数理统计教程》6.4 最小方差无偏估计这一节进行了解，属于选修内容。
```

## 充分性原则

在例 {prf:ref}`ex:chap20_UE_uniform_distribution` 中，我们发现在两个无偏估计 $\hat{\theta}_1 = \frac{n+1}{n}x_{(n)}$ 和 $\hat{\theta}_2 = 2\bar{x}$ 中，更优的估计是 $\hat{\theta}_1$ ，其是充分统计量 $x_{(n)}$ 的函数。

```{admonition} Question
由充分统计量得到的估计更优，这是偶然吗？
```

``````{prf:theorem} Rao-Blackwell 定理
设总体概率函数是 $p(x;\theta)$ , $x_1,x_2,\cdots,x_n$ 是其样本， $T = T(x_1,x_2,\cdots,x_n)$ 是 $\theta$ 的充分统计量。则对 $\theta$ 的任一无偏估计 $\hat{\theta} = \hat{\theta}(x_1,x_2,\cdots,x_n)$ ，令 $\tilde{\theta} = E(\hat{\theta}|T)$ ，有 $\tilde{\theta}$ 也是 $\theta$ 的无偏估计，且

$$
\text{Var}(\tilde{\theta}) \leq \text{Var}(\hat{\theta}).
$$


```{dropdown} Proof
第一，欲证明 $\tilde{\theta}$ 是 $\theta$ 的无偏估计，即

$$
\begin{eqnarray*}
E(\tilde{\theta}) = E( E(\hat{\theta}|T)) = E(\hat{\theta}) = \theta,
\end{eqnarray*}
$$

其中，第二个等号成立是由于重期望公式。
第二，考察 $\tilde{\theta}$ 的方差，即

$$
\begin{eqnarray*}
\text{Var}(\hat{\theta}) &=&E(\hat{\theta}-E \hat{\theta})^{2} \\
&=&E(\hat{\theta}-\tilde{\theta}+\tilde{\theta}-E \tilde{\theta})^{2},E(\hat{\theta } )=E(\tilde{\theta }) \\
&=&E(\hat{\theta}-\tilde{\theta})^{2}+E(\tilde{\theta}-E(\tilde{\theta}))^{2} +2 E((\hat{\theta}-\tilde{\theta}) \cdot(\tilde{\theta}-E(\tilde{\theta}))) \\
&=&E(\hat{\theta}-\tilde{\theta})^{2}+\text{Var}(\tilde{\theta})
\end{eqnarray*}
$$

其中交叉项为

$$
\begin{eqnarray*}
E((\hat{\theta}-\tilde{\theta}) \cdot(\tilde{\theta}-E(\tilde{\theta}))
&=& E(E((\hat{\theta}-\tilde{\theta}) \cdot(\tilde{\theta}-E(\tilde{\theta}) \mid T))\\
&=& E((\tilde{\theta}-E(\tilde{\theta})) E((\hat{\theta}-\tilde{\theta}) \mid T)) \\
&=& 0
\end{eqnarray*}
$$

```

```{admonition} Remark
Rao-Blackwell 定理表明，对于任何无偏估计，如果其不是充分统计量的函数，那么将其对充分统计量求条件期望可以得到一个新的无偏估计，而且该估计的方差比原来的估计方差要小。
```

``````

`````{prf:example}
总体分布为泊松分布 $P(\lambda)$ ，其中参数 $\lambda >0$ 。先有两个样本 $x_1,x_2$ 。
 $x_1,x_2$ 的联合分布列为

$$
p(x_1,x_2;\lambda) = \frac{\lambda^{x_1}}{x_1!}e^{-\lambda} \cdot \frac{\lambda^{x_2}}{x_2!}e^{-\lambda} = \lambda^{(x_1+x_2)} e^{-2\lambda}\frac{1}{x_1!x_2!}.
$$

令 $T(x_1,x_2)=x_1+x_2$ ， $g(t,\lambda) = \lambda^{t} e^{-2\lambda}$ 和 $h(x_1,x_2) = \frac{1}{x_1!x_2!}$ 。根据因子分解定理，有 $T(x_1,x_2) = x_1+x_2$ 是充分的。而 $T(x_1,x_2)\sim P(2\lambda)$ 。

因为 $E(x_1) = \lambda$ ，所以 $\hat{\lambda}= x_1$ 是 $\lambda$ 的无偏估计。令 $\tilde{\lambda} = E(\hat{\lambda}|T)$ 。则

$$
\begin{eqnarray*}
P(X_1 = x_1|X_1 + X_2 =n) &=& \frac{P(X_1=x_1,X_1+X_2=n)}{P(X_1+X_2=n)}\\
&=& \frac{\frac{\lambda^{x_1}}{x_1!}e^{-\lambda} \frac{\lambda^{n-x_1}}{(n-x_1)!}e^{-\lambda} }{\frac{(2\lambda)^{n}}{n!}e^{-2\lambda} }\\
&=& \frac{\frac{\lambda^{n}}{x_1!(n-x_1)!} }{\frac{(2\lambda)^{n}}{n!} }\\
&=& \frac{n!}{x_1!(n-x_1)!} \left(1/2\right)^{x_1} \left(1/2\right)^{n-x_1}
\end{eqnarray*}
$$

且

$$
E(X_1|X_1+X_2 = x_1+x_2) = \frac{x_1+x_2}{2}.
$$

我们分别可以计算

$$
\text{Var}(\hat{\lambda}) = \lambda >
\text{Var}(\tilde{\lambda}) = \frac{\lambda}{2}, \lambda> 0.
$$

所以， $\tilde{\lambda}$ 的方差更小。
`````

```{admonition} Remark
在考虑 $\theta$ 的估计问题中，我们只需要基于充分统计量的函数来构造。这就是充分性原则，在所有统计推断的问题中都是成立的。
```

以下例子由同学课后自己自行理解。

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自 $b(1,p)$ 的样本，则 $\bar{x}$ （或 $T = n\bar{x}$ ）是 $p$ 的充分统计量。为估计 $\theta = p^2$ ，可令

$$
\hat{\theta}_1 =\left\{
\begin{aligned}
& 1, & x_1 = 1, x_2 = 1,\\
& 0, & \text{其他}.
\end{aligned}
\right.
$$

由于

$$
E(\hat{\theta}_1) = P(x_1 = 1, x_2 = 1) = p\cdot p = \theta,
$$

所以， $\hat{\theta}_1$ 是 $\theta$ 的无偏估计。这个估计并不好，因为它只用了两个观测值。但我们可以用 Rao-Blackwell 定理来优化这个估计。具体过程如下：

$$
\begin{eqnarray*}
\hat{\theta} &=& E(\hat{\theta}_1 | T= t) = P(\hat{\theta}_1 = 1 | T = t) \\
&=& \frac{P(x_1=1,x_2=1,T =t)}{P(T=t)} = \frac{P(x_1=1,x_2=1,\sum_{i=3}^nx_i =t-2)}{P(T=t)}\\
&=& \frac{p \cdot p \cdot \begin{pmatrix}
n-2\\t-2
\end{pmatrix}p^{t-2} (1-p)^{n-t}}{\begin{pmatrix}
n\\t
\end{pmatrix}p^{t} (1-p)^{n-t}} = \frac{\begin{pmatrix}
n-2\\t-2
\end{pmatrix}}{\begin{pmatrix}
n\\t
\end{pmatrix}}\\
&= & \frac{t(t-1)}{n(n-1)}.
\end{eqnarray*}
$$

其中， $t=\sum_{i=1}^n x_i$ 。可以验证， $\hat{\theta}$ 是 $\theta$ 的无偏估计，且 $\text{Var}(\hat{\theta}) < \text{Var}(\hat{\theta}_1)$ 。
`````