# 单个总体正态分布下的假设检验问题
## 方差已知时， $\mu$ 的检验

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自正态分布 $N(\mu,\sigma_0^2)$ 的样本，其中 $\sigma_0^2$ 是已知的。我们需要检验以下假设

$$
H_0: \mu \leq \mu_0 \quad \text{vs} \quad H_0: \mu > \mu_0. $$

求显著性水平为 $\alpha$ 的检验。
```{dropdown} Solution

因为备择假设依旧为 $\mu > \mu_0$ ，所以，我们构造拒绝域为

$$
W = \left\{\bar{x} \geq c\right\}.
$$

考虑第一类错误发生的概率为

$$
\begin{eqnarray*}
\alpha_{\mu}(c) &=& P_{\mu}(\bar{x} \geq c|H_0) \\
&=& 1-\Phi\left(\frac{c-\mu}{\sqrt{\sigma_0^2/n}}\right) , \mu \leq \mu_0.
\end{eqnarray*}
$$

注意到 $\alpha_{\mu}(c)$ 是关于 $\mu$ 的增函数。我们要求对任意 $\mu\leq \mu_0$ ，有

$$
\alpha_{\mu}(c) \leq \alpha.
$$

只需要 $\max_{\mu \leq \mu_0}\alpha_{\mu}(c)= \alpha$ ，等价于 $\alpha_{\mu_0}(c)\leq \alpha$ 。于是可以解得

$$
c = \mu_0 + z_{1-\alpha}\sqrt{\sigma_0^2/n}.
$$

由此，所构造的拒绝域仍为

$$
W = \{(x_1,x_2,\cdots,x_n): \bar{x} \geq \mu_0 + z_{1-\alpha} \sqrt{\sigma_0^2/n}\}.
$$

```
`````

```{admonition} Remark
假设$
H_0: \mu = \mu_0 \quad \text{vs} \quad H_0: \mu > \mu_0 $和$ 
H_0: \mu \leq \mu_0 \quad \text{vs} \quad H_0: \mu > \mu_0$
我们构造的水平为 $\alpha$ 的显著性检验是相同的，拒绝域均为 $W = \left\{ \bar{x} \geq \mu_0 + z_{1-\alpha} \sqrt{\sigma_0^2/n} \right\}$ 。
```

## 方差未知时， $\mu$ 的检验

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自正态分布 $N(\mu,\sigma)$ 的样本，其中 $\sigma$ 是未知的。我们需要检验以下假设

$$
H_0: \mu \leq \mu_0 \quad \text{vs} \quad H_0: \mu > \mu_0. $$

求显著性水平为 $\alpha$ 的检验。
```{dropdown} Solution

我们构造的拒绝域为
$
W = \left\{\bar{x} \geq c\right\}.
$
考虑第一类错误发生的概率为

$$
\begin{eqnarray*}
\alpha_{\mu_0}(c) &=& P_{\mu}(\bar{x} \geq c|H_0) \\
&=& P_{\mu}\left(\frac{\bar{x} - \mu}{\sqrt{\hat{\sigma}^2/n}} \geq \frac{c - \mu}{\sqrt{\hat{\sigma}^2/n}}|H_0\right)\\
&=& 1- P\left(\frac{\bar{x} - \mu_0}{\sqrt{\hat{\sigma}^2/n}}\leq \frac{c - \mu_0}{\sqrt{\hat{\sigma}^2/n}}\right)
\end{eqnarray*}
$$

其中， $\hat{\sigma}^2 = (n-1)^{-1}\sum_{i=1}^n (x_i - \bar{x})^2$ 且检验统计量为

$$
\frac{\bar{x} - \mu_0}{\sqrt{\hat{\sigma}^2/n}} \sim t(n-1).
$$

为了 $\alpha_{\mu_0}(c) = \alpha$ ，可解得

$$
c = \mu_0 + t_{1-\alpha}(n-1)\sqrt{\hat{\sigma}^2/n}.
$$

由此，所构造的拒绝域仍为

$$
W = \{(x_1,x_2,\cdots,x_n): \bar{x} \geq \mu_0 + t_{1-\alpha}(n-1)\sqrt{\hat{\sigma}^2/n}\}.
$$

```
`````

```{admonition} Remark
这个检验是单样本的 $t$ 检验，这是因为检验统计量服从 $t$ 分布。
```

上述介绍的检验都是单边检验，以下我们给一个双边检验的例子。

`````{prf:example} 
:label: ex:chap22_one_sample_mean_t
设 $x_1,x_2,\cdots,x_n$ 是来自正态分布 $N(\mu,\sigma)$ 的样本，其中 $\sigma$ 是未知的。我们需要检验以下假设

$$
H_0: \mu = \mu_0 \quad \text{vs} \quad H_0: \mu \neq \mu_0. $$

求显著性水平为 $\alpha$ 的检验。
```{dropdown} Solution

我们构造的拒绝域为

$$
W = \left\{\bar{x} \leq c_1\right\} \cup \left\{\bar{x} \geq c_2\right\}.
$$

考虑第一类错误发生的概率为

$$
\begin{eqnarray*}
\alpha_{\mu_0}(c) &=& P_{\mu_0}\left(\left\{\bar{x} \leq c_1\right\} \cup \left\{\bar{x} \geq c_2\right\}\right) \\
&=& P_{\mu_0}\left(\left\{\bar{x} \leq c_1\right\} |H_0\right) + P\left( \left\{\bar{x} \geq c_2\right\}\right) \\
&=& P_{\mu_0}\left(\frac{\bar{x} - \mu_0}{\sqrt{\hat{\sigma}^2/n}} \leq \frac{c_1 - \mu_0}{\sqrt{\hat{\sigma}^2/n}}\right) + P_{\mu_0}\left(\frac{\bar{x} - \mu_0}{\sqrt{\hat{\sigma}^2/n}} \geq \frac{c_2 - \mu_0}{\sqrt{\hat{\sigma}^2/n}}\right)\\
&=& P\left( t \leq \frac{c_1 - \mu_0}{\sqrt{\hat{\sigma}^2/n}} \right) + 1 - P\left( t \leq \frac{c_2 - \mu_0}{\sqrt{\hat{\sigma}^2/n}}\right).
\end{eqnarray*}
$$

为了 $\alpha_{\mu_0}(c) = \alpha$ ，我们将 $\alpha$ 拆成两部分，即

$$
\left\{
\begin{aligned}
& P\left( t \leq \frac{c_1 - \mu_0}{\sqrt{\hat{\sigma}^2/n}} \right) = \alpha/2\\
& 1 - P\left( t \leq \frac{c_2 - \mu_0}{\sqrt{\hat{\sigma}^2/n}}\right) = \alpha/2
\end{aligned}
\right.
$$

于是解得
\begin{equation*}
\begin{aligned}
& c_1 = \mu_0 - t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n} \\
& c_2 = \mu_0 + t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n} .
\end{aligned}
\end{equation*}
由此，所构造的拒绝域仍为

$$
W = \{(x_1,x_2,\cdots,x_n): \bar{x} \leq \mu_0 - t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n} \text{ 或 } \bar{x} \geq \mu_0 + t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n}\}.
$$

```
`````
## 假设检验与区间估计之间的关系
在例题 {prf:ref}`ex:chap22_one_sample_mean_t` 中，我们构造的拒绝域为

$$
W = \{\bar{x} \leq \mu_0 - t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n} \text{ 或 } \bar{x} \geq \mu_0 + t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n}\}.
$$

则接受域为

$$
\overline{W} = \left\{ \mu_0 - t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n} \leq \bar{x} \leq \mu_0 + t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n} \right\}.
$$

根据上述区间，并进行变换，可以解得

$$
\left\{
\begin{aligned}
& \mu_0 \leq \bar{x} + t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n} \\
& \mu_0 \geq \bar{x} - t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n}
\end{aligned}
\right.
$$

从 $\mu_0$ 的角度来看， $\mu_0$ 的区间为

$$
[\bar{x} - t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n},\bar{x} + t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n}].
$$

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 来自于一个正态分布 $N(\mu,\sigma^2)$ ，其中 $\sigma^2$ 未知。求 $\mu$ 的置信水平为 $1-\alpha$ 的置信区间。
```{dropdown} Solution

因为 $\mu$ 的点估计为 $\hat{\mu} = \bar{x}$ ，其分布为 $N(\mu,\sigma^2/n)$ ，而 $\hat{\sigma}^2 = (n-1)^{-1}\sum_{i=1}^n (x_i-\bar{x})^2$ 。所构造的枢轴量为

$$
\frac{\bar{x} - \mu}{\sqrt{\hat{\sigma}^2/n}} \sim t(n-1).
$$

所以， $\mu$ 的置信水平为 $1-\alpha$ 的置信区间为

$$
[\bar{x} - t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n},\bar{x} + t_{1-\alpha/2}(n-1)\sqrt{\hat{\sigma}^2/n}]
$$

```
`````

```{admonition} Remark
区间估计也可以解决假设检验问题。以显著性水平为 $\alpha$ 的双边检验问题为例，如果所构造的置信水平为 $1-\alpha$ 置信区间能够盖住 $\theta_0$ ，那么我们可以通过变换确定样本落在接受域 $\overline{W}$ 中，从而接受原假设。
```