# 独立同分布下的中心极限定理

``````{prf:theorem} 林德伯格-莱维（Lindeberg-Levy）中心极限定理
设 $\{X_n\}$ 是独立同分布的随机变量序列，且 $E(X_i)=\mu,\text{Var}(X_i) = \sigma^2>0$ 存在，若记

$$
S_n^{\ast} = \frac{\sum_{i=1}^n X_i - n \mu}{\sigma \sqrt{n}},
$$

则对任意实数 $y$ ，有

$$
\lim_{n\rightarrow \infty} P(S_n^{\ast} \leq s) = \Phi(s)
$$

``````

```{admonition} Remark

- 这个定理的证明需要利用特征函数，学生可以参考《概率论与数理统计教程》第 212 页。
- 林德伯格-莱维中心极限定理表示独立同分布，且二阶矩存在的随机变量序列是满足中心极限定理。

```

以下，我们讨论一种特定的分布——二项分布。

``````{prf:theorem} 棣莫弗-拉普拉斯（de Moivre-Laplace）中心极限定理
设 $n$ 重伯努利实验中，事件 $A$ 在每次实验中出现的概率为 $p(0<p<1)$ ，记 $S_n$ 为 $n$ 次实验中实验 $A$ 出现的次数，且记

$$
S_n^{\ast} = \frac{S_n - np}{\sqrt{np(1-p)}}
$$

则对任意实数 $y$ ，有

$$
\lim_{n\rightarrow \infty} P(S_n^{\ast} \leq s) = \Phi(s).
$$

``````

```{admonition} Remark

对于棣莫弗-拉普拉斯（de Moivre-Laplace）中心极限定理，我们具体讨论一下。

- 二项分布的近似分布，可以采用泊松分布，也可以使用正态分布。一般来说，在 $p$ 比较小时，用泊松分布近似较好；而在 $np>5$ 和 $n(1-p)>5$ 时，用正态分布比较好。
- 因为二项分布是离散分布，而正态分布是连续分布，在近似时通常可以做一些修正来提高精度。对任意 $s_1<s_2$ ， $P(s_1 \leq S_n \leq s_2)$ 的修正方案为

$$
P(s_1-0.5 \leq S_n \leq s_2+0.5) = \Phi\left(\frac{s_2+0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{s_1 - 0.5 - np}{\sqrt{np(1-p)}}\right).
$$

`````{prf:example}
若 $S_n \sim b(25,0.4)$ ，那么 $P(5\leq S_n \leq 15) = 0.9774$ 。我们可以计算

$$
\begin{eqnarray*}
\text{修正后：}P(5\leq S_n \leq 15) &=& \Phi\left(\frac{15+0.5 - 10}{\sqrt{25\times 0.4\times 0.6}}\right) -\Phi\left(\frac{5-0.5 - 10}{\sqrt{25\times 0.4\times0.6}}\right) = 0.9753,\\
\text{未修正：}P(5\leq S_n \leq 15) &=& \Phi\left(\frac{15 - 10}{\sqrt{25\times 0.4\times 0.6}}\right) -\Phi\left(\frac{5 - 10}{\sqrt{25\times 0.4\times 0.6}}\right) = 0.9588.
\end{eqnarray*}
$$

`````

同时，这种修正方案也可以适用于计算 $P(S_n = k)$ 的情况。

`````{prf:example}
若 $S_n \sim b(25,0.4)$ ，那么 $P(S_n = 10) = 0.1612$ 。根据修正方案，我们可以计算

$$
\Phi\left(\frac{10+0.5 - 10}{\sqrt{25\times 0.4\times 0.6}}\right) -\Phi\left(\frac{10-0.5 - 10}{\sqrt{25\times 0.4\times 0.6}}\right) = 0.1617.
$$

`````