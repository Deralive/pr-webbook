# 分布的拟合优度检验
## 概述

`````{prf:example} 孟德尔豌豆实验
:label: ex:chap23_pea_experiment
在 19 世纪，孟德尔按颜色与形状把豌豆分为四类：黄圆、绿圆、黄皱、绿皱。孟德尔根据遗传学原理判断这四类的比例应为 $9:3:3:1$ 。为做验证，孟德尔在一次豌豆实验中收获了 $n=556$ 个豌豆，其中这四类豌豆的个数分别为 $315,108,101,32$ 。该数据是否与孟德尔提出的比例吻合？
这个问题可以转化为分类数据的检验问题。总体被分为 $r$ 类： $A_1,A_2,\cdots,A_r$ 。我们提出假设：

$$
H_0: A_i\text{ 所占的比率是 }p_{i0},\quad i=1,2,\cdots,r, $$

其中， $p_{i0}$ 已知，且满足 $\sum_{i=1}^r p_{i0}=1$ 。记 $x_1,x_2,\cdots,x_n$ 表示从该总体抽取的样本，且 $n_i$ 表示 $n$ 个样本中属于 $A_i$ 的样本个数。由于当 $H_0$ 成立时，在 $n$ 个样本中属于 $A_i$ 类的“期望个数” $np_{i0}$ 。而我们实际观测到的值为 $n_i$ ，故当 $H_0$ 成立时， $n_i$ 与 $np_{i0}$ 应相差不大。于是，卡尔·皮尔逊提出检验统计量

$$
\chi^2 = \sum_{i=1}^r \frac{(n_i - np_{i0})^2}{np_{i0}}
$$

来衡量“期望个数”与“实际个数”间的差异。
`````

``````{prf:theorem}
总体被分为 $r$ 类： $A_1,A_2,\cdots,A_r$ 。考虑假设：

$$
H_0: A_i\text{ 所占的比率是 }p_{i0},\quad i=1,2,\cdots,r, $$

其中， $p_{i0}$ 已知，且满足 $\sum_{i=1}^r p_{i0}=1$ 。记 $x_1,x_2,\cdots,x_n$ 表示从该总体抽取的样本，且 $n_i$ 表示 $n$ 个样本中属于 $A_i$ 的样本个数。
在 $H_0$ 成立时，检验统计量

$$
\chi^2 = \sum_{i=1}^r \frac{(n_i - np_{i0})^2}{np_{i0}} \overset{L}{\rightarrow} \chi^2(r-1).
$$

``````

```{admonition} Remark
根据上述定理，我们所确定的拒绝域为

$$
W = \{\chi^2 \geq \chi^2_{1-\alpha}(r-1)\}.
$$

这个检验通常称为皮尔逊 $\chi^2$ 拟合优度检验。
```

`````{prf:example} 例题续
（例 {prf:ref}`ex:chap23_pea_experiment` 续）：

根据题意，我们有：

```{list-table}
:header-rows: 1

* - $X$
  - 黄圆 $(A_{1})$
  - 绿圆 $(A_{2})$
  - 黄皱 $(A_{3})$
  - 绿皱 $(A_{4})$
* - 概率
  - $p_{10}=\frac{9}{16}$
  - $p_{20}=\frac{3}{16}$
  - $p_{30}=\frac{3}{16}$
  - $p_{40}=\frac{1}{16}$
* - 频数
  - $315$
  - $108$
  - $101$
  - $32$
```

于是，该统计量为

$$
\begin{eqnarray*}
\chi^2 &=& \frac{\left(315 - 556 \times \frac{9}{16}\right)^2}{ 556 \times \frac{9}{16}} +
\frac{\left(108 - 556 \times \frac{3}{16}\right)^2}{ 556 \times \frac{3}{16}} +
\frac{\left(101 - 556 \times \frac{3}{16}\right)^2}{ 556 \times \frac{3}{16}} +
\frac{\left(32 - 556 \times \frac{1}{16}\right)^2}{ 556 \times \frac{1}{16}}\\
&=& 0.47
\end{eqnarray*}
$$

若取显著性水平 $\alpha = 0.05$ ，则 $\chi^2_{0.95}(3) = 7.8147 > 0.47$ 。所以，认为孟德尔的结论是可接受的。
`````

从似然比检验的角度也可以得到皮尔逊 $\chi^2$ 拟合优度检验统计量。
样本的联合分布为

$$
P_{\theta}(X_1 = x_1,X_2=x_2,\cdots,X_n = x_n) = p_1^{n_1}p_2^{n_2}\cdots p_r^{n_r}=\prod_{i=1}^r p_i^{n_i}.
$$

由此求得

$$
\begin{eqnarray*}
\sup_{\theta \in\Theta} =P_{\theta}(X_1 = x_1,X_2=x_2,\cdots,X_n = x_n) = \prod_{i=1}^r \left(\frac{n_i}{n}\right)^{n_i},\\
\sup_{\theta \in\Theta} =P_{\theta}(X_1 = x_1,X_2=x_2,\cdots,X_n = x_n) = \prod_{i=1}^r \left(p_{i0}\right)^{n_i}
\end{eqnarray*}
$$

于是，似然比检验统计量为

$$
\Lambda(x_1,x_2,\cdots,x_n ) = \prod_{i=1}^r \left(\frac{n_i}{np_{i0}}\right)^{n_i}.
$$

由于

$$
\begin{eqnarray*}
\ln \Lambda(x_1,x_2,\cdots,x_n ) &=&\sum_{i=1}^r n_i \frac{n_i}{np_{i0}}\\
&=& \sum_{i=1}^r ( np_{i0} + (n_i-np_{i0})) \ln \left( 1 + \frac{n_i - np_{i0}}{np_{i0}}\right)\\
&=& \sum_{i=1}^r ( np_{i0} + (n_i-np_{i0})) \left( \frac{n_i - np_{i0}}{np_{i0}} - \frac{1}{2} \left( \frac{n_i - np_{i0}}{np_{i0}}\right)^2 + o(n^{-2})\right)\\
&\approx& \frac{1}{2} \sum_{i=1}^r \frac{(n_i - np_{i0})^2}{np_{i0}} + o(n^{-1}).
\end{eqnarray*}
$$

所以

$$
2\ln \Lambda(x_1,x_2,\cdots,x_n ) \approx \sum_{i=1}^r \frac{(n_i - np_{i0})^2}{np_{i0}} .
$$

```{admonition} Remark

- 在孟德尔豌豆实验中，诸 $p_{i0}$ 都是已知的。但实际中， $p_{i0}$ 可能依赖于 $k$ 个未知参数，这 $k$ 个参数可以通过最大似然估计来得到，此时检验统计量为

$$
\chi^2 = \sum_{i=1}^r \frac{(n_i - n\hat{p}_{i})^2}{n\hat{p}_{i}} \overset{L}{\rightarrow} \chi^2(r-k-1).
$$

- $\chi^2$ 检验法用于大样本场景，一般要求，各个类中的观测值均不能小于 5。

```

## 离散分布
设 $x_1,x_2,\cdots,x_n$ 是来自总体 $F(x)$ 的样本，所需要检验的原假设为

$$
H_0: F(x) = F_0(x)
$$

其中， $F_0(x)$ 称为理论分布，可以是一个完全已知的分布，也可以是一个依赖于有限个实参数且分布形式已知的分布函数。这类问题可以用 $\chi^2$ 拟合优度来解决。
设总体 $X$ 为取有限或可列个值 $a_1,a_2,\cdots$ 的离散随机变量。如有需要，可以将相邻的取值进行合并，最后分为有限个类 $A_1,A_2,\cdots,A_r$ ，并使得样本观测值 $x_1,x_2,\cdots,x_n$ 落入每个 $A_i$ 内的个数 $n_i$ 不少于 5。记 $P(X\in A_i) = p_i (i=1,2,\cdots,r)$ 。

`````{prf:example}
考虑卢瑟福实验的数据。表 {numref}`tab:chap23_discrete_distribution_chi2_test` 是卢瑟福以 7.5 秒为时间单位做的 2608 次观测得到的数据，观测的是一枚放射性 $\alpha$ 物质在单位时间点放射的质点数。
```{list-table} 卢瑟福实验数据
:header-rows: 1
:name: tab:chap23_discrete_distribution_chi2_test
* - 质点数 $k$ 
  - 0
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  - 9
  - 10
  - 11
  - 12
  - 13
  - 14
* - 观察数 $n_k$ 
  - 57
  - 203
  - 383
  - 525
  - 532
  - 408
  - 273
  - 139
  - 45
  - 27
  - 10
  - 4
  - 2
  - 0
  - 0
```
现要检验假设

$$
H_0: \text{数据服从泊松分布}P(\lambda)
$$

```{dropdown} Solution

首先，需要估计泊松分布参数 $\lambda$ 。因为其最大似然估计为样本均值，所以

$$
\hat{\lambda} = \bar{x} = 3.87.
$$

其次，计算各个类别的概率的估计值

$$
\hat{p}_k = \frac{\hat{\lambda}^k}{k!} e^{-\hat{\lambda}},k=0,1,2,\cdots
$$

为了满足每个类出现的样本观测次数不少于 5，我们将 $k\geq 11$ 作为一类。于是，检验统计量为

$$
\chi^2 = \sum_{i=0}^{11} \frac{(n_{i} - n \hat{p}_{i})^2}{n \hat{p}_i} = 12.8967.
$$

此时，卡方分布自由度为 $12-1-1 =10$ 。取显著性水平 $\alpha = 0.05$ ，临界值 $\chi^2_{0.95}(10) = 18.3070$ ，拒绝域为 $W = \{ \chi^2 \geq 18.3070\}$ ，观测结果的 $\chi^2$ 不落在拒绝域，因此不能拒绝 $H_0$ 。
```
`````
## 连续分布
设总体 $X$ 为连续随机变量，分布函数 $F_0(x)$ ，一般选取 $r-1$ 个实数 $a_1<a_2<\cdots<a_{r-1}$ ，将实数族分为 $r$ 个区间

$$
(-\infty, a_1],(a_1,a_2],\cdots, (a_{r-1},\infty)
$$

当观测值落入第 $i$ 个区间内，就把它看作属于第 $i$ 类，因此，这 $r$ 个区间就相当于 $r$ 个类。在 $H_0$ 为真时，记

$$p_i = P(a_{i-1} < X \leq a_i ) = F_0(a_i) - F_0(a_{i-1}) ,i=1,2,\cdots,r $$

其中， $a_0 = -\infty$ , $a_{r} = \infty$ ， 以 $n_i$ 表示样本的观测值 $x_1,x_2,\cdots,x_n$ 落入区间 $(a_{i-1},a_i]$ 内的个数。

`````{prf:example}
某工厂生产一种滚珠，现随机地抽取了 50 件产品，测得其直径为

$$
\begin{eqnarray*}
15.0, \quad 15.8, \quad 15.2, \quad 15.1, \quad 15.9, \quad
14.7, \quad 14.8, \quad 15.5, \quad 15.6, \quad 15.3\\
15.0, \quad 15.6, \quad 15.7, \quad 15.8, \quad 14.5, \quad
15.1, \quad 15.3, \quad 14.9, \quad 14.9, \quad 15.2\\
15.9, \quad 15.0, \quad 15.3, \quad 15.6, \quad 15.1, \quad
14.9, \quad 14.2, \quad 14.6, \quad 15.8, \quad 15.2\\
15.2, \quad 15.0, \quad 14.9, \quad 14.8, \quad 15.1, \quad
15.5, \quad 15.5, \quad 15.1, \quad 15.1, \quad 15.0\\
15.3, \quad 14.7, \quad 14.5, \quad 15.5, \quad 15.0, \quad
14.7, \quad 14.6, \quad 14.2, \quad 14.2, \quad 14.5
\end{eqnarray*}
$$

问滚珠直径是否服从正态分布？
```{dropdown} Solution

设滚珠直径为 $X$ ，其分布函数为 $F(x)$ ，现假设为

$$
H_0 : F(x) = \Phi\left(\frac{x-\mu}{\sigma}\right)
$$

对于此问题，我们首先需要估计 $\mu$ 和 $\sigma^2$ 。根据极大似然估计，

$$
\hat{\mu} = 15.1,\quad \hat{\sigma}^2 = 0.4379^2
$$

根据数据特点，我们取

$$
a_0 = -\infty,\quad a_1 = 14.55, \quad a_2 = 14.95, \quad a_3 = 15.35, \quad a_4 = 15.75, \quad a_5 = \infty
$$

各组数据个数分别为

$$
n_1 = 6, \quad n_2 = 11, \quad n_3 = 20, \quad n_4 = 8,\quad n_5 = 5.
$$

利用公式计算各组理论概率，即

$$
\hat{p}_i = \Phi\left(\frac{a_i-15.1}{0.4379}\right) - \Phi\left(\frac{a_{i-1}-15.1}{0.4379}\right) ,\quad i=1,2,3,4,5
$$

求得

$$
\hat{p}_1 = 0.104559, \quad \hat{p}_2 = 0.261412, \quad \hat{p}_3 = 0.349998, \quad \hat{p}_4 = 0.215174, \quad \hat{p}_5 = 0.068857
$$

于是，可以计算统计量

$$
\chi^{2} = 2.2109
$$

此时，分布自由度为 $5-2-1=2$ 。取显著性水平 $\alpha =0.05$ ，则 $\chi^2_{0.95}(2) = 5.9915>2.2109$ 。故不能拒绝原假设。
```
`````