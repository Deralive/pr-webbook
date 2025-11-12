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

# 不同形式的大数定律

由此，我们可以给出以下不同形式的**大数定律**。它们的差异在于对于随机变量序列 $\{X_n\}$ 的假设条件不同。

## 切比雪夫大数定律

在伯努利大数定律中，要求每个随机变量是独立同分布，且该分布是伯努利分布。为了放松**独立同分布**这一条件，我们有以下这个定理。

``````{prf:theorem} 切比雪夫大数定律
设 $\left \{ X_{n} \right \}$ 为一列两两不相关的随机变量序列。若每个 $X_{i}$ 的方差存在，且有共同的上界，即

$$\text{Var}(X_{i})\leq c, \quad
i=1,2,\cdots.$$

则 $\left \{ X_{n} \right \}$ 服从（弱）大数定律。
```{dropdown} Proof
因为 $\{X_n\}$ 两两不相关，故

$$
\text{Var}\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2}\sum_{i=1}^n \text{Var}(X_i) \leq \frac{c}{n}.
$$

根据切比雪夫不等式可知，对任意的 $\varepsilon > 0$ ，有

$$
P\left(\left| \frac{1}{n}\sum_{i=1}^n X_i - \frac{1}{n} \sum_{i=1}^n E(X_i) \right| < \varepsilon \right)\geq 1-\frac{\text{Var}\left(\frac{1}{n}\sum_{i=1}^n X_i\right)}{\varepsilon^2} \geq 1-\frac{c}{n\varepsilon^2}.
$$

于是，当 $n\rightarrow \infty$ 时，有

$$
\lim_{n\rightarrow \infty} P\left(\left| \frac{1}{n}\sum_{i=1}^n X_i - \frac{1}{n} \sum_{i=1}^n E(X_i) \right| < \varepsilon \right) = 1.
$$

```

```{admonition} Remark
:class: dropdown
切比雪夫大数定律只要求 $\left \{ X_{n} \right \}$ 互不相关，并不要求 $X_n$ 是独立的，也不要求它们是同分布的。因此，如果 ${X_{n}}$ 是独立同分布的随机变量序列且方差有限，则 $\left \{ X_{n} \right \}$ 必定服从大数定律。这表明了伯努利大数定律是切比雪夫大数定律的一个特例。
```

``````

## 马尔可夫大数定律
在切比雪夫大数定律证明的过程中，我们不难发现，其核心在于使用了切比雪夫不等式。而切比雪夫不等式本质上证明的是大偏差存在的概率可以被其方差所约束。因此，我们只需要要求这些随机变量的算术平均数的方差不能过大。

在切比雪夫大数定律中要求了随机变量序列中两两不相关，这样可以使得随机变量的算术平均数的方差可以由每一个随机变量的方差计算而得。切比雪夫大数定律中又约束了每一个随机变量的方差存在且存在共同上界。由此，解决了随机变量的算术平均数的方差不能过大的问题。

事实上，切比雪夫大数定律的条件仍是比较严苛的，因为随机变量序列中仍需要它们是两两不相关的。但，这个条件并不是必要的。于是，我们考虑以下这个定理。

``````{prf:theorem} 马尔可夫大数定律
对随机变量序列 $\left \{ X_{n} \right \}$ ，若马尔可夫条件即

$$
\text{Var}\left(\frac{1}{n}\sum_{i=1}^{n}X_{i} \right)=\frac{1}{n^{2}} \text{Var}\left(\sum_{i=1}^{n}X_{i} \right)\rightarrow 0$$

满足，则 $\left \{ X_{n} \right \}$ 服从（弱）大数定律。
``````

```{admonition} Remark
马尔可夫大数定律对 $\left \{ X_{n} \right \}$ 已经没有同分布、独立性、不相关的假定。
```

```{dropdown} Proof
本定理的证明过程由学生课后自行补充
```

## 辛钦大数定律
之前我们介绍的大数定律都假定了随机变量序列 $\{X_n\}$ 的方差存在。而我们也知道，对于一个随机变量而言，如果它的方差是存在的，那么它的期望一定是存在的。但反之不然。在大数定律的一般形式中，并未涉及随机变量序列的方差。所以，在随机变量序列的方差不存在的情况下，大数定律仍可以存在。

``````{prf:theorem} 辛钦大数定律
设 $\left \{ X_{n} \right \}$ 为一独立同分布的随机变量序列，若 $X_{i}$ 的数学期望存在，则 $\left \{ X_{n} \right \}$ 服从（弱）大数定律。

```{admonition} Remark
:class: dropdown

- 在辛钦大数定律中，可以放松对随机变量方差存在性的假定，但要求 $\left \{ X_{n} \right \}$ 为独立同分布的随机变量序列。
- 因为 $\left \{ X_{n} \right \}$ 是同分布的随机变量序列，所以

$$E(X)=\frac{1}{n}\sum_{i=1}^{n}E(X_{i}) $$

因此，从另一角度来看辛钦大数定律，可以计算一个随机变量期望 $E(X)$ 的近似值：对随机变量 $X$ 有 $n$ 次独立重复地观测，记第 $k$ 次观测值为 $X_{k}$ 。则 $X_{1},X_{2},\cdots,X_{n}$ 是相互独立的，且它们的分布应该与 $X$ 的分布相同。于是，在 $E(X)$ 存在的条件下，按照辛钦大数定律，当 $n$ 足够大时，可以把这些观测的平均值

$$\frac{1}{n}\sum_{i=1}^{n}X_{i}$$

作为 $E(X)$ 的近似值。
- 类似的方法也可以推广到计算随机变量的 $k$ 阶原点矩的近似值。

```

``````

```{code-block} python3
import numpy as np
import matplotlib.pyplot as plt


def prompt_int(message: str, *, min_value: int = None, max_value: int = None) -> int:
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("请输入有效的整数。")
            continue
        if min_value is not None and value < min_value:
            print(f"数值必须 >= {min_value}。")
            continue
        if max_value is not None and value > max_value:
            print(f"数值必须 <= {max_value}。")
            continue
        return value


def read_parameters():
    print("Monte Carlo Integration (Hit-or-Miss vs Mean)")
    n_samples = prompt_int("请输入样本数量 n（>=10，例如 500）: ", min_value=10)
    seed = prompt_int("请输入随机种子（>=0，例如 42）: ", min_value=0)
    return n_samples, seed


def monte_carlo_comparison(n_samples: int, seed: int) -> None:
    a, b = 0.0, 1.0
    exact_value = np.e - 1.0
    rng = np.random.default_rng(seed)

    x_samples = rng.uniform(a, b, n_samples)
    y_samples = rng.uniform(0.0, np.e, n_samples)
    fx_samples = np.exp(x_samples)
    hit_mask = y_samples <= fx_samples

    hit_estimate = (b - a) * np.e * hit_mask.mean()
    mean_estimate = (b - a) * fx_samples.mean()
    hit_error = abs(hit_estimate - exact_value)
    mean_error = abs(mean_estimate - exact_value)

    x_fine = np.linspace(a, b, 400)
    fx_fine = np.exp(x_fine)

    fig, (ax_hit, ax_mean) = plt.subplots(1, 2, figsize=(12, 5))

    # Hit-or-miss (area sampling)
    ax_hit.plot(x_fine, fx_fine, color="black", linewidth=2, label="f(x) = e^x")
    ax_hit.fill_between(x_fine, fx_fine, color="steelblue", alpha=0.25, label=f"Exact area = {exact_value:.4f}")
    ax_hit.scatter(x_samples[hit_mask], y_samples[hit_mask], color="green", s=15, alpha=0.7, label=f"Hits: {hit_mask.sum()}")
    ax_hit.scatter(x_samples[~hit_mask], y_samples[~hit_mask], color="red", s=15, alpha=0.5,
                   label=f"Misses: {n_samples - hit_mask.sum()}")
    ax_hit.set_xlim(a, b)
    ax_hit.set_ylim(0.0, np.e)
    ax_hit.set_xlabel("x")
    ax_hit.set_ylabel("y")
    ax_hit.set_title(f"Hit-or-Miss Method (n={n_samples})")
    ax_hit.grid(alpha=0.25)
    ax_hit.legend(loc="upper left", fontsize=9)
    ax_hit.text(
        0.02,
        0.02,
        f"Estimate = {hit_estimate:.6f}\n"
        f"Exact = {exact_value:.6f}\n"
        f"Abs. error = {hit_error:.6f}\n"
        f"Rel. error = {hit_error / exact_value * 100:.2f}%",
        transform=ax_hit.transAxes,
        bbox=dict(facecolor="white", alpha=0.85),
        fontsize=9,
    )

    # Mean value method
    ax_mean.plot(x_fine, fx_fine, color="black", linewidth=2, label="f(x) = e^x")
    ax_mean.scatter(x_samples, fx_samples, color="purple", s=15, alpha=0.6, label="Sampled f(x)")
    mean_level = fx_samples.mean()
    ax_mean.axhline(mean_level, color="tomato", linestyle="--", linewidth=2, label=f"Sample mean = {mean_level:.4f}")
    ax_mean.fill_between([a, b], mean_level, color="tomato", alpha=0.25,
                         label=f"Approx. area = {mean_estimate:.4f}")
    ax_mean.set_xlim(a, b)
    ax_mean.set_ylim(0.0, np.e)
    ax_mean.set_xlabel("x")
    ax_mean.set_ylabel("f(x)")
    ax_mean.set_title(f"Mean Value Method (n={n_samples})")
    ax_mean.grid(alpha=0.25)
    ax_mean.legend(loc="upper left", fontsize=9)
    ax_mean.text(
        0.02,
        0.02,
        f"Estimate = {mean_estimate:.6f}\n"
        f"Exact = {exact_value:.6f}\n"
        f"Abs. error = {mean_error:.6f}\n"
        f"Rel. error = {mean_error / exact_value * 100:.2f}%",
        transform=ax_mean.transAxes,
        bbox=dict(facecolor="white", alpha=0.85),
        fontsize=9,
    )

    fig.suptitle("Comparison of Two Monte Carlo Integration Methods", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()

    print("----- Numerical Summary -----")
    print(f"Hit-or-miss estimate : {hit_estimate:.6f} (abs error = {hit_error:.6f})")
    print(f"Mean-value estimate  : {mean_estimate:.6f} (abs error = {mean_error:.6f})")
    print(f"Exact integral value : {exact_value:.6f}")


def main():
    n_samples, seed = read_parameters()
    monte_carlo_comparison(n_samples, seed)


if __name__ == "__main__":
    main()

```

```{code-block} python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def prompt_int(message: str, *, min_value: int = None, max_value: int = None) -> int:
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("请输入有效的整数。")
            continue
        if min_value is not None and value < min_value:
            print(f"数值必须 >= {min_value}。")
            continue
        if max_value is not None and value > max_value:
            print(f"数值必须 <= {max_value}。")
            continue
        return value


def read_parameters():
    print("Step-by-step Monte Carlo Integration Demo")
    n_samples = prompt_int("请输入样本数量 n（50-2000，例如 200）: ", min_value=50, max_value=2000)
    seed = prompt_int("请输入随机种子（>=0，例如 7）: ", min_value=0)
    interval = prompt_int("请输入帧间隔毫秒（>=20，例如 80）: ", min_value=20)
    return n_samples, seed, interval


class MonteCarloAnimator:
    def __init__(self, n_samples: int, seed: int, interval_ms: int):
        self.a, self.b = 0.0, 1.0
        self.n_samples = n_samples
        self.interval_ms = interval_ms
        self.exact_value = np.e - 1.0
        self.rng = np.random.default_rng(seed)
        self.x_samples = self.rng.uniform(self.a, self.b, n_samples)
        self.y_samples = self.rng.uniform(0.0, np.e, n_samples)
        self.fx_samples = np.exp(self.x_samples)

        self.x_fine = np.linspace(self.a, self.b, 400)
        self.fx_fine = np.exp(self.x_fine)

        self.fig, (self.ax_hit, self.ax_mean) = plt.subplots(1, 2, figsize=(12, 5))
        self._setup_axes()

        self.hit_scatter = self.ax_hit.scatter([], [], color="green", s=25, alpha=0.7, label="Hits")
        self.miss_scatter = self.ax_hit.scatter([], [], color="red", s=25, alpha=0.5, label="Misses")
        self.sample_scatter = self.ax_mean.scatter([], [], color="purple", s=30, alpha=0.7, label="Samples")
        (self.mean_line,) = self.ax_mean.plot([], [], "tomato", linestyle="--", linewidth=2, label="Current mean")

        self.hit_text = self.ax_hit.text(
            0.02,
            0.98,
            "",
            transform=self.ax_hit.transAxes,
            va="top",
            bbox=dict(facecolor="white", alpha=0.85),
        )
        self.mean_text = self.ax_mean.text(
            0.02,
            0.98,
            "",
            transform=self.ax_mean.transAxes,
            va="top",
            bbox=dict(facecolor="white", alpha=0.85),
        )

        self.ax_hit.legend(loc="lower right")
        self.ax_mean.legend(loc="lower right")
        self.fig.suptitle("Incremental Estimates: Hit-or-Miss vs Mean Value", fontsize=14)
        self.fig.tight_layout(rect=[0, 0, 1, 0.96])

    def _setup_axes(self):
        # Hit-or-miss panel
        self.ax_hit.plot(self.x_fine, self.fx_fine, color="black", linewidth=2, label="f(x) = e^x")
        self.ax_hit.fill_between(self.x_fine, self.fx_fine, color="steelblue", alpha=0.2)
        self.ax_hit.set_xlim(self.a, self.b)
        self.ax_hit.set_ylim(0.0, np.e)
        self.ax_hit.set_xlabel("x")
        self.ax_hit.set_ylabel("y")
        self.ax_hit.set_title("Hit-or-Miss method")
        self.ax_hit.grid(alpha=0.3)

        # Mean method panel
        self.ax_mean.plot(self.x_fine, self.fx_fine, color="black", linewidth=2, label="f(x) = e^x")
        self.ax_mean.set_xlim(self.a, self.b)
        self.ax_mean.set_ylim(0.0, np.e)
        self.ax_mean.set_xlabel("x")
        self.ax_mean.set_ylabel("f(x)")
        self.ax_mean.set_title("Mean value method")
        self.ax_mean.grid(alpha=0.3)

    def init_artists(self):
        empty = np.empty((0, 2))
        self.hit_scatter.set_offsets(empty)
        self.miss_scatter.set_offsets(empty)
        self.sample_scatter.set_offsets(empty)
        self.mean_line.set_data([], [])
        self.hit_text.set_text("")
        self.mean_text.set_text("")
        return (
            self.hit_scatter,
            self.miss_scatter,
            self.sample_scatter,
            self.mean_line,
            self.hit_text,
            self.mean_text,
        )

    def update(self, frame: int):
        count = frame + 1
        x_current = self.x_samples[:count]
        y_current = self.y_samples[:count]
        fx_current = self.fx_samples[:count]
        hit_mask = y_current <= fx_current

        self.hit_scatter.set_offsets(np.column_stack((x_current[hit_mask], y_current[hit_mask])))
        self.miss_scatter.set_offsets(np.column_stack((x_current[~hit_mask], y_current[~hit_mask])))

        hit_estimate = (self.b - self.a) * np.e * hit_mask.mean()
        hit_error = abs(hit_estimate - self.exact_value)
        self.hit_text.set_text(
            f"Samples: {count}\n"
            f"Hits: {hit_mask.sum()}\n"
            f"Estimate = {hit_estimate:.6f}\n"
            f"Abs. error = {hit_error:.6f}"
        )

        self.sample_scatter.set_offsets(np.column_stack((x_current, fx_current)))
        mean_level = fx_current.mean()
        self.mean_line.set_data([self.a, self.b], [mean_level, mean_level])
        mean_estimate = (self.b - self.a) * mean_level
        mean_error = abs(mean_estimate - self.exact_value)
        self.mean_text.set_text(
            f"Samples: {count}\n"
            f"Mean f(x) = {mean_level:.5f}\n"
            f"Estimate = {mean_estimate:.6f}\n"
            f"Abs. error = {mean_error:.6f}"
        )

        return (
            self.hit_scatter,
            self.miss_scatter,
            self.sample_scatter,
            self.mean_line,
            self.hit_text,
            self.mean_text,
        )

    def run(self):
        # Keep a reference to the animation object to prevent garbage collection.
        self.ani = FuncAnimation(
            self.fig,
            self.update,
            frames=self.n_samples,
            init_func=self.init_artists,
            interval=self.interval_ms,
            blit=False,
            repeat=False,
        )
        plt.show()


def main():
    n_samples, seed, interval = read_parameters()
    animator = MonteCarloAnimator(n_samples, seed, interval)
    animator.run()


if __name__ == "__main__":
    main()

```