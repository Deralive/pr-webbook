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

