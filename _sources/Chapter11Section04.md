# 混合场合下的条件分布

`````{prf:example}
生活中，医生根据一些生理指标测量，如体温、血压等生化指标来进行医学诊断。
`````

我们简化一下这个问题。令 $A$ 是我们感兴趣的一个随机变量，而 $P(A)$ 是事件 $A$ 发生的概率。令 $Y$ 是一个连续型随机变量，并假定已知条件密度函数 $p(y|A)$ 和 $p(y|\overline{A})$ 。

```{admonition} Question
在给定 $Y$ 取值为 $y$ 时，事件 $A$ 发生的条件概率 $P(A|Y=y)$ 是什么？如何计算？
```

和连续场合下的条件分布有同一个问题，因为 $Y$ 是连续型的随机变量，所以事件 $\{Y = y\}$ 发生的概率为零。这里我们考虑 $\{y \leq Y \leq y + \delta\}$ ，其中 $\delta>0$ 。我们考虑

$$
\begin{eqnarray*}
P(A | Y= y) &\approx& P(A|y \leq Y \leq y+\delta)= \frac{P(A)P(y\leq Y\leq y+\delta | A)}{P(y \leq Y\leq y+\delta)}\\
&\approx& \frac{P(A) p(y|A)\delta}{p(y)\delta} = \frac{P(A) p(y|A)}{p(y)}
\end{eqnarray*}
$$

以上就是混合场景下条件分布的定义。由此，可以定义全概率公式和贝叶斯公式。

- 全概率公式为

$$
p_Y(y) = P(A) p(y|A) + P(\overline{A}) p(y|\overline{A}).
$$

- 贝叶斯公式为

$$
P(A|Y= y) = \frac{P(A)p(y|A)}{P(A)p(y|A) + P(\overline{A})p(y|\overline{A})}.
$$

如果已知 $P(A|Y=y)$ 后，我们也可以推导出 $p(y|A)$ ，即

$$
p(y|A) = \frac{p_Y(y) P(A|Y=y)}{P(A)} = \frac{p_Y(y) P(A|Y=y)}{\int_{-\infty}^{\infty} p_Y(y) P(A|Y=y) \text{d} y}.
$$

```{admonition} Remark
上述公式中将随机事件 $A$ 推广到离散型随机变量。
```