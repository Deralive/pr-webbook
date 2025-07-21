# 因子分解定理
根据以上例子，我们发现定义往往可以论证某一个统计量是充分统计量。但是难以通过定义来寻找那个统计量是充分的。以下我们有因子分解定理，可以帮助我们来寻找。

``````{prf:theorem} 因子分解定理
设总体概率函数为 $f(x;\theta)$ ， $x_1,\cdots,x_n$ 是样本，则 $T = T(x_1,x_2,\cdots,x_n)$ 为充分统计量的充分必要条件是：存在两个函数 $g(t,\theta)$ 和 $h(x_1,x_2,\cdots,x_n)$ 使得对任意的 $\theta$ 和任一组观测值 $x_1,x_2,\cdots,x_n$ ，有

$$
\begin{eqnarray*}
f(x_1,x_2,\cdots,x_n;\theta) = g(T(x_1,x_2,\cdots,x_n),\theta)h(x_1,x_2,\cdots,x_n),
\end{eqnarray*}
$$

其中， $g(t,\theta)$ 是通过统计量 $T$ 的取值而依赖于样本的。
```{dropdown} Proof
本定理的一般性结果的证明过程超过了本课程的内容。以下仅考虑离散随机比纳凉的证明。此时概率函数为

$$
f(x_1,x_2,\cdots,x_n;) = P(X_1 = x_1,X_2=x_2,\cdots,X_n = x_n;\theta).
$$

首先证明必要性。假定 $T$ 是充分统计量，所以

$$
\begin{eqnarray*}
P(X_1 = x_1,X_2=x_2,\cdots,X_n = x_n|T=t)
\end{eqnarray*}
$$

与 $\theta$ 无关。我们将其记为 $h(x_1,x_2,\cdots,x_n)$ 。令 $A(t) = \left\{x_1,x_2,\cdots,x_n | T(x_1,x_2,\cdots,x_n) = t\right\}$ 。当样本 $(x_1,x_2,\cdots,x_n) \in A(t)$ 时有

$$
\{T = t\} \subset \{X_1 = x_1,X_2=x_2,\cdots,X_n = x_n\},
$$

故

$$
\begin{eqnarray*}
P(X_1 =x_1,X_2=x_2,\cdots,X_n = x_n ) &=&
P(X_1 =x_1,X_2=x_2,\cdots,X_n = x_n , T= t;\theta) \\
&=& P(X_1 =x_1,X_2=x_2,\cdots,X_n = x_n | T= t) P(T =t;\theta)\\
&=& h(x_1,x_2,\cdots,x_n) g(t,\theta).
\end{eqnarray*}
$$

其中 $g(t,\theta) = P(T = t;\theta)$ ，而 $h(x_1,x_2,\cdots,x_n) = P(X_1=x_1,X_2=x_2,\cdots,X_n = x_n|T=t)$ 与 $\theta$ 无关。因此，必要性得证。
其次证明充分性。由于

$$
\begin{eqnarray*}
P(T=t;\theta) &=& \sum_{(x_1,x_2,\cdots,x_n)\in A(t)} P(X_1 = x_1,X_2=x_2,\cdots,X_n=x_n;\theta)\\
&=& \sum_{(x_1,x_2,\cdots,x_n)\in A(t)} g(t,\theta) h(x_1,x_2,\cdots,x_n).
\end{eqnarray*}
$$

对任意 $(x_1,x_2,\cdots,x_n)$ 和 $t$ ，满足 $(x_1,x_2,\cdots,x_n)\in A(t)$ 有

$$
\begin{eqnarray*}
P(X_1 = x_1,X_2=x_2,\cdots,X_n=x_n|T=t) &=& \frac{P(X_1 = x_1,X_2=x_2,\cdots,X_n=x_n,T = t;\theta)}{P(T=t;\theta)}\\
&=& \frac{P(X_1 = x_1,X_2=x_2,\cdots,X_n=x_n;\theta)}{P(T=t;\theta)}
\\
&=& \frac{g(t,\theta) h(x_1,x_2,\cdots,x_n)}{ g(t,\theta)\sum_{(x_1,x_2,\cdots,x_n)\in A(t)} h(x_1,x_2,\cdots,x_n)}\\
&=& \frac{h(x_1,x_2,\cdots,x_n)}{ \sum_{(x_1,x_2,\cdots,x_n)\in A(t)} h(x_1,x_2,\cdots,x_n)}
.
\end{eqnarray*}
$$

该分布与 $\theta$ 无关，这证明了充分性。
```

```{admonition} Remark
这里 $T$ 可以是一维的，也可以是多维的。
```

``````

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自于 $b(1,\theta)$ 的样本。于是， $x_1,x_2,\cdots,x_n$ 的概率函数为

$$
P(X_1=x_1,X_2=x_2,\cdots,X_n=x_n) = \prod_{i=1}^n \theta^{x_i}(1-\theta)^{1-x_i} = \theta^{\sum_{i=1}^n x_i} (1-\theta)^{n - \sum_{i=1}^n x_i}.
$$

令 $t = \sum_{i=1}^n x_i$ ， $g(t,\theta) = (1-\theta)^{n} \left(\theta/(1-\theta)\right)^t$ 且 $h(x_1,x_2,\cdots,x_n) = 1$ 。根据因子分解定理， $t$ 是 $\theta$ 的充分统计量。
`````

`````{prf:example}
设 $x_1,x_2,\cdots,x_n$ 是来自于 $N(\mu,\sigma^2)$ 的样本。

````{tab-set}

```{tab-item} 若 $\sigma^2 = \sigma_0^2$ ，其中 $\sigma_0^2$ 已知。 

$x_1,x_2,\cdots,x_n$ 的概率函数为

$$
\begin{eqnarray*}
p(x_1,x_2,\cdots,x_n) &=
&(2\pi\sigma_0^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma_0^2} \sum_{i=1}^n (x_i-\mu)^2\right\}\\
&=&(2\pi\sigma_0^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma_0^2} \left(\sum_{i=1}^n x_i^2 - 2n \bar{x}\mu + n\mu^2\right)\right\}\\
&=& (2\pi\sigma_0^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma_0^2} \sum_{i=1}^n x_i^2 + \frac{n}{\sigma_0^2} \bar{x}\mu -\frac{n}{2\sigma_0^2}\mu^2\right\}
\end{eqnarray*}
$$

令 $t = \bar{x}$ ，

$$g(t,\mu) = \exp\{n\bar{x}\mu / \sigma_0^2 - n\mu^2/(2\sigma_0^2)\},$$

和

$$h(x_1,x_2,\cdots,x_n) = (2\pi\sigma_0^2)^{-n/2} \exp\{ -\sum_{i=1}^n x_i^2/(2\sigma_0^2)\}.$$

根据因子分解定理， $t=\bar{x}$ 是充分统计量。
```

```{tab-item} 若 $\mu = 0$

$x_1,x_2,\cdots,x_n$ 的概率函数为

$$
\begin{eqnarray*}
p(x_1,x_2,\cdots,x_n) &=
&(2\pi\sigma^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i)^2\right\}
\end{eqnarray*}
$$

令

$$
t = \sum_{i=1}^n x_i^2,
$$

$$g(t,\sigma^2) = (2\pi\sigma^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i)^2\right\}$$

和

$$
h(x_1,x_2,\cdots,x_n) = 1.
$$

根据因子分解定理， $t = \sum_{i=1}^n x_i^2$ 是充分统计量。
```

```{tab-item} 令 $\theta = (\mu,\sigma_0^2)'$

$x_1,x_2,\cdots,x_n$ 的概率函数为

$$
\begin{eqnarray*}
p(x_1,x_2,\cdots,x_n) &=
&(2\pi\sigma^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i-\mu)^2\right\}\\
&=&(2\pi\sigma^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma^2} \left(\sum_{i=1}^n x_i^2 - 2n \bar{x}\mu + n\mu^2\right)\right\}\\
&=& (2\pi\sigma^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma^2} \sum_{i=1}^n x_i^2 + \frac{n}{\sigma^2} \bar{x}\mu -\frac{n}{2\sigma^2}\mu^2\right\}
\end{eqnarray*}
$$

令

$$
\boldsymbol{t} = (t_1,t_2)' = (\bar{x},\sum_{i=1}^n x_i^2)',
$$

$$
g(t,\mu,\sigma^2) = (2\pi\sigma^2)^{-n/2} \exp\left\{ - \frac{1}{2\sigma^2} \sum_{i=1}^n x_i^2 + \frac{n}{\sigma^2} \bar{x}\mu -\frac{n}{2\sigma^2}\mu^2\right\}
$$

和

$$
h(x_1,x_2,\cdots,x_n) = 1.
$$

根据因子分解定理， $\mathbf{t} = (t_1,t_2)' = (\bar{x},\sum_{i=1}^n x_i^2)'$ 是充分统计量。
```
````
`````

以下例子是一个拓展。

`````{prf:example}
总体分布为指数型分布族，即其概率函数为

$$
p(x;\theta) = C(\theta) \exp\left\{g(\theta) t(x)\right\}h(x).
$$

如果 $x_1,x_2,\cdots,x_n$ 是样本，则 $\sum_{i=1}^n t(x_i)$ 是充分统计量。
`````

```{admonition} Remark
 $\sum_{i=1}^n t(x_i)$ 不仅是充分统计量，还是充分完备统计量。
```

已经证明某个统计量是充分的。如果我们想要论证另一个统计量也是充分的，那么并不需要从定义或因子分解定理直接出发，我们有以下定理来解决这个问题。

``````{prf:theorem}
设统计量 $T$ 是充分统计量，而 $S$ 也是一个统计量。如果 $T$ 可以表示为 $S$ 的函数，即 $T=\varphi(S)$ ，那么 $S$ 也是充分统计量。
``````