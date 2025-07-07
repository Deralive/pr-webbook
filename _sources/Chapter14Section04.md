# 其他条件下的中心极限定理
除了满足独立同分布的随机变量序列之外，其他类型的随机变量序列也可以满足中心极限定理。以下两个定理供学生课后自学。

林德伯格条件
: 假设一个随机变量序列 $\{X_n\}$ ，其期望 $E(X_i) = \mu_i$ 且方差 $\text{Var}(X_i)=\sigma_i^2$ ， $i=1,2,\cdots$ 。令 $S_n = \sum_{i=1}^n X_i$ ，且 $B_n = \sigma(S_n) = \sqrt{\text{Var}(S_n)}$ 。
如果对于任意 $\tau >0$ ，有

$$
\lim_{n\rightarrow \infty} \frac{1}{\tau^2 B_n} \sum_{i=1}^n \int_{|x-\mu_i| > \tau B_n} (x-\mu_i)^2 p_i(x)\text{d} x = 0.
$$

那么称该随机变量序列满足林德伯格条件。

```{admonition} Remark
林德伯格条件保证了 $S_n^{\ast} = B_n^{-1}\sum_{i=1}^n (X_i-\mu_i)$ 中各加项“均匀地小”。
```

此外，还有其他中心极限定理，供同学们补充学习。

``````{prf:theorem} 林德伯格中心极限定理
设独立随机变量序列 $\{X_n\}$ 满足林德伯格条件，则对任意的 $x$ ，有

$$
\lim_{n\rightarrow \infty} P\left(\frac{1}{B_n} \sum_{i=1}^n (X_i-\mu_i) \leq x\right)
= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x} e^{-t^2/2}\text{d}t.
$$

``````

``````{prf:theorem} 李雅普诺夫中心极限定理
设 $\{X_n\}$ 为独立随机变量序列，若存在 $\delta >0$ ，满足

$$
\lim_{n\rightarrow \infty} \frac{1}{B_{n}^{2+\delta}}\sum_{i=1}^n E\left( |X_i - \mu_i|^{2+\delta} \right) =0,
$$

则对任意的 $x$ ，有

$$
\lim_{n\rightarrow \infty} P\left(\frac{1}{B_n} \sum_{i=1}^n (X_i-\mu_i) \leq x\right)
= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x} e^{-t^2/2}\text{d}t.
$$

``````