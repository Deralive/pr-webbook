# 可加性（卷积公式）
“加法”是一种最为常见的运算方法。对多个随机变量进行求和是实际场景中具有广泛应用。例如：我们考虑学生每个月在衣、食、行及其他的预算，其中每一项均可以看作一个随机变量，而这四个随机变量的和可以表示该生每个月的消费预算，具有实际意义。因此，如何求多个随机变量的和的分布这里将会给出一般的计算方法。首先，我们先看一个例子。

`````{prf:example} 
:label: ex:lect9_1
有两个服从泊松分布且相互独立的随机变量，其和仍旧服从泊松分布。即设 $X \sim P\left(\lambda_{1}\right), Y \sim P\left(\lambda_{2}\right)$ 且 $X$ 与 $Y$ 独立，则 $X+Y \sim P(\lambda_{1}+\lambda_{2})$ 。
```{dropdown} Proof
令这两个随机变量的和为 $Z$ ，即 $Z=X+Y$ 。可以注意到 $Z$ 的取值范围为 $0,1,2,\cdots$ ，即所有非负整数。而事件 ${Z=k}$ 可看作一些互不相容事件的并，即， $\{Z=k\}=\cup_{i=0}^{k}\{X=i, Y=k-i\}$ 。
于是，对于任意非负整数 $k$ ，有

$$
\begin{eqnarray*}
P(Z=k) &=&P\left(\cup_{i=0}^{k}\{X=i, Y=k-i\}\right) =\sum_{i=0}^{k} P\left(X=i, Y=k-i\right) \\
&=& \sum_{i=0}^{k} P(X=i) \cdot P(Y=k-i) \\
&=&\sum_{i=0}^{k} \frac{\lambda_{1}^{i}}{i !} e^{-\lambda_{1}} \cdot \frac{\lambda_{2}^{k-i}}{(k-i)!} e^{-\lambda_{2}} \\
&=&\frac{\left(\lambda_{1}+\lambda_{2}\right)^{k}}{k !} e^{-\left(\lambda_{1}+\lambda_{2}\right)} \sum_{i=0}^{k} \frac{k !}{i !(k-i) !}\left(\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}\right)^{i} \cdot\left(\frac{\lambda_{2}}{\lambda_{1}+\lambda_{2}}\right)^{k-i} \\
&=&\frac{\left(\lambda_{1}+\lambda_{2}\right)^{k}}{k !} e^{-\left(\lambda_{1}+\lambda_{2}\right)}
\end{eqnarray*}
$$

这表明 $X+Y \sim P(\lambda_{1}+\lambda_{2})$ 。
```
`````

```{admonition} Remark

- 上述这个性质也可以推广到有限个独立的泊松分布的和。
- 上述例子表明：两个独立且服从同一类随机变量的和仍服从该分布。由此，我们需要用一个专有名词来表述分布所独有的一种性质。

```

可加性
: 如果某个分布满足服从该分布的多个独立随机变量的和仍服从该类分布，那么称该分布具有可加性。

对于更为一般的求两个随机变量和的形式，我们这里提供以下定理来解决。

``````{prf:theorem} 卷积公式
:label: def:convolution
设 $X$ 与 $Y$ 是两个相互独立的连续随机变量，其密度函数分别为 $p_X(x)$ 和 $p_Y(y)$ ，则其和 $Z = X+Y$ 的密度函数为

$$
\begin{eqnarray*}
p_Z(z) = \int_{-\infty}^{\infty} p_{X}(z-y) p_{Y}(y) \text{d} y \\
= \int_{-\infty}^{\infty} p_{X}(x) p_{Y}(z-x) \text{d} x
\end{eqnarray*}
$$

```{dropdown} Proof
考虑到 $Z = X+Y$ 的分布函数为

$$
\begin{eqnarray*}
F_Z(z) &=& P(Z \leq z) = \iint_{x+y\leq z} p_{X}(x) p_Y(y) \text{d}x \text{d}y\\
& = &\int_{-\infty}^{\infty} \left(\int_{-\infty}^{z-y} p_X(x)\text{d}x\right)p_Y(y)\text{d}y\\
&=&\int_{-\infty}^{\infty} \left(\int_{-\infty}^{z} p_X(t-y)\text{d}t\right)p_Y(y)\text{d}y\\
&=& \int_{-\infty}^{z} \left(\int_{-\infty}^{\infty} p_X(t-y) p_Y(y)\text{d}y\right)\text{d}t
\end{eqnarray*}
$$

由此可得， $Z$ 的密度函数为

$$
p_Z(z) = \int_{-\infty}^{\infty} p_X(z-y) p_{Y}(y)\text{d}y.
$$

令 $z-y=x$ ，则可得

$$
p_Z(z) = \int_{-\infty}^{\infty} p_{X}(x) p_{Y}(z-x) \text{d}x.
$$

```

```{admonition} Remark
:class: dropdown
- **卷积**名称的由来：在泛函分析中，卷积指的是通过两个可积函数 $f$ 和 $g$ ，利用积分运算来生成一个新的函数，即

$$
\int_{-\infty}^{\infty} f(\tau)g(x-\tau)\text{d} \tau.
$$

- 在上述定理中假定两个随机变量 $X$ 和 $Y$ 是相互独立的。但是，对于不独立的 $X$ 和 $Y$ ，只需要把边际密度函数的乘积改为联合密度函数即可。
- 上述定理给出的是连续场合的卷积公式，在离散场合同样适用。值得注意的是，连续场合下的密度函数应被替换为分布列，而求积分运算应被替换为求和。

```

``````

根据卷积公式，我们应用于两个例子中。

`````{prf:example} 正态分布的可加性
设随机变量 $X \sim N\left(\mu_{1}, \sigma_{1}^{2}\right), Y \sim N\left(\mu_{2}, \sigma_{2}^{2}\right)$ ,且 $X$ 与 $Y$ 独立。证明

$$Z=X+Y \sim N\left(\mu_{1}+\mu_{2}, \sigma_{1}^{2}+\sigma_{2}^{2}\right).$$

```{dropdown} Proof
首先， $Z=X+Y$ 仍在 $(-\infty,+\infty)$ 上取值。
其次，利用连续场合下的卷积公式，可得

$$p_{Z}(z)=\frac{1}{2 \pi \sqrt{\sigma_{1}^{2} \sigma_{2}^{2}}} \int_{-\infty}^{+\infty} \exp \left\{-\frac{1}{2 \sigma_{1}^{2}}\left(z-y-\mu_{1}\right)^{2}\right\} \exp \left\{-\frac{1}{2 \sigma_{2}^{2}}\left(y-\mu_{2}\right)^{2}\right\} \text{d} y .$$

注意到

$$
\begin{eqnarray*}
& &\frac{1}{\sigma_{1}^{2}}\left(z-y-\mu_{1}\right)^{2}+\frac{1}{\sigma_{2}^{2}}\left(y-\mu_{2}\right)^{2} \\
&=& \frac{1}{\sigma_{1}^{2}} y^{2}-\frac{2}{\sigma_{1}^{2}}\left(z-\mu_{1}\right) y+\frac{1}{\sigma_{1}^{2}}\left(z-\mu_{1}\right)^{2}+\frac{1}{\sigma_{1}^{2}} y^{2}-\frac{2}{\sigma_{2}^{2}} \mu_{2} z+\frac{1}{\sigma_{2}^{2}} \mu_{2}^{2} \\
&=&\left(\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}\right) y^{2}-2 y\left(\frac{z-\mu_{1}}{\sigma_{1}^{2}}+\frac{\mu_{2}}{\sigma_{2}^{2}}\right)+\frac{1}{\sigma_{1}^{2}}\left(z-\mu_{1}\right)^{2}+\frac{1}{\sigma_{2}^{2}} \mu_{2}^{2} \\
&=&\left(\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}\right)\left(y-\frac{\frac{z-\mu_{1}}{\sigma_{1}^{2}}+\frac{\mu_{2}}{\sigma_{2}^{2}}}{\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}}\right)^{2}-\frac{\left(\frac{z-\mu_{1}}{\sigma_{1}^{2}}+\frac{\mu_{2}}{\sigma_{2}^{2}}\right)^{2}}{\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}}+\frac{1}{\sigma_{2}^{2}}\left(z-\mu_{1}^{2}\right)+\frac{1}{\sigma_{2}^{2}} \mu_{2}^{2} \\
&=& A\left(y-\frac{B}{A}\right)^{2}-\frac{\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}}{\sigma_{1}^{2}+\sigma_{2}^{2}}\left(z-\mu_{1}\right)^{2}-\frac{\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}}{\sigma_{1}^{2}+\sigma_{2}^{2}} \mu_{2}^{2}
-\frac{2}{\sigma_{1}^{2}+\sigma_{2}^{2}} \cdot\left(z-\mu_{1}\right) \mu_{2}+\frac{1}{\sigma_{1}^{2}}\left(z-\mu_{1}\right)^{2}+\frac{1}{\sigma_{2}^{2}} \mu_{2}^{2} \\
&=& A\left(y-\frac{B}{A}\right)^{2}+\frac{1}{\sigma_{1}^{2}+\sigma_{2}^{2}}\left(z-\mu_{1}-\mu_{2}\right)^{2},
\end{eqnarray*}
$$

其中，

$$
A = \frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2}, \quad \text{且}\quad
B = \frac{z-\mu_1}{\sigma_1^2} + \frac{\mu_2}{\sigma_2^2}.
$$

于是，我们有

$$
\begin{eqnarray*}
p_{Z}(z)&=&\frac{1}{2 \pi \sqrt{\sigma_{1}^{2} \sigma_{2}^{2}}} \int_{-\infty}^{+\infty} \exp \left\{-\frac{1}{2}\left(\frac{1}{ \sigma_{1}^{2}}\left(z-y-\mu_{1}\right)^{2} -\frac{1}{\sigma_{2}^{2}}\left(y-\mu_{2}\right)^{2}\right)\right\} \text{d} y
\\
&=&\frac{1}{2 \pi \sqrt{\sigma_{1}^{2} \sigma_{2}^{2}}} \exp \left\{-\frac{1}{2} \cdot\frac{\left(z-\mu_{1}-\mu_{2}\right)^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}\right\} \cdot \int_{-\infty}^{+\infty} \exp \left\{-\frac{A}{2}\left(y-\frac{B}{A}\right)^{2}\right\} \text{d} y \\
&=&\frac{1}{\sqrt{2 \pi (\sigma_{1}^{2} +\sigma_{2}^{2})}} \exp \left\{-\frac{1}{2} \cdot \frac{\left(z-\mu_{1}-\mu_{2}\right)^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}\right\}
\end{eqnarray*}
$$

其中 $\int_{-\infty}^{+\infty} \exp \left\{-\frac{A}{2}\left(y-\frac{B}{A}\right)^{2}\right\} \text{d} y$ 看成一个正态随机变量的核，即 $N\left(\frac{B}{A}, \frac{1}{A}\right)$ 。
因此， $Z$ 的密度函数为

$$
\begin{eqnarray*}
P_{Z}(z) =\frac{1}{\sqrt{2 \pi\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)}} \exp \left\{-\frac{1}{2} \cdot \frac{\left(z-\mu_{1}-\mu_{2}\right)^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}\right\}.
\end{eqnarray*}
$$

也就是说， $Z \sim N\left(\mu_{1}+\mu_{2}, \sigma_{1}^{2}+\sigma_{2}^{2}\right)$ 。
```

```{admonition} Remark
:class: dropdown
这个结论也可推广至有限个独立的正态分布随机变量的线性组合。也就是说，若 $X_i\sim N(\mu_i,\sigma_i^2),i=1,2,\cdots,n$ ，诸 $X_i$ 之间相互独立且 $a_1,a_2,\cdots,a_n$ 为 $n$ 个非零常数，则

$$
\sum_{i=1}^n a_i X_i = a_1X_1+a_2X_2+\cdots+a_nX_n\sim N(\mu_0,\sigma_0^2),
$$

其中， $\mu_0 = \sum_{i=1}^n a_i \mu_i$ ， $\sigma_0^2 = \sum_{i=1}^n a_i^2 \sigma_0^2$ 。
```

`````

````{admonition} Question
如果 $(X_1,X_2)'$ 服从二元正态分布随机变量，且 $\text{Corr}(X_1,X_2) = \rho \neq 0$ ，那么 $X-Y$ 的分布是什么？

```{admonition} Tips
这个问题留给学生课后思考。
````
`````{prf:example}
设随机变量 $X \sim Ga\left(\alpha_{1}, \lambda\right), Y \sim Ga\left(\alpha_{2}, \lambda\right)$ 且 $X$ 与 $Y$ 独立。证明

$$ X+Y \sim Ga\left(\alpha_{1}+\alpha_{2}, \lambda\right).$$

```{dropdown} Proof
首先， $Z=X+Y$ 仍在 $(0,+\infty)$ 上取值，所以当 $z \leqslant 0$ 时， $p_Z(z)=0$ 。而当 $z>0$ 时，

$$
\begin{eqnarray*}
p_{z}(z) &=&\int_{0}^{z} \frac{\lambda^{\alpha_{1}+\alpha_{2}}}{\Gamma\left(\alpha_{1}\right) P\left(\alpha_{2}\right)}(z-y)^{\alpha_{1}-1} e^{-\lambda(\lambda-y)} y^{\alpha_{2}-1} e^{-\lambda y} \text{d} y \\
&=&\frac{\lambda^{\alpha_{1}+\alpha_{2}} e^{-\lambda z}}{\Gamma\left(\alpha_{1}\right) \Gamma\left(\alpha_{2}\right)} \int_{0}^{z}(z-y)^{\alpha_{1}-1} y^{\alpha_{2}-1} \text{d} y \\
&=&\frac{\lambda^{\alpha_{1}+\alpha_{2}} z^{\alpha_{1}+\alpha_{2}-2} e^{-\lambda z}}{\Gamma\left(\alpha_{1}\right) \Gamma\left(\alpha_{2}\right)} \int_{0}^{z}\left(1-\frac{y}{z}\right)^{\alpha_{1}-1}\left(\frac{y}{z}\right)^{\alpha_{2}-1} \text{d} y \\
&=&\frac{\lambda^{\alpha_{1}+\alpha_{2}}}{\Gamma\left(\alpha_{1}+\alpha_{2}\right)} z^{\alpha_{1}+\alpha_{2}-1} e^{-\lambda z}
\end{eqnarray*}
$$

因此， $Z \sim \operatorname{Ga}\left(\alpha_{1}+\alpha_{2}, \lambda\right)$ 。
```

```{admonition} Remark
:class: dropdown
- 这个结论也可以推广至有限个独立的伽马分布随机变量的和。
- 由于指数分布是一种特殊的伽马分布，即 $Exp(\lambda) = Ga(1,\lambda)$ 。那么 $m$ 个独立同分布的指数分布随机变量之和为伽马分布。
- 由于卡方分布是一种特殊的伽马分布，
即 $\chi^2(n) = Ga\left(\frac{n}{2},\frac{1}{2}\right)$ 。那么 $m$ 个独立的卡方分布随机变量之和仍为卡方分布。

```

`````

这里我们总结一下，具有可加性的常见分布。

- 二项分布： $b(n,p) * b(m,p) = b(n+m,p)$ .（留作学生课后自学内容）
- 泊松分布： $P(\lambda_1)*P(\lambda_2) = P(\lambda_1+\lambda_2)$ .
- 正态分布：
 $N(\mu_1,\sigma_1^2) * N(\mu_2,\sigma_2^2) = N(\mu_1+\mu_2, \sigma_1^2 + \sigma_2^2)$ .
- 伽马分布：
 $Ga(\alpha_1,\lambda) * Ga(\alpha_2,\lambda) = Ga(\alpha_1+\alpha_2,\lambda)$ .