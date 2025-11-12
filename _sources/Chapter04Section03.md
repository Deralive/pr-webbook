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

# 二项分布与二点分布

在二项分布中，伯努利试验是一个重要的概念。

两个实验独立性
: 设有两个试验 $E_1$ 和 $E_2$ 。假如试验 $E_1$ 的任一结果（事件）与试验 $E_2$ 的任一结果（事件）都是相互独立的事件，则称这两个试验相互独立的。

  $n$ 个实验独立性
: 如果 $E_1$ 的任一结果， $E_2$ 的任一结果， $\cdots$ ， $E_n$ 的任一结果都是相互独立的事件，则称试验 $E_1,E_2,\cdots,E_n$ 相互独立。

  $n$ 重独立重复试验
: 如果这 $n$ 个独立试验还是相同的，则称为 $n$ 重独立重复试验。

伯努利试验
: 如果在 $n$ 重独立重复试验中，每次试验的可能结果有两个（ $A$ 和 $\overline{A}$ ），则称这种试验为 $n$ 重伯努利试验。

```{prf:remark} 

  $n$ 次抛一枚硬币是一种典型的伯努利试验。
```

二项分布
: 假定伯努利试验中成功（事件 $A$ )概率为 $p$ 。记 $X$ 为 $n$ 重伯努利试验中成功的次数，其分布列为：

$$
P(X=k) = C_n^k p^k (1-p)^{(n-k)}, k=0,1,2,\cdots,n.
$$

称这个分布为二项分布。记 $X\sim b(n,p)$ 。

```{code-block} python3
:class: thebe
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


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


def prompt_probability(message: str) -> float:
    while True:
        try:
            value = float(input(message))
        except ValueError:
            print("请输入有效的小数。")
            continue
        if not (0 < value < 1):
            print("概率需要在 0 和 1 之间（不含端点）。")
            continue
        return value


def read_parameters():
    print("Binomial Distribution Visualizer")
    n = prompt_int("请输入试验次数 n（>=1，例如 10）: ", min_value=1)
    p = prompt_probability("请输入成功概率 p（0-1 之间，例如 0.5）: ")
    return n, p


def plot_binomial_distribution(n: int, p: float) -> None:
    k_values = np.arange(0, n + 1)
    probabilities = comb(n, k_values) * (p ** k_values) * ((1 - p) ** (n - k_values))

    plt.figure(figsize=(10, 6))
    plt.bar(k_values, probabilities, color="skyblue")
    plt.xlabel("Number of successes k")
    plt.ylabel("Probability P(X = k)")
    plt.title(f"Binomial Distribution: n={n}, p={p}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    n, p = read_parameters()
    plot_binomial_distribution(n, p)


if __name__ == "__main__":
    main()

```

二点分布
: 假定伯努利试验中成功（事件 $A$ )概率为 $p$ 。记 $X$ 为一次伯努利试验中成功的次数，其分布列为：

$$
P(X=k) = p^k (1-p)^{(1-k)} = \left\{
\begin{aligned}
 & p,& k=1\\ 
 &1-p ,& k=0.
\end{aligned}\right., k=0,1.
$$

称这个分布为二点分布（或伯努利分布）。记 $X\sim b(1,p)$ 。

```{prf:remark}

二项分布与二点分布之间的关系是很紧密的。
- 二点分布是二项分布的一种特例，即 $n=1$ ；
- 服从二项分布的随机变量可分解为 $n$ 个独立同为二点分布的随机变量之和，设 $X\sim b(n,p)$ 且：

$$
X_i \overset{\text{i.i.d}}{\sim} b(1,p),i=1,2,\cdots,n
$$

于是有 $X=\sum_{i=1}^n X_i$ 。
```










