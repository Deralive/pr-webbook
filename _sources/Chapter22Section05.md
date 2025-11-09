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

# $p$ 值
在假设检验中，实际问题中需要考虑如何选取显著性水平 $\alpha$ 更为合适？这里我们利用一个简单的假设检验来比较在不同显著性水平的取值下的检验。

`````{prf:example} 例题续 
例题 {prf:ref}`ex:chap22_one_sample_mean_z` 续。

正态分布 $N(\mu,\sigma_0^2)$ 下， $\sigma_0^2$ 已知，我们需要检验

$$
H_0: \mu = \mu_0 \quad \text{vs} \quad H_1: \mu > \mu_0
$$

基于样本 $x_1,x_2,\cdots,x_n$ ，我们所构造的拒绝域为

$$
\{ \bar{x} \geq \mu_0 + z_{1-\alpha} \sqrt{\sigma_0^2/n} \} = \left\{ \frac{\bar{x} - \mu_0}{\sqrt{\sigma_0^2/n}} \geq z_{1-\alpha}\right\}.
$$

如果根据真实的数据，我们可以计算检验统计量 $u = 2.25$ ，那么在不同的显著性水平 $\alpha$ 下，我们得到的结论是不同的，如表 {numref}`tab:lect22_3` 。

```{list-table} 不同显著性水平下拒绝域的对比
:header-rows: 1
:name: tab:lect22_3
* - $\alpha$ 
  - $z_1-\alpha$ 
  - 结论
* - $10^-4$ 
  - $3.72$ 
  - 接受
* - $10^-3$ 
  - $3.09$ 
  - 接受
* - $0.01$ 
  - $2.33$ 
  - 接受
* - $0.025$ 
  - $1.96$ 
  - 拒绝
* - $0.05$ 
  - $1.64$ 
  - 拒绝
* - $0.1$ 
  - $1.28$ 
  - 拒绝
```

我们发现存在一个 $\tilde{\alpha}$ 值，恰好使得 $z_{1-\tilde{\alpha}} = 2.25$ ，自然 $\tilde{\alpha} = \Phi(-2.25)$ ，这就是我们定义的 $p$ 值。

`````

$p$ 值
: 在一个假设检验问题中，利用样本观测值能够作出拒绝原假设的最小显著性水平称为检验的 $p$ 值。

```{admonition} Remark
有了 $p$ 值之后，我们不需要预先设置显著性水平 $\alpha$ 的具体取值，直接反馈 $p$ 值即可。
```

根据 $p$ 值，也可以做出假设检验的结论：

- 如果 $p \leq \alpha$ ，则在显著性水平 $\alpha$ 下拒绝 $H_0$ ；
- 如果 $p>\alpha$ ，则在显著性水平 $\alpha$ 下接受 $H_0$ 。

```{thebe-button}
启动交互式环境
```

```{code-block} python3
:class: thebe
import numpy as np
from scipy.stats import norm

n = int(input("请输入样本量（一个整数 eg: 30）："))  
alpha = float(input("请输入显著性水平（一个小数 eg: 0.05）"))
num_simulations = int(input("请输入实验重复次数（一个整数 eg: 10000）："))  
method = input("请输入临界值法或p值法（eg: 临界值法）：")
reject_count = 0 
rejection_rate = 0

match method:
    case "临界值法": 
        z_critical = norm.ppf(1 - alpha / 2)  

        for _ in range(num_simulations):
            sample = np.random.normal(0, 1, n)  
            sample_mean = np.mean(sample)  
            z_statistic = sample_mean / (1 / np.sqrt(n))  
            if np.abs(z_statistic) > z_critical:  
                reject_count += 1
        # 计算拒绝原假设的频率
        rejection_rate = reject_count / num_simulations  
        print(f"通过临界值法在{num_simulations}次实验中拒绝原假设的频率: {rejection_rate}")
    
    case "p值法":
        for _ in range(num_simulations):
            sample = np.random.normal(0, 1, n)  
            sample_mean = np.mean(sample)  
            z_statistic = sample_mean / (1 / np.sqrt(n))  
            p_value = 2 * (1 - norm.cdf(np.abs(z_statistic)))  
            if p_value < alpha:  
                reject_count += 1
        # 计算拒绝原假设的频率
        rejection_rate = reject_count / num_simulations  
        print(f"通过p值法在{num_simulations}次实验中拒绝原假设的频率: {rejection_rate}")
        
print(f"显著性水平: {alpha}")
if np.abs(rejection_rate - alpha) < 0.01:  
    print("拒绝原假设的频率接近显著性水平，符合预期，说明模拟实验在一定程度上验证了假设检验的理论")
else:
    print("拒绝原假设的频率与显著性水平有差异，可能受样本量、模拟次数等因素影响，可进一步分析")
```