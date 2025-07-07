# 随机变量的独立性

```{admonition} Question
请同学们回顾一下 $n$ 个随机事件相互独立是如何定义的？
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

```{admonition} Question
为什么我们常常假定变量是满足独立性？
```