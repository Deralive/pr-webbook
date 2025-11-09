# 按分布收敛
在学习泊松分布时，泊松分布是二项分布的一种近似，见定理 {prf:ref}`thm04-d` 。若设 $X_n \sim b(n,p_n)$ ，其分布函数为 $F_n(x)$ ，且 $X \sim P(\lambda)$ ， $p=\lim_{n\rightarrow} np_n$ ，其分布函数为 $F(x)$ 。
对于分布函数序列 $\{F_n(x)\}$ ，根据泊松定理可知，当 $n$ 充分大时，其收敛到一个极限分布函数 $F(x)$ 。

```{admonition} Question
如何定义分布函数序列 ${F_n(x)}$ 的收敛性?
```

一个很自然的想法是——对于任意的 $x\in R$ ，当 $n\rightarrow +\infty$ 时，有

$$
F_n(x) \rightarrow F(x).
$$

这也就是“点点收敛”，但是这个要求过于严格了。以下例子正好说明了这个问题。

`````{prf:example}
我们考虑以下随机变量序列 $\{X_n\}$ 的分布列，即

$$P\left(X_{n}=\frac{1}{n}\right)=1 \quad n=1.2, \cdots.$$

于是，其分布函数为

$$F_{n}(x)=\left\{\begin{aligned}
&0,& x<\frac{1}{n}, \\
&1,& x \geqslant \frac{1}{n}.
\end{aligned}\right.$$

那么，对于任意的 $x$ ， $F_n(x)$ 的极限函数为

$$
g(x)=\left\{\begin{aligned}
&0, & x \leq 0, \\
&1, & x>0.
\end{aligned}\right.$$

然而，我们发现 $g(x)$ 并不满足右连续性，所以， $g(x)$ 不是一个随机变量的分布函数。由此，随机变量序列的分布函数的极限不是一个随机变量的分布函数，这是不合理的。
我们发现，随机变量 $X_n$ 的分布函数 $F_n(x)$ 是在点 $x_0=\frac{1}{n}$ 处有跳跃点。当 $n \rightarrow +\infty$ 时，跳跃点 $x_0 \rightarrow 0$ 。可以证明

$$
F(x)=\left\{\begin{aligned}
&0, & x<0 \\
&1, & x \geqslant 0
\end{aligned}\right.
$$

是一个随机变量的分布函数。对于任意的 $x \in (-\infty,0)\cup (0,+\infty)$ ，有 $\lim_{n\rightarrow +\infty} F_n(x) = F(x)$ 。但在 $x=0$ 处，

$$\lim _{n \rightarrow \infty} F_{n}(0)=0 \neq 1=F_{n}(0).$$

`````

```{admonition} Remark
在上面的例子中，分布函数的收敛性不成立的点 $x=0$ 恰好是 $F(x)$ 的间断点（或跳跃点）。我们在定义分布函数的收敛性仅需要考虑 $F(x)$ 的连续点。
```

设随机变量 $X, X_{1}, X_{2}, \cdots, X_{n}, \cdots$ 的分布函数分别为 $F(x),F_1(x),F_2(x),\cdots,F_n(x),\cdots$ 。若对 $F(x)$ 的任意连续点 $x$ ，都有

$$\lim _{n \rightarrow \infty} F_{n}(x)=F_{(x)}.$$

则称 $F_n(x)$ 弱收敛与 $F(x)$ ,记作

$$F_{n}(x) \stackrel{\omega}{\longrightarrow} F(x).$$

也称相应的随机变量序列 ${X_n}$ 按分布收敛于 $X$ ,

$$X_{n} \stackrel{L}{\longrightarrow} X.$$

如果 $F(x)$ 是连续函数，那么弱收敛就点点收敛。

`````{prf:property}

- $X_{n} \stackrel{P}{\rightarrow} X \Rightarrow X_{n} \stackrel{L}{\rightarrow} X$ ；
- 如果 $c$ 是一个常数，那么 $X_{n} \stackrel{P}{\rightarrow} c \Leftrightarrow X_{n} \stackrel{L}{\rightarrow} c$ 。

`````