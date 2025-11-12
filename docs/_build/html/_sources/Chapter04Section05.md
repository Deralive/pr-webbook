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

# 泊松分布

泊松分布
: 假定一个离散随机变量 $X$ ，其分布列为

$$
P(X=k)=\frac{\lambda ^{k} }{k!} e^{-\lambda } ,k=0,1,2,\cdots 
$$

其中，参数 $\lambda >0$ 。称随机变量 $X$ 的概率分布为泊松分布，记 $X\sim P(\lambda)$ 。


泊松分布是有法国数学家 Siméon-Denis Poisson 教授提出的。故此得名。

```{admonition} Question

为什么泊松分布是这样的？
```


``````{prf:theorem} 
:label: thm04-c
 
证明函数

$$
P(X=k)=\frac{\lambda ^{k} }{k!} e^{-\lambda } ,k=0,1,2,\cdots 
$$

是一个随机变量的分布列。

`````{admonition} Hint
:class: hint, dropdown

1. 要论证一个函数是一个随机变量的分布列，就是要证明该函数满足非负性和正则性。
2. 在这个问题的论证中，我们需要以下 {prf:ref}`lemma04-a`。

````{prf:lemma} 
:class: dropdown 
:label: lemma04-a

$$
\sum_{k=0}^{+\infty }\frac{\lambda ^{k} }{k!} = e^{\lambda }
$$

```{dropdown} Proof

令 $f(x)=e^{\lambda x}$ 可知：

\begin{eqnarray*}
f'(x)&=&\lambda e^{\lambda x}, \\ 
f''(x)&=&\lambda^{2} e^{\lambda x},\\ 
&\vdots&\\
f^{(k)}(x) &=&\lambda^{k} e^{\lambda x}.
\end{eqnarray*}

在 $x = x_0$ 处对 $f(x)$ 进行泰勒展开，可知：

$$
f(x)=f(x_{0} )+\sum_{k=1}^{\infty } \frac{f^{(k)}(x_{0} )}{k!} (x-x_{0})^{k}
$$

所以，取 $x= 1$ 且 $x_0=0$ 时，有：

$$
e^{\lambda} = f(1)=f(0 )+\sum_{k=1}^{\infty } \frac{f^{(k)}(0)}{k!} = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}
$$
```
````
`````

```{dropdown} Proof

- 要证明非负性，即 $P(X= k ) \geq 0$ 。

这是一个显然的结果 $P(X=k)=\frac{\lambda ^{k} }{k!} e^{-\lambda } > 0,k=0,1,2,\cdots$ ，这是因为参数 $\lambda>0$ 。

- 要证明正则性，即 $\sum_{k=0}^\infty P(X=k) = 1$ 。于是：

\begin{eqnarray*}
1=\sum_{k=0}^{+\infty } \frac{\lambda ^{k} }{k!} e^{-\lambda } = e^{-\lambda }\sum_{k=0}^{+\infty }\frac{\lambda ^{k} }{k!}=e^{-\lambda }e^{\lambda }
\end{eqnarray*}

根据 {prf:ref}`lemma04-a`，可知：

$$
\sum_{k=0}^{+\infty }\frac{\lambda ^{k} }{k!} = e^{\lambda }
$$
```    
``````

```{code-block} python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def prompt_positive_float(message: str) -> float:
    while True:
        try:
            value = float(input(message))
        except ValueError:
            print("请输入有效的小数。")
            continue
        if value <= 0:
            print("参数必须大于 0。")
            continue
        return value


def read_parameter():
    print("Poisson Distribution Visualizer")
    lambd = prompt_positive_float("请输入参数 λ（>0，例如 3）: ")
    return lambd


def plot_poisson_distribution(lambd: float) -> None:
    spread = lambd + 4 * np.sqrt(lambd)  # mean + 4 std covers most mass
    max_k = max(10, int(np.ceil(spread)))
    k_values = np.arange(0, max_k + 1)
    probabilities = (lambd ** k_values / factorial(k_values)) * np.exp(-lambd)

    plt.figure(figsize=(10, 6))
    plt.bar(k_values, probabilities, color="skyblue")
    plt.xlabel("Count k")
    plt.ylabel("Probability P(X = k)")
    plt.title(f"Poisson Distribution: λ={lambd}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    lambd = read_parameter()
    plot_poisson_distribution(lambd)


if __name__ == "__main__":
    main()

```

```{prf:remark} 
:label: dropdown

- 泊松分布是一种常见的离散型随机变量的分布。常用于计数数据。
- 泊松分布常常用于刻画单位时间内或单位面积上的所关心事件发生的次数。
```


```{admonition} Question

都可以表示所关心事件发生的次数，泊松分布与二项分布有什么关系？
```


```{prf:example}
:label: ex04-c

我们想要关注学校东门在每天上午 $7:00-8:00$ 这一个小时内的车流量——在这一个小时内东门通过 $K$ 辆车。 $K$ 可以看作一个泊松分布随机变量。

如果将这一个小时切分为 $n$ 个时段，并满足以下两个假定：

- $n$ 非常大，导致 $\frac{1}{n}$ 非常小，在某一个时段内**仅可通过一辆车**。
- 在各个时段内是否通过车是**互不影响**的。假设通过一辆车的概率为 $p_{n}$ 。在 $n$ 个时段中，有 $K$ 个时段中通过了一辆车，而余下的 $n-K$ 个时段中并没有通过。

由此，每一个时段内是否有车辆通过可以看作一个伯努利试验。 $K$ 也可以看作一个二项分布随机变量。这是一种直观的认知，理论解释见。
```

````{prf:theorem}
:label: thm04-d

在 $n$ 重伯努利试验中，记事件 $A$ 在一次试验中发生的概率为 $p_{n}$ （与试验次数 $n$ 有关），如果当 $n\to \infty$ 时，有 $np_{n}\to \lambda$ ，则：

$$
\lim_{n \to \infty} C_{n}^{k}p_{n} ^{k} (1-p_{n})^{n-k}=\frac{\lambda ^{k} }{k!} e^{-\lambda }
$$

```{dropdown} Proof

令 $\lambda_{n}=np_{n}$ ，即 $p_{n}=\frac{\lambda _{n}}{n}$ ，可得：

\begin{eqnarray*}
C_{n}^{k}p_{n} ^{k} (1-p_{n})^{n-k}&=&\frac{n(n-1)\cdots (n-k+1)}{k!} (\frac{\lambda _{n}}{n} )^{k}(1-\frac{\lambda _{n}}{n} )^{n-k}\\
&=&\frac{\lambda _{n}^{k}}{k!} (1-\frac{1}{n} )(1-\frac{2}{n} )\cdots (1-\frac{k-1}{n} )(1-\frac{\lambda _{n}}{n} )^{n-k}
\end{eqnarray*}

对固定的 $k$ 有：

$$
\lim_{n \to \infty} \lambda _{n}=\lambda
$$

于是有：

$$
\lim_{n \to \infty} (1-\frac{\lambda _{n}}{n})^{n-k} =e^{-\lambda }
$$

$$\lim_{n \to \infty} (1-\frac{1}{n} )\cdots (1-\frac{k-1}{n} )=1
$$

从而：

$$
\lim_{n \to \infty} C_{n}^{k}p_{n} ^{k} (1-p_{n})^{n-k}=\frac{\lambda ^{k} }{k!} e^{-\lambda }
$$

对任意 $k$ 均成立。
```
````

