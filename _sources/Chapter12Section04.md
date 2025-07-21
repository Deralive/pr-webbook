# 以概率 1 收敛（选修）

以概率 1 收敛
: 设 $\{X_n\}$ 是一列随机变量，如果

$$P\left(\lim _{n \rightarrow \infty} X_{n}=X\right)=1$$

则称序列 $\{X_n\}$ 以概率 1 收敛于 $X$ ，记 $X_{n} \stackrel{a \cdot s}{\rightarrow} X$ 。

`````{prf:property}
 $X_{n} \stackrel{a \cdot s}{\rightarrow} X \Rightarrow X_{n} \stackrel{P}{\rightarrow} X$ ，反之不然。
`````

`````{prf:example}
考虑一个离散时间的到达过程。我们假定到达的时刻属于正整数集 ${1,2,\cdots}$ 。现将这个集合分割成若干个互不相交的集合， $I_{k}=\left\{2^{k}, 2^{k}+1, \cdots, 2^{k+1}-1\right\},k=0,1,\cdots$ 。注意到集合 $I_k$ 的元素个数为 $2^k$ ，随着 $k$ 的增大而增大。具体来说，

$$
\begin{eqnarray*}
I_0 &=& \{1\}\\
I_{1}&=&\{2,3\}\\
I_{2}&=&\{4,5,6,7\}\\
\vdots
\end{eqnarray*}
$$

假设在每个区间 $I_k$ 中只有唯一的一个到达时刻，且在区间内每个时刻到达是等可能的。同时假定在各个区间到达时刻是相互独立的。

记第 $k$ 个区间 $I_k$ 内的到达时刻为 $n_k$ ，则 $n_k$ 是相互独立的随机变量序列， $k=1,2,\cdots$ 。定义一个新的随机变量序列 $\{Y_n\}$ ，如果时刻 $n$ 到达了，则定义 $Y_n = 1$ ；否则， $Y_n = 0$ 。如果 $n \in I_k$ ，则 $P(Y_n =1) = P(Y_n \neq 0) = \frac{1}{2^k}$ 。

接下来，我们来考虑随机变量序列 $\{Y_n\}$ 的收敛性。

- 因为 $I_k$ 互不相容，对于任意的 $n$ ，存在唯一 $k$ ，使得 $n \in I_k$ 。当 $n$ 越大，则 $k$ 也越大，即

$$
\lim_{n\rightarrow +\infty} P(Y_n > \varepsilon) = \lim_{n\rightarrow +\infty} \frac{1}{2^k} = 0.
$$

因此， $Y_{n} \stackrel{P}{\longrightarrow} 0$ 。
- 然而，每个区间 $I_k$ 都有到达时刻，所以，取值为 $1$ 的 $Y_n$ 的个数是无穷多次，即对于任意 $N$ ，存在 $n > N$ ，使得

$$
P(Y_n = 1) = 1
$$

因此， $P(\lim_{n \rightarrow +\infty} Y_n = 0) \neq 1$ ，即 $Y_n$ 不以概率 $1$ 收敛到 $0$ 。

`````