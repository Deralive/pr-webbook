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

# 经验分布函数
经验分布函数
: 设 $x_1,x_2,\cdots,x_n$ 是取自总体分布函数 $F(x)$ 的样本，若将样本的观测值由小到大进行排列，记为 $x_{(1)}\leq x_{(2)}\leq \cdots\leq x_{(n)}$ ，则称 $x_{(1)}, x_{(2)}, \cdots, x_{(n)}$ 为**有序样本**，用有序样本定义函数

$$
F_n(x) = \left\{
\begin{aligned}
&0, &\text{当 $x<x_{(1)}$ },\\
& k/n, & \text{当 $x_{(k)}\leq x<x_{(k+1)},k=1,2,\cdots,n-1$ },\\
&1, &\text{当 $x\geq x_{(n)}$ }.
\end{aligned}
\right.
$$

则 $F_n(x)$ 是样本的**经验分布函数**。

```{admonition} Remark

- 对固定的 $x$ ， $F_n(x)$ 是样本中事件 $\{x_i\leq x\}$ 发生的频率。
- 当 $n$ 固定时， $F_n(x)$ 是样本的函数，而样本是随机变量，所以 $F_n(x)$ 也是一个随机变量。若对任意给定的实数 $x$ ，定义

$$
I_i(x) = \left\{
\begin{aligned}
& 1, & x_i \leq x,\\
& 0, & x_i > x.
\end{aligned}
\right.
$$

则经验分布函数的定义可以看出，

$$
F_n(x)= \frac{1}{n}\sum_{i=1}^n I_i(x).
$$

注意到 $I_i(x)$ 是独立同分布的随机变量，其共同分布为 $b(1,F(x))$ .
- 由伯努利大数定律可知，只要 $n$ 充分大， $F_n(x)$ 依概率收敛于 $F(x)$ .

```

比较一下分布函数 $F(x)$ 和经验分布函数 $F_n(x)$ 的区别：

- $F_{n}(x)$ 不是 $F(x)$ ；
- 但 $F_{n}(x)$ 可代表 $F(x)$ ；
- $F_{n}(x)$ 可观测到，而 $F(x)$ 不可观测到。

``````{prf:theorem} 格利文科定理
设 $x_{1},x_{2},\cdots,x_{n}$ 是取自总体分布函数为 $F(x)$ 的样本， $F_{n}(x)$ 是其经验分布函数，当 $n$ 充分大时， $F_{n}(x)$ 能充分逼近 $F(x)$ .

```{admonition} Remark
格利文科定理保证了经典统计中一切统计推断都以样本为依据。
```

``````

```{code-block} python
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["SimHei"]  
plt.rcParams["axes.unicode_minus"] = False  

sample_size = int(input("请输入样本量（一个正整数 eg: 200）："))
endl = int(input("请输入显示区间 [-a, a] 中的 a（一个正整数 eg: 4）："))

data = np.random.normal(loc=0, scale=1, size=sample_size)
sorted_data = np.sort(data)
n = len(sorted_data)
empirical_probs = np.arange(1, n+1) / n 

plt.figure(figsize=(10, 6))

# 绘制水平实线段（横向）
for i in range(n):
    if i < n - 1:
        if i == 0:
            plt.plot([sorted_data[i], sorted_data[i+1]], [empirical_probs[i], empirical_probs[i]], 'b-', linewidth=1.5, alpha=0.5, label='实际CDF')  # 水平实线
        plt.plot([sorted_data[i], sorted_data[i+1]], [empirical_probs[i], empirical_probs[i]], 'b-', linewidth=1.5, alpha=0.5) 

plt.plot([-endl, sorted_data[0]], [0, 0], 'b-', linewidth=1.5, alpha=0.5)  # 左侧水平实线
plt.plot([sorted_data[n-1], endl], [1, 1], 'b-', linewidth=1.5, alpha=0.5)  # 右侧水平实线

# 添加左空心、右实心点
for i in range(n):
    plt.scatter(sorted_data[i], empirical_probs[i], c='white', edgecolor='blue', s=10, zorder=3)  # 左侧空心点
    if i < n-1:
        plt.scatter(sorted_data[i+1], empirical_probs[i], marker='o', facecolor='blue', edgecolor='blue', s=10, zorder=3)  # 右侧实心点
plt.scatter(sorted_data[n-1], 1, c='white', edgecolor='blue', s=10, zorder=3)   # 左侧空心点
plt.scatter(sorted_data[0], 0, marker='o', facecolor='blue', edgecolor='blue', s=10, zorder=3)   # 右侧实心点

# 对比：带理论CDF的效果
from scipy import stats
x_theory = np.linspace(-endl, endl, endl*25)
cdf_theory = stats.norm.cdf(x_theory, loc=0, scale=1)
plt.plot(x_theory, cdf_theory, 'orange', label='理论CDF', linewidth=1.5, alpha=0.9)

plt.title(f'正态分布经验CDF与理论CDF对比(样本量: {sample_size})', fontsize=15)
plt.xlabel('模拟数据值', fontsize=12)
plt.ylabel('累积概率', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```
