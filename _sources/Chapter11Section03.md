# 连续场合下的条件分布
设二维连续随机变量 $(X,Y)$ 的联合密度为 $p(x,y)$ ，边际密度函数为 $p_{X}(x)$ 和 $p_{Y}(y)$ 。
在离散随机变量场合，其条件分布函数为 $P(X\le x | Y=y)$ ，但是连续随机变量取某个值的概率为零，即 $P(Y=y)=0$ 。所以无法用条件概率直接计算 $P(X\le x | Y=y)$ 。一个自然的想法是，将 $P(X\le x | Y=y)$ 看成当 $h \rightarrow 0$ 时 $P(X\le x | y\le Y\le y+h)$ 的极限，即

$$
\begin{eqnarray*}
P(X \leq x | Y=y) &=&\lim _{h \rightarrow 0} P(X \leqslant x | y \leqslant Y \leqslant y+h) \\
&=&\lim _{h \rightarrow 0} \frac{P(X \leq x, y \leq Y \leq y+h)}{P(y \leq Y \leq y+h)} \\
&=&\lim _{h \rightarrow 0} \frac{\int_{-\infty}^{x} \int_{y}^{y+h} p(u, v) \text{d} v \text{d} u}{\int_{y}^{y+h} p(v) \text{d} v} \\
&=&\lim _{h \rightarrow 0} \frac{\int_{-\infty}^{x}\left(\frac{1}{h} \int_{y}^{y+h} p(u, v) \text{d} v\right) \text{d} u}{\frac{1}{h} \int_{y}^{y+h} P_{Y}(v) \text{d} v}
\end{eqnarray*}
$$

当 $p_{Y}(y),p(x,y)$ 在 $y$ 处连续时，由积分中值定理可得

$$
\begin{eqnarray*}
\lim _{h \rightarrow 0} \frac{1}{h} \int_{y}^{y+h} p_{Y}(v) \text{d} v
&=&\lim _{h \rightarrow 0} \frac{1}{h} \cdot(y+h-y) \cdot p_{Y}(y+\delta h)=p_{Y}(y) \\
\lim _{h \rightarrow 0} \frac{1}{h} \int_{y}^{y+h} p(u, v) \text{d} v&=&\lim _{h \rightarrow 0} \frac{1}{h}(y+h-y) \cdot p(u, y+\delta h)=p(u, y)
\end{eqnarray*}
$$

所以

$$P(X \leq x | Y=y)=\int_{-\infty}^{x} \frac{p(u, y)}{p_{Y}(y)} \text{d} u.$$

给定条件下的条件分布函数与条件密度函数
: 对一切使 $p_{Y}(y)>0$ 的 $y$ ，给定 $Y=y$ 条件下 $X$ 的条件分布函数和条件密度函数分别为

$$
\begin{eqnarray*}
F(x | y)&=&\int_{-\infty}^{x} \frac{p(u, y)}{p_{Y}(y)} \text{d} u, \\
p(x | y)&=&\frac{p(x, y)}{p_{Y}(y)}.
\end{eqnarray*}
$$

`````{prf:example}
设 $(X,Y)$ 服从二维正态分布

$$N_{2}\left(\begin{pmatrix}
\mu_{1} \\
\mu_{2}
\end{pmatrix},\begin{pmatrix}
\sigma_{1}^{2} & \rho \sigma_{1} \sigma_{2} \\
\rho \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{pmatrix}
\right)$$

由边际分布可知， $X$ 服从正态分布 $N(\mu_{1},\sigma_{1}^{2})$ ， $Y$ 服从正态分布 $N(\mu_{2},\sigma_{2}^{2})$ 。
在给定 $Y=y$ 的条件下， $X$ 的边际密度函数为

$$
\begin{eqnarray*}
p(x | y) &=&\frac{p(x, y)}{p_{Y}(y)} \\
&=&\frac{\frac{1}{2 \pi \sqrt{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho ^{2}\right)}} \exp \left\{-\frac{1}{2\left(1-\rho ^{2}\right)}\left(\frac{(x-\mu_{1})^{2}}{\sigma_{1}^{2}}-2 \rho \frac{\left(x-\mu_{1}\right)\left(y-\mu_{2}\right)}{\sigma_{1} \sigma_{2}}+\frac{\left(y-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right)\right\}}{\frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} \exp \left\{-\frac{1}{2 \sigma_{2}^{2}}\left(y-\mu_{2}\right)^{2}\right\}} \\
&=&\frac{1}{\sqrt{2 \pi}} \cdot \frac{1}{\sqrt{\sigma_{1}^{2}(1-\rho ^{2})}} \exp \left\{-\frac{1}{2\left(1-\rho^{2}\right)}\left(\frac{\left(x-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}-2 \rho \frac{\left(x-\mu_{1}\right)\left(y-\mu_{2})\right.}{\sigma_{1} \sigma_{2}}+\frac{\rho^{2}\left(y-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right)\right\}\\
&=&\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}(1-\rho ^{2})}} \exp \left\{-\frac{1}{2 \sigma_{1}^{2}\left(1-\rho^{2}\right)}\left(x-\left(\mu_{1}+\rho \cdot \frac{\sigma_{1}}{\sigma_{2}}\left(y-\mu_{2}\right)\right)\right)^{2}\right\}
\end{eqnarray*}
$$

因此，在 $Y=y$ 的条件下， $X$ 的条件分布为

$$ N\left(\mu_{1}+ \frac{\rho\sigma_{1}}{\sigma_{2}}\left(y-\mu_{2}\right), \sigma_{1}^{2}\left(1-\rho ^{2}\right)\right) .$$

`````

```{admonition} Remark
在定义连续场合下的条件密度函数下，我们可以给出连续场合下的全概率公式及贝叶斯公式。因为

$$
p_Y(y)= \frac{p(x,y)}{p_Y(y)}
$$

所以，

$$
p(x,y) = p_Y(y)p_Y(y).
$$

于是，我们有

- 全概率公式

$$
p_X(x) = \int_{-\infty}^{+\infty} p(x, y) \text{d} y = \int_{-\infty}^{+\infty} p_{Y}(y) p(x | y) \text{d} y.
$$

- 贝叶斯公式

$$
p(y|x) = \frac{p(x,y)}{p_{X}(x)} = \frac{p_Y(y)p(x|y)}{\int_{-\infty}^{+\infty} p_{Y}(y) p(x | y) \text{d} y}.
$$

```

`````{prf:example}
设 $X\sim N(\mu,\sigma_{1}^{2})$ 且在给定 $X = x$ 的条件下， $Y$ 的条件分布为 $N(x,\sigma_{2}^{2})$ ，求 $Y$ 的密度函数 $p_{Y}(y)$ 。
```{dropdown} Solution

由题可知，

$$
\begin{eqnarray*}
p_X(x) &=& \frac{1}{\sqrt{2\pi \sigma_1^2}} \exp\left\{-\frac{1}{2\sigma_1^2} (x-\mu)^2\right\},\\
p(y|x) &=& \frac{1}{\sqrt{2\pi \sigma_2^2}}
\exp\left\{-\frac{1}{2\sigma_2^2} (y-x)^2\right\}.
\end{eqnarray*}
$$

所以，根据全概率公式可知，

$$
\begin{eqnarray*}
P_{Y}(y)
&=&\int_{-\infty}^{+\infty}p_{X}(x)p(y | x) \text{d} x\\
&=&\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi \sigma_{1}^{2}}} \exp \left\{-\frac{1}{2 \sigma_{1}^{2}}(x-\mu)^{2}\right\} \cdot \frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} \exp \left\{-\frac{1}{2 \sigma_{2}^{2}}(y-x)^{2}\right\} \text{d} x\\
&=&\frac{1}{2 \pi \sqrt{\sigma_{1}^{2} \sigma_{2}^{2}}} \int_{-\infty}^{+\infty} \exp \left\{-\frac{1}{2} \left(\frac{1}{\sigma_{1}^{2}} x^{2}-\frac{2 \mu}{\sigma_{1}^{2}} x+\frac{\mu^{2}}{\sigma_{1}^{2}}\right.\right.
\left.\left.+\frac{y^{2}}{\sigma_{2}^{2}}-\frac{2 y}{\sigma_{2}^{2}} x+\frac{x^{2}}{\sigma_{2}^{2}} \right)\right\} \text{d} x\\
&=& \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi \frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}}}
\exp \left\{-\frac{1}{2} \left(\left( \frac { 1 } { \sigma _ { 1 } ^ { 2 } } + \frac { 1 } { \sigma _ { 2 } ^ { 2 } } \right)
\left(x-\left(\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}\right)^{-1}\left(\frac{\mu}{\sigma_{1}^{2}}+\frac{y}{\sigma_{2}^{2}}\right)\right)^{2} \right)\right\}\text{d}x \\
&& \cdot \frac{1}{\sqrt{2 \pi\sigma_{1}^{2}+\sigma_{2}^{2}}} \exp\left\{
-\left(\frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}\right)\left(\frac{\mu^{2}}{\sigma_{1}^{4}}+\frac{2 \mu y}{\sigma_{1}^{2} \sigma_{2}^{2}}+\frac{y^{2}}{\sigma_{2}^{4}}\right)+\frac{y^{2}}{\sigma_{2}^{2}}+\frac{\mu^{2}}{\sigma_{1}^{2}} \right\} \\
&=&\frac{1}{\sqrt{2 \pi\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)}} \exp \left\{-\frac{1}{2} \left(\frac{1}{\sigma_{1}^{2}+\sigma_{2}^{2}} y^{2}-\frac{2 \mu y}{\sigma_{1}^{2}+\sigma_{2}^{2}}+\frac{\mu^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}} \right)\right\}\\
&=&\frac{1}{\sqrt{2 \pi(\sigma_{1}^{2}+\sigma_{2}^{2})}} \exp \left\{-\frac{1}{2\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)}(y-\mu)^{2}\right\}
\end{eqnarray*}
$$

因此，

$$Y\sim N(\mu,\sigma_{1}^{2}+\sigma_{2}^{2}).$$

```
`````