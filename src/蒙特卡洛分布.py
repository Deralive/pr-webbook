import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import matplotlib.gridspec as gridspec

plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False  

sample_sizes = np.array(input("请输入样本量集合（以逗号分隔的正整数 eg: 3, 4, 5, 6, 7, 8, 9, 10, ..., 20）：").split(","), dtype=int)
p_values = np.array(input("请输入分位数集合（以逗号分隔的小数 eg: 0.001, 0.01, 0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.975, 0.99, 0.999）：").split(","), dtype=float)
num_simulations = int(input("请输入蒙特卡洛模拟次数（一个正整数 eg: 1500）："))  
bins_num = int(input("请输入柱状图间隔数（一个正整数 eg: 50）：")) 

mean_results = np.zeros((len(p_values), len(sample_sizes)))
variance_results = np.zeros((len(p_values), len(sample_sizes)))
skewness_results = np.zeros((len(p_values), len(sample_sizes)))
kurtosis_results = np.zeros((len(p_values), len(sample_sizes)))

# 对每个样本量进行蒙特卡洛模拟
for i, n in enumerate(sample_sizes):
    means = np.zeros(num_simulations)
    variances = np.zeros(num_simulations)
    skewnesses = np.zeros(num_simulations)
    kurtosises = np.zeros(num_simulations)
    
    # 执行蒙特卡洛模拟
    for j in range(num_simulations):
        sample = np.random.normal(0, 1, n)
        means[j] = np.mean(sample)
        variances[j] = np.var(sample, ddof=1)  # 使用无偏估计
        skewnesses[j] = stats.skew(sample)
        kurtosises[j] = stats.kurtosis(sample, fisher=True)  # Fisher=True表示计算超额峰度
    
    # 计算各统计量的分位数
    for k, p in enumerate(p_values):
        mean_results[k, i] = np.quantile(means, p)
        variance_results[k, i] = np.quantile(variances, p)
        skewness_results[k, i] = np.quantile(skewnesses, p)
        kurtosis_results[k, i] = np.quantile(kurtosises, p)

fig = plt.figure(figsize=(15, 10))
gs = gridspec.GridSpec(2, 2, figure=fig)

# 绘制样本均值的分布
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(means, bins=bins_num, density=True, alpha=0.7, color='skyblue', label='样本均值分布')
x = np.linspace(min(means), max(means), 100)
ax1.plot(x, stats.norm.pdf(x, 0, 1/np.sqrt(n)), 'r-', lw=2, label=f'理论分布')
ax1.set_title(f'{n}个标准正态分布样本的样本均值的蒙特卡洛分布(蒙特卡洛模拟次数{num_simulations})')
ax1.set_xlabel('样本均值')
ax1.set_ylabel('密度')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.7)

# 绘制样本方差的分布
ax2 = fig.add_subplot(gs[0, 1])
ax2.hist(variances, bins=bins_num, density=True, alpha=0.7, color='lightgreen', label='样本方差分布')
df = n - 1
x = np.linspace(min(variances), max(variances), 100)
ax2.plot(x, stats.chi2.pdf((df*x), df) * df, 'r-', lw=2, label=f'理论分布')
ax2.set_title(f'{n}个标准正态分布样本的样本方差的蒙特卡洛分布(蒙特卡洛模拟次数{num_simulations})')
ax2.set_xlabel('样本方差')
ax2.set_ylabel('密度')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)

# 绘制样本偏度的分布
ax3 = fig.add_subplot(gs[1, 0])
ax3.hist(skewnesses, bins=bins_num, density=True, alpha=0.7, color='salmon', label='样本偏度分布')
x = np.linspace(min(skewnesses), max(skewnesses), 100)
ax3.set_title(f'{n}个标准正态分布样本的样本偏度的蒙特卡洛分布(蒙特卡洛模拟次数{num_simulations})')
ax3.set_xlabel('样本偏度')
ax3.set_ylabel('密度')
ax3.legend()
ax3.grid(True, linestyle='--', alpha=0.7)

# 绘制样本峰度的分布
ax4 = fig.add_subplot(gs[1, 1])
ax4.hist(kurtosises, bins=bins_num, density=True, alpha=0.7, color='plum', label='样本峰度分布')
x = np.linspace(min(kurtosises), max(kurtosises), 100)
ax4.set_title(f'{n}个标准正态分布样本的样本峰度的蒙特卡洛分布(蒙特卡洛模拟次数{num_simulations})')
ax4.set_xlabel('样本峰度')
ax4.set_ylabel('密度')
ax4.legend()
ax4.grid(True, linestyle='--', alpha=0.7)

plt.show()

# 创建并显示四个统计量的分位数表格
def create_quantile_table(results, statistic_name):
    df = pd.DataFrame(results, index=p_values, columns=sample_sizes)
    df.index.name = 'p'
    df.columns.name = 'n'
    print(f"\n{statistic_name}的分位数表：")
    print(df)

mean_table = create_quantile_table(mean_results, "样本均值")
variance_table = create_quantile_table(variance_results, "样本方差")
skewness_table = create_quantile_table(skewness_results, "样本偏度")
kurtosis_table = create_quantile_table(kurtosis_results, "样本峰度")