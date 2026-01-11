---
title: "외부 공간: 간격을 잇다"
date: 2006-09-01
tags:
  - Bridge
  - Clifton
  - 다리
  - Suspension
  - Ponte
  - Luz
  - 케이블
  - Gate
---

> [!NOTE]
> https://plus.maths.org/content/outer-space-bridging-gap
>
> 긴장감을 유지하는 방법

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/issue40/outerspace/icon.jpg?itok=KdHTmEVo)

*돌아가기:*

[Constructing our lives package](https://plus.maths.org/content/ingenious-constructing-our-lives)

![The Golden Gate Bridge](https://plus.maths.org/issue40/outerspace/Golden_Gate.jpg)

캘리포니아의 Golden Gate Bridge

인류의 위대한 공학적 성취 중 하나는 강과 협곡을 가로지르는 거대한 다리를 건설하여 원래는 통과할 수 없었던 장애물을 극복한 것입니다. 이러한 방대한 건설 프로젝트는 종종 미적 품질을 지니고 있어 현대 세계 불가사의 중 최고 수준에 속합니다. 우아한 [Golden Gate Bridge](http://www.goldengatebridge.org/), Brunel의 놀라운 [Clifton Suspension Bridge](http://www.clifton-suspension-bridge.org.uk/index.php), 또는 브라질의 [Ponte Hercilio Luz](http://en.structurae.de/structures/data/index.cfm?ID=s0000939)는 부드럽고 유사해 보이는 멋진 형태를 가지고 있습니다. 그런데 이 형태는 정확히 무엇일까요?

많은 수학자들은 처음에 이러한 다리들이 [현수선(catenary)](http://www-groups.dcs.st-and.ac.uk/~history/Curves/Catenary.html) 형태를 따를 것이라고 짐작할 수 있습니다. 이 곡선은 1690년 [Jacob Bernoulli](http://www-gap.dcs.st-and.ac.uk/~history/Biographies/Bernoulli_Jacob.html)가 문제를 제시한 후, 1691년에 [Gottfried von Leibniz](http://www-gap.dcs.st-and.ac.uk/~history/Biographies/Leibniz.html), [Christiaan Huygens](http://www-gap.dcs.st-and.ac.uk/~history/Biographies/Huygens.html), [David Gregory](http://www-gap.dcs.st-and.ac.uk/~history/Biographies/Gregory_David.html), 그리고 [Johann Bernoulli](http://www-gap.dcs.st-and.ac.uk/~history/Biographies/Bernoulli_Johann.html)에 의해 각각 독립적으로 발견되었습니다.

> 현수선(catenary)은 균일한 밀도를 가진 사슬이나 케이블이 자신의 무게만으로 양 끝에서 매달렸을 때 형성되는 곡선입니다. 이 곡선은 수학적으로 쌍곡선 코사인 함수 $y = a \cosh(x/a)$로 표현됩니다. 라틴어 'catena(사슬)'에서 유래한 이 용어는 매우 중요한 물리적 의미를 지닙니다. 사슬의 각 점에서 장력은 오직 접선 방향으로만 작용하며, 각 미소 요소는 자신의 무게와 양쪽 끝의 장력이 완벽하게 균형을 이룹니다. 이는 변분법(calculus of variations)의 초기 응용 사례 중 하나로, "주어진 조건에서 위치 에너지를 최소화하는 곡선은 무엇인가?"라는 문제의 해답입니다. 17세기 말 이 문제는 수학계의 큰 관심을 끌었고, 당대 최고의 수학자들이 경쟁적으로 해를 찾았습니다.

![The Ponte Hercilio Luz in Brazil](https://plus.maths.org/issue40/outerspace/Herzilio.jpg)

브라질의 Ponte Hercilio Luz

그러나 매달린 사슬과 Clifton이나 Golden Gate 같은 현수교(suspension bridge) 사이에는 큰 차이가 있습니다. 현수교는 두 점에서 매달린 단일 사슬의 무게만을 지탱하는 것이 아닙니다. 현수교 케이블이 지탱해야 하는 무게의 대부분은 다리의 평평한 바닥판(deck) 자체의 무게입니다. 만약 바닥판이 수평이고, 전체 길이에 걸쳐 밀도와 단면적이 일정하다면, 다리의 단위 길이당 무게는 상수가 됩니다. 각 구간의 무게는 그 위의 케이블 장력에 의해 지탱됩니다. 

> 여기서 핵심적인 물리적 차이를 이해해야 합니다. 현수선의 경우 사슬 자체의 무게만이 작용하므로, 아래로 갈수록 누적되는 무게는 사슬의 호의 길이에 비례합니다. 반면 현수교의 경우 바닥판이 수평으로 균일하게 분포되어 있으므로, 케이블이 지탱해야 하는 무게는 수평 거리 $x$에 정확히 비례합니다. 이 차이가 곡선의 형태를 현수선에서 포물선으로 바꾸는 결정적 요인입니다. 또한 실제 현수교 설계에서 바닥판의 무게는 케이블 자체 무게의 수십 배에 달하므로, 케이블의 형태는 포물선에 매우 가까워집니다.

지지하는 다리 케이블의 형태가 최저점이 원점에 있는 어떤 곡선 $y(x)$라고 가정해봅시다. 여기서 $x = 0$이고 $y = 0$인 지점은 다리 중앙에 위치합니다. 이 곡선의 형태는 무엇일까요?

케이블의 임의의 점에서 기울기는 그 아래 있는 무게(단위 길이당 무게 곱하기 $x$와 같음)를 지지하는 케이블의 장력으로 나눈 비율로 주어집니다. 그런데 이 기울기는 도함수 $\frac{dy}{dx}$와도 같습니다. 따라서 두 식을 같다고 놓고 $x$에 대해 $dx$로 적분하면, 최저점이 $x = 0$, $y = 0$에 위치한 포물선의 방정식을 얻습니다. 현수 케이블의 형태 방정식은 $y = \frac{x^{2}}{2B}$인 포물선이 됩니다. 여기서 $B$는 장력을 다리 바닥판의 단위 길이당 무게로 나눈 값과 같은 상수입니다(자세한 유도 과정을 스스로 채워보세요).

> 이 유도를 좀 더 자세히 살펴봅시다. 케이블의 한 점 $(x, y)$를 생각해보면, 이 점에서 케이블에 작용하는 수평 장력을 $T$라 하고, 단위 길이당 바닥판의 무게를 $w$라 하겠습니다. 중앙에서 수평 거리 $x$만큼 떨어진 점까지의 바닥판이 케이블에 가하는 총 무게는 $wx$입니다. 이 점에서 케이블의 기울기는 수직 방향 힘과 수평 방향 힘의 비율이므로 $\frac{dy}{dx} = \frac{wx}{T}$입니다. 양변을 적분하면 $y = \frac{wx^{2}}{2T} + C$이고, 최저점 $(0, 0)$을 지나므로 $C = 0$입니다. 따라서 $y = \frac{x^{2}}{2B}$, 여기서 $B = \frac{T}{w}$입니다. 이 상수 $B$는 장력과 단위 무게의 비율로, 물리적으로는 케이블이 얼마나 '팽팽한지'를 나타내는 척도입니다. $B$가 클수록 케이블은 더 팽팽하고 곡선은 더 완만해집니다.

다음은 홍콩의 아름다운 포물선 형태의 Tsing Ma 현수교 사진입니다. 세계에서 여섯 번째로 큰 이 다리는 1377미터에 걸쳐 있고 높이는 206미터입니다. 따라서 이 다리의 방정식은 $y = \frac{x^{2}}{2301.13 \text{ m}}$입니다. 왜냐하면 이 다리의 양 끝점은 $x = 688.5\text{m}$, $y = 206\text{m}$와 $x = -688.5\text{m}$, $y = 206\text{m}$를 지나고, 좌표의 원점은 케이블의 최저점에 위치하기 때문입니다.

> 이 방정식을 어떻게 구했는지 확인해봅시다. 포물선 $y = \frac{x^{2}}{2B}$가 점 $(688.5, 206)$을 지나므로, $206 = \frac{(688.5)^{2}}{2B}$입니다. 이를 풀면 $2B = \frac{(688.5)^{2}}{206} = \frac{474,032.25}{206} \approx 2301.13$미터입니다. 이 값은 다리의 물리적 특성(케이블 장력과 바닥판의 단위 무게 비율)을 담고 있습니다. 흥미롭게도 경간(span)이 1377m이고 처짐(sag)이 206m인 경우, 케이블의 최대 각도는 양 끝에서 약 $\arctan\left(\frac{688.5}{2301.13}\right) \approx 16.6°$입니다. 실제 현수교 설계에서는 이 각도가 너무 크면 케이블에 가해지는 장력이 지나치게 커지므로, 적절한 처짐을 선택하는 것이 중요합니다.

![The Tsing Ma suspension bridge in Hong Kong](https://plus.maths.org/issue40/outerspace/Hong_Kong.jpg)

홍콩의 Tsing Ma Suspension Bridge

영국에서 19세기의 가장 주목할 만한 공학적 업적 중 하나는 1829년 [Isambard Kingdom Brunel](http://www.brunel200.com/brunel_biography.htm)이 설계한 브리스톨의 [Clifton Suspension Bridge](http://www.clifton-suspension-bridge.org.uk/index.php)입니다. 이 다리는 그가 사망한 지 3년 후인 1865년에야 완공되었습니다. 이 다리는 214미터에 걸쳐 있고 높이는 21.3미터입니다. 이 다리의 방정식을 구할 수 있나요?

> 같은 방법을 적용해봅시다. 경간이 214m이므로 중심에서 양 끝까지의 거리는 107m입니다. 포물선 $y = \frac{x^{2}}{2B}$가 점 $(107, 21.3)$을 지나므로, $21.3 = \frac{(107)^{2}}{2B}$입니다. 따라서 $2B = \frac{11,449}{21.3} \approx 537.6$미터이고, 방정식은 $y = \frac{x^{2}}{537.6 \text{ m}}$가 됩니다. Tsing Ma 다리와 비교하면, Clifton 다리는 훨씬 짧은 경간에 대해 상대적으로 큰 처짐을 가지고 있습니다. 이는 19세기 중반의 건설 기술과 재료의 한계를 반영합니다. Brunel은 체인 링크(chain link) 방식을 사용했는데, 이는 현대의 강철 케이블보다 유연성이 떨어지고 무거웠습니다. 그럼에도 불구하고 이 다리는 완공 후 150년이 넘도록 여전히 사용되고 있으며, Victorian 시대 공학의 걸작으로 평가받고 있습니다.

![The Clifton suspension bridge in Bristol](https://plus.maths.org/issue40/outerspace/clifton.jpg)

브리스톨의 Clifton Suspension Bridge

[Outer space: Superficiality?](https://plus.maths.org/issue39/outerspace/index.html)에서 제시된 퍼즐을 풀어보셨나요? 그렇지 않다면

[여기서 답을 찾을 수 있습니다](https://plus.maths.org/issue40/outerspace/solution-gifd.html)!