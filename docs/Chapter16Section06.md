# 习题

- 设 $x_1,x_2,x_n$ 和 $y_1,y_2,\cdots,y_n$ 是两组样本观测值，且关系如下：

$$
y_i = a x_i + b, i=1,2,\cdots,n
$$

其中， $a$ 和 $b$ 为非零常数。试求：

- 样本均值 $\bar{x}$ 和 $\bar{y}$ 间的关系；
- 样本方差 $s_x^2$ 和 $s_y^2$ 间的关系。

- 设总体 $X$ 的 $3$ 阶矩存在，若 $x_1,x_2,\cdots,x_n$ 是取自该总体的简单随机样本， $\bar{x}$ 为样本均值， $s^2$ 为样本方差，试证：

$$
\text{Cov}(\bar{x},s^2) = \frac{\nu_3}{n},
$$

其中 $\nu_3 = E(x-E(x))^3$ 。
- 设 $\bar{x}_1$ 和 $\bar{x}_2$ 是从同一正态总体 $N(\mu,\sigma^2)$ 独立抽取的容量相同的两个样本均值。试确定样本容量 $n$ ，使得两样本均值的差超过 $\sigma$ 的概率不超过 $0.01$ 。
- 从指数总体 $Exp(1/\theta)$ 抽取了 $40$ 个样品，试求 $\bar{x}$ 的渐近分布。
- 设总体 $X$ 的分布函数 $F(x)$ 是连续的， $x_{(1)},x_{(2)},\cdots,x_{(n)}$ 为取自此总体的次序统计量，设 $\eta_i = F(x_{(i)})$ ，试证：

- $\eta_1 \leq \eta_2 \leq \cdots \leq \eta_n$ ， $\eta_i$ 是来自均匀分布 $U(0,1)$ 总体的次序统计量；
- $E(\eta_i) = \frac{i}{n+1}$ ， $\text{Var}(\eta_i) = \frac{i(n+1-i)}{(n+1)^2(n+2)}, 1\leq i\leq n$ ；
- $\eta_i$ 和 $\eta_j$ 的协方差矩阵为

$$
\begin{pmatrix}
\frac{a_1(1-a_1)}{n+2} & \frac{a_1(1-a_2)}{n+2}\\
\frac{a_1(1-a_2)}{n+2} & \frac{a_2(1-a_2)}{n+2}
\end{pmatrix}
$$

其中， $a_1 = \frac{i}{n+1},a_2 = \frac{j}{n+1}$ .