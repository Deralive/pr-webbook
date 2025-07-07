# 基于矩的概率不等式
``````{prf:theorem} Morkov不等式
:label: {thm:chap06_Markov_Inequality}
设 $X$ 是一个非负随机变量。如果 $a>0$ ，那么

$$P(X>a ) \leq \frac{E(X)}{a}.$$

```{dropdown} Proof
(仅考虑连续情况)设 $X$ 是一个连续随机变量，其密度函数为 $p(x)$ 。于是， $X$ 的期望是
\begin{eqnarray*}
E(X) &=& \int_{0}^{\infty} xp(x)\text{d} x \\
&=& \int_{0}^{a} xp(x)\text{d} x +\int_{a}^{\infty} xp(x)\text{d} x \\
&\geq& \int_{a}^{\infty} xp(x)\text{d} x
\\
&\geq& \int_{a}^{\infty} ap(x)\text{d} x \\
&=& a P(X\geq a)
\end{eqnarray*}
因此，定理得证，对离散随机变量亦可类似进行证明。
```

``````

``````{prf:theorem} Chebyshev不等式
:label: thm:chap06_Chebyshev_Inequality

设随机变量 $X$ 的数学期望和方差都存在，则对任意常数 $\varepsilon >0$ ,有

$$P(|x-E x| \geqslant \varepsilon) \leq \frac{\text{Var}(X)}{\varepsilon^{2}}.$$

```{dropdown} Proof
(仅考虑连续情况)其密度函数 $p(x)$ ,记 $E(x)=\mu$ ,
\begin{eqnarray*}
P(|X-\mu| \geqslant \varepsilon) &=&\int_{\{x:|x-\mu| \geqslant \varepsilon\}} p(x) d x \\
& \leqslant &\int_{\{x:|x-\mu| \geqslant \varepsilon\}} \frac{(x-\mu)^{2}}{\varepsilon^{2}} p(x) d x \\
& \leqslant& \frac{1}{\varepsilon^{2}} \int_{-\infty}^{+\infty}(x-\mu)^{2} p(x) d x \\
&=&\frac{\text{Var}(X)}{\varepsilon^{2}}.
\end{eqnarray*}
```

```{admonition} Remark
事件 ${|x-E x| \geqslant \varepsilon}$ 称为大偏差，其概率 $P(|x-E x| \geqslant \varepsilon)$ 称为大偏差发生概率。
```

``````
