# 随机向量的联合分布函数

对任意 $n$ 个实数 $x_{1}, x_{2}, \cdots, x_{n}$ ， $n$ 个事件 $\left\{X_{1} \leqslant x_{1}\right\},\left\{X_{2} \leqslant x_{2}\right\},...,\left\{X_{n} \leqslant x_{n}\right\}$ 同时发生的概率

$$
\begin{eqnarray*}
F\left(x_{1}, x_{2}, \cdots, x_{n}\right)&=&P\left( \{X_{1} \leqslant x_{1}\} \cap \{X_{2} \leqslant x_{2}\}\cap \cdots\cap \{X_{n} \leqslant x_{n}\}\right)\\
&=& P\left(X_{1} \leq x_1, X_2 \leq x_2,\cdots,X_n \leq x_{n}\right)
\end{eqnarray*}
$$

称为 $n$ 维随机向量 $\mathbf{X}$ 的联合分布函数。

```{admonition} Remark
对于二维随机向量 $(X,Y)'$ ，其联合分布函数为

$$
F(x,y) = P(X\leq x, Y\leq y)
$$

```

``````{prf:theorem} 二维随机变量联合分布函数的性质
:label: thm: property_of_two_dim_rv
任一二维联合分布函数 $F(x,y)$ 必具有如下性质:

- **单调性**： $F(x,y)$ 分别对 $x$ 或 $y$ 是单调非减的，即
当 $x_{1}<x_{2}$ 时，有

$$F\left(x_{1}, y\right) \leq F\left(x_{2}, y\right);$$

当 $y_{1}<y_{2}$ 时，有

$$F\left(x, y_{1}\right) \leq F\left(x, y_{2}\right).$$

- **有界性**:对任意的 $x$ 和 y，有 $0 \leqslant F(x, y) \leqslant 1$ 且

$$
\begin{eqnarray*}
F(-\infty, y)&=&\lim _{x \rightarrow-\infty} F(x, y)=0, \\
F(x,-\infty)&=&\lim _{y \rightarrow-\infty} F(x, y)=0, \\
F(\infty, \infty)&=&\lim _{x, y \rightarrow \infty} F(x, y)=1.
\end{eqnarray*}
$$

- **右连续性**：对每个变量都是右连续的，即

$$
\begin{eqnarray*}
F(x+0, y)&=&F(x, y) \\
F(x, y+0)&=&F(x, y)
\end{eqnarray*}
$$

- **非负性**：对任意的 $a<b,c<d$ 有

$$
\begin{eqnarray*}
P(a<X \leq b, c<Y \leqslant d) &=&F(b, d)-F(a, d)-F(b, c)+F(a, c) \geqslant 0
\end{eqnarray*}
$$

``````

```{admonition} Remark

- 具有以上四条性质的二元函数 $F(x,y)$ 一定是某个二维随机变量的分布函数。
- 性质(4)是二维随机向量所特有的，也是合理的，但性质(4)不能由前三条性质推出，因此需要单独列出。

```

`````{prf:example}
设二元函数为

$$G(x, y)=\left\{\begin{array}{ll}
0 & x+y<0 \\
1 & x+y \geqslant 0
\end{array}\right. $$

可以证明其满足前三个性质（这里留给学生课后完成），但该函数不满足性质 4。考虑在 $(-1,-1),(1,-1),(-1,1),(1,1)$ 所围成的正方形上的面积。
`````