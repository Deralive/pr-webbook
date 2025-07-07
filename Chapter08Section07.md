# 常见的多维随机变量的分布
## 多项分布

进行 $n$ 次独立重复实验，如果每次实验有 $r$ 个互不相容的结果： $A_1,A_2,\cdots,A_r$ 之一发生，且每次是试验中 $A_i$ 发生的概率为 $p_i = P(A_i),i=1,2,\cdots,r$ ，且 $p_{1}+p_{2}+ \cdots +p_{r}=1$ 。记 $X_{i}$ 为 $n$ 次独立重复试验中 $A_{i}$ 出现的次数， $i=1,2, \cdots ,r$ ，则 $(X_{1}, X_{2}, \cdots, X_{r})$ 取值 $(x_{1}, x_{2}, \cdots, x_{r})$ 的概率，即 $A_{1}$ 出现 $x_{1}$ 次， $A_{2}$ 出现 $x_{2}$ 次, $\cdots$ , $A_{r}$ 出现 $x_{r}$ 的概率为

$$P\left(X_{1}=x_{1}, X_{2}=x_{2}, \cdots, X_{r}=x_{r}\right)=\frac{n!}{x_{1} ! x_{2} !\cdots x_{r} !} p_{1}^{x_{1}} p_{2}^{x_{2}} \ldots p_{r}^{x_{r}}$$

其中 $n=n_{1}+n_{2}+ \cdots +n_{r}$ 。
称这个联合分布列为多项分布,又称为 $r$ 项分布。记 $M(n,p_{1}, p_{2}, \cdots, p_{r})$ 。

```{admonition} Remark

- 典型例子：投掷 $r$ 面骰子。
- 当 $r=2$ 时，即为二项分布。
- $r$ 项分布是 $r-1$ 维随机变量的分布。

```

接下来，我们用一个例子来讨论多项分布与二项分布之间的关系。

`````{prf:example}
考虑三项分布 $M(n,p_{1}, p_{2}, p_{3})$ 实质上是一个二维随机变量 $(X,Y)$ 的分布，其联合分布为

$$
P(X=i, Y=j)=\frac{n !}{i ! j !(n-i-j) !} p_{1}^{i} p_{2}^{j}\left(1-p_{1}-p_{2}\right)^{n-i-j},
\left\{\begin{aligned}
&i, j=0,1, \cdots, n \\
&i+j \leq n
\end{aligned}
\right.
$$

于是， $X$ 的边际分布为

$$
\begin{eqnarray*}
P(X=i) &=&\sum_{j=0}^{n-i} \frac{n !}{i ! j !(n-i-j) !} p_{1}^{i} p_{2}^{j}\left(1-p_{1}-p_{2})^{n-i-j}\right.\\
&=&\frac{n !}{i !(n-i) !} p_{1}^{i}\left(1-p_{1}\right)^{n-i}
\sum_{j=0}^{n-i} \frac{(n-i) !}{j !(n-i-j) !} \frac{p_{2}^{j}\left(1-p_{1}-p_{2}\right)^{n-i-j}}{\left(1-p_{1}\right)^{n-i}} \\
&=&\frac{n !}{i !(n-i) !} p_{1}^{i}\left(1-p_{1}\right)^{n-i} \sum_{j=0}^{n-i} \frac{(n-i) !}{j !(n-i-j) !} (p_{2}^{\ast})^{ j}\left(1-p_{2}^{\ast}\right)^{n-i-j} \\
&=&\frac{n !}{i !(n-i) !} p_{1}^{i}\left(1-p_{1}\right)^{n-i},
\end{eqnarray*}
$$

其中， $p_{2}^{\ast}=\frac{p_{2}}{1-p_{1}}$ 。因此， $X \sim b\left(n, p_{1}\right)$ 。
`````

```{admonition} Remark

- 三项分布的一维边际分布为二项分布；
- 多项分布的一维边际分布为二项分布；

```

## 多维超几何分布

袋中有 $N$ 个球，其中有 $N_i$ 个 $i$ 号球， $i=1,2,\cdots,r$ ，且 $N = N_1+N_2 + \cdots + N_r$ . 从中任意取出 $n(n\leq N)$ 个，若记 $X_i$ 为取出的 $n$ 个球中 $i$ 号球的个数， $i=1,2,\cdots,r$ ，则

$$
P(X_1=n_1,X_2=n_2,\cdots,X_r= n_r) = \frac{\begin{pmatrix}
N_1\\n_1
\end{pmatrix}\begin{pmatrix}
N_2\\n_2
\end{pmatrix}\cdots\begin{pmatrix}
N_r\\n_r
\end{pmatrix}}{\begin{pmatrix}
N\\n
\end{pmatrix}}
$$

其中 $n_1+n_2+\cdots+n_r = n,n_i\leq N_i,i=1,2,\cdots,r$ 。称这个联合分布列为多项超几何分布。

```{admonition} Remark

- 当 $r=2$ 时，我们可以只考虑 $X_1$ 或 $X_2$ ，这是因为 $X_1+X_2=n$ 。此时的分布列就是（一维）超几何分布。
- 当 $r\geq 2$ 时，多维超几何分布也是 $r-1$ 维随机变量的分布。

```

## 多维均匀分布

设 $D$ 为 $R^n$ 中的一个有界区域，其度量为 $S_D$ 。如果多维随机变量 $(X_{1}, X_{2}, \cdots, X_{n})'$ 的联合密度函数为

$$p\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\left\{
\begin{aligned}
&\frac{1}{S_{D}}, & \left(x_{1}, x_{2}, \cdots, x_{n}\right) \in D \\
&0, & \text { 其他 }
\end{aligned}
\right.$$

则称 $X_{1}, X_{2}, \cdots, X_{n}$ 服从 $D$ 上的多维均匀分布，记为 $X_{1}, X_{2}, \cdots, X_{n}\sim U(D)$ 。

```{admonition} Remark
二维均匀分布所描述的随机现象就是向平面区域 $D$ 中随机投点。
如果该点坐标 $(X,Y)$ 落在 $D$ 的子区域 $G$ 中概率只与 $G$ 的面积有关，而与 $G$ 的位置无关，则

$$P((X, Y) \in G)=\iint_{G} p(x, y) d x d y=\iint_{G} \frac{1}{S_{D}} d x d y=\frac{S_{G}}{S_{D}}$$

```

## 多维正态分布

若 $\mathbf{X}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)'$ 为一个 $n$ 维随机变量，其密度函数为

$$p\left(x_{1}, x_{2}, \cdots, x_{n}\right)=p(\mathbf{x})=(2 \pi)^{-\frac{n}{2}}|\Sigma|^{-\frac{1}{2}} \exp \left\{-\frac{1}{2}(\mathbf{x}-\mathbf{\mu})' \Sigma^{-1}(\mathbf{x}-\mathbf{\mu})\right\}$$

称 $\mathbf{X}$ 满足 $n$ 元正态分布，记 $X \sim N_{n}(\mathbf{\mu}, \Sigma)$ 。

```{admonition} Remark

- 当 $n=1$ 时， $\mathbf{\mu} = \mu_1$ ， $\Sigma = \sigma_1^2$ ，一元正态分布的密度函数为

$$
p(x) = (2\pi \sigma_1^2)^{-1/2} \exp\left\{
-\frac{1}{2\sigma_1^2} (x_1-\mu_1)^2
\right\}
$$

- 当 $n=2$ 时， $\mathbf{\mu} = (\mu_1,\mu_2)'$ 且

$$
\Sigma = \begin{pmatrix}
\sigma_1^2 & \rho \sigma_1\sigma_2\\
\rho \sigma_1\sigma_2 & \sigma_2^2
\end{pmatrix}
$$

所以， $\Sigma$ 的行列式为

$$
|\Sigma| = \sigma_1^2\sigma_2^2 - (\rho \sigma_1\sigma_2)^2 = (1-\rho^2) \sigma_1^2\sigma_2^2
$$

而它的逆矩阵为

$$
\begin{eqnarray*}
\Sigma^{-1} &=& \frac{1}{|\Sigma|} \Sigma^{\ast}\\
&=& \frac{1}{|\Sigma|}\begin{pmatrix}
\sigma_2^2 & -\rho \sigma_1\sigma_2 \\
-\rho \sigma_1\sigma_2 & \sigma_1^2
\end{pmatrix}
\end{eqnarray*}
$$

其中， $\Sigma^{\ast}$ 是 $\Sigma$ 的伴随矩阵。所以，二元正态分布的密度函数为

$$
\begin{eqnarray*}
p(\mathbf{x}) &=&p(x_1,x_2) = (2 \pi)^{-\frac{2}{2}}|\Sigma|^{-\frac{1}{2}} \exp \left\{-\frac{1}{2}(\mathbf{x}-\mathbf{\mu})' \Sigma^{-1}(\mathbf{x}-\mathbf{\mu})\right\}\\
&=& (2 \pi)^{-1} \left((1-\rho^2) \sigma_1^2\sigma_2^2\right)^{-1/2}\\
&&\cdot
\exp\left\{
-\frac{1}{2} ((x_1,x_2)' - (\mu_1,\mu_2)')' \frac{1}{(1-\rho^2) \sigma_1^2\sigma_2^2}\begin{pmatrix}
\sigma_2^2 & -\rho \sigma_1\sigma_2 \\
-\rho \sigma_1\sigma_2 & \sigma_1^2
\end{pmatrix} ((x_1,x_2)' - (\mu_1,\mu_2)')
\right\}\\
&=& (2 \pi)^{-1} \left((1-\rho^2) \sigma_1^2\sigma_2^2\right)^{-1/2}\\
&&\cdot
\exp\left\{
-\frac{1}{2(1-\rho^2)} \left(\frac{(x_1 -\mu_1)^2}{\sigma_1^2} - 2\rho \cdot \frac{(x_1 -\mu_1)(x_2-\mu_2)}{\sigma_1\sigma_2} + \frac{(x_2 -\mu_2)^2}{\sigma_2^2}
\right)
\right\}\\
\end{eqnarray*}
$$

```

`````{prf:example}
二维正态分布的边际分布为一元正态分布。
```{dropdown} Solution

 $(X_1,X_2)'$ 的联合密度函数为

$$
\begin{eqnarray*}
p(x_1,x_2)&=&(2 \pi)^{-1} \left((1-\rho^2) \sigma_1^2\sigma_2^2\right)^{-1/2}\\
&&\cdot
\exp\left\{
-\frac{1}{2(1-\rho^2)} \left(\frac{(x_1 -\mu_1)^2}{\sigma_1^2} - 2\rho \cdot \frac{(x_1 -\mu_1)(x_2-\mu_2)}{\sigma_1\sigma_2} + \frac{(x_2 -\mu_2)^2}{\sigma_2^2}
\right)
\right\}\\
\end{eqnarray*}
$$

于是， $X$ 的边际密度函数为

$$
\begin{eqnarray*}
p_{X_1}(x_1) &=&\int_{-\infty}^{+\infty} p(x_1, x_2) d x_2 \\
&=&\int_{-\infty}^{+\infty}(2 \pi)^{-1} \left((1-\rho^2) \sigma_1^2\sigma_2^2\right)^{-1/2}\\
&&\cdot
\exp\left\{
-\frac{1}{2(1-\rho^2)} \left(\frac{(x_1 -\mu_1)^2}{\sigma_1^2} - 2\rho \cdot \frac{(x_1 -\mu_1)(x_2-\mu_2)}{\sigma_1\sigma_2} + \frac{(x_2 -\mu_2)^2}{\sigma_2^2}
\right)
\right\} \text{d} x_2 \\
&=&
\int_{-\infty}^{+\infty} (2 \pi)^{-1/2} \left((1-\rho^2) \sigma_2^2\right)^{-1/2}
\exp\left\{ -\frac{1}{2(1-\rho^2)}\cdot
\left( \frac{(x_2 -\mu_2)}{\sigma_2} - \rho \frac{(x_1 -\mu_1)}{\sigma_1} \right)^2 \right\} \text{d} x_2 \\
&&\cdot (2\pi \sigma_1^2)^{-1/2}\cdot \exp\left\{ -\frac{(1-\rho^2)}{2(1-\rho^2)} \frac{(x_1 -\mu_1)^2}{\sigma_1^2}
\right\} \\
&=&(2\pi \sigma_1^2)^{-1/2}\cdot \exp\left\{ - \frac{(x_1 -\mu_1)^2}{2\sigma_1^2}
\right\}
\end{eqnarray*}
$$

其中，第三个等式成立的原因是

$$
\begin{eqnarray*}
&& \frac{(x_2 -\mu_2)^2}{\sigma_2^2} - 2\rho \cdot \frac{(x_1 -\mu_1)(x_2-\mu_2)}{\sigma_1\sigma_2} +\frac{(x_1 -\mu_1)^2}{\sigma_1^2} \\
&=& \frac{(x_2 -\mu_2)^2}{\sigma_2^2} - 2\rho \cdot \frac{(x_1 -\mu_1)(x_2-\mu_2)}{\sigma_1\sigma_2} + \rho^2\frac{(x_1 -\mu_1)^2}{\sigma_1^2} + \frac{(x_1 -\mu_1)^2}{\sigma_1^2} - \rho^2\frac{(x_1 -\mu_1)^2}{\sigma_1^2}\\
&=& \left( \frac{(x_2 -\mu_2)}{\sigma_2} - \rho \frac{(x_1 -\mu_1)}{\sigma_1} \right)^2 + (1-\rho^2) \frac{(x_1 -\mu_1)^2}{\sigma_1^2}.
\end{eqnarray*}
$$

所以， $X$ 的边际分布为 $N(\mu_1,\sigma_1^2)$ 。
```
`````