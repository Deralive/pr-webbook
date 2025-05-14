# 引导问题：对于早八点的课程，学生何时能到教室？

```{prf:example}
:label: ex05-a

我们想要研究：上早八课程的学生一般什么时候会到教室。记学生到达教室的时刻为$X$。$X$表示7点后的分钟数，显然是一个随机变量。共采集了83名学生的打卡时间。我们分别按1分钟间隔、2分钟间隔、5分钟间隔和10分钟间隔绘制了直方图，如图 {numref}`fig:chap05_continuous_rv`。学生大部分在40分到55分之间到达教室，一小部分学生会提前20分钟到达教室，还有一部分学生倾向于临近8点才到。

```{figure} fig/Chap5_continuous_rv.png
---
name: fig:chap05_continuous_rv
width: 80%
---
学生到达教室的直方图
```


我们发现，时间是连续的，且$X$的取值可以充满$(0,60)$这个区间。于是，$X$就是一个连续型随机变量。当我们不断细化间隔的划分，在同一时刻到达教室的学生不会超过1人。于是，利用概率分布列$P(X=x)$来刻画$X$是不恰当的。所以，我们需要提出一个新的概念——概率密度函数。

# 概率密度函数
概率密度函数$p(x)$的值虽不是概率，但乘微分元$\text{d} x$就可以得小区间$(x,x+\text{d}x)$上概率的近似值，即
$$p(x)\text{d}x = P(x<X<x+\text{d}x).$$
在$(a,b)$上很多相邻的微分元的累积就得到$p(x)$在$(a,b)$上的积分，这个积分值就是$X$在$(a,b)$上取值的概率，即
$$\int_{a}^b p(x)\text{d}x = P(a<X<b).$$
特别，在$(-\infty,x]$上$p(x)$的积分就是分布函数$F(x)$，即
$$\int_{-\infty}^x p(t)\text{d} t = P(X\leq x)=F(x).$$
这一关系式是连续随机变量$X$的概率密度函数$p(x)$最本质的属性。

概率密度函数
: 设随机变量$X$的分布函数为$F(x)$,如果存在实数轴上的一个非负可积函数$p(x)$，使得对任意实数$x$有
$$F(x) = \int_{-\infty}^{x} p(t) d t,$$
那么称$p(x)$为$X$的概率密度函数（probability density function, p.d.f.)。称随机变量$X$为连续型随机变量，其分布函数$F(x)$是连续分布函数。

```{admonition} Property
:class: dropdown
连续型随机变量$X$的概率密度函数$p(x)$，其具有
1. 非负性\quad $p(x) \geq 0$；
2. 正则性 \quad  $\int_{-\infty}^{\infty} p(x) d x = 1$。
:class: dropdown
上述两条也是判别某个函数是否为密度函数的充要条件。

向区间$(0,a)$上任意投点，用$X$表示其坐标。设这个点落在$(0,a)$中任一小区间的概率与这个小区间的长度成正比，而与小区间位置无关。求$X$的分布函数和密度函数。

```{dropdown} Solution
记$X$的分布函数为$F(x)$,则
- 当$x<0$时，因为$\{X \leq x\}$是不可能事件,所以$F(x)=P( X \leq x)=0$；
- 当$x \geq a$时，因为$\{X \leq x\}$是必然事件,所以$F(x)=P( X \leq x)=1$；
- 当$0 \leq x <a $ 时， $F(x) =P(X \leq x)=P(0 \leq X \leq x) = k x$，其中$k$为比例系数。因为$F(a)=ka=1$，所以$k = \frac{1}{a}$。于是，分布函数为
  $$F(x)=\left\{\begin{aligned}
      0, &\quad  x<0 \\
  \frac{x}{a}, & \quad 0 \leq x<a \\
  1, &\quad  x \geq a.
  \end{aligned}\right.
  $$

令$X$的密度函数$p(x)$，
- 当$x<0$或$x>a$时，$p(x)=F'(x)=0$；
- 当$x>a$时，$p(x)=F'(x)=0$； (Note: this line is redundant with the one above it)
- 当$0< x< a$，
  $$
  p(x) = F'(x) =  \frac{1}{a}.
  $$

而在$x=0$和$x=a$处，$p(x)$可取任意值，一般就近取值为宜，这不会影响概率的计算。于是，$X$的概率密度是
$$
p(x)= \left\{\begin{aligned}
\frac{1}{a}, &\quad  0<x<a \\
0, & \quad \text { 其他 }
\end{aligned}\right.
$$

```{prf:remark}
:class: dropdown
这个分布就是区间$(0,a)$上的均匀分布，记$U(0, a)$。






