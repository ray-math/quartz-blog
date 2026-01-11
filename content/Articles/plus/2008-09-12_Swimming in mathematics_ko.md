---
title: 수학 속에서 수영하기
date: 2008-09-12
tags:
  - 구조
  - Phelan
  - Weaire
  - 거품
  - Water
  - 켈빈
  - Cube
  - www
---

> [!NOTE]
> https://plus.maths.org/content/swimming-mathematics
>
> 올림픽 수영 경기장을 덮은 거품의 수학

![foam](https://plus.maths.org/content/sites/default/files/styles/small_square/public/latestnews/sep-dec08/watercube/icon.jpg?itok=3E2dA13e)

[Constructing our lives package](https://plus.maths.org/content/ingenious-constructing-our-lives)

-->

베이징에서 올림픽이 끝나고 패럴림픽이 그 뒤를 이어 계속되면서 스포츠 영광이 이어지는 가운데, 많은 이들이 스포츠 성취만큼이나 건축물에 감탄했다. 올림픽 경기장 중 하나인 국가수영센터(National Aquatic Centre)는 '워터 큐브(Water Cube)'라는 이름에 걸맞게, 거대한 거품 덩어리에서 잘라낸 듯한 모습을 하고 있다. 이 효과는 밤하늘을 배경으로 푸른 빛을 발할 때 더욱 극대화된다.

![The Water Cube at night](https://plus.maths.org/latestnews/sep-dec08/watercube/watercube_bosse_crop.jpg)

밤의 워터 큐브. 이미지 © [Chris Bosse](http://www.chrisbosse.de).

이러한 거품 같은 외관을 구현하기 위해 [ARUP](http://www.arup.com)의 엔지니어들과 [PTW](http://www.ptw.com.au)의 건축가들은 두 아일랜드 물리학자, Denis Weaire와 Robert Phelan의 연구를 기반으로 설계했다. 1993년 Weaire와 Phelan은 *켈빈 문제(Kelvin problem)*에 대한 새로운 해답을 찾아냈다. 켈빈 문제란 다음과 같다: 동일한 부피의 셀들로 공간을 분할하되, 표면적이 최소가 되도록 하는 가장 효율적인 방법은 무엇인가?

> 켈빈 문제는 자연계에서 흔히 관찰되는 거품 구조의 본질을 묻는 문제다. 비누 거품이나 금속 결정, 생물학적 세포 조직 등은 모두 에너지를 최소화하려는 자연의 경향을 따른다. 표면적을 최소화한다는 것은 곧 표면 에너지를 최소화한다는 의미이며, 이는 주어진 부피를 담는 데 가장 "경제적인" 방법을 찾는 것과 같다. 이 문제는 단순해 보이지만, 3차원 공간을 균일하게 채우면서 동시에 표면적을 최소화하는 구조를 찾는 것은 기하학적으로 매우 복잡한 최적화 문제다. 켈빈이 이 문제를 제기한 1887년 이후 100년 넘게 더 나은 해답이 발견되지 않았다는 사실이 이 문제의 난이도를 말해준다.

![Truncated octahedron](https://plus.maths.org/latestnews/sep-dec08/watercube/truncatedoctahedron.png)

절단된 팔면체로 이루어진 켈빈의 제안 구조

이것이 복잡하게 들릴 수 있지만, 사실 설거지를 할 때마다 만들어내는 비눗물 거품이 이 구조의 성질 중 일부를 보여준다. 비누 거품과 거품 구조는 *최소 곡면(minimal surface)*이라는 수학적 성질을 갖는다. 즉, 주어진 부피를 둘러싸는 데 가장 적은 표면적을 사용하는 구조를 취한다.

> 최소 곡면은 표면의 각 점에서 평균 곡률이 0이 되는 곡면이다. 직관적으로 설명하면, 곡면이 어느 방향으로도 "선호"하지 않고 균형을 이루는 상태다. 비누막이 이러한 형태를 취하는 이유는 물리적으로 표면 장력을 최소화하려고 하기 때문이다. 수학적으로는 이것이 변분법(calculus of variations)의 문제로, 곡면의 넓이를 최소화하는 함수를 찾는 것이다. 역사적으로 최소 곡면 연구는 Joseph-Louis Lagrange가 1760년대에 시작했으며, 이후 많은 수학자들이 다양한 경계 조건에서 최소 곡면을 찾는 문제를 연구했다. 비누막 실험은 복잡한 최소 곡면을 물리적으로 구현하는 훌륭한 방법이며, 컴퓨터가 발달하기 전에는 이러한 물리적 모형이 최소 곡면을 찾는 실질적인 도구였다.

켈빈 경은 1887년 거품 문제에 대한 [해답](http://zapatopi.net/kelvin/papers/on_the_division_of_space.html)을 제안했다. 그는 각 셀이 절단된 팔면체(truncated octahedron)라고 제안했는데, 이것은 익숙한 3차원 다이아몬드 모양의 모서리를 잘라낸 14면체이다.

> 절단된 팔면체는 정팔면체(정삼각형 8개로 이루어진 입체)의 6개 꼭짓점을 잘라낸 형태다. 이 과정을 통해 8개의 정삼각형 면은 정육각형이 되고, 잘라낸 6개의 꼭짓점 자리에는 정사각형 면이 생긴다. 결과적으로 6개의 정사각형 면과 8개의 정육각형 면을 가진 14면체가 된다. 켈빈이 이 구조를 선택한 이유는 이것이 공간을 빈틈없이 채울 수 있으면서(space-filling property) 동시에 비교적 대칭성이 높고 표면적이 작기 때문이다. 벌집의 육각형 구조가 2차원 평면을 가장 효율적으로 채우는 것처럼, 켈빈은 절단된 팔면체가 3차원 공간을 가장 효율적으로 채울 것이라고 추측했다. 이 구조는 실제로 일부 금속의 결정 구조에서도 관찰된다.

켈빈은 자신의 거품 구조가 실제로 가능한 최소 표면적을 가진 구조라는 수학적 증명을 제공하지 않았지만, Weaire와 Phelan이 발견하기까지 한 세기 이상 더 나은 해답이 발견되지 않았다. 그들의 구조는 두 종류의 불규칙한 다면체로 이루어져 있다. 하나는 오각형 면을 가진 비뚤어진 12면체(즉, 각 면이 5개의 변을 가진 12개의 면으로 이루어짐)이고, 다른 하나는 2개의 육각형 면과 12개의 오각형 면을 가진 비뚤어진 14면체(따라서 14개의 면 중 2개는 6개의 변을, 12개는 5개의 변을 가짐)이다. 사실 더 비뚤어지게 만드는 요소가 있는데, 거품의 법칙에 따라 켈빈 구조와 Weaire-Phelan 구조 모두 약간 휘어진 면을 갖는다.

> Weaire-Phelan 구조의 핵심은 단순히 면의 개수가 아니라 이 두 다면체가 특정 비율로 반복되어 공간을 완벽하게 채운다는 점이다. 구체적으로, 이 구조는 12면체 6개와 14면체 2개가 하나의 단위 셀을 이루며, 이 단위 셀이 3차원 공간에서 반복된다. 면이 "약간 휘어진다"는 것은 Plateau의 법칙을 따른다는 의미다. 거품 구조에서 세 개의 면이 만나는 곳에서는 약 120도 각도를 이루고, 네 개의 모서리가 만나는 곳에서는 약 109.47도(정사면체 각도)를 이룬다. 이러한 기하학적 제약 때문에 면이 완벽한 평면이 될 수 없고 약간 휘어지게 된다. Weaire와 Phelan은 컴퓨터 시뮬레이션을 통해 이 구조가 켈빈 구조보다 약 0.3% 표면적이 작다는 것을 발견했다. 작은 차이처럼 보이지만, 100년 넘게 지배적이었던 켈빈의 추측을 깨뜨린 획기적인 발견이었다.

![The Weaire-Phelan foam](https://plus.maths.org/latestnews/sep-dec08/watercube/weairephelanfoam.jpg)

Weaire-Phelan 거품 구조(왼쪽)는 오각형 면을 가진 비뚤어진 12면체(오른쪽 위)와 2개의 육각형 면과 12개의 오각형 면을 가진 14면체(오른쪽 아래)로 이루어져 있다.

"우리는 이 거품 구조에 대해 흥미로운 특징을 곧 발견했습니다. 완전히 규칙적인 구조임에도 불구하고, 임의의 각도에서 보면 완전히 무작위적이고 유기적으로 보인다는 점이었죠."라고 Arup Fellow인 Tristram Carfrae는 워터 큐브의 설계를 Weaire-Phelan 구조에 기반한 이유를 설명하면서 말했다. "우리는 이 독특한 기하학에 기반한 구조가 매우 반복적이고 건설 가능하면서도 동시에 매우 유기적이고 무작위적으로 보일 것임을 깨달았습니다. 실제로 이러한 공간 채움 패턴은 생물학적 세포와 광물 결정에서 규칙적으로 관찰되며, 아마도 자연에서 가장 흔한 구조일 것입니다. 또한 이 기하학으로부터 생성되는 연성 공간 프레임(ductile space frame)은 베이징에서 발견되는 지진 조건에 이상적으로 적합합니다."

> 이 설명은 수학과 건축의 만남에서 중요한 통찰을 제공한다. 수학적으로 규칙적인 패턴이 시각적으로는 무작위하게 보이는 현상은 패턴의 복잡성과 관찰자의 인지 사이의 관계를 보여준다. 워터 큐브의 벽면은 수학적으로는 Weaire-Phelan 구조의 단순한 반복이지만, 이 패턴이 3차원 곡면에 투영되고 다양한 각도에서 관찰되면 우리의 뇌는 이를 자연스러운 거품 패턴으로 인식한다. "연성 공간 프레임"이란 외부 힘에 대해 탄성적으로 변형될 수 있는 구조 시스템을 의미한다. 지진 발생 시 건물이 완전히 강체처럼 움직이는 것보다, 구조 전체가 약간씩 변형되면서 에너지를 분산시키는 것이 더 안전하다. Weaire-Phelan 구조는 수많은 절점(node)과 부재(member)로 이루어진 트러스 시스템을 생성하며, 이는 자연스럽게 하중을 분산시키고 지진력을 흡수하는 데 유리하다. 이는 단순히 미학적 선택이 아니라 구조 공학적으로도 합리적인 선택이었다.

![The Water Cube at night](https://plus.maths.org/latestnews/sep-dec08/watercube/23917cArupBenMcMillan.jpg)

이미지 © [Arup Ben McMillan.](http://www.arup.com)

따라서 우리는 Weaire와 Phelan의 수학 덕분에 이처럼 독특하고 아름다운 건물을 갖게 되었으며, 그 구조는 내부에 담긴 물과 같은 물질로 만들어진 것처럼 보인다. 그리고 Weaire와 Phelan이 그들의 거품 구조가 켈빈의 것보다 표면적이 작다는 것(비누를 덜 사용한다고 생각할 수 있다)을 보여주었지만, 그들도 이것이 가능한 최소 표면적을 가진다는 것을 증명하지는 못했다. 그러니 다음에 설거지를 하거나 2012년 올림픽을 위해 훈련할 때 생각해볼 만한 또 다른 주제다.

> 이 마지막 언급은 수학에서 자주 등장하는 상황을 보여준다. 더 나은 해답을 찾았다고 해서 그것이 최적해라는 보장은 없다. Weaire-Phelan 구조는 켈빈 구조를 개선했지만, 이것이 절대적으로 최소 표면적을 가진 구조인지는 여전히 열린 문제다. 이론적으로 증명하기 어려운 이유는, 가능한 모든 공간 분할 방식을 체계적으로 탐색하고 비교할 수 있는 일반적인 방법이 없기 때문이다. 이는 많은 최적화 문제에서 "충분히 좋은" 해답과 "최적의" 해답 사이의 차이를 보여준다. 실용적 목적으로는 Weaire-Phelan 구조가 충분히 효율적이지만, 수학적으로는 더 나은 구조가 존재할 가능성이 여전히 열려 있다. 이러한 미해결 문제들이 바로 수학을 흥미롭게 만드는 요소다.

### 더 읽을거리

*Plus*에는 거품, 최소 곡면, 건축에 관한 여러 기사가 있다:

[Getting a handle on soap](http://plus.maths.org/latestnews/sep-dec05/minimal/index.html)
[Double bubble is no trouble](http://plus.maths.org/issue12/news/bubble/)
[Still life](http://plus.maths.org/latestnews/sep-dec06/visualisation/index.html)
[Perfect buildings: the maths of modern architecture](http://plus.maths.org/issue42/features/foster/)
[Career interview with Architect Wen Quek](http://plus.maths.org/issue26/interview/index.html)

*Architecture Australia*의 [Engineering the Water Cube](http://www.architectureaustralia.com/aa/aaissue.php?issueid=200607&article=18&typeon=3)

*이 콘텐츠는 현재 Isaac Newton Institute for Mathematical Sciences(INI)와의 협력의 일부를 이룬다. 우리의 협력으로부터 나온 모든 콘텐츠는 여기서 찾을 수 있다.
INI는 국제 연구 센터이자 케임브리지 대학교 수학 캠퍼스에 있는 우리의 이웃이다. 전 세계의 주요 수학자들을 끌어들이며, 모두에게 열려 있다. www.newton.ac.uk를 방문하여 더 자세히 알아보라.*

![INI logo](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)