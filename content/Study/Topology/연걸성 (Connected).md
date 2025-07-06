### $\operatorname{Int}A$ 와 $\partial A$ 가 각각 connected일 때, $A$ 는 connected이다.

$A$ 의 내부 $\operatorname{Int}A$ 와 경계 $\partial A$ 가 둘 다 연결되어 있다면 $A$ 도 연결.

우선 용어를 다시 정확히 정의합니다.  
- $\operatorname{Int}A$ 는 $A$ 의 내부, 즉 $X$ 의 open set 중 $A$ 에 포함된 것들의 합집합입니다.  
- $\partial A$ 는 $A$ 의 경계, 즉 $\overline{A}\setminus \operatorname{Int}A$ 입니다. 여기서 $\overline{A}$ 는 $A$ 의 closure 입니다.  
- 한 공간이 connected(연결) 이라는 것은, 그 공간을 서로소이면서 nonempty한 두 개의 open set의 합으로 나눌 수 없다는 뜻입니다.

류법을 사용하여, $A$ 가 연결되지 않았다고 가정하고 모순을 도출하겠습니다.

$A$ 가 연결되지 않았다고 가정하겠습니다. 그러면 $A$ 는 서로소인 두 nonempty한 부분집합 $C$ 와 $D$ 의 합으로 나뉠 수 있습니다. 이때  
- $C,D\subset A$,  
- $C\cap D = \varnothing$,  
- $C,D$ 는 $A$ 의 상대위상에서 모두 open이고 closed 입니다,  
- 즉 $A = C \cup D$ 입니다.

이제 $\operatorname{Int}A$ 가 연결이라는 가정을 사용하겠습니다. $\operatorname{Int}A$ 는 $A$ 의 내부이므로 $C$ 와 $D$ 로 나눌 수밖에 없습니다. 즉, $\operatorname{Int}A = (\operatorname{Int}A \cap C) \cup (\operatorname{Int}A \cap D)$ 입니다. 그런데 $C,D$ 는 $A$ 에서 서로소이고 closed $\cap$ open 이므로, 이 두 교집합은 $\operatorname{Int}A$ 의 서로소 closed $\cap$ open 집합입니다.

$\operatorname{Int}A$ 가 connected 라는 가정에 따라 이 둘 중 하나는 공집합이어야 합니다. 일반성을 잃지 않고 $\operatorname{Int}A\subset C$ 라고 두겠습니다. 즉 $\operatorname{Int}A \cap D = \varnothing$ 입니다.

이제 $D$ 는 $A$ 에 포함된 집합으로서 $\operatorname{Int}A$ 와 겹치지 않습니다. 하지만 $D$ 는 비어있지 않으므로 적어도 하나의 점을 포함합니다. 이 점들은 $A$ 의 내부에 속하지 않으므로 $A$ 의 경계 위에 있어야 합니다. 정확히 말해 $D\subset A\setminus \operatorname{Int}A\subset \overline{A}\setminus \operatorname{Int}A = \partial A$ 가 됩니다.

즉 $D\subset \partial A$ 입니다.

$D$ 가 $A$ 에서 open 이고 $D \subset \partial A$ 이면, $D$ 는 $\partial A$ 에서 open 입니다. 왜냐하면, $D = A \cap V$ 로 $V$ 가 $X$ 에서 open 이면 $\partial A \cap V$ 는 $\partial A$ 에서 open 이고, $D = \partial A \cap V$ 이므로 $\partial A$ 에서 open 입니다. 

따라서 $D$ 는 $\partial A$ 안에서 open $\cap$ closed 입니다. $D$ 와 $\partial A \setminus D$ 는 서로소 closed $\cap$ open 집합이며 합하면 $\partial A$ 가 됩니다. 그리고 $D$ 는 비어 있지 않습니다.

이는 $\partial A$ 가 connected 라는 가정과 모순됩니다. 왜냐하면 connected 공간은 nontrivial 한 open $\cap$ closed 분해를 가질 수 없습니다.

### The long line is path connected and locally homeomorphic to $\mathbb{R}$, but it cannot be imbedded in $\mathbb{R}$.

long line이란, $S_\Omega \times [0,1)$ 의 dictionary order 로 정의된 순서공간입니다. 단, $S_\Omega$ 에서 최소원소을 제외한 나머지 원소들은 잘 정렬된 집합입니다.

(a)  어떤 순서집합 $X$ 안에서 $a < b < c$ 일 때, $[a, c)$ 이 $[0,1)$ 과 동형이려면 $[a,b]$, $[b,c]$ 도 $[0,1]$ 과 동형이 되어야 한다는 것을 보이시오.  

핵심 아이디어:  
순서동형의 핵심은 순서와 위상이 모두 보존된다는 점입니다.  
$[a,c]$ 가 $[0,1]$ 과 동형이면, 그 안의 임의의 중간점 $b$ 를 잡았을 때 양쪽 절반도 역시 $[0,1]$ 의 부분구간과 같은 구조여야 합니다.  
즉 $[a,b]$, $[b,c]$ 가 $[0,1]$ 과 위상적으로 동형이 아니면 $[a,c]$ 전체도 그럴 수 없습니다.

(b)  
질문: $x_0 < x_1 < \dots$ 는 $X$ 안의 증가수열이고, 극한 $b = \sup \{x_i\}$ 를 가정할 때, $[x_0,b]$ 가 $[0,1]$ 과 동형이려면 각 구간 $[x_i, x_{i+1}]$ 이 $[0,1]$ 과 동형이어야 함을 보이시오.  
핵심 아이디어:  
작은 조각들이 전부 $[0,1]$ 과 같다면, countable many 조각들의 union 이므로 전체도 그런 성질을 유지할 수 있습니다.  
반대로 전체 구간이 $[0,1]$ 과 동형이라면, 중간의 유한 조각도 반드시 그 구조를 가져야 합니다.  
$\Rightarrow$ 전체의 동형성을 조각별로 쪼개는 조건으로 연결합니다.

(c)  
질문: $S_\Omega$ 의 원소 $a$ 에 대해, $[a_0 \times 0, a \times 0]$ 이 $[0,1]$ 과 동형임을 귀한 유도(transfinite induction)로 보이시오.  
핵심 아이디어:  
이건 long line $S_\Omega \times [0,1)$ 이 어떻게 순서정렬되는지를 보여주는 기초입니다.  
$S_\Omega$ 는 최소 비가산 잘 정렬 집합이므로, transfinite induction 을 사용할 수 있습니다.  
- successor ordinal 일 경우엔 이전 점에서 조각을 붙이듯 진행합니다.  
- limit ordinal 이면 점렬극한이 존재하는 경우처럼 처리합니다.  
조각들이 전부 $[0,1]$ 과 같다면 전체도 쌓아서 만들어짐을 유도할 수 있습니다.

(d)  
질문: $L$ 이 path connected 임을 보여라.  
핵심 아이디어:  
$L$ 은 직관적으로 보면 매우 긴 선분처럼 생긴 순서공간입니다.  
시작점에서부터 임의의 점까지 "좌표 증가"를 따라 계속 올라가는 경로를 만들 수 있습니다.  
즉, $L$ 의 각 점은 그 앞에 countable 혹은 uncountable 한 길이가 있으며, 그 길이만큼 점차 증가하면서 이어지는 path 를 만들 수 있습니다.  
순서공간에서의 경로 연결성은 이러한 점들의 "이동 경로"로 구현됩니다.

(e)  
질문: $L$ 의 임의의 점은 $\mathbb{R}$ 의 열린구간과 위상동형인 neighborhood 를 갖는다는 것을 보여라.  
핵심 아이디어:  
$L = S_\Omega \times [0,1)$ 의 dictionary order 는 각 점에서 로컬로 보면 $\mathbb{R}$ 의 간격처럼 보입니다.  
즉 각 점은 이전 점들과 연속적으로 연결되어 있으며, 주변을 확대해 보면 $\mathbb{R}$ 의 간격처럼 보입니다.  
이로 인해 $L$ 은 locally Euclidean 하며, local homeomorphism 으로 $\mathbb{R}$ 의 간격과 같다고 말할 수 있습니다.

(f)  
질문: $L$ 은 $\mathbb{R}$ 안에 (또는 $\mathbb{R}^n$ 안에도) homeomorphic 하게 매장될 수 없음을 보이시오.  
힌트: $\mathbb{R}^n$ 의 부분공간은 countable 한 basis 를 가져야 함.  
핵심 아이디어:  
$L$ 은 uncountable 한 구조를 갖고 있으며, $\sigma$-compact 하지 않고, first countable 도 아닙니다.  
반면, $\mathbb{R}^n$ 의 부분공간은 항상 countable basis (즉, second countable) 를 갖습니다.  
따라서 $L$ 이 그 안에 homeomorphic 하게 들어갈 수 없습니다.  
이는 일반적인 위상적 embedding 조건에서 자주 사용하는 대조적 특징입니다.

## Long line에 대한 질문
1. 시각적으로 어떻게 이해하는게 좋을까?

Long line $L$ 은 일반적인 실수 직선 $\mathbb{R}$ 과 로컬(topologically locally) 로는 같지만, 글로벌(global) 하게는 훨씬 더 깁니다. $\mathbb{R}$ 의 길이를 넘는, 비가산한 "길이"를 갖는 선분처럼 생각하면 좋습니다.

이를 시각화하려면 다음과 같이 생각할 수 있습니다:

- 먼저 $\mathbb{R}$ 은 countable 한 많은 간격들로 덮일 수 있습니다.
- 반면 $S_\Omega$ 는 uncountable 하게 긴 정렬된 집합이고, 여기에 $[0,1)$ 를 곱해서 각 $\alpha \in S_\Omega$ 에 길이 1 인 작은 열린 간격을 붙인다고 생각하면,
- $L = S_\Omega \times [0,1)$ 는 $\omega_1$ 개의 간격을 이어붙인 긴 줄입니다.
- 순서가 $(\alpha,x) < (\beta,y)$ iff $\alpha < \beta$, 또는 $\alpha = \beta$ 이고 $x < y$ 라는 dictionary order 로 정해져 있으므로,
- 각 $\alpha$ 에 $[0,1)$ 을 붙인 것을 좌에서 우로, 하나씩 순서대로 이어붙인 구조라고 생각하면 됩니다.
- 이 선은 로컬로 보면 늘 $\mathbb{R}$ 과 같지만, 그 길이는 $\mathbb{R}$ 로는 닿을 수 없을 만큼 깁니다.

그래픽 상상법:
- 가산히 많은 간격을 이어붙인 건 $\mathbb{R}$ 처럼 보이지만,
- 비가산히 많은 간격을 이어붙인 건 무한히 더 긴 선입니다.
- 하지만 이 "선"은 어디에도 꼬이거나 접히거나 하지 않으며, 순서대로 한 방향으로만 쭉 이어집니다.

2. 최소원소를 제외한 이유가 뭘까?

$L$ 을 정의할 때 가장 작은 원소 $(0,0)$ 을 제외하는 이유는 다음 두 가지 관점에서 이해할 수 있습니다.

(1) 로컬 위상 성질 유지:  
$(0,0)$ 은 $L$ 에서 유일하게 left neighborhood 가 존재하지 않는 점입니다.  
즉, $(0,0)$ 은 가장 왼쪽에 고립된 점이므로, 이 점만 다른 점들과 달리 $\mathbb{R}$ 과 위상동형인 열린 근방을 가질 수 없습니다.  
그래서 $L$ 이 모든 점에서 $\mathbb{R}$ 과 locally homeomorphic 하다는 성질을 가지려면 $(0,0)$ 을 제외해야 합니다.

(2) 기술적 단순화 및 통일성:  
이 점 하나가 특이점(singular point)이기 때문에 $L$ 을 path connected 하거나 위상동형성 판단 등을 논의할 때 걸림돌이 됩니다.  
따라서 위상적 성질을 보다 명확하게 논의하고 싶을 때, 보통 이 점을 제거한 버전을 다룹니다.

3. long line이란 표현을 쓴 이유는 무엇일까?

“Long line” 이라는 명칭은 수학적으로도, 직관적으로도 다음과 같은 이유에서 적절합니다.

(1) 긴 직선처럼 생긴 위상공간:  
- $L$ 은 실수직선 $\mathbb{R}$ 과 로컬 구조가 똑같고,  
- 모든 점이 직선처럼 양옆으로 열린 간격을 가지며,  
- 연결되고, 심지어 path-connected 하기도 합니다.  
즉, 진짜 “선(line)” 입니다.

(2) 하지만 훨씬 길다:  
- $\mathbb{R}$ 은 countable 한 개의 $[0,1)$ 로 덮을 수 있지만,  
- $L$ 은 uncountable 개의 $[0,1)$ 를 이어붙인 것이므로 $\mathbb{R}$ 보다 훨씬 긴 공간입니다.  
- 심지어 $\mathbb{R}$ 에는 embedding 할 수도 없습니다.

(3) 끝없는 오른쪽 방향:  
- $L$ 은 순서가 정의되어 있으며 맨 왼쪽에서 시작하여 끝없이 오른쪽으로 이어지는 한 줄의 구조입니다.  
- 하지만 단순한 실수 직선이 아니라, $\omega_1$ 개의 간격을 가지는 무한히 긴 선이라는 점에서 “long” 입니다.

요약하면,  
> “long line” 은 로컬로는 $\mathbb{R}$ 같고, 전역적으로는 훨씬 더 길어서 실수공간에 들어갈 수 없는, 직관적이면서도 위상적으로 특별한 “직선”입니다.


## 국소 연결(locally connected)

$X$가 국소연결이려면, 임의의 점 $x\in X$와 그 점의 임의의 근방 $N$에 대해, “$x$를 포함하는 연결 열린집합이 $N$ 안에 있다”가 성립해야 합니다.

  “$X$가 국소연결이다”  
  $\Longleftrightarrow$  
  “$X$의 모든 열린집합 $U\subset X$에 대해, $U$의 각 연결성분 $C\subset U$가 다시 $X$에서 열린집합이다.”

정리하자면, **$U$의 성분**이란 **$U$ 안에서 더 이상 커질 수 없는 최대 연결 부분집합**을 말합니다. 국소연결이기 위해서는, 임의의 열린 $U\subset X$를 이 성분들로 나눌 때, 그 나눠진 각 덩어리(성분) 역시 $X$에서 열린이어야 한다는 것이 필요·충분조건입니다.

### 성분(connected component)

위상 공간 $(X,\tau)$에서 연결 집합이란, 두 개의 서로 다른(비어 있지 않으면서) 열린집합으로 나눌 수 없는 집합을 말합니다.

$U\subset X$가 임의의 부분집합일 때, $U$의 성분이란 $U$ 안에서 더 이상 커질 수 없는(maximal) 연결 부분집합을 뜻합니다.

구체적으로, $x\in U$를 택하면

$$
    C_x \;=\;\bigcup\{\;A\subset U\mid A\text{는 연결이고 }x\in A\}
  $$

로 두면, $C_x$는 $x$를 포함하는 최대 연결 부분집합—즉 $U$의 하나의 성분—이 됩니다. $U$의 각 성분들은 서로소(공통점이 없고)이며, 그 합집합이 $U$를 이루므로 $\{C_x:x\in U\}$가 $U$의 분할(partition) 을 이룹니다.


어떤 성분 $C\subset U$는 항상 $U$ 안에서는 닫힌집합(closed in $U$)입니다. 왜냐하면, **최대 연결집합**이라는 성질로 인해, $U\setminus C$가 열린이기 때문입니다. 

그러나 열린집합(open in $U$)인지 여부는 일반 위상공간에서 자동으로 성립하지 않습니다. 특히 $U$가 $X$에서 열린이라고 해도,  

$$C\text{가 }U\text{에서 열린} \; \nRightarrow \; C\text{가 }X\text{에서 열린}$$

은 “$X$가 국소연결이다”라는 추가 가정이 있을 때만 보장됩니다. 따라서 국소연결이 아닐 경우, $C$는 $X$에서 닫힌집합이지만 $U$에서는 열린집합이 아닐 수 있습니다.