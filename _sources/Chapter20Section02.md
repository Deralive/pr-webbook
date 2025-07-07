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
`````

```{admonition} Remark
回看样本方差 $s_n^2$ ，这个估计量的偏差为

$$
-\frac{1}{n}\sigma^2 .
$$

当样本量 $n$ 越大时， $s_n^2$ 的偏差越接近 0，而 $s_n^2$ 的期望也越接近 $\sigma^2$ 。于是，我们称 $s_n^2$ 是 $\sigma^2$ 的**渐近无偏**估计。
```

```{admonition} Question
总体标准差 $\sigma$ 的无偏估计会是怎样的？样本标准差 $s$ 是 $\sigma$ 的无偏估计吗？
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