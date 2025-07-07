### 프레네 공식

곡선 $\alpha(s)$가 호의 길이 $s$로 매개변수화되어 있다고 가정하자. $t(s) = \alpha'(s)$ 일 때 각 점 $s$에 대해, 단위 접벡터 $t(s)$, 법선벡터 $n(s)$, 종법선벡터 $b(s)$로 구성된 직교 기저 $(t, n, b)$를 프레네 구조(Frenet–Serret frame)라고 한다. 이 벡터들은 다음의 프레네 공식을 만족한다[^1]

$$
\begin{aligned}
t'(s) &= k(s)n(s) \\
n'(s) &= -k(s)t(s) - \tau(s)b(s) \\
b'(s) &= \tau(s)n(s)
\end{aligned}
$$

* $k(s)$: 곡률 (curvature), 곡선이 얼마나 휘어졌는지
* $\tau(s)$: 비틀림 (torsion), 곡선이 얼마나 평면에서 벗어나는지

* $t(s)$: 단위 접벡터
* $n(s)$: 곡률 방향의 법선벡터 (곡선이 휘는 방향)
* $b(s)$: $t \wedge n$으로 정의되는 종법선벡터

* $(t, n)$ 평면은 접촉법면 (osculating plane)
* $(n, b)$ 평면은 법평면 (normal plane)
* $(t, b)$ 평면은 전직평면 (rectifying plane)이라 한다.

## 곡률, 비틀림률 계산
- 곡률[^2]
$$
\kappa(t) = \frac{|\alpha'(t) \wedge \alpha''(t)|}{|\alpha'(t)|^3}
$$
- 비틀림률[^3]
$$
\tau(ts) = \frac{(\alpha'(t) \wedge \alpha''(t)) \cdot \alpha'''(t)}{|\alpha'(t) \wedge \alpha''(t)|^2}
$$

- 평면 곡선 $\alpha(s) = (x(t), y(t)) \in \mathbb{R}^2$의 경우, 곡률은

$$
\kappa(t) = \frac{x'(t)y''(t) - x''(t)y'(t)}{(x'(t)^2 + y'(t)^2)^{3/2}}
$$

- $\alpha(s)$가 구면 위의 곡선이고, $R$을 곡률 반경, $T$을 비틀림 반경이라고 하면

$$
R^2 + (R')^2 T^2 = \text{const.}
$$
### 국소 곡선 이론의 기본 정리(Fundamental Theorem of Local Theory)

미분가능한 함수 $k(s) > 0$, $\tau(s)$가 주어지면, 유일한 정칙 곡선 $\alpha: I \to \mathbb{R}^3$이 존재하며 이러한 곡선은 강체 운동에 의해서만 달라질 뿐, 본질적으로 동일하다. 즉, 동일한 $k(s), \tau(s)$를 가지는 두 곡선은 회전 및 평행이동만으로 서로 대응된다.

[^1]: $\frac{d}{ds} \begin{bmatrix} t \\ n \\ b\end{bmatrix} = \begin{bmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{bmatrix} \begin{bmatrix} t \\ n \\ b \end{bmatrix}$, $A^T = -A$ 이므로 $A$는 skew-symmetric matrix (반대칭 행렬)이다. $v \cdot Av = 0$ 이므로 $Av$항상 $v$에 수직이다. 반대칭 행렬은 프레임이 길이를 보존한 채 회전(크기는 유지하고 방향만 바꾸는 유일한 방법)만 한다는 걸 수학적으로 보장해 주는 구조이다.
[^2]: 속도와 가속도의 외적의 크기를 속도 보정으로 나눈다.
[^3]: 속도와 가속도의 외적의 방향이 얼마나 회전하는가 측정한다.