---
title: 켤레 전치(Conjugate Transpose, Hermitian Transpose) 행렬
date: 2025-02-22
tags:
---
## 켤레 전치(Conjugate Transpose)의 정의
행렬 $A$ 에 대해, 켤레 전치는 다음과 같이 정의된다.

$$ A^* = \overline{A}^T $$

즉, 행렬을 전치(Transpose)한 후, 복소 켤레(Conjugate)를 취한 것이다. 문헌에 따라 다르게 표현하는 경우도 있다. ($A^H$ 또는 특히 양자역학에서 $A^\dagger$)
## 켤레 전치의 성질
### 덧셈과 곱셈에 대한 성질
- 덧셈과 스칼라 곱에 대한 성질 
 $$  (A + B)^* = A^* + B^*  $$
 $$  (\lambda A)^* = \overline{\lambda} A^*, \quad \forall \lambda \in \mathbb{C}  $$

- 곱셈에 대한 성질 (반자동형) 
 $$  (AB)^* = B^* A^*  $$

 즉, ==켤레 전치를 취하면 행렬 곱의 순서가 바뀐다.==

### 켤레와 전치
- 두 번 켤레 전치를 취하면 원래 행렬이 된다.
 $$
 (A^*)^* = A
 $$
 
- 켤레와 전치는 가환이다.

 $$
 A^* = \overline{A^T} = (\overline{A})^T
 $$
### 켤레 전치와 역행렬

$$
(A^{-1})^* = (A^*)^{-1}
$$

역행렬의 켤레 전치는 켤레 전치의 역행렬과 동일하다.

### 켤레 전치의 행렬식(Determinant)

$$
\det(A^*)= \overline{\det(A)}
$$

행렬식(Determinant)의 켤레는 행렬의 켤레 전치의 행렬식과 동일하다.[^1]

### 켤레 전치와 고유값(Eigenvalues)
 $$
 A x = \lambda x \quad \Rightarrow \quad A^* \overline{x} = \overline{\lambda} \overline{x}
 $$

 즉, $A$ 의 고유값이 $\lambda$ 이면, $A^*$ 의 고유값은 $\overline{\lambda}$ 입이다.

[^1]: $\det(\overline{A})= \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\prod_{i=1}^{n} \overline{A_{i, \sigma(i)}} = \overline{\sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\prod_{i=1}^{n} A_{i, \sigma(i)}}$ 이므로, $\det(\overline{A})= \overline{\det(A)}$