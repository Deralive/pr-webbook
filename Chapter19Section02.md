# 替换思想
## 矩法
替换的本质思想是：利用经验分布函数 $F_n(x)$ 来替换总体分布函数 $F(x)$ 。这里因为我们假定了参数模型，由参数唯一能够决定分布函数，于是记为 $F_{\theta}(x)$ 。比较一下这两个“分布”函数是不同的。

- $F_n(x)$ ：基于样本可计算而得，是完全已知的；
- $F_{\theta}(x)$ ：一定存在未知的信息，完全未知或部分未知；

替换原理，是有卡尔·皮尔逊教授于 1900 年提出的，也被称为**矩法**。简单可以概括为

- 用样本矩替换总体矩（既可以是原点矩，也可以是中心矩）；
- 用样本矩的函数去替换相应的总体矩的函数；

这个替换原理也可以应用于分布未知的场合，对参数作出估计，即

- 用样本均值 $\bar{x}$ 估计总体均值 $E(X)$ ；
- 用样本方差 $s^2$ 估计总体方差 $\text{Var}(X)$ ；
- 用事件 $A$ 出现的频率估计事件 $A$ 发生的概率；
- 用样本的 $p$ 分位数估计总体的 $p$ 分位数。

## 矩估计
基于替换原理，以下我们给出得到矩估计的具体步骤：

- 设总体具有已知的概率函数 $p(x;\theta_{1},\theta_{2},\cdots,\theta_{k}),(\theta_{1},\cdots,\theta_{k})\in \Theta$ 是未知参数（向量）；
- 得到样本 $x_{1},x_{2},\cdots,x_{n}$ ；
- 假设总体分布的 $k$ 阶原点矩 $\mu_{k}$ 存在（对所有的 $0<j\leq k$ ，各低阶矩 $\mu_{j}$ 均存在）；
- 若假设 $\theta_{1},\theta_{2},\cdots,\theta_{k}$ 能表示成总体矩 $\mu_{1},\mu_{2},\cdots,\mu_{k}$ 的函数，即

$$\theta_{j}=\theta_{j}(\mu_{1},\mu_{2},\cdots,\mu_{k})$$

则可给出诸 $\theta_{j}$ 的矩估计

$$\hat{\theta}_{j}=\theta_{j}(a_{1},a_{2},\cdots,a_{k}),j=1,2,\cdots,k$$

其中， $a_{j}=\frac{1}{n}\sum_{i=1}^{n}x_{i}^{j}$ ，是 $j$ 阶样本原点矩， $j=1,2,\cdots,k.$ 
- 另外，我们要估计参数的函数 $\eta =\eta (\theta _{1} ,\theta _{2} ,\cdots ,\theta _{k})$ ，则 $\eta$ 的矩估计为

$$\hat{\eta } =\eta (\hat{\theta}_{1} ,\hat{\theta }_{2} ,\cdots ,\hat{\theta}_{k}).$$

`````{prf:example}
设总体为指数分布，即

$$
p(x;\lambda) = \lambda e^{-\lambda}, x\geq 0.
$$

 $x_1,x_2,\cdots,x_n$ 是样本。
一方面，注意到 $E(X) = 1/\lambda$ ，即 $\lambda= 1/E(X)$ 。故 $\lambda$ 的矩估计为

$$
\hat{\lambda}_1 = \frac{1}{\bar{x}}.
$$

另一方面，由于 $\text{Var}(X) = 1/\lambda^2$ ，即 $\lambda = 1/\sqrt{\text{Var}(X)}$ 。故 $\lambda$ 的矩估计为

$$
\hat{\lambda}_2 = \frac{1}{s}.
$$

`````

```{admonition} Remark
这表明了矩估计不唯一，但通常应该尽量采用**低阶矩**给出未知参数的估计。
```

`````{prf:example}
设一个实验有三种可能结果，其发生的概率分别为

$$p_{1}=\theta^{2},\quad p_{2}=2\theta(1-\theta) ,\quad p_{3}=(1-\theta)^{2}$$

现在估了 $n$ 次试验，观测到三种结果发生的次数分别为 $n_{1},n_{2},n_{3}$ 。如何估计 $\theta$ ？

````{dropdown} Solution

设该实验的三种结果分别是 $a_1,a_2,a_3$ 。于是，分布列如表 {numref}`tab:lecture18_1` 。

```{list-table} 三种结果的实验
:header-rows: 1
:name: tab:lecture18_1
* - 结果
  - $a_1$ 
  - $a_2$ 
  - $a_3$ 
* - 概率
  - $\theta^2$ 
  - $2\theta(1-\theta)$ 
  - $(1-\theta)^2$ 
* - 频率
  - $\frac{n_1}{n}$ 
  - $\frac{n_2}{n}$ 
  - $\frac{n_3}{n}$ 
```

为估计 $\theta$ ，我们可以构建三个矩估计，即

- 可以用 $n_1/n$ 来估计 $\theta^2$ ，则

$$\hat{\theta}_1 = \sqrt{\frac{n_1}{n}}.$$

- 可以用 $n_3/n$ 来估计 $(1-\theta)^2$ ，则

$$\hat{\theta}_2 = 1 - \sqrt{\frac{n_3}{n}}.$$

- 可以用 $n_1/n + n_2/(2n)$ 来估计 $\theta$ ，则

$$\hat{\theta}_3 = \frac{2n_1 + n_2}{2n}.$$

````
`````

`````{admonition} Question
都是针对 $\theta$ 的估计，三种估计 $\hat{\theta}_1,\hat{\theta}_2,\hat{\theta}_3$ 有无好坏差异？
`````