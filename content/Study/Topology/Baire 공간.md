---
title: Baire 공간(Baire Spaces)
date: 2025-06-14
tags:
---
## 빈 내부(empty interior)
$A$가 빈 내부(empty interior)를 갖는다는 것은 $A$가 공집합을 제외하고는 $X$의 어떤 열린집합도 포함하지 않는다는 의미입니다. 즉, $\text{int}(A) = \emptyset$인 상태를 말합니다.

$A$에 속한 어떤 점 $a$를 잡아도, 그 점 주변에 **온전히 $A$에만 속하는 근방**을 만들 수 없다는 것은 $a$의 근방에 $A$의 바깥, 즉 $A^c$의 점을 포함하게 됩니다. 따라서, $A$가 공집합 내부를 갖는 것은 $A$의 모든 점이 $A^c$의 극한점(limit point)에 포함됩니다. 

$$
\overline{A^c} =  (A^c )' \cup A^c = X
$$

따라서 $A^c$는 $X$에서 조밀(dense)합니다. 

## 성긴 집합(nowhere dense)
$A$가 nowhere dense라는 것은 $\overline{A}$의 내부가 공집합인 상태를 말합니다.

$$
\text{int}(\overline{A}) = \emptyset
$$

## Baire 공간(Baire Spaces)

### 정의
$X$의 **닫힌집합**들로 이루어진 **가산** 집합족(countable collection) $\{A_n\}$의 각 원소 $A_n$이 모두 $X$에서 빈 내부(empty interior)를 가질 때, 그들의 합집합 $\bigcup A_n$ 또한 $X$에서 빈 내부를 가진다.

$\{ A_n \}$이 닫힌집합이면, $A_n = \overline{A_n}$이므로, $A_n$은 nowhere dense 집합이다. 따라서, Baire 공간의 정의는 "$X$의 nowhere dense 집합들로 이루어진 가산 집합족 $\{A_n\}$이 주어졌을 때, $\bigcup_{n=1}^{\infty} A_n$은 $X$에서 빈 내부(empty interior)를 가진다"로 바꿀 수 있다.

이를 이용하면 Baire 공간을 쉽게 판단할 수도 있다. 

$$
\text{int} \left( \bigcup_{n=1}^{\infty} A_n \right) = \emptyset \quad \Rightarrow  \quad \bigcup_{n=1}^{\infty} A_n \not= X
$$

### 보조정리
공간 $X$가 베르 공간인 것은, $X$의 열린집합들로 이루어진 임의의 가산 집합족(countable collection) $\{U_n\}$에서 각 $U_n$이 모두 $X$에서 조밀(dense)할 때, 그들의 교집합 $\bigcap U_n$ 또한 $X$에서 조밀한 것과 필요충분조건이다.[^1]

### category
어떤 집합 $S$가 제1 범주라는 것은, $S = \bigcup_{n=1}^{\infty} A_n$ 을 만족하는, 성긴(nowhere dense) 집합들의 수열 $\{A_n\}$이 존재한다는 의미이다.

어떤 집합 $S$가 제2 범주라는 것은, $S$가 제1 범주가 아니라는 것이다. 풀어서 쓰면 $S = \bigcup_{n=1}^{\infty} A_n$을 만족하는, 성긴(nowhere dense) 집합들의 수열 $\{A_n\}$이 존재하지 않는다는 의미다. 즉, 공간 $X$가 베르 공간이라는 것은, 공간 $X$ 자기 자신이 제2 범주라는 뜻입니다.

#### 예시1. 실수 직선 $\mathbb{R}$
$\mathbb{R}$에서 가산개의 nowhere dense 집합들 $A_1, A_2, A_3, \cdots$에 대하여, $\text{int} \left( \bigcup_{n=1}^{\infty} A_n \right) \not= \emptyset$이라 가정하면, $(a, b) \subset \bigcup_{n=1}^{\infty} A_n$을 만족하는 $a, b$가 존재한다. 

$A_1$은 성긴 집합이므로, $\overline{A_1}$이 열린구간 $(a,b)$를 완전히 덮을 수 없다. 따라서, $(a,b) \setminus \overline{A_1}$은 공집합이 아닌 열린집합이다.

실수에서 공집합이 아닌 열린집합 안에는 반드시 어떤 닫힌구간이 존재하므로 $(a,b) \setminus \overline{A_1}$ 안에 완전히 포함되는 닫힌구간 $[a_1, b_1]$을 선택할 수 있다.

$$
[a_1, b_1] \subset (a,b) \setminus \overline{A_1}
$$

이제 열린구간 $(a_1, b_1)$에 대하여 $A_2$ 역시 성긴 집합이므로, $\overline{A_2}$는 $(a_1, b_1)$을 완전히 덮을 수 없다. 같은 방법으로, 이 안에 완전히 포함되는 닫힌구간 $[a_2, b_2]$를 선택할 수 있다.

$$
[a_2, b_2] \subset (a_1, b_1) \setminus \overline{A_2}

$$


이 과정을 반복하면, 축소하는 닫힌구간열을 만들 수 있다.

$$
(a,b) \supset [a_1, b_1] \supset [a_2, b_2] \supset \cdots \supset [a_n, b_n] \supset \cdots
$$

그리고 각각의 $n$에 대하여, $[a_n, b_n] \cap \overline{A_n} = \emptyset$ 이다. 교집합에 속하는 임의의 점 $x$를 생각해보면,

$$
x \in \bigcap_{n=1}^{\infty} [a_n, b_n]

$$

$x$는 모든 $n$에 대해 $[a_n, b_n]$에 속한다. 그런데 우리는 각 $[a_n, b_n]$을 $\overline{A_n}$과 만나지 않도록 잡았다. 따라서 $x$는 어떤 $\overline{A_n}$에도 속하지 않으며, 당연히 어떤 $A_n$에도 속하지 않는다.

$$
x \notin \bigcup_{n=1}^{\infty} A_n

$$

임의의 열린구간 $(a,b)$ 안에 $\bigcup A_n$에 속하지 않는 점 $x$가 존재하므로, $(a, b) \subset \bigcup_{n=1}^{\infty} A_n$라는 가정에 모순된다. 따라서, $\text{int} \left( \bigcup_{n=1}^{\infty} A_n \right) = \emptyset$이므로, 실수 직선 $\mathbb{R}$은 Baire 공간이다.

#### 예시 2. 유리수 $\mathbb{Q}$
유리수 $\mathbb{Q}$에서 한 점 집합은 닫혀있고, 빈 내부를 갖는다.(따라서 유리수 $\mathbb{Q}$는 nowhere dense 집합이다.) 유리수 $\mathbb{Q}$는 자신의 한 점 집합들의 가산 합집합이므로, $\mathbb{Q}$는 제1 범주이다. 따라서 $\mathbb{Q}$는 Baire 공간이 아니다.

## 베르 범주 정리(Baire Category Theorem)

만약 $X$가 컴팩트 하우스도르프 공간(compact Hausdorff space)이거나 완비 거리 공간(complete metric space)이면, $X$는 베르 공간(Baire space)이다.

### 증명
빈 내부(empty interior)를 갖는 $X$의 닫힌집합들로 이루어진 가산 집합족 $\{A_n\}$이 주어졌을 때, 우리는 그들의 합집합 $\bigcup A_n$ 또한 빈 내부를 가짐을 보여야 한다. 그러므로, $X$의 공집합이 아닌 임의의 열린집합 $U_0$가 주어졌을 때, 우리는 $U_0$에 속하면서 $A_n$ 중 어느 곳에도 놓이지 않는 점 $x$를 찾아야 한다.

첫 번째 집합 $A_1$을 생각해보자. 가정에 의해, $A_1$은 $U_0$를 포함하지 않는다. 따라서 우리는 $A_1$에 속하지 않는 $U_0$의 한 점 $y$를 선택할 수 있다. $X$의 정칙성(Regularity)과 $A_1$이 닫힌집합이라는 사실을 이용하면, 우리는 $y$의 근방(neighborhood) $U_1$을 다음과 같이 선택할 수 있다.

$$
\begin{gather*}
\overline{U}_1 \cap A_1 = \emptyset, \\
\overline{U}_1 \subset U_0
\end{gather*}
$$

만약 $X$가 거리 공간(metric)이라면, 우리는 또한 $U_1$을 지름(diameter)이 1보다 작도록 충분히 작게 선택할 수 있다.

일반적으로, 공집합이 아닌 열린집합 $U_{n-1}$이 주어졌을 때, 우리는 닫힌집합 $A_n$에 속하지 않는 $U_{n-1}$의 한 점을 선택하고, 이 점의 근방 $U_n$을 다음과 같이 선택한다. (단, 거리 공간의 경우, $\text{diam } U_n < 1/n$)

$$
\begin{gather*}
\overline{U}_n \cap A_n = \emptyset, \\
\overline{U}_n \subset U_{n-1}
\end{gather*}
$$

우리는 교집합 $\bigcap \overline{U}_n$이 공집합이 아니라고 주장한다. 이로부터 우리의 정리는 따라 나온다. 만약 $x$가 $\bigcap \overline{U}_n$의 점이라면, $\overline{U}_1 \subset U_0$이므로 $x$는 $U_0$ 안에 있다. 그리고 각각의 $n$에 대해, $\overline{U}_n$이 $A_n$과 서로소이기 때문에 점 $x$는 $A_n$에 속하지 않는다.

$\bigcap \overline{U}_n$이 공집합이 아니라는 증명은 $X$가 **컴팩트 하우스도르프 공간**인지 혹은 **완비 거리 공간인지**에 따라 두 부분으로 나뉜다. 만약 $X$가 컴팩트 하우스도르프 공간이면, 우리는 공집합이 아닌 컴팩트 부분집합들의 축소 수열(nested sequence) $\overline{U}_1 \supset \overline{U}_2 \supset \cdots$을 갖는다. 집합족 $\{\overline{U}_n\}$은 유한 교집합 성질(finite intersection property)을 가진다. $X$가 컴팩트이므로, 교집합 $\bigcap \overline{U}_n$은 반드시 공집합이 아니어야 한다.

만약 $X$가 완비 거리 공간이라면, 우리는 다음의 보조정리를 적용한다.

#### lemma
완비 거리 공간(complete metric space) $X$에서, $C_1 \supset C_2 \supset \cdots$가 공집합이 아닌 닫힌집합들의 축소 수열(nested sequence)이라고 하자. 만약 $\text{diam } C_n \to 0$ 이면, 그 교집합 $\bigcap C_n$은 공집합이 아니다.

각각의 $n$에 대해 $x_n \in C_n$을 선택하자. $n, m \ge N$일 때 $x_n, x_m \in C_N$이고, $N$을 충분히 크게 선택함으로써 $\text{diam } C_N$을 임의의 주어진 $\epsilon$보다 작게 만들 수 있으므로, 수열 $(x_n)$은 코시 수열(Cauchy sequence)이다. 이 수열이 $x$로 수렴한다고 가정하자. 그러면 주어진 $k$에 대해, 부분수열 $x_k, x_{k+1}, \cdots$ 또한 $x$로 수렴한다. 따라서 $x$는 필연적으로 $\overline{C}_k = C_k$에 속한다. 그러므로 원하는 대로 $x \in \bigcap C_k$이다.

[^1]: 빈 내부를 갖는 닫힌집합의 가산합집합이 빈 내부를 갖는다는 것은, 성긴 집합의 가산합집합이 빈 내부를 갖는다는 것과 동치다. 또한, 조밀한 열린집합의 가산교집합이 조밀하다는 것과도 동치이다.