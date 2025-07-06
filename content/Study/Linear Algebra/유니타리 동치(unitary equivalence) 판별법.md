### 유니타리 동치(Unitarily Equivalent)의 정의
두 $n \times n$ 복소 행렬 $A$ 와 $B$ 가 유니타리 동치(unitarily equivalent) 라고 하면, 다음을 만족하는 유니타리 행렬 $P$ 가 존재해야 한다.

$$
B = P^* A P
$$

여기서 $P^*$ 는 $P$ 의 켤레전치(conjugate transpose)이며, 유니타리 행렬의 정의에 따라 다음이 성립한다.

$$
P^* P = P P^* = I
$$

즉, 유니타리 행렬은 정규직교 기저를 보존하는 성질을 가지며, 행렬의 크기를 변형시키지 않는다.

## $\text{tr}(A^* A) = \text{tr}(B^* B)$

$$
\begin{align*}
B^* B &= (P^* A P)^* (P^* A P) \\
&= P^* A^* (P^* P) A P
\end{align*}
$$

유니타리 행렬 $P$ 는 유니타리 성질 $P P^* = I$ 을 만족하므로,

$$
B^* B = P^* A^* A P
$$

이제 트레이스의 기본 성질을 이용하면,

$$
\text{tr}(A^* A) = \text{tr}(P^* A^* A P)
$$

트레이스의 순환 성질 $\text{tr}(XY) = \text{tr}(YX)$ 를 적용하면,

$$
\begin{align*}
\text{tr}(P^* A^* A P) &= \text{tr}(A^* A P P^*) \\
&= \text{tr}(A^* A I) \\
&= \text{tr}(A^* A)
\end{align*}
$$

따라서,

$$
\text{tr}(A^* A) = \text{tr}(B^* B)
$$

## $\sum_{i,j} |A_{ij}|^2 = \sum_{i,j} |B_{ij}|^2$

트레이스의 정의를 이용하면,

$$
\text{tr}(A^* A) = \sum_{k=1}^{n} (A^* A)_{kk}
$$

행렬 성분을 전개하면,

$$
(A^* A)_{kk} = \sum_{l=1}^{n} \overline{A_{lk}} A_{lk}
$$

이를 다시 전체 트레이스로 합하면,

$$
\text{tr}(A^* A) = \sum_{k=1}^{n} \sum_{l=1}^{n} \overline{A_{lk}} A_{lk}
$$

복소수 성분의 제곱 절댓값을 이용하면,

$$
\text{tr}(A^* A) = \sum_{k=1}^{n} \sum_{l=1}^{n} |A_{lk}|^2
$$

행렬 성분의 순서를 변경하면,

$$
\text{tr}(A^* A) = \sum_{i=1}^{n} \sum_{j=1}^{n} |A_{ij}|^2
$$

위에서 증명한 첫 번째 명제에 의해,

$$
\text{tr}(A^* A) = \text{tr}(B^* B)
$$

따라서 동일한 과정으로 $B$ 에 대해서도 적용하면,

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} |A_{ij}|^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} |B_{ij}|^2
$$

즉,

$$
\sum_{i,j} |A_{ij}|^2 = \sum_{i,j} |B_{ij}|^2
$$

## 제곱합이 같지만 유니타리 동치가 아닌 행렬의 예시

다음 두 행렬을 고려하자.

$$
A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
$$

1. 제곱합 계산  
   행렬의 모든 원소의 절댓값 제곱을 더해보자.


$$
\sum_{i,j} |A_{ij}|^2 = 1^2 + 0^2 + 0^2 + 1^2 = 2
$$

$$
\sum_{i,j} |B_{ij}|^2 = 0^2 + 1^2 + 1^2 + 0^2 = 2
$$
즉, 두 행렬의 원소의 제곱합은 같다.

2. 유니타리 동치 여부 확인  
   행렬이 유니타리 동치이려면, 반드시 같은 고윳값을 가져야 한다. 

   - $A$ 의 고윳값:

$$
\det(A - \lambda I) = \begin{vmatrix} 1 - \lambda & 0 \\ 0 & 1 - \lambda \end{vmatrix} = (1-\lambda)(1-\lambda) = 0
 $$

$$
\lambda = 1, 1
 $$
- $B$ 의 고윳값:

$$
\det(B - \lambda I) = \begin{vmatrix} -\lambda & 1 \\ 1 & -\lambda \end{vmatrix} = \lambda^2 - 1 = 0
$$

$$
\lambda = \pm 1
$$

즉, $A$ 의 고윳값은 $(1,1)$, $B$ 의 고윳값은 $(1,-1)$ 이므로, 두 행렬은 서로 다른 고윳값을 가진다.  

이 반례를 통해, 행렬의 모든 원소의 절댓값 제곱합이 같다고 해서 유니타리 동치인 것은 아니라는 사실을 확인할 수 있다.