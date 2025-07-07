---
title: 케일리 해밀턴 정리(Cayley-Hamilton theorem)
date: 2025-02-20
tags:
---
## 케일리 해밀턴 정리(Cayley-Hamilton theorem)
$T$를 유한 차원 벡터 공간 $V$ 위의 선형 변환이라 하자. 또한, $f(t)$를 $T$의 특성 다항식이라 하자. 그러면  
$$
f(T) = T_0
$$

즉, $T$는 자신의 특성 방정식을 만족한다.

### $T$-순환 부분공간 (T-cyclic subspace)
$T$를 벡터 공간 $V$ 위의 선형 변환이라 하고, $x$를 $V$의 0이 아닌 벡터라고 하자. 이때, 부분공간

$$
W = \text{span}(\{x, T(x), T^2(x), \dots\})
$$

를 $x$에 의해 생성된 $V$의 $T$-순환 부분공간이라고 한다. $W$는 $x$를 포함하는 $V$의 **가장 작은** $T$-불변 부분공간이다. 즉, $x$를 포함하는 모든 $T$-불변 부분공간은 반드시 $W$를 포함해야 한다.

### $T_W$의 특성 다항식은 $T$의 특성 다항식을 나눈다.
$W$가 $V$의 $T$-불변 부분공간이면, $T_W$의 특성 다항식은 $T$의 특성 다항식을 나눈다. $W$에 대한 순서 있는 기저를 $\gamma = \{v_1, v_2, \dots, v_k\}$라 하고, 이를 확장하여 $V$에 대한 순서 있는 기저 $\beta = \{v_1, v_2, \dots, v_k, v_{k+1}, \dots, v_n\}$를 정의하자. 이때,

$$
A = [T]_{\beta}, \quad B_1 = [T_W]_{\gamma}
$$

라고 하면,

$$
A =
\begin{pmatrix}
B_1 & B_2 \\
O & B_3
\end{pmatrix}
$$

의 형태로 쓸 수 있다.

$T$의 특성 다항식을 $f(t)$, $T_W$의 특성 다항식을 $g(t)$라 하자. 그러면

$$

f(t) = \det(A - t I_n) = \det

\begin{pmatrix}

B_1 - t I_k & B_2 \\

O & B_3 - t I_{n-k}

\end{pmatrix}

= g(t) \cdot \det(B_3 - t I_{n-k})

$$

이다. 따라서 $g(t)$는 $f(t)$를 나눈다.

### $T_W$의 특성다항식
만약

$$
a_0 v + a_1 T(v) + \dots + a_{k-1} T^{k-1}(v) + T^k(v) = 0
$$

을 만족하는 스칼라 $a_0, a_1, \dots, a_{k-1}$가 존재한다면, $T_W$의 특성 다항식은

$$
f(t) = (-1)^k (a_0 + a_1 t + \dots + a_{k-1} t^{k-1} + t^k)
$$

이다.

$\dim{W}=k$일 때, $\beta = \{v, T(v), \dots, T^{k-1}(v)\}$를 $W$의 순서 기저라 하자.

스칼라 $a_0, a_1, \dots, a_{k-1}$가 존재하여

$$

a_0 v + a_1 T(v) + \dots + a_{k-1} T^{k-1}(v) + T^k(v) = 0

$$

이 성립한다고 하자. 이때,

$$

[T_W]_{\beta} =

\begin{pmatrix}

0 & 0 & \dots & 0 & -a_0 \\

1 & 0 & \dots & 0 & -a_1 \\

0 & 1 & \dots & 0 & -a_2 \\

\vdots & \vdots & \ddots & \vdots & \vdots \\

0 & 0 & \dots & 1 & -a_{k-1}

\end{pmatrix}

$$

이다. 이 행렬의 특성 다항식은

$$

f(t) = (-1)^k (a_0 + a_1 t + \dots + a_{k-1} t^{k-1} + t^k)

$$

이다.

## 케일리 해밀턴 정리 증명
$f(T)(v) = 0$임을 모든 $v \in V$에 대해 보인다. $v = 0$일 경우 자명하므로, $v \neq 0$인 경우를 가정하자. $v$에 의해 생성되는 $T$-순환 부분공간 $W$를 고려하자.

$\dim(W) = k$라 하면, $T^{k} (v) \in W$이므로, 스칼라 $a_0, a_1, \dots, a_{k-1}$가 존재하여 다음이 성립한다.  

$$
a_0 v + a_1 T(v) + \dots + a_{k-1} T^{k-1}(v) + T^k(v) = 0
$$

따라서 $T_W$의 특성 다항식 $g(t)$는 다음과 같다.

$$
g(t) = (-1)^k (a_0 + a_1 t + \dots + a_{k-1} t^{k-1} + t^k)
$$

위 식에서 $T$를 적용하면, 

$$
g(T)(v) = (-1)^k (a_0 I + a_1 T + \dots + a_{k-1} T^{k-1} + T^k)(v) = 0
$$

이다.

불변 부분공간의 특성 다항식 $g(t)$는 특성 다항식 $f(t)$를 나누므로, 어떤 다항식 $q(t)$가 존재하여  

$$
f(t) = q(t) g(t)
$$
이다.

$$
f(T)(v) = q(T) g(T)(v) = q(T) (0) = 0
$$

따라서 $f(T) = 0$이 성립한다.

## 행렬로 표현한 케일리-해밀턴 정리
$n \times n$ 행렬 $A$와 $A$의 특성다항식 $f(t)$에 대하여, 

$$
f(A)=O
$$
이다.

### 이차 정사각행렬에서의 케일리-해밀턴 정리
$2 \times 2$ 행렬 $A$를

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

라 하자. 이때, 

$$
\begin{align*}
f(t) = \det(A - tI) &= \det\begin{pmatrix} a-t & b \\ c & d-t \end{pmatrix} \\\\
& = (a-t)(d-t) - bc \\\\
& = t^2 - (a+d)t + (ad-bc) \\\\
& = t^2 - \text{tr}(A)t + \text{det}(A)
\end{align*}
$$

이므로, 케일리 해밀턴 정리에 의해

$$
A^2 - \text{tr}(A)A + \text{det}(A)I = O
$$

이 성립한다.
