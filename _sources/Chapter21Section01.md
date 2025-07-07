# 区间估计的概念
设 $x_{1},x_{2},\cdots,x_{n}$ 是样本。我们想要找到两个统计量 $\hat{\theta}_{L}=\hat{\theta}_{L}(x_{1},\cdots,x_{n})$ 和 $\hat{\theta}_{U}=\hat{\theta}_{U}(x_{1},\cdots,x_{n})$ ， $\hat{\theta}_{L}<\hat{\theta}_{U}$ 。于是，所构造的一个区间 $[\hat{\theta}_{L},\hat{\theta}_{U}]$ 为 $\theta$ 的一个区间估计。

```{admonition} Question
一个合适的区间估计应该有什么要求？
```

因为样本具有随机性，所以， $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 是一个随机区间。但待估参数 $\theta$ 是一个未知常数。我们通常要求区间 $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 盖住 $\theta$ 的概率

$$
P(\hat{\theta}_{L}\leq \theta\leq \hat{\theta}_{U})=P\left ( \left \{ \hat{\theta}_{L}\le \theta \right \}\cap \left \{ \hat{\theta}_{U}\le \theta \right \} \right )
$$

尽可能大。

设 $\theta$ 是总体的一个参数，其参数空间为 $\Theta$ ， $x_1,x_2,\cdots,x_n$ 是来自该总体的样本，对给定的一个 $\alpha(0<\alpha<1)$ ，假设有两个统计量 $\hat{\theta}_L = \hat{\theta}_L(x_1,x_2,\cdots,x_n)$ 和 $\hat{\theta}_U = \hat{\theta}_U(x_1,x_2,\cdots,x_n)$ ，若对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta\le \hat{\theta}_{U}) \geq 1-\alpha
$$

则称随机区间 $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的置信区间，或简称 $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 是 $\theta$ 的 $1-\alpha$ 置信区间， $\hat{\theta}_{L}$ 和 $\hat{\theta}_{U}$ 分别称为 $\theta$ 的（双侧）置信下限和置信上限。

```{admonition} Remark

- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta\le \hat{\theta}_{U}) = 1-\alpha
$$

则称 $\left[ \hat{\theta}_{L},\hat{\theta}_{u} \right]$ 是 $\theta$ 的 $1-\alpha$ 同等置信区间；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta) \geq 1-\alpha
$$

则称 $\hat{\theta}_{L}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）置信下限；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta) = 1-\alpha
$$

则称 $\hat{\theta}_{L}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）同等置信下限；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\theta\leq \hat{\theta}_{U}) \geq 1-\alpha
$$

则称 $\hat{\theta}_{U}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）置信上限；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\theta\leq \hat{\theta}_{U}) = 1-\alpha
$$

则称 $\hat{\theta}_{U}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）同等置信上限；

```