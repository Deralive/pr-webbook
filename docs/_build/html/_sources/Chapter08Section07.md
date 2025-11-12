---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 常见的多维随机变量的分布
## 多项分布

多项分布
: 进行 $n$ 次独立重复实验，如果每次实验有 $r$ 个互不相容的结果： $A_1,A_2,\cdots,A_r$ 之一发生，且每次是试验中 $A_i$ 发生的概率为 $p_i = P(A_i),i=1,2,\cdots,r$ ，且 $p_{1}+p_{2}+ \cdots +p_{r}=1$ 。记 $X_{i}$ 为 $n$ 次独立重复试验中 $A_{i}$ 出现的次数， $i=1,2, \cdots ,r$ ，则 $(X_{1}, X_{2}, \cdots, X_{r})$ 取值 $(x_{1}, x_{2}, \cdots, x_{r})$ 的概率，即 $A_{1}$ 出现 $x_{1}$ 次， $A_{2}$ 出现 $x_{2}$ 次, $\cdots$ , $A_{r}$ 出现 $x_{r}$ 的概率为

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


```{admonition} Remark
:class: dropdown

- 三项分布的一维边际分布为二项分布；
- 多项分布的一维边际分布为二项分布；

```
`````

## 多维超几何分布

多维超几何分布
: 袋中有 $N$ 个球，其中有 $N_i$ 个 $i$ 号球， $i=1,2,\cdots,r$ ，且 $N = N_1+N_2 + \cdots + N_r$ . 从中任意取出 $n(n\leq N)$ 个，若记 $X_i$ 为取出的 $n$ 个球中 $i$ 号球的个数， $i=1,2,\cdots,r$ ，则

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

多维均匀分布
: 设 $D$ 为 $R^n$ 中的一个有界区域，其度量为 $S_D$ 。如果多维随机变量 $(X_{1}, X_{2}, \cdots, X_{n})'$ 的联合密度函数为

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

多维正态分布
: 若 $\boldsymbol{X}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)'$ 为一个 $n$ 维随机变量，其密度函数为

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

```{code-block} python3
:class: thebe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("请输入有效的数字。")


def prompt_positive_float(message: str) -> float:
    while True:
        value = prompt_float(message)
        if value <= 0:
            print("该参数必须大于 0。")
            continue
        return value


def prompt_rho(message: str) -> float:
    while True:
        value = prompt_float(message)
        if value <= -0.99 or value >= 0.99:
            print("相关系数需要在 (-0.99, 0.99) 范围内，以避免奇异协方差矩阵。")
            continue
        return value


def read_parameters():
    print("Bivariate Normal Visualization")
    mu_x = prompt_float("请输入 μ_x（例如 0）: ")
    mu_y = prompt_float("请输入 μ_y（例如 0）: ")
    sigma_x = prompt_positive_float("请输入 σ_x（>0，例如 1）: ")
    sigma_y = prompt_positive_float("请输入 σ_y（>0，例如 1）: ")
    rho = prompt_rho("请输入相关系数 ρ（-0.99 到 0.99，例如 0）: ")
    return mu_x, mu_y, sigma_x, sigma_y, rho


def compute_bivariate_pdf(mu_x, mu_y, sigma_x, sigma_y, rho):
    span_x = max(4 * sigma_x, 6.0)
    span_y = max(4 * sigma_y, 6.0)
    x = np.linspace(mu_x - span_x, mu_x + span_x, 150)
    y = np.linspace(mu_y - span_y, mu_y + span_y, 150)
    X, Y = np.meshgrid(x, y)

    rho_sq = rho ** 2
    sigma_x_sq = sigma_x ** 2
    sigma_y_sq = sigma_y ** 2
    denom = 2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho_sq)
    diff_x = X - mu_x
    diff_y = Y - mu_y
    exponent = (
        (diff_x ** 2) / sigma_x_sq
        - 2 * rho * diff_x * diff_y / (sigma_x * sigma_y)
        + (diff_y ** 2) / sigma_y_sq
    )
    Z = np.exp(-exponent / (2 * (1 - rho_sq))) / denom
    return X, Y, Z, x, y


def plot_bivariate_normal(mu_x, mu_y, sigma_x, sigma_y, rho):
    X, Y, Z, x, y = compute_bivariate_pdf(mu_x, mu_y, sigma_x, sigma_y, rho)
    z_max = Z.max() * 1.05
    fig = plt.figure(figsize=(14, 6))

    # 3D surface
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    ax1.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.85, rstride=2, cstride=2)
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Density")
    ax1.set_title(f"Joint PDF (μx={mu_x}, μy={mu_y})")
    ax1.set_xlim(x.min(), x.max())
    ax1.set_ylim(y.min(), y.max())
    ax1.set_zlim(0, z_max)
    ax1.view_init(elev=30, azim=45)

    # Contour
    ax2 = fig.add_subplot(1, 2, 2)
    contour = ax2.contour(X, Y, Z, 12, cmap=cm.viridis)
    ax2.clabel(contour, inline=True, fontsize=8)
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.set_title(f"Contours (ρ={rho}, σx={sigma_x}, σy={sigma_y})")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def main():
    params = read_parameters()
    plot_bivariate_normal(*params)


if __name__ == "__main__":
    main()

```

```{code-block} python3
:class: thebe
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal
from matplotlib import cm


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("请输入有效的数字。")


def prompt_positive_float(message: str) -> float:
    while True:
        value = prompt_float(message)
        if value <= 0:
            print("该参数必须大于 0。")
            continue
        return value


def prompt_rho(message: str) -> float:
    while True:
        value = prompt_float(message)
        if -0.99 < value < 0.99:
            return value
        print("相关系数需要在 (-0.99, 0.99) 范围内。")


def read_parameters():
    print("Interactive Bivariate Normal Surface")
    mu_x = prompt_float("请输入 μ_x（例如 0）: ")
    mu_y = prompt_float("请输入 μ_y（例如 0）: ")
    sigma_x = prompt_positive_float("请输入 σ_x（>0，例如 1）: ")
    sigma_y = prompt_positive_float("请输入 σ_y（>0，例如 1）: ")
    rho = prompt_rho("请输入相关系数 ρ（-0.99 到 0.99，例如 0.5）: ")
    return mu_x, mu_y, sigma_x, sigma_y, rho


def compute_surface(mu_x, mu_y, sigma_x, sigma_y, rho):
    cov = [
        [sigma_x ** 2, rho * sigma_x * sigma_y],
        [rho * sigma_x * sigma_y, sigma_y ** 2],
    ]

    span_x = max(3 * sigma_x, 4.0)
    span_y = max(3 * sigma_y, 4.0)
    x = np.linspace(mu_x - span_x, mu_x + span_x, 150)
    y = np.linspace(mu_y - span_y, mu_y + span_y, 150)
    X, Y = np.meshgrid(x, y)
    pos = np.dstack((X, Y))
    Z = multivariate_normal.pdf(pos, mean=[mu_x, mu_y], cov=cov)
    return X, Y, Z


def plot_surface(X, Y, Z, mu_x, mu_y, sigma_x, sigma_y, rho):
    fig = plt.figure(figsize=(9, 7))
    # 使用 fig.add_subplot 配合 projection='3d' 创建 3D 坐标轴
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(
        X, Y, Z,
        cmap=cm.viridis,
        linewidth=0,
        antialiased=False,
        alpha=0.85
    )

    ax.set_title(f"3D Bivariate Normal Surface (μx={mu_x}, μy={mu_y}, ρ={rho})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Density")
    ax.view_init(elev=30, azim=45)

    plt.tight_layout()
    plt.show()


def main():
    mu_x, mu_y, sigma_x, sigma_y, rho = read_parameters()
    X, Y, Z = compute_surface(mu_x, mu_y, sigma_x, sigma_y, rho)
    plot_surface(X, Y, Z, mu_x, mu_y, sigma_x, sigma_y, rho)


if __name__ == "__main__":
    main()
```

```{code-block} python3
:class: thebe
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (needed for 3D plotting)
from scipy.stats import multivariate_normal, norm


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("请输入有效的数字。")


def prompt_positive_float(message: str) -> float:
    while True:
        value = prompt_float(message)
        if value > 0:
            return value
        print("该参数必须大于 0。")


def prompt_rho(message: str) -> float:
    while True:
        value = prompt_float(message)
        if -0.99 < value < 0.99:
            return value
        print("相关系数需要在 (-0.99, 0.99) 范围内。")


def read_parameters():
    print("Projection of Bivariate Normal onto X-Z plane (Y=0)")
    mu_x = prompt_float("请输入 μ_x（例如 0）: ")
    mu_y = prompt_float("请输入 μ_y（例如 0）: ")
    sigma_x = prompt_positive_float("请输入 σ_x（>0，例如 1）: ")
    sigma_y = prompt_positive_float("请输入 σ_y（>0，例如 1.2）: ")
    rho = prompt_rho("请输入相关系数 ρ（-0.99 到 0.99，例如 0.6）: ")
    return mu_x, mu_y, sigma_x, sigma_y, rho


def build_grid(mu_x, mu_y, sigma_x, sigma_y):
    span_x = max(4 * sigma_x, 6.0)
    span_y = max(4 * sigma_y, 6.0)
    x = np.linspace(mu_x - span_x, mu_x + span_x, 120)
    y = np.linspace(mu_y - span_y, mu_y + span_y, 120)
    X, Y = np.meshgrid(x, y)
    return x, y, X, Y


def plot_projection(mu_x, mu_y, sigma_x, sigma_y, rho):
    cov = [
        [sigma_x ** 2, rho * sigma_x * sigma_y],
        [rho * sigma_x * sigma_y, sigma_y ** 2],
    ]
    x, y, X, Y = build_grid(mu_x, mu_y, sigma_x, sigma_y)
    pos = np.dstack((X, Y))
    Z = multivariate_normal.pdf(pos, mean=[mu_x, mu_y], cov=cov)

    # Projection onto Y=mu_y plane (shift to zero-centered axis for clarity)
    y_proj = mu_y
    slice_points = np.dstack((x, np.full_like(x, y_proj)))
    z_slice = multivariate_normal.pdf(slice_points, mean=[mu_x, mu_y], cov=cov).flatten()

    # Theoretical 1D marginal over X
    x_marginal = norm.pdf(x, loc=mu_x, scale=sigma_x)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Main surface
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.7, linewidth=0, antialiased=True)

    # Projection plane (Y = mu_y)
    xx, zz = np.meshgrid(x, np.linspace(0, Z.max(), 30))
    yy = np.full_like(xx, y_proj)
    ax.plot_surface(xx, yy, zz, color="gray", alpha=0.15, shade=False)
    ax.text(
        mu_x + 3,
        y_proj,
        Z.max() * 0.8,
        "Plane Y = μ_y",
        color="gray",
    )

    # Slice curve (actual projection)
    ax.plot(
        x,
        np.full_like(x, y_proj),
        z_slice,
        "r-",
        linewidth=3,
        label="Slice at Y = μ_y",
    )

    # Theoretical marginal curve (scaled to overlay)
    scale = z_slice.max() / max(x_marginal.max(), 1e-12)
    ax.plot(
        x,
        np.full_like(x, y_proj),
        x_marginal * scale,
        "b--",
        linewidth=2,
        label="Theoretical marginal (scaled)",
    )

    # Vertical projection lines
    sample_x = np.linspace(mu_x - 3 * sigma_x, mu_x + 3 * sigma_x, 9)
    for xi in sample_x:
        z_proj = multivariate_normal.pdf([xi, y_proj], mean=[mu_x, mu_y], cov=cov)
        ax.plot([xi, xi], [y_proj, y_proj], [0, z_proj], "k--", alpha=0.3)

    ax.set_title("Projection of Bivariate Normal onto X-Z plane (Y fixed)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Density")
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(y.min(), y.max())
    ax.set_zlim(0, Z.max() * 1.1)
    ax.legend(loc="upper right")
    ax.view_init(elev=30, azim=45)
    plt.tight_layout()
    plt.show()


def main():
    params = read_parameters()
    plot_projection(*params)


if __name__ == "__main__":
    main()
```
