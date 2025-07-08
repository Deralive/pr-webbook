# 大数定律的一般形式

我们从另一个视角看一下伯努利大数定律，所谓的频率是

$$
\frac{S_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i
$$

而所谓的概率是

$$
p = E\left( \frac{1}{n} \sum_{i=1}^n X_i\right) =\frac{1}{n} \sum_{i=1}^n E(X_i).
$$

伯努利大数定律表明了对于 $\{X_n\}$ 这个随机变量序列，如果 $X_i$ 是服从伯努利分布 $b(1,p)$ ，且每个随机变量是相互独立，那么对任意 $\varepsilon>0$ ，都有

$$
\lim_{n\rightarrow \infty} P\left( \left| \frac{1}{n} \sum_{i=1}^n X_i - \frac{1}{n} \sum_{i=1}^n E(X_i)\right| >\varepsilon \right) =1.
$$

注意到的是，伯努利大数定律给了一个**很强**的条件——不仅约束了随机变量序列中每一个随机变量的分布类型，还约束了随机变量序列中每一个随机变量之间都是相互独立的。于是，我们可以给出以下这个定义。

弱大数定律
: 设有一随机变量序列 $\{X_{n}\}$ ，如果其具有形如

$$P\left( \left | \frac{1}{n}\sum_{i=1}^{n}X_{i}-\frac{1}{n}\sum_{i=1}^{n}E(X_{i}) \right | < \varepsilon \right)\rightarrow 1$$

的性质，则称该随机变量序列 ${X_{n}}$ 服从（弱）大数定律。

我们自然有下面的一个问题：

```{admonition} Question
是否只有满足伯努利大数定律的条件，随机变量序列才能满足大数定律？
```