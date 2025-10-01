### 10. (10 pts.) Let $A \subset \mathbb{R}^d$ be a non-empty set. For $x \in \mathbb{R}^d$, we define
$d(x,A) = \inf_{y \in A} ||x-y||$
where $||\cdot||$ denotes the usual Euclidean norm in $\mathbb{R}^d$. Prove or disprove the following identity:
$\bigcap_{n=1}^\infty \{x \in \mathbb{R}^d : d(x, A) < 1/n\} = \bar{A}$,
where $\bar{A}$ is the closure of A.

#### Theorem
* **집합의 폐포(Closure of a Set)** : 거리 공간에서 집합 $A$의 폐포 $\bar{A}$는 $A$까지의 거리가 0인 모든 점들의 집합과 같다. 즉, $\bar{A} = \{x \mid d(x,A) = 0\}$.

#### Answer
증명: 주어진 등식은 참이다.
1. 먼저, 등식의 좌변에 있는 집합의 의미를 파악한다.
$S = \bigcap_{n=1}^\infty \{x \in \mathbb{R}^d : d(x, A) < 1/n\}$
점 $x$가 집합 $S$에 속한다는 것은, 모든 자연수 $n$에 대해 $d(x,A) < 1/n$ 이 성립한다는 의미이다.
2. $d(x,A)$는 음이 아닌 실수이다. 임의의 양수 $\epsilon > 0$에 대해, $1/n < \epsilon$을 만족하는 자연수 $n$을 항상 찾을 수 있다 (아르키메데스 원리). 따라서, 모든 $n$에 대해 $d(x,A) < 1/n$ 이라는 조건은 $d(x,A)=0$ 이라는 조건과 동치이다.
3. 따라서, 좌변의 집합은 $S = \{x \in \mathbb{R}^d \mid d(x,A)=0\}$ 으로 다시 쓸 수 있다.
4. 거리 공간에서 집합 $A$의 폐포 $\bar{A}$는 $A$까지의 거리가 0인 점들의 집합이라는 것이 잘 알려진 정리이다.
* **증명** :
* ($\bar{A} \subseteq S$): $x \in \bar{A}$라 하자. 그러면 $x$의 임의의 근방은 $A$와 만난다. 즉, 임의의 $\epsilon>0$에 대해, $||x-y|| < \epsilon$인 $y \in A$가 존재한다. 이는 $d(x,A) = \inf_{y \in A} ||x-y|| \le \epsilon$을 의미한다. 이 식이 모든 $\epsilon>0$에 대해 성립하므로, $d(x,A)=0$이다. 따라서 $x \in S$이다.
* ($S \subseteq \bar{A}$): $x \in S$라 하자. 즉, $d(x,A)=0$이다. 이는 $\inf_{y \in A} ||x-y|| = 0$임을 의미한다. 하한(infimum)의 정의에 의해, 임의의 $\epsilon > 0$에 대해, $||x-y|| < \epsilon$인 $y \in A$가 존재한다. 이는 $x$를 중심으로 하는 임의의 열린 공(open ball)이 $A$의 원소를 포함한다는 의미이며, 이는 $x$가 $\bar{A}$에 속한다는 정의이다.
5. 따라서 $S = \bar{A}$ 이므로, 주어진 등식은 참이다.



### 11. (10 pts.) Is a finite product of Hausdorff spaces Hausdorff? Is an infinite product of Hausdorff spaces Hausdorff? (The product spaces are endowed with the product topology.) Justify your answers.

#### Theorem
* **하우스도르프 공간(Hausdorff Space)** : 서로 다른 두 점 $x, y$가 주어졌을 때, $x$를 포함하는 열린 집합 $U$와 $y$를 포함하는 열린 집합 $V$가 존재하여 $U \cap V = \emptyset$을 만족하는 위상 공간이다.
* **곱위상(Product Topology)** : 곱공간 $\prod X_\alpha$에서, 유한개의 성분을 제외한 나머지 성분은 전체 공간인 형태의 곱집합들을 기저로 하는 위상이다.

#### Answer
**두 경우 모두 답은 '예'이다.** 하우스도르프 공간의 유한 또는 무한 곱공간은 곱위상에 대해 항상 하우스도르프 공간이다.

**유한 곱의 경우:**
1. $X_1, \dots, X_n$을 하우스도르프 공간이라 하고, $X = \prod_{i=1}^n X_i$라 하자.
2. $X$에서 서로 다른 두 점 $x=(x_1, \dots, x_n)$과 $y=(y_1, \dots, y_n)$를 선택하자.
3. $x \neq y$ 이므로, $x_j \neq y_j$인 인덱스 $j \in \{1, \dots, n\}$가 적어도 하나 존재한다.
4. $X_j$는 하우스도르프 공간이므로, $x_j \in U_j$, $y_j \in V_j$이고 $U_j \cap V_j = \emptyset$인 열린 집합 $U_j, V_j \subset X_j$가 존재한다.
5. $X$에서 두 개의 열린 집합 $U, V$를 다음과 같이 정의한다.

$$
U = X_1 \times \dots \times U_j \times \dots \times X_n
$$

  

$$
V = X_1 \times \dots \times V_j \times \dots \times X_n
$$

6. $x \in U$이고 $y \in V$이다. 또한, 어떤 점 $z \in U \cap V$가 존재한다면, 그 점의 $j$번째 성분 $z_j$는 $U_j \cap V_j$에 속해야 한다. 그러나 $U_j$와 $V_j$는 서로소이므로 이는 불가능하다. 따라서 $U \cap V = \emptyset$이다.
7. 그러므로 유한 곱공간은 하우스도르프 공간이다.

**무한 곱의 경우:**
1. $\{X_\alpha\}_{\alpha \in I}$를 하우스도르프 공간들의 집합족이라 하고, $X = \prod_{\alpha \in I} X_\alpha$라 하자.
2. $X$에서 서로 다른 두 점 $x=(x_\alpha)$와 $y=(y_\alpha)$를 선택하자.
3. $x \neq y$ 이므로, $x_\beta \neq y_\beta$인 인덱스 $\beta \in I$가 존재한다.
4. $X_\beta$는 하우스도르프 공간이므로, $x_\beta \in U_\beta$, $y_\beta \in V_\beta$이고 $U_\beta \cap V_\beta = \emptyset$인 열린 집합 $U_\beta, V_\beta \subset X_\beta$가 존재한다.
5. $X$에서 두 개의 열린 집합 $U, V$를 다음과 같이 정의한다.

$$
U = \pi_\beta^{-1}(U_\beta) = \{z \in X \mid z_\beta \in U_\beta\}
$$

  

$$
V = \pi_\beta^{-1}(V_\beta) = \{z \in X \mid z_\beta \in V_\beta\}
$$

여기서 $\pi_\beta$는 $\beta$번째 성분으로의 사영 함수이다. $U_\beta, V_\beta$가 열려있으므로, 곱위상의 정의에 의해 $U, V$는 $X$에서 열린 집합이다.
6. $x \in U$이고 $y \in V$이다. 또한 $U \cap V = \emptyset$인데, 만약 $z \in U \cap V$이면 $z_\beta \in U_\beta \cap V_\beta$가 되어 모순이 발생하기 때문이다.
7. 그러므로 임의의 곱공간은 하우스도르프 공간이다.



### 12. (10 pts.) Let $X$ be a topological space.
(a) Define what it means for $X$ to be (1) compact, (2) normal.
(b) Show that a compact Hausdorff space is normal.

#### Theorem
* **컴팩트 공간(Compact Space)** : 공간 $X$의 모든 열린 덮개가 유한 부분 덮개를 갖는다.
* **정규 공간(Normal Space)** : 임의의 서로소인 닫힌 집합 $A, B$에 대해, $A \subset U, B \subset V$이고 $U \cap V = \emptyset$인 열린 집합 $U, V$가 존재한다.
* **보조정리** : 하우스도르프 공간에서, 컴팩트 부분집합 $K$와 $K$에 속하지 않는 점 $x$가 주어지면, $x \in U, K \subset V$이고 $U \cap V = \emptyset$인 열린 집합 $U,V$가 존재한다.

#### Answer
(a) 정의
1. 컴팩트(Compact) : 위상 공간 $X$의 임의의 열린 덮개(open cover)가 유한개의 원소로 이루어진 부분 덮개(finite subcover)를 가질 때, $X$를 컴팩트 공간이라고 한다.
2. 정규(Normal) : 위상 공간 $X$의 임의의 서로소인(disjoint) 닫힌(closed) 부분집합 $A, B$에 대해, $A$를 포함하는 열린 집합 $U$와 $B$를 포함하는 열린 집합 $V$가 존재하여 $U$와 $V$가 서로소($U \cap V = \emptyset$)일 때, $X$를 정규 공간이라고 한다.

(b) 컴팩트 하우스도르프 공간이 정규 공간임을 보인다.
1. $X$를 컴팩트 하우스도르프 공간이라 하고, $A$와 $B$를 $X$의 서로소인 닫힌 부분집합이라 하자.
2. $X$가 컴팩트하므로, 닫힌 부분집합인 $A$와 $B$ 역시 컴팩트하다.
3. 먼저 $A$의 각 점 $a \in A$에 대해, $a \notin B$이고 $B$는 컴팩트하다. 보조정리(위 Theorem 참조, 증명은 14번 문제 풀이와 유사)에 의해, $a \in U_a, B \subset V_a$이고 $U_a \cap V_a = \emptyset$인 열린 집합 $U_a, V_a$가 존재한다.
4. 집합족 $\{U_a\}_{a \in A}$는 컴팩트 집합 $A$의 열린 덮개이다. 따라서 유한 부분 덮개 $\{U_{a_1}, \dots, U_{a_n}\}$가 존재하여 $A \subset \bigcup_{i=1}^n U_{a_i}$ 이다.
5. 이제 두 개의 열린 집합 $U, V$를 다음과 같이 정의한다.

$$
U = \bigcup_{i=1}^n U_{a_i}, \qquad V = \bigcap_{i=1}^n V_{a_i}
$$

6. $U$는 열린 집합들의 합집합이므로 열린 집합이고, 정의에 의해 $A \subset U$ 이다.
7. $V$는 유한개의 열린 집합들의 교집합이므로 열린 집합이고, 모든 $i$에 대해 $B \subset V_{a_i}$ 이므로, $B \subset V$ 이다.
8. 마지막으로, $U$와 $V$가 서로소임을 보인다. 임의의 $i \in \{1, \dots, n\}$에 대해 $U_{a_i} \cap V_{a_i} = \emptyset$ 이고, $V \subset V_{a_i}$ 이므로 $U_{a_i} \cap V = \emptyset$ 이다. 따라서, $U \cap V = (\bigcup_{i=1}^n U_{a_i}) \cap V = \bigcup_{i=1}^n (U_{a_i} \cap V) = \bigcup_{i=1}^n \emptyset = \emptyset$ 이다.
9. 따라서 $X$는 정규 공간이다.

---

물론입니다. 정칙 곡면의 정의에 관한 이 두 문제에 대해 번역, 필수 개념, 그리고 가장 이상적인 답안을 제시해 드리겠습니다.

### 1. 문제 번역

**13. (10점)
**(a)** $\mathbb{R}^3$ 안에서 $x^2+y^2+z^2=1$ 로 주어진 구(sphere)가 **매개변수 사상(parametrization maps)** 을 이용하여 **정칙 곡면(regular surface)** 임을 보여라.

**(b)** $f:\mathbb{R}^3 \to \mathbb{R}$를 $C^\infty$ 함수라 하자. $a \in f(\mathbb{R}^3)$를 $f$의 **정칙값(regular value)** 이라 하자. 역상(inverse image) $f^{-1}(a)$가 **정칙 곡면** 임을 보여라.

### 2. 문제 풀이를 위한 필수 개념

#### (a)를 위한 개념

* **정칙 곡면 (Regular Surface):** 부분집합 $S \subset \mathbb{R}^3$가 정칙 곡면이라는 것은, $S$ 위의 **모든** 점 $p$에 대해, 그 점 근방을 덮는 **매개변수 사상(parametrization map) $\mathbf{x}$** 가 존재한다는 의미입니다. 이 사상은 다음 조건을 만족해야 합니다.
1. 매끄러움(Smooth): $\mathbf{x}$는 무한히 미분 가능합니다.
2. 동형사상(Homeomorphism): $\mathbf{x}$는 연속이고 연속인 역함수를 가집니다.
3. 정칙 조건(Regular): 접벡터 $\mathbf{x}_u, \mathbf{x}_v$가 모든 점에서 선형 독립입니다.
* **아틀라스 (Atlas):** 전체 곡면을 덮는 이러한 매개변수 사상들의 모음을 아틀라스라고 합니다. 구 전체가 정칙 곡면임을 보이려면, 구 위의 모든 점을 포함하는 아틀라스를 구성해야 합니다.

#### (b)를 위한 개념

* **정칙값 (Regular Value):** 값 $a \in \mathbb{R}$가 함수 $f$의 정칙값이라는 것은, 역상 $f^{-1}(a)$에 속하는 모든 점 $p$에서 $f$의 미분(그래디언트)이 0이 아님($\nabla f(p) \neq \mathbf{0}$)을 의미합니다.
* **음함수 정리 (Implicit Function Theorem):** 이 문제 증명의 핵심 정리입니다. 점 $p$에서 $f(p)=a$이고 $\nabla f(p) \neq \mathbf{0}$ 이면, 점 $p$ 근방에서 등위 집합 $f^{-1}(a)$을 국소적으로 하나의 변수를 나머지 변수들에 대한 매끄러운 함수(예: $z=g(x,y)$)의 그래프로 나타낼 수 있음을 보장합니다. 이 정리는 **정칙값 정리(Regular Value Theorem)** 또는 **원상 정리(Preimage Theorem)** 의 기초가 됩니다.

### 3. 가장 쉽고 완벽한 답안

#### (a) 구가 정칙 곡면임의 증명

**목표:** 구 $S^2$ 위의 임의의 점을 포함하는 매개변수 사상(좌표 조각)이 존재함을 보인다. 이를 위해 6개의 좌표 조각으로 구성된 아틀라스를 제시한다.

1. 구 $S^2: x^2+y^2+z^2=1$ 위의 임의의 점 $p=(x_0,y_0,z_0)$을 생각하자. $x_0, y_0, z_0$ 중 적어도 하나는 0이 아니다.
2. 일반성을 잃지 않고 $z_0 > 0$ 이라 가정하자. (다른 경우도 대칭적으로 동일하다.)
3. 점 $p$를 포함하는 북반구($z>0$)는 함수 $z = g(x,y) = \sqrt{1-x^2-y^2}$ 의 그래프로 표현된다.
4. 이를 이용하여 열린 단위 디스크 $U = \{(x,y) \in \mathbb{R}^2 | x^2+y^2<1\}$ 에서 북반구로 가는 매개변수 사상 $\mathbf{x}: U \to S^2$ 를 다음과 같이 정의한다.

$$
\mathbf{x}(x,y) = (x, y, \sqrt{1-x^2-y^2})
$$

5. 이 사상 $\mathbf{x}$가 정칙 곡면의 조건을 만족하는지 확인한다.
* **매끄러움:** $g(x,y)$는 열린 집합 $U$에서 무한히 미분 가능하므로, $\mathbf{x}$는 매끄럽다.
* **동형사상:** $\mathbf{x}$는 연속 함수의 그래프이므로 이미지와의 동형사상이다. (역함수는 $S^2$에서 xy평면으로의 투영으로 이 또한 연속이다.)
* **정칙 조건:** 접벡터 $\mathbf{x}_x=(1,0, g_x)$와 $\mathbf{x}_y=(0,1, g_y)$의 외적은 $(-g_x, -g_y, 1)$이다. 이 벡터는 z성분이 1이므로 절대 영벡터가 될 수 없다. 따라서 $\mathbf{x}_x, \mathbf{x}_y$는 항상 선형 독립이다.

6. 위와 같이 북반구($z>0$), 남반구($z<0$), 앞($y>0$), 뒤($y<0$), 오른쪽($x>0$), 왼쪽($x<0$)에 해당하는 총 6개의 매개변수 사상을 만들 수 있다. 이 6개의 사상(좌표 조각)들의 이미지의 합집합은 구 $S^2$ 전체를 덮는다.

**결론:** 구 위의 모든 점은 위와 같은 6개의 매개변수 사상 중 적어도 하나에 포함되므로, **구는 정칙 곡면이다.** ∎


네, 아주 좋은 지적입니다. 실제로 구의 넓이를 계산하거나 구 위의 점을 다룰 때처럼 많은 응용 분야에서는 **구면 좌표계가 훨씬 더 편하고 직관적** 입니다.

하지만 이전 문제의 목표였던 "** 정의를 이용하여** 구가 정칙 곡면임을 증명하는 것"에 한해서는, 구면 좌표계에 결정적인 약점이 있어서 단독으로 사용할 수 없습니다.

--

### \#\# 구면 좌표계의 장점과 결정적 약점

* **장점: 하나의 수식으로 표현**
구면 좌표계는 단 하나의 매개변수 사상으로 구 전체(를 거의 다) 표현할 수 있어 매우 우아합니다.

$$
\mathbf{X}(\theta, \phi) = (\sin\phi\cos\theta, \sin\phi\sin\theta, \cos\phi)
$$

여기서 $\theta$는 경도, $\phi$는 위도와 관련된 각도입니다. 이는 구의 넓이나 구 위에서의 적분 등을 계산할 때 압도적으로 편리합니다.

* **결정적 약점: 극점에서의 특이점(Singularity)**
정칙 곡면의 정의에 따르면, 모든 점 근방에서 접벡터들이 선형 독립이어야 합니다. 하지만 구면 좌표계에서는 **북극($\phi=0$)과 남극($\phi=\pi$)** 에서 이 조건이 깨집니다.

* 접벡터 $\mathbf{X}_\theta$를 계산하면 $(-\sin\phi\sin\theta, \sin\phi\cos\theta, 0)$ 이 됩니다.
* 북극($\phi=0$) 또는 남극($\phi=\pi$)에서는 $\sin\phi=0$ 이므로, **$\mathbf{X}_\theta = (0,0,0)$** 이 되어버립니다.
* 접벡터 중 하나가 영벡터가 되면 두 접벡터는 선형 독립일 수 없습니다. 따라서 이 매개변수 사상은 두 극점에서 **정칙(regular)이 아닙니다.**
* 결론적으로, 구면 좌표계 하나만으로는 구 위의 **모든** 점이 정칙 조건을 만족함을 보일 수 없으므로, 증명 도구로는 불완전합니다.

--

### \#\# 6개 좌표 조각(함수 그래프) 방식의 장점

* **장점: 완벽한 정칙성 보장**
$z=f(x,y)=\sqrt{1-x^2-y^2}$ 와 같은 함수 그래프 방식의 가장 큰 장점은, 그 정의상 **항상 정칙 조건을 만족** 한다는 것입니다.
* 접벡터가 $\mathbf{X}_x=(1,0,f_x)$ 와 $\mathbf{X}_y=(0,1,f_y)$ 형태이므로, 두 벡터는 항상 선형 독립입니다.
* 따라서 이 방식은 '정칙 곡면임을 증명하라'는 문제의 요구사항을 군더더기 없이 만족시키는, 수학적으로 가장 엄밀하고 안전한 방법입니다.

결론적으로, **어떤 목적으로 사용하느냐** 에 따라 더 편한 방법이 달라집니다. 일상적인 계산에는 구면 좌표계가 훨씬 편리하지만, 정칙성을 엄밀하게 증명해야 할 때는 허점이 없는 여러 개의 함수 그래프 조각을 사용하는 것이 정석입니다.

#### (b) 정칙값의 역상이 정칙 곡면임의 증명

**목표:** $a$가 $f:\mathbb{R}^3 \to \mathbb{R}$의 정칙값일 때, 등위 집합 $S=f^{-1}(a)$가 정칙 곡면임을 보인다. 이를 위해 $S$ 위의 임의의 점 $p$에 대해 정칙 곡면의 조건을 만족하는 국소 매개변수 표현이 존재함을 **음함수 정리** 를 이용하여 증명한다.

1. $S = f^{-1}(a)$ 위의 임의의 점 $p=(x_0,y_0,z_0)$을 생각하자. 정의에 의해 $f(p)=a$이다.
2. $a$가 정칙값이므로, 점 $p$에서 $f$의 그래디언트는 0이 아니다.

$$
\nabla f(p) = \left(\frac{\partial f}{\partial x}(p), \frac{\partial f}{\partial y}(p), \frac{\partial f}{\partial z}(p)\right) \neq (0,0,0)
$$

3. 이는 세 편도함수 중 적어도 하나는 $p$에서 0이 아님을 의미한다. 일반성을 잃지 않고 $\frac{\partial f}{\partial z}(p) \neq 0$ 이라고 가정하자.
4. 음함수 정리 에 따르면, 위 조건 하에서 점 $p$의 적절한 근방 $V \subset \mathbb{R}^3$이 존재하여, $V$ 안의 등위 집합 $S \cap V$를 점 $(x_0,y_0)$의 근방 $W \subset \mathbb{R}^2$ 위에 정의된 매끄러운($C^\infty$) 함수 $z=g(x,y)$의 그래프로 나타낼 수 있다.
5. 이 함수 $g$를 이용하여 $p$ 근방에서 $S$의 국소 매개변수 사상 $\mathbf{x}: W \to S$를 다음과 같이 구성할 수 있다.

$$
\mathbf{x}(x,y) = (x, y, g(x,y))
$$

6. (a)에서 보았듯이, 매끄러운 함수의 그래프로 주어진 매개변수 사상은 정칙 곡면의 세 가지 조건(매끄러움, 동형사상, 정칙 조건)을 모두 만족한다.

**결론:** $S$ 위의 임의의 점 $p$에 대해, 그 점 근방에서 정칙 곡면의 조건을 만족하는 매개변수 사상이 존재한다. 따라서, **정칙값의 역상 $f^{-1}(a)$는 정칙 곡면이다.** ∎

---

물론입니다. 향을 줄 수 있는 곡면의 조건에 관한 이 문제에 대해 번역, 필수 개념, 그리고 가장 이상적인 답안을 제시해 드리겠습니다.

### 1. 문제 번역

**14. (10점) X를 $\mathbb{R}^3$ 안의 연결된(connected) 곡면이라 하고, U와 V를 X 위의 연결된 좌표 근방(connected coordinate neighborhoods) 이라 하자. 단, $X=U \cup V$ 이다. 만약 교집합 $U \cap V$ 또한 연결되어 있다면 , X가 향을 줄 수 있는 곡면(orientable) 임을 보여라.

### 2. 문제 풀이를 위한 필수 개념

이 증명은 곡면의 국소적인 성질(각 조각의 향)을 어떻게 전역적인 성질(곡면 전체의 향)로 확장할 수 있는지에 대한 문제로, **위상수학의 연결성(connectedness) 개념** 이 핵심적인 역할을 합니다.

* **향을 줄 수 있는 곡면 (Orientable Surface):** 곡면 전체에 걸쳐 모순 없이 연속적인(매끄러운) 단위 법선 벡터장을 정의할 수 있는 곡면입니다. 뫼비우스의 띠처럼 꼬여있지 않은 곡면을 생각할 수 있습니다.
* **좌표 근방 (Coordinate Neighborhood):** 곡면의 일부를 $\mathbb{R}^2$의 열린 집합으로 매끄럽게 표현한 '지도 조각'입니다. **모든 좌표 근방은 그 자체로는 항상 향을 줄 수 있습니다.** 즉, 각 조각 U와 V에는 국소적인 법선 벡터장 $N_U$와 $N_V$를 각각 정의할 수 있습니다.
* **연결 집합 (Connected Set):** 하나의 '덩어리'로 이루어져 떨어져 있지 않은 집합입니다. 연결 집합의 중요한 성질은, **연결 집합 위에서 정의된 연속 함수가 이산적인 값(예: {1, -1})만을 가질 경우, 그 함수는 반드시 상수 함수** 라는 것입니다. 이 성질이 증명의 핵심 열쇠입니다. 🔑

### 3. 가장 쉽고 완벽한 답안

**목표:** 두 개의 국소적인 법선 벡터장 $N_U$와 $N_V$를 교집합에서 '부드럽게' 이어 붙여, 곡면 X 전체에 대한 전역적인 법선 벡터장 $N$을 구성할 수 있음을 보인다.

**증명**

1. 국소적인 향(법선 벡터) 선택
U와 V는 좌표 근방이므로, 각각 향을 줄 수 있다. 따라서 U 위에서 정의된 연속 단위 법선 벡터장 $N_U$와 V 위에서 정의된 연속 단위 법선 벡터장 $N_V$를 선택할 수 있다.

2. 교집합에서의 관계 분석
교집합 $W = U \cap V$ 위의 임의의 점 $p$를 생각하자. 이 점에서는 $N_U(p)$와 $N_V(p)$가 모두 정의된다. 두 벡터는 모두 점 $p$에서 곡면 X에 수직이므로, 서로 평행해야 한다. 두 벡터 모두 단위 벡터이므로, 다음 관계가 성립한다.

$$
N_V(p) = N_U(p) \quad \text{또는} \quad N_V(p) = -N_U(p)
$$

3. 연결성(Connectedness)의 활용
교집합 $W$ 위에서 다음과 같이 함수 $f: W \to \{-1, 1\}$를 정의하자.

$$
f(p) = \langle N_U(p), N_V(p) \rangle
$$

$N_U$와 $N_V$는 연속이므로, 두 벡터의 내적인 $f(p)$ 또한 **연속 함수** 이다.
그런데 문제의 가정에서 교집합 $W = U \cap V$는 **연결 집합** 이다.

위상수학의 기본 정리에 따르면, **연결 집합** 위에서 정의된 **연속 함수** 가 이산적인 값들의 집합(여기서는 $\{-1, 1\}$)을 함숫값으로 가질 경우, 그 함수는 반드시 **상수 함수** 여야 한다.

따라서, $W$ 위의 모든 점 $p$에 대해 $f(p)=1$ 이거나, 또는 모든 점 $p$에 대해 $f(p)=-1$ 이다.

4. 전역적인 법선 벡터장 구성
* **경우 1: $f(p) = 1$ 인 경우**
교집합의 모든 점에서 $N_U(p) = N_V(p)$ 이다. 즉, 두 법선 벡터장이 이미 일치하므로, 곡면 X 전체에 대한 법선 벡터장 $N$을 다음과 같이 자연스럽게 정의할 수 있다.

$$
N(p) = \begin{cases} N_U(p) & p \in U \text{ 일 때} \\ N_V(p) & p \in V \text{ 일 때} \end{cases}
$$

* **경우 2: $f(p) = -1$ 인 경우**
교집합의 모든 점에서 $N_U(p) = -N_V(p)$ 이다. 이 경우, 한쪽의 법선 벡터장을 뒤집어 주면 된다. 예를 들어, $N_V' = -N_V$ 로 새로운 법선 벡터장을 정의하자. 그러면 교집합에서 $N_U(p) = N_V'(p)$ 가 성립한다. 이제 X 전체에 대한 법선 벡터장 $N$을 다음과 같이 정의할 수 있다.

$$
N(p) = \begin{cases} N_U(p) & p \in U \text{ 일 때} \\ N_V'(p) & p \in V \text{ 일 때} \end{cases}
$$

### 최종 결론
두 경우 모두, 곡면 X 전체에 걸쳐 잘 정의된 연속 단위 법선 벡터장 $N$을 성공적으로 구성하였다. 따라서 정의에 의해, **곡면 X는 향을 줄 수 있다.** ∎

---

물론입니다. 타원체의 가우스 곡률에 관한 이 문제에 대해 번역, 필수 개념, 그리고 가장 이상적인 답안을 제시해 드리겠습니다.

### 1. 문제 번역

**15. (10점) X를 방정식 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ ($a,b,c$는 양의 실수)로 주어진 $\mathbb{R}^3$ 안의 곡면이라 하자. X의 각 점에서의 가우스 곡률을 계산하라.

### 2. 문제 풀이를 위한 필수 개념

이 문제를 푸는 방법은 크게 두 가지, 즉 직접 매개변수화하여 계산하는 방법과 등위 집합(level set) 공식을 이용하는 방법이 있습니다. 후자가 훨씬 더 간단하고 우아합니다.

* **등위 집합 (Level Set):** 곡면을 $F(x,y,z)=c$ 형태의 방정식으로 표현하는 것입니다. 이 문제에서 타원체는 $F(x,y,z) = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2}$ 의 $F=1$ 등위 집합입니다.
* **그래디언트 (Gradient, $\nabla F$):** 함수의 각 변수에 대한 편미분을 성분으로 갖는 벡터로, 등위 집합 곡면의 법선 벡터가 됩니다.
* **헤세 행렬 (Hessian Matrix, $H_F$):** 함수의 2차 편미분들을 성분으로 갖는 행렬입니다. 곡면의 2차 근사를 나타냅니다.
* **등위 집합의 가우스 곡률 공식:** 등위 집합 $F=c$로 주어진 곡면의 가우스 곡률 $K$는 다음과 같이 계산할 수 있습니다.

$$
K = \frac{(\nabla F)^T \cdot \text{adj}(H_F) \cdot (\nabla F)}{\|\nabla F\|^4}
$$

여기서 $\text{adj}(H_F)$는 헤세 행렬의 딸림 행렬(adjugate matrix)입니다. 이 공식은 복잡해 보이지만, 타원체의 경우 매우 간단하게 정리됩니다.

### 3. 가장 쉽고 완벽한 답안

**목표:** 타원체 $X: \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ 위의 임의의 점 $(x,y,z)$에서 가우스 곡률 $K$를 계산한다.

**방법:** 곡면을 함수 $F(x,y,z) = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2}$의 등위 집합 $F=1$로 간주하고, 그래디언트와 헤세 행렬을 이용한 가우스 곡률 공식을 적용한다. 
1. 함수 및 도함수 계산
* 함수: $F(x,y,z) = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2}$
* 그래디언트 $\nabla F$:

$$
\nabla F = \left(\frac{2x}{a^2}, \frac{2y}{b^2}, \frac{2z}{c^2}\right)
$$

* 헤세 행렬 $H_F$:

$$
H_F = \begin{pmatrix} 2/a^2 & 0 & 0 \\ 0 & 2/b^2 & 0 \\ 0 & 0 & 2/c^2 \end{pmatrix}
$$

2. 가우스 곡률 공식의 분자 계산
* 헤세 행렬이 대각행렬이므로, 딸림 행렬 $\text{adj}(H_F)$를 쉽게 계산할 수 있다.

$$
\text{adj}(H_F) = \begin{pmatrix} 4/(b^2c^2) & 0 & 0 \\ 0 & 4/(a^2c^2) & 0 \\ 0 & 0 & 4/(a^2b^2) \end{pmatrix}
$$

* 이제 공식의 분자인 $(\nabla F)^T \cdot \text{adj}(H_F) \cdot (\nabla F)$를 계산한다.

$$
\left(\frac{2x}{a^2}, \frac{2y}{b^2}, \frac{2z}{c^2}\right) \begin{pmatrix} 4/(b^2c^2) & 0 & 0 \\ 0 & 4/(a^2c^2) & 0 \\ 0 & 0 & 4/(a^2b^2) \end{pmatrix} \begin{pmatrix} 2x/a^2 \\ 2y/b^2 \\ 2z/c^2 \end{pmatrix}
$$



$$
= \frac{16x^2}{a^4b^2c^2} + \frac{16y^2}{a^2b^4c^2} + \frac{16z^2}{a^2b^2c^4}
$$

    

$$
= \frac{16}{a^2b^2c^2} \left( \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} \right)
$$

* 점 $(x,y,z)$는 타원체 위의 점이므로 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ 이다. 따라서 분자는 놀랍게도 상수가 된다.

$$
\text{분자} = \frac{16}{a^2b^2c^2}
$$

3. 가우스 곡률 공식의 분모 계산
* 분모는 $\|\nabla F\|^4$ 이다.

$$
\|\nabla F\|^2 = \left(\frac{2x}{a^2}\right)^2 + \left(\frac{2y}{b^2}\right)^2 + \left(\frac{2z}{c^2}\right)^2 = 4\left(\frac{x^2}{a^4} + \frac{y^2}{b^4} + \frac{z^2}{c^4}\right)
$$

    

$$
\|\nabla F\|^4 = 16\left(\frac{x^2}{a^4} + \frac{y^2}{b^4} + \frac{z^2}{c^4}\right)^2
$$

4. 최종 결론
분자와 분모를 합치면 가우스 곡률 $K$는 다음과 같다.

$$
K(x,y,z) = \frac{16/(a^2b^2c^2)}{16\left(\frac{x^2}{a^4} + \frac{y^2}{b^4} + \frac{z^2}{c^4}\right)^2} = \frac{1}{a^2b^2c^2 \left(\frac{x^2}{a^4} + \frac{y^2}{b^4} + \frac{z^2}{c^4}\right)^2}
$$

**기하학적 해석:**
원점에서 점 $(x,y,z)$에서의 접평면까지의 수직 거리를 $p$라고 하면, $p^{-2} = \frac{x^2}{a^4} + \frac{y^2}{b^4} + \frac{z^2}{c^4}$ 라는 관계가 성립한다. 이를 이용하면 가우스 곡률을 다음과 같이 매우 아름다운 형태로 표현할 수 있다.

$$
K = \frac{p^4}{a^2b^2c^2}
$$

이는 타원체의 가우스 곡률이 원점에서 접평면까지 거리의 네제곱에 비례함을 의미한다.


네, 당연히 다른 방법이 있습니다. 가장 대표적인 대안은 곡면을 직접 **매개변수화(parameterization)** 하여 가우스 곡률을 계산하는 것입니다.

이 방법은 원리적으로는 모든 곡면에 적용할 수 있지만, 타원체의 경우 계산 과정이 매우 길고 복잡해지기 때문에 보통 첫 번째 방법(등위 집합 공식)을 선호합니다. 하지만 어떤 원리로 계산되는지 아는 것은 중요합니다.

--

### \#\# 매개변수화를 이용한 직접 계산법

**핵심 아이디어:** 구면 좌표계를 타원체에 맞게 변형하여 매개변수 표현을 만든 뒤, 제1 및 제2 기본 형식의 계수($E, F, G, L, M, N$)를 모두 계산하여 표준 공식에 대입합니다.

#### 1. 타원체의 매개변수화

구면 좌표계 $(x = r\sin\phi\cos\theta, y=r\sin\phi\sin\theta, z=r\cos\phi)$에서 반지름 $r$ 대신 각 축의 길이 $a, b, c$를 곱해주면 타원체의 매개변수 표현을 얻을 수 있습니다.

$$
\mathbf{X}(\theta, \phi) = (a\sin\phi\cos\theta, b\sin\phi\sin\theta, c\cos\phi)
$$

(단, $0 \le \theta < 2\pi$, $0 \le \phi \le \pi$)

#### 2. 계산 과정 (개요)

이 방법은 그야말로 대수 계산의 향연입니다. 😵‍💫

1. 1차 편미분 계산: $\mathbf{X}_\theta$ 와 $\mathbf{X}_\phi$ 를 계산합니다.

* $\mathbf{X}_\theta = (-a\sin\phi\sin\theta, b\sin\phi\cos\theta, 0)$
* $\mathbf{X}_\phi = (a\cos\phi\cos\theta, b\cos\phi\sin\theta, -c\sin\phi)$

2. 제1 기본 형식 계수 (E, F, G) 계산:

* $E = \langle \mathbf{X}_\theta, \mathbf{X}_\theta \rangle = \sin^2\phi(a^2\sin^2\theta + b^2\cos^2\theta)$
* $F = \langle \mathbf{X}_\theta, \mathbf{X}_\phi \rangle = (b^2-a^2)\sin\phi\cos\phi\sin\theta\cos\theta$
* $G = \langle \mathbf{X}_\phi, \mathbf{X}_\phi \rangle = \cos^2\phi(a^2\cos^2\theta + b^2\sin^2\theta) + c^2\sin^2\phi$
(벌써부터 식이 매우 복잡해집니다.)

3. 법선 벡터 및 2차 편미분 계산:

* 외적 $\mathbf{X}_\theta \times \mathbf{X}_\phi$ 를 계산하여 법선 벡터를 구하고, 정규화하여 단위 법선 벡터 $\mathbf{n}$을 찾습니다.
* 2차 편미분 벡터 $\mathbf{X}_{\theta\theta}, \mathbf{X}_{\theta\phi}, \mathbf{X}_{\phi\phi}$ 를 모두 계산합니다.

4. 제2 기본 형식 계수 (L, M, N) 계산:

* $L = \langle \mathbf{X}_{\theta\theta}, \mathbf{n} \rangle$
* $M = \langle \mathbf{X}_{\theta\phi}, \mathbf{n} \rangle$
* $N = \langle \mathbf{X}_{\phi\phi}, \mathbf{n} \rangle$
(이 과정은 계산량이 엄청나게 많습니다.)

5. 최종 공식 대입:
위에서 구한 6개의 계수를 모두 가우스 곡률 공식에 대입하여 정리합니다.

$$
K = \frac{LN - M^2}{EG - F^2}
$$

이 복잡한 대수 계산을 모두 마치고 나면, 놀랍게도 이전에 구했던 것과 동일한 결과로 정리됩니다.

$$
K = \frac{1}{a^2b^2c^2 \left(\frac{x^2}{a^4} + \frac{y^2}{b^4} + \frac{z^2}{c^4}\right)^2}
$$

