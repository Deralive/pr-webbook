# 期望向量与协方差矩阵

记 $n$ 维随机向量 $\mathbf{X}=\left(X_{1}, X_{2}, \cdots, X_{n}\right)'$ ，若其每个分量的数学期望都存在，则称

$$E(\mathbf{X})=\left(E\left(X_{1}\right), E\left(X_{2}\right), \cdots, E\left(X_{n}\right)\right)'$$

为 $n$ 维随机向量的数学期望向量，而称

$$
E(\mathbf{X}-E(\mathbf{X}))(\mathbf{X}-E(\mathbf{X}))'\\
=\left(\begin{matrix}
\text{Var}\left(X_{1}\right) & \text{Cov}\left(X_{1}, X_{2}\right) & \cdots & \text{Cov}\left(X_{1}, X_{n}\right) \\
\text{Cov}\left(X_{2}, X_{1}\right) & \text{Var}\left(X_{2}\right) & \cdots & \text{Cov}\left(X_{2}, X_{n}\right) \\
\vdots & \vdots & & \vdots \\
\text{Cov}\left(X_{n}, X_{1}\right) & \text{Cov}\left(X_{n}, X_{2}\right) & \cdots & \text{Var}\left(X_{n}\right)
\end{matrix}\right)
$$

为该随机向量的方差—协方差矩阵，记为 $\text{Cov}(\mathbf{X})$ 

``````{prf:theorem}
 $n$ 维随机向量的协方差矩阵 $\text{Cov}(\mathbf{X})=\left\{\text{Cov}\left(X_{i}, X_{j}\right)\right\}_{n\times n}$ 是一个对称非负定矩阵。
``````