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