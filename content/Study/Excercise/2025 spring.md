---
tags:
  - 곡면
  - map
  - is
  - Compute
  - 콤팩트
  - 타원면
  - 벡터
  - 홀로노미
---

### 11. Given a continuous map $f: \mathbb{R} \to \mathbb{R}$, show that the map $\Gamma_f: \mathbb{R} \to \mathbb{R}^2$ defined by $\Gamma_f(x)=(x, f(x))$ is continuous.
#### Theorem
**곱공간으로 가는 함수의 연속성 (Continuity of a Map into a Product Space)**

함수 $F: A \to X \times Y$가 연속 함수일 필요충분조건은 그 성분 함수(component functions) $f_X = \pi_X \circ F: A \to X$ 와 $f_Y = \pi_Y \circ F: A \to Y$ 가 모두 연속 함수인 것이다. 여기서 $\pi_X$와 $\pi_Y$는 각각 $X \times Y$에서 $X$와 $Y$로 가는 사영 함수(projection map)이다.

#### Answer
주어진 함수 $\Gamma_f: \mathbb{R} \to \mathbb{R}^2$의 연속성을 보이기 위해, 이 함수의 각 성분 함수가 연속임을 보이면 된다.
$\mathbb{R}^2$의 좌표를 $(y_1, y_2)$라 하고, 사영 함수를 $\pi_1(y_1, y_2) = y_1$과 $\pi_2(y_1, y_2) = y_2$로 정의하자.

1. 첫 번째 성분 함수:
$(\pi_1 \circ \Gamma_f)(x) = \pi_1(x, f(x)) = x$.
이 함수는 항등 함수(identity map)이다. 항등 함수는 항상 연속이다.

2. 두 번째 성분 함수:
$(\pi_2 \circ \Gamma_f)(x) = \pi_2(x, f(x)) = f(x)$.
이 함수는 문제의 가정에 의해 연속 함수이다.

두 성분 함수가 모두 연속이므로, 위의 정리에 따라 함수 $\Gamma_f$는 연속이다.



### 12. Show that every compact metric space has a countable basis.
#### Theorem
**콤팩트 공간과 열린 덮개 (Compact Space and Open Cover)**

위상 공간 $X$가 **콤팩트 공간** 이라는 것은 $X$의 임의의 열린 덮개(open cover)가 항상 유한 부분덮개(finite subcover)를 가진다는 의미이다.

**위상의 기저 (Basis for a Topology)**

위상 공간 $(X, \mathcal{T})$의 기저 $\mathcal{B}$는 다음 조건을 만족하는 열린 집합들의 모임이다: $X$의 모든 열린 집합은 $\mathcal{B}$에 속한 집합들의 합집합으로 표현될 수 있다. 기저 $\mathcal{B}$가 가산 집합(countable set)일 때, $X$는 **가산 기저를 가진다** 고 한다.

#### Answer
$(X,d)$를 콤팩트 거리 공간이라고 하자. $X$가 가산 기저를 가짐을 보여야 한다.

1. 각 자연수 $n \in \mathbb{N}$에 대하여, 반지름이 $1/n$인 열린 공(open ball)들의 집합 $\mathcal{C}_n = \{B(x, 1/n) \mid x \in X\}$을 생각하자. 이 집합은 $X$의 열린 덮개가 된다.
2. $X$는 콤팩트 공간이므로, 이 열린 덮개 $\mathcal{C}_n$은 유한 부분덮개를 가진다. 즉, 각 $n$에 대해 $X$ 안의 유한 개의 점들 $\{x_{n,i}\}_{i=1}^{k_n}$이 존재하여, $X = \bigcup_{i=1}^{k_n} B(x_{n,i}, 1/n)$ 이 성립한다.
3. 이제 모든 자연수 $n$에 대한 이러한 유한 개의 공들을 모두 모은 집합 $\mathcal{B} = \bigcup_{n=1}^{\infty} \{ B(x_{n,i}, 1/n) \mid 1 \le i \le k_n \}$ 를 정의하자. $\mathcal{B}$는 가산 개의 집합들의 가산 합집합이므로 가산 집합이다.
4. $\mathcal{B}$가 $X$의 위상에 대한 기저임을 보이자.
* $U$를 $X$의 임의의 공집합이 아닌 열린 집합이라 하고, $p \in U$라 하자.
* $U$는 열린 집합이므로, $B(p, \epsilon) \subset U$를 만족하는 $\epsilon > 0$이 존재한다.
* $2/n < \epsilon$을 만족하는 충분히 큰 자연수 $n$을 선택하자.
* 단계 2에서 구성한 유한 부분덮개 $\{B(x_{n,i}, 1/n)\}_{i=1}^{k_n}$는 $X$ 전체를 덮으므로, $p \in B(x_{n,i}, 1/n)$를 만족하는 $i$가 존재한다.
* 이때 $p \in B(x_{n,i}, 1/n) \subset U$ 임을 보이자. 임의의 점 $y \in B(x_{n,i}, 1/n)$에 대해, 삼각부등식에 의해 다음이 성립한다.

$$
d(y, p) \le d(y, x_{n,i}) + d(x_{n,i}, p) < 1/n + 1/n = 2/n
$$

* $2/n < \epsilon$ 이었으므로, $d(y,p) < \epsilon$ 이다. 이는 $y \in B(p, \epsilon)$를 의미한다. 따라서, $B(x_{n,i}, 1/n) \subset B(p, \epsilon) \subset U$ 이다.
5. 임의의 열린 집합 $U$와 그 안의 임의의 점 $p$에 대해, $p \in B \subset U$를 만족하는 기저의 원소 $B \in \mathcal{B}$를 찾았으므로, $\mathcal{B}$는 $X$의 기저이다.

따라서 콤팩트 거리 공간 $X$는 가산 기저를 가진다.



### 13. Let $D^2$ be the closed unit disc in $\mathbb{R}^2$ (centered at the origin).
#### (a) Show that the quotient space $D^2/\partial D^2$ is homeomorphic to $\mathbb{R}^2$.
#### (b) Let $U$ be the interior of $D^2$. Is $\mathbb{R}^2/U$ homeomorphic to $\mathbb{R}^2$? Explain your answer.

#### Theorem
**위상수학적 불변량 (Topological Invariants)**
**콤팩트성(Compactness)** 과 **하우스도르프 성질(Hausdorff property)** 은 위상동형사상(homeomorphism)에 의해 보존되는 위상적 성질이다. 즉, 두 위상 공간이 위상동형이라면, 한 공간이 콤팩트 공간일 때 다른 공간도 콤팩트 공간이어야 하며, 한 공간이 하우스도르프 공간일 때 다른 공간도 하우스도르프 공간이어야 한다.
* **콤팩트 공간** : 모든 열린 덮개가 유한 부분덮개를 가지는 공간.
* **하우스도르프 공간** : 임의의 서로 다른 두 점에 대해, 서로 만나지 않는 열린 근방을 각각 잡아줄 수 있는 공간.

#### Answer
**(a)**
이 명제는 **거짓(False)** 이다. 두 공간이 위상동형이 될 수 없다.

1. 닫힌 단위 원판 $D^2$는 유계이고 닫힌 집합이므로 하이네-보렐 정리에 의해 $\mathbb{R}^2$의 콤팩트 부분 공간이다.
2. 몫 사상 $q: D^2 \to D^2/\partial D^2$는 연속 함수이다. 연속 함수에 의한 콤팩트 공간의 상은 항상 콤팩트 공간이다. 따라서 몫공간 $D^2/\partial D^2$은 콤팩트 공간이다. (이는 경계원 $\partial D^2$을 한 점으로 축소시켜 만든 2차원 구면 $S^2$과 위상동형이며, 구면은 콤팩트 공간이다.)
3. 반면에, $\mathbb{R}^2$는 유계가 아니므로 콤팩트 공간이 아니다. 예를 들어, 열린 덮개 $\{B((0,0), n) \mid n \in \mathbb{N}\}$는 유한 부분덮개를 갖지 않는다.
4. 콤팩트성은 위상동형사상에 의해 보존되는 성질인데, $D^2/\partial D^2$는 콤팩트하고 $\mathbb{R}^2$는 콤팩트하지 않으므로, 두 공간은 위상동형일 수 없다.

**(b)**
두 공간은 위상동형이 **아니다(No)** .

1. 몫공간 $\mathbb{R}^2/U$는 열린 단위 원판 $U = \{x \in \mathbb{R}^2 \mid \|x\| < 1\}$을 하나의 점으로 축소시킨 공간이다. 이 점을 $p_U$라 하자.
2. 이 몫공간이 하우스도르프 공간인지 확인해보자. 점 $p_U$와 경계원 $\partial D^2$ 위의 한 점 $q$ (예: $q=(1,0)$)를 생각해보자.
3. 몫 위상의 정의에 따라, $p_U$를 포함하는 임의의 열린 근방 $V_p$는, 그 역상 $q^{-1}(V_p)$가 원래 공간 $\mathbb{R}^2$에서 $U$를 포함하는 열린 집합이어야 한다. 따라서 $q^{-1}(V_p)$는 반드시 $U$의 경계 $\partial D^2$에 있는 점 $q$에 임의로 가까운 점들을 포함한다.
4. 마찬가지로 $q$를 포함하는 임의의 열린 근방 $V_q$는, 그 역상 $q^{-1}(V_q)$가 $\mathbb{R}^2$에서 $q$를 포함하는 열린 집합이다.
5. $q$를 포함하는 어떤 열린 집합을 잡아도 $U$를 포함하는 어떤 열린 집합과 반드시 겹치게 된다. 이는 몫공간에서 $p_U$의 임의의 열린 근방 $V_p$와 $q$의 임의의 열린 근방 $V_q$가 항상 겹침($V_p \cap V_q \neq \emptyset$)을 의미한다.
6. 따라서 몫공간 $\mathbb{R}^2/U$에서는 서로 다른 두 점 $p_U$와 $q$를 분리하는 서로소인 열린 근방을 찾을 수 없으므로, 이 공간은 하우스도르프 공간이 아니다.
7. $\mathbb{R}^2$는 거리 공간이므로 하우스도르프 공간이다.
8. 하우스도르프 성질은 위상동형사상에 의해 보존되는데, $\mathbb{R}^2/U$는 하우스도르프가 아니고 $\mathbb{R}^2$는 하우스도르프이므로, 두 공간은 위상동형일 수 없다.



### 14. For $a,b,c > 0$ consider the ellipsoid $E_{a,b,c} := \{(x,y,z) \in \mathbb{R}^3 \mid (\frac{x}{a})^2 + (\frac{y}{b})^2 + (\frac{z}{c})^2 = 1\}$.
#### (a) First assume that $a=b$. Show that $E_{a,a,c}$ is a surface of revolution.
#### (b) Give a parametrization of $E_{a,a,c}$. Compute the first fundamental form of this parametrization and the Christoffel symbols.
#### (c) Show that the curve $E_{a,a,c} \cap \{x=0\}$ is the image of a geodesic.

#### Theorem
**회전곡면 (Surface of Revolution)**
한 평면 위의 곡선을 그 평면 안의 한 축을 중심으로 회전시킬 때 생기는 곡면을 회전곡면이라 한다. $xz$-평면 위의 곡선이 $r(z) > 0$ 으로 주어질 때, 이 곡선을 $z$-축 중심으로 회전시킨 곡면의 방정식은 $x^2+y^2 = (r(z))^2$ 형태가 된다.

**측지선 (Geodesic)**
곡면 위의 곡선 중에서 두 점을 잇는 가장 짧은 경로의 성질을 국소적으로 만족하는 곡선이다. 회전곡면의 경우, 모든 자오선(meridian)은 측지선이 된다. 자오선은 회전축을 포함하는 평면으로 회전곡면을 잘랐을 때 생기는 교선이다.

#### Answer
**(a)**
$a=b$일 때, 타원면의 방정식은 다음과 같다.

$$
\frac{x^2}{a^2} + \frac{y^2}{a^2} + \frac{z^2}{c^2} = 1 \implies \frac{x^2+y^2}{a^2} + \frac{z^2}{c^2} = 1
$$

$z$-축으로부터의 거리를 $r = \sqrt{x^2+y^2}$라 하면, 위 식은 $z$와 $r$에 대한 관계식 $\frac{r^2}{a^2} + \frac{z^2}{c^2} = 1$ 로 표현된다.
이는 $xz$-평면(또는 $yz$-평면) 상의 타원 $\frac{x^2}{a^2} + \frac{z^2}{c^2} = 1$ 을 $z$-축을 중심으로 회전시켜 얻은 곡면의 방정식과 일치한다. 따라서 $E_{a,a,c}$는 회전곡면이다.

**(b)**
**매개화:** $xz$-평면 상의 타원을 $x = a \sin u, z = c \cos u$ ($u \in [0,\pi]$)로 매개화하고, 이를 $z$-축 중심으로 각도 $v$ ($v \in [0, 2\pi]$)만큼 회전시킨다.

$$
\mathbf{x}(u,v) = (a \sin u \cos v, a \sin u \sin v, c \cos u)
$$

**제1 기본 형식:**
$\mathbf{x}_u = (a \cos u \cos v, a \cos u \sin v, -c \sin u)$
$\mathbf{x}_v = (-a \sin u \sin v, a \sin u \cos v, 0)$
$E = \mathbf{x}_u \cdot \mathbf{x}_u = a^2 \cos^2 u + c^2 \sin^2 u$
$F = \mathbf{x}_u \cdot \mathbf{x}_v = 0$
$G = \mathbf{x}_v \cdot \mathbf{x}_v = a^2 \sin^2 u$
따라서 제1 기본 형식의 행렬은 $\begin{pmatrix} a^2 \cos^2 u + c^2 \sin^2 u & 0 \\ 0 & a^2 \sin^2 u \end{pmatrix}$ 이다.

**크리스토펠 기호:**
$F=0$이므로 계산이 간단해진다. 0이 아닌 기호들은 다음과 같다.
$\Gamma_{11}^1 = \frac{E_u}{2E} = \frac{(c^2-a^2)\sin(2u)}{2(a^2 \cos^2 u + c^2 \sin^2 u)}$
$\Gamma_{22}^1 = -\frac{G_u}{2E} = -\frac{a^2 \sin u \cos u}{a^2 \cos^2 u + c^2 \sin^2 u}$
$\Gamma_{12}^2 = \Gamma_{21}^2 = \frac{G_u}{2G} = \frac{a^2 \sin u \cos u}{a^2 \sin^2 u} = \cot u$
나머지 기호들($\Gamma_{12}^1, \Gamma_{21}^1, \Gamma_{11}^2, \Gamma_{22}^2$)은 모두 0이다.

**(c)**
곡면 $E_{a,a,c}$와 평면 $\{x=0\}$의 교선을 생각하자.
$x = a \sin u \cos v = 0$ 에서, $a>0, \sin u > 0$ (극점 제외)이므로 $\cos v = 0$ 이어야 한다. 이는 $v=\pi/2$ 또는 $v=3\pi/2$를 의미한다.
이 곡선들은 $v$가 상수인 곡선으로, 회전곡면의 **자오선(meridian)** 에 해당한다.
회전곡면의 모든 자오선은 측지선임이 잘 알려져 있다.
이를 확인하는 한 방법은 대칭성을 이용하는 것이다. 자오선 위의 임의의 점 $p$를 생각하자. 자오선을 포함하는 평면(이 경우 $yz$-평면)에 대해 곡면이 대칭이다. 따라서 점 $p$에서의 곡면의 법선 벡터는 이 평면 안에 놓인다. 또한 자오선 자체도 이 평면 안에 있으므로, 자오선의 주 법선 벡터(principal normal)도 이 평면 안에 놓인다. 회전곡면의 대칭성으로 인해 이 두 벡터(곡면의 법선과 곡선의 주 법선)는 평행하게 되며, 이는 곡선이 측지선일 필요충분조건이다.
따라서 $E_{a,a,c} \cap \{x=0\}$는 두 개의 자오선으로 이루어져 있으며, 이는 측지선의 상이다.



### 15. Define the map for $0 < r < R$ ...
#### Let $T^2$ be the image of the map $x$.
#### (a) Compute the integral $\int_{T^2} K dA$, where $K$ is the Gaussian curvature of $T^2$.
#### (b) Fix $\theta_0$. Take $p=x(\theta_0, 0)$, and let $v=x_\theta(\theta_0, 0)$ be a tangent vector at $p$. Define the path $\gamma_{\theta_0}: [0, 2\pi] \to T^2$, $\phi \mapsto x(\theta_0, \phi)$. Compute the parallel transport of $v$ along $\gamma_{\theta_0}$. What is the angle change modulo $2\pi$?

#### Theorem
**가우스-보네 정리 (Gauss-Bonnet Theorem)**
경계가 없는 콤팩트 유향 곡면 $S$에 대해, 가우스 곡률 $K$를 곡면 전체에 대해 적분한 값은 곡면의 오일러 지표(Euler characteristic) $\chi(S)$에 $2\pi$를 곱한 값과 같다.

$$
\int_S K dA = 2\pi \chi(S)
$$

원환면(torus)의 오일러 지표는 $\chi(T^2)=0$이다.

**홀로노미 (Holonomy)**
곡면 위의 닫힌 곡선을 따라 벡터를 평행이동시켰을 때, 시작점으로 돌아온 벡터는 원래 벡터와 각도 차이를 보일 수 있다. 이 각도 변화량(홀로노미) $\Delta \alpha$는 곡선이 둘러싼 영역 $A$의 가우스 곡률 총합과 같다. (부호는 방향에 따라 결정됨)

$$
\Delta \alpha = -\iint_A K dA
$$

#### Answer
주어진 사상 $\mathbf{x}(\theta, \phi)$는 큰 반지름이 $R$이고 작은 반지름이 $r$인 원환면(torus) $T^2$를 매개화한다.

**(a)**
가우스-보네 정리를 이용한다.
1. 원환면 $T^2$는 경계가 없는 콤팩트 유향 곡면이다.
2. 원환면의 오일러 지표는 $\chi(T^2) = 2-2g$ (여기서 $g$는 구멍의 개수, genus)이고, $g=1$이므로 $\chi(T^2)=0$ 이다.
3. 따라서 가우스-보네 정리에 의해,

$$
\int_{T^2} K dA = 2\pi \chi(T^2) = 2\pi \cdot 0 = 0
$$

**(b)**
곡선 $\gamma_{\theta_0}$는 $\theta=\theta_0$로 고정된 원환면의 위선(parallel)이다. 이 닫힌 곡선을 따라 접벡터 $v$를 평행이동 시켰을 때의 총 각도 변화는 홀로노미 정리에 의해 계산할 수 있다.
1. 각도 변화량 $\Delta\alpha$는 이 위선이 둘러싸는 영역(원환면의 '모자' 부분) $A$에 대한 가우스 곡률의 총합에 음수를 취한 값과 같다.
2. 영역 $A$는 매개변수 $\theta$가 $0$부터 $\theta_0$까지, $\phi$가 $0$부터 $2\pi$까지 변할 때의 영역이다.
3. 원환면의 가우스 곡률 $K$와 면적 요소 $dA$는 다음과 같다.
* $K(\theta, \phi) = \frac{\cos\theta}{r(R+r\cos\theta)}$
* $dA = \sqrt{EG-F^2} d\theta d\phi = r(R+r\cos\theta) d\theta d\phi$
4. 따라서 홀로노미는 다음과 같이 계산된다.

$$
\begin{aligned} \Delta\alpha &= -\iint_A K dA \\ &= -\int_0^{2\pi} \int_0^{\theta_0} \left( \frac{\cos\theta}{r(R+r\cos\theta)} \right) (r(R+r\cos\theta)) d\theta d\phi \\ &= -\int_0^{2\pi} \int_0^{\theta_0} \cos\theta d\theta d\phi \\ &= -\int_0^{2\pi} [\sin\theta]_0^{\theta_0} d\phi \\ &= -\int_0^{2\pi} \sin\theta_0 d\phi \\ &= -(\sin\theta_0) [\phi]_0^{2\pi} \\ &= -2\pi \sin\theta_0 \end{aligned}
$$

따라서 $v$를 $\gamma_{\theta_0}$를 따라 평행이동시켰을 때의 총 각도 변화량은 $-2\pi \sin\theta_0$ 이다. 법 $2\pi$에 대한 각도 변화는 $-2\pi \sin\theta_0 \pmod{2\pi}$ 이다.

---

다음은 타원면에 대한 미분기하학 문제의 번역, 핵심 개념 설명 및 모범 답안입니다.

### 문제 번역

14. (15점) $a, b, c > 0$에 대하여 다음과 같은 타원면(ellipsoid)을 생각하자.

$$
E_{a,b,c} := \{(x, y, z) \in \mathbb{R}^3 | \left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2 + \left(\frac{z}{c}\right)^2 = 1\}
$$

(a) 먼저 $a=b$라고 가정하자. $E_{a,a,c}$가 회전곡면(surface of revolution)임을 보여라.
(b) $E_{a,a,c}$의 매개변수화를 제시하라. 이 매개변수화에 대한 제1 기본 형식(first fundamental form)과 크리스토펠 기호(Christoffel symbols)를 계산하라.
(c) 곡선 $E_{a,b,c} \cap \{x=0\}$이 측지선(geodesic)의 상(image)임을 보여라.

### 핵심 개념

이 문제를 풀기 위해 알아야 할 주요 개념들입니다. 🧐

* **회전곡면 (Surface of Revolution)** : 평면 위의 한 곡선(프로파일 곡선)을 같은 평면 위의 한 직선(회전축)을 중심으로 회전시킬 때 생기는 곡면입니다. * **제1 기본 형식 (First Fundamental Form)** : 곡면의 내재적 기하(intrinsic geometry)를 설명하는 도구로, 곡면 위에서 거리, 각도, 넓이를 측정할 수 있게 해줍니다. 계수 $E, F, G$를 이용해 $I = E du^2 + 2F du dv + G dv^2$로 표현됩니다.
* **크리스토펠 기호 (Christoffel Symbols, $\Gamma_{ij}^k$)** : 제1 기본 형식의 계수와 그 도함수로부터 계산되며, 곡면의 곡률에 대한 정보를 담고 있습니다. 측지선의 방정식을 세우는 데 필수적입니다.
* **측지선 (Geodesic)** : 곡면 위에서 두 점을 잇는 가장 짧은 경로를 국소적으로 나타내는 곡선입니다. 평면에서의 직선을 곡면으로 일반화한 개념이죠. 가장 중요한 성질은 **곡선의 가속도 벡터가 항상 곡면에 수직** 이라는 것입니다. 📏

### 모범 답안

#### (a) $E_{a,a,c}$가 회전곡면임을 보이기

$a=b$일 때, 타원면의 방정식은 다음과 같습니다.

$$
\frac{x^2}{a^2} + \frac{y^2}{a^2} + \frac{z^2}{c^2} = 1 \quad \implies \quad \frac{x^2 + y^2}{a^2} + \frac{z^2}{c^2} = 1
$$

이 방정식은 $x^2+y^2$ 항을 포함하고 있어 **z축에 대한 회전 대칭성** 을 가집니다. 즉, 어떤 점 $(x,y,z)$가 이 곡면 위에 있다면, 이 점을 z축을 중심으로 임의의 각도 $\theta$만큼 회전시킨 점 $(x\cos\theta - y\sin\theta, x\sin\theta + y\cos\theta, z)$ 또한 위 방정식을 만족합니다.

따라서 이 곡면은 $yz$-평면($x=0$)이나 $xz$-평면($y=0$)에 있는 단면 곡선을 z축을 중심으로 회전시켜 얻을 수 있습니다. 예를 들어, $xz$-평면($y=0$)에 있는 프로파일 곡선은 타원 $\frac{x^2}{a^2} + \frac{z^2}{c^2} = 1$입니다.

결론적으로, **$E_{a,a,c}$는 $xz$-평면의 타원을 z축을 중심으로 회전시킨 회전곡면** 입니다.

#### (b) 매개변수화, 제1 기본 형식, 크리스토펠 기호

**1. 매개변수화

(a)에서 보인 바와 같이, $E_{a,a,c}$는 회전곡면이므로 다음과 같이 매개변수화할 수 있습니다. $u$는 위도와 유사한 각도, $v$는 경도와 유사한 회전 각도입니다. ($u \in [0, \pi], v \in [0, 2\pi]$)

$$
\mathbf{x}(u,v) = (a\sin u \cos v, a\sin u \sin v, c\cos u)
$$

**2. 제1 기본 형식 (FFF)

먼저 각 매개변수에 대한 편미분 벡터를 구합니다.

$$
\mathbf{x}_u = (a\cos u \cos v, a\cos u \sin v, -c\sin u)
$$



$$
\mathbf{x}_v = (-a\sin u \sin v, a\sin u \cos v, 0)
$$

이제 FFF의 계수 $E, F, G$를 계산합니다.
* $E = \mathbf{x}_u \cdot \mathbf{x}_u = (a\cos u \cos v)^2 + (a\cos u \sin v)^2 + (-c\sin u)^2 = a^2\cos^2 u + c^2\sin^2 u$
* $F = \mathbf{x}_u \cdot \mathbf{x}_v = -a^2\cos u \sin u \cos v \sin v + a^2 \cos u \sin u \sin v \cos v + 0 = 0$
* $G = \mathbf{x}_v \cdot \mathbf{x}_v = (-a\sin u \sin v)^2 + (a\sin u \cos v)^2 = a^2\sin^2 u$

따라서 제1 기본 형식은 다음과 같습니다.

$$
I = (a^2\cos^2 u + c^2\sin^2 u)du^2 + (a^2\sin^2 u)dv^2
$$

**3. 크리스토펠 기호

$F=0$이고 $E, G$는 $v$에 무관하므로 계산이 간단해집니다. 필요한 도함수는 다음과 같습니다.
* $E_u = \frac{\partial E}{\partial u} = -2a^2\cos u \sin u + 2c^2\sin u \cos u = (c^2-a^2)\sin(2u)$
* $G_u = \frac{\partial G}{\partial u} = 2a^2\sin u \cos u = a^2\sin(2u)$
* $E_v = G_v = 0$

이를 크리스토펠 기호 공식에 대입하면 $0$이 아닌 기호들은 다음과 같습니다.

$$
\Gamma_{11}^1 = \frac{E_u}{2E} = \frac{(c^2-a^2)\sin(2u)}{2(a^2\cos^2 u + c^2\sin^2 u)}
$$



$$
\Gamma_{22}^1 = \frac{-G_u}{2E} = \frac{-a^2\sin(2u)}{2(a^2\cos^2 u + c^2\sin^2 u)}
$$



$$
\Gamma_{12}^2 = \Gamma_{21}^2 = \frac{G_u}{2G} = \frac{a^2\sin(2u)}{2a^2\sin^2 u} = \cot u
$$

나머지 기호들($\Gamma_{11}^2, \Gamma_{12}^1, \Gamma_{22}^2$)은 모두 0입니다.

#### (c) 곡선 $E_{a,b,c} \cap \{x=0\}$이 측지선임을 보이기

주어진 곡선은 일반 타원면 $E_{a,b,c}$를 $yz$-평면($x=0$)으로 자른 단면으로, 방정식은 $\frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$인 타원입니다.

이 곡선이 측지선임을 보이는 가장 명확한 방법은 **대칭성** 을 이용하는 것입니다.
**"어떤 곡면을 대칭면으로 잘랐을 때 생기는 교선은 항상 그 곡면의 측지선이다."** 라는 정리가 있습니다.

**증명:**
1. 타원면 $F(x,y,z) = (\frac{x}{a})^2 + (\frac{y}{b})^2 + (\frac{z}{c})^2 - 1 = 0$은 $F(-x,y,z) = F(x,y,z)$를 만족하므로 $yz$-평면($x=0$)에 대해 대칭 입니다. 문제의 곡선은 바로 이 대칭면에 포함됩니다.
2. 측지선의 정의는 곡선을 호장(arc-length)으로 매개변수화했을 때, 그 가속도 벡터 $\ddot{\gamma}(s)$가 모든 점에서 곡면에 수직 인 것입니다.
3. 우리의 곡선 $\gamma(s) = (0, y(s), z(s))$를 호장 $s$로 매개변수화했다고 합시다. 이 곡선은 $yz$-평면 안에 있으므로, 가속도 벡터 $\ddot{\gamma}(s)=(0, y''(s), z''(s))$ 역시 $yz$-평면 안에 있습니다.
4. 한편, $yz$-평면 위의 점 $(0,y,z)$에서 타원면의 법선 벡터(normal vector)는 그라디언트로 주어집니다.

$$
\nabla F = \left(\frac{2x}{a^2}, \frac{2y}{b^2}, \frac{2z}{c^2}\right) \implies \nabla F|_{(0,y,z)} = \left(0, \frac{2y}{b^2}, \frac{2z}{c^2}\right)
$$

이 법선 벡터 또한 **$yz$-평면 안에 있습니다.**
5. $yz$-평면 안에서 곡선 $\gamma(s)$는 타원입니다. 평면 곡선을 호장으로 매개변수화할 때, 그 가속도 벡터는 곡선의 법선 방향을 향합니다. $yz$-평면에서 타원 $\frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$의 법선 벡터 방향은 그라디언트 방향인 $(\frac{2y}{b^2}, \frac{2z}{c^2})$와 같습니다.
6. 따라서 곡선의 가속도 벡터 $\ddot{\gamma}(s)=(0, y''(s), z''(s))$는 벡터 $(0, \frac{2y}{b^2}, \frac{2z}{c^2})$에 평행합니다.
7. 이는 곡선의 가속도 벡터가 곡면의 법선 벡터와 평행함 을 의미하므로, 정의에 따라 이 곡선은 측지선입니다.

이 증명은 $b$와 $c$의 값에 관계없이 성립하므로, 일반적인 타원면의 주축 단면은 항상 측지선이 됩니다.

다음은 주어진 미분기하학 문제에 대한 번역, 핵심 개념 설명 및 모범 답안입니다.

### 문제 번역

15. (10점) $0 < r < R$에 대해 다음과 같은 사상(map)을 정의하자.

$$
\mathbf{x} : \mathbb{R}^2 \to \mathbb{R}^3
$$



$$
(\theta, \phi) \mapsto ((R+r\cos\theta)\cos\phi, (R+r\cos\theta)\sin\phi, r\sin\theta)
$$

$T^2$를 사상 $\mathbf{x}$의 상(image)이라고 하자.

(a) 적분 $\int_{T^2} K dA$를 계산하라. 여기서 $K$는 $T^2$의 가우스 곡률이다.

(b) $\theta_0$를 고정하자. 점 $p = \mathbf{x}(\theta_0, 0)$를 잡고, $p$에서의 접선벡터를 $v = \mathbf{x}_\theta(\theta_0, 0)$라고 하자. 경로 $\gamma_{\theta_0} : [0, 2\pi] \to T^2$를 $\phi \mapsto \mathbf{x}(\theta_0, \phi)$로 정의하자.
경로 $\gamma_{\theta_0}$를 따라 $v$를 평행이동(parallel transport)한 결과를 계산하라. 각도 변화량(modulo $2\pi$)은 얼마인가?

### 핵심 개념

이 문제를 해결하려면 다음 개념들을 알아야 합니다.

* **원환면 (Torus, $T^2$)** : 문제에 주어진 사상은 **토러스** (도넛 모양 🍩)를 매개변수화한 것입니다. $R$은 토러스 중심에서 튜브 중심까지의 거리(** 큰 반지름** ), $r$은 튜브 자체의 반지름(** 작은 반지름** )입니다.
* **가우스-보네 정리 (Gauss-Bonnet Theorem)** : 곡면의 총 가우스 곡률(기하학적 속성)이 그 곡면의 오일러 지표(위상적 속성)와 같다는 정리입니다. 닫힌 곡면 $S$에 대해 $\int_S K dA = 2\pi\chi(S)$가 성립합니다.
* **오일러 지표 (Euler Characteristic, $\chi$)** : 표면의 위상적 특성으로, 구멍의 개수와 관련이 있습니다. 구의 오일러 지표는 2이고, 구멍이 하나인 토러스의 오일러 지표는 0입니다.
* **평행이동 (Parallel Transport)** : 곡면 위의 한 벡터를 곡선을 따라 "방향을 바꾸지 않고" 그대로 옮기는 과정입니다. 여기서 '방향을 바꾸지 않는다'는 것은 3차원 공간 기준이 아니라, 곡면 자체의 기하학적 관점에서의 의미입니다. 수학적으로는 벡터의 공변 도함수(covariant derivative)가 0이 되도록 이동하는 것을 말합니다.
* **홀로노미 (Holonomy)** : 평행이동을 통해 닫힌 경로를 따라 벡터를 한 바퀴 돌렸을 때, 원래 벡터와 달라진 각도 차이를 홀로노미라고 합니다. 이 값은 곡면의 곡률에 의해 결정됩니다.

### 모범 답안

#### (a) 총 가우스 곡률 적분

이 문제는 **가우스-보네 정리** 를 이용하면 즉시 해결됩니다.

1. 곡면 식별 : 주어진 사상 $\mathbf{x}(\theta, \phi)$가 나타내는 곡면 $T^2$는 원환면(토러스) 입니다.
2. 오일러 지표 : 토러스는 손잡이가 하나 달린 구와 위상적으로 같으며, 구멍이 하나 뚫려 있습니다. 토러스의 오일러 지표(Euler characteristic)는 $\chi(T^2) = 0$ 입니다.
3. 가우스-보네 정리 적용 : 닫힌 곡면에 대한 가우스-보네 정리는 다음과 같습니다.

$$
\int_{T^2} K dA = 2\pi \chi(T^2)
$$

4. 결론 : 위 식에 $\chi(T^2)=0$을 대입하면,

$$
\int_{T^2} K dA = 2\pi \cdot 0 = 0
$$

따라서 토러스의 총 가우스 곡률은 **0** 입니다. 이는 토러스의 바깥쪽(양의 곡률)과 안쪽(음의 곡률)의 휘어짐이 전체적으로 서로 상쇄됨을 의미합니다.

#### (b) 평행이동과 각도 변화

벡터 $v$를 경로 $\gamma_{\theta_0}$를 따라 평행이동시킨 벡터 필드 $V(\phi)$를 구해야 합니다. 이는 공변 도함수를 이용한 미분방정식을 푸는 과정입니다.

1. 경로와 벡터 :
* 경로 $\gamma_{\theta_0}(\phi) = \mathbf{x}(\theta_0, \phi)$는 $\theta_0$가 일정한 **위선(latitude circle)** 입니다.
* 초기 벡터 $v = \mathbf{x}_\theta(\theta_0, 0)$는 $\phi$ 방향에 수직인 **경선(meridian)** 방향의 접선벡터입니다.

2. 평행이동 방정식 :
평행이동된 벡터 필드 $V(\phi) = a(\phi)\mathbf{x}_\theta + b(\phi)\mathbf{x}_\phi$는 평행이동의 정의($\nabla_{\dot{\gamma}}V=0$)에 따라 다음 연립 미분방정식을 만족합니다. (크리스토펠 기호를 사용한 계산 과정은 길어 생략하며, 결과만 보입니다.)

$$
a'(\phi) = -b(\phi) \frac{\sin\theta_0(R+r\cos\theta_0)}{r}
$$

  

$$
b'(\phi) = a(\phi) \frac{r\sin\theta_0}{R+r\cos\theta_0}
$$

초기 조건은 $V(0) = v = \mathbf{x}_\theta$이므로 $a(0)=1, b(0)=0$ 입니다.

3. 미분방정식 풀이 :
위 연립방정식을 풀면 다음과 같은 해를 얻습니다.

$$
a(\phi) = \cos(\phi\sin\theta_0)
$$

  

$$
b(\phi) = \frac{r}{R+r\cos\theta_0} \sin(\phi\sin\theta_0)
$$

4. 평행이동된 벡터 :
따라서 경로를 따라 평행이동된 벡터 필드는 다음과 같습니다.

$$
V(\phi) = \cos(\phi\sin\theta_0) \mathbf{x}_\theta(\theta_0, \phi) + \frac{r}{R+r\cos\theta_0} \sin(\phi\sin\theta_0) \mathbf{x}_\phi(\theta_0, \phi)
$$

경로를 한 바퀴 돈 후($\phi=2\pi$)의 최종 벡터는 $V(2\pi)$가 됩니다.

5. 각도 변화량 계산 :
초기 벡터 $v$와 최종 벡터 $V(2\pi)$ 사이의 각도 변화를 계산해야 합니다.
벡터 $\mathbf{x}_\theta$와 $\mathbf{x}_\phi$는 서로 직교하므로, 이들을 정규화한 기저벡터 $e_1 = \mathbf{x}_\theta/r$, $e_2 = \mathbf{x}_\phi/(R+r\cos\theta_0)$를 기준으로 $V(\phi)$를 표현하면, $V(\phi)$가 $e_1$ 방향(초기 벡터 방향)과 이루는 각은 $\alpha(\phi) = \phi\sin\theta_0$ 입니다.

따라서 $\phi$가 $0$에서 $2\pi$까지 변하는 동안 총 각도 변화량 $\Delta\alpha$는 다음과 같습니다.

$$
\Delta\alpha = \alpha(2\pi) - \alpha(0) = 2\pi\sin\theta_0 - 0 = 2\pi\sin\theta_0
$$

**결론** : 경로를 따라 벡터 $v$를 평행이동했을 때 생기는 총 각도 변화량은 **$2\pi\sin\theta_0$** 입니다. 이 결과는 토러스의 곡률 때문에 발생하며, 특히 위선이 토러스의 가장 바깥쪽($\theta_0=0$)이나 안쪽($\theta_0=\pi$)에 있을 때는 각도 변화가 없고($\sin\theta_0=0$), 가장 위쪽($\theta_0=\pi/2$)이나 아래쪽($\theta_0=3\pi/2$)에 있을 때 가장 큰 각도 변화($\pm 2\pi$)가 생깁니다.