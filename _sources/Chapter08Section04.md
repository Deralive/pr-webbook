# 边际分布函数

边际分布函数
: 如果二维随机变量 $(X,Y)$ 的联合分布函数为 $F(x,y)$ ，那么，称

$$F_X(x) = P(X\leq x) = P(X\leq x, Y< \infty) = \lim_{y\rightarrow \infty} F(x,y)$$

为 $X$ 的边际分布。
类似地，称

$$
F_Y(y) = F(\infty,y)
$$

为 $Y$ 的边际分布。

`````{prf:example}
设二维随机变量 $(X,Y)$ 的联合分布函数为

$$
F(x,y) = \left\{
\begin{aligned}
&1-e^{-x} - e^{-y} + e^{-x-y-\lambda xy}, &x>0,y>0.\\
&0, &\text{其他}.
\end{aligned}
\right.
$$

这个分布被称为二维指数分布，其中参数 $\lambda>0$ 。求 $X$ 的边际分布函数。
```{dropdown} Solution

 $X$ 的边际分布函数为

$$
\begin{eqnarray*}
F_{X}(x) = \lim_{y\rightarrow\infty} F(x,y) = \left\{
\begin{aligned}
& 1 - e^{-x}, & x>0,\\
& 0 , & \text{其他}.
\end{aligned}
\right.
\end{eqnarray*}
$$

```
`````

学生课后可以自行求 $Y$ 的边际分布函数。