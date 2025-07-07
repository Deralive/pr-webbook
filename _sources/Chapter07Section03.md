# 连续随机变量函数的分布
## $g(X)$ 是一个离散型随机变量
倘若 $Y=g(X)$ 是一个离散型随机变量，我们只需要将 $Y$ 的所有可能取值一一列出，在球 $Y$ 的取各个可能值的概率。

`````{prf:example}
若 $X$ 服从正态分布 $N(\mu,\sigma^2)$ ，则

$$
Y=\left\{\begin{matrix}
0&,X<\mu \\
1&,X\ge \mu
\end{matrix}\right.
$$

那么， $Y$ 服从二点分布 $b(1,0.5)$ 。
`````

## $g(\cdot)$ 是严格单调函数
当 $g(x)$ 是一个关于 $x$ 的严格单调函数，我们有以下定理。

`````{prf:theorem} 
:label: thm:rv_transform
设 $X$ 是连续随机变量，其密度函数为 $p_{X}(x)$ 。 $Y=g(X)$ 是另一个连续随机变量。若 $y=g(x)$ 严格单调，其反函数 $h(y)$ 有连续导函数，则 $Y=g(X)$ 的密度函数为

$$p_{Y}(y)=\left\{\begin{aligned}
p_{X}\left [ h(y) \right ]\left | h'(y) \right | &,a<y<b \\
0&,\text{其他}\end{aligned}\right.$$

其中， $a=\min\left \{ g(-\infty ),g(+\infty ) \right \} ,b=\max\left \{ g(-\infty ),g(+\infty ) \right \}$ 


```{dropdown} Proof
不妨设 $g(x)$ 是一个严格单调增函数，这时它的反函数 $h(y)$ 也是严格单调增函数，且 $h'(y)>0$ 。
首先，考虑 $Y$ 的取值范围。记 $a = \min\{g(-\infty),g(\infty)\}$ ， $b = \max\{g(-\infty),g(\infty)\}$ 。于是， $Y=g(X)$ 仅在区间 $(a,b)$ 取值。
其次，考虑 $Y$ 的分布函数和密度函数。

- 若 $y\leq a$ ，那么 $P(Y\leq y) = 0$ ，则 $p_Y(y) = 0$ ；
- 若 $y\geq b$ ，那么 $P(Y\leq y) = 1$ ，则 $p_Y(y) = 0$ ；
- 若 $a< y<b$ ，那么 $Y$ 的分布函数为

$$
\begin{eqnarray*}
F_Y(y) &=& P(Y \leq y) = P(g(X) \leq y ) \\
&=& P(h(g(X)) \leq h(y)) \\
&=& P(X \leq h(y)) \\
&=& \int_{a}^{h(y)} p_X(x) \text{d}x
\end{eqnarray*}
$$

 $Y$ 的密度函数为

$$
\begin{eqnarray*}
p_Y(y) &=& \frac{\text{d} }{\text{d} y} F(y)= \frac{\text{d} }{\text{d} y} P(Y\leq y) \\
&=& \frac{\text{d} }{\text{d} y}\int_{a}^{h(y)} p_X(x) \text{d}x \\
&=& p_X(h(y)) \cdot h'(y).
\end{eqnarray*}
$$

类似地，因为 $g(x)$ 是严格单调减函数，其反函数 $h(y)$ 也是严格单调减函数，所以 $h'(y)<0$ 。因此，结论中 $h'(y)$ 需要绝对值符号。
```

``````


`````{prf:example}
设随机变量 $X$ 服从正态分布 $N(\mu ,\sigma^{2})$ ，则当 $a \neq 0$ 时，有 $Y=aX+b\sim N(a\mu+b,a^{2}\sigma^{2})$ .
```{dropdown} Solution


- 若 $a>0$ ， $y=g(x)=ax+b$ 是严格增函数。仍在 $(-\infty,+\infty)$ 上取值，其反函数 $x=h(y)=\frac{y-b}{a}$ 。由上述定理可知，

$$
\begin{eqnarray*}
p_{Y}(y)&=&p_{X}\left ( h(y) \right )\left | h'(y) \right | \\
&=&\frac{1}{\sqrt{2\pi \sigma ^{2}} } \exp\left\{-\frac{1}{2\sigma ^{2}}(\frac{y-b}{a} -\mu)^{2} \right\}\cdot \frac{1}{a} \\
&=& \frac{1}{\sqrt{2\pi (a\sigma )^{2}} } \exp\left\{-\frac{1}{2(a\sigma) ^{2}}(y-a\mu-b)^{2} \right\}.
\end{eqnarray*}
$$

因此， $Y\sim N((a\mu+b,a^{2}\sigma^{2})$ 。
- 若 $a<0$ ，证明结果类似，学生可以在课后进行补充。

```
`````

`````{prf:example}
设随机变量 $X\sim N(\mu,\sigma^{2})$ ，则 $Y=e^{X}$ 的概率密度函数为

$$p_{Y}(y)=\left\{\begin{matrix}
\frac{1}{\sqrt{2 \pi} y \sigma} e ^{ -\frac{(\ln y-\mu)^{2}}{2 \sigma^{2}} } &, \quad y>0 \\
0&, \quad y \leqslant 0
\end{matrix}\right.$$

```{dropdown} Solution


$$
\begin{eqnarray*}
p_{Y}(y)&=&p_{X}\left ( h(y) \right )\left | h'(y) \right | \\
&=&\frac{1}{\sqrt{2\pi \sigma ^{2}} } \exp\left\{-\frac{1}{2\sigma ^{2}}(lny -\mu)^{2} \right\}\cdot \frac{1}{y} \\
&=&\frac{1}{\sqrt{2\pi }y\sigma } \exp\left\{-\frac{1}{2\sigma ^{2}}(lny -\mu)^{2} \right\}
\end{eqnarray*}
$$

```
`````

```{admonition} Remark
这个分布称为对数正态分布 $\omega \left(\mu, \sigma^{2}\right)$ 。
```

`````{prf:example}
设 $X\sim Ga(\alpha,r)$ ，则当 $k>0$ 时，有 $Y=kX\sim Ga(\alpha,\frac{r}{k})$ 。
```{dropdown} Solution

因为 $k>0$ ，所以 $y=kx$ 是严格增函数，它仍在 $(0,+\infty)$ 上取值，其反函数 $x=\frac{y}{k}$ 。

- 当 $y<0$ 时， $p_{Y}(y)=0$ ；
- 当 $y\ge0$ 时，我们根据上述定理有

$$
\begin{eqnarray*}
p_{Y}(y)&=&p_{X}\left(\frac{y}{k}\right) \cdot \frac{1}{k} \\
&=&\frac{\lambda^{\alpha}}{\Gamma(\alpha)}\left(\frac{y}{k}\right)^{\alpha-1} e^{-\lambda \frac{y}{k}} \cdot \frac{1}{k} \\
&=&\frac{\left(\frac{\lambda}{k}\right)^{\alpha}}{\Gamma(\alpha)} y^{\alpha-1} e^{-\frac{\lambda}{k} y}
\end{eqnarray*}
$$

即 $Y\sim Ga(\alpha,\frac{\lambda}{k})$ 。

```
`````

````{prf:corollary}
若随机变量 $X$ 的分布函数 $F_{X}(x)$ 为严格单调增的连续函数，其反函数 $F_{X}^{-1}(y)$ 存在，则 $Y=F_{X}(X)$ 服从 $(0,1)$ 上的均匀分布 $U(0,1)$ 。


```{dropdown} Proof
首先注意到 $Y=F_{X}(X)$ 是一个随机变量，于是，我们需要求其分布函数。由于根据分布函数的有界性，分布函数 $F_{X}(x)$ 仅在 $[0,1]$ 区间上取值，故当 $y<0$ 时，因为 $\left \{ F_{X}(X)\leq y \right \}$ 是不可能事件，所以

$$F_{Y}(y)=P(Y \leqslant y)=P\left(F_{X}(X) \leqslant y\right)=0$$

当 $y\geq 1$ 时，因为 $\left \{ F_{X}(X)\le y \right \}$ 是必然事件，所以

$$F_{Y}(y)=P(Y \leqslant y)=P\left(F_{X}(X) \leqslant y\right)=1.$$

当 $0\leq y<1$ 时，有

$$
\begin{eqnarray*}
F_{Y}(y) &=&P(Y \leqslant y) \\
&=&P\left(F_{X}(X) \leqslant y\right) \\
&=&P\left(F_{X}^{-1}\left(F_{X}(X)\right) \leqslant F_{X}^{-1}(y)\right) \\
&=&P\left(X \leqslant F_{X}^{-1}(y)\right) \\
&=&F_{X}\left(F_{X}^{-1}(y)\right) \\
&=&y
\end{eqnarray*}
$$

综上所述， $Y=F_{X}(X)$ 的分布函数为

$$F_{Y}(y)=\left\{
\begin{aligned}
& 0 &,y<0 \\
& y &,0 \leq y<1 \\
& 1 &,y \geqslant 1
\end{aligned}\right.$$

因此， $Y\sim U(0,1)$ 。
```

````


```{admonition} Remark

- 任一个连续随机变量 $X$ 都可通过其分布函数 $F(x)$ 与均匀分布随机变量 $U$ 有关联。
- $X\sim {Exp}(\lambda)$ ，其分布函数 $F(x)=1-e^{-\lambda x}$ 。于是，

$$U=1-e^{-\lambda x} \Rightarrow x=\frac{1}{\lambda} \ln \frac{1}{1-u}.$$

这表明了由均匀分布 $U(0,1)$ 的随机数 $u_{i}$ 可得指数分布 ${Exp}(\lambda)$ 的随机数

$$x_{i}=\frac{1}{\lambda} \cdot \ln \frac{1}{1-u_{i}} \quad i=1,2, \cdots, n, \cdots,$$

这是 Monte Carlo 法的基础。

```

## $g(\cdot)$ 是其他特殊形式

`````{prf:example}
 $X\sim N(0,1)$ ，求 $Y=X^{2}$ 的密度函数。
```{dropdown} Solution

先求 $Y$ 的分布函数 $F_{Y}(y)$ 。由于 $Y=X^{2}\ge 0$ ，故当 $y\leq 0$ 时，有 $F_{Y}(y)=0$ ，从而 $P_{Y}(y)=0$ .
当 $y>0$ 时，有

$$F_{Y}(y)=P(Y \leqslant y)=P\left(X^{2} \leqslant y\right)=P(-\sqrt{y} \leqslant X \leqslant \sqrt{y})=2 \Phi(\sqrt{y})-1$$

因此， $Y$ 的分布函数为

$$F_{Y}(y)=\left\{\begin{array}{cc}
2 \Phi(\sqrt{y})-1 & ,y>0 \\
0 & , y \leq 0
\end{array}\right.$$

再用求导的方式求出 $Y$ 的密度函数

$$p_{Y}(y)=\left\{\begin{array}{cc}
\varphi(\sqrt{y}) \cdot y^{-\frac{1}{2}} & ,y>0 \\
0 & , y \leqslant 0
\end{array}=\left\{\begin{array}{cc}
\frac{1}{\sqrt{2 \pi}} y^{-\frac{1}{2}} e^{-\frac{y}{2}} & ,y>0 \\
0 & ,y \leqslant 0
\end{array}\right.\right.$$

称 $Y$ 服从自由度为 $1$ 的卡方分布，记 $\chi ^{2}(1)$ 。
```
`````

```{admonition} Remark
可以发现，这个分布也是伽马分布，即 $Ga(\frac{n}{2},\frac{1}{2})=\chi ^{2}(n)$ 。
```