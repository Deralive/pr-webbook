# 变量变换法
## 二维情况
设二维随机变量 $(X,Y)$ 的联合密度函数为 $p(x,y)$ ，如果函数

$$\left\{\begin{aligned}
&u=g_{1}(x, y) \\
&v=g_{2}(x, y)
\end{aligned}\right.$$

有连续偏导数，且存在唯一的反函数

$$\left\{\begin{aligned}
x=x(u, v) \\
y=y(u, v)
\end{aligned}\right.$$

其变换的雅克比行列式

$$J=\frac{\partial(x, y)}{\partial(u, v)}=\left|\begin{array}{ll}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{array}\right|=\left(\frac{\partial(u, v)}{\partial(x, y)}\right)^{-1}=\left|\begin{array}{ll}
\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
\end{array}\right|^{-1} \neq 0$$

若

$$\left\{\begin{array}{l}
U=g_{1}(X, Y) \\
V=g_{2}(X, Y)
\end{array}\right.$$

则 $(U,V)'$ 的联合密度函数为

$$p(u, v)=p(x(u, v), y(u, v)) \cdot|J|.$$

```{admonition} Remark
这个方法实际上就是二重积分的变量变换法。
```

`````{prf:example} 
:label: ex:lect9_3
设随机变量 $X$ 与 $Y$ 独立同分布，都服从正态分布 $N(\mu,\sigma^2)$ 。记

$$
\left\{\begin{aligned}
& U = X+Y\\
& V = X-Y
\end{aligned}
\right.
$$

试求 $(U,V)'$ 的联合密度函数，且问 $U$ 与 $Y$ 是否独立？
```{dropdown} Solution

因为

$$
\left\{\begin{aligned}
& u = x + y,\\
& v = x - y
\end{aligned}
\right.
$$

的反函数为

$$
\left\{\begin{aligned}
& x = \frac{u+v}{2},\\
& y = \frac{u-v}{2},
\end{aligned}
\right.
$$

则

$$
J = \left|\begin{matrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v}\\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}\\
\end{matrix}
\right|=
\left|\begin{matrix}
\frac{1}{2} & \frac{1}{2}\\
\frac{1}{2} & -\frac{1}{2}\\
\end{matrix}
\right| = -\frac{1}{2}.
$$

所以， $(U,V)'$ 的联合密度函数为

$$
\begin{eqnarray*}
p(u,v) &=& p(x(u,v),y(u,v)) |J| \\
&=& p_X\left(\frac{u+v}{2}\right)p_Y\left(\frac{u-v}{2}\right)\left|-\frac{1}{2}\right|\\
&=& \frac{1}{2\sqrt{2\pi\sigma^2}} \exp\left\{-\frac{((u+v)/2 - \mu)^2}{2}\right\} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{
-\frac{((u-v)/2-\mu)^2}{2\sigma^2}
\right\}\\
&=& \frac{1}{4\pi \sigma^2} \exp\left\{
-\frac{(u-2\mu)^2 + v^2}{4\sigma^2} \right\}\\
&=& \frac{1}{\sqrt{2\pi (2\sigma^2)}} \exp\left\{-\frac{(u-2\mu)^2}{2 \cdot (2\sigma^2)}\right\}\cdot \frac{1}{\sqrt{2\pi \cdot (2\sigma^2)}} \exp\left\{-\frac{v^2}{2 \cdot (2\sigma^2)}\right\}.
\end{eqnarray*}
$$

根据联合密度函数可知， $U\sim N(2\mu,2\sigma^2)$ ， $V\sim N(0,2\sigma^2)$ 。同时，由 $p(u,v) = p_U(u)p_V(v)$ 可知， $U$ 与 $V$ 相互独立。
```
`````

```{admonition} Remark
作为变量变换法的一种变形，**增补变量法**也是常用的方法，为求出二维随机变量 $(X,Y)$ 的函数

$$U=g(X,Y)$$

的密度函数，需要增补一个新的随机变量

$$V = h(X,Y).$$

如何增补这个随机变量是该方法中的难点，通常令 $V = X$ 或 $Y$ 可以解决大部分的问题。
其基本解法是

- 利用变量变换法求出 $(U,V)'$ 的联合密度函数 $p(u,v)$ ；
- 对 $p(u,v)$ 关于 $v$ 积分，从而得到 $U$ 的边际密度函数。

```

以下我们给出两个常用的公式，请同学们课后自行学习增补变量法后将证明过程不全。

`````{prf:example} 积的公式
设随机变量 $X$ 与 $Y$ 相互独立，其密度函数分别为 $p_X(x)$ 和 $p_{Y}(y)$ 。则 $U= XY$ 的密度函数为

$$
p_U(u) = \int_{-\infty}^{\infty} p_{X}(u/v)p_{Y}(v)\frac{1}{|v|} \text{d}v.
$$

```{dropdown} Proof
证明过程待写.
```

`````

`````{prf:example} 商的公式
设随机变量 $X$ 与 $Y$ 相互独立，其密度函数分别为 $p_X(x)$ 和 $p_{Y}(y)$ 。则 $U= X/Y$ 的密度函数为

$$
p_U(u) = \int_{-\infty}^{\infty} p_{X}(uv)p_{Y}(v)|v| \text{d}v.
$$

```{dropdown} Proof
证明过程待写.
```

`````
## $n$ 维情况（选修）
设 $n$ 维随机变量 $\boldsymbol{X}=\left(X_{1}, X_{2}, \cdots, X_{n}\right)'$ 的联合密度函数为 $p(x_1,x_2,\cdots,x_n)$ 。如果变换

$$\left\{\begin{aligned}
&y_{1}=g_{1}\left(x_{1}, x_{2}, \cdots, x_{n}\right) \\
&y_{2}=g_{2}\left(x_{1}, x_{2}, \cdots, x_{n}\right) \\
&\vdots \\
&y_{n}=g_{n}\left(x_{1}, x_{2}, \cdots, x_{n}\right)
\end{aligned} \right.$$

有连续偏导数，且存在唯一的逆变换

$$\left\{\begin{aligned}
&x_{1}=h_{1}\left(y_{1}, y_{2}, \cdots, y_{n}\right) \\
&x_{2}=h_{2}\left(y_{1}, y_{2}, \cdots, y_{n}\right) \\
&\vdots \\
&x_{n}=h_{n}\left(y_{1}, y_{2}, \cdots, y_{n}\right)
\end{aligned}\right.
$$

其变换的雅克比行列式

$$
J=\left|\frac{\partial\left(x_{1}, \cdots, x_{n}\right)}{\partial\left(y_{1}, \cdots, y_{n}\right)}\right|=\left|\left(\frac{\partial x_{i}}{\partial y_{j}}\right)\right|$$

则 

$$\mathbf{Y}=\begin{pmatrix}
Y_1\\
Y_2\\
\vdots\\
Y_n
\end{pmatrix}=
\begin{pmatrix}
g_1(X_1,X_2,\cdots,X_n)\\
g_2(X_1,X_2,\cdots,X_n)\\
\vdots\\
g_n(X_1,X_2,\cdots,X_n)
\end{pmatrix}$$

的联合密度函数为

$$p_{\mathbf{Y}}\left(\mathbf{y}\right)=p_{\mathbf{X}}\left(
g_1(\mathbf{y}),g_2(\mathbf{y}),\cdots,g_n(\mathbf{y})\right) \cdot|J|$$

`````{prf:example}
利用矩阵的技巧，我们重新来看一下例 {prf:ref}`ex:lect9_3` 。从矩阵的角度来看，

$$
\begin{pmatrix}
u\\
v
\end{pmatrix}
=\begin{pmatrix}
1& 1\\
1 & -1\\
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
$$

记

$$A = \begin{pmatrix}
1& 1\\
1 & -1\\
\end{pmatrix}$$

可以计算其逆矩阵为

$$
A^{-1} = \begin{pmatrix}
1/2 & 1/2\\
1/2 & -1/2\\
\end{pmatrix}
$$

于是，雅可比行列式为

$$
|J| = |A^{-1}| = -\frac{1}{2}.
$$

因为

$$(X,Y)'\sim N_2\left(
\begin{pmatrix}
\mu \\ \mu
\end{pmatrix},
\begin{pmatrix}
\sigma^2 & 0 \\ 0 & \sigma^2\\
\end{pmatrix}
\right),$$

其联合密度函数为

$$
\begin{eqnarray*}
p(x,y) &=& (2\pi)^{-2/2} |\sigma^2 I_2|^{-1/2}\exp\left\{-\frac{1}{2} \left(\begin{pmatrix}
x \\y
\end{pmatrix} - \begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)' (\sigma^2 I_2)^{-1}\left(\begin{pmatrix}
x \\y
\end{pmatrix} - \begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right) \right\}\\
&=& (2\pi\sigma^2)^{-1}\exp\left\{
-\frac{1}{2\sigma^2} \left(\begin{pmatrix}
x \\y
\end{pmatrix} - \begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)' \left(\begin{pmatrix}
x \\y
\end{pmatrix} - \begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)
\right\}
\end{eqnarray*}
$$

所以， $(U,V)$ 的联合密度函数为

$$
\begin{eqnarray*}
p(u,v) &=& (2\pi\sigma^2)^{-1}\exp\left\{
-\frac{1}{2\sigma^2} \left(A^{-1}\begin{pmatrix}
u \\v
\end{pmatrix} - \begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)' \left(A^{-1}\begin{pmatrix}
u \\v
\end{pmatrix} - \begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)
\right\}\cdot |J|\\
&=& (2\pi\sigma^2)^{-1}\exp\left\{
-\frac{1}{2\sigma^2} \left(\begin{pmatrix}
u \\v
\end{pmatrix} - A\begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)'(A^{-1})' (A^{-1}) \left(\begin{pmatrix}
u \\v
\end{pmatrix} - A\begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)
\right\}\cdot \frac{1}{2}\\
&=& (2\pi\sigma^2)^{-1}\exp\left\{
-\frac{1}{2\sigma^2} \left(\begin{pmatrix}
u \\v
\end{pmatrix} - A\begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)' (A I_2 A')^{-1}\left(\begin{pmatrix}
u \\v
\end{pmatrix} - A\begin{pmatrix}
\mu \\ \mu
\end{pmatrix}\right)
\right\}\cdot \frac{1}{2}\\
&=& (4\pi\sigma^2)^{-1}\exp\left\{
-\frac{1}{2} \left(\begin{pmatrix}
u \\v
\end{pmatrix} - \begin{pmatrix}
2\mu \\ 0
\end{pmatrix}\right)' \begin{pmatrix}
2\sigma^2&0\\
0 & 2\sigma^2\\
\end{pmatrix}^{-1}\left(\begin{pmatrix}
u \\v
\end{pmatrix} - \begin{pmatrix}
2\mu \\ 0
\end{pmatrix}\right)
\right\}
\end{eqnarray*}
$$

所以，

$$
\begin{pmatrix}
U\\V
\end{pmatrix}\sim N_2\left(
\begin{pmatrix}
2\mu\\0
\end{pmatrix},
\begin{pmatrix}
2\sigma^2 & 0 \\
0 & 2\sigma^2\\
\end{pmatrix}
\right)
$$

`````

若 $\mathbf{X}\sim N_{n}\left(\mathbf{\mu},\Sigma\right)$ ，对于任意常数矩阵 $A_{m,n}$ ，有 $\mathbf{Y} = A \mathbf{X} \sim N_m(A\mathbf{\mu}, A\Sigma A')$ 。