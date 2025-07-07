# 分布函数

为了掌握随机变量 $X$ 的统计规律，我们只需要掌握 $X$ 的各种取值的概率。由于：

\begin{eqnarray*}
&\{a < X \leq b\} = \{X\leq b\} - \{X\leq a\}\\
& \{X > c\} = \Omega - \{X \leq c\}
\end{eqnarray*}

因此对任意实数 $x$ ，只要确定事件 $\{X\leq x\}$ 的概率就足够了。

分布函数
: 设 $X$ 为一个随机变量。对任意实数 $x$ ，称：

$$
F(x) = P(X\leq x)
$$

为随机变量 $X$ 的**累积分布函数**，简称**分布函数**。也称 $X$ 服从 $F(x)$ ，记 $X\sim F(x)$ 。

```{prf:remark}

任一随机变量 $X$ 都有一个分布函数。
```

````{prf:theorem} 
:label: thm03-a

任一分布函数 $F(x)$ 都具有以下三条基本性质：
- **单调性**： $F(x)$ 是定义在整个实数轴 $(-\infty,\infty)$ 上的单调非减函数，即对任意 $x_1<x_2$ ，有：

$$
F(x_1)\leq F(x_2).
$$

- **有界性**：对任意的 $x$ ，有 $0 \leq F(x) \leq 1$ ，且：

$$
\left\{\begin{aligned}
F(-\infty)&=&\lim _{x \rightarrow-\infty} F(x)=0 \\
F(\infty)&=&\lim _{x \rightarrow \infty} F(x)=1
\end{aligned}\right.
$$

- **右连续性**： $F(x)$ 是 $x$ 的右连续函数，即对任意的 $x_0$ ，有：

$$
 \lim \limits_{x \rightarrow x_0 +0} F(x_0)=0
$$
 
 即
 
$$
  F(x_0 + 0) = F(x_0)
$$

```{dropdown} Proof

- 设事件 $A =\left\{\omega: X(\omega) \leqslant x_{1}\right\} \quad B=\left\{\omega: X(\omega) \leqslant x_{2}\right\}$ 。若 $x_1<x_2$ ，那么 $A \subset B$ 。根据概率的单调性：

$$
P\left(x \leqslant x_{1}\right)=P(A) \leqslant P(B)=P\left(X \leqslant x_{2}\right)
$$

即 $F(x_1) \leq F(x_2)$ 。

- 因为 $F(x) = P(X \leq x)$ 表示事件 ${X \leq x}$ 的概率。所以， $0 \leq F(x) \leq 1$ 。根据 $F(x)$ 的单调性可知： $F(\lfloor x\rfloor) \leqslant F(x) \leqslant F(\lceil x\rceil)$ 。
对于整数 $m$ 和 $n$ ，

$$
\lim _{x \rightarrow-\infty} F(x)=\lim _{m \rightarrow-\infty} F(m) \quad \lim _{x \rightarrow \infty} F(x)=\lim _{x \rightarrow \infty} F(n)
$$

存在。由于概率的可列可加性：

  $$
  \begin{aligned}
1 &=P(-\infty<X<+\infty) \\
&=P\left(\bigcup_{i=-\infty}^{+\infty}\{i-1<X \leqslant i\}\right) \\
&=\sum_{i=-\infty}^{+\infty} P(i-1<X \leqslant i) \\
&=\lim _{n \rightarrow \infty} \lim _{n \rightarrow \infty} \sum_{i=m}^{n} {P(i-1<X \leqslant i)}{}=\lim _{n \rightarrow \infty} \lim _{m \rightarrow-\infty} P(m<X \leqslant n) \\
&=\lim _{n \rightarrow \infty} F(n)-\lim _{m \rightarrow-\infty} F(m) \Rightarrow 1 \geqslant \lim _{n \rightarrow \infty} F(n)=1+\lim _{m \rightarrow \infty} F(m) \geqslant 1 \\
\end{aligned}
  $$
  
因此， $\lim \limits_{n \rightarrow \infty} F(x)=1=\lim \limits_{x \rightarrow \infty} F(x) \quad ; \lim \limits_{m \rightarrow-\infty} F(m)=0=\lim \limits_{x \rightarrow \infty} F(x)$ 。

- 因为 $F(x)$ 是有界、单调函数，所以其任一点 $x_0$ 的右极限 $F(x_0 +0)$ 存在。考虑数列 $x_1>x_2>...>x_n>...>x_0$ ，当 $x_n \Rightarrow x_0(n \Rightarrow \infty)$ 时：

$$\begin{aligned}
F\left(x_{1}\right)-F\left(x_{0}\right) &=P\left(x_{0}<x \leqslant x_{1}\right)=P\left(\bigcup_{i=1}^{\infty}\left\{x_{i+1}<x \leqslant x_{i}\right\}\right) \\
&=\sum_{i=1}^{\infty} P\left(x_{i+1}<x \leqslant x_{i}\right)=\sum_{i=1}^{\infty} F\left(x_{i}\right)-F\left(x_{i+1}\right) \\
&=\lim _{n \rightarrow \infty} \sum_{i=1}^{n}\left[F\left(x_{i}\right)-F\left(x_{i+1}\right)\right]=F\left(x_{1}\right)-\lim _{n \rightarrow \infty} F\left(x_{n}\right) \\
\end{aligned}$$

因此， $F\left(x_{0}\right) =\lim _{n \rightarrow \infty} F\left(x_{n}\right)=F\left(x_{0}+0\right)$ 。
```
```{prf:remark} 
:class: dropdown

- 这三条基本性质也是判断某个函数是否为某个随机变量的分布函数的充要条件。
- 利用分布函数，我们可以容易地计算概率
	- $P(X>x) = 1- F(x)$ ;
	- $P(X<x) = F(x-0) = \lim_{y \rightarrow x-} F(y)$ ;
	- $P(X =x) = F(x) - F(x-0)$ ;
	- $P(X\geq x) = 1- F(x-0)$ ;
	- $P(a<X\leq b) = F(b) - F(a)$ ;
	- $P(a<X<b) = F(b-0)-F(a)$ ; 
	- $P(a\leq X < b) = F(b-0) - F(a-0)$ ;
	- $P(a\leq X\leq b) = F(b) - F(a-0)$ .

- 特别地， $F(x)$ 在 $a,b$ 处连续时，有 $F(a-0)=F(a) \quad F(b-0)=F(b)$ 。
```
````

```{prf:example}
:label: ex03-c

对于反正切函数：

$$F(x)=\frac{1}{\pi}\left(\arctan x+\frac{\pi}{2}\right),-\infty<x<\infty$$

我们可以发现：

- $F(x)$ 是连续且严格单调增函数；
- $F(\infty) = 1$ 且 $F(-\infty) = 0$ ；
- $F(x)$ 是某个随机变量的分布函数，该分布为柯西分布。
- 设 $X$ 为一个服从柯西分布的随机变量，则

\begin{eqnarray*}
        P(-1\leq X \leq 1) &=& F(1) - F(-1) \\&=& \frac{1}{\pi}\left(\arctan(1) - \arctan(-1)\right)\\
        &=&\frac{1}{2}
\end{eqnarray*}
```


