# 概率密度函数

概率密度函数 $p(x)$ 的值虽不是概率，但乘微分元 $\text{d} x$ 就可以得小区间 $(x,x+\text{d}x)$ 上概率的近似值，即

$$
p(x)\text{d}x = P(x<X<x+\text{d}x)
$$

在 $(a,b)$ 上很多相邻的微分元的累积就得到 $p(x)$ 在 $(a,b)$ 上的积分，这个积分值就是 $X$ 在 $(a,b)$ 上取值的概率，即：

$$
\int_{a}^b p(x)\text{d}x = P(a<X<b)
$$

特别，在 $(-\infty,x]$ 上 $p(x)$ 的积分就是分布函数 $F(x)$ ，即

$$
\int_{-\infty}^x p(t)\text{d} t = P(X\leq x)=F(x)
$$

这一关系式是连续随机变量 $X$ 的概率密度函数 $p(x)$ 最本质的属性。

概率密度函数
: 设随机变量 $X$ 的分布函数为 $F(x)$ ,如果存在实数轴上的一个非负可积函数 $p(x)$ ，使得对任意实数 $x$ 有

$$
F(x) = \int_{-\infty}^{x} p(t) d t
$$

那么称 $p(x)$ 为 $X$ 的概率密度函数（probability density function, p.d.f.)。称随机变量 $X$ 为连续型随机变量，其分布函数 $F(x)$ 是连续分布函数。

````{prf:theorem}
连续型随机变量 $X$ 的概率密度函数 $p(x)$ ，其具有
1. 非负性  $p(x) \geqslant 0$ ；
2. 正则性  $\int_{-\infty}^{\infty} p(x) d x = 1$ 。

```{prf:remark}
:class: dropdown
上述两条也是判别某个函数是否为密度函数的充要条件。
```
````

`````{prf:example}
向区间 $(0,a)$ 上任意投点，用 $X$ 表示其坐标。设这个点落在 $(0,a)$ 中任一小区间的概率与这个小区间的长度成正比，而与小区间位置无关。求 $X$ 的分布函数和密度函数。

````{dropdown} Solution

记 $X$ 的分布函数为 $F(x)$ ,则
- 当 $x<0$ 时，因为 $\{X \leq x\}$ 是不可能事件,所以 $F(x)=P( X \leq x)=0$ ；
- 当 $x \geq a$ 时，因为 $\{X \leq x\}$ 是必然事件,所以 $F(x)=P( X \leq x)=1$ ；
- 当 $0 \leq x <a $  时，  $F(x) =P(X \leq x)=P(0 \leq X \leq x) = k x$ ，其中 $k$ 为比例系数。因为 $F(a)=ka=1$ ，所以 $k = \frac{1}{a}$ 。于是，分布函数为

$$
F(x)=\left\{\begin{aligned}
      0, &\quad  x<0 \\
  \frac{x}{a}, & \quad 0 \leq x<a \\
  1, &\quad  x \geq a.
  \end{aligned}\right.
$$

令 $X$ 的密度函数 $p(x)$ ，
- 当 $x<0$ 或 $x>a$ 时， $p(x)=F'(x)=0$ ；
- 当 $x>a$ 时， $p(x)=F'(x)=0$ ；
- 当 $0< x< a$ ， $p(x) = F'(x) =  \frac{1}{a}$ .

而在 $x=0$ 和 $x=a$ 处， $p(x)$ 可取任意值，一般就近取值为宜，这不会影响概率的计算。于是， $X$ 的概率密度是

$$
p(x)= \left\{\begin{aligned}
\frac{1}{a}, &\quad  0<x<a \\
0, & \quad \text { 其他 }
\end{aligned}\right.
$$

```{prf:remark}
:class: dropdown
这个分布就是区间 $(0,a)$ 上的均匀分布，记 $U(0, a)$ 。
```
````
`````

````{prf:example}
验证

$$
f(x)=\left\{\begin{aligned}
\frac{1}{2 \sqrt{x}}, &\quad  0<x<1 \\
0, & \quad \text { 其他 }
\end{aligned}\right.
$$

是否为一个随机变量 $X$ 的概率密度函数?

```{dropdown} Solution
【思路】验证 $f(x)$ 是否满足非负性和正则性。具体证明过程由同学们课后证明。
```

````


```{admonition} Remark
比较密度函数与分布列的异同：
- 已知概率分布列或概率密度函数，可以求出概率分布函数或概率值；
- 离散随机变量的分布函数 $F(x)$ 总是右连续的阶梯函数；而连续随机变量的分布函数 $F(x)$ 一定是整个数轴上的连续函数，
    其增量为
    
    $$
    F(x+\Delta x)-F(x)=\int_{x}^{x+\Delta x} p(t) d t \rightarrow 0(\Delta x \rightarrow 0)
    $$
    
- 离散型随机变量 $X$ 在其可能取值的点 $x_1,x_2,...,x_n,...,$ 上的概率不为 $0$ ，而连续随机变量 $X$ 在( $-\infty,+\infty$ )上任一点 $a$ 的概率恒为 $0$ ，
    即 $P(x=a)=\int_{a}^{a} p(x) d x=0$ 。这可以作为以下观点的一个例子：不可能事件的概率为 $0$ ，但概率为 $0$ 的事件不一定是不可能事件。类似地，必然事件的概率为 $1$ ，但概率为1的事件不一定是必然事件。

- 连续型随机变量 $P(a \leq X \leq b)=P(a<X \leq b)=P(a \leq X<b)=P(a<X<b)$ ，但离散型随机变量并不满足这个性质，要"点点计较"。
- 由于在若干点上改变概率密度函数 $p(x)$ 的值并不影响其积分值，从而不影响分布函数 $F(x)$ 的值。这意味着一个连续分布的密度函数不唯一。
```