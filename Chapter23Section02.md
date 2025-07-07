# 似然比检验
似然比
: 设 $x_1,x_2,\cdots,x_n$ 为来自密度函数为 $p(x;\theta),\theta\in \Theta$ 的总体的样本，考虑如下检验问题：

$$
H_0: \theta \in \Theta_0 \quad \text{vs} \quad H_1: \theta \in \Theta_1 = \Theta- \Theta_0.
$$

令

$$
\Lambda_1(x_1,x_2,\cdots,x_n) = \frac{\sup_{\theta \in \Theta_1} p(x_1,x_2,\cdots,x_n;\theta)}{\sup_{\theta \in \Theta_0} p(x_1,x_2,\cdots,x_n;\theta)}
$$

和

$$
\Lambda(x_1,x_2,\cdots,x_n) = \frac{\sup_{\theta \in \Theta} p(x_1,x_2,\cdots,x_n;\theta)}{\sup_{\theta \in \Theta_0} p(x_1,x_2,\cdots,x_n;\theta)}
=\max\{\Lambda_1,1\}$$

则称统计量 $\Lambda_1(x_1,x_2,\cdots,x_n)$ 和 $\Lambda(x_1,x_2,\cdots,x_n)$ 为该假设的似然比（likelihood ratio）。

似然比检验
: 如果似然比统计量 $\Lambda(x_1,x_2,\cdots,x_n)$ 是假设检验问题

$$
H_0: \theta \in \Theta_0 \quad \text{vs} \quad H_1: \theta \in \Theta_1 = \Theta- \Theta_0
$$

的检验统计量，且取其拒绝域为 $W = \{\Lambda(x_1,x_2,\cdots,x_n)\geq c\}$ ，其中临界值 $c$ 满足

$$
P(\Lambda(x_1,x_2,\cdots,x_n)\geq c)\leq \alpha, \forall \theta \in \Theta_0,
$$

则称此检验为显著性水平 $\alpha$ 的似然比检验（likelihood ratio test），简称 LRT。

```{admonition} Question
对于两个似然比，什么时候该用 $\Lambda_1$ ，什么时候该用 $\Lambda$ ？
```{dropdown} Solution

一般来说， $\Lambda_1$ 用于分布类型的选择， $\Lambda$ 用于参数假设检验。
```


`````{prf:example} 分布类型选择类的假设检验问题
在研究轴承的寿命时，记轴承的寿命为 $T$ 。在美苏冷战时期，美国使用的分布时对数正态分布（logNormal），而苏联使用的是韦布尔分布（Weibull）。那么，对于中国所生产的轴承，其寿命应服从对数正态分布，还是应服从韦布尔分布？
`````

`````{prf:example}
设 $x_{1},\cdots,x_{n}$ 是来自正态总体 $N(\theta,\sigma _{0}^{2}),\sigma _{0}^{2}$ 的样本。检验问题为

$$
H_{0}: \theta=\theta_{0} \quad \text{vs} \quad H_{1}: \theta \neq \theta_{0} .$$

根据原假设和备择假设， $\Theta_0 = \{\theta_0\}$ ，而 $\Theta_1 = (-\infty,\theta_0)\cup (\theta_0,\infty)$ 。于是， $\Theta = (-\infty,\infty)$ 。
对于参数 $\theta$ 而言，其似然函数为

$$
l(\theta) = p(x_1,x_2,\cdots,x_n;\theta) = (2\pi \sigma_0^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\theta)^2\right\}.
$$

对于 $\theta \in \Theta_0$ ，

$$
\sup_{\theta\in \Theta_0} l(\theta) = l(\theta_0) = (2\pi \sigma_0^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\theta_0)^2\right\},
$$

而对于 $\theta \in \Theta$ ，

$$
\sup_{\theta\in \Theta} l(\theta) = l(\hat{\theta}_{\text{ML}}) = (2\pi \sigma_0^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\bar{x})^2\right\}.
$$

于是，似然比统计量为

$$
\begin{eqnarray*}
\Lambda &=& \frac{\sup_{\theta\in \Theta} l(\theta)}{\sup_{\theta\in \Theta_0} l(\theta)}\\
&=& \frac{ (2\pi \sigma_0^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\bar{x})^2\right\}}{ (2\pi \sigma_0^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\theta_0)^2\right\}}\\
&=& \frac{ \exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\bar{x})^2\right\}}{ \exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\theta_0)^2\right\}}\\
&=& \frac{ \exp\left\{-\frac{1}{2\sigma_0^2} \sum_{i=1}^n(x_i-\bar{x})^2\right\}}{ \exp\left\{-\frac{1}{2\sigma_0^2} \left(\sum_{i=1}^n(x_i-\bar{x})^2 + n(\bar{x} - \theta_0)^2\right)\right\}}\\
&=& \exp \left\{ \frac{n}{2\sigma_0^2} \left( \bar{x} - \theta_0 \right)^2\right\}
\end{eqnarray*}
$$

而 $z$ 检验统计量为

$$
z = \frac{\bar{x}-\theta_0}{\sqrt{\sigma_0^2/n}}.
$$

由此，似然比统计量 $\Lambda$ 是 $z$ 检验统计量的绝对值的严格递增函数。易知， $\{\Lambda \geq c_1\}$ 等价于 $\{|z|\geq c_2\}$ ，这里两个临界值 $c_1$ 和 $c_2$ 是根据显著性水平 $\alpha$ 来确定的。因此，此时的似然比检验与双侧 $z$ 检验完全等价。
`````

```{admonition} Remark
虽然难以求得似然比检验的精确分布，但是在一般条件下，其存在一个渐近分布，即 $-2\ln \Lambda$ 服从卡方分布，其自由度为其独立参数个数。
```