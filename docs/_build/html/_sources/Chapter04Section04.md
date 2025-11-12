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

# 几何分布与负二项分布

几何分布
: 假定伯努利试验中成功（事件 $A$ )概率为 $p$ 。记 $X$ 为伯努利试验首次成功的次数，其分布列为：

$$
P(X=k) = (1-p)^{(k-1)}p, k=1,2,\cdots.
$$
称这个分布为几何分布。记 $X\sim Ge(p)$ 。


````{prf:theorem}
:label: thm04-b

设 $X \sim Ge(p)$ ，则对任意正整数 $m$ 和 $n$ ，有：

$$
P(X>m+n|X>m)=P(X>n)
$$

```{dropdown} Proof

因为 $X$ 的概率分布列为：

$$
P(X= k) = (1-p)^{k-1} p , k=1,2,\cdots,
$$

所以，

$$
P(X>n)=\sum_{k=n+1}^{+\infty } (1-p)^{k-1} p=p\cdot \frac{(1-p)^{n} }{p} =(1-p)^{n}
$$
	
因此，对于任意正整数 $m$ 和 $n$ ，条件概率为：

$$
P(X>m+n|X>m)=\frac{P(X>m+n,X>m)}{P(X>m)} =\frac{P(X>m+n)}{P(X>m)}=\frac{(1-p)^{m+n} }{(1-p)^{m} }=(1-p)^{n}
$$
```

```{prf:remark}
:class: dropdown

在本证明中，我们使用到等比数列的求和公式。对于一个等比数列 $\{a_n\}$ ，首项为 $a_1$ ，公比为 $q$ 。
- 前 $n$ 项和 $S_n = \sum_{i=1}^n a_i = \frac{a_1 ( 1- q^n)}{(1-q)}$ ；
- 无穷项求和 $S_\infty = \sum_{i=1}^\infty a_i$ 有两种需要讨论的情况。
   - 若 $|q|<1$ ，则：
   
     $$
     S_\infty = \lim_{n\rightarrow \infty} S_n = \frac{a_1}{1-q};
     $$
     
   - 若 $|q| \geq 1$ ，则 $S_\infty$ 是发散的；
```

````

负二项分布
: 假定伯努利试验中成功（事件 $A$ )概率为 $p$ 。记 $X$ 为伯努利试验第 $r$ 次成功的次数，其分布列为：

$$
P(X=k) = C_{k-1}^{r-1} (1-p)^{(k-r)}p^{r}, k=r,r+1,r+2,\cdots.
$$

称这个分布为负二项分布。记 $X\sim Nb(r,p)$ 。

```{code-block} python3
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
    print("Negative Binomial Distribution Visualizer")
    r = prompt_int("请输入目标成功次数 r（>=1，例如 3）: ", min_value=1)
    p = prompt_probability("请输入每次成功概率 p（0-1 之间，例如 0.5）: ")
    return r, p


def plot_negative_binomial(r: int, p: float) -> None:
    mean = r / p
    std = np.sqrt(r * (1 - p)) / p
    n_max = max(r + 10, int(np.ceil(mean + 4 * std)))
    n_values = np.arange(r, n_max + 1)
    probabilities = comb(n_values - 1, r - 1) * (p ** r) * ((1 - p) ** (n_values - r))

    plt.figure(figsize=(10, 6))
    plt.bar(n_values, probabilities, color="skyblue")
    plt.xlabel("Number of trials n")
    plt.ylabel("Probability P(X = n)")
    plt.title(f"Negative Binomial Distribution: r={r}, p={p}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    r, p = read_parameters()
    plot_negative_binomial(r, p)


if __name__ == "__main__":
    main()

```

```{prf:remark}

负二项分布与几何分布之间的关系是很紧密的。
- 几何分布是负二项分布的一种特例，即 $r=1$ ；
- 负二项分布的随机变量可以分解为 $r$ 个独立同分布的几何分布随机变量之和，即如果 $X \sim Nb(r,p)$ ，

$$
X_i \overset{\text{i.i.d}}{\sim} Ge(p) ,
$$

那么， $X = \sum_{i=1}^r X_i$ 。
```



