---
title: 타일링 속의 유령들
date: 2021-01-29
---

> [!NOTE]
> https://plus.maths.org/content/ghosts-tiles
>
> 곡선을 좋아하시나요? 그렇다면 삼곡선(tricurve)과 그들의 유령 같은 환영(phantom)을 사랑하게 될 것입니다!

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/tricurves_frontpage.jpg?itok=IsOcNM0l)

컴퍼스와 자를 가지고 놀다 보면, 호(arc)를 변으로 가진 온갖 흥미로운 도형들을 발견할 수 있습니다. 호로 이루어진 몇 가지 간단한 기하학적 도형들을 살펴봅시다.

한 예로 *뢸로 삼각형(Reuleaux triangle)*이 있습니다. 이 도형은 정삼각형의 꼭짓점들로부터 만들어지는데, 아래 그림과 같습니다. 컴퍼스의 바늘을 각 꼭짓점에 놓고 나머지 두 꼭짓점을 연결하는 원호를 그립니다. 세 개의 호 각각은 중심에 해당하는 꼭짓점에서 60°의 각을 이룹니다. 뢸로 삼각형은 호로 이루어진 도형 중에서 유일하게 꼭짓점(모서리)이 동시에 변을 이루는 호의 중심이 되는 도형입니다.

![Reuleaux triangle](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/reuleaux2.png)

뢸로 삼각형(오른쪽)은 정삼각형으로부터 만들어진다.

> 뢸로 삼각형은 19세기 독일 기계공학자 Franz Reuleaux의 이름을 딴 것입니다. 이 도형의 가장 놀라운 성질은 "등폭 곡선(curve of constant width)"이라는 점입니다. 즉, 어느 방향에서 측정하더라도 두 평행선 사이의 폭이 항상 일정합니다. 이는 원이 아니면서도 원과 같은 성질을 가진다는 의미로, 실제로 영국의 50펜스 동전이나 캐나다의 일부 동전이 이 모양을 사용합니다. 회전하는 기계 부품 설계에도 응용되는데, 정사각형 구멍을 뚫을 수 있는 드릴 비트가 바로 이 원리를 이용합니다.

일반적으로 원호의 모양은 두 가지 정보로 정의됩니다: 원의 반지름과 그 호가 원의 중심에서 이루는 각도(중심각)입니다. 위 그림에서 보는 바와 같습니다.

호로 이루어진 다른 도형들 중에서도 호의 중심과 도형의 꼭짓점 사이에 흥미로운 관계를 가진 것들을 찾을 수 있습니다. 아래의 세 도형 각각에 대해, 꼭짓점으로부터 호를 그리면 같은 도형이 다시 나타나는데, 회전되거나 대칭 이동된 형태입니다. 원래 도형의 호의 중심들이 새 도형의 꼭짓점에 위치하고, 그 역도 성립합니다. 이 과정은 가역적입니다.

![Three shapes with phantoms](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/shapes_with_phantoms.png)

환영을 가진 세 개의 도형.

이렇게 만들어지는 두 번째 도형을 첫 번째 도형의 "환영(phantom)"이라고 부를 수 있습니다. 즉, 환영은 원래 도형의 꼭짓점들로부터 (같은, 원래의 반지름으로) 그린 호들로 둘러싸인 도형입니다. 이것은 같은 도형이지만 회전이나 대칭 이동에 의해 변환된 것입니다. 위에서 본 뢸로 삼각형은 자기 참조적입니다. 즉, 자기 자신이 자신의 환영입니다. 이 환영들을 원래 도형과 함께 보이지 않게 떠다니는 존재, 일종의 유령 같은 존재로 생각할 수 있습니다.

> "환영(phantom)"이라는 용어는 원래 도형과 밀접하게 연결되어 있지만 물리적으로는 분리된 이 기하학적 대응물의 성질을 포착합니다. 수학에서 쌍대성(duality)의 개념과 유사한데, 한 구조의 점들이 다른 구조의 선이 되는 사영기하학의 쌍대 원리를 떠올릴 수 있습니다. 여기서는 꼭짓점과 호의 중심이 서로 역할을 바꾸면서 새로운 도형을 생성합니다. 이러한 변환의 가역성은 군론(group theory)에서 역원(inverse element)의 존재와 유사한 깊은 대칭성을 시사합니다.

이 글의 목적을 위해 우리가 관심을 가지는 것은 수학자들이 2차원 도형과 마주쳤을 때 자주 던지는 질문입니다: 만약 이 모양의 타일을 준다면, 그 타일만으로 평면 전체를 타일링할 수 있을까요? 마치 정사각형으로 평면을 타일링할 수 있는 것처럼 말입니다.

지금까지 살펴본 네 개의 도형에 대한 답은 "아니오"입니다. 이들 중 어느 것도 홀로(*단일 타일로, monohedrally*) 평면을 타일링할 수 없습니다. 호로 이루어진 도형이 평면을 타일링하기 위해 필요한 것은 *오목한(concave)* 호(안쪽으로 볼록한)와 *볼록한(convex)* 호(바깥쪽으로 볼록한)가 같은 양만큼 있어야 한다는 것입니다.

> 타일링(tessellation)은 빈틈이나 겹침 없이 평면을 덮는 방법을 다룹니다. 오목한 호와 볼록한 호가 같은 양이어야 한다는 조건은 기하학적으로 깊은 의미를 담고 있습니다. 볼록한 호는 면적을 "추가"하고 오목한 호는 면적을 "제거"하는 것으로 볼 수 있는데, 이들이 균형을 이루어야 타일들이 서로 맞물려 빈틈을 채울 수 있습니다. 이는 위상수학(topology)에서 오일러 특성수(Euler characteristic)와도 관련이 있으며, 곡률의 합이 0이 되어야 평면을 채울 수 있다는 가우스-보네 정리(Gauss-Bonnet theorem)의 직관적인 예시라고 할 수 있습니다.

하지만 다섯 번째 도형, 아니 정확히는 도형들의 족(family)을 살펴봅시다.

### 삼곡선(Tricurves)

렌즈(lens)는 가장 단순한 기하학적 도형 중 하나로, 양 끝에서 만나는 두 개의 동일한 호로 이루어져 있습니다. 호의 반지름이 1이라고 가정하면 (단순화를 위해) 렌즈는 단순히 호의 각도로 기술될 수 있습니다.

한 호 위의 한 점을 선택하여 호를 두 부분으로 나눈 다음, 각 부분으로부터 렌즈를 만들 수 있습니다. 큰 렌즈에서 두 개의 작은 렌즈를 빼면 특이한 성질을 가진 *삼곡선(tricurve)* 도형을 얻게 됩니다:

![Tricurve geometry](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/tricurve_geometry.jpg)

삼곡선의 기하학.

> 삼곡선은 세 개의 원호로 이루어진 도형으로, 그 구성 방법이 매우 독창적입니다. 큰 렌즈 하나에서 작은 렌즈 두 개를 "빼는" 과정은 불 대수(Boolean algebra)의 차집합 연산으로 볼 수 있습니다. 이렇게 만들어진 도형은 하나의 큰 볼록한 호와 두 개의 작은 오목한 호를 가지게 되는데, 이것이 앞서 언급한 오목-볼록 균형 조건을 자동으로 만족시킵니다. 실제로 두 작은 각도의 합이 큰 각도와 같다는 관계식이 성립하며, 이는 삼곡선이 평면을 타일링할 수 있는 핵심 이유입니다.

어떤 삼곡선이든 평면을 *주기적으로(periodically)* 타일링할 수 있습니다. 즉, 패턴을 들어 올려 특정 방향으로 특정 거리만큼 이동시킨 후 다시 놓아도 같아 보이는 패턴입니다. 아래 그림과 같습니다.

![A periodic tiling](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/periodic_tiling.png)

주기적 타일링.

삼곡선을 이루는 호의 각도들이 360°의 약수이고 호들이 보기 좋은 비율(1:2:3과 같은)을 이루면, 삼곡선은 놀랍게도 방사형 타일링과 비주기적 타일링도 가능합니다. 이것은 흥미로운 퍼즐을 만들어내는데, [구매](https://www.cherryarbordesign.com/product/tricurve/)하거나 [직접 만들](https://aperiodical.com/2019/02/making-tricurves/) 수 있습니다:

![Tricurve puzzle](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/fig4a.jpg)

![Tricurve puzzle](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/fig4b.jpg)

퍼즐들

각 삼곡선은 세 호의 각도를 오름차순으로 나타내어 기술되며, 두 오목한 호의 각도를 더하면 항상 큰 볼록한 호의 각도가 됩니다. 지금까지 만들어진 퍼즐들은 30°-60°-90° (위 이미지)나 36°-72°-180° 호(아래 이미지)를 가진 삼곡선을 사용하지만, 많은 조화로운 각도와 비율을 사용할 수 있습니다. 단일 타일 타일링 외에도, 삼곡선은 둘 이상의 크기로 이루어진 집합으로도 타일링할 수 있습니다.

> 30°-60°-90°와 36°-72°-180° 삼곡선이 특별한 이유는 이들의 각도가 정다각형과 관련이 있기 때문입니다. 30°는 정십이각형(12각형)과, 60°는 정육각형과, 90°는 정사각형과, 36°는 정십각형과, 72°는 정오각형과 연결됩니다. 360°의 약수라는 조건은 회전 대칭(rotational symmetry)을 가능하게 하여, 중심 주위로 정수 개의 타일을 배치할 수 있게 만듭니다. 이는 결정학(crystallography)에서 공간군(space group)의 허용 대칭과 유사한 제약입니다. 1:2:3 같은 비율이 "보기 좋다"는 것은 단순한 미적 판단이 아니라, 수학적으로 작은 정수비가 조화로운 분할을 만들어낸다는 피타고라스 학파의 통찰과도 연결됩니다.

### 삼곡선의 환영들

삼곡선의 환영을 살펴보면 어떻게 될까요? 각 삼곡선은 환영을 가지고 있으며, 이는 그 도형에 고유한 회전 중심을 기준으로 180° 회전한 결과입니다. 삼곡선에 따라 환영은 원래 도형과 겹칠 수도 있고 꽤 떨어져 있을 수도 있습니다.

![Some tricurves with phantoms](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/some_tricurves_with_phantoms.jpg)

환영을 가진 몇 가지 삼곡선들.

어떤 삼곡선에 대해서든 환영의 위치를 결정하거나 시각화하려면, 단순히 삼곡선을 반 바퀴 회전시키고 중간 꼭짓점(두 오목한 변을 연결하는 점)을 원래 삼곡선의 큰 호의 중심에 위치시키면 됩니다. 예를 들어, 큰 호가 180°인 삼곡선의 경우, 두 개의 작은 호가 무엇이든 관계없이 환영의 중간 꼭짓점은 항상 그 반원의 중심에 위치합니다:

![Some tricurves with 180° large arc](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/some_tricurves_with_180_large_arc.jpg)

큰 호가 180°인 몇 가지 삼곡선들.

> 180° 호가 특별한 이유는 그것이 정확히 반원이기 때문입니다. 반원의 중심은 직경의 중점이며, 이는 기하학적으로 매우 안정적인 기준점입니다. 환영을 찾는 규칙이 "중간 꼭짓점을 큰 호의 중심에 놓는다"는 것은 매우 우아한 구성 원리입니다. 이는 역기하학적 변환(inverse geometric transformation)의 한 형태로 볼 수 있으며, 복소평면에서 원에 대한 반전(inversion with respect to a circle)과 유사한 면이 있습니다. 삼곡선의 세 꼭짓점 중 중간 것이 특별한 이유는 그것이 두 오목한 호가 만나는 지점, 즉 도형의 "허리"에 해당하기 때문입니다.

대칭적인 삼곡선의 경우, 환영은 원래 삼곡선을 180° 회전시킨 것입니다. 하지만 그것은 또한 원래 삼곡선의 대칭축을 따라 거울 대칭 이동한 것이기도 합니다.

![Some symmetrical tricurves and phantoms](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/some_symmetrical_tricurves_and_phantoms.jpg)

대칭적인 삼곡선들과 환영들.

> 대칭적인 삼곡선에서는 180° 회전과 거울 대칭이 같은 결과를 낳습니다. 이는 대칭군(symmetry group) 이론에서 중요한 상황입니다. 도형이 대칭축을 가질 때, 점대칭(point symmetry)과 선대칭(line symmetry)이 교환 가능(commute)하다는 것을 의미합니다. 군론적으로 표현하면, 이 두 변환의 합성이 항등원소(identity element)를 생성합니다. 이러한 이중 대칭성은 결정학에서 특정 공간군이 더 높은 대칭성을 갖는 이유를 설명하며, 삼곡선 타일링의 패턴이 왜 시각적으로 조화로운지를 수학적으로 뒷받침합니다.

### 환영과 함께하는 타일링

삼곡선을 타일링한 후 환영을 살펴보면, 기쁘게도 환영들도 타일링한다는 것을 발견합니다. 주기적 타일링은 예상할 수 있듯이 환영들도 주기적으로 타일링하게 만듭니다:

![A periodic tiling with phantoms](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/periodic_tiling_phantoms.png)

환영과 함께하는 주기적 타일링.

그러나 이 간단한 설명과 이미지는 다소 오해의 소지가 있습니다. 상황은 보이는 것만큼 단순하지 않습니다. 위 이미지에서 어떤 환영이 어떤 원래 도형과 짝을 이루는지 보려면 자세히 살펴봐야 합니다. 그렇게 하면 원래 삼곡선들의 전체 그룹이 180° 회전하는 것 외에도 환영들이 위치를 바꾸었다는 것을 알게 됩니다. 환영 그룹을 180° 되돌려 회전시키면, 그룹이 원래 그룹과 달라졌음을 발견합니다.

이것은 다른 크기의 삼곡선을 사용할 때 더 명확하게 보입니다. 아래 예시에서 환영들은 180° 회전했을 뿐만 아니라 서로 반대편에 있습니다. 그들은 더 이상 같은 호를 공유하지 않습니다:

![Transposed phantoms](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/transposed_phantoms.jpg)

전치된 환영들.

> 이 "전치(transposition)" 현상은 삼곡선 타일링의 가장 신비롭고 반직관적인 특성입니다. 단순히 각 타일의 환영이 그 타일 근처에 나타날 것이라고 예상하지만, 실제로는 환영들이 집단적으로 재배열됩니다. 이는 양자역학에서 입자들의 교환 대칭성(exchange symmetry)이나, 대수학에서 치환군(permutation group)의 행동을 연상시킵니다. 수학적으로 이는 타일링 공간에서 두 가지 독립적인 변환-국소적 180° 회전과 전역적 위치 교환-이 동시에 일어나고 있음을 의미합니다. 이러한 이중 구조는 타일링이 단순한 기하학적 패턴 이상의 풍부한 조합론적 구조를 가지고 있음을 보여줍니다.

이런 종류의 섬뜩한 행동은 방사형 타일링에서도 나타납니다. 아래의 삼곡선 별 또는 꽃 패턴에서, 환영들은 고리를 형성합니다:

![Flower pattern with phantom ring](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/flowe_phantom.png)

환영 고리가 있는 꽃 패턴.

따라서 삼곡선을 사용하여 타일링할 때-두 조각부터 평면 전체를 타일링하는 것까지-환영들은 항상 타일링하지만 직관적이지 않은, 전치된 방식으로 타일링합니다. 나무로 만든 삼곡선 조각들을 맞추는 동안 환영들도 뒤에서 이상한 방식으로 함께 맞춰지고 있다고 생각하면 조금 섬뜩합니다.

또한 흥미로운 다른 질문이 있습니다. 삼곡선을 사용하여 특정한 모양을 채우면 어떻게 될까요? 그것은 [다음 페이지](https://plus.maths.org/content/ghosts-tiles-continued)에서 알아보겠습니다.

> 방사형 타일링에서 환영들이 고리를 형성한다는 것은 각 개별 타일의 환영이 회전 중심으로부터 같은 거리에 위치한다는 의미입니다. 이는 원의 방정식 $r = \text{constant}$를 만족하는 위치 집합으로, 극좌표계(polar coordinates)에서 자연스러운 구조입니다. 중심으로부터의 방사 패턴과 환영들의 원형 배열은 서로 쌍대적(dual) 관계에 있으며, 이는 푸리에 변환(Fourier transform)에서 시간 영역과 주파수 영역의 관계, 또는 위치와 운동량의 상보성과 유사한 깊은 수학적 구조를 암시합니다.

### 더 읽을거리

Tim Lexen의 *Tiling with one arc-sided shape*, *mathblog*  
Tim Lexen의 *Bending the law of sines*, *Aperiodical*  
Tim Lexen의 *Combining tricurves*, *Aperiodical*  
Tim Lexen의 *Phantom tilings*, *Aperiodical*

### 저자 소개

![Tim Lexen](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/Tricurves/t._lexen.jpg)

Tim Lexen

Tim Lexen은 40년 이상 다양한 신제품 연구개발 분야에서 기계공학자로 일해왔습니다. 그는 우아한 해법, 설계 과정, 손재주, 훌륭한 의사소통, 좋은 이야기, 그리고 가족을 즐깁니다. 결혼하여 6명의 자녀와 10명의 손주가 있으며, 미국 위스콘신주의 작은 마을 컴벌랜드에 살고 있습니다.