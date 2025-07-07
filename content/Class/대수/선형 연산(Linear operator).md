---
title: 선형 연산자(Linear operator)
date: 2025-02-21
tags:
---
벡터 공간에서의 ==선형 변환(Linear transformation)==은 다음과 같이 정의한다. 
 $$
 T(v+w)= T(v)+ T(w), \quad T(cv)= cT(v)
 $$

## 고등
- 원점을 지나는 일차함수(정비례)
 $$
 f(x)= ax, \quad f(x+y)= f(x)+ f(y), \quad f(cx)= c f(x)
 $$

- 행렬 덧셈 
 $$
 A(x + y)= Ax + Ay, \quad A(c x)= c(Ax)
 $$

- (수렴하는)수열의 합(급수) 연산[^1]
 $$
 \sum (a_n + b_n)= \sum a_n + \sum b_n, \quad \sum (c a_n)= c \sum a_n
 $$

- 확률에서의 기댓값 연산
 $$
 E[X + Y] = E[X] + E[Y], \quad E[cX] = cE[X]
 $$

-  (수렴하는)극한 연산

$$
\lim_{x \to a} (f(x)+ g(x))= \lim_{x \to a} f(x)+ \lim_{x \to a} g(x), \quad \lim_{x \to a} (c f(x))= c \lim_{x \to a} f(x)
$$

- 미분 연산 
 $$
 D(f)= f', \quad D(f+g)= D(f)+ D(g), \quad D(cf)= cD(f)
 $$

- 적분 연산
 $$
 I(f)= \int f(x)\,dx, \quad I(f+g)= I(f)+ I(g), \quad I(cf)= cI(f)
 $$

- 벡터 덧셈

$$
(x+w, y+z) = (x,y)+ (w,z),  \quad  (cx,cy) = c(x,y)
$$

---

- 행렬의 대각합

$$
\text{tr}(A+B)= \text{tr}(A)+ \text{tr}(B), \quad \text{tr}(cA)= c \cdot \text{tr}(A)
$$

- 행렬의 전치

$$
(A+B)^T= A^T+ B^T, \quad (cA)^T= cA^T
$$

- 행렬식 (한 행 또는 한 열에 대해 선형성 성립)
 $$
 \det{\begin{bmatrix} u+w \\ v \end{bmatrix}}
 = \det{\begin{bmatrix} u \\ v \end{bmatrix}} + \det{\begin{bmatrix} w \\ v \end{bmatrix}},
 \quad
 \det{\begin{bmatrix} cu \\ v \end{bmatrix}}
 = c \cdot \det{\begin{bmatrix} u \\ v \end{bmatrix}}
 $$
 
 - 내적 (==첫번째 벡터에 대해== 선형성 성립)[^2]
 $$ 
 \langle u+v, w \rangle = \langle u, w \rangle + \langle v, w \rangle, \quad \langle c u, w \rangle = c \langle u, w \rangle
 $$
 
- 외적 (한 벡터에 대해 선형성 성립)

$$
\mathbf{a} \times (\mathbf{b} + \mathbf{c})= \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}, \quad (c \mathbf{a})\times \mathbf{b} = c (\mathbf{a} \times \mathbf{b})
$$

## 학부
- 푸리에 변환 
 $$
 \mathcal{F}(f+g)= \mathcal{F}(f)+ \mathcal{F}(g), \quad \mathcal{F}(cf)= c \mathcal{F}(f)
 $$

- 라플라스 변환 
 $$
 \mathcal{L}(f+g)= \mathcal{L}(f)+ \mathcal{L}(g), \quad \mathcal{L}(cf)= c \mathcal{L}(f)
 $$
 
- 선형 미분 방정식 연산자 
 $$L(y+z)= L(y)+ L(z), \quad L(cy)= cL(y) $$
 
- 맥스웰 방정식
 $$
 \nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}, \quad \nabla \times \mathbf{B} - \frac{1}{c^2} \frac{\partial \mathbf{E}}{\partial t} = \mu_0 \mathbf{J}
 $$
- 파동 방정식

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u, \quad (\Box u = 0)
$$

- 슈뢰딩거 방정식 
 $$ i\hbar \frac{\partial}{\partial t} \Psi = H \Psi, \quad H(\Psi_1 + \Psi_2)= H\Psi_1 + H\Psi_2 $$

- 아인슈타인 장 방정식
 $$
 G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
 $$

[^1]: 단, 더하는 순서가 바뀌면 수렴하지 않을 수 있다. 절대 수렴 $\sum |a_n | < \infty$인 경우에는 더하는 순서가 바뀌어도 수렴한다. 절대 수렴하지 않는다면, 리만 재배열 정리(Riemann Rearrangement Theorem)에 의해 어떤 방식으로 재배열(rearrangement)하느냐에 따라 급수의 합이 다르게 나올 수도 있다.
[^2]: 두 번째 벡터에 대해서는 성립하지 않는다. $\langle x, cy \rangle$ = $\bar{c} \langle x, y \rangle$