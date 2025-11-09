# 条件数学期望
正如之前课程内容中介绍的，我们讨论过条件概率是符合概率的公理化定义。由此，根据条件概率，我们可以定义随机变量的**条件分布**。既然有分布，我们也可以定义这个分布的特征数。这里，我们首先介绍如何定义条件分布的数学期望——条件期望。

条件期望
: 条件分布的数学期望（若存在）称为条件期望，即

$$E(X | Y=y)=\left\{\begin{aligned}
&\sum_{i} x_{i} P\left(X=x_{i} | Y=y\right) , &\quad \text{离散场合},\\
&\int_{-\infty}^{+\infty} x P(x | y) d x,&\quad \text{连续场合}.
\end{aligned}
\right.$$

因为条件期望是一种期望，所以条件期望也满足期望的性质。

`````{prf:property}
 $E\left(a_{1} X_{1}+a_{2} X_{2} | Y=y\right)=a_{1} E\left(X_{1} | Y=y\right)+a_{2} E\left(X_{2} | Y=y\right)$ ;
`````

这里从另一个角度来看条件期望。在给定 $Y=y$ 的条件下， $X$ 的条件分布会因 $y$ 的取值不同而不同，从而导致了 $E(X|Y=y)$ 亦是如此。所以， $E(X|Y=y)$ 可以看作 $y$ 的函数。我们记 $g(y) = E(X|Y=y)$ 。

对于随机变量 $Y$ ， $g(Y)= E(X|Y)$ 是随机变量 $Y$ 的函数。所以，条件期望 $E(X|Y)$ 可以看作随机变量 $Y$ 的函数，通常仍是一个随机变量。这里，我们讨论一下，其期望 $E(E(X|Y))$ 是什么呢？

``````{prf:theorem} 重期望公式
设 $(X,Y)$ 是二维随机变量且 $E(X)$ 存在，则

$$E(X)=E(E(X | Y)).$$

```{dropdown} Proof
这里仅证明连续场合。
设二维随机变量 $(X,Y)$ 的联合密度函数为 $p(x,y)$ ，记 $g(y)=E(X | Y=y)$ ，则 $g(X)=E(X | Y)$ ，由于 $p(x,y)=p(x | Y)\cdot p_{Y}(y)$ ，可得

$$
\begin{eqnarray*}
E(X) &=&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} x p(x, y) d x d y \\
&=&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} x \cdot p(x | y) \cdot p_{Y}(y) d x d y \\
&=&\int_{-\infty}^{+\infty} \left(\int_{-\infty}^{+\infty} x p(x | y) dx \right) \cdot p_{Y}(y) d y \\
&=&\int_{-\infty}^{+\infty} E(X | Y=y) \cdot p_{Y}(y) d y \\
&=&\int_{-\infty}^{+\infty} g(y) \cdot p_{Y}(y) d y \\
&=&E[g(Y)] \\
&=&E(E(X | Y)).
\end{eqnarray*}
$$

```
``````
类似地，我们可以定义条件方差，即 $Var(X|Y)$ ，即

$$
\begin{eqnarray*}
\text{Var}(X | Y) &=& E\left ( (X-E(X | Y))^{2} | Y \right )\\
&=&E(X^{2} | Y)-\left ( E(X | Y) \right )^{2}.
\end{eqnarray*}
$$

类似于重期望公式，我们也可以将 $X$ 的方差拆解成两个部分，即

$$\text{Var}(X)=E(\text{Var}(X | Y))+\text{Var}(E(X | Y)),$$

其中，前者可以看成组内方差，后者可以看成组间方差。

`````{prf:example}
一矿工被困在有三个门的矿井里。第一个门通一坑道，沿此坑道走 3 小时可到达安全区；第二个门通一坑道，沿此坑道走 5 小时又回到原处；第三个门通一坑道，沿此坑道走 7 小时也回到原处。假定此矿工总是等可能地在三个门中选择一个，试求他平均要用多少时间才能到达安全区。

```{dropdown} Solution

如果直接求 $X$ 的分布， $X$ 的可能取值为 $3,5+3,7+3,5+5+3,5+7+3,\cdots$ 这是很困难的。
这里，我们考虑另一种解法： $Y$ 表示在矿井中选的门，即 ${Y=i}$ 表示选了第 $i$ 个门。可知

$$P(Y=1)=P(Y=2)=P(Y=3)=\frac{1}{3}.$$

因为选了第一个门后， $3$ 小时到达安全区，所以 $E(X | Y=1)=3$ ；因为选了第二个门后， $5$ 小时回到原地，所以 $E(X | Y=2)=5+E(X)$ ；因为选了第三个门后， $7$ 小时回到原地，所以 $E(X | Y=3)=7+E(X)$ .
综上，

$$
\begin{eqnarray*}
E(X) &=&E(E(X | Y)) \\
&=&E(X | Y=1) \cdot \frac{1}{3}+E(X | Y=2) \cdot \frac{1}{3}+E(X | Y=3) \cdot \frac{1}{3} \\
&=&3 \cdot \frac{1}{3}+(5+E(X)) \cdot \frac{1}{3}+(7+E(X)) \cdot \frac{1}{3} \\
&=& 5 +\frac{2}{3} E(X).
\end{eqnarray*}
$$

解得 $E(X)=15$ .
```
`````

`````{prf:example}
设 $X_{1},X_{2},\cdots$ 为一列独立同分布的随机变量，随机变量 $N$ 只取正整数值且 $N$ 与 ${X_{n}}$ 独立，证明

- 

$$
E\left(\sum_{i=1}^{N} X_{i}\right)=E\left(X_{1}\right) \cdot E(N)
$$

- （课后自学）

$$
\text{Var}\left(\sum_{i=1}^{N} X_{i}\right)=\operatorname{Var}\left(X_{1}\right) E(N)+\left(E\left(X_{1}\right)\right)^{2} \operatorname{Var}(N)
$$

```{dropdown} Proof

- 我们先考虑第一个问题，这里与之前介绍的期望的性质有一个明显的差异——这里考虑了随机变量个随机变量之和的期望，而之前考虑的是有限个随机变量之和的期望。

$$
\begin{eqnarray*}
E\left(\sum_{i=1}^{N} X_{i}\right) &=&E\left(E\left(\sum_{i=1}^{N} X_{i} | N\right)\right) \\
&=&\sum_{n=1}^{+\infty} E\left(\sum_{i=1}^{N} X_{i} | N=n\right) \cdot p_{N}(n) \\
&=&\sum_{n=1}^{+\infty} E\left(\sum_{i=1}^{n} X_{i} | N=n\right) p_{N}(n) \\
&=&\sum_{n=1}^{+\infty} E\left(\sum_{i=1}^{n} X_{i}\right) \cdot p_{N}(n) \\
&=&\sum_{n=1}^{+\infty} n \cdot E\left(X_{1}\right) \cdot p_{N}(n) \\
&=&E\left(X_{1}\right) \cdot E(N)
\end{eqnarray*}
$$

- 随机变量个随机变量之和的方差的证明过程由学生课后自学。

$$
\begin{eqnarray*}
\text{Var}\left(\sum_{i=1}^{N} X_{i}\right) &=&
E\left(\text{Var}\left(\sum_{i=1}^{N} X_{i} | N\right)\right)+\text{Var}\left(E\left(\sum_{i=1}^{N} X_{i} | N\right)\right) \\
& =& I_{1}+I_{2}
\end{eqnarray*}
$$

其中

$$
\begin{eqnarray*}
I_{1} &=&\sum_{n=1}^{+\infty} \text{Var}\left(\sum_{i=1}^{n} X_{i} | N=n\right) \cdot p_{N}(n) \\
&=&\sum_{n=1}^{+\infty} \text{Var}\left(\sum_{i=1}^{n} X_{i}\right) p_{N}(n) \\
&=&\sum_{n=1}^{+\infty} \sum_{i=1}^{n} \text{Var}\left(X_{i}\right) p_{N}(n) \\
&=&\text{Var}\left(X_{1}\right) \cdot E(N)
\end{eqnarray*}
$$

$$
\begin{eqnarray*}
I_{2} &=&E\left(E\left(\sum_{i=1}^{N} X_{i} | N\right)\right)^{2}-E^{2}\left(E\left(\sum_{i=1}^{N} X_{i} | N\right)\right) \\
&=&\sum_{n=1}^{+\infty}\left(E\left(\sum_{i=1}^{N} X_{i} | N=n\right)\right)^{2} p_{N}(n)-\left(E\left(X_{1}\right) \cdot E(N)\right)^{2} \\
&=&\sum_{n=1}^{+\infty}\left(E\left(\sum_{i=1}^{n} X_{i} | N=n\right)\right)^{2} p_{N}(n)-\left(E\left(X_{1}\right) \cdot E(N)\right)^{2} \\
&=&\sum_{n=1}^{+\infty}\left(n \cdot E\left(X_{1}\right)\right)^{2} p_{N}(n) \\
&=&\left(E\left(X_{1}\right)\right)^{2} E\left(N^{2}\right)-\left(E\left(X_{1}\right)\right)^{2} \cdot(E(N))^{2} \\
&=&\left(E\left(X_{1}\right)\right)^{2} \text{Var}(N)
\end{eqnarray*}
$$

```
`````