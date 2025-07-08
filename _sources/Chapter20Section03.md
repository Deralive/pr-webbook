# 大样本的评估方式 1——相合性
相合性是参数估计的必要条件。
[相合估计]
设 $\theta \in \theta$ 为未知参数， $\hat{\theta}_{n}=\hat{\theta}_{n}\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 是 $\theta$ 的一个估计， $n$ 为样本容量。若对任何一个 $\varepsilon>0$ ，有

$$\lim _{n \rightarrow \infty} P\left(\left|\hat{\theta}_{n}-\theta\right| \geqslant \varepsilon\right)=0 $$

则称 $\hat{\theta}_{n}$ 为参数 $\theta$ 的相合估计。

```{admonition} Remark
相合性的本质是 $\hat{\theta}_{n}$ 依概率收敛于 $\boldsymbol{\theta}$ 。
```

`````{prf:example}
设 $x_1,x_2,\cdots$ 是来自正态总体 $N(\mu,\sigma^2)$ 的样本序列。由中心极限定理（CLT）可知，

- $\bar{x}$ 是 $\mu$ 的相合估计；
- $s_{n}^{2}$ 是 $\sigma^{2}$ 的相合估计；
- $s^{2}$ 是 $\sigma^{2}$ 的相合估计。

`````

``````{prf:theorem}
设 $\hat{\theta}_n = \hat{\theta}_n (x_1,x_2,\cdots,x_n)$ 是 $\theta$ 的一个估计，若

$$
\lim_{n\rightarrow \infty} E(\hat{\theta}_n) = \theta,\quad \lim_{n\rightarrow \infty} \text{Var}(\hat{\theta}_n) = 0.
$$

则 $\hat{\theta}$ 是 $\theta$ 的相合估计。
```{dropdown} Proof
我们考虑事件

$$
\left\{ |\hat{\theta}_n - \theta| \geq \varepsilon \right\}
$$

其中，

$$
\hat{\theta}_n - \theta = \left(\hat{\theta}_n - E(\hat{\theta}_n) \right) + \left( E(\hat{\theta}_n) - \theta\right).
$$

于是，

$$
|\hat{\theta}_n - \theta| \leq \left|\hat{\theta}_n - E(\hat{\theta}_n) \right| + \left| E(\hat{\theta}_n) - \theta\right|.
$$

如果 $\left|\hat{\theta}_n - E(\hat{\theta}_n) \right| < \varepsilon/2$ 且 $\left| E(\hat{\theta}_n) - \theta\right|< \varepsilon/2$ ，那么 $\left|\hat{\theta}_n - \theta\right| <\varepsilon$ 。考虑其逆否命题，如果
$
\left|\hat{\theta}_n - \theta\right| \geq \varepsilon,
$
那么

$$\left\{\left|\hat{\theta}_n - E(\hat{\theta}_n) \right| \geq \varepsilon/2 \right\} \cup \left\{\left| E(\hat{\theta}_n) - \theta\right|\geq \varepsilon/2\right\}.
$$

于是，当 $n\rightarrow \infty$ 时，

$$
\begin{eqnarray*}
P\left( |\hat{\theta}_n - \theta| \geq \varepsilon \right) &\leq& P\left( \left|\hat{\theta}_n - E(\hat{\theta}_n) \right| \geq \varepsilon/2 \right) + P\left( \left| E(\hat{\theta}_n) - \theta\right|\geq \varepsilon/2 \right)\\
&\leq & \frac{4}{\varepsilon^2} \text{Var}(\hat{\theta}_n) + 0 \rightarrow 0
\end{eqnarray*}
$$

其中，第二个不等式满足因为切比雪夫不等式，即对任意的 $\varepsilon >0$ ，有

$$
P\left( |\hat{\theta}_n - E(\hat{\theta}_n)| \geq \frac{\varepsilon}{2} \right)\leq \frac{4}{\varepsilon^2} \text{Var}(\hat{\theta}_n).
$$

因此， $\hat{\theta}_n$ 是 $\theta$ 的相合估计。
```
``````

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自于均匀总体 $U(0,\theta)$ 的样本。接下来我们考虑 $\theta$ 的估计 $\hat{\theta}_1 = x_{(n)}$ 。因为 $x_{(n)} \sim Be(n,1)$ ，所以，当 $n\rightarrow \infty$ 时，

$$
\begin{eqnarray*}
E(\hat{\theta}_1) &=& \frac{n}{n+1}\theta \rightarrow \theta \\
\text{Var}(\hat{\theta}_1) &=& \frac{n}{(n+1)^2 (n+2)}\theta \rightarrow 0.
\end{eqnarray*}
$$

由此可证， $x_{(n)}$ 是 $\theta$ 的相合估计。
`````

``````{prf:theorem}
若 $\hat{\theta}_{n1},\hat{\theta}_{n2},\cdots,\hat{\theta}_{nk}$ 分别是 $\theta_1,\theta_2,\cdots,\theta_k$ 的相合估计， $\eta = g(\theta_1,\theta_2,\cdots,\theta_k)$ 是 $\theta_1,\theta_2,\cdots,\theta_k$ 的连续函数，则 $\hat{\eta}_n =g(\hat{\theta}_{n1},\hat{\theta}_{n2},\cdots,\hat{\theta}_{nk})$ 是 $\eta$ 的相合估计。
```{dropdown} Proof
由函数 $g$ 的连续性，对任意给定的 $\varepsilon > 0$ ，存在一个 $\delta>0$ ，当 $|\hat{\theta}_{nj}-\theta_j|< \delta,j=1,2,\cdots,k$ 时，有

$$
\left| g(\hat{\theta}_{n1},\hat{\theta}_{n2},\cdots,\hat{\theta}_{nk})-g(\theta_{1},\theta_2,\cdots,\theta_{k}) \right| < \varepsilon
$$

又由 $\hat{\theta}_{n1},\hat{\theta}_{n2},\cdots,\hat{\theta}_{nk}$ 的相合性，对给定的 $\delta>0$ ，对任意给定的 $\nu>0$ ，存在正整数 $N$ ，使得 $n\geq N$ 时，

$$
P\left( \left| \hat{\theta}_{nj} - \theta_j \right| \geq \delta \right) < \nu /k, kj=1,2,\cdots,k.
$$

从而有

$$
\begin{eqnarray*}
P\left( \cap_{j=1}^k \left\{\left| \hat{\theta}_{nj} - \theta_j \right| <\delta\right\} \right) &=& 1 - P\left( \cup_{j=1}^k \left\{ \left| \hat{\theta}_{nj} - \theta_j \right| \geq \delta \right\}\right)\\
&\geq & 1 - \sum_{j=1}^k P\left( \left| \hat{\theta}_{nj} - \theta_j \right| \geq \delta \right)\\
&> & 1- k \cdot \nu /k = 1-\nu.
\end{eqnarray*}
$$

于是，

$$
\cap_{j=1}^k \left\{\left| \hat{\theta}_{nj} - \theta_j \right| <\delta\right\} \subset \left\{ |\hat{\eta}_n - \eta|< \varepsilon \right\}
$$

所以，

$$
P(|\hat{\eta}_n - \eta|< \varepsilon ) > 1-\nu.
$$

由 $\nu$ 的任意性，定理得证。
```
``````

```{admonition} Remark
矩估计和最大似然估计均具有相合性。
```