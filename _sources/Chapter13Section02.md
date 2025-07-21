# 伯努利大数定律
考虑抛硬币这个伯努利实验，记第 $i$ 次抛硬币的结果为 $X_{i}$ 。一般假定每次抛硬币的结果仅有两个：正面（感兴趣的）和反面（不感兴趣的）；而且每次的结果是相互独立的。正面朝上的概率记为 $p$ 。所以， $X_i$ 是服从伯努利分布或二点分布，即 $X_i\overset{iid}{\sim} b(1,p)$ ，即 $P(X_{i}=1)=p$ 。

于是，在 $n$ 次抛硬币的结果中，正面朝上的总次数为

$$S_{n}=\sum_{i=1}^{n}X_{i},$$

在 $n$ 次结果中，正面朝上的频率为

$$\frac{S_{n}}{n}=\frac{1}{n}\sum_{i=1}^{n} X_{i}.$$

根据二项分布的可加性，可知

$$S_{n}\sim b(n,p).$$

那么，

$$
\begin{eqnarray*}
E\left(\frac{S_{n}}{n}\right) &=& \frac{1}{n} E(S_{n})=\frac{1}{n}\cdot (np)=p, \\
\text{Var}\left(\frac{S_{n}}{n}\right) &=& \frac{1}{n^{2}}\text{Var}(S_{n})=\frac{1}{n^{2}}\cdot (np(1-p))=\frac{p(1-p)}{n} .
\end{eqnarray*}
$$

我们发现：

- 这个频率的期望是概率，意味着频率是在概率附近周围波动的；
- 频率的方差 $p(1-p)/n$ ，随着 $n$ 不断增大而快速减小的。

于是，一个很自然的问题：这个频率的“极限”是不是这个概率呢？由此，我们来看以下定理。

``````{prf:theorem} 伯努利大数定律
设 $S_{n}$ 为 $n$ 重伯努利试验中事件 $A$ 发生的次数， $p$ 为每次试验中 $A$ 出现的概率，则对任意的 $\varepsilon>0$ ，有

$$\lim_{n \to \infty} P\left( \left | \frac{S_{n}}{n}-p \right | < \varepsilon \right)=1.$$

```{dropdown} Proof
由于 $S_{n}\sim b(n,p)$ 且

$$E(\frac{S_{n}}{n})=p,\text{Var}(\frac{S_{n}}{n})=\frac{p(1-p)}{n}.$$

由切比雪夫不等式，可得

$$1\ge P \left( \left | \frac{S_{n}}{n}-p \right | < \varepsilon \right )\ge 1-\frac{\text{Var}(\frac{S_{n}}{n})}{\varepsilon ^{2}}=1-\frac{p(1-p)}{n\varepsilon ^{2}} \rightarrow 1 $$

因此

$$P\left( \left | \frac{S_{n}}{n}-p \right | < \varepsilon \right)\rightarrow 1.$$

```

```{admonition} Remark
:class: dropdown
随着 $n$ 的增大，事件 $A$ 发生的频率 $\frac{S_{n}}{n}$ 与其概率 $p$ 的偏差 $\left | \frac{S_{n}}{n}-p \right |$ 大于预先给定的精度 $\varepsilon$ 的可能性越来越小，这就是频率稳定于概率的含义。
```

``````
