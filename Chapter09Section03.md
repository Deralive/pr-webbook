# 协方差与相关系数
## 协方差
在考虑多个随机变量时，每一个随机变量的期望与方差是我们关注的特征数之外，两个随机变量之间的关系也是我们关心的一个特征数。以下我们介绍特征数——协方差。

协方差
: 设 $(X,Y)$ 是一个二维随机变量，若

$$E\left( (X-E(X))(Y-E(Y)) \right) $$

存在，则称其为 $X$ 与 $Y$ 的协方差或相关（中心）矩，并记为 $\text{Cov}(X,Y)=E\left ( (X-E(X))(Y-E(Y)) \right)$ 

```{admonition} Remark

- 特别地， $\text{Cov}(X,X)=\text{Var}(X)$ ；
- 通过协方差可以判断两个随机变量之间的关系，即

- $\text{Cov}(X,Y)>0$ 时，称 $X$ 与 $Y$ 正相关
- $\text{Cov}(X,Y)<0$ 时，称 $X$ 与 $Y$ 负相关
- $\text{Cov}(X,Y)=0$ 时，称 $X$ 与 $Y$ 不相关（毫无关联/非线性关系）

```

以下介绍协方差的一些性质。

`````{prf:property}

- $\text{Cov}(X,Y)=E(XY)-E(X)E(Y)$ ；
- $X$ 与 $Y$ 独立 $\Rightarrow \text{Cov}(X,Y)=0$ ，反之不然。

```{admonition} Remark
令 $X\sim N(0,\sigma^{2}),Y=X^{2}$ 。我们可以计算

$$
\text{Cov}(X,Y) = E(XY) - E(X)E(Y) = E(X^3) = 0.
$$

```

- $\text{Var}(X \pm Y)= \text{Var}(X)+\text{Var}(Y) \pm 2\text{Cov}(X, Y)$ 。

```{admonition} Remark
对任意 $n$ 个随机变量 $X_{1},X_{2},\cdots,X_{n}$ ，有

$$\text{Var}\left(\sum_{i=1}^{n} X_{i}\right)=\sum_{i=1}^{n} \text{Var}\left(X_{i}\right)+2 \sum_{i=1}^{n} \sum_{j=1}^{i-1} \text{Cov}\left(X_{i}, X_{j}\right).$$

```

- 若 $X$ 与 $Y$ 不相关，则

$$E(X Y)=E(X)E(Y), \quad \text{且}\quad \text{Var}(X \pm Y)= \text{Var}(X)+\text{Var}(Y).$$

- 协方差的计算与次序无关，即 $\text{Cov}(X,Y)=\text{Cov}(Y,X)$ 。
- 任意随机变量 $X$ 与常数 $a$ 的协方差为零，即 $\text{Cov}(X,a)=0$ 。
- 对任意常数 $a,b$ ，有 $\text{Cov}(aX,bY)=ab\cdot \text{Cov}(X,Y)$ 。
- 对于任意三个随机变量 $X,Y,Z$ ，有

$$\text{Cov}(X+Y, Z)=\text{Cov}(X, Z)+\text{Cov}(Y, Z)$$

`````

## 相关系数

相关系数
: 设 $(X,Y)$ 是一个二维随机变量，且 $\text{Var}(X)=\sigma _{X} ^{2} >0, \text{Var}(Y)=\sigma _{Y} ^{2} >0$ ，则称

$$
\text{Corr}(X, Y)=\frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X) \cdot \text{Var}(Y)}}=\frac{\text{Cov}(X, Y)}{\sigma_{X} \sigma_{Y}}$$

为 $X$ 与 $Y$ 的（线性）相关系数。

```{admonition} Remark
从另一个角度来看相关系数，令 $E(X) = \mu_X$ ， $E(Y) = \mu_Y$ 。将原始的随机变量进行标准化，即

$$
X^{\ast} = \frac{X-\mu_{X}}{\sigma_{X}} , \quad Y^{\ast} = \frac{Y-\mu_{Y}}{\sigma_{Y}}.
$$

经过标准化后的两个随机变量的协方差为

$$
\begin{eqnarray*}
\text{Cov}(X^{\ast},Y^{\ast}) &=& \text{Cov}\left(\frac{X-\mu_{X}}{\sigma_{X}}, \frac{Y-\mu_{Y}}{\sigma_{Y}}\right)\\
&=& \frac{1}{\sigma_X\sigma_Y} \text{Cov}(X,Y)\\
&=& \text{Corr}(X,Y).
\end{eqnarray*}
$$

```

`````{prf:example}
证明二维正态分布 $\left(\mu_{X}, \mu_{Y}, \sigma_{X}^{2}, \sigma_{Y}^{2}, \rho\right)$ 的相关系数为 $\rho$ 。
```{dropdown} Solution

首先，计算协方差

$$
\begin{eqnarray*}
\text{Cov}(X, Y) &=&E((X-E(X))(Y-E(Y)))\\
&=& \frac{1}{2 \pi \sqrt{\sigma_{X}^{2} \sigma_{Y}^{2}(1-\rho ^{2})}} \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}\left(x-\mu_{X}\right)\left(y-\mu_{Y}\right) \\
&& \cdot \exp \left\{-\frac{1}{2\left(1-\rho^{2}\right)}\left[\frac{\left(x-\mu_{X}\right)^{2}}{\sigma_{1}^{2}}-2 \rho \frac{\left(x-\mu_{X}\right)\left(y-\mu_{Y}\right)}{\sigma_{1} \sigma_{2}}+\frac{\left(y-\mu_{Y}\right)^{2}}{\sigma_{2}^{2}}\right]\right\} \text{d} x \text{d} y \\
&=& \frac{1}{2 \pi \sqrt{\sigma_{X}^{2} \sigma_{Y}^{2}\left(1-\rho^{2}\right)}} \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}\left(x-\mu_{X}\right)\left(y-\mu_{Y}\right)\cdot \\
&& \cdot \exp \left\{-\frac{1}{2\left(1-\rho^{2}\right)}\left[\left(\frac{x-\mu_{X}}{\sigma_{X}}-\rho \frac{y-\mu_{Y}}{\sigma_{Y}}\right)^{2}+\left(\sqrt{1-\rho^{2}} \frac{y-\mu_{Y}}{\sigma_{Y}}\right)^{2}\right]\right\} \text{d} x \text{d} y
\end{eqnarray*}
$$

令

$$u=\frac{1}{\sqrt{1-\rho^{2}}}\left(\frac{x-\mu_{X}}{\sigma_{X}}-\rho \frac{\left(y-\mu_{Y}\right)}{\sigma_{Y}}\right), \quad \text{且}\quad v=\frac{y-\mu_{Y}}{\sigma_{Y}}$$

则

$$
\begin{eqnarray*}
\left\{\begin{aligned}
&x-\mu_{X}=\sigma_{X}\left(u \sqrt{1-\rho^{2}}+\rho v\right),\\
& y-\mu_{Y}=\sigma_{Y} v,
\end{aligned}\right.
\quad \text{且}\quad
|J|=\left|\begin{matrix}
\sqrt{1-\rho^{2}} \sigma_{X} & \rho \sigma_{X} \\
0 & \sigma_{Y}
\end{matrix}\right|=\sqrt{1-\rho^{2}} \sigma_{X} \sigma_{Y}
\end{eqnarray*}
$$

$$
\begin{eqnarray*}
\text{Cov}\left(X, Y\right)&=& \frac{1}{2 \pi \sqrt{\sigma_{X}^{2} \sigma_{Y}^{2}\left(1-\rho^{2}\right)}} \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}\left(\sigma_{X}\left(u \sqrt{1-\rho^{2}}+\rho v\right)\right)\left(\sigma_{Y} v\right) \\
&& \cdot \exp \left\{-\frac{1}{2}\left[u^{2}+v^{2}\right]\right\} \cdot \sqrt{1-\rho^{2}} \cdot \sigma_{X} \sigma_{Y} \text{d} u \text{d} v \\
&=& \frac{\sigma_{X} \sigma_{Y}}{2 \pi} \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}\left(u v \sqrt{1-\rho^{2}}+\rho v^{2}\right) \exp \left\{-\frac{1}{2}\left(u^{2}+v^{2}\right)\right\} \text{d} u \text{d} v
\end{eqnarray*}
$$

注意到

$$
\begin{eqnarray*}
&&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} u v \exp \left\{-\frac{1}{2}\left(u^{2}+v^{2}\right)\right\} \text{d} u \text{d} v=\int_{-\infty}^{+\infty} u \exp \left\{-\frac{1}{2} u^{2}\right\} \text{d} u \cdot \int_{-\infty}^{+\infty} v \exp \left\{-\frac{1}{2} v^{2}\right\} \text{d} v=0 \\
&&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} v^{2} \exp \left\{-\frac{1}{2}\left(u^{2}+v^{2}\right)\right\} \text{d} u \text{d} v=\int_{-\infty}^{+\infty} \exp \left\{-\frac{1}{2}\left(u^{2}\right)\right\} \text{d} u \cdot \int_{-\infty}^{+\infty} v^{2} \exp \left\{-\frac{1}{2} v^{2}\right\} \text{d} v \\
&=&2 \pi \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi}} \exp \left\{-\frac{1}{2} u^{2}\right\} \text{d} u \int_{-\infty}^{+\infty} v^{2} \cdot \frac{1}{\sqrt{2 \pi}} \exp \left\{-\frac{1}{2} v^{2}\right\} \text{d} v=1 \cdot E\left(v^{2}\right) \cdot 2 \pi=2 \pi .
\end{eqnarray*}
$$

则

$$
\begin{eqnarray*}
\text{Cov}(X, Y)=\frac{\sigma_{X} \sigma_{Y}}{2 \pi} \cdot \rho \cdot 2 \pi=\rho \sigma_{X} \sigma_{Y} \\
\text{Corr}(X, Y)=\frac{\text{Cov}(X ,Y)}{\sqrt{\text{Var}(X) \text{Var}(Y)}}=\frac{\rho \sigma_{X} \sigma_{Y}}{\sigma_{X} \sigma_{Y}}=\rho.
\end{eqnarray*}
$$

```
`````

``````{prf:theorem} Schwarz 不等式
对任意二维随机变量 $(X,Y)$ ，若 $X$ 与 $Y$ 的方差都存在，且记 $\sigma_{X}^{2}=\text{Var}(X),\sigma_{Y}^{2}=\text{Var}(Y)$ ，则有

$$(\text{Cov}(X, Y))^{2} \leq \sigma_{X}^{2} \sigma_{Y}^{2}.$$

```{dropdown} Proof
不妨设 $\sigma_{X}^{2}>0$ ，设函数

$$
\begin{eqnarray*}
g(t) &=&E(t(X-E(X))+(Y-E(Y)))^{2} \\
&=&t^{2} \sigma_{X}^{2}+2t\text{Cov}\left(X, Y\right)+\sigma_{Y}^{2}.
\end{eqnarray*}
$$

因为 $g(t)$ 是一个非负随机变量的期望，所以， $g(t)$ 恒非负。而且，这个二次函数的开口向上，其只有一个或零个零根。所以，其判别式小于或等于零，即

$$ {(2 \text{Cov}(X, Y))^{2}-4 \sigma_{X}^{2} \sigma_{Y}^{2} \leqslant 0}. $$

也就是说，

$$(\text{Cov}(X, Y))^{2} \leqslant \text{Var}(X) \text{Var}(Y).$$

```
``````

`````{prf:property}

- $\left | \text{Corr}(X,Y) \right | \le1$ ；
- $\text{Corr}(X,Y)=\pm1\Leftrightarrow X$ 与 $Y$ 之间几乎处处有线性关系，即存在 $a \neq0$ 与 $b$ ，使得

$$P(Y=aX+b)=1$$

其中，当 $\text{Corr}(X,Y)=1$ 时，有 $a>0$ ；当 $\text{Corr}(X,Y)=-1$ 时，有 $a<0$ 。

```{admonition} Remark

- $\text{Corr}(X,Y)=0$ ，则称 $X$ 与 $Y$ 不相关；
- $\text{Corr}(X,Y)=+1$ ，则称 $X$ 与 $Y$ 完全正相关；
- $\text{Corr}(X,Y)=-1$ ，则称 $X$ 与 $Y$ 完全负相关；
- $0<\left | \text{Corr}(X,Y) \right | <1$ ，则称 $X$ 与 $Y$ 有“一定程度”的线性关系。

```

- 在二维正态分布 $N\left(\mu_{X}, \mu_{Y}, \sigma_{X}^{2}, \sigma_{Y}^{2}, \rho\right)$ 场合，不相关与独立是等价的。

`````