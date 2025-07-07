# 习题

- 设 $\hat{\theta}$ 是参数 $\theta$ 的无偏估计，且有 $\text{Var}(\hat{\theta})>0$ ，试证 $\left(\hat{\theta}\right)^2$ 不是 $\theta^2$ 的无偏估计。
- 设 $x_1,x_2,\cdots,x_n$ 是来自于下列总体的简单样本

$$
p(x;\theta) = \left\{
\begin{aligned}
& 1, &\theta - \frac{1}{2} \leq x\leq \theta + \frac{1}{2},\\
& 0, &\text{其他},
\end{aligned}\right.
$$

证明样本均值 $\bar{x}$ 及 $\frac{1}{2}(x_{(1)}+x_{(n)})$ 都是 $\theta$ 的无偏估计，问哪一个更为有效？（提示：从充分性原则来具体分析一下这个结论。）
- 设从均值为 $\mu$ ，方差为 $\sigma^2>0$ 的总体中分布抽取容量为 $n_1$ 和 $n_2$ 的两独立样本， $\bar{x}_1$ 和 $\bar{x}_2$ 是这两个样本的均值。试证，对于任意常数 $a,b (a+b=1)$ ， $Y = a\bar{x}_1 + b\bar{x}_2$ 都是 $\mu$ 的无偏估计，并确定常数 $a,b$ 使得 $\text{Var}(Y)$ 达到最小。
- 设总体密度函数为

$$p(x;\theta) = \theta x^{\theta - 1}, 0<x<1,\theta > 0.$$

 $x_1,x_2,\cdots,x_n$ 是样本。求 $g(\theta) = 1/\theta$ 的最大似然估计。
- 设总体 $X\sim Exp(1/\theta)$ , $x_1,x_2,\cdots,x_n$ 是样本。

- 验证 $\theta$ 的矩估计和最大似然估计都是 $\bar{x}$ ；
- 验证 $\bar{x}$ 也是 $\theta$ 的相合估计和无偏估计；
- 试证明在均方误差准则下存在优于 $\bar{x}$ 的估计。（提示：考虑 $\hat{\theta}_n = a \bar{x}$ ，找均方误差最小者）

- 设 $x_1,x_2,\cdots,x_n$ 是来自密度函数为

$$
p(x;\theta) = e^{-(x-\theta)},
x>\theta
$$

的总体的样本。

- 求 $\theta$ 的最大似然估计 $\hat{\theta}_1$ , 它是否是相合估计？是否是无偏估计？
- 求 $\theta$ 的矩估计 $\hat{\theta}_2$ ，它是否是相合估计？它是否是无偏估计？