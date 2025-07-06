---
title: "유니타리 행렬(Unitary Matrix)"
date: "2025-02-18"
tags:
---
## 유니타리 행렬(Unitary Matrix)
유니타리 행렬 $U$은 다음 조건을 만족하는 정사각 행렬이다.

$$
U^* U = U U^* = I
$$

- $U^*$는 $U$의 켤레 전치(conjugate transpose)

## 유니타리 행렬의 성질[^1]
### 노름 보존(Norm Preservation)
유니타리 행렬은 벡터의 노름(norm)을 보존한다. 즉, 임의의 복소수 벡터 $x$에 대해,

$$
\| Ux \| = \| x \|
$$

이 성질은 유니타리 행렬이 내적을 보존한다는 의미이기도 하다.

$$
\langle Ux, Uy \rangle = \langle x, y \rangle
$$

이를 통해 유니타리 행렬이 ==길이를 변형하지 않는 등거리 변환(isometry)==임을 알 수 있다.

### 고윳값의 크기는 1
유니타리 행렬은 내적을 보존하므로,

$$
\langle Ux, Ux \rangle = \langle \lambda x, \lambda x \rangle = \langle x, x \rangle
$$

내적의 선형성과 켤레 복소수 성질을 이용하면,

$$
\lambda \overline{\lambda} \langle x, x \rangle = |\lambda|^2 \langle x, x \rangle = \langle x, x \rangle 
$$

$x \neq 0$이므로,

$$
|\lambda| = 1
$$

따라서 자명하게,

$$
|\det(U)| = 1
$$

이는 유니타리 행렬이 ==부피를 보존==한다는 의미이기도 하다.

### 정규직교기저
유니타리 행렬은 $U^* U = I$을 만족하므로,

$$
(U^* U)_{ij} = u_i^* u_j = \delta_{ij}
$$

각 열벡터의 노름이 1이고,  $i \neq j$일 때, $\langle u_i, u_j \rangle = 0$이므로 열벡터들은 서로 직교한다. 따라서, 유니타리 행렬의 열벡터(행벡터)는 정규직교 기저를 이룬다.

## $\det(A^*) = \overline{\det(A)}$
임의의 복소수 정사각행렬 $A$에 대해 켤레 전치(conjugate transpose, Hermitian transpose)를 취한 행렬의 행렬식(determinant)은 원래 행렬식의 켤레 복소수와 같다.

$A$가 $n \times n$ 행렬일 때, 행렬식의 정의에 의해,

$$
\det(A) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} a_{i, \sigma(i)}
$$

여기서 $S_n$은 대칭군(순열군)이고, $\operatorname{sgn}(\sigma)$는 순열의 부호(순열을 만들기 위해 필요한 교환 횟수가 짝수인 경우 $+1$, 홀수인 경우 $-1$)를 나타낸다.

행렬 $A^*$의 성분은 $(A^*)_{ij} = \overline{A_{ji}}$이므로,

$$
\det(A^*) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} \overline{a_{\sigma(i), i}}
$$

복소수의 켤레 연산은 곱셈과 덧셈에서 분배되므로,

$$
\det(A^*) = \overline{\sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} a_{\sigma(i), i}}
$$

위 식의 우변은 정확히 $\det(A)$의 켤레 복소수와 같으므로,

$$
\det(A^*) = \overline{\det(A)}
$$

[^1]: 이러한 성질은 유니타리 행렬의 필요충분조건이기도 하다.