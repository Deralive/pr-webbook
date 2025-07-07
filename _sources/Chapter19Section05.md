# EM 算法（选修）
最大似然估计是一种非常有效的参数估计方法，但是当分布里有多余参数或数据为截尾或缺失时，求最大似然估计就变得困难。EM 算法由 Dempster 等人于 1977 年提出的，最初可以解决缺失数据场景下的最大似然估计求解问题。EM 算法的核心想法是分两步骤：E 步求期望；M 步求最值。这里我们仅用一个例子来演示一下如何利用 EM 算法来求最大似然估计。

`````{prf:example}
设一次试验可能有四个结果，其发生的概率分别为 $\frac{1}{2}-\frac{\theta}{4}, \frac{1-\theta}{4},\frac{1+\theta}{4},\frac{\theta}{4}$ ，其中 $\theta \in (0,1)$ 。现进行了 197 次试验，四种结果发生的次数分别为 75，18，70，34。求 $\theta$ 的最大似然估计。
```{dropdown} Solution

设 $y_1,y_2,y_3,y_4$ 表示四种结果发生的次数。这个总体分布是一个多项分布，故其似然函数为

$$
\begin{eqnarray*}
L(y_1,y_2,y_3,y_4;\theta) &=& \frac{(y_1+y_2+y_3+y_4)!}{y_1!y_2!y_3!y_4!} \left(\frac{1}{2}-\frac{\theta}{4}\right)^{y_1} \left(\frac{1-\theta}{4}\right)^{y_{2}}\left(\frac{1+\theta}{4}\right)^{y_{3}}\left(\frac{\theta}{4}\right)^{y_{4}}\\
&\propto& (2-\theta)^{y_1} (1-\theta)^{y_2} (1+\theta)^{y_3} \theta^{y_4}.
\end{eqnarray*}
$$

其对数似然函数为

$$
l(\theta) \propto y_1 \ln(2-\theta) + y_2 \ln (1-\theta) + y_3 \ln(1+\theta) + y_4 \ln \theta.
$$

我们可以对 $l(\theta)$ 关于 $\theta$ 求导，即

$$
\frac{\partial l(\theta)}{\partial \theta} = - \frac{y_1}{2-\theta} - \frac{y_2}{1-\theta} + \frac{y_3}{1+\theta} + \frac{y_4}{\theta}.
$$

方程 $\frac{\partial l(\theta)}{\partial \theta} = 0$ 的求解是相对复杂的。于是，这里介绍 EM 算法的一般形式。我们引入两个潜变量 $z_1,z_2$ 。假设第一种结果可以分为两部分，其发生的概率分别为 $\frac{1-\theta}{4}$ 和 $\frac{1}{4}$ ，令 $z_1$ 和 $y_1-z_1$ 分别表示落入这两部分的次数。再假设第三种结果分为两部分，其发生的概率分别为 $\frac{\theta}{4}$ 和 $\frac{1}{4}$ ，令 $z_2$ 和 $y_3-z_2$ 分别表示落入这两部分的次数。这里 $z_1,z_2$ 是我们虚构的，它们具体的数值是不可观测的。
数据 $(y_1,y_2,y_3,y_4,z_1,z_2)$ ，称为完全数据，而数据 $(y_1,y_2,y_3,y_4)$ ，称为不完全数据。考虑我们可以观测到完全数据，其似然函数为

$$
\begin{eqnarray*}
&&L(\theta;y_1,y_2,y_3,y_4,z_1,z_2) \\
&=& \frac{n!}{z_1!(y_1-z_1)!y_2!z_2!(y_3-z_2)!y_4!} \left(\frac{1}{4}\right)^{y_{1}-z_{1}}\left(\frac{1-\theta}{4}\right)^{z_{1}+y_{2}}\left(\frac{1}{4}\right)^{y_{3}-z_{2}}\left(\frac{\theta}{4}\right)^{z_{2}+y_{4}} \\
&\propto& (1-\theta)^{z_1+y_2} (\theta)^{z_2+y_4}.
\end{eqnarray*}
$$

其对数似然函数为

$$
l(\theta;y_1,y_2,y_3,y_4,z_1,z_2) = (z_1+y_2)\ln (1-\theta) + (z_2 + y_4) \ln \theta.
$$

基于此，可以解得其最大似然估计为

$$
\hat{\theta} = \frac{z_2 + y_4}{z_1 + y_2 + z_2 + y_4}.
$$

遗憾的是，我们并没有观测到 $z_1,z_2$ 。但是我们知道，当 $y_1,y_2,y_3,y_4$ 及 $\theta$ 已知时，

$$
z_1 \sim b\left(y_1, \frac{1-\theta}{2-\theta}\right),\quad z_{2} \sim b\left(y_3,\frac{\theta}{1+\theta}\right).
$$

EM 算法具体如下：

- E 步：在观测数据 $y_1,y_2,y_3,y_4$ 和已知 $\theta = \theta^{(i)}$ 的条件下，我们求基于完全数据的对数似然函数的期望

$$
\begin{eqnarray*}
Q(\theta | y_1,y_2,y_3,y_4,\theta^{(i)}) &=& E_{z_1,z_2} l(\theta;y_1,y_2,y_3,y_4,z_1,z_2) \\
&=& (E_{\theta^{(i)}}(z_1|y_1) + y_2)\ln (1-\theta) + (E_{\theta^{(i)}}(z_2|y_3) + y_4) \ln(\theta)\\
&=& \left( \frac{1-\theta^{(i)}}{2-\theta^{(i)}} y_1 + y_2 \right) \ln (1-\theta) + \left( \frac{\theta^{(i)}}{1+\theta^{(i)}} y_3 + y_4 \right) \ln \theta.
\end{eqnarray*}
$$

- M 步：求 $Q(\theta | y_1,y_2,y_3,y_4,\theta^{(i)})$ 关于 $\theta$ 的最大值 $\theta^{(i+1)}$ ，即

$$
\theta^{(i+1)} = \arg\max_{\theta} Q(\theta | y_1,y_2,y_3,y_4,\theta^{(i)})
$$

也就是说，对 $Q(\theta | y_1,y_2,y_3,y_4,\theta^{(i)})$ 关于 $\theta$ 求导，即

$$
\frac{\frac{\theta^{(i)}}{1+\theta^{(i)}} y_3 + y_4 }{\theta^{(i+1)}} - \frac{\frac{1-\theta^{(i)}}{2-\theta^{(i)}} y_1 + y_2 }{1-\theta^{(i+1)}} =0
$$

由此可得

$$
\theta^{(i+1)} = \frac{\frac{\theta^{(i)}}{1+\theta^{(i)}} y_3 + y_4 }{ \frac{\theta^{(i)}}{1+\theta^{(i)}} y_3 + y_4
+ \frac{1-\theta^{(i)}}{2-\theta^{(i)}} y_1 + y_2}.
$$

```
`````

```{admonition} Question
EM 算法是一个迭代算法。我们仍有以下三个问题：

- EM 算法在什么条件下是收敛？
- EM 算法如何才能停止？
- 如何选择 EM 算法的初始值？

```