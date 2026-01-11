---
title: 오일러의 다면체 공식
date: 2016-08-05
tags:
  - 다면체
  - 공식
  - 수학
  - 필사본
  - 오일러
  - polyhedron
  - 입체
  - dual
---

> [!NOTE]
> https://plus.maths.org/content/eulers-polyhedron-formula-2
>
> 3차원 도형에 관한 이 놀라운 결과는 공간의 본질에 대해 깊은 통찰을 제공한다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/abstractpics/%5Buid%5D/%5Bsite-date%5D/polyhedron_icon.png?itok=bHYU1ZDN)

*이 글은 Five of Euler's best 시리즈의 일부입니다. 2016년 유럽 수학 학회에서 수학자 Günter M. Ziegler가 발표한 강연을 바탕으로 한 이 시리즈의 다른 네 가지 문제를 읽으려면 여기를 클릭하세요.*

삼각형을 떠올려보자. 이제 사각형, 오각형, 육각형 등을 차례로 생각해보자. 이러한 도형들을 *다각형(polygon)*이라 부른다. "poly"는 그리스어로 "많은"을 의미하고 "gon"은 그리스어로 "각"을 의미한다.

이제 차원을 하나 올려보자. 정육면체, 피라미드, 혹은 정팔면체를 생각해보자. 이들은 모두 *다면체(polyhedra)*이다("hedra"는 그리스어로 "밑면"을 의미한다). 다면체는 여러 개의 평평한 다각형 *면(face)*으로 이루어진 입체도형이다. 면의 변을 *모서리(edge)*라 하고, 다면체의 꼭짓점을 *꼭짓점(vertex)*이라 한다.

> 다면체는 우리가 일상에서 접하는 대부분의 3차원 입체도형을 포괄하는 개념이다. 핵심은 "평평한 다각형 면들로 이루어져 있다"는 점이다. 예를 들어 구(sphere)는 표면이 곡면이므로 다면체가 아니다. 반면 각뿔, 각기둥, 플라톤 입체 등은 모두 다면체에 속한다. 수학적으로 엄밀하게는 다면체를 "유한 개의 평면 다각형으로 둘러싸인 3차원 공간의 유계 영역"으로 정의한다. 이 정의가 중요한 이유는, 단순히 "보기 좋은 입체도형"을 넘어서 위상수학적 성질을 논할 수 있는 수학적 대상으로 다면체를 확립하기 때문이다.

![플라톤 입체](https://plus.maths.org/issue43/features/kirk/Solids.jpg)

플라톤 입체는 다면체의 대표적인 예이다. 왼쪽부터 네 개의 면을 가진 정사면체, 여섯 개의 면을 가진 정육면체, 여덟 개의 면을 가진 정팔면체, 열두 개의 면을 가진 정십이면체, 스무 개의 면을 가진 정이십면체이다.

> 플라톤 입체(Platonic solids)는 수학사에서 특별한 위치를 차지한다. 고대 그리스 시대부터 알려진 이 다섯 개의 정다면체는 모든 면이 합동인 정다각형이고, 각 꼭짓점에 모이는 면의 개수가 같다는 놀라운 대칭성을 지닌다. 플라톤은 『티마이오스』에서 이 다섯 입체를 우주를 구성하는 네 원소(불, 공기, 물, 흙)와 우주 전체에 대응시켰다. 정사면체는 불, 정팔면체는 공기, 정이십면체는 물, 정육면체는 흙, 정십이면체는 우주 전체를 상징했다. 수학적으로 흥미로운 사실은, 정다면체가 정확히 다섯 개만 존재한다는 점이다. 이는 오일러의 다면체 공식과도 깊은 관련이 있으며, 각 꼭짓점에 모이는 면들의 내각의 합이 $360°$보다 작아야 한다는 기하학적 제약에서 비롯된다.

이제 다면체의 꼭짓점의 개수 $V$, 모서리의 개수 $E$, 면의 개수 $F$를 세어보자. 놀랍게도, 다면체가 *볼록(convex)*(튀어나온 부분이 없는)하고 내부를 관통하는 구멍이 없다면, 꼭짓점의 개수에서 모서리의 개수를 빼고 면의 개수를 더한 값,

$$
V - E + F,
$$

는 항상 2와 같다. 다면체가 정육면체든, 정팔면체든, 아래 그림의 [대능형이십이면체(great rhombicosidodecahedron)](http://mathworld.wolfram.com/GreatRhombicosidodecahedron.html)처럼 더 복잡한 형태든, 심지어 훨씬 더 불규칙한 형태라 하더라도 마찬가지이다. 이것은 정말로 놀라운 결과이다.

> 이 공식이 왜 놀라운지 생각해보자. 먼저, 이 공식은 다면체의 구체적인 형태와 무관하게 성립한다. 정육면체처럼 규칙적인 도형이든, 아무렇게나 찌그러뜨린 불규칙한 다면체든 상관없다. 둘째, $V$, $E$, $F$는 각각 독립적으로 변할 수 있는 값들인데, 이들 사이에 $V - E + F = 2$라는 고정된 관계식이 성립한다는 것 자체가 놀랍다. 셋째, 이 공식은 순수하게 조합론적(combinatorial) 성질로, 길이나 각도 같은 측정값이 전혀 들어가지 않는다. 이는 공식이 기하학을 넘어 위상수학의 영역에 속한다는 신호이다. 실제로 확인해보자. 정육면체는 $V = 8$, $E = 12$, $F = 6$이므로 $8 - 12 + 6 = 2$이다. 정사면체는 $V = 4$, $E = 6$, $F = 4$이므로 $4 - 6 + 4 = 2$이다.

![대능형이십이면체](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/Euler/polyhedron.png)

대능형이십이면체. 이미지 출처: [Wolfram Demonstrations Project](http://demonstrations.wolfram.com/PolyhedraSpheresAndCylinders/), 제작자 [Russell Towle](http://demonstrations.wolfram.com/author.html?author=Russell%20Towle), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) 라이선스 하에 재사용.

다음 식

$$
V - E + F = 2
$$

을 오일러의 다면체 공식(Euler's polyhedron formula)이라 한다. 그러나 오일러가 이 공식을 처음 발견한 것은 아니다. 그 영예는 1630년경에 이미 이에 관해 기록을 남긴 프랑스 수학자 [René Descartes](http://www-history.mcs.st-and.ac.uk/Biographies/Descartes.html)에게 돌아간다. 1650년 스웨덴에서 데카르트가 사망한 후, 그의 논문들은 프랑스로 운송되었으나, 이를 실은 배가 센 강에 침몰했다. 논문들은 강 바닥에 사흘 동안 가라앉아 있었지만, 다행히 건져 올린 후 말릴 수 있었다. 또 다른 유명한 수학자 [Gottfried Wilhelm von Leibniz](http://www-groups.dcs.st-and.ac.uk/history/Biographies/Leibniz.html)는 1675년경에 이 공식에 관한 데카르트의 노트를 필사했다. 그 후 데카르트의 원본 필사본은 완전히 사라졌고, 라이프니츠의 사본도 분실되었다가 1860년에 하노버 왕립 도서관의 한 찬장에서 누군가가 재발견했다. 수학 공식치고는 참으로 극적인 역사가 아닐 수 없다.

> 이 일화는 수학사에서 중요한 발견들이 얼마나 우연과 행운에 의존하는지를 보여준다. 데카르트의 논문이 센 강에서 영영 사라졌다면, 또는 라이프니츠가 필사본을 남기지 않았다면, 이 공식의 발견자가 데카르트라는 사실 자체가 역사 속으로 묻혔을 것이다. 더 흥미로운 점은 데카르트가 이 공식을 발견했음에도 불구하고 그 중요성을 충분히 인식하지 못했던 것으로 보인다는 사실이다. 그의 노트에는 이 공식이 간략하게만 언급되어 있었다. 반면 오일러는 이 공식을 체계적으로 연구하고 증명했으며, 더 나아가 그것이 위상수학적 본질을 담고 있다는 통찰을 제공했다. 이것이 바로 공식이 "오일러의 공식"으로 불리는 이유이다. 수학에서 누가 처음 발견했는가만큼이나 그 발견의 의미를 이해하고 발전시키는 것이 중요하다.

데카르트가 이 공식을 먼저 발견했을지 몰라도, 결정적인 통찰을 제공한 사람은 오일러였다. 다면체 공식을 볼 때, 정확한 측정값은 중요하지 않다. 다면체의 두 면이 어떤 각도로 만나는지, 또는 변의 길이가 얼마인지 알 필요가 없다. 다면체 공식은 [쾨니히스베르크의 다리](https://plus.maths.org/content/bridges-k-nigsberg) 문제가 그러하듯이 위상수학(topology)의 세계에 속한다. 이 공식은 특정한 치수를 가진 개별 대상에 관한 것이 아니라, 공간의 본질에 관한 무언가를 말해준다.

> 여기서 "위상수학의 세계에 속한다"는 말의 의미를 깊이 이해해야 한다. 위상수학은 19세기 후반에 본격적으로 발전한 분야로, "연속적 변형 하에서 보존되는 성질"을 연구한다. 다시 말해, 찢거나 붙이지 않고 늘리거나 구부리거나 비트는 등의 변형을 가해도 변하지 않는 성질을 다룬다. 오일러의 공식에서 $V - E + F$라는 값이 항상 2인 이유는, 이것이 바로 그러한 위상적 불변량(topological invariant)이기 때문이다. 정육면체를 점토로 만들어 이리저리 주물러 모양을 바꿔도, 면을 찢거나 새로운 구멍을 뚫지 않는 한 $V - E + F = 2$는 유지된다. 이 값은 현대 위상수학에서 오일러 특성수(Euler characteristic) $\chi$로 일반화되며, $\chi = V - E + F$로 정의된다. 구면(sphere)과 위상동형인 모든 다면체는 $\chi = 2$를 가지며, 토러스(torus, 도넛 모양)는 $\chi = 0$을 가진다. 이는 오일러의 통찰이 단순한 공식을 넘어 공간 자체의 구조를 분류하는 강력한 도구가 됨을 보여준다.

다면체 공식을 증명하는 것은 사실 그다지 어렵지 않다. [Plus의 이 글](https://plus.maths.org/content/eulers-polyhedron-formula)에서 증명을 읽을 수 있고, [Geometry Junkyard](https://www.ics.uci.edu/~eppstein/junkyard/euler/)에서는 총 스무 가지의 서로 다른 증명을 찾아볼 수 있다.

> 하나의 수학 정리에 대해 스무 가지가 넘는 증명이 존재한다는 사실은 무엇을 의미할까? 이는 그 정리가 수학의 여러 분야와 깊이 연결되어 있음을 시사한다. 오일러의 다면체 공식은 조합론, 그래프 이론, 위상수학, 심지어 선형대수학의 관점에서도 증명할 수 있다. 가장 직관적인 증명 중 하나는 "다면체를 평면에 투영하는 방법"이다. 다면체에서 한 면을 제거하고 나머지를 평면 위에 펼쳐 그래프로 만든 후, 변을 하나씩 제거하면서 $V - E + F$가 불변임을 보이는 것이다. 또 다른 증명은 다면체의 쌍대성(duality)을 이용한다. 각 면의 중심에 꼭짓점을 놓고, 인접한 면들을 연결하면 쌍대 다면체(dual polyhedron)를 얻는데, 원래 다면체에서 $V$와 $F$가 바뀔 뿐 $V - E + F$는 동일하다. 이처럼 여러 증명을 통해 같은 정리를 바라보는 것은 수학적 통찰을 깊게 한다.

### 이 글에 대하여

이 글은 [Five of Euler's best](https://plus.maths.org/content/five-eulers-best-0)의 일부입니다. 2016년 유럽 수학 학회에서 수학자 [Günter M. Ziegler](http://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/)가 발표한 강연을 바탕으로 한 이 시리즈의 다른 네 가지 문제를 읽으려면 [여기](https://plus.maths.org/content/five-eulers-best-0)를 클릭하세요.

[Günter M. Ziegler](http://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/)는 베를린 자유대학교(Freie Universität Berlin)의 수학 교수이며, [독일 수학회 DMV](https://dmv.mathematik.de)의 수학 미디어 사무소 소장을 겸임하고 있습니다. 그의 저서로는 Martin Aigner와 공저한 [Proofs from THE BOOK](http://www.springer.com/us/book/9783642008566)과 [Do I count? Stories from Mathematics](https://www.crcpress.com/Do-I-Count-Stories-from-Mathematics/Ziegler/p/book/9781466564916) 등이 있습니다.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)는 *Plus* 매거진의 편집자입니다. 그녀는 2016년 7월 베를린에서 열린 유럽 수학 학회에서 Ziegler가 발표한 오일러에 관한 강연을 매우 즐겁게 들었으며, 이 글은 그 강연을 바탕으로 작성되었습니다.

> 오일러(Leonhard Euler, 1707-1783)는 역사상 가장 다작의 수학자로, 그의 전집은 90권이 넘는다. 그는 해석학, 정수론, 그래프 이론, 위상수학, 수리물리학 등 수학의 거의 모든 분야에 기여했다. 오일러의 다면체 공식은 그의 업적 중에서도 특히 현대 수학의 발전에 지대한 영향을 미쳤다. 이 공식은 19세기 중반 Augustin-Louis Cauchy의 엄밀한 증명을 거쳐, 20세기 Henri Poincaré의 위상수학으로 발전했으며, 현대 대수적 위상수학의 초석이 되었다. 오늘날 오일러 특성수는 미분기하학, 대수기하학, 심지어 끈 이론에서도 중심적 역할을 한다. 하나의 간단한 공식이 300년에 걸쳐 수학의 풍경을 어떻게 바꿀 수 있는지를 보여주는 완벽한 사례이다.

## 댓글

## Guest

훌륭한 글과 멋진 그림들, 감사합니다. 저는 오일러의 공식을 알고 있었지만 그 역사는 몰랐습니다.

글 끝부분에 오타가 있는 것 같습니다: "you don't need to know at what angle $to$ faces of a polyhedron meet"

## Marianne

지적해 주셔서 감사합니다. 수정했습니다.