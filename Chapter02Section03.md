# 乘法公式

```{prf:theorem} 乘法公式
:label: thm02-b

若$P(B)>0$，则

$$P(AB)=P(B)\cdot P(A|B).$$
```

````{prf:theorem} 
:label: thm02-c

若$P(A_{1}A_{2}\cdots A_{n-1} )>0$，则

$$P(A_{1}A_{2}\cdots A_{n} )=P(A_{1})\cdot P(A_{2}|A_{1})\cdot P(A_{3}|A_{1}A_{2})\cdots P(A_{n}|A_{1}A_{2}\cdots A_{n-1}).$$

```{dropdown} Proof

令 $B_{i}=A_{1}A_{2}\cdots A_{i},i=1,2,\cdots,n$。

一方面，我们想要证明所定义的$P(B_i)$均大于零。因为
$P(B_{n-1}) = P(A_{1}A_{2}\cdots A_{n-1})>0$而且
\begin{eqnarray*}
    P(B_{i}) &=& P(A_1A_2\cdots A_i)\\
    &\geq& P(A_1A_2\cdots A_i \cap A_{i+1}\cdot A_{n-1}) \\
    & = &  P(B_{n-1}) >0, i=1,2,\cdots,n-1.
\end{eqnarray*}

另一方面，我们证明$P(A_{1}A_{2}\cdots A_{n}) = P(A_{1}A_{2}\cdots A_{n-1})\cdot P(A_n|A_{1}A_{2}\cdots A_{n-1})$.
因为 $P(B_{n-1}) = P(A_{1}A_{2}\cdots A_{n-1})>0$，所以
\begin{eqnarray*}
P(B_{n})&=&P((A_{1}A_{2}\cdots A_{n-1})\cap A_{n})\\
&=&P(B_{n-1}\cap A_{n})\\
&=&P(B_{n-1})\cdot P(A_{n}|B_{n-1})\\
&=&P(B_{n-1})\cdot P(A_{n}|A_{1}A_{2}\cdots A_{n-1}).
\end{eqnarray*}

类似地，我们有$P(B_{i}) = P(B_{i-1}) P(A_{i}|B_{i-1}),i=2,3,\cdots,n-2$。由此得证。
```
````

`````{prf:example} 罐子模型
:label: ex02-b

设罐子里有$b$个黑球，$r$个红球。每次随机取出一个球，取出后将原球放回，同时放入$c$个同色球和$d$个异色球。若连续从罐子里取出三个球，求三个球中有两个红球、一个黑球的概率。

```{dropdown} Solution

记$B_{i}$为“第$i$次取出的是黑球”，$R_{j}$为“第$j$次取出的是红球”。由乘法公式，可知所求的概率为

\begin{eqnarray*}
P(B_{1} R_{2}R_{3})&=&P(B_{1})P(R_{2}|B_{1})P(R_{3}|B_{1}R_{2})=\frac{b}{b+r} \cdot \frac{r+d}{b+r+c+d}\cdot \frac{r+d+c}{b+r+2c+2d}, \\
P(R_{1} B_{2}R_{3})&=&P(R_{1})P(B_{2}|R_{1})P(R_{3}|R_{1}B_{2})=\frac{r}{b+r} \cdot \frac{b+d}{b+r+c+d}\cdot \frac{r+d+c}{b+r+2c+2d},  \\
P(R_{1} R_{2}B_{3})&=&P(R_{1})P(R_{2}|R_{1})P(B_{3}|R_{1}R_{2})=\frac{r}{b+r} \cdot \frac{r+c}{b+r+c+d}\cdot \frac{b+2d}{b+r+2c+2d}.
\end{eqnarray*}
```

````{prf:remark} Remark
:label: remark02-b
:class: dropdown

罐子模型有四种变形，见{numref}`tab02-a`。

```{list-table} 两种情况的比较 
:header-rows: 1
:name: tab02-a
* -  模型名称
   - $c$
   - $d$
   - 概率计算
   - 描述
* -  不放回抽样
   - $-1$
   - $0$
   - \begin{eqnarray*}
    P(B_{1} R_{2}R_{3})&=&\frac{br(r-1)}{(b+r)(b+r-1)(b+r-2)}\\
    P(R_{1} B_{2}R_{3})&=&\frac{br(r-1)}{(b+r)(b+r-1)(b+r-2)} \\
    P(R_{1} R_{2}B_{3})&=&\frac{br(r-1)}{(b+r)(b+r-1)(b+r-2)}
    \end{eqnarray*}
   -  前次抽样结果会影响后次抽样结果；抽取的黑、红球个数确定，概率不依赖其抽球次序。
* -  放回抽样
   - $0$
   - $0$
   -  \begin{eqnarray*}
    P(B_{1} R_{2}R_{3})&=&\frac{br^{2} }{(b+r)^{3} } \\
    P(R_{1} B_{2}R_{3})&=&\frac{br^{2} }{(b+r)^{3} }  \\
    P(R_{1} R_{2}B_{3})&=&\frac{br^{2} }{(b+r)^{3} } 
    \end{eqnarray*}

   -  前次抽样结果不会影响后次抽样结果；抽取的概率相等。
* -  传染病模型
   - $>0$
   - $0$
   - \begin{eqnarray*}
    P(B_{1} R_{2}R_{3})&=&\frac{br(r+c) }{(b+r)(b+r+c)(b+r+2c) } \\
    P(R_{1} B_{2}R_{3})&=&\frac{br(r+c) }{(b+r)(b+r+c)(b+r+2c) } \\
    P(R_{1} R_{2}B_{3})&=&\frac{br(r+c) }{(b+r)(b+r+c)(b+r+2c) } 
    \end{eqnarray*}
   -  每次取出球后会增加下一次取到同色球的概率；每次发现一个传染病患者，以后都会增加再传染的概率。
* -  安全模型
   - $0$
   - $>0$
   -   \begin{eqnarray*}
    P(B_{1} R_{2}R_{3})&=&\frac{b }{b+r } \cdot \frac{r+d }{b+r+d }\cdot \frac{r+d }{b+r+2d }\\
    P(R_{1} B_{2}R_{3})&=&\frac{r }{b+r } \cdot \frac{b+d }{b+r+d }\cdot \frac{r+d }{b+r+2d }\\
    P(R_{1} R_{2}B_{3})&=&\frac{r }{b+r } \cdot \frac{r}{b+r+d }\cdot \frac{b+2d }{b+r+2d }
    \end{eqnarray*}
   -  每当事故发生，安全工作就抓紧，下次再发生事故的概率就会减少；反之，没有事故，发生事故的概率增大。
```

- 只要$d=0$且抽取的黑球和红球个数确定，则所求的概率不依赖抽球的次序；
- 当$d>0$时，则所求的概率与抽球的次序有关。
````

`````









