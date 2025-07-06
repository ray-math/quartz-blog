---
title: 
date: 2025-06-09
tags: 
---
## 국소 유한 (Locally Finite)

어떤 위상 공간 $(X, \mathcal{T})$의 부분

 집합들의 모음 $\mathcal{A} = \{A_i\}_{i \in I}$이 국소 유한이라는 것은,

> 공간 $X$의 모든 점 $x$에 대해, $x$를 포함하는 어떤 열린 근방(open neighborhood) $U_x$가 존재하여, 이 $U_x$가 $\mathcal{A}$의 원소들 중 유한개하고만 만난다.

라는 의미입니다. 즉, $U_x \cap A_i \neq \emptyset$ 인 $A_i$들의 개수가 유한하다는 뜻입니다.

직관적으로 집합들의 모음이 국소 유한하다는 것은, 공간 전체를 보면 무한히 많은 집합이 있을 수 있지만, 특정 점 주변을 확대해서 보면 유한한 개수만 보인다는 개념입니다.

## 가산 국소 유한 (Countably Locally Finite or $\sigma$-Locally Finite)

어떤 위상 공간 $(X, \mathcal{T})$의 부분 집합들의 모음 $\mathcal{A} = \{A_i\}_{i \in I}$이 가산 국소 유한이라는 것은,

> $\mathcal{A}$가 가산개의 국소 유한 모음들의 합집합으로 표현될 수 있다.

라는 의미입니다. 즉, $\mathcal{A} = \bigcup_{j=1}^{\infty} \mathcal{A}_j$ 와 같이 쓸 수 있고, 여기서 각 $\mathcal{A}_j$는 국소 유한 모음이라는 것입니다.

가산 국소 유한은 국소 유한보다 훨씬 더 광범위한 집합들의 모음을 포괄하는 개념입니다. 특정 점 주변을 확대해도 무한히 많은 집합이 나타날 수 있지만, 그 무한한 집합들을 셀 수 있는(가산) 묶음들로 나누었을 때, 각 묶음은 국소 유한하다는 것입니다.

## $\mathbb{R}$의 모든 열린 구간들의 모음

위상 공간 $(X, \mathcal{T}) = (\mathbb{R}, \mathcal{U})$ (여기서 $\mathcal{U}$는 $\mathbb{R}$의 보통 위상)을 생각하고, 집합족 $\mathcal{A}$를 $\mathbb{R}$의 모든 열린 구간들의 모음이라고 합시다.

$$
\mathcal{A} = \{ (a, b) \mid a, b \in \mathbb{R}, a < b \}

$$

$\mathcal{A}$는 국소 유한은 아니지만 가산 국소 유한입니다.

### $\mathcal{A}$는 국소 유한이 아니다.

> 국소 유한의 정의: 공간 $X$의 모든 점 $x$에 대해, $x$를 포함하는 어떤 열린 근방 $U_x$가 존재하여, 이 $U_x$가 $\mathcal{A}$의 원소들 중 유한개하고만 만난다.

이 정의에 따라 $\mathcal{A}$가 국소 유한이 아님을 보여보겠습니다.

예를 들어, $x=0$이고 $U_x = (-1, 1)$이라고 가정해 봅시다. $\mathcal{A}$에 속하는 다음과 같은 열린 구간들을 생각해 보면

$$
\mathcal{A}_k = \left( -\frac{1}{k}, \frac{1}{k}\right) \quad (k=1, 2, 3, \cdots)
$$ 
이 모든 구간들은 $U_x = (-1, 1)$ 안에 포함되며, 따라서 $U_x$와 교집합이 공집합이 아닙니다. 그리고 이 구간들은 무한히 많습니다. 마찬가지로, $U_x$가 아무리 작더라도, 예를 들어 $U_x = (x-\epsilon, x+\epsilon)$이더라도, 이 구간 안에 무한히 많은 형태의 열린 구간 (예: $(x-\epsilon/k, x+\epsilon/k)$)이 존재하며, 이는 $U_x$와 교차합니다.

따라서 어떤 점 $x$를 잡더라도, $x$의 임의의 열린 근방은 $\mathcal{A}$의 무한히 많은 원소와 만납니다. 그러므로 $\mathcal{A}$는 국소 유한이 아닙니다.

### $\mathcal{A}$는 가산 국소 유한입니다.

> 가산 국소 유한의 정의: $\mathcal{A}$가 가산개의 국소 유한 모음들의 합집합으로 표현될 수 있습니다. 즉, $\mathcal{A} = \bigcup_{j=1}^{\infty} \mathcal{A}_j$ 이고, 각 $\mathcal{A}_j$는 국소 유한입니다.

$\mathbb{R}$의 모든 열린 구간들의 모음 $\mathcal{A}$를 다음과 같이 분할합니다.

$$
\mathcal{A}_n = \{ (a, b) \in \mathcal{A} \mid b - a \ge 1/n \}
$$

길이가 $1/n$ 이상인 모든 열린 구간들의 모음 $\mathcal{A}_n$이 국소 유한임을 보이겠습니다.

임의의 점 $x \in \mathbb{R}$에 대해 근방 $U_x = (x-1/(2n), x+1/(2n))$에 대하여 구간 $(a,b) \in \mathcal{A}_n$이 $U_x$와 만난다면, $a < x + 1/(2n)$ 이고 $b > x - 1/(2n)$ 이어야 합니다. $b - a \ge 1/n$ 이므로, 이를 결합하면 $a < x + 1/(2n)$ 이고 $a + 1/n \le b$ 입니다. 따라서 $a < x + 1/(2n)$ 이고 $x - 1/(2n) < a + 1/n$ 입니다. 정리하면 $x - 3/(2n) < a < x + 1/(2n)$ 마찬가지로 $b$에 대해서는 $x - 1/(2n) < b < x + 1/(2n) + 1/n = x + 3/(2n)$ 입니다.

따라서 $U_x$와 만나는 모든 구간 $(a,b) \in \mathcal{A}_n$은 다음을 만족합니다.

$$
x - 3/(2n) < a < b < x + 3/(2n)
$$

구간 $(x - 3/(2n), x + 3/(2n))$의 길이는 $3/n$입니다. 이 유한한 구간 안에서 서로 다른 길이 $\ge 1/n$인 열린 구간들의 개수는 최대 $3$개를 넘을 수 없습니다. 왜냐하면 각 구간의 길이가 최소 $1/n$이므로, $3$개보다 많으면 총 길이가 $3/n$을 초과하기 때문입니다.

마지막으로 임의의 열린 구간 $(a,b) \in \mathcal{A}$에 대해 $L = b-a > 0$이므로, 아르키메데스 성질에 의해 $1/n \le L$을 만족하는 자연수 $n$이 존재합니다. 따라서 $(a,b) \in \mathcal{A}_n$이고, $\mathcal{A} = \bigcup_{n=1}^{\infty} \mathcal{A}_n$입니다. 따라서 $\mathcal{A}$는 가산개의 국소 유한 집합족들의 합집합이므로 가산 국소 유한입니다.

## 세분(Refinement)

세분(refinement)은 주어진 집합족(collection of subsets) $\mathcal{A}$에 대해, 더 '미세한' 집합족 $\mathcal{B}$를 만들어서, $\mathcal{A}$의 구조를 더 잘 파악하거나, 더 정밀하게 다루고자 할 때 사용합니다. 예를 들어, 어떤 공간 $X$의 open cover(열린 덮개) $\mathcal{A}$가 주어졌을 때, 이 덮개를 더 작은 열린 집합들로 이루어진 open refinement(열린 세분) $\mathcal{B}$로 바꿔서, 각 $B \in \mathcal{B}$가 어떤 $A \in \mathcal{A}$에 포함되도록 할 수 있습니다. 이 과정은 Compactness(콤팩트성) 같은 위상수학의 중요한 성질을 증명할 때 필수적입니다.

>$X$라는 공간의 부분집합들의 모임 $\mathcal{A}$가 있다고 하자. $X$의 부분집합들의 모임 $\mathcal{B}$가 $\mathcal{A}$의 세분(refinement)이라고 하거나, $\mathcal{B}$가 $\mathcal{A}$를 세분한다고 말하는 것은, $\mathcal{B}$의 각 원소 $B$에 대해 $B$를 포함하는 $\mathcal{A}$의 원소 $A$가 존재함을 의미한다. 만약 $\mathcal{B}$의 원소들이 모두 열린 집합(open set)이라면, $\mathcal{B}$를 $\mathcal{A}$의 열린 세분(open refinement)이라고 부른다. 만약 $\mathcal{B}$의 원소들이 모두 닫힌 집합(closed set)이라면, $\mathcal{B}$를 $\mathcal{A}$의 닫힌 세분(closed refinement)이라고 부른다.

## Lemma
거리화 가능 공간 $X$의 임의의 열린 덮개(open covering) $\mathcal{A}$가 있을 때, $\mathcal{A}$를 세분(refine)하는 가산 국소 유한(countably locally finite) 열린 덮개 $\mathcal{E}$가 존재한다.


## 가산 국소 유한 기저(Countably Locally Finite Basis)

위상 공간 $(X, \mathcal{T})$의 부분 집합들의 모음 $\mathcal{B}$가 가산 국소 유한 기저(countably locally finite basis)라는 것은 $\mathcal{B}$가 $(X, \mathcal{T})$의 기저이면서 동시에 가산 국소 유한 집합족이라는 조건을 모두 만족하는 경우를 지칭합니다.

1. $\mathcal{B}$는 위상 공간 $(X, \mathcal{T})$의 기저(basis)여야 합니다. 어떤 집합족 $\mathcal{B} \subseteq \mathcal{T}$가 위상 $\mathcal{T}$의 기저가 된다는 것은 임의의 열린 집합(open set) $U \in \mathcal{T}$와 그 안의 임의의 점 $x \in U$에 대하여, $x \in B \subseteq U$를 만족하는 $B \in \mathcal{B}$가 존재해야 합니다. 이는 모든 열린 집합 $U \in \mathcal{T}$가 $\mathcal{B}$의 원소들의 합집합으로 표현될 수 있다는 것과 동치입니다. 즉, $\mathcal{B}$의 원소들은 모두 열린 집합이어야 하며, 이들을 이용하여 $X$의 모든 열린 집합을 생성할 수 있어야 합니다.

2. $\mathcal{B}$는 가산 국소 유한(countably locally finite) 집합족이어야 합니다. 집합족 $\mathcal{B}$가 가산 국소 유한이라는 것은, $\mathcal{B}$를 다음과 같이 국소 유한인 집합족 $\mathcal{B}_n$들의 가산 합집합으로 표현할 수 있다는 의미입니다.
$$
\mathcal{B} = \bigcup_{n=1}^{\infty} \mathcal{B}_n
$$
여기서 각각의 $\mathcal{B}_n$ ($n \in \mathbb{N}$)은 국소 유한(locally finite) 집합족입니다. 집합족 $\mathcal{B}_n$이 국소 유한이라는 것은, $X$ 안의 모든 점 $x \in X$에 대하여, $x$의 적절한 열린 근방(open neighborhood) $N_{x,n}$이 존재하여, 이 $N_{x,n}$과 교집합을 가지는 $\mathcal{B}_n$의 원소의 개수가 유한하다는 것을 의미합니다. 즉, 집합 $\{ B \in \mathcal{B}_n \mid N_{x,n} \cap B \neq \emptyset \}$의 원소의 개수가 유한개라는 것입니다.

여기서 중요한 점은, 각각의 $\mathcal{B}_n$이 그 자체로 $(X, \mathcal{T})$의 기저일 필요는 없다는 것입니다. 기저의 성질은 $\mathcal{B}_n$들의 합집합인 $\mathcal{B}$ 전체에 대해 요구되는 조건입니다. 즉, $\mathcal{B} = \bigcup_{n=1}^{\infty} \mathcal{B}_n$이 $(X, \mathcal{T})$의 기저가 되어야 하며, 동시에 각 구성 요소인 $\mathcal{B}_n$은 국소 유한의 성질을 만족해야 합니다. 각각의 $\mathcal{B}_n$은 단순히 열린 집합들의 모임일 수 있으며, 이들이 모여 전체 기저 $\mathcal{B}$를 형성하는 것입니다.


## 가산기저와 가산국소유한기저
가산 기저(countable basis)를 가지는 위상 공간은 항상 가산 국소 유한 기저(countably locally finite basis)를 가집니다.

이를 증명하기 위해, 위상 공간 $(X, \mathcal{T})$가 가산 기저 $\mathcal{B}$를 가진다고 가정해 보겠습니다. $\mathcal{B}$가 가산 기저이므로, 우리는 $\mathcal{B}$의 원소들을 다음과 같이 셀 수 있습니다. (단, $B_n$ ($n \in \mathbb{N}$)은 열린 집합)

$$
\mathcal{B} = \{B_1, B_2, B_3, \dots, B_n, \cdots \} 
$$

이제 우리는 $\mathcal{B}$를 국소 유한(locally finite) 집합족들의 가산 합집합으로 표현해야 합니다.
다음과 같이 각 $n \in \mathbb{N}$에 대하여 집합족 $\mathcal{B}_n$을 정의합니다.

$$
\mathcal{B}_n = {B_n} 
$$

즉, $\mathcal{B}_n$은 단 하나의 원소 $B_n$만을 가지는 집합족입니다. 그러면 $\mathcal{B}$는 이 $\mathcal{B}n$들의 가산 합집합으로 표현될 수 있습니다.

$$
\mathcal{B}  = \bigcup_{n=1}^{\infty} \mathcal{B}_n
$$

$\mathcal{B}_n$은 단 하나의 원소 $B_n$만을 가지고 있으므로 임의의 열린 근방 $N_x$에 대하여, $N_x$와 교집합을 가지는 $\mathcal{B}_n$의 원소는 $B_n$이거나($N_x \cap B_n \neq \emptyset$), 혹은 없을 수도($N_x \cap B_n = \emptyset$)있습니다. 어느 경우든, $N_x$와 교집합을 가지는 $\mathcal{B}_n$의 원소의 개수는 유한하므로, $\mathcal{B}$는 가산 국소 유한 기저의 정의를 만족합니다.