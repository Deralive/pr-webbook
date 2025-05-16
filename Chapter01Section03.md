# 概率公理化定义

事件域
: 设 $\Omega$ 为一样本空间。  $\mathcal{F}$  为 $\Omega$ 的某些子集所组成的集合。如果 $\mathcal{F}$ 满足以下条件：
-  $\Omega \in \mathcal{F} $ ；
- 若 $A \in \mathcal{F} $  ，则 $ \overline{A} \in \mathcal{F} $ ；
- 若  $A_{n} \in \mathcal{F} ,n=1,2,\dots $  ，则可列并 $\bigcup_{i=1}^{\infty } A_{i} \in \mathcal{F}$ 。

那么，称  $\mathcal{F}$ 为样本空间 $\Omega$ 的一个事件域，又称为  $\sigma$ 域或 $\sigma$ 代数。

```{prf:example} 事件域
:label: ex01-c
在抛硬币的场景中，硬币正面朝上记为1，硬币反面朝上记为0。则样本空间为 $\Omega = \{0,1\}$ 。令

$$
\mathcal{F} = \{\emptyset, \{0\},\{1\} , \Omega \}
$$
是样本空间 $\Omega$ 的一个事件域。
```

概率
: 设 $\Omega$  的一个样本空间，且 $\mathcal{F}$ 为 $\Omega $ 的一个事件域。如果对任一事件 $A \in \mathcal{F}$ ，定义在 $\mathcal{F}$  上的一个实值函数 $P(A)$ 满足以下条件：

- **非负性公理**：若  $A \in \mathcal{F}$ ，则 $P(A)\geq 0$ ；
- **正则性公理**： $P(\Omega)=1$ ；
- **可列可加性公理**：若  $A_{1} ,A_{2} ,\dots ,A_{n} ,\dots $ 互不相容，则

$$
P \left(\bigcup_{i=1}^{\infty }A_{i}  \right)=\sum_{i=1}^{\infty } P(A_{i} )
$$

则称 $P(A)$ 为事件 $A$ 的概率，称三元素 $\{\Omega,\mathcal{F},P\}$ 为**概率空间**。

```{prf:remark} 
:label: remark1.1

- 概率的公理化定义是由俄国数学家柯尔莫格罗夫提出的；
- 概率的公理化定义没有告诉我们如何确定概率。
```

