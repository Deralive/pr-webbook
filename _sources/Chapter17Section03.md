# 正态分布下样本方差的分布
以下定理是本课程数理统计部分中最为重要的一个定理。对于这个定理，在本课程中，我们需要掌握该定理的应用，并不需要掌握证明过程，但是这个定理的证明过程是后续课程的基础。

`````{prf:theorem} 
:label: thm:lect16_normality

设 $x_{1},x_{2},\cdots,x_{n}$ 是来自正态总体 $N(\mu,\sigma ^{2})$ 的样本，其样本均值和样本方差分别为

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i \quad\text{和}\quad s^2 = \frac{1}{n-1}\sum_{i=1}^n(x_i- \bar{x})^2
$$

则有

- $\bar{x} \sim N\left(\mu, \frac{\sigma^{2}}{n}\right)$ ；
- $\frac{(n-1) s^{2}}{\sigma^{2}}=\frac{\sum\left(x_{i}-\bar{x}\right)^{2}}{\sigma^{2}} \sim \chi^{2}(n-1)$ ；
- $\bar{x}$ 与 $s^{2}$ 独立。

``````

```{admonition} Remark
在正态总体的假定下，这个定理阐述了三个结论。第一，样本均值 $\bar{x}$ 服从正态分布；第二，样本方差 $s^2$ 与卡方分布有关；第三，样本均值 $\bar{x}$ 和 $s^2$ 是相互独立的。
```

我们先来看看这个定理怎么用？我们先看两个例子，这两个例子也是这个定理的重要推论。

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自正态分布 $N(\mu,\sigma^2)$ 的一组样本， $\bar{x}$ 和 $s^2$ 分别是该样本的样本均值和样本方差，则有

$$
t = \frac{\sqrt{n}(\bar{x}-\mu)}{s} \sim t(n-1)
$$

```{dropdown} Solution

根据定理 {prf:ref}`thm:lect16_normality` ，我们可以知道，

$$
\frac{\bar{x}-\mu}{\sqrt{\sigma^2/n}}\sim N(0,1),\quad \text{且} \frac{(n-1)s^2}{\sigma^2} \sim \chi^2(n-1)
$$

而且这两者是相互独立的。所以,

$$
t = \frac{\sqrt{n}(\bar{x}-\mu)}{s} = \frac{\frac{\bar{x}-\mu}{\sqrt{\sigma^2/n}}}{\sqrt{\frac{(n-1)s^2}{\sigma^2}/(n-1)}} \sim t(n-1).
$$

```
`````

`````{prf:example}
设 $x_1,x_2,\cdots,x_m$ 是来自 $N(\mu_1,\sigma^2_1)$ 的样本， $y_1,y_2,\cdots,y_n$ 是来自 $N(\mu_2,\sigma^2_2)$ 的样本，且两样本相互独立，记

$$
s_1^2 = \frac{1}{m-1}\sum_{i=1}^m (x_i-\bar{x})^2 \quad \text{和}\quad
s_2^2 = \frac{1}{n-1}\sum_{i=1}^n (y_i-\bar{y})^2,
$$

其中， $\bar{x} = m^{-1}\sum_{i=1}^m x_i$ 和 $\bar{y}=n^{-1}\sum_{i=1}^n y_i$ ，则有

$$
F = \frac{s_1^2 / \sigma_1^2}{s_2^2 /\sigma_2^2} \sim F(m-1,n-1).
$$

特别地，当 $\sigma_1^2 = \sigma_2^2 =\sigma^2$ 时，并记

$$
s_w^2 = \frac{(m-1)s_1^2 + (n-1)s_2^2}{m+n -2} = \frac{\sum_{i=1}^m(x_i-\bar{x})^2 + \sum_{i=1}^n(y_i-\bar{y})^2}{m+n -2}
$$

则

$$
\frac{(\bar{x} -\bar{y}) - (\mu_1 - \mu_2)}{s_w \sqrt{\frac{1}{m} + \frac{1}{n}}} \sim t(m+n-2).
$$

```{dropdown} Solution

根据定理 {prf:ref}`thm:lect16_normality` ，我们知道

$$
\begin{eqnarray*}
\frac{(m-1) s_1^2}{\sigma_1^2} \sim \chi^2(m-1)\\
\frac{(n-1) s_2^2}{\sigma_2^2} \sim \chi^2(n-1)
\end{eqnarray*}
$$

因为两个样本是相互独立的，所以

$$
F = \frac{s_1^2/\sigma_1^2}{s_2^2/\sigma_2^2} = \frac{\frac{(m-1) s_1^2}{\sigma_1^2}/(m-1)}{\frac{(n-1) s_2^2}{\sigma_2^2}/(n-1)} \sim F(m-1,n-1).
$$

当 $\sigma_1^2=\sigma_2^2 =\sigma^2$ ，则 $s_1^2/s_2^2 \sim F(m-1,n-1)$ 。根据定理 {prf:ref}`thm:lect16_normality` ，我们知道

$$
(\bar{x}-\bar{y}) \sim N((\mu_1 - \mu_2),\sigma^2/m + \sigma^2/n)
$$

因为

$$
(m+n-2) s_w^2 = (m-1)s_1^2 + (n-1)s_2^2 = \sum_{i=1}^m(x_i-\bar{x})^2 + \sum_{i=1}^n(y_i-\bar{y})^2
$$

可以看作两个独立的卡方随机变量的和，所以其仍为卡方分布，即 $s_w^2 \sim \chi^2((m-1)+(n-1))$ 。且 $\bar{x} - \bar{y}$ 与 $s_w^2$ 是相互独立的。于是，

$$
\frac{(\bar{x} -\bar{y}) - (\mu_1 - \mu_2)}{s_w \sqrt{\frac{1}{m} + \frac{1}{n}}} = \frac{\frac{(\bar{x} -\bar{y}) - (\mu_1 - \mu_2)}{ \sqrt{\sigma^2\left(\frac{1}{m} + \frac{1}{n}\right)}} }{\sqrt{\frac{(m+n-2) s_w^2}{\sigma^2}/(m+n-2)}}
\sim t(m+n-2)$$

```
`````

接下来，我们给出定理 {prf:ref}`thm:lect16_normality` 的证明。整体证明思路与教材中的证明思路一致，这里需要用到一些数学知识，这里我们用引理的方式罗列一下。

`````{prf:lemma}
如果 $\mathbf{A}$ 是一个正交矩阵，则

- $\mathbf{A}$ 的逆矩阵等于其转置矩阵，即 $\mathbf{A}^{-1} = A'$ ；
- $\mathbf{A}$ 的行列式为 $\pm 1$ 。

```{dropdown} Proof
我们可以构建一个 $n$ 维随机向量

$$
\mathbf{x} = (x_1,x_2,\cdots,x_n)' \sim N(\mu \mathbf{1}_n,\sigma^2 \mathbf{I}_n),
$$

其中 $\mathbf{1}_n = (1,1,\cdots,1)'$ 一个 $n\times 1$ 向量，且元素均为 1； $\mathbf{I}_n$ 是单位矩阵，即其主对角线上的元素为 1，而非主对角线上的元素为 0。于是， $\mathbf{x} = (x_1,x_2,\cdots,x_n)'$ 的密度函数为

$$
p(\mathbf{x}) = (2\pi)^{-n/2} |\sigma^2\mathbf{I}_n|^{-1/2} \exp\left\{-\frac{1}{2} (\mathbf{x}-\mu \mathbf{1}_n)' (\sigma^2 \mathbf{I}_n)^{-1} (\mathbf{x}-\mu \mathbf{1}_n)\right\}.
$$

接下来，我们构造一个**特别**的正交矩阵 $A$ ，即

$$\mathbf{A}=\left(\begin{array}{ccccc}
\frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \cdots & \frac{1}{\sqrt{n}} \\
\frac{1}{\sqrt{2 \times 1}} & -\frac{1}{\sqrt{2 \times 1}} & 0 & \cdots & 0 \\
\frac{1}{\sqrt{3 \times 2}} & \frac{1}{\sqrt{3 \times 2}} & -\frac{2}{\sqrt{3 \times 2}} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{1}{\sqrt{n \times(n-1)}} & \frac{1}{\sqrt{n \times(n-1)}} &\frac{1}{\sqrt{n \times(n-1)}}& \cdots & -\frac{n-1}{\sqrt{n \times(n-1)}}
\end{array}\right)$$

并令

$$\mathbf{y} = \mathbf{A} \mathbf{x}.$$

构造 $A$ 的目的是为了将 $\bar{x}$ 和 $x_2-\bar{x},\cdots,x_n - \bar{x}$ 构成一些新的随机变量，从而可以通过变量变换法得到我们想要求的统计量的分布。这个 $A$ 的构造方法不为一，这里提供了一个相对容易的证明方案。基于矩阵 $\mathbf{A}$ ，我们发现

- $\frac{1}{\sqrt{n}} \sum_{i=1}^n x_i = y_1$ ，即 $\bar{x} = \frac{1}{\sqrt{n}}y_1$ ；
- $\sum_{i=1}^n y_i^2 = \mathbf{y}'\mathbf{y} = (\mathbf{A}\mathbf{x})'(\mathbf{A}\mathbf{x}) = \mathbf{x}'(\mathbf{A}'\mathbf{A})\mathbf{x} = \mathbf{x}'\mathbf{x} = \sum_{i=1}^n x_i^2$ 。

于是，

$$
\sum_{i=1}^n x_i^2= \sum_{i=1}^n y_i^2 = y_1^2 + \sum_{i=2}^n y_i^2 = n (\bar{x})^2 + \sum_{i=2}^n y_i^2，
$$

则

$$
\sum_{i=2}^n y_i^2 = \sum_{i=1}^n x_i^2 - n(\bar{x})^2 = \sum_{i=1}^n (x_i -\bar{x})^2 = (n-1) s^2.
$$

所以， $\mathbf{y}=(y_1,y_2,\cdots,y_n)'$ 的密度函数为

$$
\begin{eqnarray*}
p(\mathbf{y}) &=& (2\pi)^{-n/2} |\sigma^2 \mathbf{I}_n|^{-1/2} \exp\left\{-\frac{1}{2} (\mathbf{A}^{-1}\mathbf{y}-\mu \mathbf{1}_n)' (\sigma^2 \mathbf{I}_n)^{-1} (\mathbf{A}^{-1}\mathbf{y}-\mu \mathbf{1}_n)\right\} \cdot ||\mathbf{A}||\\
&=& (2\pi)^{-n/2} |\sigma^2 \mathbf{I}_n|^{-1/(2\sigma^2)} \exp\left\{-\frac{1}{2} (\mathbf{y}- \mathbf{A}\mu \mathbf{1}_n)' \mathbf{A} ( \mathbf{I}_n)^{-1} \mathbf{A}'(\mathbf{y}-\mathbf{A}\mu \mathbf{1}_n)\right\}\\
&=& (2\pi)^{-n/2} |\sigma^2 \mathbf{I}_n|^{-1/(2\sigma^2)} \exp\left\{-\frac{1}{2} (\mathbf{y}- \mu\mathbf{A} \mathbf{1}_n)' (\mathbf{A}\mathbf{A}')^{-1}(\mathbf{y}- \mu \mathbf{A} \mathbf{1}_n)\right\}
\end{eqnarray*}
$$

这表明了 $\mathbf{y}$ 仍服从 $n$ 维正态分布，其均值向量为 $\mu\mathbf{A} \mathbf{1}_n$ ，而方差-协方差矩阵为 $\sigma^2 \mathbf{A}\mathbf{A}'$ 。
这里我们具体地讨论一下均值向量

$$
\mathbf{A}\cdot \mu \mathbf{1}_n = \mu \mathbf{A}\mathbf{1}_n = \begin{pmatrix}
\sqrt{n}\mu\\0\\\vdots\\0
\end{pmatrix}
$$

而方差-协方差矩阵为

$$
\sigma^2 \mathbf{A}\mathbf{A}'= \sigma^2 \mathbf{I}_n = \begin{pmatrix}
\sigma^2 & 0 & 0 & \cdots & 0 \\
0& \sigma^2 & 0 & \cdots & 0 \\
0& 0 &\sigma^2 & \cdots & 0 \\
\vdots & \vdots & \vdots &&\vdots\\
0& 0 & 0 & \cdots &\sigma^2
\end{pmatrix}
$$

这表明了 $\mathbf{y}=(y_1,y_2,\cdots,y_n)'$ 中每个随机变量均是独立的，且 $y_1\sim N(\sqrt{n}\mu,\sigma^2)$ ，而剩余的每一个分量 $y_i^2 \sim N(0,\sigma^2),i=2,3,\cdots,n$ 。
所以，样本均值

$$
\bar{x} = \frac{1}{\sqrt{n}} y_1 \sim N(\mu,\sigma^2),
$$

而样本方差

$$
\frac{(n-1)s^2}{\sigma^2} = \frac{\sum_{i=2}^n y_i^2}{\sigma^2} \sim \chi^2(n-1),
$$

同时， $\bar{x}$ 仅由 $y_1$ 构造而得， $s^2$ 由 $y_2,\cdots,y_n$ 构造而得，于是， $\bar{x}$ 和 $s^2$ 是独立的。
```
`````

````{admonition} Remark
表 {numref}`tab_lect16_1` 中列出了在正态总体下常见统计量的抽样分布及其分位数的记号。
```{list-table} 几种抽样分布及其分位数
:header-rows: 1
:name: tab_lect16_1

* - 分布
  - $\alpha$ 分位数
* - $N(0,1)$
  - $z_{\alpha}$
* - $\chi^2(n)$
  - $\chi_{\alpha}^2(n)$
* - $F(m,n)$
  - $F_{\alpha}(m,n)$
* - $t(n)$
  - $t_{\alpha}(n)$
```
````