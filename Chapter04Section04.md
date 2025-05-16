# 几何分布与负二项分布

几何分布
: 假定伯努利试验中成功（事件 $A$ )概率为 $p$ 。记 $X$ 为伯努利试验首次成功的次数，其分布列为

$$
P(X=k) =   (1-p)^{(k-1)}p, k=1,2,\cdots.
$$
称这个分布为几何分布。记 $X\sim Ge(p)$ 。


````{prf:theorem}
:label: thm04-b

设 $X \sim Ge(p)$ ，则对任意正整数 $m$ 和 $n$ ，有  

$$
P(X>m+n|X>m)=P(X>n).
$$

```{dropdown} Proof

因为 $X$ 的概率分布列为

$$
P(X= k) = (1-p)^{k-1} p , k=1,2,\cdots,
$$

所以，

$$
P(X>n)=\sum_{k=n+1}^{+\infty } (1-p)^{k-1} p=p\cdot \frac{(1-p)^{n} }{p} =(1-p)^{n}. 
$$
	
因此，对于任意正整数 $m$ 和 $n$ ，条件概率为

$$
P(X>m+n|X>m)=\frac{P(X>m+n,X>m)}{P(X>m)} =\frac{P(X>m+n)}{P(X>m)}=\frac{(1-p)^{m+n} }{(1-p)^{m} }=(1-p)^{n}.
$$
```

```{prf:remark}
:class: dropdown

在本证明中，我们使用到等比数列的求和公式。对于一个等比数列 $\{a_n\}$ ，首项为 $a_1$ ，公比为 $q$ 。
- 前 $n$ 项和 $S_n = \sum_{i=1}^n a_i =  \frac{a_1 ( 1- q^n)}{(1-q)}$ ；
- 无穷项求和 $S_\infty = \sum_{i=1}^\infty a_i$ 有两种需要讨论的情况。
   - 若 $|q|<1$ ，则
   
     $$
     S_\infty = \lim_{n\rightarrow \infty} S_n = \frac{a_1}{1-q};
     $$
   - 若 $|q| \geq 1$ ，则 $S_\infty$ 是发散的；
```

````

负二项分布
: 假定伯努利试验中成功（事件 $A$ )概率为 $p$ 。记 $X$ 为伯努利试验第 $r$ 次成功的次数，其分布列为

$$
P(X=k) =   C_{k-1}^{r-1} (1-p)^{(k-r)}p^{r}, k=r,r+1,r+2,\cdots.
$$

称这个分布为负二项分布。记 $X\sim Nb(r,p)$ 。


```{prf:remark}

负二项分布与几何分布之间的关系是很紧密的。
- 几何分布是负二项分布的一种特例，即 $r=1$ ；
- 负二项分布的随机变量可以分解为 $r$ 个独立同分布的几何分布随机变量之和，即如果 $X \sim Nb(r,p)$ ，

$$
X_i \overset{\text{i.i.d}}{\sim} Ge(p) ,
$$

那么，  $X = \sum_{i=1}^r X_i$ 。
```



