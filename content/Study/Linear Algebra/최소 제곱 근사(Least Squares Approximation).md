---
title: 최소제곱법(Least Squares Approximation)
date: 2025-02-28
tags:
---
## 최소 제곱 근사 (Least Squares Approximation)
한 실험자가 측정값 $y_1, y_2, \cdots, y_m$ 을 시간 $t_1, t_2, \cdots, t_m$ 에서 수집한다고 하자.

![[least square.webp|400]]

데이터 $(t_1, y_1), (t_2, y_2), \cdots, (t_m, y_m)$ 이 평면상의 점으로 표시되어 있다고 가정하자. 우리는 $y$ 와 $t$ 사이에 본질적으로 선형적인 관계가 존재한다고 느낀다. 

$$
y = ct + d
$$

와 같은 관계가 존재한다고 가정하고, 이 방정식에서 상수 $c$ 와 $d$ 를 찾아서 주어진 데이터에 대해 최적의 적합(fit)을 이루는 직선을 구하고자 한다. 

이러한 적합도를 평가하는 한 가지 방법은, 데이터 점들로부터 직선까지의 수직 거리의 제곱합을 나타내는 오차 $E$ 를 계산하는 것이다.

$$
E = \sum_{i=1}^{m} (y_i - c t_i - d)^2
$$

이제 행렬 표현을 도입하자.

$$
A = \begin{bmatrix} 
t_1 & 1 \\ 
t_2 & 1 \\ 
\vdots & \vdots \\ 
t_m & 1 
\end{bmatrix}, 
\quad 
x = \begin{bmatrix} 
c \\ 
d 
\end{bmatrix}, 
\quad 
y = \begin{bmatrix} 
y_1 \\ 
y_2 \\ 
\vdots \\ 
y_m 
\end{bmatrix}
$$

라고 하면, 오차는 다음과 같이 표현할 수 있다.

$$
E = \| y - Ax \|^2
$$

우리는 이제 일반적인 방법을 사용하여 $E$ 를 최소화하는 명시적인 벡터 $x_0 \in F^n$ 을 찾고자 한다. 즉, 주어진 $m \times n$ 행렬 $A$ 에 대해,

$$
\| y - Ax_0 \| \leq \| y - Ax \|
$$

가 모든 벡터 $x \in F^n$ 에 대해 성립하는 $x_0$ 을 찾는다. 

## 최소제곱 해를 찾는 방법
$A$ 를 $m \times n$ 행렬, $y$ 를 $F^m$ 의 원소로 두고, 집합

$$
W = \{ Ax : x \in F^n \}
$$

를 정의하자. 즉, $W$ 는 $A$ 에 의해 생성된 열 공간(column space) $R(L_A)$ 이다. 

![[projection.webp|400]]

벡터 $y$가 행렬 $A$의 열공간 $W$에 속하지 않는 경우, $y$ 에 가장 가까운 벡터가 $W$ 안에 유일하게 존재한다. 이 벡터를 $u=Ax_0$ 라 하자. 여기서 $x_0$ 는 $F^n$ 의 원소이다. 

그러면

$$
\| Ax_0 - y \| \leq \| Ax - y \|, \quad \forall x \in F^n
$$

가 성립한다. 즉, $x_0$ 는

$$
E = \| Ax_0 - y \|
$$

를 최소화하는 성질을 갖는다. 이제 이러한 $x_0$ 를 찾는 실용적인 방법을 개발하고자 한다. 

$$
Ax_0 - y \in W^\perp
$$

가 성립하므로,

$$
\langle Ax, Ax_0 - y \rangle_m = 0, \quad \forall x \in F^n
$$

이 된다. 내적의 성질[^1]에 의해

$$
\langle x, A^*(Ax_0 - y) \rangle_n = 0, \quad \forall x \in F^n
$$

즉,

$$
A^*(Ax_0 - y) = 0
$$

이 된다. 결국, 우리는 다음 방정식을 만족하는 $x_0$ 를 찾으면 된다.

$$
A^* A x_0 = A^* y
$$

추가로, $A$ 의 랭크가 $n$ 이라고 가정[^2]하면,

$$
x_0 = (A^* A)^{-1} A^* y
$$

를 얻는다. 이제 이 내용을 다음의 정리로 요약할 수 있다.

### 정리
$A \in M_{m \times n}(F)$ 및 $y \in F^m$ 에 대하여, 다음을 만족하는 $x_0 \in F^n$ 이 존재한다.

$$
(A^* A) x_0 = A^* y
$$

또한,

$$
\| Ax_0 - y \| \leq \| Ax - y \|, \quad \forall x \in F^n
$$

가 성립한다. 

추가적으로, 만약 $\text{rank}(A) = n$ 이라면,

$$
x_0 = (A^* A)^{-1} A^* y
$$

이 성립한다.

## 활용
수집한 데이터가 다음과 같다고 가정하자.

$$
(1,2), (2,3), (3,5), (4,7)
$$

이 데이터를 행렬 형태로 나타내면,

$$
A = \begin{bmatrix} 
1 & 1 \\ 
2 & 1 \\ 
3 & 1 \\ 
4 & 1 
\end{bmatrix}, 
\quad 
y = \begin{bmatrix} 
2 \\ 
3 \\ 
5 \\ 
7 
\end{bmatrix}
$$

따라서,

$$
A^* A = 
\begin{bmatrix} 
1 & 2 & 3 & 4 \\ 
1 & 1 & 1 & 1 
\end{bmatrix}
\begin{bmatrix} 
1 & 1 \\ 
2 & 1 \\ 
3 & 1 \\ 
4 & 1 
\end{bmatrix}
=
\begin{bmatrix} 
30 & 10 \\ 
10 & 4 
\end{bmatrix}
$$

이제, $(A^* A)^{-1}$ 를 구하면,

$$
(A^* A)^{-1} = \frac{1}{20} 
\begin{bmatrix} 
4 & -10 \\ 
-10 & 30 
\end{bmatrix}
$$

따라서, 최소제곱 해 $x_0 = (c, d)^T$ 는 다음과 같이 계산된다.

$$
\begin{bmatrix} 
c \\ 
d 
\end{bmatrix} 
= x_0 = \frac{1}{20} 
\begin{bmatrix} 
4 & -10 \\ 
-10 & 30 
\end{bmatrix}
\begin{bmatrix} 
2 \\ 
3 \\ 
5 \\ 
7 
\end{bmatrix}
$$

이를 계산하면,

$$
x_0 = \begin{bmatrix} 
1.7 \\ 
0 
\end{bmatrix}
$$

즉, 최소제곱 직선은

$$
y = 1.7x
$$

가 된다.

또한, 최소제곱 오차 $E$ 는 다음과 같이 계산된다.

$$
E = \| Ax_0 - y \|^2 = 0.3
$$

### $A^*A$의 구조
$A^*$ 는 $A$ 의 켤레전치행렬이므로,

$$
A^* =
\begin{bmatrix}
\overline{t_1} & \overline{t_2} & \cdots & \overline{t_m} \\
1 & 1 & \cdots & 1
\end{bmatrix}
$$

이를 $A$ 와 곱하면,

$$
A^* A =
\begin{bmatrix}
\overline{t_1} & \overline{t_2} & \cdots & \overline{t_m} \\
1 & 1 & \cdots & 1
\end{bmatrix}
\begin{bmatrix}
t_1 & 1 \\
t_2 & 1 \\
\vdots & \vdots \\
t_m & 1
\end{bmatrix}
$$

이므로, 

$$
A^* A =
\begin{bmatrix}
\sum_{i=1}^{m} ||t_i ||^2 & \sum_{i=1}^{m} t_i \\
\sum_{i=1}^{m} t_i & m
\end{bmatrix}
$$

즉, 행렬의 각 성분은 다음과 같이 해석할 수 있다.

$$
A^* A =
\begin{bmatrix}
\text{측정된 시간값들의 제곱합} & \text{시간값들의 합} \\
\text{시간값들의 합} & \text{데이터 개수}
\end{bmatrix}
$$

### 일반화 공식

$$
A^* y =
\begin{bmatrix}
\sum_{i=1}^{m} t_i y_i \\
\sum_{i=1}^{m} y_i
\end{bmatrix}
$$

이므로, 일반적인 최소제곱 직선의 해는 다음과 같다.

$$
\begin{bmatrix}
c \\
d
\end{bmatrix}
=
\begin{bmatrix}
\sum ||t_i ||^2 & \sum t_i \\
\sum t_i & m
\end{bmatrix}^{-1}
\begin{bmatrix}
\sum t_i y_i \\
\sum y_i
\end{bmatrix}
$$

위의 식을 전개하면,

$$
c = \frac{m \sum t_i y_i - \sum t_i \sum y_i}{m \sum ||t_i||^2 - (\sum t_i)^2}
$$


이고,

$$
d = \frac{\sum y_i - c \sum t_i}{m}
$$

이다.

[^1]: 임의의 행렬 $A$, 벡터 $x$, $y$ 에 대해 $Ax$ 와 $y$ 의 내적은 $x$ 와 $A^* y$ 의 내적과 같다. 즉, $\langle Ax, y \rangle_m = \langle x, A^* y \rangle_n$ 이 성립한다. 이는 선형 변환을 적용한 후의 내적이 전치 연산을 통해 변환될 수 있음을 의미한다. 이를 증명하기 위해 내적의 성질을 사용하면, $\langle Ax, y \rangle_m = y^* (Ax)$ 가 되고, 행렬 곱셈의 결합 법칙을 적용하면 $y^* (Ax) = (y^* A) x$ 가 된다. 여기서 $y^* A$ 는 $(A^* y)^*$ 와 같으므로, 최종적으로 $(A^* y)^* x = \langle x, A^* y \rangle_n$ 이 성립한다. 따라서 원래 명제가 참임을 알 수 있다.
[^2]: 행렬 $A^* A$ 의 랭크는 $A$ 의 랭크와 같다. 즉, $\text{rank}(A^* A) = \text{rank}(A)$ 가 성립한다. 이를 증명하기 위해 차원 정리를 사용하면, 영공간(null space)의 차원이 같으면 랭크의 차원도 같기에 $A^* A x = 0$ 이 $Ax = 0$ 과 동치임을 보이면 된다. 먼저, $Ax = 0$ 이면 명백히 $A^* A x = A^* 0 = 0$ 이므로 성립한다. 반대로, $A^* A x = 0$ 이라고 가정하면, 내적의 성질을 이용하여 $0 = \langle A^* A x, x \rangle_n$ 이 성립한다. $\langle A^* A x, x \rangle_n = \langle Ax, Ax \rangle_m = \| Ax \|^2$ 이므로, $\| Ax \|^2 = 0$ 이고 $Ax = 0$ 이 성립한다. 결국, $A^* A$ 의 영공간과 $A$ 의 영공간이 동일하다는 결론을 얻을 수 있고, 이를 통해 $A^* A$ 와 $A$ 의 랭크가 동일함을 보일 수 있다. 행렬 $A$ 가 $m \times n$ 행렬이며 $\text{rank}(A) = n$ 이면, $A^* A$ 는 가역 행렬이다. $\text{rank}(A^* A) = \text{rank}(A)$ 가 성립하므로, 만약 $A$ 가 풀랭크(full-rank)라면 $A^* A$ 도 풀랭크가 되어 가역 행렬이 됨을 의미한다. 이 성질은 최소제곱 해를 구하는 공식 $x_0 = (A^* A)^{-1} A^* y$ 가 유일한 해를 갖도록 보장하는 중요한 역할을 한다.