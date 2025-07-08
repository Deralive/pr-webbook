# 点估计

`````{prf:example}
回顾工厂生产产品的例子。我们想要估计产品的合格率 $\theta$ 。

- 现有样本 $x_1,x_2,\cdots,x_n$ 。每一个样本表示所抽中的产品是合格品还是不合格品。如果该产品是合格品，记 $x_i$ 为 1；如果该产品是不合格品，记 $x_i$ 为 0。用伯努利分布来刻画该数据分布，即 $x_i|\theta \sim b(1,\theta),i=1,2,\cdots,n$ 。
- 在估计之前，我们需要对参数 $\theta$ 有一个认识，即认为 $\theta$ 有一个先验分布。如何假定 $\theta$ 的先验分布？
 $\theta$ 表示 $(0,1)$ 之间的一个实数。根据我们所掌握的分布，可以采用贝塔分布 $Be(a,b)$ 来刻画这个分布。称 $a,b$ 为超参数。如何估计这两个超参数呢？

- 倘若有 $m$ 天的历史数据 $(n_1,x_1),\cdots,(n_m,x_m)$ ，可以得到 $\theta$ 的一个分布 $\pi(\theta)$ 。假定 $\pi(\theta) = Be(a,b)$ ，这里两个超参数 $a$ 和 $b$ 可以通过矩估计来获得。
- 倘若没有历史数据，我们认为 $\theta$ 在 $(0,1)$ 区间上的取值是等可能的，也就是说，可以用 $U(0,1) = Be(1,1)$ 来刻画这个先验分布。这就是“**同等无知**”的假定。

无论有无历史数据，我们可以得到先验分布 $Be(a,b)$ 。
- 我们需要求出 $\theta$ 的后验分布。贝叶斯公式就是其中所需要使用的关键。
设样本分布为 $p(x_1,x_2,\cdots,x_n|\theta)$ 。于是
 $(x_1,x_2,\cdots,x_n,\theta)$ 的联合概率函数为

$$
h(x_1,x_2,\cdots,x_n,\theta) = \pi(\theta) p(x_1,x_2,\cdots,x_n|\theta)
$$

令

$$
m(x_1,x_2,\cdots,x_n) = \int h(x_1,x_2,\cdots,x_n,\theta)\text{d}\theta =
\int \pi(\theta) p(x_1,x_2,\cdots,x_n|\theta)\text{d}\theta.
$$

于是，

$$
\begin{eqnarray*}
p(\theta|x_1,x_2,\cdots,x_n) &=& \frac{h(x_1,x_2,\cdots,x_n,\theta)}{m(x_1,x_2,\cdots,x_n) }\\
&=& \frac{\pi(\theta) p(x_1,x_2,\cdots,x_n|\theta)}{\int \pi(\theta) p(x_1,x_2,\cdots,x_n|\theta)\text{d}\theta }\\
&=& \frac{\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\theta^{a-1}(1-\theta)^{b-1}
\theta^{\sum_{i=1}^n x_i} (1-\theta)^{n-\sum_{i=1}^n x_i}}{\int \frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\theta^{a-1}(1-\theta)^{b-1}
\theta^{\sum_{i=1}^n x_i} (1-\theta)^{n-\sum_{i=1}^n x_i}\text{d}\theta }\\
&=&\frac{\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\theta^{a+\sum_{i=1}^n x_i -1}(1-\theta)^{b+n-\sum_{i=1}^n x_i-1}}
{\int \frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\theta^{a+\sum_{i=1}^n x_i -1}(1-\theta)^{b+n-\sum_{i=1}^n x_i-1}\text{d}\theta }\\
&=& \frac{\Gamma(a+b+n)}{\Gamma(a+\sum_{i=1}^n x_i)\Gamma(b+n-\sum_{i=1}^n x_i)} \theta^{a+\sum_{i=1}^n x_i -1}(1-\theta)^{b+n-\sum_{i=1}^n x_i-1}
\end{eqnarray*}
$$

因此， $\theta|x_1,x_2,\cdots,x_n \sim Be(a+\sum_{i=1}^n x_i,b+n-\sum_{i=1}^n x_i)$ ，这就是 $\theta$ 的后验分布。
- 基于后验分布，我们如何得到 $\theta$ 的点估计呢？

- MAP 估计，指的是求最大后验概率估计（ Maximum a Posteriori Probability estimator）。令

$$
\begin{eqnarray*}
l(\theta|x_1,x_2,\cdots,x_n) = \left(a+\sum_{i=1}^n x_i -1\right) \ln \theta + \left(b+n-\sum_{i=1}^n x_i-1\right) \ln (1-\theta)
\end{eqnarray*}
$$

该函数只有唯一最大值。我们可以对 $l(\theta)$ 关于 $\theta$ 求导，即

$$
\frac{\partial l(\theta)}{\partial \theta}= \frac{a+\sum_{i=1}^n x_i -1}{\theta} - \frac{b+n-\sum_{i=1}^n x_i-1}{1-\theta} =0
$$

解得

$$
\hat{\theta}_{\text{MAP}} = \frac{a+\sum_{i=1}^n x_i -1}{a+b+n-2}
$$

- 后验期望估计，指的是求后验分布的期望，又称为贝叶斯估计。
我们取后验分布的均值，即

$$
\hat{\theta}_{\text{Bayes}} = \frac{a+\sum_{i=1}^n x_i}{a+b+n} = \frac{a+b}{a+b+n} \cdot \frac{a}{a+b} + \frac{n}{a+b+n} \cdot\frac{\sum_{i=1}^n x_i}{n}.
$$

`````

以下我们介绍一个例子。

`````{prf:example}
样本 $x_1,x_2,\cdots,x_n$ 来自于正态分布 $N(\mu,\sigma_0^2)$ 。 $\mu$ 的先验分布为 $N(\mu_0,\tau^2)$ 。求 $\mu$ 的贝叶斯估计。
```{dropdown} Solution

 $\mu$ 的先验分布为

$$
\pi(\mu) = \frac{1}{\sqrt{2\pi \tau^2}} \exp\left\{
- \frac{1}{2\tau^2} (\mu-\mu_0)^2
\right\}.
$$

而样本 $(x_1,x_2,\cdots,x_n)$ 的联合密度函数为

$$
\begin{eqnarray*}
p\left(x_{1}, \cdots, x_{n} |\mu\right) &=& \prod_{i=1}^n \frac{1}{\sqrt{2\pi \sigma_0^2}} \exp\left\{-\frac{1}{2\sigma_0^2} (x_i-\mu)^2\right\}\\
&=& (2\pi \sigma_0^2)^{-n/2} \exp\left\{ -\frac{1}{2\sigma_0^2}\sum_{i=1}^n (x_i-\mu)^2 \right\}\\
&=&(2\pi \sigma_0^2)^{-n/2} \exp\left\{ -\frac{1}{2\sigma_0^2}\sum_{i=1}^n (x_i -\bar{x} + \bar{x}-\mu)^2 \right\}\\
&=&(2\pi \sigma_0^2)^{-n/2} \exp\left\{ -\frac{1}{2\sigma_0^2}\sum_{i=1}^n \left((x_i -\bar{x})^2 + (\bar{x}-\mu)^2 \right)\right\}\\
&=& (2\pi \sigma_0^2)^{-n/2}\exp\left\{ -\frac{1}{2\sigma_0^2}\sum_{i=1}^n (x_i -\bar{x})^2 \right\} \cdot \exp\left\{ -\frac{n}{2\sigma_0^2}(\bar{x}-\mu)^2 \right\}.
\end{eqnarray*}
$$

于是， $\mu$ 的后验分布为

$$
\begin{eqnarray*}
\pi(\mu|x_1,x_2,\cdots,x_n) &=& \frac{\pi(\mu) p(x_1,x_2,\cdots,x_n|\mu)}{m(x_1,x_2,\cdots,x_n)}\\
&\propto& \pi(\mu) p(x_1,x_2,\cdots,x_n|\mu)\\
&\propto& \exp\left\{
- \frac{1}{2\tau^2} (\mu-\mu_0)^2
\right\} \cdot \exp\left\{ -\frac{n}{2\sigma_0^2}(\mu- \bar{x})^2 \right\}\\
&\propto& \exp\left\{ -\frac{1}{2} \left( \left( \frac{1}{\tau^2} + \frac{1}{\sigma_0^2/n}\right) \mu^2 - 2 \left( \frac{\mu_0}{\tau^2} + \frac{\bar{x}}{\sigma_0^2/n}\right)\mu \right)\right\}\\
&=& \exp\left\{ -\frac{1}{2} \left( A \mu^2 - 2 B\mu \right)\right\}.
\end{eqnarray*}
$$

其中， $A = \left( \frac{1}{\tau^2} + \frac{1}{\sigma_0^2/n}\right)$ 和 $B = \left( \frac{\mu_0}{\tau^2} + \frac{\bar{x}}{\sigma_0^2/n}\right)$ 。
这里利用配方公式，我们可知，

$$
A\mu^2 - 2B\mu = A \left(\mu - \frac{B}{A}\right)^2 - \frac{B^2}{A}.
$$

从分布核中可以发现， $\mu$ 的后验分布是正态分布 $N\left(\frac{B}{A},A^{-1}\right)$ ，即

$$
N\left(\frac{\frac{\mu_0}{\tau^2} + \frac{\bar{x}}{\sigma_0^2/n}}{\frac{1}{\tau^2} + \frac{1}{\sigma_0^2}}, \frac{1}{\frac{1}{\tau^2} + \frac{1}{\sigma_0^2/n}}\right).
$$

基于后验分布，MAP 估计和后验期望估计一致的，即

$$
\hat{\mu}_{\text{MAP}} = \hat{\mu}_{\text{Bayes}} = \frac{\frac{\mu_0}{\tau^2} + \frac{\bar{x}}{\sigma_0^2/n}}{\frac{1}{\tau^2} + \frac{1}{\sigma_0^2/n}} = \frac{1/\tau^2}{1/\tau^2+1/(\sigma_0^2/n)} \mu_0 + \frac{1/(\sigma_0^2)}{1/\tau^2+1/(\sigma_0^2/n)} \bar{x}
$$

```
`````

```{admonition} Remark

- 在正态分布的例子中，均值 $\mu$ 的贝叶斯估计本质上是先验分布均值 $\mu_0$ 和样本均值 $\bar{x}$ 的加权平均数，其权重本质上是该分布的方差的倒数，也称为该分布的精度。
- 所求的后验分布与先验分布的分布都是正态分布，这是贝叶斯估计里一种特殊且具有一定普遍性的现象。

```

共轭先验分布（族）
: 若后验分布 $\pi \left(\theta \mid x_{1}, \cdots, x_{n}\right)$ 与先验分布属于同一分布族，则称该分布族是 $\theta$ 的共轭先验分布（族）。

这里我们针对贝叶斯估计做一些更为深入的讨论。

```{admonition} Remark

- **充分性原则体现在贝叶斯估计之中**。
由于贝叶斯估计是根据参数的后验分布求得的，而参数的后验分布为

$$
\begin{eqnarray*}
\pi(\theta | x_1,x_2,\cdots,x_n) &\propto& \pi(\theta) \cdot p(x_1,x_2,\cdots,x_n|\theta)\\
&=& \pi(\theta) \cdot g(t(x_1,x_2,\cdots,x_n),\theta) h(x_1,x_2,\cdots,x_n)\\
&\propto& \pi(\theta) \cdot g(t(x_1,x_2,\cdots,x_n),\theta)
\end{eqnarray*}
$$

其中第二个等式成立是根据因子分解定理， $t(x_1,x_2,\cdots,x_n)$ 是 $\theta$ 的充分统计量。
- **贝叶斯估计是一种整体最优的估计方法**。
对于 $\theta$ 的任意一种估计 $\hat{\theta}(x_1,x_2,\cdots,x_n)$ ，我们之前介绍过可以通过均方误差来进行评价，即

$$
\begin{eqnarray*}
\text{MSE}_{\theta}(\hat{\theta}) &=& E_{x_1,x_2,\cdots,x_n}(\hat{\theta}-\theta)^2\\
&=& \int_{x_n \in R} \cdots \int_{x_1 \in R} (\hat{\theta}-\theta)^2 p(x_1,x_2,\cdots,x_n|\theta) \text{d}x_1\cdots\text{d}x_n\\
&=& \int_{\boldsymbol{x} \in R^{n}} (\hat{\theta}-\theta)^2 p(\boldsymbol{x}|\theta) \text{d} \boldsymbol{x}.
\end{eqnarray*}
$$

这里 $\boldsymbol{x} = (x_1,x_2,\cdots,x_n)'$ 。我们之前在介绍均方误差时，参数 $\theta$ 认为是一个未知常数，但在贝叶斯学派中， $\theta$ 认为是一个随机变量，所以 $MSE(\hat{\theta})$ 也被认为是一个随机变量，其依赖于 $\theta$ 。我们可以整体来比较估计的均方误差，于是计算均方误差的期望，即

$$
\begin{eqnarray*}
E_\theta(\text{MSE}_{\theta}(\hat{\theta})) &=& \int_{\theta \in \Theta} \int_{\boldsymbol{x} \in R^{n}} \left( \int (\hat{\theta}-\theta)^2 p(\boldsymbol{x}|\theta) \text{d} \mathbf{x} \right)\cdot \pi(\theta) \text{d} \theta\\
&=& \int_{\theta \in \Theta} \int_{\mathbf{x} \in R^{n}} (\hat{\theta}-\theta)^2 p(\mathbf{x}|\theta) \cdot \pi(\theta) \text{d} \mathbf{x} \text{d} \theta\\
&=& \int_{\theta \in \Theta} \int_{\mathbf{x} \in R^{n}} (\hat{\theta}-\theta)^2 \pi(\theta|\mathbf{x}) m(\mathbf{x})\text{d} \mathbf{x} \text{d} \theta\\
&=&\int_{\mathbf{x} \in R^{n}} \int_{\theta \in \Theta} (\hat{\theta}-\theta)^2 \pi(\theta|\mathbf{x}) \text{d} \theta m(\mathbf{x}) \text{d} \mathbf{x}
\end{eqnarray*}
$$

令 $\int_{\theta \in \Theta} (\hat{\theta}-\theta)^2 \pi(\theta|\mathbf{x}) \text{d} \theta$ 为 $R(\hat{\theta}|\mathbf{x})$ ，称其为条件风险函数。对于给定的样本 $\mathbf{x} = (x_1,x_2,\cdots,x_n)'$ ，我们所求的贝叶斯估计是使得条件风险函数最小的估计，即

$$
\hat{\theta}_{\text{Bayes}} = \arg\min_{\hat{\theta}} R(\hat{\theta}|\mathbf{x}).
$$

我们对 $R(\hat{\theta}|\mathbf{x})$ 关于 $\hat{\theta}$ 求导，即

$$
\begin{eqnarray*}
\frac{\partial R(\hat{\theta}|\mathbf{x})}{\partial \hat{\theta}} &=& \frac{\partial }{\partial \hat{\theta}} \int_{\theta \in \Theta} (\hat{\theta}-\theta)^2 \pi(\theta|\mathbf{x}) \text{d} \theta\\
& = & \int_{\theta \in \Theta} \frac{\partial }{\partial \hat{\theta}} \left((\hat{\theta}-\theta)^2 \pi(\theta|\mathbf{x}) \right)\text{d} \theta \\
&=& \int_{\theta \in \Theta} \left( 2(\hat{\theta} - \theta) \pi(\theta|\mathbf{x}) \right)\text{d} \theta
\end{eqnarray*}
$$

其中第二个等式成立是有条件的。如果感兴趣的同学可以参考华东师范大学数学系编写的《数学分析（下册）》第 187 页定理 19.3。
令

$$\int_{\theta \in \Theta} \left( 2(\hat{\theta} - \theta) \pi(\theta|\mathbf{x}) \right)\text{d} \theta = 0$$

即

$$
\hat{\theta} = \int_{\theta \in \Theta} \theta \pi(\theta|\mathbf{x})\text{d} \theta = E(\theta|\mathbf{x})
$$

这就是我们定义的贝叶斯估计。

```

## 参考书目
对贝叶斯学派感兴趣的同学，这里提供了一些贝叶斯统计方面的学习资料列表。

- Gelman A, Carlin J B, Stern H S, et al. Bayesian data analysis[M]. CRC press, 2013.
- B 站：《贝叶斯统计 梅长林 西安交通大学》系列视频.
- 茆诗松，汤银才.贝叶斯统计. 中国统计出版社.