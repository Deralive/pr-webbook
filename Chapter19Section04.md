# 似然思想

```{admonition} Question
考虑有两个盒子各有 100 个球，记为 A 盒和 B 盒。A 盒中有 99 个白球，1 个黑球；B 盒中有 1 个白球，99 个黑球。我们从某个盒子中抽出了一个球，发现这个球是白球。请问：我们是从哪个盒子中抽出球的？
```

```{admonition} Remark
似然思想的本质是“以成败论英雄”。
```

最大似然估计，顾名思义就是使得似然函数的最大值点。

```{admonition} Question
什么是似然函数？
```

似然函数
: 设总体分布的概率分布列或概率密度函数为 $p(x;\theta)$ ，其中 $\theta$ 是未知参数。而 $x_1,x_2,\cdots,x_n$ 是样本。 $x_1,x_2,\cdots,x_n$ 的联合分布列或联合密度函数为

$$
p(x_1,x_2,\cdots,x_n;\theta) = \prod_{i=1}^n p(x_i;\theta).
$$

对于未知参数 $\theta$ 而言，称 $p(x_1,x_2,\cdots,x_n;\theta)$ 为似然函数，记为 $L(\theta)$ .

既然我们明确了，似然函数本质上就是样本的联合概率（质量/密度）函数。将其看成参数的函数，这个函数就是似然函数。于是，我们给出最大似然估计明确的定义。

最大似然估计
: 
设 $\theta$ 是待估参数， $L(\theta)$ 是似然函数。如果统计量 $\hat{\theta} = \hat{\theta}(x_1,x_2,\cdots,x_n)$ 满足

$$
L(\hat{\theta}) = \sup_{\theta\in \overline{\Theta}} L(\theta).
$$

那么称 $\hat{\theta}$ 是 $\theta$ 的最大似然估计，记为 MLE(maximum likelihood estimate)。

```{admonition} Remark
这里 $\overline{\Theta}$ 包括 $\theta$ 的定义域 $\Theta$ 及其边界。
```

```{admonition} Question
最大似然估计怎么求？
```

求最大似然估计的一般步骤为

- 求对数似然函数，即 $l(\theta) = \ln L(\theta)$ .
- 求对数似然函数的驻点 $\hat{\theta}$ ，即 $\hat{\theta}$ 满足

$$
\frac{\partial l(\theta)}{\partial \theta} = 0.
$$

- 验证 $\hat{\theta}$ 是 $L(\theta)$ 或 $l(\theta)$ 的最大值点。

```{admonition} Remark
从上述步骤来看，就是找似然函数或者对数似然函数的最大值点，这才是本质问题。
```

`````{prf:example}
设总体分布 $X\sim b(1,\theta)$ ，而 $x_1,x_2,\cdots,x_n$ 是样本。于是， $x_1,x_2,\cdots,x_n$ 的联合分布列为

$$
p(x_1,x_2,\cdots,x_n) = (\theta)^{\sum_{i=1}^n x_i} (1-\theta)^{n-\sum_{i=1}^n x_i}
$$

这也是似然函数，记为 $L(\theta)$ 。然后，对数似然函数为

$$
l(\theta) = \ln L(\theta) = \sum_{i=1}^n x_i \ln (\theta) + (n-\sum_{i=1}^n x_i) \ln (1-\theta).
$$

对 $l(\theta)$ 关于 $\theta$ 求导，即

$$
0=\frac{\partial l(\theta)}{\partial \theta} = \frac{\sum_{i=1}^n x_i}{\theta} - \frac{n-\sum_{i=1}^n x_i}{1-\theta}.
$$

由此可得

$$
\hat{\theta} = \frac{1}{n} \sum_{i=1}^n x_i = \bar{x}.
$$

我们还可以验证

$$
\left. \frac{\partial^2 l(\theta)}{\partial \theta^2}\right|_{\theta = \hat{\theta}} = \left.-\frac{\sum_{i=1}^n x_i}{\theta^2} - \frac{n-\sum_{i=1}^n x_i}{(1-\theta)^2} \right|_{\theta = \hat{\theta}} < 0
$$

所以， $\hat{\theta}$ 是 $l(\theta)$ 最大值点。因此， $\theta$ 的最大似然估计为 $\bar{x}$ .
`````

`````{prf:example}
设该实验的三种结果分别是 $a_1,a_2,a_3$ 。于是，分布列如表 {numref}`tab:lecture18_2` 。
这里我们介绍 $\theta$ 的最大似然估计。
```{list-table} 三种结果的实验
:header-rows: 1
:name: tab:lecture18_2
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
首先，似然函数为

$$
L(\theta) = \frac{n!}{n_1!n_2!n_3!} (\theta^2)^{n_1} (2\theta (1-\theta))^{n_2}((1-\theta)^2)^{n_3} = \frac{n!}{n_1!n_2!n_3!} 2^{n_2}\theta^{2n_1+n_2}(1-\theta)^{n_2+2n_3}.
$$

而对数似然函数为

$$
l(\theta) = \ln L(\theta) = \ln \left(\frac{n!}{n_1!n_2!n_3!} 2^{n_2} \right) + (2n_1+n_2) \ln (\theta) + (n_2+2n_3) \ln (1-\theta).
$$

然后对 $l(\theta)$ 关于 $\theta$ 求导，即

$$
\frac{\partial l(\theta)}{\partial \theta} = \frac{2n_1+n_2}{\theta} - \frac{n_2+2n_3}{1-\theta}.
$$

可以解得

$$
\hat{\theta} = \frac{2n_1 + n_2}{2n_1 + n_2 + n_2 + 2n_3} = \frac{2n_1 + n_2}{2n}.
$$

`````

```{admonition} Remark
“求导”是求最大似然估计最常用的方法，但并不是在所有场合求导都有效。
```

`````{prf:example}
设总体分布 $U(0,\theta)$ ，而 $x_1,x_2,\cdots,x_n$ 是样本。
 $\theta$ 的似然函数为

$$
\begin{eqnarray*}
L(\theta) &=& \prod_{i=1}^n \frac{1}{\theta} I(0 < x_i < \theta)\\
&=&\frac{1}{\theta^n} I( 0 < x_1,x_2,\cdots,x_n < \theta)\\
&=&\frac{1}{\theta^n} I( 0 < x_{(1)}\leq x_{(n)} < \theta)
\end{eqnarray*}
$$

要使得 $L(\theta)$ 达到最大。对于示性函数取值应为 1，而 $1/(\theta^n)$ 是 $\theta$ 的减函数。所以， $\theta$ 的取值应尽可能小，而 $\theta$ 要大于 $x_{(n)}$ ，所以 $\Theta = (x_{(n)},\infty)$ ，而 $\overline{\Theta} = [x_{(n)},\infty)$ 。因此， $\theta$ 的最大似然估计为

$$
\hat{\theta} = x_{(n)}.
$$

`````

以上的例子都是一维参数的情况，以下我们举一个二维参数的例子。

`````{prf:example}
设总体分布 $X\sim N(\mu,\sigma^2)$ ， $\theta = (\mu,\sigma^2)$ 是二维参数。而 $x_1,x_2,\cdots,x_n$ 是样本。于是，似然函数为

$$
L(\mu,\sigma^2) = \prod_{i=1}^n p(x_i) = (2\pi \sigma^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i-\mu)^2\right\}.
$$

而其对数似然函数为

$$
l(\mu,\sigma^2) = \ln L(\mu,\sigma^2) = -(n/2)\ln (2\pi ) - (n/2) \ln (\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i-\mu)^2.
$$

对 $l(\mu,\sigma^2)$ 分别关于 $\mu$ 和 $\sigma^2$ 求导，即

$$
\begin{eqnarray*}
\frac{\partial l(\mu,\sigma^2)}{\partial \mu} &=& \frac{1}{\sigma^2} \sum_{i=1}^n (x_i - \mu) = 0\\
\frac{\partial l(\mu,\sigma^2)}{\partial \sigma^2} &=& -\frac{n}{2\sigma^2} + \frac{1}{2(\sigma^2)^2} \sum_{i=1}^n (x_i-\mu)^2 =0
\end{eqnarray*}
$$

由此解得

$$
\left\{
\begin{aligned}
& \hat{\mu} = \bar{x},\\
& \hat{\sigma}^2 = s_n^2.
\end{aligned}
\right.
$$

`````

```{admonition} Question
如何求 $\sigma$ 的最大似然估计？
```

`````{prf:property} 最大似然估计的不变性
如果 $\hat{\theta}$ 是 $\theta$ 的最大似然估计， 则对任一函数 $g(\theta)$ ， $g(\hat{\theta})$ 是其最大似然估计。
`````