# 引导问题
在参数模型中，假定总体分布 $X\sim p(x;\boldsymbol{\theta}),\boldsymbol{\theta}\in \boldsymbol{\Theta}$ 。这里 $\boldsymbol{\theta}$ 是总体分布中的未知参数，可以是一维的，也可以是多维的。

`````{prf:example}
考虑以下两个总体分布：

- 若 $X \sim P(\lambda)$ 。这里总体分布存在一个泊松分布族，即

$$
\mathcal{P} = \left\{\frac{\lambda^x}{x!}e^{-\lambda}: \lambda > 0\right\},
$$

其中参数是 $\boldsymbol{\theta} = \lambda, \boldsymbol{\Theta} = R^{+}$ 。一旦 $\lambda = \lambda_0$ 确定后，总体分布就唯一确定。
- 若 $X \sim N(\mu,\sigma^2)$ 。这里总体分布存在一个正态分布族，即

$$
\mathcal{P} = \left\{\frac{1}{\sqrt{2\pi \sigma^2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}: \mu \in R, \sigma^2 > 0\right\},
$$

其中参数是 $\boldsymbol{\theta} = (\mu,\sigma^2)', \boldsymbol{\Theta} = R\times R^{+}$ 。一旦 $(\mu,\sigma^2) = (\mu_0,\sigma_0^2)$ 确定后，总体分布就唯一确定。

`````

实际中，参数模型中的参数都是未知的，而我们需要通过样本 $x_1,x_2,\cdots,x_n$ 来推断 $\boldsymbol{\theta}$ （或其函数 $g(\boldsymbol{\theta})$ ）。

估计
: 设 $x_1,x_2,\cdots,x_n$ 是来自总体的一个样本，称用于估计未知参数 $\boldsymbol{\theta}$ 的统计量

$$
\hat{\boldsymbol{\theta}} = \hat{\boldsymbol{\theta}}(x_1,x_2,\cdots,x_n)
$$

为 $\boldsymbol{\theta}$ 的估计量，或称为 $\boldsymbol{\theta}$ 的点估计，简称估计。

在本讲中，我们讲介绍三种频率学派的点估计思想：替换、拟合、似然及其对应的估计方法。