# 方差与标准差
通过定理 {prf:ref}`thm:chap06_expectation_rv_funciton`，我们可以计算随机变量 $X$ 函数的期望。其中，有一个特殊的函数，即 $(X-E(X))^2$ ，它的期望也是分布的重要特征，我们单独给一个定义——方差。

方差与标准差
: 若随机变量 $X^{2}$ 的数学期望 $E(X^{2})$ 存在，则称偏差平方

$$E(X-E(X))^{2}$$

为随机变量 $X$ 的方差，记为

$$
\begin{eqnarray*}
\text{Var}(X) &=&E(X-E(X))^{2}\\
&=& \left\{
\begin{aligned}
& \sum_{i}\left(x_{i}-E(x)\right)^{2} p\left(x_{i}\right), \qquad \mbox{在离散场合}\\
&\int_{-\infty}^{+\infty}(x-E(X))^{2} p(x) d x, \quad \mbox{在连续场合}
\end{aligned}
\right.
\end{eqnarray*}
$$

称方差的平方根 $\sqrt{\operatorname{Var}(X)}$ 为随机变量 $X$ 的标准差，记为 $\sigma(x)$ 或 $\sigma_x$ 。

`````{prf:property}

- $\text{Var}(X) = E(X^2) - (E(X))^2$ ；
- 常数的方差为零，即若 $c$ 为常数，则 $\text{Var}(c) = 0$ ；
- 若 $a,b$ 为常数，则 $\text{Var}(aX+b) = a^2 \text{Var}(X)$ .

`````

这里介绍三个常见随机变量期望和方差的计算方法。

`````{prf:example}
如果 $X\sim b(n,p)$ ，那么 $E(X) = np$ 且 $\text{Var}(X) = np(1-p)$ 。

```{dropdown} Solution
 $X$ 的分布列为

$$
P(X=k) = C_n^k p^k (1-p)^{n-k},k = 0,1,2,\cdots,n.
$$

于是， $X$ 的期望为
\begin{eqnarray*}
E(X) &=& \sum_{k=0}^n k P(X=k)\\
&=& \sum_{k=0}^n k \cdot C_n^k p^k (1-p)^{n-k}\\
&=& \sum_{k=1}^n k\cdot \frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}\\
&=& \sum_{k=1}^n \frac{n!}{(k-1)!(n-k)!} p^k (1-p)^{n-k}\\
&=& np\cdot \sum_{k=1}^n \frac{(n-1)!}{(k-1)!(n-k)!} p^{k-1} (1-p)^{n-k}\\
&\overset{k'=k-1}{=}& np\cdot \sum_{k'=0}^{n-1} \frac{(n-1)!}{(k')!(n-1-k')!} p^{k'} (1-p)^{n-1-k'}\\
&=& np,
\end{eqnarray*}
因为 $X$ 的方差 $\text{Var}(X) = E(X^2) - (E(X))^2$ ，所以，需要计算 $X^2$ 的期望。而 $X^2$ 的期望为
\begin{eqnarray*}
E(X) &=& \sum_{k=0}^n k^2 P(X=k)\\
&=& \sum_{k=0}^n k^2\cdot C_n^k p^k (1-p)^{n-k}\\
&=& \sum_{k=1}^n k^2\cdot \frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}\\
&=& \sum_{k=1}^n k\cdot \frac{n!}{(k-1)!(n-k)!} p^k (1-p)^{n-k}\\
&=& np\cdot \sum_{k=1}^n k\cdot \frac{(n-1)!}{(k-1)!(n-k)!} p^{k-1} (1-p)^{n-k}\\
&\overset{k'=k-1}{=}& np\cdot \sum_{k'=0}^{n-1} (k'+1) \frac{(n-1)!}{(k')!(n-1-k')!} p^{k'} (1-p)^{n-1-k'}\\
&=& np\cdot ((n-1)p+1) \\
&=& n(n-1)p^2 + np,
\end{eqnarray*}
于是，

$$\text{Var}(X) = E(X^2) - (E (X))^2 = n(n-1)p^2 + np - (np)^2 = np - np^2 = np(1-p).$$

```

`````

`````{prf:example}
如果 $X\sim N(\mu,\sigma^2)$ ，那么 $E(X) = \mu$ 且 $\text{Var}(X) = \sigma^2$ 。

```{dropdown} Solution
 $X$ 的密度函数为

$$
p(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} (x-\mu)^2\right\},x\in R.
$$

于是， $X$ 的期望为
\begin{eqnarray*}
E(X) &=& \int_{0}^{\infty} x p(x) \text{d}x\\
&=& \int_{-\infty}^{\infty} x \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} (x-\mu)^2\right\} \text{d}x\\
&\overset{z = x-\mu}{=}& \int_{-\infty}^{\infty} (z+\mu) \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} (z)^2\right\} \text{d} z\\
&= & \int_{-\infty}^{\infty} z \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} (z)^2\right\} \text{d} z + \mu\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} (z)^2\right\} \text{d} z\\
&=& \mu.
\end{eqnarray*}
而 $X$ 的方差为
\begin{eqnarray*}
\text{Var}(X) &=& E(X-E(X))^2\\
&=&\int_{-\infty}^{\infty} (x-\mu)^2 \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} (x-\mu)^2\right\} \text{d} x \\
&\overset{z = x-\mu}{=}& \int_{-\infty}^{\infty} z^2 \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} z^2\right\} \text{d} z\\
&=& \frac{1}{\sqrt{2\pi \sigma^2}} \int_{-\infty}^{\infty} -{\sigma^2} z \text{d} \exp\left\{ - \frac{1}{2\sigma^2} z^2\right\} \\
&=& \frac{1}{\sqrt{2\pi \sigma^2}} \cdot \left(\left.-{\sigma^2} z\exp\left\{ - \frac{1}{2\sigma^2} z^2\right\} \right|_{-infty}^{\infty}+ \int_{-\infty}^{\infty} {\sigma^2}\exp\left\{ - \frac{1}{2\sigma^2} z^2\right\} \text{d}z \right)\\
&=& \int_{-\infty}^{\infty} {\sigma^2} \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left\{ - \frac{1}{2\sigma^2} z^2\right\} \text{d}z \\
&=& \sigma^2.
\end{eqnarray*}
```

`````

`````{prf:example}
如果 $X\sim Ga(\alpha,\lambda)$ ，那么 $E(X) = \frac{\alpha}{\lambda}$ 且 $\text{Var}(X) = \frac{\alpha}{\lambda^2}$ 。

````{dropdown} Solution
 $X$ 的密度函数为

$$
p(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} \exp\{-\lambda x\},x>0.
$$

这里我们先考虑 $X^k$ 的期望
\begin{eqnarray*}
E(X^k) &=& \int_{0}^{\infty} x^k p(x) \text{d}x = \int_{0}^{\infty} x^k \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} \exp\{-\lambda x\}\text{d}x\\
&=& \int_{0}^{\infty} \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha+k -1} \exp\{-\lambda x\}\text{d}x\\
&=& \int_{0}^{\infty} \frac{(\alpha+k-1)\times \cdots \times (\alpha)}{\lambda^k}\cdot \frac{\lambda^{\alpha+k}}{\Gamma(\alpha+k)} x^{\alpha+k -1} \exp\{-\lambda x\}\text{d}x\\
&=&\frac{(\alpha+k-1)\times \cdots \times (\alpha)}{\lambda^k}.
\end{eqnarray*}
于是， $X$ 的期望为

$$E(X) = \frac{\alpha}{\lambda}.$$

而
 $X$ 的方差为

$$
\text{Var}(X) = E(X^2) - (E X)^2 = \frac{(\alpha+1)\alpha}{\lambda^2} - \frac{\alpha^2}{\lambda^2} = \frac{\alpha}{\lambda^2}.
$$


```{admonition} Remark
在计算期望时，一个最常用的方法是“合成概率函数”。
```


````
`````
