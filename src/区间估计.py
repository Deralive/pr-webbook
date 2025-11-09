import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams["font.family"] = ["SimHei"]  
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
plt.axhline(y=0, color='blue', linestyle='--', linewidth=1.5, label='实际均值')

plt.title(f'标准正态分布均值t估计的置信区间 (样本量: {sample_size}, 实验次数: {n_experiments}, 置信水平: {confidence_level}, 实际成功率: {success_rate:.2f}%)', fontsize=14)
plt.xlabel('实验次数', fontsize=12)
plt.ylabel('均值', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()