# 独立性

## 两个事件间的独立性
```{prf:example} 有回放机制 VS 无回放机制
:label: ex02-h

假设罐子里有$r$个红球，有$b$个黑球。令$R_1$为事件“第一个人抽到红球”，$R_2$为事件“第二个人抽到红球”。

在**有回放**机制下，“第二个人是否能够抽到红球”不受到“第一个人是否抽到红球”结果的影响。于是，
\begin{eqnarray*}
    P(R_1) &=& \frac{r}{r+b}\\
    P(R_2) &=& \frac{r}{r+b}\\
    P(R_1R_2) &=& \frac{r^2}{(r+b)^2} = \frac{r}{r+b} \cdot \frac{r}{r+b}  = P(R_1)\cdot P(R_2). 
\end{eqnarray*}

在**无回放**机制下，“第二个人是否能够抽到红球”会受到“第一个人是否抽到红球”结果的影响。
\begin{eqnarray*}
    P(R_1) &=& \frac{r}{r+b}\\
    P(R_2) &=& P(R_1) P(R_2|R_1) + P(\overline{R_1}) P(R_2|\overline{R_1}) \\
    & = & \frac{r}{r+b} \cdot \frac{r-1}{r+b-1} + \frac{b}{r+b}\cdot \frac{r}{r+b-1} = \frac{r}{r+b}\\
    P(R_1R_2) &=& \frac{C_r^2}{C_{r+b}^2} = \frac{r!/(2!(r-2)!)}{(r+b)!/(2!(r+b-2)!)} = \frac{r(r-1)}{(r+b)(r+b-1)}\neq P(R_1)\cdot P(R_2). 
\end{eqnarray*}
```

独立性
: 如果

$$P(AB) = P(A)P(B)$$
   
   成立，则称事件$A$与$B$相互独立，简称$A$与$B$独立。否则，称$A$与$B$不独立或相依。

````{prf:theorem}
:label: thm02-f

若事件$A$与$B$独立，则$A$与$\overline{B}$独立。
```{dropdown} Proof

由于概率的性质可知，

$$
P(A\overline{B}) = P(A) - P(AB) = P(A)- P(A)P(B) = P(A)(1-P(B)) = P(A)P(\overline{B}).
$$
    
于是，性质得证。
```
````

```{prf:corollary}
:label: cor02-a

若事件$A$与$B$独立，则
- $\overline{A}$与$B$独立；
- $\overline{A}$与$\overline{B}$独立。
```

## 三个事件间的独立性

两两独立
: 设有三个事件$A,B,C$。如果
    \begin{equation*}
        \left\{
        \begin{aligned}
       &    P(AB)=P(A)P(B)\\
       & P(AC)=P(A)P(C)\\
       & P(BC)=P(B)P(C)
        \end{aligned}
        \right.
    \end{equation*}
则称$A,B,C$两两独立。

相互独立
: 设有三个事件$A,B,C$两两独立且
    \begin{equation*}
P(ABC)=P(A)P(B)P(C)    
    \end{equation*}
 则称$A,B,C$相互独立。
 
 ```{prf:remark}
 
 三个事件$A,B,C$两两独立无法推导出$P(ABC)=P(A)P(B)P(C)$；反之也不成立。以下给出两个反例，供参考。
 ```
 
```{prf:example}
 :label: ex02-i
 
 设又一个均匀的正四面体，其第一面染成红色，第二面染成白色，第三面染成黑色，而第四面染成有红、白、黑三种颜色。现在以$A,B,C$分别记为投一次四面体出现红、白、黑颜色的事件，则由于四面体种有两面染有红色，因此，$P(A)= P(B) = P(C) = 1/2$。另外，容易算出
        
$$
P(AB) = P(BC) = P(AC)=1/4.
$$
        
所以，$A,B,C$两两独立。但是，
        
$$
P(ABC) = 1/4 \neq 1/8 = P(A)P(B)P(C).
$$
        
因而，$A,B,C$不相互独立。
 ```

```{prf:example}
 :label: ex02-j
 
 由一个均匀正八面体，其第一、二、三、四面染上红色；第一、二、三、五面染上白色，第一、六、七、八面染上黑色。令$A = \{\text{抛一次正八面体，朝下的一面出现红色}\}$，$B = \{\text{抛一次正八面体，朝下的一面出现白色}\}$，$C = \{\text{抛一次正八面体，朝下的一面出现黑色}\}$。
 
 则
 
 \begin{eqnarray*}
 P(A) &=& P(B) = P(C) = \frac{4}{8} = \frac{1}{2}.\\
 P(ABC) = \frac{1}{8} = P(A) P(B) P(C).
 \end{eqnarray*}
 
 但是，
 
 $$
 P(AB) = \frac{3}{8} \neq P(A) P(B).
 $$
 
 所以，事件$A,B,C$不两两独立。
  ```

````{prf:theorem}
:label: thm02-g

设$A,B,C$三个事件相互独立，那么事件$A\cup B$与$C$相互独立。

```{dropdown} Proof

 因为$P(A\cup B) C = AC \cup BC$. 所以，
    \begin{eqnarray*}
        P((A\cup B)C) &=& P(AC \cup BC) \\
        &=& P(AC) + P(BC) - P(AC \cap BC)\\
        &=& P(A)P(C) + P(B)P(C) - P(A)P(B)P(C)\\
        &=& \left(P(A) + P(B) -P(A)P(B)\right)\cdot P(C)\\
        &=& P(A\cup B) P(C).
    \end{eqnarray*}
    因此，$A\cup B$与$C$相互独立。
```
````

## $n$个事件的独立性

$n$个事件的独立性
: 设有$n$个事件$A_1,A_2,\cdots,A_n$，对任意的$1\leq i<j<k<\cdots\leq n $，如果
    \begin{equation*}
        \left\{
        \begin{aligned}
       &    P(A_iA_j) = P(A_i)P(A_j)\\
       & P(A_iA_jA_k) = P(A_i)P(A_j)P(A_k)\\
       &\vdots\\
       & P(A_1A_2\cdots A_n) = \prod_{i=1}^n P(A_i) 
        \end{aligned}
        \right.
    \end{equation*}
    则称此$n$个事件$A_1,A_2,\cdots,A_n$相互独立。

##  条件独立性

条件独立性
: 设有三个事件$A,B,C$，且$P(C)>0$。如果
    $$
    P(AB|C) = P(A|C) P(B|C)
    $$
    则称在给定事件$C$,$A$与$B$是条件独立的。
    
    
```{prf:remark}

- 若$P(B\cap C)>0$, 给定$C$，$A$与$B$是条件独立的等价于$P(A|B\cap C) = P(A|C)$.
- 独立性无法推导出条件独立性；反之亦然。
```

```{prf:example}
:label: ex02-k

考虑独立地投掷两枚公平的硬币，即所有结果都是等可能的。令

\begin{eqnarray*}
H_1 &=& \{\text{第一枚硬币正面}\}\\
H_2 &=& \{\text{第二枚硬币正面}\}\\
 D &=&  \{\text{两枚硬币的结果不一致}\}
\end{eqnarray*}
    
于是，$H_1$和$H_2$是独立的。但是，
    
$$
P(H_1|D) = \frac{1}{2},\quad P(H_2|D) = \frac{1}{2},\quad P(H_1\cap H_2|D) =0.
$$
    
所以，$P(H_1\cap H_2|D) \neq P(H_1|D) P(H_2|D)$。这意味着$H_1$和$H_2$不是条件独立的。
```

```{prf:example}
:label: ex02-l

有两枚硬币，一红一蓝。我们从中等概率地随机选择一枚，并独立地进行两次投掷。假定这两枚硬币是有偏的。蓝色的硬币正面朝上的概率为0.99，而红色的硬币正面朝上的概率为0.01.

令$B$为事件“蓝色的硬币被选中”，$H_i$为事件“第$i$次投掷的结果为正面朝上”。在选定硬币后，$H_1$和$H_2$是独立的。于是，
    
$$
 P(H_1 \cap H_2 | B) = P(H_1|B) P(H_2|B) = 0.99^2.
$$

另一方面，$H_1$和$H_2$不是独立的。这是因为，如果第一次投掷的结果为正面朝上，者导致我们会猜测，选中的是蓝色硬币，这样第二次投掷正面朝上的概率就更大。从数学公式中，我们可以计算
    
\begin{eqnarray*}
        P(H_1) &=& P(H_2) = P(B)P(H_1|B) + P(\overline{B})P(H_1|\overline{B}) \\
        &=& 0.5 \cdot 0.99 + 0.5 \cdot 0.01 = 0.5.\\
        P(H_1\cap H_2) &=& P(B) P(H_1\cap H_2|B) + P(\overline{B})P(H_1\cap H_2|\overline{B}) \\
        &=& 0.5 \cdot 0.99^2 + 0.5 \cdot 0.01^2 = 0.4901.
\end{eqnarray*}
    
因此，$P(H_1\cap H_2) \neq P(H_1)P(H_2)$，即$H_1$和$H_2$不独立。
```