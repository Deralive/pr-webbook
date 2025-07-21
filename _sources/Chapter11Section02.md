# 离散场合下的条件分布
设二维离散随机变量 $(X,Y)$ 的联合分布列为

$$p_{i j}=P\left(X=x_{i}, Y=y_{j}\right), i=1,2, \cdots;\quad j=1,2, \cdots.$$

条件分布列
: 对一切使 $P\left(Y=y_{j}\right)=p_{\cdot j}=\sum_{i=1}^{\infty} p_{i j}>0$ 的 $y_{j}$ ，称

$$
\begin{eqnarray*}
p_{i | j} &=&P\left(X=x_{i} | Y=y_{j}\right) \\
&=&\frac{P\left(X=x_{i}, Y=y_{j}\right)}{P\left(Y=y_{j}\right)} \\
&=&\frac{p_{i j}}{p_{\cdot j} }
\end{eqnarray*}
$$

条件分布函数
: 为给定 $Y=y_{j}$ 条件下 $X$ 的条件分布列， $i=1,2,\cdots$ 。

给定 $Y=y_{j}$ 条件下 $X$ 的条件分布函数为

$$F\left(x | y_{j}\right)=\sum_{x_{i} \leq x} P\left(X=x_{i} | Y=y_{j}\right)=\sum_{x_{i} \leq x} p_{i | j}$$

`````{prf:example}
设随机变量 $X$ 与 $Y$ 独立，且 $x \sim P\left(\lambda_{1}\right), Y \sim P\left(\lambda_{2}\right)$ 。在已知 $X+Y=n$ 的条件下，求 $X$ 的条件分布。
```{dropdown} Solution

在例 {prf:ref}`ex:lect9_1` 中已经证明了 $X+Y\sim P(\lambda_{1}+\lambda_{2})$ 。所以

$$
\begin{eqnarray*}
P(X=k | X+Y=n)&=&\frac{P(X=k, X+Y=n)}{P(X+Y=n)}\\
&=&\frac{P(X=k, Y=n-k)}{P(X+Y=n)} \\
&=& \frac{P(X=k) \cdot P(Y=n-k)}{P(X+Y=n)}\\
&=&\frac{\frac{\lambda_{1}^{k}}{k !} e^{-\lambda_{1}} \cdot \frac{\lambda_{2}^{(n-k)}}{(n-k) !} e^{-\lambda_{2}}}{\frac{\left(\lambda_{1}+\lambda_{2}\right)^{n}}{n !} e^{-\left(\lambda_{1}+\lambda_{2}\right)}}\\
&=&\frac{n !}{k !(n-k) !}\left(\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}\right)^{k}\left(1-\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}\right)^{n-k}
\end{eqnarray*}
$$

因此，在 $X+Y=n$ 的条件下， $X$ 的条件分布为二项分布 $b\left(n, \frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}\right).$ 
```
`````

`````{prf:example}
设在一段时间内进入某一商店的顾客人数 $X$ 服从泊松分布 $P(\lambda)$ ，每位顾客购买某商品的概率为 $p$ ，并且每位顾客是否购买该种物品相互独立。求进入商店的顾客购买这种物品的人数 $Y$ 的分布列。
```{dropdown} Solution

由题可知，

$$P(X=m)=\frac{\lambda^{m}}{m !} e^{-\lambda} \quad m=0,1,2, \cdots$$

在进入商店的人数 $X=m$ 的条件下，购买某种物品的人数 $Y$ 的条件分布为二项分布 $b(m,p)$ ，即

$$P(Y=k | X=m)=\begin{pmatrix}
m \\
k
\end{pmatrix} p^{k}(1-p)^{m-k}, \quad k=0,1, \cdots, m.$$

由全概率公式有

$$\begin{aligned}
P(Y=k) &=\sum_{m=k}^{+\infty} P(X=m) \cdot P(Y=k | X=m) \\
&=\sum_{m=k}^{+\infty} \frac{\lambda^{m}}{m !} e^{-\lambda} \cdot \frac{m !}{k !(m-k) !} p^{k}(1-p)^{m-k} \\
&=\frac{1}{k !} e^{-\lambda}(\lambda p)^{k} \cdot \sum_{m=k}^{+\infty} \frac{(\lambda(1-p))^{m-k}}{(m-k) !} \\
&=\frac{1}{k !}(\lambda p)^{k} e^{-\lambda} \sum_{m=0}^{+\infty} \frac{(\lambda(1-p))^{m}}{m !} e^{-\lambda(1-p)} \cdot e^{\lambda(1-p)} \\
&=\frac{(\lambda p)^{k}}{k !} e^{-\lambda p} ,\quad k=0,1,2, \cdots
\end{aligned}$$

因此， $Y\sim P(\lambda p)$ 。
```
`````