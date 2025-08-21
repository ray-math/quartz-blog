---
tags:
  - 기하
description:
---
랭글리 삼각형 문제는 삼각형에서 주어진 각도들로부터 다른 각도를 추론하는 문제로, 1922년 에드워드 맨 랭글리(Edward Mann Langley)에 의해 'The Mathematical Gazette'에 처음 제시된 문제 입니다.

주어진 몇 개의 각도만을 이용해 미지의 각을 구하는 고전적인 기하학 문제이지요.

### 문제 정의

![[Langley's Adventitious Angles 2.svg|300]]
이 문제를 차근차근 살펴보겠습니다.

- 삼각형 $ABC$는 이등변삼각형이며, $\angle B = \angle C = 80^\circ$ 입니다.
- 점 $F$는 변 $AB$위의 점으로 $\angle ACF=30^\circ$입니다.
- 점 $E$는 변 $AC$위의 점으로 $\angle ABE=20^\circ$입니다.

이 때, $\angle FEB$는 얼마일까요?

얼핏보면 몇 개의 보조선을 그려 풀 수 있을 것 같습니다. 하지만, 실제로 풀어보려하면 꽤나 어렵습니다. 여러가지 풀이가 있지만 가장 일반적으로 알려진 풀이를 같이 보도록 하겠습니다.

![[Langley 1.svg|500]]
먼저 문제를 정의하고 나면, $\angle A$는 $\angle B$와 $\angle C$를 정의하는데 이외에는 쓰이지 않으므로, 점 $A$를 제외하고 사각형 $FBCE$와 그 주변에 집중해서 문제를 바라보겠습니다.

### 1단계: 기본 각도 계산
우선 주어진 정보로부터 알 수 있는 기본적인 각도들을 모두 계산해보겠습니다.

점 $E$, $F$로 인해 나뉘는 각도를 보면

$$
\begin{align*}
\angle EBC = \angle ABC - \angle ABE = 80^\circ - 20^\circ = 60^\circ \\
\angle FCB = \angle ACB - \angle ACF = 80^\circ - 30^\circ = 50^\circ
\end{align*}
$$

이 됩니다. 

여기서 삼각형 $BFC$의 내각의 합은 $180^\circ$ 이므로, $\angle BFC$는

$$
\begin{align*}
\angle BFC &= 180^\circ - \angle FBC - \angle FCB\\
 &= 180^\circ - 80^\circ - 50^\circ = 50^\circ
\end{align*}
$$

이 됩니다.

따라서 $\angle BFC = \angle FCB = 50^\circ$ 이므로, 삼각형 $BFC$는 이등변삼각형이 됩니다. 이등변 삼각형의 성질에 의해 마주보는 두 변의 길이가 같으므로

$$
\overline{BF} = \overline{BC}
$$

입니다.

![[Langley 2.svg|500]]
### 2단계: 보조선 그리기

변 $EC$ 위에 점 $G$를 $\angle CBG = 20^\circ$ 가 되도록 잡아보겠습니다.[^1] (why?)

$\angle GCB = 80^\circ$ 이고, 작도에 의해 $\angle CBG = 20^\circ$ 이므로

$$
\begin{align*}
\angle BGC &= 180^\circ - \angle GCB - \angle CBG \\
&= 180^\circ - 80^\circ - 20^\circ = 80^\circ
\end{align*}
$$

이 됩니다.

따라서 $\angle GCB = \angle BGC = 80^\circ$ 이므로, 삼각형 $GBC$ 또한 이등변삼각형이 됩니다. 이등변 삼각형의 성질에 의해 마주보는 두 변의 길이는 같으므로

$$
\overline{BC} = \overline{BG}
$$

입니다.

![[Langley 3.svg|500]]


### 3단계: 정삼각형 그리기

앞선 과정에서 증명된 변의 관계를 이용해 정삼각형을 찾아보겠습니다. 

먼저 $\overline{BF} = \overline{BC}$ 이고, $\overline{BC} = \overline{BG}$ 이므로 $\overline{BF} = \overline{BG}$ 입니다. 그러므로 삼각형 $FBG$는 이등변삼각형이고, 이 삼각형의 꼭지각
 
$$
\begin{align*}
\angle FBG &= \angle ABC - \angle CBG\\
&= 80^\circ - 20^\circ = 60^\circ
\end{align*}
$$

이므로, 삼각형 $FBG$는 정삼각형이 됩니다. 따라서, 

$$
\begin{gather*}
\overline{BF} = \overline{BG} = \overline{FG} \\
\angle FBG = \angle BFG = \angle BGF = 60^\circ
\end{gather*}
$$

입니다.

![[Langley 4.svg|500]]
### 4단계: 같은 길이 찾기

이제 점 $E$를 포함하는 삼각형들을 분석하여 마지막 단서들을 찾아보겠습니다.

점 $G$는 선분 $AC$ 위에 있으므로, 

$$
\begin{align*}
\angle BGE &= 180^\circ - \angle BGC\\
&= 180^\circ - 80^\circ = 100^\circ
\end{align*}
$$

이고,

$$
\begin{align*}
\angle GBE &= \angle ABG - \angle ABE\\
&= (80^\circ - 20^\circ) - 20^\circ\\
&= 60^\circ - 20^\circ = 40^\circ
\end{align*}
$$

입니다. 삼각형 $BGE$의 내각의 합을 이용하여

$$
\begin{align*}
\angle GEB &= 180^\circ - \angle BGE - \angle GBE \\
&= 180^\circ - 100^\circ - 40^\circ = 40^\circ
\end{align*}
$$

라고 계산할 수 있습니다. 따라서 삼각형 $BGE$는 이등변삼각형이 됩니다. 이등변 삼각형의 성질에 의해 마주보는 두 변의 길이는 같으므로

$$
\overline{GB} = \overline{GE}
$$
입니다.

![[Langley 5.svg|500]]
### 5단계: 최종 계산

지금까지 알아낸 모든 변의 관계를 종합하여 마지막 이등변삼각형을 찾고 답을 구해보겠습니다.

삼각형 $\triangle FGE$는 이등변 삼각형이므로, 두 밑각의 크기는 같습니다. 따라서

$$
\begin{align*}
\angle GEF &= \angle GFE \\
&= (180^\circ - 40^\circ) \div 2\\
&= 70^\circ
\end{align*}
$$

이고, 우리가 구하고자 하는 $\angle BEF$는 $\angle GEB$에서 $\angle GEF$를 뺀 값이므로,

$$
\begin{align*}
x &= \angle GEF - \angle GEB\\
&= 70^\circ - 40^\circ = 30^\circ
\end{align*}
$$

입니다.

![[Langley 6.svg|500]]
이 문제의 가장 큰 매력은 고급 수학 지식이나 복잡한 공식 없이, 오직 중학교 수준의 기하학 지식과 순수한 논리력만으로 풀어낼 수 있다는 점입니다. 모든 단서는 문제 안에 있고, 해답으로 가는 길은 정해져 있지요. 여러분들이 해결한 다른 풀이가 있다면 댓글로 알려주시기 바랍니다.

[^1]: 풀이 초반에 $\triangle BFC$가 이등변삼각형이라서 $BF = BC$라는 아주 중요한 사실을 알아냈습니다. 이제 이 정보를 활용해 다음 단계로 넘어가야 합니다. 같은 길이의 변을 만드는 가장 확실한 방법은 이등변삼각형 이나 정삼각형을 만드는 것입니다. 어떤 각도로 선을 그어야 이등변삼각형이 만들어질까요? 이때 문제에 주어진 숫자들이 단서가 됩니다. 결론적으로, '20도를 만들어야겠다'는 생각은 뜬구름 잡는 이야기가 아니라, 정보를 연결하기 위해 '같은 길이의 변'이 필요하다는 목표를 세우고, 같은 길이를 만들기 위해 '이등변삼각형'이라는 도구를 선택한 뒤, 문제에 주어진 '20도'라는 단서를 재활용해 가설을 세우고 검증하는, 논리적인 추론 과정의 결과입니다. 