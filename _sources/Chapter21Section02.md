# 枢轴量法

````{admonition} Question
如何求 $1-\alpha$ 置信区间？

```{dropdown} Solution

我们知道 $\theta$ 的点估计为 $x_{(n)}$ ，而且我们知道

$$
\frac{x_{(n)}}{\theta} \sim Be(n,1).
$$

于是， $x_{(n)}/\theta$ 就是我们所构造的枢轴量。我们希望找到两个常数 $c_!$ 和 $c_2$ 使得

$$
P(c_1 \leq \frac{x_{(n)}}{\theta} \leq c_2) = 1-\alpha.
$$

一旦可以确定 $c_1$ 和 $c_2$ ，我们可以得到 $\theta$ 的 $1-\alpha$ 置信区间为

$$
\left[\frac{x_{(n)}}{c_2}, \frac{x_{(n)}}{c_1}\right].
$$

显然满足条件的 $(c_1,c_2)$ 个数是无穷的。这里我们考虑最短的置信区间。因为我们知道，对于一个随机变量 $X\sim Be(n,1)$ ，其密度函数为

$$
p(x) = nx^{n-1}, 0<x<1.
$$

于是，

$$
P(X\leq c) = \int_{0}^c nx^{n-1}\text{d}x = c^{n}.
$$

我们令 $c_1^n = \alpha_1$ ， $c_2^n = 1-(\alpha-\alpha_1)$ 。我们要求 $(c_1,c_2)$ 使得

$$
\frac{1}{c_1} - \frac{1}{c_2}
$$

达到最小。
所以，我们构造了一个函数

$$
l(\alpha_1) = \alpha_1^{-1/n} - (1-\alpha+\alpha_1)^{-1/n}, 0<\alpha_1<\alpha
$$

我们可以证明 $l(\alpha_1)$ 是一个单调递减的函数，则 $l(\alpha_1)$ 在 $\alpha_1 = \alpha$ 处取到最小值。于是，

$$
c_1 = \alpha^{1/n},\quad c_2 = 1.
$$

因此， $\theta$ 的 $1-\alpha$ 置信区间为

$$
\left[ x_{(n)}, x_{(n)} \cdot \alpha^{-1/n} \right].
$$
```
````

`````{prf:example}
若总体分布为 $N(\mu,\sigma^2)$ ，其中 $\sigma^2$ 是待估参数，而 $\mu$ 也是未知的。 $x_1,x_2,\cdots,x_n$ 是样本。这里我们考虑 $\sigma^2$ 的 $1-\alpha$ 置信区间。首先考虑 $\sigma^2$ 的点估计为

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2
$$

其分布为

$$
\frac{(n-1)s^2}{\sigma^2} \sim \chi^2(n-1).
$$

很自然地我们想要找到两个常数 $c_1$ 和 $c_2$ 使得

$$
P(c_1\leq \frac{(n-1)s^2}{\sigma^2}\leq c_2 ) =1-\alpha
$$

当然，我们可以类似于例题 1.3 的做法求解最短的区间，但是我们也可以取

$$
c_1 = \chi_{\alpha/2}^{2}(n-1), \quad c_2 = \chi_{1-\alpha/2}^{2}(n-1).
$$

虽然这个区间不是最短的，但是它是最简单的取法。于是， $\sigma^2$ 的 $1-\alpha$ 置信区间为

$$
\left[ \frac{(n-1)s^2}{\chi_{1-\alpha/2}^{2}(n-1)}, \frac{(n-1)s^2}{\chi_{\alpha/2}^{2}(n-1)}\right].
$$

这个区间被称为等尾置信区间。
`````

以上介绍例子大多都是在正态总体假定下的置信区间估计的构造方法。这些方法还可以应用于大样本的情形中。

`````{prf:example}
若总体分布为 $b(1,\theta)$ ，其中 $\theta$ 是待估参数。 $x_1,x_2,\cdots,x_n$ 是样本。当样本量 $n$ 比较大时，我们想要得到 $\theta$ 的 $1-\alpha$ 置信区间。
首先考虑 $\theta$ 的点估计，即

$$
\hat{\theta} = \bar{x} = \frac{1}{n}\sum_{i=1}^n x_i.
$$

因为样本量 $n$ 比较大，这里我们可以考虑 $\bar{x}$ 的渐近分布，即

$$
\frac{\bar{x} - \theta}{\sqrt{\theta(1-\theta)/n}} \sim AN(0,1).
$$

因此， $\frac{\bar{x} - \theta}{\sqrt{\theta(1-\theta)/n}}$ 就是我们所构造的（渐近）枢轴量。类似于正态总体下的置信区间，我们取 $\pm z_{1-\alpha/2}$ ，有

$$
P\left( - z_{1-\alpha/2} \leq \frac{\bar{x} - \theta}{\sqrt{\theta(1-\theta)/n}} \leq z_{1-\alpha/2} \right)= 1-\alpha.
$$

于是，我们需要从上述等式的左边将 $\theta$ 反解出来。

- 第一种想法：通过解一个一元二次不等式，从而得到 $\theta$ 的置信区间。具体来说，

$$
\frac{|\bar{x} - \theta|}{\sqrt{\theta(1-\theta)/n}} \leq z_{1-\alpha/2}
$$

- 第二种想法：实际上我们注意到分母中 $\theta(1-\theta)/n$ 是 $\bar{x}$ 也可以看作一种冗余参数，很自然的想法是我们用估计来代替。在样本量大的情形下， $\bar{x}$ 可以近似 $\theta$ ，所以

$$
\frac{\theta(1-\theta)}{n} \approx \frac{\bar{x}(1-\bar{x})}{n}.
$$

这样可以很容易反解出 $\theta$ ，从而得到 $\theta$ 的 $1-\alpha$ 置信区间

$$
\left [ \bar{x}-z_{1-\frac{\alpha }{2} }\sqrt{\frac{\bar{x}(1-\bar{x})}{n} } ,\bar{x}+z_{1-\frac{\alpha }{2} }\sqrt{\frac{\bar{x}(1-\bar{x})}{n} } \right ] .
$$

`````

`````{prf:example}
现有两个独立总体 $N(\mu_1,\sigma_1^2)$ 和 $N(\mu_2,\sigma_2^2)$ 。设 $x_1,x_2,\cdots,x_m$ 是来自 $N(\mu_1,\sigma_1^2)$ 的样本，而 $y_1,y_2,\cdots,y_n$ 是来自 $N(\mu_2,\sigma_2^2)$ 的样本。
考虑不同 $\theta$ 以及它们的 $1-\alpha$ 置信区间。

- $\theta = \mu_1 - \mu_2$ 。

- 若 $\sigma_1^2$ 和 $\sigma_2^2$ 已知。由于 $\theta$ 的点估计为
$
\hat{\theta} = \bar{x} - \bar{y}
$
其分布为

$$
\hat{\theta} = \bar{x} - \bar{y} \sim N\left(\theta, \frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n}\right).
$$

于是，枢轴量为

$$
G = \frac{\hat{\theta} - \theta}{ \sqrt{\frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n}}} \sim N(0,1).
$$

所以， $\theta$ 的 $1-\alpha$ 置信区间为

$$
\left[
(\bar{x}-\bar{y}) - \sqrt{\frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n}} z_{1-\alpha},
(\bar{x}-\bar{y}) + \sqrt{\frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n}} z_{1-\alpha}
\right]
$$

- 若 $\sigma_1^2= \sigma_2^2 = \sigma^2$ 未知。令

$$
s_w^2 = \frac{(m-1)s_1^2 + (n-1)s_2^2}{m+n-2}.
$$

则 $(m+n-2)s_w^2 / \sigma^2$ 的分布为 $\chi^2(m+n-2)$ 。
于是，我们可以构造枢轴量

$$
\frac{\hat{\theta} -\theta }{s_w\sqrt{\frac{1}{m}+\frac{1}{n}} } \sim t(m+n-2)
$$

所以， $\theta$ 的 $1-\alpha$ 置信区间为

$$
\bar{x}-\bar{y} \pm s_w\sqrt{\frac{1}{m}+\frac{1}{n}} t_{1-\alpha/2}(m+n-2)
$$

- $\theta = \sigma_1^2/\sigma_2^2$ 。我们考虑 $\theta$ 的点估计为 $s_1^2/s_2^2$ ，则

$$
\frac{s_1^2}{s_2^2}/\theta \sim F(m-1,n-1).
$$

所以， $\theta$ 的 $1-\alpha$ 置信区间为

$$
\left[
\frac{s_1^2}{s_2^2}/ F_{1-\alpha/2}(m-1,n-1),
\frac{s_1^2}{s_2^2}/ F_{\alpha/2}(m-1,n-1)
\right].
$$

`````