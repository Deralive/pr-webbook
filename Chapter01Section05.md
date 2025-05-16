# 概率的性质

除了在概率的公理化定义中的非负性、正则性和可列可加性之外，以下是概率常用的性质。这些性质都可以由概率的公理化定义推导出。

## 概率的有限可加性

````{prf:lemma} 
:label: lem1.1

如果事件 $\emptyset$ 是不可能事件，则 $P(\emptyset)=0$ 。

:::{dropdown} Proof

令 $A_1 = \Omega$ 而 $A_i = \emptyset,i=2,3,\cdots$ 。当 $i\neq j$ ， $A_i A_j = \emptyset$ ，所以所构造的 $A_1,A_2,\cdots,A_n,\cdots$ 是一列互不相容的随机事件。根据概率的公理化定义中可列可加性，我们有

\begin{eqnarray*}
 1= P(\Omega) &=& P\left( \cup_{n=1}^{\infty} A_n \right) \\
 &=& \sum_{n=1}^{\infty} P(A_n) \\
 &=& P(\Omega) + \sum_{n=2}^{\infty} P(\emptyset) \\
 &=& 1+ \sum_{n=2}^{\infty} P(\emptyset)
\end{eqnarray*}

并根据概率的公理化定义中非负性有，

$$
P(\emptyset) = 0
$$
:::
````

````{prf:theorem} 有限可加性
:label: thm1.1

 若有限个事件 $A_{1} ,A_{2} ,\dots ,A_{n} $  互不相容，则有
```{math}
P\left(\bigcup_{i=1}^{n}A_{i}  \right)=\sum_{i=1}^{n } P(A_{i} )
```

:::{dropdown} Proof
令 $A_{n+1} = A_{n+2} = \cdots = \emptyset$ 。根据概率的公理化定义中可列可加性，我们有
\begin{eqnarray*}
P\left( \cup_{k=1}^{n} A_k \right)   &=& P\left( \cup_{n=1}^{\infty} A_n \right) \\
 &=& \sum_{n=1}^{\infty} P(A_n) \\
 &=&  \sum_{k=1}^{n} P(A_k) + \sum_{k=n+1}^{\infty} P(A_k)  \\
 &=& \sum_{k=1}^{n} P(A_k)
\end{eqnarray*}
其中，最后一个等式成立是因为对于 $k\geq n+1$ ， $A_k = \emptyset$ ，所以根据{prf:ref}`lem1.1`， $P(A_k)=0$ 。
:::

````

````{prf:corollary} 
:label: cor1.1

 对任一事件A，有 $P(\overline{A} )=1-P(A)$ 。
````

## 概率的单调性

````{prf:lemma}
:label: lem1.2

若 $A\supset B$  ，则 $P(A-B)=P(A)-P(B)$ 。

:::{dropdown} Proof
当 $A\supset B$ 时， $A = B \cup (A-B)$ ，而且 $B$ 与 $A-B$ 是互不相容的。根据 {prf:ref}`thm1.1` 有

$$
P(A) = P(B) + P(A-B)
$$

所以，

$$
P(A-B)=P(A)-P(B).
$$
:::
````

````{prf:theorem} 概率的单调性
:label: thm1.2

若 $A\supset B$  ，则 $P(A)\geq P(B)$ ；

:::{dropdown} Proof
根据{prf:ref}`lem1.2`， $P(A-B) = P(A) -P(B) $ 。因为概率的非负性，所以 $P(A-B)\geq 0$ ，于是，
$$
P(A) \geq P(B).
$$ 
:::

````



## 概率的半可加性

````{prf:lemma} 
:label: lem1.3

对任意两个事件 $A,B$ ，有 $P(A-B)=P(A)-P(AB)$ 。

:::{dropdown} Proof
因为 $A = (A-B) \cup AB$ ，而且这两个事件均是互不相容的。根据{prf:ref}`thm1.1` 有

\begin{equation*}
P(A) = P(A-B) + P(AB) 
\end{equation*}

所以，

$$
P(A-B)=P(A)-P(AB).
$$
:::
````
```{prf:remark}
:label: remark1.5

{prf:ref}`lem1.3` 与 {prf:ref}`lem1.2` 的结论是类似的。注意到当 $A\supset B$ ， $AB = B$ 。{prf:ref}`lem1.2`  是 {prf:ref}`lem1.3` 的一种特例。
```

````{prf:lemma} 概率的加法公式
:label: lem1.4

对任意两个事件 $A,B$ ，有

$$P(A\cup B)=P(A)+P(B)-P(AB).$$

:::{dropdown} Proof
因为 $A\cup B = (A-B) \cup (B-A) \cup AB$ ，而且这三个事件均是互不相容的。根据 {prf:ref}`thm1.1` 有

\begin{eqnarray*}
P(A\cup B) &=& P(A-B) + P(B-A) + P(AB) \\
& = & P(A-B) + P(AB) + P(B-A) + P(AB) - P(AB)\\
&=& P(A) + P(B) - P(AB) 
\end{eqnarray*}
其中最后一个等式成立是因为 {prf:ref}`lem1.3`。因此，

$$P(A\cup B)=P(A)+P(B)-P(AB).$$
:::
````

````{prf:theorem} 概率的半可加性
:label: thm1.3

对任意两个事件 $A,B$ ，有

$$P(A\cup B)\leq P(A)+P(B).$$

:::{dropdown} Proof
根据 {prf:ref}`lem1.4` 有 $P(A\cup B)=P(A)+P(B)-P(AB)$ 。
又由于概率的非负性，有

$$P(A\cup B)\leq P(A)+P(B).$$
:::
````
````{prf:corollary} 
:label: cor1.2

对任意 $n$ 个事件 $A_{1} ,A_{2} ,\dots ,A_{n} $  ，有

$$P\left(\bigcup_{i=1}^{n}A_{i}  \right)\leq \sum_{i=1}^{n } P(A_{i} ).$$
````

```{prf:remark}
:label: remark1.6

{prf:ref}`cor1.2` 也是统计学和机器学习在理论推导时一个重要的技巧，可以通过缩放来得到**误差**的上界。
```

## 概率的连续性【选修内容】

极限事件
: 有以下两种定义方式：
-  对 $\mathcal{F}$ 中任一单调不减的事件序列 $F_{1} \subset F_{2}\subset \cdots \subset F_{n}\subset \cdots $ ，称可列并集  $\bigcup_{n=1}^{\infty } F_{n}$ 为  $\{F_{n}\}$ 的极限事件记为 $\lim_{n \to \infty} F_{n} =\bigcup_{n=1}^{\infty } F_{n}$ 。
- 对 $\mathcal{F}$ 中任一单调不增的事件序列 $E_{1} \supset E_{2}\supset \cdots \supset E_{n}\supset \cdots $ ，称可列交集  $\bigcap_{n=1}^{\infty } E_{n}$ 为  $\{E_{n}\}$ 的极限事件记为 $\lim_{n \to \infty} E_{n} =\bigcap_{n=1}^{\infty } E_{n}$ 。

上连续
: 设一个概率 $P$ 定义在 $\mathcal{F}$ 上。若概率 $P$ 对  $\mathcal{F}$ 中任一单调不增的事件序列  $\{E_{n}\}$ 均成立，即 $\lim_{n \to \infty} P(E_{n} )=P(\lim_{n \to \infty}E_{n}  )$ ，则称概率 $P$ 是上连续的。

下连续
: 设一个概率 $P$ 定义在 $\mathcal{F}$ 上。若概率 $P$ 对  $\mathcal{F}$ 中任一单调不减的事件序列  $\{F_{n}\}$ 均成立，即 $\lim_{n \to \infty} P(F_{n} )=P(\lim_{n \to \infty}F_{n}  )$ ，则称概率 $P$ 是下连续的。

````{prf:theorem} 概率的连续性
:label: thm1.4

若 $P$ 为事件域 $\mathcal{F}$ 上的概率，则 $P$ 既是下连续的又是上连续的。

:::{dropdown} Proof

先证 $P$ 的下连续性。

设  $\left \{ F_{n}  \right \} $ 是  $\mathcal{F}$ 中一个单调不减的事件序列，即

$$\lim_{n \to \infty} F_{n} =\cup_{n=1}^{\infty } F_{n}.$$

若定义  $F_{0} =\phi $ ，则

$$\cup_{i=1}^{\infty } F_{i}=\cup_{i=1}^{\infty }(F_{i}-F_{i-1}).$$

由于 $F_{i-1} \subset F_{i}$  ，显然  $\left (  F_{i}-F_{i-1}  \right ) $ 两两不相容，再由可列可加性得

\begin{eqnarray*}
   P\left(\cup_{i=1}^{\infty }F_{i}  \right)
   &=&P\left(\cup_{i=1}^{\infty }(F_{i}-F_{i-1})\right)\\
   &=&\sum_{i=1}^{\infty } P(F_{i}-F_{i-1}) \\
   &=&\lim_{n\to \infty} \sum_{i=1}^{n } P(F_{i}-F_{i-1})\\
   &=&\lim_{n\to \infty} P( \cup_{i=1}^{n}  (F_{i}-F_{i-1}  ) )\\
   &=&\lim_{n\to \infty} P( F_{n} )\\
\end{eqnarray*}

所以，概率 $P$ 的下连续性由此得证。

再证概率 $P$ 的上连续性。

设  $\left \{ E_{n}  \right \} $ 是单调不增的事件序列，则 $\left \{ \overline{E_{n} }  \right \} $ 为单调不减的事件序列，由概率的下连续性可得

\begin{eqnarray*}
   1-\lim_{n\to \infty} P(E_{n} )
   &=&\lim_{n\to \infty } (1-P(E_{n}))\\
   &=&\lim_{n\to \infty } P\left(\overline{E_{n} } \right)\\
   &=&P\left(\cup_{n=1}^{\infty } \overline{E_{n} } \right)\\
   &=&P\left(\overline{\cap_{n=1}^{\infty } E_{n} }  \right)\\
   &=&1-P\left(\cap_{n=1}^{\infty } E_{n}   \right)\\
\end{eqnarray*}

因此，

$$\lim_{n \to \infty} P(E_{n} )=P(\cap_{n=1}^{\infty } E_{n} )=P(\lim_{n \to \infty}E_{n} ).$$

这就证明了概率 $P$ 的上连续性。
:::
````

`````{admonition} Summary
:class: caution

由概率的连续性可知，**可列可加性**是概率公理化定义中最重要的一个性质。可列可加性等价于有限可加性和下连续性。
`````

