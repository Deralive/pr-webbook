# 极值分布
 $\max$ 和 $\min$ 是两种常见的运算，其广泛的应用于风险管理问题中。比如：上海地区今年最高气温达到 40 摄氏度的概率有多大？这里我们利用两个例题来阐述在不同的条件下如何计算极值的分布。

`````{prf:example}
设 $X_1,X_2,\cdots,X_n$ 是相互独立的 $n$ 个随机变量，若 $Y=\max\{X_1,X_2,\cdots,X_n\}$ ，在以下情况下求 $Y$ 的分布。

- 若 $X_i \sim F_i(x),i=1,2,\cdots,n$ ，则 $Y=\max\{X_1,X_2,\cdots,X_n\}$ 的分布函数为

$$
\begin{eqnarray*}
F_Y(y) &=& P(Y\leq y)\\
&=& P(\max\{X_1,X_2,\cdots,X_n\}\leq y)\\
&=& P(X_1\leq y,X_2\leq y,\cdots,X_n \leq y)\\
&=& P(X_1\leq y) P(X_2\leq y) \cdots P(X_n \leq y)\\
&=& \prod_{i=1}^n F_{i}(y).
\end{eqnarray*}
$$

- 若诸 $X_i$ 同分布，即 $X \sim F(x), i=1,2,\cdots,n$ ，则
 $Y$ 的分布函数为

$$
F_Y(y) = \left(F(y)\right)^n.
$$

- 若诸 $X_i$ 为连续随机变量，且诸 $X_i$ 同分布，即 $X_i$ 的密度函数为 $p(x),i=1,2,\cdots,n$ ，则 $Y$ 的分布函数仍为

$$
F_Y(y) = \left(F(y)\right)^n.
$$

而 $Y$ 的密度函数为

$$
\begin{eqnarray*}
p_Y(y) &=& \frac{\text{d}}{\text{d}y}F_Y(y) \\
&=& n \left(F(y)\right)^{n-1} p(y).
\end{eqnarray*}
$$

- 若 $X_i \sim Exp(\lambda),i=1,2,\cdots,n$ ，则
 $Y$ 的分布函数为

$$
F_Y(y) = \left\{
\begin{aligned}
& (1-e^{-\lambda y})^n, & y\geq 0\\
& 0, & y < 0\\
\end{aligned}
\right.
$$

而 $Y$ 的密度函数为

$$
p_Y(y) = \left\{
\begin{aligned}
& n(1-e^{-\lambda y})^{n-1}\cdot \lambda e^{-\lambda y} , & y\geq 0\\
& 0, & y < 0\\
\end{aligned}
\right.
$$

`````

`````{prf:example}
设 $X_1,X_2,\cdots,X_n$ 是相互独立的 $n$ 个随机变量，若 $Z=\min\{X_1,X_2,\cdots,X_n\}$ ，在以下情况下求 $Z$ 的分布。

- 若 $X_i \sim F_i(x),i=1,2,\cdots,n$ ，则 $Z=\min\{X_1,X_2,\cdots,X_n\}$ 的分布函数为

$$
\begin{eqnarray*}
F_Z(z) &=& P(Z\leq z)\\
&=& P(\min\{X_1,X_2,\cdots,X_n\}\leq z)\\
&=&1 - P(\min\{X_1,X_2,\cdots,X_n\} > z)\\
&=& 1- P(X_1> z,X_2> y,\cdots,X_n >z)\\
&=& 1-P(X_1>z) P(X_2>z) \cdots P(X_n>z)\\
&=& 1- \prod_{i=1}^n\left( 1-F_{i}(z)\right).
\end{eqnarray*}
$$

- 若诸 $X_i$ 同分布，即 $X \sim F(x), i=1,2,\cdots,n$ ，则
 $Z$ 的分布函数为

$$
F_Z(z) = 1-\left(1-F(z)\right)^n.
$$

- 若诸 $X_i$ 为连续随机变量，且诸 $X_i$ 同分布，即 $X_i$ 的密度函数为 $p(x),i=1,2,\cdots,n$ ，则 $Z$ 的分布函数仍为

$$
F_Z(z) =1- \left(1-F(z)\right)^n.
$$

而 $Z$ 的密度函数为

$$
\begin{eqnarray*}
p_Z(z) &=& \frac{\text{d}}{\text{d}z}F_Z(z) \\
&=& n \left(1-F(z)\right)^{n-1} p(z).
\end{eqnarray*}
$$

- 若 $X_i \sim Exp(\lambda),i=1,2,\cdots,n$ ，则
 $Z$ 的分布函数为

$$
F_Z(z) = \left\{
\begin{aligned}
& 1-e^{-n\lambda z}, & z\geq 0\\
& 0, & z < 0\\
\end{aligned}
\right.
$$

而 $Z$ 的密度函数为

$$
p_Y(y) = \left\{
\begin{aligned}
& n\lambda e^{-n\lambda z}, & z\geq 0\\
& 0, & z < 0\\
\end{aligned}
\right.
$$

`````