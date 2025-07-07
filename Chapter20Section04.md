# 大样本的评估方式 2——渐近正态性

若 $\hat{\theta}_n$ 是 $\theta$ 的相合估计。若存在趋于 $0$ 的非负常数序列 $\sigma_n(\theta)$ ，使得

$$
\frac{\hat{\theta}-n \theta}{\sigma_n(\theta)}
$$

按分布收敛于标准正态分布。称 $\hat{\theta}_n$ 是渐近正态的，又称 $\hat{\theta}_n$ 服从渐近正态分布 $N(\theta,\sigma_n^2(\theta))$ ，记为

$$
\hat{\theta}_n \sim AN (\theta,\sigma_n^2(\theta)).
$$

其中称 $\sigma_n^2(\theta)$ 为 $\hat{\theta}_n$ 的渐近方差。

在三种估计方法中，矩估计、最小二乘估计以及最大似然估计在现有理论中一般可以论证其的渐近正态性。其中，最大似然估计的渐近正态性的表现具有一定普遍性，有以下定理。

``````{prf:theorem}
设总体 $X$ 有概率函数 $p(x;\theta),\theta\in \Theta$ ， $\Theta$ 为非退化区间，假定

- 对任意 $x$ ，偏导数 $\frac{\partial \ln p}{\partial \theta}, \frac{\partial^2 \ln p}{\partial \theta^2}, \frac{\partial^3 \ln p}{\partial \theta^3}$ 对所有 $\theta \in \Theta$ 都存在；
- 对任意 $\theta \in \Theta$ ，有

$$
\left|\frac{\partial \ln p}{\partial \theta} \right| < F_1(x),\quad \left|\frac{\partial^2 \ln p}{\partial \theta^2} \right| < F_2(x), \quad
\left|\frac{\partial^3 \ln p}{\partial \theta^3} \right| < F_3(x),
$$

其中函数 $F_1(x),F_2(x),F_3(x)$ 满足

$$
\int_{-\infty}^{\infty} F_1(x) \text{d} x < \infty, \int_{-\infty}^{\infty} F_2(x) \text{d} x < \infty, \sup_{\theta \in \Theta} \int_{-\infty}^{\infty} F_3(x) p(x;\theta)\text{d} x < \infty.
$$

- Fisher 信息量为

$$
I(\theta) = \int_{-\infty}^{\infty} \left(\frac{\partial \ln p}{\partial \theta}\right)^2 p(x;\theta) \text{d}x
$$

对任意 $\theta \in \Theta$ ， $0<I(\theta)<\infty$ 。

若 $x_1,x_2,\cdots,x_n$ 是来自该总体的样本，则存在未知参数 $\theta$ 的最大似然估计 $\hat{\theta}_n = \hat{\theta}_n(x_1,x_2,\cdots,x_n)$ ，且 $\hat{\theta}_n$ 具有相合性和渐近正态性，即

$$
\hat{\theta}_n \sim AN \left(\theta,\frac{1}{nI(\theta)}\right).
$$

``````

```{admonition} Remark
值得关注的是，最大似然估计的渐近方差为样本量为 $n$ 的样本的 Fisher 信息量——这是参数 $\theta$ 的无偏估计的方差的 CR 下界。如果一个参数的无偏估计的方差恰好达到了 CR 下界，那么这个估计被称为**有效估计**，认为其实所有无偏估计中方差最小的估计，也就是说，在无偏估计中最优的估计。虽然 MLE 不一定都是无偏的，但 MLE 通常是渐近无偏的，而且其渐近方差可达到无偏估计的方差的 CR 下界。
因此，一般认为，在**参数模型的假定正确**时，最大似然估计通常是最优的估计。
```

`````{prf:example}
设总体分布为泊松分布 $P(\lambda)$ ，可以证明 ${\lambda}$ 的矩估计和最大似然估计为

$$
\hat{\lambda}_n = \bar{x}_n = \frac{1}{n} \sum_{i=1}^n x_i.
$$

根据中心极限定理可知，

$$
\frac{\hat{\lambda}_n - \lambda}{\sqrt{\lambda /n}} \overset{L}{\longrightarrow} N(0,1).
$$

所以， $\hat{\lambda}_n$ 是渐近正态的，即

$$
\hat{\lambda}_n \sim AN(\lambda, \lambda/n).
$$

总体分布的分布列为

$$
p(x;\lambda) = \frac{\lambda^x}{x!} e^{-\lambda}
$$

其对数为

$$
\ln p(x;\lambda) = x \ln \lambda - \ln x! - \lambda.
$$

其导数为

$$
\frac{\partial \ln p}{\partial \lambda} = \frac{x}{\lambda} -1
$$

所以，Fisher 信息量为

$$
\begin{eqnarray*}
I(\lambda) &=& \int_{-\infty}^{\infty} \left(\frac{\partial \ln p}{\partial \lambda}\right)^2 p(x;\lambda) \text{d}x \\
&=& \sum_{x=0}^{\infty} \left( \frac{x}{\lambda} -1\right)^2 p(x;\lambda) \\
&=& \frac{E(X^2)}{\lambda^2} - \frac{2E(X)}{\lambda} +1 \\
&=& \frac{\lambda + \lambda^2}{\lambda^2} - 1 \\
&=& \frac{1}{\lambda}.
\end{eqnarray*}
$$

所以， $\hat{\theta}_n$ 服从渐近正态分布，即

$$
\hat{\theta}_n \sim AN (\lambda, \lambda/n).
$$

`````