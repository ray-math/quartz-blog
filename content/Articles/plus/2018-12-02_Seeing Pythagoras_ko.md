---
title: 피타고라스 정리를 눈으로 보기
date: 2018-12-02
tags:
  - 증명
  - 수학
  - State
  - 애플릿
  - Garfield
  - Northeastern
  - 마우스
  - 대통령
---

> [!NOTE]
> https://plus.maths.org/content/seeing-pythagoras
>
> 기하학의 위대한 점은 때때로 그림만으로도 증명할 수 있다는 것입니다. 피타고라스 정리의 세 가지 훌륭한 시각적 증명을 즐겨보세요!

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/visual_frontpage.png?h=1c7b55f3&itok=ptXBmZIl)

아래는 피타고라스 정리의 세 가지 시각적 증명으로, [Northeastern State University](https://academics.nsuok.edu/mathematics/MeettheFaculty/JohnDiamantopoulos.aspx)의 수학 교수인 John Diamantopoulos가 *Plus* 매거진에 보내준 것입니다.

> 피타고라스 정리는 직각삼각형에서 빗변의 제곱이 두 직각변의 제곱의 합과 같다는 것을 말합니다($a^{2} + b^{2} = c^{2}$). 이 정리는 수학사에서 가장 많은 증명이 존재하는 정리 중 하나로, 대수적 증명부터 기하학적 증명까지 수백 가지 방법이 알려져 있습니다. 시각적 증명의 특별한 가치는 복잡한 대수 계산 없이도 면적의 재배열이라는 직관적 아이디어만으로 정리의 본질을 파악할 수 있다는 점입니다. 이는 "증명 없는 증명(proof without words)"이라는 수학적 미학의 전통과도 연결됩니다.

첫 번째 시각적 증명은 아마도 피타고라스 본인이 사용했을 것으로 추정되는 것과 유사합니다. 애니메이션 GIF를 보면서 초기 정사각형 내부의 영역들이 어떻게 재배열되어 증명을 제공하는지 관찰해보세요. 애니메이션을 다시 보려면 이미지 위로 마우스를 가져가면 됩니다.

![Visual proof 1](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/visual_proof/Pythagoras1.gif)

> 이 증명의 핵심 아이디어는 다음과 같습니다. 한 변의 길이가 $a + b$인 큰 정사각형을 두 가지 다른 방법으로 쪼개어 생각합니다. 첫 번째 방법에서는 중앙에 한 변이 $c$(빗변)인 정사각형이 있고, 그 주변에 네 개의 합동인 직각삼각형이 배치됩니다. 두 번째 방법에서는 같은 네 개의 직각삼각형을 재배치하되, 이번에는 한 변이 $a$인 정사각형과 한 변이 $b$인 정사각형이 남게 됩니다. 큰 정사각형의 전체 넓이는 변하지 않으므로 $c^{2} + 4 \times \frac{1}{2}ab = a^{2} + b^{2} + 4 \times \frac{1}{2}ab$가 성립하고, 양변에서 삼각형들의 넓이를 빼면 $c^{2} = a^{2} + b^{2}$를 얻습니다. 이 증명의 아름다움은 면적의 보존이라는 단순한 원리만으로 정리를 증명한다는 점입니다.

아래는 이 증명을 설명하는 동영상입니다. 또한 [여기](https://www.geogebra.org/classic/xqanbavm)에서 Geogebra 애플릿으로 직접 조작해볼 수 있습니다.

두 번째 시각적 증명은 아마도 고대 인도 수학자 [Bhaskara](https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/)가 사용한 것과 유사할 것입니다. 이것 역시 초기의 두 정사각형 내부 영역들의 재배열을 통해 증명을 제공합니다. 애니메이션을 다시 보려면 이미지 위로 마우스를 가져가면 됩니다.

![Visual proof 2](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/visual_proof/Pythagoras_second.gif)

> Bhaskara는 12세기 인도의 위대한 수학자이자 천문학자로, 그의 저서에는 종종 간결한 시각적 증명들이 포함되어 있었습니다. 이 두 번째 증명의 독창성은 다음과 같습니다. 한 변이 $c$인 정사각형 안에 네 개의 합동인 직각삼각형을 특별한 방식으로 배치하면, 중앙에 한 변이 $b - a$(또는 $a - b$)인 작은 정사각형이 남습니다. 이를 수식으로 표현하면 $c^{2} = 4 \times \frac{1}{2}ab + (b - a)^{2}$입니다. 우변을 전개하면 $c^{2} = 2ab + b^{2} - 2ab + a^{2} = a^{2} + b^{2}$가 됩니다. Bhaskara는 이 증명 옆에 단지 "보라!(Behold!)"라는 한 단어만 적었다고 전해지는데, 이는 그림 자체가 모든 것을 말해준다는 자신감의 표현이었습니다. 이 증명은 첫 번째 증명과는 다른 분해 방식을 사용하여 같은 진리에 도달한다는 점에서 수학적 다양성의 아름다움을 보여줍니다.

아래는 이 증명을 설명하는 동영상입니다. 또한 [여기](https://www.geogebra.org/classic/ypgfeza4)에서 Geogebra 애플릿으로 직접 조작해볼 수 있습니다.

세 번째 시각적 증명은 미국의 20대 대통령인 [James Garfield](https://en.wikipedia.org/wiki/James_A._Garfield)가 원래 고안한 것입니다. 이 증명은 삼각형의 넓이 공식을 사용합니다. 현재 미국 대통령도 여가 시간에 기하학을 다루는지 궁금하지 않을 수 없습니다. 애니메이션을 다시 보려면 이미지 위로 마우스를 가져가면 됩니다.

![Visual proof 3](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/visual_proof/Pythagoras3a.gif)

> James Garfield는 대통령이 되기 전 수학 교수였으며, 1876년에 이 독창적인 증명을 발견했습니다. 그의 접근법은 이전 두 증명과는 근본적으로 다릅니다. 세 개의 직각삼각형으로 사다리꼴을 구성하는 것이 핵심입니다. 구체적으로, 빗변이 $c$인 합동인 직각삼각형 두 개와 빗변이 각각 $a$와 $b$인 직각삼각형 하나를 적절히 배치하면 사다리꼴이 만들어집니다. 이 사다리꼴의 넓이는 두 가지 방법으로 계산할 수 있습니다. 첫째, 사다리꼴 공식을 사용하면 $\frac{(a + b)(a + b)}{2} = \frac{(a + b)^{2}}{2}$입니다. 둘째, 세 삼각형의 넓이를 더하면 $\frac{1}{2}ab + \frac{1}{2}ab + \frac{1}{2}c^{2} = ab + \frac{1}{2}c^{2}$입니다. 두 식을 같다고 놓으면 $\frac{(a + b)^{2}}{2} = ab + \frac{1}{2}c^{2}$이고, 양변에 2를 곱하고 정리하면 $a^{2} + 2ab + b^{2} = 2ab + c^{2}$, 즉 $a^{2} + b^{2} = c^{2}$를 얻습니다. 이 증명의 독창성은 사다리꼴이라는 보조 도형을 사용하여 넓이를 두 가지 방식으로 계산한다는 발상에 있습니다. Garfield는 이 증명으로 수학 저널에 논문을 게재한 유일한 미국 대통령이 되었습니다.

아래는 이 증명을 설명하는 동영상입니다. 또한 [여기](https://www.geogebra.org/m/hxuve76q)에서 Geogebra 애플릿으로 직접 조작해볼 수 있습니다.

![Visual proof 1](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/visual_proof/animation1a.gif)

> 이 세 가지 증명은 모두 같은 정리를 증명하지만, 각각 다른 기하학적 통찰을 제공합니다. 첫 번째는 정사각형의 분해와 재구성, 두 번째는 직각삼각형의 회전과 배치, 세 번째는 사다리꼴의 넓이 비교라는 서로 다른 전략을 사용합니다. 이러한 다양성은 수학의 중요한 특징을 보여줍니다. 하나의 진리에 도달하는 길은 여러 개 있으며, 각각의 길은 그 나름의 아름다움과 통찰을 제공합니다. 시각적 증명의 가치는 단지 정리를 증명하는 것을 넘어, 왜 그것이 참인지에 대한 직관적 이해를 제공한다는 데 있습니다. 이는 형식적인 대수적 증명이 제공하지 못하는 종류의 깨달음입니다.

### 필자 소개

![John C. D. Diamantopoulos](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2014/maya/john.jpg)

John C. D. Diamantopoulos는 Oklahoma주 Tahlequah에 위치한 Northeastern State University의 수학 및 컴퓨터 과학과 교수입니다. 그의 수학적 관심사는 상미분방정식, 수학 교육, 수학사를 포함합니다. Diamantopoulos는 또한 교회에서 매우 활발하게 활동하며 컴퓨터 제작/프레젠테이션 및 관심이 필요한 모든 영역에서 자원봉사를 하고 있습니다.

이 글은 2018년 2월에 처음 출판되었으며 2019년 12월에 업데이트되었습니다.