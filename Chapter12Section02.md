# 依概率收敛
我们举一个例子，可以直观感受一下随机变量序列是可以收敛的。

`````{prf:example}
在抛一枚均匀硬币（正面反面出现的概率相等）的场景下，令随机变量 $X_i$ 表示 $i$ 枚硬币正面朝上的频率。考虑一次实验的数据，如表 {numref}`tab:Lect11_cointossing10_result` 。
```{list-table} 10 次抛硬币的结果
:header-rows: 1
:name: tab:Lect11_cointossing10_result
* - 第 $i$ 次抛硬币
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
* - 结果
  - 反面
  - 反面
  - 正面
  - 正面
  - 反面
  - 正面
  - 正面
  - 正面
  - 反面
  - 反面
```
于是，根据抛硬不的结果，随机变量序列 $\{X_i\}$ 的取值为 $x_i$ ，见表 {numref}`tab:Lect11_cointossing10_frequency` 
```{list-table} 随机变量序列的取值情况
:header-rows: 1
:name: tab:Lect11_cointossing10_frequency
* - $x_i$ 
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
* - 取值
  - $0$ 
  - $0$ 
  - $0.33$ 
  - $0.50$ 
  - $0.40$ 
  - $0.50$ 
  - $0.57$ 
  - $0.63$ 
  - $0.56$ 
  - $0.50$ 
```
根据表 {numref}`tab:Lect11_cointossing10_frequency` ，我们可以将 $\{X_i\}$ 绘制在一张图中，如图 {numref}`fig:Lect11_cointossing10_frequency` 。
```{figure} /fig/Lect11_Coin_Toss.png
:name: fig:Lect11_cointossing10_frequency

抛 10 枚硬币的结果
```
`````

类似地，我们分别抛 30、60、90 以及 120 次硬币后的结果，如图 {numref}`fig:Lect11_cointossing2` 所示。
```{figure} /fig/Lect11_coin_tossing2.png
:name: fig:Lect11_cointossing2

多次抛硬币的结果
```
请思考一下以下两个问题：

```{admonition} Question

- 从你运行的实验中，你发现了什么相似点？
- 这些相似的结果是否普遍存在的？

```{dropdown} Solution

由题可知，

$$P\left(\left|X_{n}\right|>\varepsilon\right)=P\left(X_{n}=n^{2}\right)=\frac{1}{n} \rightarrow 0.$$

因此， $X_{n} \stackrel{P}{\rightarrow} 0$ 。我们来计算一下 $X_n$ 的数学期望，即

$$E\left(X_{n}\right)=0 \cdot\left(1-\frac{1}{n}\right)+n^{2} \cdot \frac{1}{n}=n \rightarrow \infty. $$

因此， $E\left(X_{n}\right) \rightarrow 0$ 。
```