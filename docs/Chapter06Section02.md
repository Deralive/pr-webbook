# 数学期望 

数学期望
: 分为离散型和连续型两种定义。

- 假设 $X$ 为一个离散随机变量，其分布列记为
 $p_{i}=P\left(X=x_{i}\right) \quad i=1.2, \cdots, n, \cdots$ 。
如果 $\sum_{i=1}^{\infty}\left|x_{i}\right| p_{i}<\infty$ ，则称

$$E(x)=\sum_{i=1}^{\infty} x_{i} p\left(x_{i}\right)$$

为随机变量 $X$ 的（数学）期望或均值。

- 假设 $X$ 为一个连续随机变量，其密度函数 $p(x)$ 。如果 $\int_{-\infty}^{+\infty}|x| p(x) d x<\infty$ ，则称 

$$E(x)=\int_{-\infty}^{+\infty} x p(x) d x$$

为随机变量 $X$ 的（数学）期望或均值。

```{admonition} Remark
如果 $\sum_{i=1}^{\infty}\left|x_{i}\right| p_{i}$ 或 $\int_{-\infty}^{+\infty}|x| p(x)$ 不收敛，则称 $X$ 的期望不存在。
```

`````{prf:example}
设 $X$ 服从区间 $(a,b)$ 上的均匀分布，求 $E(X)$ .

```{dropdown} Solution
因为 $X$ 的密度函数为

$$
p(x) = \left\{
\begin{aligned}
& \frac{1}{b-a}, & a<x<b,\\
& 0, & \text{其他}.
\end{aligned}
\right.
$$

所以，

$$
E(X) = \int_{a}^b x \frac{1}{b-a}\text{d} x = \frac{1}{b-a} \left.\frac{x^2}{2}\right|_a^b = \frac{a+b}{2}.
$$

```
`````

`````{prf:example}
:label: ex:chap06_discrete_rv_expectation
如果 $X$ 的分布列为

```{list-table} $X$ 的分布列
:header-rows: 1
:name: tab6.2.1
* - $X$
   - -1
   - 0
   - 1
* - $P$
   - $\frac{1}{3}$
   - $\frac{1}{3}$
   - $\frac{1}{3}$
```

那么 $E(X) = 0$ 。而 $X^2$ 的分布列为

```{list-table} $X^2$ 的分布列
:header-rows: 1
:name: tab6.2.2
* - $X^2$
   - 0
   - 1
* - $P$
   - $\frac{1}{3}$
   - $\frac{2}{3}$
```

那么 $E(X^2) = \frac{2}{3}$ 。
`````
