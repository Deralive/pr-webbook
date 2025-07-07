# 数学期望的性质
通过例 {prf:ref}`ex:chap06_discrete_rv_expectation`，我们在计算随机变量函数的期望时有统一的公式。

``````{prf:theorem}
:label: thm:chap06_expectation_rv_funciton
若随机变量 $X$ 的分布用分布列 $p(x_i)$ 或密度函数 $p(x)$ 表示，则 $X$ 的某一函数 $g(X)$ 的数学期望为

$$E(g(x))=\left\{\begin{aligned}
&\sum_{i} g\left(x_{i}\right) p\left(x_{i}\right), &\quad \text{在离散场合}, \\
&\int_{-\infty}^{+\infty} g(x) p(x) d x, &\quad \text{在连续场合}.
\end{aligned}\right.$$

``````
`````{prf:property}

- 若 $c$ 是常数，则 $E(c) = c$ ；
- 对任意常数 $a$ ，有 $E(aX) = aE(X)$ ；
- 对任意的两个函数 $g_1(x)$ 和 $g_2(x)$ ，有

$$
E(g_1(X)\pm g_2(X)) = E(g_1(X)) \pm E(g_2(X)).
$$

`````

```{admonition} Question
已知 $X$ 的期望 $E(X)$ ，如何计算 $X$ 的线性变换 $aX+b$ 的期望呢？
```

