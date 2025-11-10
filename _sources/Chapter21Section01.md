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


# 区间估计的概念
设 $x_{1},x_{2},\cdots,x_{n}$ 是样本。我们想要找到两个统计量 $\hat{\theta}_{L}=\hat{\theta}_{L}(x_{1},\cdots,x_{n})$ 和 $\hat{\theta}_{U}=\hat{\theta}_{U}(x_{1},\cdots,x_{n})$ ， $\hat{\theta}_{L}<\hat{\theta}_{U}$ 。于是，所构造的一个区间 $[\hat{\theta}_{L},\hat{\theta}_{U}]$ 为 $\theta$ 的一个区间估计。

```{admonition} Question
一个合适的区间估计应该有什么要求？
```

因为样本具有随机性，所以， $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 是一个随机区间。但待估参数 $\theta$ 是一个未知常数。我们通常要求区间 $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 盖住 $\theta$ 的概率

$$
P(\hat{\theta}_{L}\leq \theta\leq \hat{\theta}_{U})=P\left ( \left \{ \hat{\theta}_{L}\le \theta \right \}\cap \left \{ \hat{\theta}_{U}\le \theta \right \} \right )
$$

尽可能大。

置信区间
: 设 $\theta$ 是总体的一个参数，其参数空间为 $\Theta$ ， $x_1,x_2,\cdots,x_n$ 是来自该总体的样本，对给定的一个 $\alpha(0<\alpha<1)$ ，假设有两个统计量 $\hat{\theta}_L = \hat{\theta}_L(x_1,x_2,\cdots,x_n)$ 和 $\hat{\theta}_U = \hat{\theta}_U(x_1,x_2,\cdots,x_n)$ ，若对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta\le \hat{\theta}_{U}) \geq 1-\alpha
$$

则称随机区间 $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的置信区间，或简称 $\left[ \hat{\theta}_{L},\hat{\theta}_{U} \right]$ 是 $\theta$ 的 $1-\alpha$ 置信区间， $\hat{\theta}_{L}$ 和 $\hat{\theta}_{U}$ 分别称为 $\theta$ 的（双侧）置信下限和置信上限。

```{admonition} Remark

- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta\le \hat{\theta}_{U}) = 1-\alpha
$$

则称 $\left[ \hat{\theta}_{L},\hat{\theta}_{u} \right]$ 是 $\theta$ 的 $1-\alpha$ 同等置信区间；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta) \geq 1-\alpha
$$

则称 $\hat{\theta}_{L}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）置信下限；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\hat{\theta}_{L}\le \theta) = 1-\alpha
$$

则称 $\hat{\theta}_{L}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）同等置信下限；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\theta\leq \hat{\theta}_{U}) \geq 1-\alpha
$$

则称 $\hat{\theta}_{U}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）置信上限；
- 若对给定的 $\alpha(0<\alpha<1)$ ，对任意的 $\theta \in \Theta$ ，有

$$
P(\theta\leq \hat{\theta}_{U}) = 1-\alpha
$$

则称 $\hat{\theta}_{U}$ 为 $\theta$ 的置信水平为 $1-\alpha$ 的（单侧）同等置信上限；

```

```{code-block} python
:class: thebe
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams["axes.unicode_minus"] = False
np.random.seed(400)

n_experiments = int(input("请输入实验次数（一个整数 eg: 100）："))
sample_size = int(input("请输入样本量（一个整数 eg: 500）：")) 
confidence_level = float(input("请输入置信水平（一个小数 eg: 0.95）："))   
z_critical = stats.norm.ppf((1 + confidence_level) / 2)  # 临界值

success_count = 0
intervals = []
sample_means = []

for i in range(n_experiments):
    sample = np.random.normal(loc=0, scale=1, size=sample_size)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)  # 使用无偏估计
    standard_error = sample_std / np.sqrt(sample_size)
    lower_bound = sample_mean - z_critical * standard_error
    upper_bound = sample_mean + z_critical * standard_error
    is_correct = (lower_bound <= 0 <= upper_bound)
    if is_correct:
        success_count += 1
    intervals.append((lower_bound, upper_bound, is_correct))
    sample_means.append(sample_mean)

success_rate = success_count / n_experiments * 100

plt.figure(figsize=(12, 8))

# 绘制正确和错误的区间
for i, (lower, upper, is_correct) in enumerate(intervals):
    color = 'green' if is_correct else 'red'
    plt.plot([i+1, i+1], [lower, upper], color=color, linewidth=1.5)
    plt.plot(i+1, sample_means[i], 'o', color=color, markersize=3)

# 绘制真实均值线
plt.axhline(y=0, color='blue', linestyle='--', linewidth=1.5, label='Actual Mean Value')

plt.title(f'Confidence Intervals for Mean Estimation of Standard Normal Distribution \n(Sample size: {sample_size}, Number of experiments: {n_experiments}, Confidence level: {confidence_level}, Actual success rate: {success_rate:.2f}%)', fontsize=14)
plt.xlabel('Experiment number', fontsize=12)
plt.ylabel('Mean value', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
```