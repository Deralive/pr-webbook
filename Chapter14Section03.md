# 棣莫弗-拉普拉斯中心极限定理的应用案例
回顾一下棣莫弗-拉普拉斯中心极限定理，我们知道

$$
P(S_n^{\ast} \leq s) = \Phi(s).
$$

注意到， $\Phi(s)$ 本质上是一个概率值。对于给定概率 $\Phi(s)$ 时， $s$ 可以认为是相应的分位数。而二项分布中由两个参数 $n$ 和 $p$ ，其中 $n$ 表示实验次数，也通常被认为是样本量（这个概念将会在第 14 讲中给出）。
于是，在棣莫弗-拉普拉斯中心极限定理的应用，我们要解决以下三个问题：

- 求分位数；
- 求概率；
- 求样本量。

## 求分位数

`````{prf:example}
某奶茶店共售卖两种奶茶：珍珠奶茶和纯奶茶。其差异在于是否放珍珠。假设每位顾客点任何一种奶茶是等可能的，且点单是相互不受影响。已知每杯珍珠奶茶中需放入 5 克珍珠。请问，至少要准备多少克珍珠，才可以有 $95\%$ 的可能性，接受 100 杯奶茶的点单？
```{dropdown} Solution

设第 $i$ 位顾客点了珍珠奶茶为 $X_i$ ， $X_i \sim b(1,p_0),p_0=0.5$ ，即

$$X_{i}=\left\{\begin{aligned}
&1,&\text{如果第 i 位顾客点了珍珠奶茶}\\
&0,&\text{如果第 i 位顾客点了纯奶茶}\\
\end{aligned}\right.$$

所以，100 位顾客中共有

$$
\sum_{i=1}^{100}X_i \sim b(100,p_0)
$$

点了珍珠奶茶。设我们拟准备 $s$ 克珍珠。于是， $s$ 克珍珠能够满足 100 位顾客的点单，即

$$
\begin{eqnarray*}
95\% &\leq& P\left( 5\times \sum_{i=1}^{100}X_i \leq s\right)\\
& = & P\left( \sum_{i=1}^{100}X_i \leq \frac{s}{5}\right) \\
& = & P\left(\frac{\sum_{i=1}^{100} X_{i}-50}{\sqrt{25}} \leq \frac{\frac{s}{5}+0.5-50}{\sqrt{25}}\right)\\
&=& \Phi\left(\frac{s}{25}-9.9\right)
\end{eqnarray*}
$$

可以解得

$$
s = (\Phi^{-1}(0.95) + 0.99 ) \times 25 = 288.62 \approx 290.
$$

```
`````
## 求概率

`````{prf:example}
已知我们预定了 290 克珍珠，共 58 杯珍珠奶茶。某公司一次性订购 100 杯奶茶，该公司的员工更加偏好珍珠奶茶。假设每一杯珍珠奶茶的点单可能性提高到了 60\%，请问 290 克是否能够满足这 100 杯奶茶的订单？
```{dropdown} Solution

由于 $X_i\sim b(1,p_0)$ ，这里 $p_0=0.6$ 。我们考虑以下概率

$$
P\left( \sum_{i=1}^{100} X_i \leq 58 \right) .
$$

这个概率可以直接利用二项分布来计算，即

$$
P\left( \sum_{i=1}^{100} X_i \leq 58 \right) = \sum_{k=0}^{58} 0.6^{58} 0.4^{100-58}=0.3775.
$$

也可以用正态分布来近似计算，即

$$
\begin{eqnarray*}
P\left(\sum_{i=1}^{100} x_{i} \leq 58\right) &=&P\left( \frac{\sum_{i=1}^{100} x_{i}-60}{\sqrt{24}} \leq \frac{58+05-60}{\sqrt{24}} \right)
\\
&=& 0.3797.
\end{eqnarray*}
$$

```
`````
## 求样本量

`````{prf:example}
结合上述两个例子，我们发现顾客的奶茶偏好对备料十分重要。于是，我们需要调研一下顾客的奶茶偏好。假定顾客的真实奶茶偏好为 $p$ 。理解为本奶茶店接单中每杯奶茶是珍珠奶茶的概率是 $p$ 。我们通常可以利用历史订单得到概率 $p$ 的估计值 $\hat{p}$ 。请问至少要看多少历史订单数量（多少杯奶茶），要保证有 95 $\%$ 的把握使得估计值 $\hat{p}$ 与真实的 $p$ 之间的差异不超过 $1\%$ ？
```{dropdown} Solution

令 $X_i$ 表示第 $i$ 杯奶茶是珍珠奶茶，即

$$
X_i = \left\{
\begin{aligned}
&1,& \text{如果第 $i$ 杯奶茶是珍珠奶茶};
&0,& \text{其他}.
\end{aligned}
\right.
$$

于是， $X_i \sim b(1,p)$ ， $p$ 表示珍珠奶茶的点单概率。假设共需要看 $n$ 杯奶茶的历史订单信息，则

$$
S_n = \sum_{i=1}^n X_i
$$

表示 $n$ 杯奶茶中的珍珠奶茶的数量，即 $S_n \sim b(n,p)$ 。根据大数定律(LLN)，当 $n$ 很大时，

$$
\frac{S_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i \overset{P}{\rightarrow} p.
$$

根据中心极限定理（CLT），

$$
\begin{eqnarray*}
95\% &\leq& P\left(\left|\frac{S_{n}}{n}-p\right| \leqslant 0.01 \right)\\
&=&=P\left(\left|\frac{S_{n} / n-p}{\sqrt{\frac{p(1-p)}{n}}}\right| \leq \frac{0.01}{\sqrt{\frac{p(1-p)}{n}}}\right) \\
&=& 2 \Phi\left(0.01 \sqrt{\frac{n}{p(1-p)}}\right)-1,
\end{eqnarray*}
$$

于是，

$$
\begin{eqnarray*}
\Phi\left(0.01 \sqrt{\frac{n}{p(1-p)}}\right) \geq 0.975\\
\end{eqnarray*}
$$

我们可以解出

$$
\begin{eqnarray*}
\frac{n}{p(1-p)} \geq \left(\frac{\Phi^{-1}(0.975)}{0.01}\right)^2.
\end{eqnarray*}
$$

注意到

$$
p(1-p) \leqslant \frac{1}{2} \times \frac{1}{2}=0.25
$$

所以，

$$
n \geq \left(\frac{\Phi^{-1}(0.975)}{0.01}\right)^2 \times 0.25 = 9604.
$$

因此，至少要看 $9604$ 杯奶茶的历史订单数量，要保证有 95 $\%$ 的把握使得估计值 $\hat{p}$ 与真实的 $p$ 之间的差异不超过 $1\%$ 。
```
`````