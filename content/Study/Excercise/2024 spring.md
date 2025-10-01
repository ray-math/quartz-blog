### 1. Let $S \subset \mathbb{R}^3$ be a smooth surface. Let $f: S \to \mathbb{R}$ be a smooth function. Let $p \in S$ be a point such that the differential $(df)_p$ is not zero as a linear map from $T_pS$ to $\mathbb{R}$. Let $c := f(p)$. Show that the inverse image $f^{-1}(c)$ is a curve containing $p$; more precisely, there exists an open neighborhood $V \subset S$ of $p$ and an injective smooth curve $X:(-a, a) \to S$ (for some $a > 0$) such that $X(0) = p$ and the image $X((-a, a))$ is equal to $f^{-1}(c) \cap V$.
#### Theorem
**음함수 정리 (Implicit Function Theorem)**

$S$가 2차원 매끄러운 곡면이고 $f: S \to \mathbb{R}$가 매끄러운 함수라고 하자. 점 $p \in S$에서 $f$의 미분 $(df)_p: T_pS \to \mathbb{R}$가 전사 함수(surjective linear map)이면 (즉, $(df)_p \neq 0$), $c=f(p)$에 대해 $p$를 포함하는 $f^{-1}(c)$의 근방은 매끄러운 1차원 부분다양체(곡선)이다.

이는 $p$ 근방에서 곡면 $S$의 좌표계를 $(u,v)$로 잡고 $f$를 이 좌표에 대한 함수로 보았을 때, $(df)_p \neq 0$ 조건은 $\frac{\partial f}{\partial u}(p)$ 또는 $\frac{\partial f}{\partial v}(p)$ 중 적어도 하나가 0이 아님을 의미한다. 만약 $\frac{\partial f}{\partial v}(p) \neq 0$ 이라면, 음함수 정리에 의해 $f(u,v) - c = 0$ 방정식은 $p$ 근방에서 $v$를 $u$에 대한 매끄러운 함수 $g(u)$로 표현할 수 있게 해준다. 즉, $v=g(u)$이다. 따라서, $p$ 근방에서 $f^{-1}(c)$는 $t \mapsto (t, g(t))$ 형태의 곡선으로 매개화될 수 있다.

#### Answer
$S$는 $\mathbb{R}^3$ 안의 2차원 매끄러운 곡면이므로, 점 $p \in S$ 근방의 열린 집합 $W \subset \mathbb{R}^2$와 매끄러운 사상 $\mathbf{x}: W \to S$가 존재하여 $\mathbf{x}(q) = p$이고, 미분 $d\mathbf{x}_q$가 단사(injective)인 좌표 조각(coordinate chart)을 잡을 수 있다.

함수 $f: S \to \mathbb{R}$를 이 좌표 조각을 이용해 $g = f \circ \mathbf{x}: W \to \mathbb{R}$로 표현할 수 있다. $g$는 매끄러운 함수이다. $p = \mathbf{x}(q)$라 하면 $f(p)=c$는 $g(q)=c$와 같다.

문제의 조건에서 $(df)_p \neq 0$이다. 연쇄 법칙에 의해 $(dg)_q = (df)_{\mathbf{x}(q)} \circ (d\mathbf{x})_q = (df)_p \circ (d\mathbf{x})_q$ 이다. $d\mathbf{x}_q$는 동형사상(isomorphism)이므로, $(df)_p \neq 0$ 이라는 것은 $(dg)_q \neq 0$ 임을 의미한다. $W$가 $\mathbb{R}^2$의 열린 집합이므로, $q=(u_0, v_0)$라 하면 $(dg)_q$는 행렬 $[\frac{\partial g}{\partial u}(q) \quad \frac{\partial g}{\partial v}(q)]$로 표현된다. 따라서, 두 편도함수 중 적어도 하나는 0이 아니다.

일반성을 잃지 않고 $\frac{\partial g}{\partial v}(q) \neq 0$ 라고 가정하자. 그러면 $\mathbb{R}^2$에 대한 음함수 정리에 의해, $q=(u_0, v_0)$를 포함하는 열린 근방 $U_0 \times V_0 \subset W$와 매끄러운 함수 $h: U_0 \to V_0$가 존재하여, 모든 $u \in U_0$에 대해 $g(u, h(u)) = c$를 만족한다. 또한, $g(u,v)=c$를 만족하는 $(u,v) \in U_0 \times V_0$는 반드시 $v=h(u)$ 형태를 가진다.

이제 $a>0$를 충분히 작게 선택하여 $(-a, a)+u_0 \subset U_0$가 되도록 하고, 곡선 $\gamma: (-a, a) \to W$를 $\gamma(t) = (t+u_0, h(t+u_0))$로 정의하자. 그러면 이 곡선은 단사(injective)이고 매끄럽다.

우리가 찾는 곡선 $X: (-a, a) \to S$를 $X = \mathbf{x} \circ \gamma$로 정의하자. $V = \mathbf{x}(U_0 \times V_0)$는 $p$의 열린 근방이다.
1. $X(0) = \mathbf{x}(\gamma(0)) = \mathbf{x}(u_0, h(u_0)) = \mathbf{x}(u_0, v_0) = p$ 이다.
2. $\mathbf{x}$와 $\gamma$가 단사이므로 $X$도 단사(injective)이다.
3. $X$의 상(image)은 $f^{-1}(c) \cap V$와 같다. 임의의 $t \in (-a, a)$에 대해 $f(X(t)) = f(\mathbf{x}(\gamma(t))) = g(\gamma(t)) = g(t+u_0, h(t+u_0)) = c$ 이므로, $X((-a, a)) \subset f^{-1}(c) \cap V$ 이다. 역으로, $y \in f^{-1}(c) \cap V$ 라면, $y = \mathbf{x}(u,v)$인 $(u,v) \in U_0 \times V_0$가 존재하고, $f(y)=c$ 이므로 $g(u,v)=c$이다. 음함수 정리에 의해 $v=h(u)$이고 $u \in U_0$이다. $t = u-u_0$라고 두면, $(u,v) = \gamma(t)$를 만족하는 $t$를 찾을 수 있으므로 $y \in X((-a, a))$이다.

따라서, $f^{-1}(c)$는 $p$를 포함하는 곡선임이 증명되었다.



### 2. Compute the Gauss curvature at $p = (0,0,0)$ of the smooth surface given by $z = y^2 - x^2$.
#### Theorem
**그래프로 주어진 곡면의 가우스 곡률 (Gauss Curvature of a Surface as a Graph)**

매끄러운 함수 $f(x, y)$에 의해 $z=f(x,y)$로 정의된 곡면의 가우스 곡률 $K$는 다음 공식으로 계산된다.

$$
K = \frac{f_{xx}f_{yy} - f_{xy}^2}{(1 + f_x^2 + f_y^2)^2}
$$

여기서 $f_x, f_y$는 $f$의 1계 편도함수이고, $f_{xx}, f_{yy}, f_{xy}$는 2계 편도함수이다.

#### Answer
주어진 곡면은 $z = f(x,y) = y^2 - x^2$ 이다. 가우스 곡률을 계산하기 위해 점 $p=(0,0,0)$에 해당하는 $(x,y)=(0,0)$에서 $f$의 1계 및 2계 편도함수를 구해야 한다.

1. 1계 편도함수 계산:
* $f_x = \frac{\partial}{\partial x}(y^2 - x^2) = -2x$
* $f_y = \frac{\partial}{\partial y}(y^2 - x^2) = 2y$

2. $(x,y)=(0,0)$에서 1계 편도함수 값:
* $f_x(0,0) = -2(0) = 0$
* $f_y(0,0) = 2(0) = 0$

3. 2계 편도함수 계산:
* $f_{xx} = \frac{\partial}{\partial x}(-2x) = -2$
* $f_{yy} = \frac{\partial}{\partial y}(2y) = 2$
* $f_{xy} = \frac{\partial}{\partial y}(-2x) = 0$

4. $(x,y)=(0,0)$에서 2계 편도함수 값:
* $f_{xx}(0,0) = -2$
* $f_{yy}(0,0) = 2$
* $f_{xy}(0,0) = 0$

5. 가우스 곡률 공식에 대입:

$$
K(0,0) = \frac{f_{xx}(0,0)f_{yy}(0,0) - (f_{xy}(0,0))^2}{(1 + (f_x(0,0))^2 + (f_y(0,0))^2)^2}
$$



$$
K(0,0) = \frac{(-2)(2) - 0^2}{(1 + 0^2 + 0^2)^2} = \frac{-4}{1^2} = -4
$$

따라서 점 $p=(0,0,0)$에서 주어진 곡면의 가우스 곡률은 $-4$이다.



### 3. Let $S \subset \mathbb{R}^3$ be a smooth surface with a smooth unit normal vector field $N:S \to \mathbb{R}^3$. Show that there exists a family of coordinate neighborhoods $X_i: U_i \to S$ for $i \in I$ (so that the union of all $X_i(U_i)$ is equal to $S$) such that whenever $X_i(U_i) \cap X_j(U_j) \neq \emptyset$, the corresponding Jacobian of the coordinate change is positive.
#### Theorem
**향이 있는 곡면 (Orientable Surface)**

$\mathbb{R}^3$ 안의 매끄러운 곡면 $S$가 **향을 줄 수 있다(orientable)** 는 것은 다음의 동치 조건 중 하나를 만족하는 것이다.
1. 곡면 전체에 걸쳐 연속적으로 변하는 매끄러운 단위 법선 벡터장 $N: S \to \mathbb{R}^3$가 존재한다.
2. 곡면을 덮는 좌표근방(atlas) $\{X_i: U_i \to S\}$가 존재하여, 두 좌표근방이 겹치는 영역에서 좌표 변환 함수 $X_j^{-1} \circ X_i$의 야코비안 행렬식(Jacobian determinant) 값이 항상 양수가 되게 할 수 있다. 이러한 atlas를 향이 있는 아틀라스(oriented atlas) 라고 한다.

이 문제는 조건 1이 성립할 때 조건 2가 성립함을 보이는 것이다.

#### Answer
문제에서 매끄러운 단위 법선 벡터장 $N: S \to \mathbb{R}^3$이 존재한다고 주어졌다. 이는 곡면 $S$가 향을 줄 수 있다는 정의이다. 우리는 이로부터 야코비안 행렬식 값이 양수인 좌표근방들의 집합(atlas)을 구성할 수 있음을 보여야 한다.

1. 먼저, 곡면 $S$를 덮는 임의의 좌표근방들의 집합 $\{Y_\alpha: V_\alpha \to S\}_{\alpha \in A}$를 생각하자. 각 좌표 조각 $Y_\alpha(u,v)$에 대해, 접평면의 기저는 $Y_{\alpha,u} = \frac{\partial Y_\alpha}{\partial u}$와 $Y_{\alpha,v} = \frac{\partial Y_\alpha}{\partial v}$로 주어진다. 이로부터 유도되는 지역적인 단위 법선 벡터는 다음과 같다.

$$
n_\alpha = \frac{Y_{\alpha,u} \times Y_{\alpha,v}}{|Y_{\alpha,u} \times Y_{\alpha,v}|}
$$

2. 각 점 $p \in Y_\alpha(V_\alpha)$에서, 지역 법선 벡터 $n_\alpha(p)$는 주어진 전역 법선 벡터 $N(p)$와 같거나, 또는 $n_\alpha(p) = -N(p)$이다.

3. 이제 새로운 좌표근방들의 집합 $\{X_i: U_i \to S\}_{i \in I}$을 다음과 같이 구성한다.
* 만약 $n_\alpha$가 $Y_\alpha(V_\alpha)$ 상에서 $N$과 같은 방향을 가지면 (즉, $n_\alpha \cdot N > 0$), 원래의 좌표 조각을 그대로 사용한다: $X_i = Y_\alpha$.
* 만약 $n_\alpha$가 $N$과 반대 방향을 가지면 (즉, $n_\alpha \cdot N < 0$), 좌표의 순서를 바꾸어 새로운 좌표 조각을 정의한다. $V_\alpha \subset \mathbb{R}^2$의 좌표를 $(u,v)$라 할 때, 새로운 좌표 조각 $X_i: U_i \to S$를 $X_i(u', v') = Y_\alpha(v', u')$로 정의한다. (여기서 $U_i$는 $V_\alpha$와 점들의 집합으로서는 같지만 좌표 순서가 다르다.) 이 새로운 좌표 조각의 편도함수는 $X_{i,u'} = Y_{\alpha,v'}$ 이고 $X_{i,v'} = Y_{\alpha,u'}$ 이다. 따라서 새로운 지역 법선 벡터는 다음과 같다.

$$
\frac{X_{i,u'} \times X_{i,v'}}{|X_{i,u'} \times X_{i,v'}|} = \frac{Y_{\alpha,v'} \times Y_{\alpha,u'}}{|Y_{\alpha,v'} \times Y_{\alpha,u'}|} = -\frac{Y_{\alpha,u'} \times Y_{\alpha,v'}}{|Y_{\alpha,u'} \times Y_{\alpha,v'}|} = -n_\alpha
$$

이 경우 새로운 법선 벡터는 $N$과 같은 방향을 가지게 된다.

4. 이렇게 구성된 새로운 atlas $\{X_i\}$는 $S$를 덮으며, 모든 $i$에 대해 $X_i$로부터 유도된 법선 벡터는 전역 법선 벡터 $N$과 같은 방향을 가진다.

5. 이제 두 좌표근방 $X_i(U_i)$와 $X_j(U_j)$가 겹친다고 가정하자. 겹치는 영역에서 좌표 변환 함수는 $\phi = X_i^{-1} \circ X_j$ 이다. $U_j$의 좌표를 $(u,v)$, $U_i$의 좌표를 $(\tilde{u},\tilde{v})$라 하자. 연쇄 법칙에 의해 다음 관계가 성립한다.

$$
\frac{\partial X_j}{\partial u} = \frac{\partial X_i}{\partial \tilde{u}}\frac{\partial \tilde{u}}{\partial u} + \frac{\partial X_i}{\partial \tilde{v}}\frac{\partial \tilde{v}}{\partial u}
$$



$$
\frac{\partial X_j}{\partial v} = \frac{\partial X_i}{\partial \tilde{u}}\frac{\partial \tilde{u}}{\partial v} + \frac{\partial X_i}{\partial \tilde{v}}\frac{\partial \tilde{v}}{\partial v}
$$

벡터곱을 계산하면 다음과 같은 관계식을 얻는다.

$$
\frac{\partial X_j}{\partial u} \times \frac{\partial X_j}{\partial v} = \left(\frac{\partial \tilde{u}}{\partial u}\frac{\partial \tilde{v}}{\partial v} - \frac{\partial \tilde{u}}{\partial v}\frac{\partial \tilde{v}}{\partial u}\right) \left(\frac{\partial X_i}{\partial \tilde{u}} \times \frac{\partial X_i}{\partial \tilde{v}}\right) = \det(J_\phi) \left(\frac{\partial X_i}{\partial \tilde{u}} \times \frac{\partial X_i}{\partial \tilde{v}}\right)
$$

여기서 $J_\phi$는 좌표 변환 $\phi$의 야코비안 행렬이다.

6. 우리의 구성에 의해, 두 법선 벡터 $\frac{\partial X_j}{\partial u} \times \frac{\partial X_j}{\partial v}$ 와 $\frac{\partial X_i}{\partial \tilde{u}} \times \frac{\partial X_i}{\partial \tilde{v}}$는 모두 전역 법선 벡터 $N$과 같은 방향을 가리킨다. 따라서 이 두 벡터는 서로 양의 스칼라배 관계에 있다. 이는 $\det(J_\phi)$가 반드시 양수여야 함을 의미한다.

따라서, 주어진 조건을 만족하는 좌표근방들의 집합이 존재한다.



### 4. Let $X$ be a compact Hausdorff space. Show that $X$ is metrizable if and only if $X$ has a countable basis.
#### Theorem
**유리존 거리화 정리 (Urysohn's Metrization Theorem)**

위상공간 $X$가 거리화 가능하다(metrizable)는 것은 $X$의 위상과 같은 위상을 유도하는 거리 함수가 존재한다는 의미이다. 유리존 거리화 정리에 따르면, 제2가산(second-countable, 가산 기저를 가짐)이고 정칙(regular)인 하우스도르프 공간은 거리화 가능하다.

특히, **콤팩트 하우스도르프 공간은 정칙 공간(regular space)이며 정규 공간(normal space)이기도 하다.** 따라서 콤팩트 하우스도르프 공간에 대해서는, 제2가산인 것과 거리화 가능한 것이 동치이다.

#### Answer

**($\implies$) $X$가 거리화 가능하면, 가산 기저를 가진다.**

1. $X$가 거리화 가능하다고 가정하자. 이는 $X$의 위상을 유도하는 거리 함수 $d$가 존재함을 의미한다. $X$는 콤팩트 공간이다.
2. 각 자연수 $n \in \mathbb{N}$에 대해, 반지름이 $1/n$인 열린 공들의 집합 $\{B(x, 1/n) : x \in X\}$는 $X$의 열린 덮개(open cover)를 이룬다.
3. $X$는 콤팩트이므로, 이 열린 덮개는 유한 부분덮개(finite subcover)를 가진다. 즉, 각 $n$에 대해 유한 집합 $\{x_{n,k}\}_{k=1}^{K_n} \subset X$가 존재하여 $X = \bigcup_{k=1}^{K_n} B(x_{n,k}, 1/n)$를 만족한다.
4. 이제 모든 자연수 $n$에 대한 이러한 유한 개의 공들을 모두 모은 집합 $\mathcal{B} = \{ B(x_{n,k}, 1/n) : n \in \mathbb{N}, 1 \le k \le K_n \}$를 생각하자. $\mathcal{B}$는 가산 개의 열린 집합들의 모임이다.
5. $\mathcal{B}$가 $X$의 기저(basis)임을 보이자. $U$를 $X$의 임의의 열린 집합이라 하고, $p \in U$라 하자. $U$가 열린 집합이므로, $B(p, \epsilon) \subset U$를 만족하는 $\epsilon > 0$이 존재한다. $2/n < \epsilon$을 만족하는 자연수 $n$을 선택하자.
6. $\{B(x_{n,k}, 1/n)\}_{k=1}^{K_n}$는 $X$를 덮으므로, $p \in B(x_{n,k}, 1/n)$인 $k$가 존재한다.
7. 이때, 임의의 점 $y \in B(x_{n,k}, 1/n)$에 대해, 삼각부등식에 의해 $d(y, p) \le d(y, x_{n,k}) + d(x_{n,k}, p) < 1/n + 1/n = 2/n < \epsilon$ 이다.
8. 이는 $B(x_{n,k}, 1/n) \subset B(p, \epsilon) \subset U$임을 의미한다. 따라서 $\mathcal{B}$는 $X$의 위상에 대한 기저이다.
9. $\mathcal{B}$는 가산 집합이므로, $X$는 가산 기저를 가진다.

**($\impliedby$) $X$가 가산 기저를 가지면, 거리화 가능하다.**

1. $X$가 가산 기저 $\mathcal{B}=\{B_n\}_{n=1}^\infty$를 가진 콤팩트 하우스도르프 공간이라고 가정하자. 콤팩트 하우스도르프 공간은 정규 공간(normal space)이다.
2. 기저의 원소 쌍 $(B_i, B_j)$ 중에서 $\overline{B_i} \subset B_j$를 만족하는 쌍들의 집합을 생각하자. 이 집합은 가산 집합이다. $X$가 정규 공간이므로, 이러한 각 쌍에 대해 유리존의 보조정리(Urysohn's Lemma) 를 적용할 수 있다. 즉, 연속 함수 $f_{ij}: X \to [0,1]$이 존재하여 $f_{ij}|_{\overline{B_i}} = 1$이고 $f_{ij}|_{X \setminus B_j} = 0$이다.
3. 이렇게 만들어진 함수들의 가산 집합을 $\{g_k\}_{k=1}^\infty$라고 하자.
4. 이제 사상 $F: X \to [0,1]^\mathbb{N}$ (힐베르트 큐브)를 다음과 같이 정의한다.

$$
F(x) = \left(g_1(x), \frac{g_2(x)}{2}, \frac{g_3(x)}{3}, \dots \right)
$$

힐베르트 큐브는 거리 공간이며, 따라서 그 부분 공간도 거리 공간이다. 각 성분 함수 $g_k(x)/k$가 연속이므로 $F$는 연속 함수이다.
5. $F$가 단사(injective)임을 보이자. $x, y \in X$이고 $x \neq y$라고 하자. $X$는 하우스도르프 공간이므로 $x$를 포함하고 $y$를 포함하지 않는 열린 집합 $U$가 존재한다. 기저의 정의에 의해, $x \in B_j \subset U$인 $B_j \in \mathcal{B}$가 존재한다. $X$는 정칙 공간이므로, $x \in B_i \subset \overline{B_i} \subset B_j$를 만족하는 $B_i \in \mathcal{B}$도 존재한다. 그러면 $\overline{B_i} \subset B_j$이고 $y \notin B_j$이다. 이 쌍 $(B_i, B_j)$에 해당하는 함수 $g_k=f_{ij}$가 존재하여 $g_k(x)=1$이고 $g_k(y)=0$이다. 따라서 $F(x) \neq F(y)$이므로 $F$는 단사이다.
6. $X$는 콤팩트 공간이고, $F$는 연속이므로 그 상 $F(X)$ 또한 힐베르트 큐브의 콤팩트 부분 공간이다. 힐베르트 큐브는 하우스도르프 공간이므로 그 부분 공간인 $F(X)$도 하우스도르프 공간이다.
7. 결론적으로 $F: X \to F(X)$는 콤팩트 공간에서 하우스도르프 공간으로 가는 연속인 전단사 함수이다. 이러한 함수는 위상동형사상(homeomorphism)이다.
8. 따라서 $X$는 거리 공간인 $F(X)$와 위상동형이므로, $X$는 거리화 가능하다.



### 5. If $(X,d)$ is a metric space, recall that a map $f: X \to X$ is called a *contraction* if there is a number $\alpha < 1$ such that $d(f(x), f(y)) \le \alpha d(x,y)$ for all $x,y \in X$. Show that if $f$ is a contraction of a complete metric space, then there is a unique point $x \in X$ such that $f(x)=x$.
#### Theorem
**바나흐 고정점 정리 (Banach Fixed-Point Theorem) 또는 축소 사상 원리 (Contraction Mapping Principle)**

$(X, d)$가 비어있지 않은 완비 거리 공간(complete metric space)이고, $f: X \to X$가 축소 사상(contraction mapping)이라고 하자. 그러면 $f$는 유일한 고정점(fixed point)을 가진다. 즉, $f(x)=x$를 만족하는 점 $x \in X$가 단 하나 존재한다.

#### Answer
증명은 **존재성(existence)** 과 **유일성(uniqueness)** 의 두 부분으로 나뉜다.

**1. 고정점의 존재성 증명

1. $X$에서 임의의 점 $x_0$를 선택하자. 그리고 수열 $\{x_n\}$을 다음과 같이 재귀적으로 정의한다.

$$
x_{n+1} = f(x_n) \quad (n=0, 1, 2, \dots)
$$

2. 이 수열이 코시 수열(Cauchy sequence)임을 보이자.
$d(x_{n+1}, x_n) = d(f(x_n), f(x_{n-1})) \le \alpha d(x_n, x_{n-1})$ 이다.
이를 반복적으로 적용하면 다음을 얻는다.

$$
d(x_{n+1}, x_n) \le \alpha d(x_n, x_{n-1}) \le \alpha^2 d(x_{n-1}, x_{n-2}) \le \dots \le \alpha^n d(x_1, x_0)
$$

3. 이제 임의의 $m > n$에 대해, 삼각부등식을 이용하여 $d(x_m, x_n)$을 계산하자.

$$
\begin{aligned} d(x_m, x_n) &\le d(x_m, x_{m-1}) + d(x_{m-1}, x_{m-2}) + \dots + d(x_{n+1}, x_n) \\ &\le (\alpha^{m-1} + \alpha^{m-2} + \dots + \alpha^n) d(x_1, x_0) \\ &= \alpha^n (1 + \alpha + \dots + \alpha^{m-n-1}) d(x_1, x_0) \end{aligned}
$$

$0 \le \alpha < 1$ 이므로, 등비급수 합 공식에 의해 $1 + \alpha + \dots + \alpha^{m-n-1} < \sum_{k=0}^{\infty} \alpha^k = \frac{1}{1-\alpha}$ 이다.
따라서,

$$
d(x_m, x_n) < \frac{\alpha^n}{1-\alpha} d(x_1, x_0)
$$

4. $n \to \infty$ 일 때 $\alpha^n \to 0$ 이므로, 임의의 $\epsilon > 0$에 대해 충분히 큰 $N$을 잡으면 모든 $m, n > N$에 대해 $d(x_m, x_n) < \epsilon$ 이 되도록 할 수 있다. 따라서 $\{x_n\}$은 코시 수열이다.
5. $X$는 완비 거리 공간(complete metric space)이므로, 모든 코시 수열은 $X$ 안의 한 점으로 수렴한다. 이 극한값을 $x$라고 하자. 즉, $\lim_{n \to \infty} x_n = x$ 이다.
6. 이 극한점 $x$가 $f$의 고정점임을 보이자. 축소 사상은 립시츠 연속(Lipschitz continuous)이므로 연속 함수이다. 따라서,

$$
f(x) = f(\lim_{n \to \infty} x_n) = \lim_{n \to \infty} f(x_n) = \lim_{n \to \infty} x_{n+1} = x
$$

그러므로 $f(x)=x$ 이고, 고정점이 존재한다.

**2. 고정점의 유일성 증명

1. $x$와 $y$가 $f$의 두 고정점이라고 가정하자. 즉, $f(x)=x$ 이고 $f(y)=y$ 이다.
2. 두 점 사이의 거리를 생각하면,

$$
d(x, y) = d(f(x), f(y))
$$

3. $f$가 축소 사상이므로,

$$
d(f(x), f(y)) \le \alpha d(x, y)
$$

4. 위 두 식을 결합하면 $d(x, y) \le \alpha d(x, y)$ 이다. 이를 이항하면,

$$
(1-\alpha)d(x, y) \le 0
$$

5. 가정에서 $\alpha < 1$ 이므로 $1-\alpha > 0$ 이다. 또한 거리 함수는 항상 $d(x,y) \ge 0$ 이다.
6. 따라서 위 부등식이 성립하기 위한 유일한 가능성은 $d(x,y)=0$ 이다.
7. 거리 공간의 정의에 따라 $d(x,y)=0$은 $x=y$와 동치이다.

그러므로 고정점은 유일하다.


---

알겠습니다. 이전 피드백을 반영하여, 증명 개요가 아닌 완전하고 엄밀한 형태의 답안을 작성하겠습니다.


### 14번 문제

**문제:** 콤팩트 하우스도르프 공간 $X$를 생각하자. $X$가 **거리화 가능 공간(metrizable)** 인 것과 $X$가 **가산 기저(countable basis)** 를 갖는 것이 동치임을 보이시오.

**답안:**
양방향의 필요충분조건이므로 각각 증명한다.

#### (⇒) $X$가 콤팩트 거리화 가능 공간이면, $X$는 가산 기저를 갖는다.

1. 1단계: $X$가 분리가능(separable)함을 보인다.
$X$가 콤팩트 거리 공간이라고 가정하자. 모든 자연수 $n \ge 1$에 대해, 반지름이 $1/n$인 열린 공들의 모임 $\mathcal{C}_n = \{B(x, 1/n) \mid x \in X\}$는 $X$의 열린 덮개이다. $X$는 콤팩트하므로, 각 $\mathcal{C}_n$은 유한 부분 덮개를 갖는다. 이 유한 부분 덮개를 구성하는 공들의 중심점 집합을 $D_n$이라 하자. $D_n$은 유한 집합이다.
이제 $D = \bigcup_{n=1}^\infty D_n$라고 정의하자. $D$는 가산 집합들의 가산 합집합이므로 가산 집합이다.
$D$가 $X$에서 조밀함을 보이자. $X$의 임의의 점 $x$와 임의의 $\epsilon > 0$에 대해, $1/n < \epsilon$을 만족하는 자연수 $n$을 선택한다. $D_n$에 해당하는 중심점들의 공들이 $X$를 덮으므로, $x \in B(d, 1/n)$을 만족하는 $d \in D_n$이 존재한다. 이는 $d(x, d) < 1/n < \epsilon$을 의미하므로, $x$의 임의의 근방은 $D$의 점을 포함한다. 따라서 $D$는 가산 조밀 부분집합이고, $X$는 분리가능하다.

2. 2단계: 분리가능한 거리 공간이 가산 기저를 가짐을 보인다.
$D$를 위에서 찾은 가산 조밀 부분집합이라 하자. 다음과 같은 열린 공들의 모임 $\mathcal{B}$를 생각한다.

$$
\mathcal{B} = \{B(d, q) \mid d \in D, q \in \mathbb{Q}^+\}
$$

$D$와 $\mathbb{Q}^+$가 모두 가산 집합이므로 $\mathcal{B}$는 가산 집합족이다. $\mathcal{B}$가 $X$의 기저임을 보이자.
$X$의 임의의 열린 집합 $U$와 그 안의 임의의 점 $x$를 선택하자. $U$는 열린 집합이므로 $B(x, \epsilon) \subseteq U$인 $\epsilon > 0$이 존재한다. $D$가 조밀하므로 $d(x, d) < \epsilon/2$인 $d \in D$가 존재한다. 또한, 유리수의 조밀성에 의해 $d(x, d) < q < \epsilon/2$인 유리수 $q$를 선택할 수 있다.
이때 $B(d, q) \in \mathcal{B}$이고 $x \in B(d, q)$이다. 또한 임의의 점 $y \in B(d, q)$에 대해, 삼각 부등식에 의해 $d(y, x) \le d(y, d) + d(d, x) < q + \epsilon/2 < \epsilon/2 + \epsilon/2 = \epsilon$ 이다. 따라서 $B(d, q) \subseteq B(x, \epsilon) \subseteq U$ 이다.
그러므로 $\mathcal{B}$는 $X$의 가산 기저이다.


#### (⇐) $X$가 콤팩트 하우스도르프이고 가산 기저를 가지면, $X$는 거리화 가능하다.

1. 1단계: $X$가 정칙(regular) 공간임을 확인한다.
콤팩트 하우스도르프 공간은 정규(normal, $T_4$) 공간이라는 것이 잘 알려진 정리이다. 모든 정규 하우스도르프($T_1$) 공간은 정칙($T_3$) 공간이다. 따라서 $X$는 정칙 공간이다.

2. 2단계: 우리손 매장 정리(Urysohn Embedding Theorem)를 이용한 증명
$X$가 정칙이고 가산 기저를 갖는 공간이므로, **우리손의 거리화 정리** 에 의해 거리화 가능하다. 아래는 그 증명의 구성 과정이다.
* $\mathcal{B} = \{B_n\}_{n=1}^\infty$를 $X$의 가산 기저라 하자. $\bar{B_i} \subseteq B_j$를 만족하는 기저 원소의 순서쌍 $(B_i, B_j)$들의 모임은 가산 집합이다. 이 순서쌍들을 자연수 $k=1, 2, \dots$로 번호 매기자.
* 각 $k$에 대해, $\bar{B_{i_k}}$와 $X \setminus B_{j_k}$는 서로소인 닫힌 집합이다. $X$가 정규 공간이므로, **우리손의 보조정리(Urysohn's Lemma)** 에 의해 연속 함수 $f_k: X \to [0, 1]$가 존재하여, $f_k(\bar{B_{i_k}}) = \{0\}$, $f_k(X \setminus B_{j_k}) = \{1\}$을 만족한다.
* 거리 공간인 힐베르트 큐브 $H = \prod_{k=1}^\infty [0, 1]_k$ 를 생각하자.
* 함수 $F: X \to H$를 $F(x) = (f_1(x), f_2(x), \dots)$ 로 정의한다.
* **$F$가 매장(embedding)임을 보인다:**
a. **연속성:** 각 좌표 함수 $f_k$가 연속이므로, 곱위상의 정의에 의해 $F$는 연속이다.
b. **단사성(Injectivity):** 서로 다른 두 점 $x, y \in X$를 생각하자. $X$는 하우스도르프이므로 $x \in B_j$이고 $y \notin B_j$인 $B_j \in \mathcal{B}$가 존재한다. 또한 $X$는 정칙이므로 $x \in B_i$이고 $\bar{B_i} \subseteq B_j$인 $B_i \in \mathcal{B}$를 찾을 수 있다. 이 순서쌍 $(B_i, B_j)$에 해당하는 함수 $f_k$에 대해 $f_k(x) = 0$, $f_k(y)=1$이므로 $F(x) \neq F(y)$이다. 따라서 $F$는 단사이다.
c. **위상동형사상:** $F$는 콤팩트 공간 $X$에서 하우스도르프 공간 $H$로 가는 연속인 단사 함수이므로, 그 상(image) $F(X)$와는 위상동형사상이다.
* $X$가 거리 공간 $H$의 부분 공간과 위상동형이므로, $X$는 거리화 가능하다.


### 15번 문제 답안 (바나흐 고정점 정리)

**문제:** $f$가 완비 거리 공간의 축소 사상이라면, $f(x)=x$를 만족하는 유일한 점 $x$가 $X$에 존재함을 보이시오.

**답안:**
증명은 **존재성** 과 **유일성** 으로 나뉜다.

#### 1. 고정점의 존재성 (Existence)

1. $X$에서 임의의 점 $x_0$를 선택하고, 수열 $\{x_n\}$을 점화식 $x_{n+1} = f(x_n)$으로 정의한다.
2. 이 수열이 코시 수열임을 보인다. 먼저 $m > n$인 자연수에 대해,

$$
d(x_{n+1}, x_n) = d(f(x_n), f(x_{n-1})) \le \alpha d(x_n, x_{n-1}) \le \dots \le \alpha^n d(x_1, x_0)
$$

삼각 부등식과 위 부등식을 이용하면,

$$
d(x_m, x_n) \le \sum_{i=n}^{m-1} d(x_{i+1}, x_i) \le \sum_{i=n}^{m-1} \alpha^i d(x_1, x_0) = \alpha^n(1+\alpha+\dots+\alpha^{m-n-1})d(x_1,x_0)
$$

무한 등비급수 합을 이용하면,

$$
d(x_m, x_n) < \alpha^n \left(\sum_{k=0}^{\infty} \alpha^k\right) d(x_1, x_0) = \frac{\alpha^n}{1-\alpha} d(x_1, x_0)
$$

3. $0 \le \alpha < 1$ 이므로 $\lim_{n \to \infty} \alpha^n = 0$ 이다. 따라서 위 부등식의 우변은 $n \to \infty$ 일 때 0으로 수렴한다. 이는 $\{x_n\}$이 코시 수열임을 의미한다.
4. $X$는 완비 거리 공간 이므로, 코시 수열 $\{x_n\}$은 어떤 점 $x^* \in X$로 수렴한다.
5. 축소 사상은 연속 함수이므로, 극한과 함수 순서를 바꿀 수 있다.

$$
x^* = \lim_{n \to \infty} x_{n+1} = \lim_{n \to \infty} f(x_n) = f\left(\lim_{n \to \infty} x_n\right) = f(x^*)
$$

따라서 $f(x^*) = x^*$ 이므로, 고정점 $x^*$는 존재한다.


#### 2. 고정점의 유일성 (Uniqueness)

1. $p$와 $q$가 $f$의 두 고정점이라고 가정하자. 즉, $f(p)=p$ 이고 $f(q)=q$ 이다.
2. 두 점 사이의 거리를 계산하면 다음과 같다.

$$
d(p, q) = d(f(p), f(q))
$$

3. $f$는 축소 사상이므로,

$$
d(f(p), f(q)) \le \alpha \, d(p, q)
$$

4. 위 두 식을 결합하면 $d(p, q) \le \alpha \, d(p, q)$ 이고, 이를 정리하면,

$$
(1-\alpha) \, d(p, q) \le 0
$$

5. $0 \le \alpha < 1$ 이므로 $(1-\alpha) > 0$ 이다. 또한 거리 $d(p, q) \ge 0$ 이다.
6. 따라서 위 부등식이 성립하기 위한 유일한 가능성은 $d(p, q) = 0$ 이다.
7. 거리의 정의에 의해 $p=q$ 이다. 그러므로 고정점은 유일하다.


---

## 1. 문제 번역

(10점) $S \subset \mathbb{R}^3$를 매끄러운 곡면(smooth surface)이라 하자. $f: S \to \mathbb{R}$를 매끄러운 함수라 하자. $p \in S$를, 미분사상(differential) $(df)_p$가 $T_pS$에서 $\mathbb{R}$로 가는 영선형사상(zero linear map)이 아닌 점이라고 하자. $c := f(p)$라 하자.

이때 역상(inverse image) $f^{-1}(c)$가 $p$를 포함하는 곡선임을 보여라. 더 정확하게는, 다음을 만족하는 $p$의 열린 근방(open neighborhood) $V \subset S$와 단사(injective)인 매끄러운 곡선 $X:(-a, a) \to S$ (어떤 $a>0$에 대해)가 존재함을 보여라:
$X(0) = p$ 이고 곡선의 상(image) $X(-a,a)$는 $f^{-1}(c) \cap V$와 같다.

## 2. 문제 풀이를 위한 필수 개념

이 문제를 증명하기 위해서는 미분다양체 이론의 핵심 정리인 **음함수 정리(Implicit Function Theorem)** 또는 이와 밀접하게 연관된 **정칙값 정리(Regular Value Theorem)** 에 대한 이해가 필요합니다. 💡

* **매끄러운 곡면/다양체 (Smooth Surface/Manifold)**
문제의 공간적 배경인 $S$는 2차원 매끄러운 다양체입니다. 이는 국소적으로(locally) $\mathbb{R}^2$의 열린 집합과 같이 보이며, 이를 통해 미적분을 할 수 있는 좌표계(chart)를 설정할 수 있습니다.

* **미분사상 (Differential, $(df)_p$)**
함수 $f: S \to \mathbb{R}$의 점 $p$에서의 미분(또는 도함수)으로, 접공간 사이의 선형사상 $(df)_p: T_pS \to T_{f(p)}\mathbb{R}$ 입니다. $T_{f(p)}\mathbb{R}$은 $\mathbb{R}$ 자신과 동일시할 수 있으므로, $(df)_p$는 접벡터를 실수로 보내는 선형 함수로 볼 수 있습니다.

* **정칙점 (Regular Point)과 정칙값 (Regular Value)**
* **정칙점:** 점 $p \in S$에서 미분사상 $(df)_p$가 전사 함수(surjective map)일 때, $p$를 $f$의 **정칙점** 이라고 합니다. 공역(codomain)이 1차원인 $\mathbb{R}$이므로, $(df)_p$가 전사라는 것은 영사상이 아니라는 말과 같습니다. 문제의 조건 "$(df)_p$ is not zero"는 가 정칙점임을 명시한 것입니다.
* **정칙값:** 값 $c \in \mathbb{R}$에 대해, 역상 $f^{-1}(c)$에 속하는 모든 점들이 정칙점일 때, $c$를 $f$의 **정칙값** 이라고 합니다.

* **정칙값 정리 (Preimage Theorem/Regular Value Theorem)**
이 문제의 해결에 결정적인 정리입니다. 매끄러운 함수 $f: M \to N$ 와 $N$의 정칙값 $c$에 대해, 역상 $f^{-1}(c)$는 $M$의 부분다양체(submanifold)가 되며, 그 차원은 $\dim(f^{-1}(c)) = \dim(M) - \dim(N)$ 입니다.
* **본 문제에 적용:** $M=S$ (2차원), $N=\mathbb{R}$ (1차원)이므로, 정칙값 $c$에 대한 역상 $f^{-1}(c)$는 $2-1=1$차원 부분다양체가 됩니다. **1차원 다양체는 정의상 곡선(curve)입니다.**

## 3. 완벽한 답안

**증명**

이 명제는 **음함수 정리(Implicit Function Theorem)** 의 직접적인 결과이다. 우리는 $p$ 근방에 국소 좌표계를 설정하고, 이 좌표계에서 다변수 미적분학의 음함수 정리를 적용하여 원하는 매끄러운 곡선 $X(t)$를 구성할 것이다.

1. 국소 좌표계 설정 (Setting up Local Coordinates)
$S$는 2차원 매끄러운 곡면이므로, 점 $p$ 근방에 대한 국소 좌표계(chart) $\phi: U \to S$를 잡을 수 있다. 여기서 $U$는 $\mathbb{R}^2$의 열린 집합이며 $\phi$는 미분동형사상(diffeomorphism)이다. 좌표 계산의 편의를 위해, $U$의 원점 $\mathbf{0}=(0,0)$이 $p$에 대응된다고 하자. 즉, $\phi(\mathbf{0}) = p$이다.

이제, $U$ 위에 정의된 실함수 $F: U \to \mathbb{R}$를 다음과 같이 정의한다.

$$
F = f \circ \phi
$$

$f$와 $\phi$가 모두 매끄러운 함수이므로, 합성 함수인 $F$ 또한 $U$ 위에서 매끄러운($C^\infty$) 함수이다. $F(\mathbf{0}) = f(\phi(\mathbf{0})) = f(p) = c$ 이다.

2. 음함수 정리 조건 확인
다변수 미적분학의 음함수 정리를 $(u_1, u_2) \in U$ 좌표계의 함수 $F$에 적용하기 위해, $F$의 원점 $\mathbf{0}$에서의 야코비 행렬(Jacobian matrix) $J_F(\mathbf{0})$의 계수(rank)를 확인해야 한다.

$$
J_F(\mathbf{0}) = \left[ \frac{\partial F}{\partial u_1}(\mathbf{0}) \quad \frac{\partial F}{\partial u_2}(\mathbf{0}) \right]
$$

연쇄 법칙(chain rule)에 의해, $(df)_p$ 와 $J_F(\mathbf{0})$는 다음과 같은 관계를 가진다. $T_pS$의 기저(basis) 벡터는 $\{\phi_{u_1}(\mathbf{0}), \phi_{u_2}(\mathbf{0})\}$로 주어지며, 이 기저 벡터에 대한 $(df)_p$의 작용은 다음과 같다.

$$
(df)_p(\phi_{u_i}(\mathbf{0})) = d(f \circ \phi)_{\mathbf{0}}(\mathbf{e}_i) = \frac{\partial F}{\partial u_i}(\mathbf{0}) \quad (i=1,2)
$$

문제의 가정에서 $(df)_p$는 영선형사상이 아니므로, $T_pS$의 어떤 벡터 $v$에 대해 $(df)_p(v) \neq 0$이다. 이는 $(df)_p$가 기저 벡터 중 적어도 하나를 0이 아닌 값으로 보내야 함을 의미한다. 따라서, $\frac{\partial F}{\partial u_1}(\mathbf{0})$ 와 $\frac{\partial F}{\partial u_2}(\mathbf{0})$ 중 적어도 하나는 0이 아니다.

이는 야코비 행렬 $J_F(\mathbf{0})$의 계수가 1임을 의미하며, 이는 공역 $\mathbb{R}$의 차원과 같다. 그러므로 음함수 정리를 적용할 수 있다.

3. 음함수 정리 적용 및 곡선 구성
일반성을 잃지 않고 $\frac{\partial F}{\partial u_2}(\mathbf{0}) \neq 0$ 이라고 가정하자. 음함수 정리에 따르면, 원점 $\mathbf{0}$의 적절한 근방 $U_0 \subset U$ 와, 어떤 $a>0$에 대해 정의된 매끄러운 함수 $g:(-a, a) \to \mathbb{R}$ 가 존재하여 다음을 만족한다:
* $g(0) = 0$
* $U_0$ 내의 모든 점 $(u_1, u_2)$에 대해, $F(u_1, u_2) = c$ 인 것과 $u_2=g(u_1)$ 인 것은 동치이다.

이제 이 함수 $g$를 이용하여 $\mathbb{R}^2$의 좌표 공간에서 매끄러운 곡선 $\gamma: (-a, a) \to U_0$ 를 다음과 같이 정의할 수 있다.

$$
\gamma(t) = (t, g(t))
$$

$\gamma$는 $t_1 \neq t_2$ 이면 $\gamma(t_1)$의 첫째 성분과 $\gamma(t_2)$의 첫째 성분이 다르므로 단사(injective)이고, $g$가 매끄러우므로 $\gamma$도 매끄럽다. 또한 $\gamma(0) = (0, g(0)) = (0,0) = \mathbf{0}$이다.

4. 곡면 위의 곡선으로 사상
마지막으로, 좌표계 곡선 $\gamma$를 좌표 사상 $\phi$를 이용해 곡면 $S$ 위의 곡선 $X$로 옮긴다.

$$
X: (-a, a) \to S, \quad X(t) = \phi(\gamma(t)) = \phi(t, g(t))
$$

$p$의 근방 $V$를 $V = \phi(U_0)$로 정의하자. 이제 $X$가 문제의 모든 조건을 만족함을 확인한다.
* **매끄러움:** $X$는 매끄러운 함수 $\phi$와 $\gamma$의 합성 함수이므로 매끄럽다.
* **단사성:** $\gamma$가 단사이고 $\phi$가 (정의상) 단사이므로, $X$는 단사이다.
* **초기 조건:** $X(0) = \phi(\gamma(0)) = \phi(\mathbf{0}) = p$ 이다.
* **상의 일치:** 곡선 $X$의 상 $X(-a,a)$는 $\{\phi(t, g(t)) \mid t \in (-a,a)\}$이다. 음함수 정리의 결과에 의해, 이는 $V$ 내에서 $f$의 값이 $c$가 되는 점들의 집합, 즉 $f^{-1}(c) \cap V$ 와 정확히 일치한다.

따라서, 조건을 만족하는 $p$의 근방 $V$와 매끄러운 곡선 $X$가 존재한다. ∎

---

## 1. 문제 번역

(10점) $z = y^2 - x^2$ 로 주어진 매끄러운 곡면의 점 $p=(0,0,0)$ 에서의 가우스 곡률(Gauss curvature)을 계산하라.

## 2. 문제 풀이를 위한 필수 개념

이 문제를 푸는 데 필요한 핵심 개념은 다음과 같습니다.

* **가우스 곡률 (Gauss Curvature, K)**
곡면 위의 한 점에서의 '휘어짐'을 측정하는 중요한 척도입니다. 이는 주곡률(principal curvatures) $\kappa_1$과 $\kappa_2$의 곱, 즉 $K = \kappa_1 \kappa_2$로 정의됩니다. 가우스 곡률이 양수이면 그 점 근방은 그릇 모양(타원점), 음수이면 말 안장 모양(쌍곡점), 0이면 한쪽 방향으로만 휜 모양(포물점)을 가집니다.
* **그래프 형태의 곡면 (Surface as a Graph)**
곡면이 $z = f(x,y)$ 형태의 함수 그래프로 주어지는 경우, 가우스 곡률을 편도함수를 이용해 직접 계산하는 강력한 공식이 있습니다. 이 문제의 곡면 $z = y^2 - x^2$가 바로 이 형태에 해당합니다. 🐴
* **함수 그래프의 가우스 곡률 공식**
곡면이 $z = f(x,y)$로 주어질 때, 점 $(x,y)$에서의 가우스 곡률 $K(x,y)$는 다음과 같이 계산됩니다.

$$
K = \frac{f_{xx}f_{yy} - f_{xy}^2}{(1 + f_x^2 + f_y^2)^2}
$$

여기서 $f_x, f_y$는 1차 편도함수이고, $f_{xx}, f_{yy}, f_{xy}$는 2차 편도함수를 나타냅니다.

## 3. 완벽한 답안

**목표:** 곡면 $S$가 $z = f(x,y) = y^2 - x^2$로 주어졌을 때, 점 $p=(0,0,0)$에서의 가우스 곡률 $K$를 계산한다.

**방법:** 곡면이 함수의 그래프 $z=f(x,y)$로 표현되므로, $f$의 편도함수를 이용하여 가우스 곡률을 계산하는 표준 공식을 사용한다.

1. 가우스 곡률 공식
$z = f(x,y)$ 형태의 곡면에 대한 가우스 곡률 공식은 다음과 같다.

$$
K(x,y) = \frac{f_{xx}f_{yy} - f_{xy}^2}{(1 + f_x^2 + f_y^2)^2}
$$

2. 편도함수 계산
주어진 함수 $f(x,y) = y^2 - x^2$ 에 대해 필요한 1차 및 2차 편도함수를 구한다.
* **1차 편도함수:**

$$
f_x = \frac{\partial f}{\partial x} = -2x
$$

    

$$
f_y = \frac{\partial f}{\partial y} = 2y
$$

* **2차 편도함수:**

$$
f_{xx} = \frac{\partial^2 f}{\partial x^2} = -2
$$

    

$$
f_{yy} = \frac{\partial^2 f}{\partial y^2} = 2
$$

    

$$
f_{xy} = \frac{\partial^2 f}{\partial x \partial y} = 0
$$

3. 점 $p=(0,0,0)$에서의 편도함수 값 계산
문제의 점 $p=(0,0,0)$은 $x=0, y=0$에 해당한다. 이 지점에서 각 편도함수의 값을 구한다.
* $f_x(0,0) = -2(0) = 0$
* $f_y(0,0) = 2(0) = 0$
* $f_{xx}(0,0) = -2$
* $f_{yy}(0,0) = 2$
* $f_{xy}(0,0) = 0$

4. 공식에 대입하여 가우스 곡률 계산
위에서 계산한 값들을 가우스 곡률 공식에 대입한다.

$$
K(0,0) = \frac{f_{xx}(0,0) \cdot f_{yy}(0,0) - (f_{xy}(0,0))^2}{(1 + (f_x(0,0))^2 + (f_y(0,0))^2)^2}
$$

  

$$
K(0,0) = \frac{(-2)(2) - (0)^2}{(1 + 0^2 + 0^2)^2} = \frac{-4}{1^2} = -4
$$

### 최종 결론
따라서, 곡면 $z = y^2 - x^2$의 점 $p=(0,0,0)$에서의 **가우스 곡률은 -4** 이다.

**기하학적 해석:**
계산된 가우스 곡률 값 $K=-4$는 음수이다. 이는 점 $p=(0,0,0)$이 **쌍곡점(hyperbolic point)** 임을 의미한다. 기하학적으로, 이 점 근방에서 곡면은 주곡률의 부호가 서로 반대인 '말 안장' 모양을 가진다. 이는 $z = y^2 - x^2$가 쌍곡 포물면(hyperbolic paraboloid)이라는 사실과 일치하는 결과이다. 

---
## 1. 문제 번역

(10점) $S \subset \mathbb{R}^3$를 매끄러운 단위 법선 벡터장(smooth unit normal vector field) $N: S \to \mathbb{R}^3$을 갖는 매끄러운 곡면이라 하자. 다음을 만족하는 좌표 근방(coordinate neighborhoods)들의 집합(family) $\{X_i: U_i \to S\}_{i \in I}$ (단, 모든 $X_i(U_i)$의 합집합은 $S$와 같다)가 존재함을 보여라:
$X_i(U_i) \cap X_j(U_j) \neq \emptyset$일 때마다, 해당하는 좌표 변환(coordinate change)의 야코비안(Jacobian) 행렬식이 양수이다.

## 2. 문제 풀이를 위한 필수 개념

이 문제는 곡면의 **향(orientation)** 에 대한 근본적인 성질을 다루고 있습니다. 증명을 이해하기 위해 다음 개념들이 필요합니다. 🧭

* **향을 줄 수 있는 곡면 (Orientable Surface)**
곡면 $S$ 위에 매끄러운 단위 법선 벡터장 $N$이 존재할 때, 이 곡면은 **향을 줄 수 있다(orientable)** 고 말합니다. 이 벡터장 $N$은 곡면의 각 점에서 '바깥쪽' 또는 '위쪽'과 같은 방향을 일관되게 지정하는 역할을 합니다. 문제의 첫 문장은 곡면 $S$가 향을 줄 수 있는 곡면임을 가정한 것입니다.
* **좌표 근방 (Coordinate Neighborhood) / 좌표 조각 (Chart)**
곡면의 일부를 $\mathbb{R}^2$의 열린 집합으로 매끄럽게 표현하는 사상 $X_i: U_i \to S$를 의미합니다. 곡면 전체를 덮는 이러한 좌표 조각들의 모음을 **아틀라스(atlas)** 라고 합니다.
* **좌표 변환 사상 (Coordinate Change / Transition Map)**
두 좌표 조각 $X_i(U_i)$와 $X_j(U_j)$가 겹치는 부분에서, 한 좌표계($U_j$의 좌표)를 다른 좌표계($U_i$의 좌표)로 변환하는 함수 $T_{ij} = X_i^{-1} \circ X_j$를 의미합니다. 이 함수는 매끄러운 함수입니다.
* **좌표 변환의 야코비안 (Jacobian of Coordinate Change)**
좌표 변환 사상 $T_{ij}$의 야코비 행렬식을 의미합니다. 이 값이 양수라는 것은 좌표 변환이 '향을 보존(orientation-preserving)'한다는 의미입니다. 즉, 오른손 좌표계를 오른손 좌표계로, 왼손 좌표계를 왼손 좌표계로 변환합니다.
* **향이 부여된 아틀라스 (Oriented Atlas)**
문제에서 요구하는 "모든 좌표 변환의 야코비안이 양수"인 아틀라스가 바로 **향이 부여된 아틀라스** 입니다. 이 문제의 핵심은, 향을 줄 수 있는 곡면은 항상 향이 부여된 아틀라스를 가진다는 것을 증명하는 것입니다.
* **접평면의 향 (Orientation of Tangent Plane)**
단위 법선 벡터 $N(p)$는 점 $p$에서의 접평면 $T_pS$에 향을 부여합니다. 접평면의 순서 기저(ordered basis) $\{ \mathbf{e}_1, \mathbf{e}_2 \}$가 $\mathbb{R}^3$에서 순서 기저 $\{ \mathbf{e}_1, \mathbf{e}_2, N(p) \}$가 **오른손 좌표계(right-handed system)** 를 이룰 때, 이 기저를 **양의 향을 가졌다(positively oriented)** 고 정의합니다.

## 3. 완벽한 답안

**증명**

**목표:** 매끄러운 단위 법선 벡터장 $N$을 갖는 곡면 $S$가 모든 좌표 변환 사상의 야코비안 행렬식이 양수인 아틀라스(향이 부여된 아틀라스)를 가짐을 보이는 것이다.

증명은 임의의 아틀라스에서 시작하여, 주어진 법선 벡터장 $N$을 기준으로 각 좌표 조각을 수정하여 새로운 '향이 부여된' 아틀라스를 구성하는 방식으로 진행된다.

1. 임의의 아틀라스에서 시작
$S$는 매끄러운 곡면이므로, $S$ 전체를 덮는 아틀라스 $\mathcal{A} = \{Y_i: V_i \to S\}_{i \in I}$가 존재한다.

2. 좌표 조각의 향 판별
각 좌표 조각 $Y_i(u,v)$에 대해, 접벡터 $Y_u = \frac{\partial Y}{\partial u}$와 $Y_v = \frac{\partial Y}{\partial v}$는 각 점에서 접평면의 기저를 이룬다. 이 순서 기저 $\{Y_u, Y_v\}$가 주어진 법선 벡터장 $N$과 양립하는지 (즉, 양의 향을 갖는지) 판별할 수 있다. 이는 $\mathbb{R}^3$에서 세 벡터 $\{Y_u, Y_v, N\}$가 오른손 좌표계를 형성하는지 확인하는 것과 같으며, 다음 행렬식의 부호로 결정된다.

$$
\det(Y_u, Y_v, N)
$$

$Y_u, Y_v$는 선형 독립이고 $N$은 이들에 수직이므로, 이 행렬식은 절대로 0이 되지 않는다. 또한, 이 값은 $V_i$ 위에서 연속이므로 (필요하다면 $V_i$를 더 작은 연결된 집합으로 쪼개어) $V_i$ 전체에서 부호가 일정하다.

3. 향에 맞게 아틀라스 수정
이제 기존 아틀라스 $\mathcal{A}$를 수정하여 모든 좌표 조각이 $N$에 대해 양의 향을 갖는 새로운 아틀라스 $\mathcal{A}' = \{X_i: U_i \to S\}_{i \in I}$를 구성한다. 각 $i \in I$에 대해:
* **경우 1: $\det((Y_i)_u, (Y_i)_v, N) > 0$ 인 경우**
이 좌표 조각은 이미 $N$과 양립하므로 수정할 필요가 없다. $U_i = V_i$ 이고 $X_i(u,v) = Y_i(u,v)$로 둔다.
* **경우 2: $\det((Y_i)_u, (Y_i)_v, N) < 0$ 인 경우**
이 좌표 조각의 향을 뒤집어야 한다. $V_i$의 좌표 $(u,v)$를 서로 바꾸어 새로운 좌표 $(u', v') = (v,u)$를 만든다. 즉, $U_i = \{(v,u) \mid (u,v) \in V_i\}$ 로 정의하고, 새로운 좌표 조각을 $X_i(u', v') = Y_i(u,v)$ 로 정의한다.
새로운 접벡터는 $(X_i)_{u'} = (Y_i)_v$, $(X_i)_{v'} = (Y_i)_u$ 이므로, 향을 판별하는 행렬식은 다음과 같이 변한다.

$$
\det((X_i)_{u'}, (X_i)_{v'}, N) = \det((Y_i)_v, (Y_i)_u, N) = -\det((Y_i)_u, (Y_i)_v, N) > 0
$$

따라서 수정된 좌표 조각 $X_i$는 $N$에 대해 양의 향을 갖는다.

4. 새로운 아틀라스의 야코비안 검증
이렇게 구성된 새로운 아틀라스 $\mathcal{A}'$의 두 좌표 조각 $X_i(u_i, v_i)$와 $X_j(u_j, v_j)$가 겹치는 영역을 생각해보자. 이 영역의 한 점 $p$에서, 접평면 $T_pS$는 두 개의 기저를 가진다:
* $B_i = \{(X_i)_{u_i}, (X_i)_{v_i}\}$
* $B_j = \{(X_j)_{u_j}, (X_j)_{v_j}\}$
우리의 구성 방식에 의해, 두 기저 $B_i$와 $B_j$는 모두 $N$에 대해 **양의 향을 갖는다** .

좌표 변환 $T_{ij} = X_i^{-1} \circ X_j$의 야코비 행렬은 기저 $B_j$를 기저 $B_i$로 변환하는 **기저 변환 행렬(change of basis matrix)** 이다. 두 기저가 같은 향(여기서는 양의 향)을 가지므로, 그 둘 사이의 기저 변환 행렬의 행렬식은 반드시 **양수** 여야 한다.

따라서, 임의의 겹치는 두 좌표 조각 $X_i, X_j$에 대해, 좌표 변환의 야코비안 행렬식 $\det(J(T_{ij}))$는 양수이다.

### 최종 결론
위의 과정을 통해, 우리는 주어진 매끄러운 법선 벡터장 $N$을 이용하여 모든 좌표 변환의 야코비안 행렬식이 양수인 아틀라스를 구성할 수 있음을 보였다. ∎