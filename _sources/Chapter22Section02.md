# 假设检验的基本概念
这里我们先给出假设检验的一些基础概念。

假设
: 设有来自某一个参数分布族 $\{F(x,\theta)|\theta \in \Theta\}$ 的样本 $x_1,x_2,\cdots,x_n$ ，其中 $\Theta$ 为参数空间。设 $\Theta_0 \subset \Theta$ 且 $\Theta_0 \neq \emptyset$ 。则称命题

$$
H_0 : \theta \in \Theta_0
$$

为一个假设，或原假设，或零假设（null hypothesis）。

对立假设或备择假设
: 若有另一个 $\Theta_1 (\Theta_1 \subset \Theta, \Theta_1 \cap \Theta_0 = \emptyset)$ ，则称命题

$$
H_1 : \theta \in \Theta_1
$$

为 $H_0$ 的对立假设或备择假设（alternative hypothesis）。于是，我们感兴趣的一对假设就是

$$
H_0: \theta \in \Theta_0 \quad \text{vs} \quad H_1: \theta \in \Theta_1
$$

其中，vs 是 versus 的缩写，即表示 $H_0$ 对 $H_1$ 的假设检验问题。

```{admonition} Remark

- $\Theta_1$ 的常见一种情况是 $\Theta_1 = \Theta-\Theta_0$ ；
- 如果 $\Theta_0$ 仅包含一个点，则称其为简单（simple）原假设；否则称为复杂（composite）或复合原假设。备择假设也会有简单和复杂的差别。
- 当原假设为简单原假设，即 $H_0:\theta = \theta_0$ ，此时，备择假设通常有三种：

- $H_1^{'}: \theta \neq \theta_0$ ；
- $H_1^{''}: \theta < \theta_0$ ；
- $H_1^{'''}: \theta > \theta_0$ ；

称 $H_0 \ \text{vs} \ H_1^{'}$ 为双侧假设或双边假设；称 $H_0 \ \text{vs} \ H_1^{''}$ 或 $H_0 \ \text{vs} \ H_1^{'''}$ 为单侧假设或单边假设。

```

`````{prf:example}
在女士品茶的例子中，我们提出的假设为

$$
H_0: p = 0.5 \quad \text{vs} \quad H_1: p>0.5.
$$

原假设时简单的，备择假设是复杂的；而且这是一个单边假设检验问题。
`````

在提出一个假设检验问题（给出一对假设）之后，我们需要给出一个具体的判断规则，称这个判断规则为该假设的一个检验或者检验法则。

接受域
: 给定样本 $x_1,x_2,\cdots,x_n$ 。对于其样本空间 $\Omega$ ，我们可以确定一组划分

$$
W \cap \overline{W} = \emptyset, \quad W \cup \overline{W} = \Omega.
$$

当 $(x_1,x_2,\cdots,x_n) \in W$ 时，拒绝 $H_0$ ；否则接受 $H_0$ 。于是，称 $W$ 为该检验的拒绝域，而称 $\overline{W}$ 为接受域。

```{admonition} Remark
一旦拒绝域确定了，检验的判断准则也就确定了。
```

因为我们的检验是基于样本而确定的，所以，对于任何的检验而言，我们所作出的判断都可能犯错。检验有常见的两类错误，如表 {numref}`tab:lect22_1` 所示。

```{list-table} 检验的两种错误
:header-rows: 1
:name: tab:lect22_1
* - 
  -
  - $H_0$ 为真
  - $H_1$ 为真
* - 判断结果
  - 判 $H_0$ 为真
  - 正确
  - 犯第二类错误
* - 判断结果
  - 判 $H_1$ 为真
  - 犯第一类错误
  - 正确
```

同时，我们需要定义这两类错误发生概率，分别为

- 第一类错误发生的概率为 $\alpha(\theta) = P_{\theta}((x_1,x_2,\cdots,x_n)\in W),\theta \in \Theta_0$ .
- 第二类错误发生的概率为 $\beta(\theta) = P_{\theta}((x_1,x_2,\cdots,x_n)\in \overline{W}),\theta \in \Theta_1$ .

```{admonition} Remark
可以类比“无罪假定”，第一类错误也称为“错判”，而第二类错误也称为“漏判”。
```

```{admonition} Question
事实上，第一类错误发生概率和第二类错误发生概率无法同时降低，那么哪一种错误值得我们在意呢？
```

势函数
: 为统一地表示第一类错误发生的概率和第二类错误发生的概率，我们引入势函数或功效函数（power function）。

设检验问题

$$
H_0: \theta\in \Theta_0 \quad \text{vs} \quad H_1: \theta\in\Theta_1
$$

的拒绝域为 $W$ ，则样本 $(x_1,x_2,\cdots,x_n)$ 落在拒绝域 $W$ 内的概率称为该检验的势函数，记为

$$
g(\theta) = P_{\theta}((x_1,x_2,\cdots,x_n) \in W), \theta \in \Theta=\Theta_0 \cup \Theta_1.
$$

```{admonition} Remark
势函数

$$
g(\theta) = \left\{
\begin{aligned}
& \alpha(\theta), & \theta\in\Theta_0\\
& 1-\beta(\theta), & \theta\in\Theta_1\\
\end{aligned}
\right.
$$

```

`````{prf:example} 
:label: ex:chap22_one_sample_mean_z
设 $x_1,x_2,\cdots,x_n$ 是来自正态分布 $N(\mu,\sigma_0^2)$ 的样本，其中 $\sigma_0^2$ 是已知的。我们需要检验以下假设

$$
H_0: \mu = \mu_0 \quad \text{vs} \quad H_0: \mu > \mu_0. $$

在上述假设中，我们想要知道总体均值 $\mu$ 是否大于给定的值 $\mu_0$ 。因为样本均值 $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ 是总体均值 $\mu$ 的一个合理估计，所以我们需要依据样本均值来推断哪种假设更可能成立。以下有两种情况：

- 第一种情况： $\bar{x} \leq \mu_0$ ，于是，我们没有任何证据来支持备择假设。
- 第二种情况： $\bar{x} > \mu_0$ ，于是，我们能够直接下结论——支持备择假设吗？

在第二种情况下，我们仍无法直接接受备择假设。这是因为如果只是大一点，这可能是由于样本的随机性造成的。于是，我们需要考虑一个问题：样本均值 $\bar{x}$ 多大，才能接受备择假设。也就是说，我们构造一个拒绝域为

$$
\{\bar{x} \geq c\}
$$

其中， $c$ 指的是临界值，怎么来确定这个 $c$ 是另一个问题。
为了确定 $c$ ，我们需要计算第一类错误发生的概率，即

$$
\begin{eqnarray*}
P\left(\bar{x} > c |H_0\right) &= &P\left(\frac{\bar{x}-\mu_0}{\sqrt{\sigma_0^2/n}} > \frac{c-\mu_0}{\sqrt{\sigma_0^2/n}} |H_0\right) \\
&=& 1-\Phi\left(\frac{c-\mu}{\sqrt{\sigma_0^2/n}}\right)
\end{eqnarray*}
$$

其中第二个等式成立是因为 $\bar{x}\sim N(\mu,\sigma_0^2)$ 且在 $H_0$ 成立时， $\mu=\mu_0$ 。
记

$$
\alpha_{\mu_0}(c) = 1-\Phi\left(\frac{c-\mu_0}{\sqrt{\sigma_0^2/n}}\right).
$$

我们发现 $\alpha_{\mu_0}(c)$ 是关于 $c$ 的减函数。为控制住第一类错误率，我们事先给出一个很小的值 $\alpha>0$ ，这个值 $\alpha$ 被称为显著性水平，也就是说， $\alpha_{\mu_0}(c)\leq \alpha$ 。我们可以通过这个不等式将临界值 $c$ 反解出来，即

$$
c = \mu_0 + z_{1-\alpha} \sqrt{\sigma_0^2/n}.
$$

因此，我们所构造的拒绝域为

$$
\begin{eqnarray*}
W &=& \left\{(x_1,x_2,\cdots,x_n): \bar{x} \geq \mu_0 + z_{1-\alpha} \sqrt{\sigma_0^2/n}\right\} \\
&=& \left\{(x_1,x_2,\cdots,x_n): \frac{\bar{x}-\mu_0}{\sqrt{\sigma_0^2/n}} \geq z_{1-\alpha} \right\} .
\end{eqnarray*}
$$

`````

```{admonition} Remark
这个检验也被称为 $z$ 检验，其中

$$
z = \frac{\bar{x}-\mu_0}{\sqrt{\sigma_0^2/n}}
$$

是 $z$ 检验的检验统计量。
```

根据例 {prf:ref}`ex:chap22_one_sample_mean_z` ，我们进一步论证：第一类错误发生的概率 $\alpha(\mu)$ 和第二类错误发生的概率 $\beta(\mu)$ 是无法同时减小。

`````{prf:example} 例题续
因为我们所构造的拒绝域为

$$W = \{(x_1,x_2,\cdots,x_n): \bar{x} \geq c\} $$

所以接受域为

$$\overline{W} = \{(x_1,x_2,\cdots,x_n): \bar{x} < c\} .$$

于是，对于 $\mu > \mu_0$ ，第二类错误率为

$$
\begin{eqnarray*}
\beta_{\mu}(c) = P_{\mu}\left( \bar{x} < c|H_1\right)
= \Phi\left(\frac{c-\mu}{\sqrt{\sigma_0^2/n}}\right),
\end{eqnarray*}
$$

其中，在 $H_1$ 成立时， $\bar{x}\sim N(\mu,\sigma_0^2)$ 。
我们发现 $\beta_{\mu}(c)$ 是关于 $c$ 的增函数。由此，

- $\alpha_{\mu_0}(c)$ 减小 $\Rightarrow c$ 增加 $\Rightarrow \beta_{\mu}(c)$ 增加。
- $\beta_{\mu}(c)$ 减小 $\Rightarrow c$ 减小 $\Rightarrow \alpha_{\mu_0}(c)$ 增加。

综上，第一类错误发生的概率和第二类错误发生的概率不可同时减小。
`````

显著性检验
: 对检验问题

$$
H_0: \theta\in \Theta_0 \quad \text{vs} \quad H_1: \theta\in\Theta_1,
$$

如果一个检验满足对任意的 $\theta\in\Theta_0$ ，都有

$$
g(\theta) = \alpha(\theta) \leq \alpha
$$

则称该检验是显著性水平为 $\alpha$ 的显著性检验，简称水平为 $\alpha$ 的检验。