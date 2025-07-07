# 常见统计量：次序统计量

`````{prf:example}
我们共有 $n$ 个学生参加本学期的期中考试，记为 $x_1,x_2,\cdots,x_{n}$ 。常常会对学生的考试成绩进行排名，学生的考试成绩可以按从小到大进行排序，于是可以得到一组有序样本 $x_{(1)}\leq x_{(2)}\leq \cdots \leq x_{(n)}$ 。我们记 $y_i = x_{(i)}$ 。易知， $y_1,y_2,\cdots,y_{n}$ 既不独立也不同分布。
`````

设 $x_1,x_2,\cdots,x_n$ 是来自于总体 $X$ 的样本， $x_{(i)}$ 称为样本的第 $i$ 个次序统计量，它表示将样本观测值从小到大排序后得到的第 $i$ 个观测值，其中 $x_{(1)}=\min\{x_1,x_2,\cdots,x_n\}$ 称为该样本的最小次序统计量， $x_{(n)}=\max\{x_1,x_2,\cdots,x_n\}$ 称为该样本的最大次序统计量， $(x_{(1)},x_{(2)},\cdots,x_{(n)})$ 称为该样本的次序统计量。

```{admonition} Question

- 如何求 $x_{(k)}$ 的分布？
- 如何求 $x_{(n)} - x_{(1)}$ 的分布？

```{dropdown} Proof
对增量 $\Delta y, \Delta z$ 以及 $y<z$ ，事件 $\{x_{(i)} \in (y,y+\Delta y], x_{(j)} \in (z , z+\Delta z]\}$ 可以表述为“样本量为 $n$ 的样本 $x_1,x_2,\cdots,x_n$ 中有 $i-1$ 个观测值小于等于 $y$ ，一个落入区间 $(y,y+\Delta y]$ , $j-i-1$ 个落入区间 $(y+\Delta y, z]$ ， 一个落入区间 $(z,z+\Delta z]$ ，而余下 $n-j$ 个大于 $z+\Delta z$ ”。
于是由多项式分布可得

$$
\begin{eqnarray*}
&&P(x_{(i)}\in (y,y+\Delta y] , x_{(j)}\in (z,z+\Delta z]) \\
&\approx& \frac{n!}{(i-1)!1!(j-i-1)!1!(n-j)!}(F(y))^{i-1} p(y)\Delta y\\
&&(F(z) - F(y+\Delta y))^{j-i-1} p(z)\Delta z (1-F(z+\Delta z))^{n-j},
\end{eqnarray*}
$$

考虑到 $F(x)$ 的连续性，当 $\Delta y \rightarrow 0, \Delta z \rightarrow 0$ 时，有 $F(y+\Delta y) \rightarrow F(y),F(z+\Delta z) \rightarrow F(z)$ ，于是

$$
\begin{eqnarray*}
p_{ij}(y,z) &=& \lim_{\Delta y \rightarrow 0,\Delta z \rightarrow 0} \frac{P(x_{(i)}\in (y,y+\Delta y] , x_{(j)}\in (z,z+\Delta z])}{\Delta y \cdot \Delta z}\\
&=& \frac{n!}{(i-1)!1!(j-i-1)!1!(n-j)!}(F(y))^{i-1} p(y) \\
&&(F(z) - F(y+\Delta y))^{j-i-1} p(z)(1-F(z+\Delta z))^{n-j}
\end{eqnarray*}
$$

```

````{prf:example}
设总体分布为 $U(0,1)$ ， $x_1,x_2,\cdots,x_n$ 为其样本，则

- $x_{(k)}$ 的分布是 $Be(k,n-k+1)$ .
因为 $x_i$ 的分布函数为

$$F(x) =
\left\{\begin{aligned}
&0, & x\leq 0\\
& x, &0<x<1\\
& 1 , & x\geq 1.\\
\end{aligned}\right.
$$

所以， $x_{(k)}$ 的密度函数为

$$
\begin{eqnarray*}
p_k(x) &=& \frac{n!}{(k-1)!(n-k)!} x^{k-1}(1-x)^{n-k} \\
&=& \frac{\Gamma(n+1)}{\Gamma(k)\Gamma(n-k+1)} x^{k-1}(1-x)^{(n-k+1)-1}, 0<x<1.
\end{eqnarray*}
$$

- $(x_{(k)},x_{(s)})$ 的联合密度函数为

$$
p_{k,s}(x,y)=\frac{n!}{(k-1)!(s-k-1)!(n-s)!} x^{k-1}(y-x)^{s-k-1}(1-y)^{n-s}, 0\leq x\leq y\leq 1.
$$

- 若 $Y=x_{(s)}-x_{(k)}$ 。令 $U=x_{(k)}$ 。则 $Y$ 的密度函数为

$$
\begin{eqnarray*}
p_{Y}(y)&=&\int_{0}^{1-y} p(y, u) \text{d} u\\
&=&\int_{0}^{1-y} \frac{n !}{(k-1) !(s-k-1) !(n-s) !} u^{k-1} y^{s-k-1}(1-u-y)^{n-s} \text{d} u\\
&\overset{u=(1-y)v}{=}&\frac{n !}{(k-1) !(s-k-1) !(n-s) !}\\
&&\cdot\int_{0}^{1} (1-y)^{k-1} v^{k-1} y^{s-k-1}(1-y)^{n-s}(1-v)^{n-s}(1-y) \text{d} v\\
&=&y^{s-k-1}(1-y)^{n-s+k} \int_{0}^{1} \frac{n !}{(k-1) !(s-k-1) !(n-s) !} v^{k-1}(1-v)^{n-s} \text{d} v\\
&=& y^{s-k-1}(1-y)^{n-s+k} \cdot \frac{n!}{{(k-1)!}(s-k-1)!{(n-s)!}}\cdot \frac{{(k-1)!}{(n-s)!}}{(n+k-s)!}\\
&& \int_{0}^{1} \frac{\Gamma(n+k-s+1)}{\Gamma(k) \Gamma(n-s+1)} v^{k-1}(1-v)^{(n-s+1)-1} \text{d} v\\
&=&\frac{\Gamma(n+1)}{\Gamma(s-k) \Gamma(n-s+k+1)} y^{(s-k)-1}(1-y)^{(n-s+k+1)-1}
\end{eqnarray*}
$$

因此， $Y$ 的分布是 $Be(s-k,n-s+k+1)$ 。

`````

```{admonition} Remark

- 均匀分布的次序统计量是贝塔分布的来源之一。
- 经验分布函数是次序统计量的函数，即

$$F_{n}(x)=\frac{1}{n} \sum_{i=1}^{n} I_{\left\{x_{i} \leq x\right\}}=\frac{1}{n} \sum_{i=1}^{n} I\left\{X_{(i)} \leq x\right\}.$$

- 样本分位数也是基于次序统计量而定义。

```

## 样本分位数

 $m_{0.5}$ 定义如下：

$$
m_{0.5} = \left\{\begin{aligned}
& x_{\left(\frac{n+1}{2}\right)} & n\text{为奇数}, \\
&\frac{1}{2}\left(x_{\left(\frac{n}{2}\right)}+x_{\left(\frac{n}{2}+1\right)}\right) & n\text{为偶数}.
\end{aligned}
\right.
$$

称 $m_{0.5}$ 为中位数。

 $m_{p}$ 定义如下：

$$
m_{p} = \left\{\begin{aligned}
& x_{\left([np+1]\right)} & \text{若 $np$ 不为整数}, \\
&\frac{1}{2}\left(x_{\left([np]\right)}+x_{\left( [np+1]\right)}\right) & \text{若 $np$ 为整数}.
\end{aligned}
\right.
$$

称 $m_{p}$ 为样本 $p$ 分位数。

对于样本分位数，我们也有相应的渐近分布，如下定理，供学生进行选修。

``````{prf:theorem}
设总体密度函数为 $p(x)$ ， $x_p$ 为其 $p$ 分位数， $p(x)$ 在 $x_p$ 处连续且 $p(x_p)>0$ ，则当 $n\rightarrow \infty$ 时，样本 $p$ 分位数 $m_p$ 的渐近分布为

$$
m_p \overset{\cdot}{\sim } N\left(x_p, \frac{p(1-p)}{np^2(x_p)}\right).
$$

特别地，对于样本中位数，当 $n\rightarrow \infty$ 时近似地有

$$
m_{0.5} \overset{\cdot}{\sim } N\left(x_{0.5}, \frac{1}{4np^2(x_{0.5})}\right).
$$

``````