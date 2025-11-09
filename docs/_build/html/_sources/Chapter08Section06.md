# 随机变量的独立性

```{admonition} Question
请同学们回顾一下 $n$ 个随机事件相互独立是如何定义的？
```

独立性
: 设 $n$ 维随机变量 $\left(X_{1}, X_{2}, \cdots, X_{n}\right)'$ 的联合分布函数 $F(x_{1}, x_{2}, \cdots, x_{n})$ ， $F_{i}\left(x_{i}\right)$ 为 $X_{i}$ 的边际分布函数。如果对任意 $n$ 个实数 $x_{1}, x_{2}, \cdots, x_{n}$ 有

$$F\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\prod_{i=1}^{n} F_{i}(x_{i})$$

则称 $X_{1}, X_{2}, \cdots, X_{n}$ 相互独立。

- 在离散随机变量场合，如果对其任意 $n$ 个取值 $x_{1}, x_{2}, \cdots, x_{n}$ 有

$$P\left(X_{1}=x_{1}, X_{2}=x_{2}, \ldots, X_{n}=x_{n}\right)=\prod_{i=1}^{n} P\left(X_{i}=x_{i}\right)$$

则称 $X_{1}, X_{2}, \cdots, X_{n}$ 相互独立。

- 在连续随机变量场合，如果对其任意 $n$ 个实数 $x_{1}, x_{2}, \cdots, x_{n},$ 有

$$p\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\prod_{i=1}^{n} p_{i}\left(x_{i}\right)$$

则称 $X_{1}, X_{2}, \cdots, X_{n}$ 相互独立。

`````{prf:example}
若二维随机变量 $(X,Y)$ 的联合密度函数为

$$
p(x,y) = \left\{
\begin{aligned}
& 8xy, & 0\leq x \leq y \leq 1 \\
& 0, & \text{其他}
\end{aligned}
\right.
$$

问 $X$ 和 $Y$ 是否相互独立？

```{dropdown} Solution

我们需要求出 $X$ 和 $Y$ 的边际密度函数。因为 $X$ 的边际密度函数为

$$
p_X(x) = \int_{-\infty}^{\infty} p(x,y)\text{d}y = \int_{x}^{1} 8xy \text{d}y = 4x(1-x^2), 0<x<1.
$$

而 $Y$ 的边际密度函数为

$$
p_Y(y) = \int_{-\infty}^{\infty} p(x,y)\text{d}x = \int_{0}^{y} 8xy \text{d}y = 4y^3, 0<y<1.
$$

因为 $(X,Y)$ 联合密度函数不等于 $X$ 和 $Y$ 边际密度函数的乘积，所以 $X$ 和 $Y$ 不独立。
```

`````

```{admonition} Question
为什么我们常常假定变量是满足独立性？
```