# 多维随机向量函数的数学期望
对一般多维随机向量函数的数学期望，我们可以类似于一维随机变量函数的数学期望定义。

``````{prf:theorem}
若多维随机变量 $\boldsymbol{X}$ 的分布用联合分布列 $P(\boldsymbol{X}=\boldsymbol{x})$ 或用联合密度函数 $p(\boldsymbol{x})$ 表示，则 $Z=g(\boldsymbol{X})$ 的数学期望为

$$E(Z)=\left\{
\begin{aligned}
&\sum_{\boldsymbol{x}} g\left(\boldsymbol{x}\right) P\left(\boldsymbol{X}=\boldsymbol{x}\right), & \text{在离散场合} \\
&\int_{R^n} g(\boldsymbol{x}) p(\boldsymbol{x}) \text{d} \boldsymbol{x} , & \text{在连续场合}
\end{aligned}\right.$$

``````

特别地，对于二维随机变量，我们定义其函数的期望如下。

``````{prf:theorem}
若二维随机变量 $(X,Y)$ 的分布用联合分布列 $P(X=x_{i},Y=y_{j})$ 或用联合密度函数 $p(x,y)$ 表示，则 $Z=g(X,Y)$ 的数学期望为

$$E(Z)=\left\{
\begin{aligned}
&\sum_{i} \sum_{j} g\left(x_{i}, y_{j}\right) P\left(X=x_{i}, Y=y_{j}\right), & \text{在离散场合} \\
&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} g(x, y) p(x, y) \text{d} x \text{d} y,& \text{在连续场合}
\end{aligned}\right.$$

``````

对于 $X$ 和 $Y$ 的期望与方差，我们都可以用一个统一的形式进行表示。

```{admonition} Remark

- 当 $g(X,Y)=X$ 时， $X$ 的数学期望为

$$
\begin{eqnarray*}
E(X) &=&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} x p(x ,y) \text{d} y \text{d} x \\
&=&\int_{-\infty}^{+\infty} x p_{X}(x) \text{d} x
\end{eqnarray*}
$$

- 当 $g(X,Y)=(X-EX)^{2}$ 时， $X$ 的方差为

$$
\begin{eqnarray*}
\text{Var}(X)&=&E(X-E X)^{2} \\
&=&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}(x-E(X))^{2} p(x, y) \text{d} y \text{d}x \\
&=&\int_{-\infty}^{+\infty}(x-E(X))^{2} p_{X}(x) \text{d} x
\end{eqnarray*}
$$

- 当 $g(X,Y)=Y$ 时， $Y$ 的数学期望为

$$
\begin{eqnarray*}
E(Y) &=&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} y p(x ,y) \text{d} x \text{d} y \\
&=&\int_{-\infty}^{+\infty} y p_{Y}(y) \text{d} y
\end{eqnarray*}
$$

- 当 $g(X,Y)=(Y-EY)^{2}$ 时， $Y$ 的方差为

$$
\begin{eqnarray*}
\text{Var}(Y)&=&E(Y-E Y)^{2} \\
&=&\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}(y-E(Y))^{2} p(x, y) \text{d} y \text{d} x\\
&=&\int_{-\infty}^{+\infty}(y-E(Y))^{2} p_{Y}(y) \text{d} y
\end{eqnarray*}
$$

```

`````{prf:example}
在长度为 $a$ 的线段上任取两个点 $X$ 与 $Y$ ，求此两点间的平均长度。
```{dropdown} Solution

因为 $X$ 与 $Y$ 均服从 $(0,a)$ 上的均匀分布且 $X$ 与 $Y$ 相互独立，所以 $(X,Y)$ 的联合密度函数为

$$p(x, y)=\left\{\begin{aligned}
&\frac{1}{a^{2}}&,0<x,y<a\\
&0&,\text{其他}
\end{aligned}\right.$$

两点间的平均长度为

$$
\begin{eqnarray*}
E(|X-Y|) &=&\int_{0}^{a} \int_{0}^{a}|x-y| \cdot \frac{1}{a^{2}} \text{d} x \text{d} y=\frac{1}{a^{2}}\left(\int_{0}^{a} \int_{0}^{x}(x-y) \text{d} y \text{d} x+\int_{0}^{a} \int_{x}^{a}(y-x) \text{d} y \text{d} x\right) \\
&=&\frac{1}{a^{2}}\left(\int_{0}^{a} \left(x y-\left.\frac{1}{2} y^{2}\right)\right|_{0} ^{x} \text{d} x+\int_{0}^{a} \left(\frac{1}{2} y^{2}-\left.x y\right)\right|_{x} ^{a} \text{d} x\right) \\
&=&\frac{1}{a^{2}} \int_{0}^{a}\left(\frac{1}{2} x^{2}+\frac{1}{2} a^{2}-a x+\frac{1}{2} x^{2}\right) \text{d} x \\
&=&\frac{1}{a^{2}}\left(\frac{1}{2} a^{2} x-\frac{1}{2} a x^{2}+\left.\frac{1}{3} x^{3}\right|_{0} ^{a}\right) = \frac{1}{a^{2}}\left(\frac{1}{2} a^{3}-\frac{1}{2} a^{3}+\frac{1}{3} a^{3}\right)\\
&=&\frac{a}{3}.
\end{eqnarray*}
$$

```
`````
以下我们介绍一些期望和方差的性质。

`````{prf:property}

- 期望与求和可交换：设 $(X,Y)$ 是二维随机变量，则有

$$E(X+Y) = E(X) + E(Y).$$

```{admonition} Remark

$n$ 个随机变量和的期望等于 $n$ 个随机变量期望的和，即

$$
E\left(\sum_{i=1}^{n} X_i\right) = \sum_{i=1}^{n} E(X_i)
$$

```

- 多个独立随机变量的期望与方差的简便计算公式。

- 若随机变量 $X$ 和 $Y$ 相互独立，则有

$$E(XY) = E(X)E(Y).$$

```{dropdown} Proof
这里仅证明 $(X,Y)$ 为连续随机变量，离散随机变量的证明过程供学生课后自行完成。其密度函数为 $p(x,y)$ 。因为 $X$ 和 $Y$ 相互独立，所以 $p(x,y) = p_X(x)p_Y(y)$ 。令 $g(X,Y) = XY$ ，则有

$$
\begin{eqnarray*}
E(XY) &=& \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} xy p(x,y) \text{d}x \text{d}y\\
&=& \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} xy p_X(x) p_Y(y) \text{d}x \text{d}y\\
&=& \int_{-\infty}^{\infty} x p_X(x)\text{d}x \cdot\int_{-\infty}^{\infty} y p_Y(y) \text{d}y\\
&=& E(X) E(Y).
\end{eqnarray*}
$$

```

```{admonition} Remark
若 $X_1,X_2,\cdots,X_n$ 相互独立，则有

$$
E\left(\prod_{i=1}^n X_i\right) = \prod_{i=1}^n E(X_i).
$$

```

- 若随机变量 $X$ 与 $Y$ 相互独立，则有

$$
\text{Var}(X\pm Y) = Var(X) + Var(Y).
$$

```{dropdown} Proof
根据定义，

$$
\begin{eqnarray*}
\text{Var} (X\pm Y) &=& E(X\pm Y - (E(X) \pm E(Y)))^2 = E((X - E(X))\pm (Y-E(Y)))^2\\
&=& E((X - E(X))^2 + (Y-E(Y))^2 \pm 2(X - E(X))(Y-E(Y)))\\
&=& E(X - E(X))^2 + E(Y-E(Y))^2 \pm 2E((X - E(X))(Y-E(Y)))\\
&=& E(X - E(X))^2 + E(Y-E(Y))^2\\
&=& \text{Var}(X)+\text{Var}(Y),
\end{eqnarray*}
$$

最后一个等式成立是因为 $E((X - E(X))(Y-E(Y))) = E(XY) - E(X)E(Y) = 0$ .
```

```{admonition} Remark

- 若 $X_1,X_2,\cdots,X_n$ 相互独立，则有

$$
\text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i).
$$

- 若 $X_1,X_2,\cdots,X_n$ 是独立同分布的随机变量，且方差存在， $Var(X_1) = \sigma^2$ ，则其算术平均数的方差为

$$
\text{Var}\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{1}{n^2} \sum_{i=1}^n \sigma^2 = \frac{\sigma^2}{n}.
$$

```

`````

`````{prf:example}
设一袋中装有 $m$ 个颜色各不相同的球，每次从中任取一个，有放回地摸取 $n$ 次，以 $X$ 表示在 $n$ 次摸球中摸到球的不同颜色的数目，求 $E(X)$ 。
```{dropdown} Solution

令 $X_i$ 表示是否第 $i$ 种颜色的球在 $n$ 次摸球中至少被摸到一次，即

$$
X_i = \left\{
\begin{aligned}
& 1, & \text{摸到过,}\\
& 0, & \text{未摸到,}
\end{aligned}\right.i=1,2,\cdots,m.
$$

于是，第 $i$ 种颜色的球在 $n$ 次摸球中未被摸到过的概率为

$$
P(X_i=0) = \left(1-\frac{1}{m} \right)^{n}.
$$

令 $X$ 为 $n$ 次摸球中不同颜色的数目，则 $X = \sum_{i=1}^m X_i$ 。于是，

$$
\begin{eqnarray*}
E(X) &=& E\left(\sum_{i=1}^m X_i \right)\\
&=& \sum_{i=1}^m E(X_i)\\
&=& \sum_{i=1}^m P(X_i = 1)\\
&=& \sum_{i=1}^m \left(1-\left(1-\frac{1}{m} \right)^{n}\right)\\
&=& m \left(1-\left(1-\frac{1}{m}\right)^{n} \right).
\end{eqnarray*}
$$

```
`````