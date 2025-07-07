# 常见的连续随机变量

## 均匀分布

均匀分布
: 设定义在区间 $(a,b)$ 的一个随机变量 $X$ ，其中 $a<b$ 为两个未知参数。 $X$ 的概率密度函数为：

$$
p(x) = \frac{1}{b-a}, a< x<b
$$

称 $X$ 的分布为均匀分布。记 $X\sim U(a,b)$ 。

## 正态分布

正态分布
: 设定义在区间 $(-\infty,\infty)$ 的一个随机变量 $X$ 。 $X$ 的概率密度函数为：

$$
p(x) =\frac{1}{\sqrt{2\pi \sigma^2}}\exp\left\{-\frac{1}{2\sigma^2} (x-\mu)^2\right\}, x \in R
$$

称 $X$ 的分布为正态分布。记 $X\sim N(\mu,\sigma^2)$ ，其中参数 $\mu \in R, \sigma^2 >0$ 。

```{prf:remark}
1. 正态分布是最早由法国数学家棣莫弗（Abraham de Moivre）在近似二项分布时得到的，后由德国数学家高斯（Carolus Fridericus Gauss）在测量误差时导出。因高斯的工作对后世的贡献巨大，所以，正态分布又称**高斯分布**。
2. 概率密度函数 $p(x)$ 是一条钟型曲线，特点为：中间高，两边低，左右对称。
3. 正态分布的两个参数 $\mu$ 和 $\sigma^2$ 是决定密度函数位置和形状，称 $\mu$ 为位置参数， $\sigma^2$ 是尺度参数。
```

这里很自然我们构建一个正态分布类，即：

$$
\mathcal{P} = \{N(\mu,\sigma^2):\mu \in R, \sigma^2 >0\}
$$

其中有个极为特殊的正态分布——标准正态分布，即 $\mu = 0,\sigma^2 = 1$ 。下面我们具体讲解。

```{prf:remark}
1. 标准正态分布的密度函数为：

$$
\phi(z) = \frac{1}{\sqrt{2\pi}} \exp\left\{-\frac{1}{2}z^2\right\}
$$

2. 标准正态分布的分布函数为：

$$
\Phi(z) = \int_{-\infty}^z \phi(x)\text{d} x
$$

3. 标准正态分布的概率计算常用公式：

   a. $\Phi (-z)=P(Z\le -z)=P(Z\ge z)=1-\Phi(z)$   
   b. $P(Z>z)=1-\Phi(z)$   
   c. $P(a<Z<b)=\Phi(b)-\Phi(a)$   
   d. $P(\left | Z \right | <c)=2\Phi(c)-1， (c\ge 0)$ 
```

```{prf:theorem}
:label: property:standard_normal
若随机变量 $X\sim N(\mu,\sigma^{2})$ ，则 $Z=\frac{x-\mu }{\sigma } \sim N(0,1)$ 。

记 $X$ 和 $Z$ 的分布函数分别为 $F_{X}(x)$ 和 $F_{Z}(z)$ ，密度函数分别为 $p_{X}(x)$ 和 $p_{Z}(z)$ 。

则由分布函数的定义可知：

::: {math}
:label: eq:chap04_proof_normal_step1
\begin{aligned}
F_{Z}(z)
&=P(Z\le z)\\
&=P\left(\frac{X-\mu }{\sigma } \le z\right)\\
&=P(X\le \mu +\sigma z )\\ % Corrected typo from original LaTeX
&=F_{X} (\mu +\sigma z)
\end{aligned}
:::

由于正态分布函数是严格单调递增且处处可导。因此：
::: {math}
:label: eq:chap04_proof_normal_step2
\begin{aligned}
p_{Z}(z)
&=\frac{\mathrm{d}}{\mathrm{d} z} F_{Z}(z)\\
&=\frac{\mathrm{d}}{\mathrm{d} z} F_{X}(\mu +\sigma z)\\
&= p_{X}(\mu +\sigma z)\cdot \sigma \\
&=\frac{1}{\sqrt{2\pi \sigma ^{2}} } \exp\left\{-\frac{1}{2\sigma ^{2}}(\mu +\sigma z -\mu )^{2} \right\}\cdot \sigma \\
&=\frac{1}{\sqrt{2\pi \sigma ^{2}} } \exp\left\{-\frac{(\sigma z)^{2}}{2\sigma ^{2}} \right\}\cdot \sigma \\
&=\frac{1}{\sqrt{2\pi \sigma ^{2}} } \exp\left\{-\frac{\sigma^2 z^{2}}{2\sigma ^{2}} \right\}\cdot \sigma \\
&=\frac{1}{\sqrt{2\pi \sigma ^{2}} } \exp\left\{-\frac{z^{2}}{2} \right\}\cdot \sigma \\
&=\frac{\sigma}{\sqrt{2\pi \sigma ^{2}} } \exp\left\{-\frac{z^{2}}{2} \right\}\\
&=\frac{\sigma}{\sigma\sqrt{2\pi } } \exp\left\{-\frac{z^{2}}{2} \right\}\\
&=\frac{1}{\sqrt{2\pi } } \exp\left\{-\frac{z^{2}}{2} \right\}\\
\end{aligned}
:::

由此可得：

$$
Z=\frac{x-\mu }{\sigma } \sim N(0,1)
$$
```

```{prf:remark}
   $3\sigma$ 原则：
1. $P(\mu -\sigma <X<\mu +\sigma )=2\Phi(1)-1\approx 0.6826$ 
2. $P(\mu -2\sigma <X<\mu +2\sigma )=2\Phi(2)-1\approx 0.9545$ 
3. $P(\mu -3\sigma <X<\mu +\sigma )=2\Phi(3)-1\approx 0.9973$ 
```

## 指数分布

指数分布
: 设一随机变量 $X$ ，其密度函数为：

$$
p(x)=\left\{\begin{matrix}
\lambda e^{-\lambda x} ,&x\ge 0 \\
0,&x<0
\end{matrix}\right.
$$

则称 $X$ 的分布为指数分布，记 $X\sim Exp(\lambda)$ ，其中参数 $\lambda>0$ 。

根据随机变量的密度函数，可以计算其分布函数为：

$$
F_{X} (x) = \left\{\begin{matrix}
\int_{0}^{x}p(t)dt=\int_{0}^{x}\lambda e^{-\lambda t} dt= e^{-\lambda t}|_{0}^{x} =1-e^{-\lambda x} ,&x\ge 0 \\
0,&x<0
\end{matrix}\right.
$$

类似于几何分布，指数分布也具有无记忆性。

````{prf:theorem} 指数分布的无记忆性
:label: property:no_memory_expential
如果随机变量 $X\sim Exp(\lambda)$ ，则对任意 $s>0,t>0$ 有：

$$
P(X>t+s|X>s)=P(X>t)
$$

```{dropdown} Proof
因为 $X\sim Exp(\lambda)$ ，所以 $P(X>s)=e^{-\lambda s},s>0$ 。又因为 $\left \{ X>s+t \right \} \subset \left \{ X>s \right \}$ ，于是，条件概率：

$$
P(X>s+t|X>s)=\frac{P(X>s+t)}{P(X>s)}=\frac{e^{-\lambda (s+t)} }{e^{-\lambda s} }=e^{-\lambda t}
$$
```
````

泊松分布与指数分布有非常紧密的关系，我们利用以下一个例子来说明。

````{prf:example}
如果某设备在长为 $t$ 的时间 $(0,t)$ 内发生故障的次数 $N(t)$ （与时间长度 $t$ 有关）服从参数为 $\lambda t$ 的泊松分布，且 $N(0)=0$ ，则从 $0$ 时开始首次发生故障的时间 $T$ 服从参数为 $\lambda$ 的指数分布。

```{dropdown} Solution
设 $N(t)\sim P(\lambda t)$ ，即：

$$
P(N(t)=k)=\frac{(\lambda t)^{k} }{k!} e^{-\lambda t} ,k=0,1,\cdots
$$

注意到从 $0$ 时开始首次发生故障的时间 $T$ 是非负随机变量且事件 $\left \{ T\geq t \right \}$ 说明此设备在 $\left [ 0,t \right ]$ 内没有发生故障。即 $\left \{ T\geq t \right \} =\left \{ N(t)=0 \right \} .$ 由此可得：

- 当 $t<0$ 时，有：

$$
F_{T} (t)=P(T\le t)=0
$$

- 当 $t\geq 0$ 时，有：

$$
F_{T} (t)=P(T\le t)=1-P(T> t) = 1-P(T\geq t)=1-P(N(t)=0)=1-e^{-\lambda t}
$$

因此， $T\sim {Exp}(\lambda)$ ，即从 $0$ 时开始首次发生故障的时间 $T$ 服从参数为 $\lambda$ 的指数分布。
```
````

## 伽马分布

伽马函数
: 称

$$
\Gamma (\alpha )=\int_{0}^{+\infty } x^{\alpha -1} e^{-x} dx,\alpha >0
$$

为伽马函数。

根据伽马函数的定义，可以证明伽马函数的一些常用性质。

````{prf:property}
1. $\Gamma (1 )=1, \quad \Gamma (\frac{1}{2} )=\sqrt{\pi }$ ；
2. $\Gamma (\alpha +1 )=\alpha \Gamma(\alpha ), \quad \text{特别地，}\Gamma (n+1 )=n\Gamma(n)=n!$ 。

```{dropdown} Proof
1. 令 $x=u^{2}$ ，于是：

::: {math}
\begin{align*}
\Gamma \left(\frac{1}{2} \right) &= \int_{0}^{+\infty} x^{-\frac{1}{2}} e^{-x} dx \\
&= \int_{0}^{+\infty} u^{-1} e^{-u^{2}} d(u^{2}) \\
&= 2\int_{0}^{+\infty} e^{-u^{2}} du \\
&= \int_{-\infty}^{+\infty} e^{-u^{2}} du \\
&= \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2\pi \cdot \frac{1}{2}}} e^{-\frac{u^{2}}{2(\frac{1}{2})}} du \cdot \sqrt{\pi} \\
&= \sqrt{\pi}.
\end{align*}
:::

2. 这里只需要证明 $\Gamma (\alpha +1 )=\alpha \Gamma(\alpha )$ ，即：

::: {math}
\begin{aligned}
\Gamma (\alpha +1)
&= \int_{0}^{+\infty} x^{\alpha } e^{-x} dx\\
&= \int_{0}^{+\infty} \left ( -x^{\alpha } \right ) d\left ( e^{-x} \right ) \\
&= -x^{\alpha }e^{-x}|_{0}^{+\infty } +\int_{0}^{+\infty} e^{-x} d\left ( x^{\alpha } \right ) \\
&= \int_{0}^{+\infty} \alpha x^{\alpha-1 }e^{-x} dx\\
&= \alpha \Gamma(\alpha ).
\end{aligned}
:::

```
````

基于伽马函数，我们来定义伽马分布。

伽马分布
: 假设 $X$ 为一随机变量，其密度函数为：

$$
p(x)=\left\{\begin{matrix} \frac{\lambda ^{\alpha } }{\Gamma (\alpha )}x^{\alpha -1}e^{-\lambda x} & ,x\ge 0\\ 
0&,x<0\end{matrix}\right.
$$

则称其分布为伽马分布，记作 $X\sim Ga(\alpha,\lambda)$ ，其中 $\alpha>0$ 为形状参数， $\lambda>0$ 为尺度参数。

```{prf:remark}
当 $\alpha = 1$ 时， $Ga(1,\lambda)=Exp(\lambda)$ 。
```

以下例子讲解了泊松分布与伽马分布之间的关系，和之前讲解过的关于泊松分布与指数分布之间的关系的证明过程类似，供学生课后自学。

````{prf:example}
若在 $(0,t)$ 内发生冲击的次数 $N(t)$ 服从参数为 $\lambda t$ 的泊松分布，试证明第 $n$ 次冲击来到的时间 $S_{n}$ 服从伽马分布 $Ga(n,\lambda)$ 。

```{dropdown} Proof
因为事件：

"第 $n$ 次冲击来到的时间 $S_{n}$ 小于等于 $t$ "

等价于事件：

"在 $(0,t)$ 内发生冲击的次数 $N(t)$ 大于等于 $n$ "，即：

$$
\left \{ S_{n} \le t \right \} =\left \{ N(t)\ge n \right \}
$$

于是， $S_{n}$ 的分布函数为：

$$
F(t)=P(S_{n}\le t )=P(N(t)\ge n)=\sum_{k=n}^{+\infty } \frac{(\lambda t)^{k} }{k!} e^{-\lambda t}
$$

令 $a_{k} = \frac{(\lambda t)^{k} }{k!} e^{-\lambda t}$ , $b_{k} = \frac{\lambda ^{k} }{\Gamma (k)}\int_{t}^{+\infty }x^{k-1}e^{-\lambda x}dx$ ，由于：

::: {math}
\begin{aligned}
b_{k}
&=\frac{\lambda ^{k} }{\Gamma (k)}\int_{t}^{+\infty }x^{k-1}e^{-\lambda x}dx \\
&=\frac{\lambda ^{k} }{(k-1)!}\int_{t}^{+\infty }-\frac{1}{\lambda } x^{k-1}d e^{-\lambda x} \\
&=\frac{\lambda ^{k} }{(k-1)!}\left(-\frac{1}{\lambda } x^{k-1}e^{-\lambda x} \Big|_{t}^{+\infty } +\frac{k-1}{\lambda }\int_{t}^{+\infty }x^{k-2} e^{-\lambda x}dx \right)\\
&=\frac{\lambda ^{k} }{(k-1)!}\left(\frac{1}{\lambda } t^{k-1}e^{-\lambda t} +\frac{k-1}{\lambda }\int_{t}^{+\infty }x^{k-2} e^{-\lambda x}dx \right)\\
&=\frac{\lambda ^{k-1} }{(k-1)!} t^{k-1}e^{-\lambda t} +\frac{\lambda ^{k-1} }{(k-2)!}\int_{t}^{+\infty }x^{k-2} e^{-\lambda x}dx \\
&=a_{k-1} +b_{k-1}
\end{aligned}
:::

可得 $a_{k-1} =b_{k}-b_{k-1}$ ，则：

::: {math}
\begin{aligned}
\sum_{k=1}^{n-1} a_{k} &=\sum_{k=1}^{n-1}(b_{k+1}-b_{k})\\
&=(b_{2}-b_{1})+\cdots +(b_{n}-b_{n-1})=b_{n}-b_{1}\\
&=\frac{\lambda ^{n} }{\Gamma (n)}\int_{t}^{+\infty } x^{n-1}e^{-\lambda x} dx-a_{0}
\end{aligned}
:::

且：

::: {math}
\begin{aligned}
b_{1} &=\frac{\lambda }{\Gamma (1)}\int_{t}^{+\infty } e^{-\lambda x} dx\\
&=\lambda \int_{t}^{+\infty } e^{-\lambda x} dx\\
&=-e^{-\lambda x}|_{t}^{+\infty }=e^{-\lambda t}=a_{0}
\end{aligned}
:::

由此，我们有：

$$
\sum_{k=0}^{n-1 } \frac{(\lambda t)^{k} }{k!} e^{-\lambda t}= \frac{\lambda ^{n} }{\Gamma (n)}\int_{t}^{+\infty } x^{n-1}e^{-\lambda x} dx
$$

因此：

::: {math}
\begin{eqnarray*}
   F(t)
   &=&\sum_{k=n}^{+\infty } \frac{(\lambda t)^{k} }{k!} e^{-\lambda t}\\
   &=&1-\frac{\lambda ^{n} }{\Gamma (n)}\int_{t}^{+\infty } x^{n-1} e^{-\lambda x} dx\\
   &=&1-\int_{t}^{+\infty } \frac{\lambda ^{n} }{\Gamma (n)}x^{n-1} e^{-\lambda x} dx\\
   &=&\int_{0}^{t} \frac{\lambda ^{n} }{\Gamma (n)}x^{n-1} e^{-\lambda x} dx
\end{eqnarray*}
:::
所以， $S_{n}\sim Ga(n,\lambda)$ .
```

````

## 贝塔分布

贝塔函数
: 称

$$
B(a,b)=\int_{0}^{1} x^{a-1} (1-x)^{b-1} dx,a>0,b>0
$$

为贝塔函数。

根据贝塔函数的定义，可以证明贝塔函数的一些常用性质。

````{prf:property}
1. % Todo
2. $B(a,b)=B(b,a)$ ；
3. $B(a,b)=\frac{\Gamma (a)\Gamma (b)}{\Gamma (a+b)}$ 。

```{dropdown} Proof
由伽马函数的定义可知：

$$
\Gamma (a)\Gamma (b)=\int_{0}^{+\infty } \int_{0}^{+\infty } x^{a-1} y^{b-1} e^{-(x+y)} dxdy
$$

作变量变换：

$$\left\{\begin{matrix}
x=uv\\
y=u(1-v)
\end{matrix}\right.\Longrightarrow
\left\{\begin{matrix}
u=x+y\\
v=\frac{u}{x} % Keeping the original LaTeX expression here.
\end{matrix}\right.\Longrightarrow
J=\begin{vmatrix}
v&u \\
(1-v)&-u
\end{vmatrix}=-u
$$

故：

::: {math}
\begin{eqnarray*}
     \Gamma (a)\Gamma (b)
   &=&\int_{0}^{1 } \int_{0}^{+\infty } (uv)^{a-1} (u(1-v))^{b-1} e^{-u} ududv\\
   &=& \int_{0}^{+\infty } u^{a+b-1}e^{-u}du \cdot \int_{0}^{1 }v^{a-1}(1-v)^{b-1}dv\\
   &=&\Gamma (a+b)B(a,b).
\end{eqnarray*}
:::
```
````

基于贝塔函数，我们来定义贝塔分布。

贝塔分布
: 假设一随机变量 $X$ ，其密度函数为：

$$
p(x)=\left\{\begin{matrix}
    \frac{\Gamma (a+b)}{\Gamma (a)\Gamma (b)}x^{a-1} (1-x)^{b-1}, &0<x<1, \\
    0,& \text{其他}.
    \end{matrix}\right.
$$

则称 $X$ 的分布为贝塔分布，记 $X\sim Be(a,b)$ ，其中 $a>0,b>0$ 均为形状参数。

```{prf:remark}
特别地，当 $a=1,b=1$ 时， $Be(1,1) = U(0,1)$ 。
```

