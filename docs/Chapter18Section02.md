# 定义
为了阐述清楚充分统计量，我们先讲以下这个简单的例子。

`````{prf:example}
30 秒口算是小学数学课课前一项测试。在表中是四位同学的 20 题的结果。

```{list-table}
:header-rows: 1

* - 题号
  - 学生 1
  - 学生 2
  - 学生 3
  - 学生 4
* - 1
  - $\surd$
  - $\times$
  - $\surd$
  - $\times$
* - 2
  - $\times$
  - $\times$
  - $\surd$
  - $\times$
* - 3
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 4
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 5
  - $\surd$
  - $\surd$
  - $\times$
  - $\surd$
* - 6
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 7
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 8
  - $\times$
  - $\surd$
  - $\surd$
  - $\surd$
* - 9
  - $\surd$
  - $\surd$
  - $\times$
  - $\surd$
* - 10
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 11
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 12
  - $\surd$
  - $\surd$
  - $\surd$
  - $\times$
* - 13
  - $\surd$
  - $\times$
  - $\surd$
  - $\surd$
* - 14
  - $\times$
  - $\surd$
  - $\surd$
  - $\surd$
* - 15
  - $\surd$
  - $\surd$
  - $\times$
  - $\surd$
* - 16
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 17
  - $\times$
  - $\surd$
  - $\surd$
  - $\times$
* - 18
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 19
  - $\surd$
  - $\surd$
  - $\surd$
  - $\surd$
* - 20
  - $\surd$
  - $\times$
  - $\times$
  - $\surd$
* - 总分
  - 16
  - 16
  - 16
  - 16
```

通过上述数据，你的直观感受是什么？

我们重新定义一下这个问题。记 $x_{i,j}$ 为第 $j$ 个学生在第 $i$ 道题目的结果，若正确， $x_{i,j}$ 取值为 $1$ ；否则为 $0$ ， $i=1,2,\cdots,20,j=1,2,3,4$ 。

以学生 1 为例，可观测到一组样本

$$\{1,0,1,1,1,
1,1,0,1,1,
1,1,1,0,1,
1,0,1,1,1\}.$$

以学生 2 为例，可以观测到另一组样本

$$\{0,0,1,1,1,
1,1,1,1,1,
1,1,0,1,1,
1,1,1,1,0\}.$$

这里的 1 或者 0 都是 $x_{i,j}$ 具体的取值。也就是说，对于学生 $j$ ，可以得到一组样本
 $\{x_{1,j},x_{2,j},\cdots,x_{20,j}\}$ ，而总分

$$
\sum_{i=1}^{20} x_{i,j}
$$

是样本的统计量。显然，给定样本，我们可以知道统计量的信息（根据样本我们能够计算统计量），但是根据统计量，我们无法得知样本的所有信息（根据总分，我们无法反推出学生 $j$ 在每道题是否回答正确的结果）。因此，在统计量对样本加工或者简化的过程中，信息被丢失了。
`````

```{admonition} Question
在构建统计量时，哪些信息可以丢失？哪些信息不可以丢失？
```

在参数模型中，我们使用参数化的概率质量函数或概率密度函数来刻画样本的信息。为了不区分概率质量函数和概率密度函数，我们这里统称为**概率函数**，记为 $p(x;\mathbf{\theta})$ ，其中 $\mathbf{\theta}$ 是未知参数。一旦参数确定，参数模型是唯一确定的。因此，参数模型中的未知参数包含的就是“有用信息”。
如果我们希望统计量不损失信息，本质上就要求了统计量囊括了未知参数的一切信息。

`````{prf:example}
对于每一个学生，其以一定概率能够回答正确任意一道口算题，假定其总体分布为 $b(1,p)$ 。每一道口算可以看作独立同分布的样本。于是，样本的符号可记为

$$x_1,x_2,\cdots,x_n$$

其中，这里样本量 $n$ 取 20。这里用 $n$ 表示只是为了更一般的情况。

对于样本来说，其联合概率（质量）函数为

$$
\begin{eqnarray*}
P(X_1 = x_1,X_2=x_2,\cdots,X_n=x_n) &=& p_{(X_1,X_2,\cdots,X_n)}(x_1,x_2,\cdots,x_n) \\
&=& \prod_{i=1}^n p_{X_i}(x_i) \\
&=& \prod_{i=1}^n P(X_i = x_i)\\ &=&\prod_{i=1}^n p^{x_i}(1-p)^{1-x_i}\\
&=& p^{\sum_{i=1}^n x_i} (1-p)^{n - \sum_{i=1}^n x_i}.
\end{eqnarray*}
$$

这是样本所有的信息，可以看出其依赖于未知参数 $p$ 。

接下来，我们来考虑统计量

$$
T = \sum_{i=1}^n X_i
$$

的分布。
根据所学习到的知识， $T$ 的分布为 $b(n,p)$ ，其概率（质量）函数为

$$
P(T = t) = p_T(t) = C_{n}^t p^{t} (1-p)^{n-t}.
$$

然后，在已知统计量的分布条件下，我们来考虑样本中剩余信息的分布，这里我们用条件概率（质量）函数来表示，即

$$
\begin{eqnarray*}
P(X_1=x_1,X_2 = x_2,\cdots,X_n = x_n | T = t) &=& \frac{P((X_1=x_1,X_2 = x_2,\cdots,X_n = x_n ,T = t)}{P(T=t)}\\
&=& \left\{
\begin{aligned}
&\frac{1}{C_{n}^t}, & \text{如果 $t = \sum_{i=1}^n x_i$ }.\\
&0 , & \text{如果 $t \neq \sum_{i=1}^n x_i$ }.
\end{aligned}
\right.
\end{eqnarray*}
$$

我们发现这个条件分布竟然与未知参数 $p$ 无关，这意味着，这个统计量已经囊括了样本中所有有用的信息，也就是数理统计里所定义的“充分的”。
`````

充分统计量
: 设 $X \sim F(x;\theta),x_1,\cdots,x_n$ 是来自某个总体的样本，总体分布函数为 $F(x;\theta)$ ，统计量 $T=T(x_1,x_2,\cdots,x_n)$ 。
如果在给定 $T$ 的取值后， $x_1,x_2,\cdots,x_n$ 的条件分布与 $\theta$ 无关，则称 $T$ 为 $\theta$ 的充分统计量。

接下来，我们来看另一个例子。

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自正态分布 $N(\mu,1)$ 的样本， $T = \bar{x}$ ，则 $T$ 是充分的。


```{dropdown} Proof
我们可知， $x_1,x_2,\cdots,x_n$ 的联合密度函数为

$$
\begin{eqnarray*}
p(x_1,x_2,\cdots,x_n;\mu) &=& \prod_{i=1}^n p(x_i) \\
&=& \prod_{i=1}^n \frac{1}{\sqrt{2\pi }} \exp\left\{-\frac{1}{2}(x_i - \mu)^2\right\}.
\end{eqnarray*}
$$

因为统计量

$$
T = \bar{x} \sim N(\mu,\frac{1}{n}),
$$

所以， $T$ 的密度函数为

$$
p_T(t) = \frac{1}{\sqrt{2\pi/n}}\exp\left\{-\frac{1}{2\sigma^2/n} (t-\mu)^2\right\}.
$$

根据定义来判断一个统计量是否是充分的，需要考虑一个条件概率（密度）函数，即

$$
p(x_1,x_2,\cdots,x_n|t) = \frac{p(x_1,x_2,\cdots,x_n,t)}{p_T(t)}
$$

我们注意到， $p(x_1,x_2,\cdots,x_n,t)$ 这是一个退化分布。一旦确定 $t$ 之后，不是所有的样本都是自由的， $x_n$ 可以改写成 $nt - (x_1+\cdots+x_{n-1})$ 。于是，

$$
\begin{eqnarray*}
&& p(x_1,x_2,\cdots,x_n,t) \\
&=& p(x_1,x_2,\cdots,x_{n-1},t)\\
&=& (2\pi)^{-n/2}\exp\left\{-\frac{1}{2}\left( \sum_{i=1}^{n-1}(x_i - \mu)^2 + \left(nt - \sum_{i=1}^{n-1} x_i -\mu \right)^2 \right)\right\}\\
&=& (2\pi)^{-n/2} \exp\left\{
-\frac{1}{2}\left( \sum_{i=1}^{n-1} x_i^2 - 2\mu(nt - x_n) + (n-1)\mu^2 + \left(nt - \sum_{i=1}^{n-1} x_i\right)^2 - 2(x_n \mu) + \mu^2
\right)
\right\}\\
&=&(2\pi)^{-n/2} \exp\left\{ -\frac{1}{2}\left( n\mu^2 - 2n \mu t + \sum_{i=1}^n x_i^2\right) \right\}
\end{eqnarray*}
$$

因此，条件概率函数为

$$
\begin{eqnarray*}
p(x_1,x_2,\cdots,x_n|t) &=& \frac{p(x_1,x_2,\cdots,x_n,t)}{p(t)} \\
&=& \frac{(2\pi)^{-n/2} \exp\left\{ -\frac{1}{2}\left( n\mu^2 - 2n \mu t + \sum_{i=1}^n x_i^2\right) \right\}}{ (2\pi/n)^{-1/2} \exp\left\{ -\frac{1}{2/n} \left(t-\mu\right)^2 \right\}} \\
&=& \frac{(2\pi)^{-n/2}}{(2\pi/n)^{-1/2} } \exp\left\{
-\frac{1}{2}\sum_{i=1}^n x_i^2 + \frac{n}{2}t^2
\right\}
\end{eqnarray*}
$$

这与参数 $\mu$ 无关。由此得证。
```

`````
