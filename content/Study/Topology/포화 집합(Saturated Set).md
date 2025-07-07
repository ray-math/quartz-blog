## 포화 집합(Saturated Set)

전사함수 $p: X \to Y$에 대해, 부분집합 $C \subseteq X$가 포화(saturated)되었다는 것은:

> $C$가 만나는 모든 동치류(=역상 $p^{-1}(\{y\})$)를 통째로 포함하고 있다는 뜻입니다.

즉, 다음을 만족합니다:

$$
\forall y \in Y, \quad \left[ p^{-1}(\{y\}) \cap C \neq \emptyset \Rightarrow p^{-1}(\{y\}) \subseteq C \right]
$$

다르게 말하면, $C$는 어떤 $B \subseteq Y$의 완전한 역상으로 쓸 수 있어야 합니다.

$$
C = p^{-1}(B) \quad \text{for some } B \subseteq Y
$$
 
이를 달리 말하면 $C$는 자신이 만나는 모든 동치류 $p^{-1}(\{y\})$를 통째로 포함해야 합니다.

## 예시

- $X = \mathbb{R}$
- $Y = \mathbb{R} / \mathbb{Z}$ (즉, 실수를 정수 차이로 식별한 몫공간)
- 사상 $p : \mathbb{R} \to \mathbb{R} / \mathbb{Z}$, $p(x) = x \mod \mathbb{Z}$

이때, $x \sim y \iff x - y \in \mathbb{Z}$, 즉 $x$와 $y$가 정수만큼 차이 나면 같은 동치류입니다.  
각 동치류는 다음처럼 생겼습니다:

$$
p^{-1}(\{[x]\}) = \{ x + n \mid n \in \mathbb{Z} \}
$$

$$
C = \bigcup_{r \in [0, 0.5)} \{ r + n \mid n \in \mathbb{Z} \}
$$

즉, $[0,0.5)$ 구간 안의 모든 수에 대해, 정수만큼 이동한 점들을 다 모읍니다. 이건 다음과 같이 쓸 수 있습니다:

$$
C = p^{-1}([0, 0.5)) \quad \Rightarrow \text{포화}
$$

이 집합은 어떤 동치류를 만나면 그 전체를 포함하므로 포화입니다.