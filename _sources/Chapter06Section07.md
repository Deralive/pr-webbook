# 信息量
在信息论中，由美国克劳德 $·$ 艾尔伍德 $·$ 香农（Claude Elwood Shannon）院士提出了一个概念——信息熵，也称为香农熵。对于一个离散的随机变量，其概率分布列

$$
P(X=x_i) = p_i,i=1,2,\cdots,n.
$$

则信息熵的定义为

$$
H(X) = -\sum_{i=1}^n p_i \log_2(p_i).
$$

从形式上来看，信息熵的定义是随机变量 $X$ 函数的期望。香农熵可以用于度量随机变量的不确定性。而如今，在机器学习中，对于信息熵有更一般的定义。

信息熵
: 对于一个随机变量 $X$ ，其概率分布列或概率密度函数为 $p(x)$ ，则称

$$
H(X) = - E(\ln(p(X)))
$$

为信息熵。

`````{prf:example}
对于一个二点分布随机变量 $X$ ， $P(X=1)=p$ 。则信息熵为
\begin{eqnarray*}
H(X) = - ((1-p) \ln(1-p) + p \ln(p)).
\end{eqnarray*}
`````
除了香农熵之外，费歇尔信息量是统计学中一个基本概念。

费歇尔信息量
: 对于一个随机变量 $X$ ，其概率分布列或概率密度函数为 $p(x;\theta), \theta \in \Theta$ 满足下列条件：

- 参数空间 $\Theta$ 是直线上的一个开区间；
- 支撑 $S = \{x:p(x;\theta)>0\}$ 与 $\theta$ 无关；
- 导数 $\frac{\partial }{\partial \theta}p(x;\theta)$ 对一切 $\theta \in \Theta$ 都存在；
- 对 $p(x;\theta)$ ，积分与微分运算可交换次序，即

$$
\frac{\partial }{\partial \theta} \int_{-\infty}^{\infty} p(x;\theta)\text{d} x = \int_{-\infty}^{\infty} \frac{\partial }{\partial \theta}p(x;\theta)\text{d} x;
$$

- 期望 $E\left(\frac{\partial }{\partial \theta} \ln p(x;\theta) \right)^2$ 存在；

则称

$$
I(\theta) = E\left(\frac{\partial }{\partial \theta} \ln p(X;\theta) \right)^2
$$

为随机变量 $X$ 的费歇尔信息量。

`````{prf:example}
随机变量 $X$ 服从泊松分布 $P(\lambda)$ ，即其分布列为

$$
p(x;\lambda) = \frac{\lambda^x}{x!}e^{-\lambda}, x=0,1,2,\cdots
$$

可验证泊松分布的分布列满足条件。于是，我们可计算

- 求对数，即

$$
\ln p(x;\lambda) = x\ln \lambda - \lambda - \ln(x!).
$$

- 求导数，即

$$
\frac{\partial }{\partial \lambda} \ln p(x;\lambda) = \frac{x}{\lambda} - 1
$$

- 求期望，即

$$
I(\lambda ) = E\left( \frac{X}{\lambda} - 1 \right)^2 = E\left( \frac{(X-\lambda)^2}{\lambda^2} \right)^2 = \frac{1}{\lambda}.
$$

`````
`````{prf:example}
随机变量 $X$ 服从指数分布 $Exp(1/\theta)$ ，即其密度函数为

$$
p(x;\theta) = \frac{1}{\theta} \exp\left\{-\frac{x}{\theta}\right\}, x>0
$$

可验证指数分布的分布列满足条件。于是，我们可计算

- 求对数，即

$$
\ln p(x;\theta) = -\ln(\theta) - \frac{x}{\theta}.
$$

- 求导数，即

$$
\frac{\partial }{\partial \theta} \ln p(x;\theta) = -\frac{1}{\theta} + \frac{x}{\theta^2}
$$

- 求期望，即

$$
I(\lambda ) = E\left( -\frac{1}{\theta} + \frac{X}{\theta^2} \right)^2 = \frac{1}{\theta^2}.
$$

`````