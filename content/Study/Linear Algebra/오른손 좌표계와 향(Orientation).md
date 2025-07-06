---
title: 오른손 좌표계와 향(Orientation)
date: 2025-02-18
tags:
---
벡터의 순서쌍 $\{ \mathbf{u}, \mathbf{w} \}$가 오른손 좌표계를 형성하기 위한 필요충분 조건이 $O( \mathbf{u}, \mathbf{w} ) = 1$과 동치임을 보인다.

## 방향성(Orientation)의 정의

주어진 $\mathbb{R}^2$의 기저 $\{ \mathbf{u}, \mathbf{w} \}$에 대해 방향성(Orientation) $O( \mathbf{u}, \mathbf{w} )$를 다음과 같이 정의한다.

$$
O \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} = \frac{ \det \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} }{ \left| \det \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} \right| }
$$

이는 행렬식 $\det \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix}$의 부호를 의미하며, 다음이 성립한다.

$$
O \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} = 1 \quad \iff \quad \det \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} > 0
$$

## 회전에 대한 행렬식의 부호

이제, 벡터 $\mathbf{w}$가 $\mathbf{u}$를 $0 < \theta < \pi$만큼 반시계 방향으로 회전하여 얻어지는 경우를 고려하자. 즉,

$$
\mathbf{u} = ( a_{1}, a_2 ), \quad \mathbf{w} = (a_1 \cos \theta - a_2 \sin \theta, a_1 \sin \theta + a_2 \cos \theta )
$$

이때, 행렬식을 계산하면

$$
\det \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} = \det \begin{bmatrix} a_1 & a_2 \\ a_1 \cos \theta - a_2 \sin \theta & a_1 \sin \theta + a_2 \cos \theta \end{bmatrix}
$$

전개하여 정리하면,

$$
\begin{aligned}
\det \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} &= a_1(a_1 \sin \theta + a_2 \cos \theta) - a_2(a_1 \cos \theta - a_2 \sin \theta) \\
&= a_1^2 \sin \theta + a_1 a_2 \cos \theta - a_2 a_1 \cos \theta + a_2^2 \sin \theta \\
&= (a_1^2 + a_2^2) \sin \theta
\end{aligned}
$$

여기서 $a_1^2 + a_2^2 > 0$이고, $\sin \theta > 0$ (왜냐하면 $0 < \theta < \pi$이므로)임을 이용하면

$$
\det \begin{bmatrix} \mathbf{u} \\ \mathbf{w} \end{bmatrix} > 0
$$

$O( \mathbf{u}, \mathbf{w} ) = 1$이 성립한다.