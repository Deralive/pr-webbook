# 两个总体正态分布下的假设检验问题
## 方差已知时，均值差的检验

`````{prf:example}
设 $x_1,x_2,\cdots,x_m$ 来自正态总体 $N(\mu,\sigma_1^2)$ 的样本， $y_1,y_2,\cdots,y_n$ 来自正态总体 $N(\mu,\sigma_2^2)$ 的样本。两样本相互独立。我们想要检验

$$
H_0: \mu_1 \leq \mu_2 + l \quad \text{vs}\quad H_1: \mu_1 > \mu_2 + l.
$$

如果 $\sigma_1^2,\sigma_2^2$ 已知，那么求水平为 $\alpha$ 的显著性检验。
```{dropdown} Solution

令 $\theta = \mu_1- \mu_2 -l$ 。原本的假设等价于

$$
H_0: \theta \leq 0 \quad \text{vs}\quad H_1: \theta > 0.
$$

通常我们对 $\theta$ 的点估计为

$$
\hat{\theta} = \bar{x} -\bar{y} -l.
$$

在原假设 $H_0$ 下，取 $\theta = 0$ ，有

$$
\bar{x} -\bar{y}-l \sim N\left(0,\frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n} \right) .
$$

所以，经标准化后，可得检验统计量为

$$\frac{\bar{x} -\bar{y}-l}{\sqrt{\frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n}}}.$$

因此，水平为 $\alpha$ 的显著性检验的拒绝域为

$$
W = \left\{
\frac{\bar{x} -\bar{y}-l}{\sqrt{\frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n}}} \geq z_{1-\alpha}
\right\}.
$$

```
`````
## 方差未知时，均值差的检验

`````{prf:example}
设 $x_1,x_2,\cdots,x_m$ 来自正态总体 $N(\mu,\sigma_1^2)$ 的样本， $y_1,y_2,\cdots,y_n$ 来自正态总体 $N(\mu,\sigma_2^2)$ 的样本。两样本相互独立。
我们想要检验

$$
H_0: \mu_1 \leq \mu_2 + l \quad \text{vs}\quad H_1: \mu_1 > \mu_2 + l.
$$

如果 $\sigma_1^2 = \sigma_2^2 =\sigma^2$ 未知，那么求水平为 $\alpha$ 的显著性检验。
```{dropdown} Solution

令 $\theta = \mu_1- \mu_2 -l$ 。原本的假设等价于

$$
H_0: \theta \leq 0 \quad \text{vs}\quad H_1: \theta > 0.
$$

通常我们对 $\theta$ 的点估计为

$$
\hat{\theta} = \bar{x} -\bar{y} -l.
$$

在原假设 $H_0$ 下，取 $\theta = 0$ ，有

$$
\bar{x} -\bar{y}-l \sim N\left(0,\sigma^2\left(\frac{1}{m} + \frac{1}{n} \right)\right) .
$$

因为 $\sigma^2$ 是冗余参数，这里我们用和方差进行估计，即

$$
s_w^2 = \frac{(m-1)\sum_{i=1}^m (x_i -\bar{x})^2 +(n-1)\sum_{i=1}^n (y_i -\bar{b})^2 }{m+n-2}.
$$

所以，经标准化后，可得检验统计量为

$$\frac{\bar{x} -\bar{y}-l}{s_w\sqrt{\frac{1}{m} + \frac{1}{n}}} \sim t(m+n-2).$$

因此，水平为 $\alpha$ 的显著性检验的拒绝域为

$$
W = \left\{
\frac{\bar{x} -\bar{y}-l}{s_w\sqrt{\frac{1}{m} + \frac{1}{n}}} \geq t_{1-\alpha}(m+n-2)
\right\}.
$$

```
`````

```{admonition} Remark
这个检验是两样本独立 $t$ 检验。
```

## 成对数据的检验

`````{prf:example}
为了比较两种谷物种子的优劣，特选取 10 块土质不全相同的工地，并将每块分为面积相同的两部分，分别种植这两种种子，施肥与田间管理在 20 块小块土地上都是一样，表 {numref}`tab:lect22_2` 是各小块上的单位产量。
```{list-table} 成对数的数据
:header-rows: 1
:name: tab:lect22_2
* - 土地
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  - 9
  - 10
* - 种子 1 $(x)$ 
  - 23
  - 35
  - 29
  - 42
  - 39
  - 29
  - 37
  - 34
  - 35
  - 28
* - 种子 2 $(y)$ 
  - 30
  - 39
  - 35
  - 40
  - 38
  - 34
  - 36
  - 33
  - 41
  - 31
* - 差 $d=x-y$ 
  - -7
  - -4
  - -6
  - 2
  - 1
  - -5
  - 1
  - 1
  - -6
  - -3
```
假定单位产量服从等方差的正态分布，试问：两种种子的平均单位产量在显著性水平 $\alpha = 0.05$ 上有无差异差异？
```{dropdown} Solution

假定 $x_1,x_2,\cdots,x_n$ 来自正态分布 $N\left(\mu_{1}, \sigma^{2}\right)$ 和 $y_1,y_2,\cdots,y_n$ 来自正态分布 $N\left(\mu_{2}, \sigma^{2}\right)$ 且两样本独立。我们需要检验的问题为

$$
H_0: \mu_1 = \mu_2 \quad \text{vs} \quad H_1: \mu_1 \neq \mu_2.
$$

首先，我们考虑两样本独立 $t$ 检验。由于检验统计量为

$$
t_1 = \frac{\bar{x}-\bar{y}}{s_w \sqrt{1/n+1/n}} = -1.1937
$$

其中， $\bar{x}=33.1$ ， $\bar{y}=35.7$ ， $s_1^2 = 33.2111$ ， $s_y^2 = 14.2333$ ， $s_w^2 = 23.7222$ 。且 $t$ 分布的 $1-\alpha/2$ 分位数为

$$
t_{0.975}(18) = 2.1009 > |t_1|
$$

所以，无法拒绝原假设，即认为两种种子的单位产量平均值没有显著差别。
但是重新看一看数据，我们发现在同一地块上不同种子的产量的差，大于零的数的绝对值比较小，但小于零的数的绝对值比较大，这让我们认为这两种种子的产量是有差异的，但与两样本独立 $t$ 检验的结论不一致。这是因为土地之间的差异性比较大，而在比较种子时，选取了同一个地块上分别验证了两种种子的产量。基于此，我们计算其差，得到 $d_i,i=1,2,\cdots,n$ 。由于两种种子的产量均服从正态分布，其差仍服从正态分布 $N(\mu_d,\sigma_d^2)$ ， $\sigma_d^2$ 未知。我们需要检验的问题也转换为

$$
H_0: \mu_d= 0 \quad \text{vs} \quad H_1: \mu_d \neq 0
$$

因为方差未知，我们采用单样本 $t$ 检验。检验统计量为

$$
t_2 = \frac{\bar{d}}{\sqrt{s_d^2/n}} = -2.3475,
$$

而 $t$ 分布的 $1-\alpha/2$ 分位数为

$$
t_{0.975}(9) = 2.2622 < |t_2|.
$$

因此，在显著性水平为 $0.05$ 时，我们发现种子 $y$ 的产量与种子 $x$ 的产量是不同的，且种子 $y$ 的产量更高。
```
`````