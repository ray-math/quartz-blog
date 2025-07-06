수학자들은 어떤 집합에 위상을 부여할 때, 그 위상이 특정 공리를 만족하도록 선택함으로써, 해당 공간에 대해 많은 정보를 미리 알 수 있기를 원한다. 이를 위해 일반적인 위상공간의 공리 외에도, 추가적인 조건을 요구하는 것이 가능하며, 그 대표적인 예가 바로 분리 공리(Separation Axioms)이다.

이러한 공리들은 서로 다른 점이나 닫힌집합을 열린집합으로 분리할 수 있는 정도를 규정하며, 다음과 같이 정의된다. 위상공간 $(X, \tau)$에 대해 다음 조건들을 고려할 수 있다:

* $T_0$ 공리는 서로 다른 두 점 $a, b \in X$에 대해, $a$만 포함하거나 $b$만 포함하는 열린집합 $O$가 존재하는지를 요구한다. 즉, $a \in O$, $b \notin O$ 또는 $b \in O$, $a \notin O$인 경우가 있어야 한다.
* $T_1$ 공리는 각 점 $a$와 $b$에 대해, $a$를 포함하되 $b$는 포함하지 않는 열린집합과, $b$를 포함하되 $a$는 포함하지 않는 열린집합이 각각 존재해야 한다.
* $T_2$ 공리, 즉 하우스도르프(Hausdorff) 공리는 두 점 $a, b$를 각각 포함하는 열린집합 $O_a, O_b$가 존재하며 이 둘이 서로소($O_a \cap O_b = \varnothing$)가 되도록 요구한다.
* $T_3$ 공리는 닫힌집합 $A$와 $A$에 속하지 않는 점 $b$에 대해, $A$와 $b$를 각각 포함하는 서로소인 열린집합이 존재함을 요구한다.
* $T_4$ 공리는 서로소인 닫힌집합 $A$, $B$에 대해, $A$와 $B$를 각각 포함하는 서로소 열린집합이 존재해야 한다.
* $T_5$ 공리는 서로 분리된 집합 $A$, $B$에 대해, 마찬가지로 서로소인 열린 근방이 존재해야 함을 의미한다. 여기서 분리되었다는 것은 $A \cap \overline{B} = \overline{A} \cap B = \varnothing$인 경우를 말한다.

공간이 이러한 공리들 중 하나라도 만족한다면, 우리는 그 공간을 $T_i$ 공간이라 부른다. $T_0$ 공간은 Kolmogorov 공간, $T_1$ 공간은 Fréchet 공간, 그리고 $T_2$ 공간은 일반적으로 Hausdorff 공간이라고 불린다.

이러한 분리 공리는 위상공간의 일반 공리들과는 독립적으로 존재할 수 있다. 예를 들어, 어떤 위상공간은 이 공리들 중 어느 것도 만족하지 않을 수 있다 (예: Double Pointed Countable Complement Topology). 그러나 이 공리들 사이에는 포함 관계가 존재한다. 예를 들어, $T_2$는 $T_1$을 함의하며, $T_1$은 $T_0$를 함의한다.

하지만 그 역은 항상 성립하지 않는다. 예를 들어, $T_0$이지만 나머지 공리를 만족하지 않는 공간이 존재한다 (예: Overlapping Interval Topology). 또, $T_1$이지만 $T_2$ 이상은 만족하지 않는 공간도 있으며 (예: Finite Complement Topology on a Countable Space), $T_2$ 공간이면서도 $T_3$, $T_4$, $T_5$는 만족하지 않는 공간도 존재한다 (예: Irrational Slope Topology).

한편, $T_3$ 또는 $T_4$ 공리가 다른 분리 공리들을 함의하지 않으며 (예: 각각 Tychonoff Corkscrew, Thomas' Corkscrew), $T_2$ 공간이면서 컴팩트하면 $T_4$가 되지만 $T_5$는 보장되지 않는다 (예: Tychonoff Plank). 이와 달리 $T_5$ 공리는 $T_4$를 항상 포함하지만, 다른 공리들과는 여전히 독립적이다.

이러한 구조는 위상공간을 분류할 때 매우 유용하다. 각각의 분리 공리는 위상의 세밀한 구조를 설명하며, 특히 함수의 연속성, 닫힘 조건, 컴팩트성 등의 개념과 밀접한 관계를 갖는다.

## 정칙 공간과 정규 공간 (Regular and Normal Spaces)

분리 공리 그 자체보다 더 중요한 것은, 이러한 공리를 활용하여 점점 더 강력한 성질을 정의할 수 있다는 점이다. 예를 들어, 한 공간이 $T_3$이며 동시에 $T_0$일 때, 그것은 $T_2$가 된다. 반면 $T_4$이고 동시에 $T_1$이면, 그것은 $T_3$ 공간이 된다. 이 중 전자의 경우를 정칙 공간(regular space) 이라 하고, 후자의 경우를 정규 공간(normal space) 이라 부른다.

구체적으로 말하면, 위상공간 $X$가 다음 조건을 만족할 때:

* $T_0$이면서 $T_3$이면, 정칙(regular)이라 하고,
* $T_1$이면서 $T_4$이면, 정규(normal)이라 하며,
* $T_1$이면서 $T_5$이면, 완전정규(completely normal)이라 한다.

이러한 정의들 사이에는 다음과 같은 포함 관계가 성립한다:

$$
\text{완전정규} \Rightarrow \text{정규} \Rightarrow \text{정칙} \Rightarrow \text{하우스도르프} \Rightarrow T_1 \Rightarrow T_0
$$

그러나 이러한 포함 관계의 역은 일반적으로 성립하지 않는다. 다음의 예시는 각각의 역이 성립하지 않음을 보여주는 반례들이다:

* $T_4$이지만 $T_1$이 아닌 경우: Tychonoff Plank
* 정칙이지만 완전정칙이 아닌 경우: Tychonoff Corkscrew
* 완전정칙이지만 정규은 아닌 경우: Deleted Tychonoff Corkscrew
* 하우스도르프이지만 완전하우스도르프는 아닌 경우: Irrational Slope Topology
* $T_1$이지만 $T_0$ 이외 공리는 만족하지 않는 경우: Finite Complement Topology on a Countable Space
* $T_0$이지만 그 외 공리는 만족하지 않는 경우: Overlapping Interval Topology

문헌에 따라 "정칙(regular)"과 "정규(normal)"의 용법은 다를 수 있다. 일부 문헌에서는 이를 각각 $T_3$, $T_4$ 공간과 동일시하지만, 여기에서는 "정칙"과 "정규"이라는 고유한 용어를 사용하여 혼동을 피하고자 한다.

## 완전 하우스도르프 공간

분리 성질의 변형 가운데 하나는, $T_2$, $T_3$, $T_4$ 공리에서 열린집합 대신 닫힌 근방(closed neighborhood) 을 사용하는 방식이다.

정규 공간에서는, 열린집합 $O$가 닫힌집합 $A$를 포함할 경우 항상 $O$ 안에 $A$의 닫힌 근방이 존재한다. 예를 들어 $A, B$가 서로소인 닫힌집합이면, 이를 포함하는 열린집합 $O_A, O_B$에 대해 닫힌 근방 $\overline{O}_A, \overline{O}_B$ 역시 서로소가 된다:

$$
\overline{O}_A \cap \overline{O}_B = \varnothing
$$

그러므로 정규성의 정의에서 열린집합 대신 닫힌 근방을 사용하는 경우도 같은 공간 범주를 정의한다.

하지만 하우스도르프 공간 중에는 두 점을 분리하는 닫힌 근방이 존재하지 않는 경우도 있으므로, 다음과 같은 새로운 공리를 도입한다:

$$
T_{2\frac{1}{2}} \text{ 공리: 두 점 } a, b \in X \text{ 에 대해, } a, b \text{ 를 포함하는 열린집합 } O_a, O_b \text{ 가 존재하여 } \overline{O}_a \cap \overline{O}_b = \varnothing \text{ 를 만족}.
$$

이 조건을 만족하는 공간을 완전 하우스도르프 공간 (completely Hausdorff space) 이라고 부른다. 모든 정칙 공간은 완전 하우스도르프이며, 이는 다시 하우스도르프 공간을 포함한다. 그러나 완전 하우스도르프이면서도 정칙이 아닌 경우도 존재한다 (예: Modified Fort Space).

요약하면 완전 하우스도르프 성질은 하우스도르프와 정칙 사이의 중간 수준에 해당한다.

## 완전 정칙 공간

분리 공리의 두 번째 변형은, 특정 연속 실수값 함수의 존재를 다룬다. 공간 $X$의 서로소 부분집합 $A$, $B$에 대해, Urysohn 함수란 다음 조건을 만족하는 연속 함수 $f: X \to [0,1]$이다:

$$
f|_A = 0, \quad f|_B = 1
$$

Urysohn의 유명한 보조정리에 따르면, 만약 $A$와 $B$가 $T_4$ 공간의 서로소 닫힌집합이라면, 그러한 Urysohn 함수는 항상 존재한다. 반대로, 만약 임의의 서로소 닫힌집합 $A$, $B$에 대해 항상 이러한 함수가 존재한다면, 그 공간은 $T_4$ 공간이다. 그러나 이러한 함수의 존재가 곧 $T_1$ 공간이거나 정규 공간임을 보장하지는 않는다 (예: Sierpiński Space).

한편, 정칙 공간에서의 Urysohn 보조정리는 일반적으로 성립하지 않는다 (예: Tychonoff Corkscrew, 예시 90 참조). 따라서 이 경우에는 다음과 같은 새로운 공리를 정의한다:

$$
T_{3\frac{1}{2}} \text{ 공리: } A \text{ 가 } X \text{ 의 닫힌집합이고, } b \notin A \text{ 일 때, } A \text{ 와 } \{b\} \text{ 에 대해 Urysohn 함수가 존재한다}.
$$

이 공리를 만족하는 공간을 완전 정칙 공간(completely regular space) 또는 Tychonoff 공간이라고 한다. 이러한 공간은 항상 $T_3$ 공간이지만, 반드시 $T_2$이거나 $T_1$ 공간일 필요는 없다. 그러나 만약 $T_0$까지 만족한다면, 이는 곧 $T_3$ 공간이 된다. 따라서 완전 정칙 공간은 일반 정칙 공간보다 더 강한 조건이며, 동시에 하우스도르프이고, 따라서 $T_1$ 공간이다.

정규 공간은 항상 $T_{3\frac{1}{2}}$ 공간이기 때문에, 완전 정칙이기도 하다. 왜냐하면 정규 공간에서는 모든 점이 닫힌집합이므로, Urysohn 보조정리를 적용할 수 있기 때문이다. 그러나 정칙이면서 완전 정칙이 아닌 공간도 존재하고 (예: Tychonoff Corkscrew), 완전 정칙이면서도 정규 공간이 아닌 경우도 존재한다 (예: Deleted Tychonoff Corkscrew).

정규 공간은 일반적으로 $T_{3\frac{1}{2}}$ 공간이지만, $T_4$ 공간이 항상 그런 것은 아니다 (예: Sorgenfrey Plane, 예시 55 참조). 그러나 어떤 $T_4$ 공간이 $T_3$ 공간이기도 하다면, 비록 정규은 아닐지라도 반드시 $T_{3\frac{1}{2}}$ 공리를 만족하게 된다. 그 이유는 다음과 같다. 점 $p$가 닫힌집합 $A$에 속하지 않는다면, $T_3$ 공간에서 $A$와 $p$를 분리하는 열린집합이 존재하고, 그 여집합 $B$는 $A$와 서로소인 닫힌집합이 된다. 이때 공간이 $T_4$이면, Urysohn 보조정리를 사용하여 $A$와 $B$를 구분하는 Urysohn 함수를 구성할 수 있다. 이 함수는 $A$와 $\{p\}$를 구분하는 함수가 되므로, $T_{3\frac{1}{2}}$ 조건을 만족하게 된다.

$$
\text{완전정규} \Rightarrow \text{정규} \Rightarrow \text{완전정칙} \Rightarrow \text{정칙} \Rightarrow \text{완전하우스도르프} \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0
$$

| 포함 관계             | 번호   | 예시                                            |
| ----------------- | ---- | --------------------------------------------- |
| 완전정상 ⇒ 정규         | (86) | Tychonoff Plank                               |
| 정규 ⇒ 완전정칙         | (82) | Deleted Tychonoff Corkscrew                   |
| 완전정칙 ⇒ 정칙         | (90) | Tychonoff Corkscrew                           |
| 정칙 ⇒ 완전하우스도르프     | (78) | Arens Square                                  |
| 완전하우스도르프 ⇒ 하우스도르프 | (75) | Irrational Slope Topology                     |
| $T_2$ ⇒ $T_1$     | (18) | Finite Complement Topology on a Countable Set |
| $T_1$ ⇒ $T_0$     | (8)  | Particular Point Topology                     |

## 함수, 곱공간, 부분공간

모든 분리 성질들은 위상적 성질들이며, 이는 곧 이러한 성질들이 위상동형(homeomorphism)에 대해 보존된다는 뜻이다. 그러나 일부 성질들은 더 약한 함수들에 대해서도 보존된다.

만약 $X$와 $Y$가 위상공간이고, $f: X \to Y$가 닫힌 전단사(closed bijection)이며 $X$가 $T_0$, $T_1$, 하우스도르프(Hausdorff), 또는 완전 하우스도르프(completely Hausdorff) 공간이라면, $Y$ 역시 각각 $T_0$, $T_1$, 하우스도르프, 또는 완전 하우스도르프가 된다. 특히, $\tau_1 \subset \tau_2$가 $X$ 위의 위상들이라면, $(X, \tau_1)$에서 $(X, \tau_2)$로 가는 항등 함수는 닫힌 함수이다. 우리는 $\tau_2$를 $\tau_1$의 확장(expansion) 이라 부르며, 이러한 확장은 위에서 언급한 분리 성질들을 보존한다. 그러나 더 강한 분리 성질들은 일반적으로 확장에서 보존되지 않는다 (예: Modified Dieudonné Plank, 원래는 Example 66).

대부분의 분리 성질들은 곱공간(product)에서는 보존된다. 만약 $X = \prod X_\alpha$이고, $X_\alpha$가 각각 $T_0$, $T_1$, 하우스도르프, 완전 하우스도르프, 정칙(regular), 또는 완전 정칙(completely regular) 공간이라면, 전체 곱공간 $X$ 역시 그러하다. 다시 말해, 각 성분이 해당 성질을 가질 때, 전체 곱도 해당 성질을 갖는다. 그러나 만약 $X$가 정규(normal) 또는 완전 정규(completely normal) 공간이라면, 각 $X_\alpha$가 정규 혹은 완전 정규이긴 하지만, 그 역은 성립하지 않는다 (예: Product of Countably Many Closed Intervals with the Box Topology, 원래는 Example 84).

정규성은 부분공간의 경우에서도 다른 분리 성질들과는 다르게 작용한다. $T_0$, $T_1$, 하우스도르프, 완전 하우스도르프, 정칙, 또는 완전 정칙 공간의 모든 부분공간은 동일한 성질을 가진다. 그러나 정규 공간의 부분공간이 항상 정규일 필요는 없다. 오직 닫힌 부분공간만이 정규성을 보존한다 (예: Tychonoff Plank, 원래는 Example 86).

반면, 완전 정규 공간(completely normal space)의 모든 부분공간은 완전 정규이다. 왜냐하면 어떤 공간이 모든 부분공간에서 정규이면, 그 공간은 완전 정규이기 때문이다. 실제로, 어떤 공간이 $T_5$ 공간임과 모든 부분공간이 $T_4$ 공간임은 동치이다.

## 추가적인 분리 성질

Urysohn의 보조정리에 따르면, $T_4$ 공간에서는 임의의 서로소 닫힌집합들 사이에 Urysohn 함수가 항상 존재한다. 이러한 함수를 점과 닫힌집합 사이에 요구하면 $T_{3\frac{1}{2}}$ 성질이 되며, 이는 $T_3$보다 강한 조건이다. 이 조건을 두 점 사이에 요구하면 이는 완전 하우스도르프(completely Hausdorff)보다도 더 강한 조건이 된다 (예: Arens Square). 우리는 임의의 두 점에 대해 Urysohn 함수가 존재하는 공간을 Urysohn 공간이라 부른다.

모든 닫힌집합이 $G_\delta$ 집합인 $T_4$ 공간은 흔히 완전 $T_4$ 공간이라 불리며, 그것이 $T_1$ 공간이기도 하면 완전정규(perfectly normal) 공간이라 부른다. 모든 완전정규 공간은 완전정규이지만, 그 역은 일반적으로 성립하지 않는다 (예: Closed Ordinal Space).

한편, $T_3$ 공간에서는 모든 열린집합이 그 안의 각 점을 포함하는 닫힌 근방을 포함하므로, 결국 모든 열린집합은 정칙(open = int(cl(open)))인 열린집합들의 합으로 표현될 수 있다. 그러나 그 역은 일반적으로 성립하지 않으므로 (예: Prime Ideal Topology), 우리는 정칙 열린집합들이 위상의 기저를 이루는 모든 $T_2$ 공간을 준정칙(semiregular) 공간이라 부른다. 그러나 이러한 준정칙 공간이 반드시 완전 하우스도르프나 Urysohn 공간이 되는 것은 아니다 (예: Arens Square 및 Prime Ideal Topology).

추가된 성질들을 기존의 분리 공리 체계에 포함하면, 아래와 같은 포함 관계가 성립한다:

$$
\text{완전정규} \Rightarrow \text{완전정규} \Rightarrow \text{정규} \Rightarrow \text{완전정칙} \Rightarrow \text{Urysohn} \Rightarrow \text{정칙} \Rightarrow \text{완전하우스도르프} \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0
$$

준정칙 공간은 정칙 공간보다 약하지만, $T_2$ 성질은 유지한다:

$$
\text{준정칙} \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0
$$






