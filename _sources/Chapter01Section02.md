# 随机事件

## 定义

样本空间
: 称随机现象的一切可能基本结果组成的集合，记为

$
\Omega=\{ \omega \}.
$。

样本点
: 样本空间中的元素，又称**基本结果**。


举一些例子来帮助理解样本空间。
```{prf:example} 样本空间
:label: ex01-a
场景一：投掷一枚硬币

  投掷一枚硬币的结果样本空间为 $\{\text{正,反}\}$ 。
***
场景二：投掷一个六面骰子

  投掷一个六面骰子的结果样本空间为 $\{1,2,3,4,5,6\}$ 。
***
场景三：在一天内使用手机的时间

  学生在未来的一天内使用手机的时间所构成的样本空间为 $\{t:0 \leq t \leq 24\}$ 。
***
场景四：一名学生在罚球线进行定点投篮
  - 只允许该学生投掷10个球。
  
  在10次投球过程中投中球数量的样本空间为 $\{0,1,\cdots ,10\}$ 。
  - 允许该学生投掷任意数量的球。
  
  投中5个球时所花费时间的样本空间为 $\{t:t\geq 0\}$ 。
  - 允许该学生投掷任意数量的球。
  
  投中5个球时所投出球数的样本空间为 $\{k:k=5,\cdots\}$ 。
```


```{admonition} Question
从集合论的角度来看，{prf:ref}`ex01-a` 中所定义的样本空间有什么差异？
```

随机事件
: 称随机现象的某些样本点组成的集合为随机事件，简称事件。常用英文大写字母表示。


```{prf:example} 随机事件
:label: ex01-b
考虑投掷一颗六面骰子，样本空间为 $\Omega = \{1,2,3,4,5,6\}$ 。

若我们感兴趣的是“骰子出现奇数点”，那么随机事件为 $A=\{1,3,5\}$ 。
```

基本事件
: 由样本空间中单个元素组成的子集。

必然事件
: 样本空间的最大子集，也即是样本空间本身。

不可能事件
: 样本空间的最小子集，也就是空集。



## 事件的关系、运算及运算性质

```{list-table} 事件间的关系
:header-rows: 1
:name: tab1.2
* - 文字描述
   - 数学表示
* - 事件 $A$ 发生必然导致事件 $B$ 发生
   - $A\subset B$  
* - 事件 $A$ 与事件 $B$ 相等
   - $A = B$  
* - 事件 $A$ 与事件 $B$ 不可能同时发生（ $A$ 与 $B$ 互不相容）
   - $AB=\emptyset$  
```

```{list-table} 事件间的运算
:header-rows: 1
:name: tab1.3
* - 文字描述
   - 数学表示
* - 事件 $A$ 与 $B$ 中至少有一个发生
   - $A\cup B$  
* - 事件 $A$ 与 $B$ 同时发生
   - $A\cap B$ 或 $AB$  
* - 事件 $A$ 发生而 $B$ 不发生
   - $A-B$  
* - 事件 $A$ 不发生
   - $\overline{A}$ 或 $A^{c}$  
```

```{list-table} 事件间的运算性质
:header-rows: 1
:name: tab1.4
* - 运算性质
   - 数学表示
* - 交换律
   - $A\cup B =B \cup A, \quad AB =BA$  
* - 结合律
   - $\left ( A\cup B \right )\cup C =A\cup \left ( B \cup C \right ),\quad \left ( A B \right ) C =A \left ( B C \right )$  
* - 分配律
   - $(A\cup B)\cap C=AC\cup BC,\quad (A\cap B)\cup C=(A\cup C)\cap (B\cup C)$  
* - 对偶律
   - $\overline{A \cup B } =\overline{A} \cap \overline{B},\quad \overline{A \cap B } =\overline{A} \cup \overline{B}$  
```

在实际应用中，**对偶律**是最为常用的运算性质，并且可以推广至有限个和可列个随机变量的情形。

$$
\begin{aligned}
&\text{有限个的情形：} &\overline{\bigcup_{i=1}^{n} A_{i} } =\bigcap_{i=1}^{n} \overline{A_{i} }, \quad \overline{\bigcap_{i=1}^{n} A_{i} } =\bigcup_{i=1}^{n} \overline{A_{i} } \\
&\text{可列个的情形：} & \overline{\bigcup_{i=1}^{\infty } A_{i} } =\bigcap_{i=1}^{\infty } \overline{A_{i} }, \quad 
 \overline{\bigcap_{i=1}^{\infty } A_{i} } =\bigcup_{i=1}^{\infty } \overline{A_{i} }
\end{aligned}
$$

```{admonition} Summary
:class: caution
样本空间本质上是一个**集合**。随机事件是样本空间的一个子集，本身也是一个**集合**。事件间的关系、运算以及运算性质本质上都是**集合**间的关系、运算及运算性质。
```




