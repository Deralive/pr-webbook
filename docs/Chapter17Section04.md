# 习题

- $x_1,x_2,\cdots,x_n$ 是来自 $N(\mu,1)$ 的样本，试确定最小的常数 $c$ 使得对任意的 $\mu\geq 0$ 有

$$P(|\bar{x}|< c) \leq \alpha. $$

- 设随机变量 $X \sim F(n,m)$ ，证明：

$$Z = \frac{\frac{n}{m}X}{(1+\frac{n}{m}X)}$$

服从贝塔分布，并指出其参数.
- 设 $x_1,x_2,\cdots,x_n$ 是来自 $N(\mu_1,\sigma^2)$ 的样本， $y_1,y_2,\cdots,y_m$ 是来自 $N(\mu_2,\sigma^2)$ 的样本， $c,d$ 是任意两个不为 $0$ 的常数，证明

$$
t = \frac{c(\bar{x} - \mu_1) + d(\bar{y} - \mu_2)}{s_w\sqrt{\frac{c^2}{n} + \frac{d^2}{m}}} \sim t(n+m-2)
$$

其中 $s_w^2 = \frac{(n-1)s_x^2 + (m-1)s_y^2}{n+m-2}$ 。