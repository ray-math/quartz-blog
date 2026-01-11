---
title: "1분 수학: 확산"
date: 2024-12-12
tags:
  - 방정식
  - 확산
  - differential
  - equations
  - 온도
  - 푸리에
  - Fourier
  - 금속
---

> [!NOTE]
> https://plus.maths.org/content/maths-minute-diffusion
>
> 신선한 커피 향기를 맡거나 뜨거운 물에 티백을 넣을 때마다 우리는 확산 현상의 혜택을 받고 있습니다. 이 기본 개념에 대한 빠른 입문을 만나보세요.

![차 한 잔](https://plus.maths.org/content/sites/default/files/styles/small_square/public/2024-12/tea.jpg?h=bd358847&itok=uct2yhX9)

신선한 커피의 향긋한 냄새를 맡거나 뜨거운 물에 티백을 떨어뜨릴 때마다 여러분은 **확산(diffusion)**의 혜택을 받고 있습니다. 확산이란 혼합물 내 입자들의 무작위 운동과 상호작용이 입자들을 주변으로 퍼지게 만드는 현상입니다. 바로 이 과정이 커피 입자를 여러분의 코까지 실어 나르고, 차가 물 전체로 퍼져나갈 수 있게 합니다. 확산은 [음식 소화](https://plus.maths.org/content/eat-drink-and-be-merry-0)부터 [동물 털의 무늬 생성](https://plus.maths.org/content/how-leopard-got-its-spots)에 이르기까지 수많은 과정의 기저를 이루며, 150년 넘게 집중적으로 연구되어 왔습니다.

> 확산은 단순히 물리적 현상을 넘어 생물학, 화학, 의학, 심지어 사회과학에까지 적용되는 보편적 원리입니다. 예를 들어, 우리 몸속에서 산소가 폐에서 혈액으로, 다시 세포로 전달되는 과정, 약물이 체내에 퍼지는 과정, 전염병이 인구 집단에서 확산되는 패턴, 심지어 혁신이나 소문이 사회에 퍼지는 현상까지도 확산 모델로 설명할 수 있습니다. 수학적으로는 무작위 보행(random walk)과 깊은 연관이 있으며, 확률론과 편미분방정식 이론의 교차점에 위치한 풍부한 연구 분야입니다.

확산을 이해하는 데 첫 진전을 이룬 사람은 19세기 초 수학자 [조제프 푸리에(Joseph Fourier)](https://mathshistory.st-andrews.ac.uk/Biographies/Fourier/)였습니다. 그는 고체에서 열이 전파되는 방식에 관심을 갖게 되었습니다. 금속 막대의 한쪽 끝을 가열하면, 미래의 어느 시점에 막대를 따라 있는 임의의 점에서의 온도는 얼마가 될까요?

> 푸리에는 나폴레옹의 이집트 원정에 동행했던 수학자로, 열 전도에 대한 연구로 유명하지만 사실 그의 가장 큰 업적은 **푸리에 급수(Fourier series)**의 발견입니다. 임의의 주기 함수를 사인과 코사인 함수들의 합으로 표현할 수 있다는 이 발견은 현대 신호처리, 음향공학, 이미지 압축의 기초가 되었습니다. 그가 열 전도 연구 과정에서 개발한 수학적 도구들은 물리학을 넘어 순수수학에도 혁명적 영향을 미쳤으며, 편미분방정식 이론의 토대를 마련했습니다.

### 확산 방정식

푸리에는 비교적 간단한 방정식 하나가 막대 위의 주어진 점 $x$에서 임의의 순간 $t$에 온도 $T$가 변하는 방식을 기술한다는 것을 깨달았습니다:

$$
\frac{\partial T}{\partial t}(x,t) = k \frac{\partial^{2} T}{\partial x^{2}}(x,t).
$$

방정식의 왼쪽은 점 $x$에서 온도 $T$가 얼마나 빠르게 변하는지(변화율)를 나타냅니다. (변화율에 대한 이러한 수학적 기술을 **미분방정식(differential equations)**과 **편미분방정식(partial differential equations)**이라고 부르는데, 자세한 내용은 [쉬운 입문](https://plus.maths.org/content/maths-minute-differential-equations)을 참조하세요.)

> 편미분방정식은 여러 변수에 대한 함수의 편미분을 포함하는 방정식입니다. 여기서 온도 $T$는 위치 $x$와 시간 $t$ 두 변수에 모두 의존하므로, 각 변수에 대한 변화율을 따로 고려해야 합니다. $\frac{\partial T}{\partial t}$는 특정 위치를 고정하고 시간에 따른 온도 변화를 측정하며, $\frac{\partial T}{\partial x}$는 특정 순간을 고정하고 공간상의 온도 변화를 측정합니다. 이러한 구분은 시공간에서 일어나는 물리 현상을 기술하는 데 필수적입니다.

방정식 오른쪽의 $k$는 푸리에의 경우 금속을 통해 열이 얼마나 빠르게 전도되는지를 나타내는 상수입니다. 더 일반적으로는 이를 **확산 계수(diffusion coefficient)**라고 부릅니다.

> 확산 계수 $k$는 물질의 성질에 따라 크게 달라지는 중요한 물리량입니다. 예를 들어, 금속에서 열 확산은 매우 빠르지만(높은 $k$ 값), 나무나 플라스틱 같은 절연체에서는 느립니다(낮은 $k$ 값). 생물학적 맥락에서 확산 계수는 분자의 크기, 용액의 점성, 온도에 의존합니다. 산소 같은 작은 분자는 세포막을 빠르게 통과하지만, 단백질 같은 큰 분자는 훨씬 느리게 확산됩니다. 확산 계수의 정확한 측정은 약물 전달 시스템 설계나 화학 반응 속도 예측에 핵심적입니다.

오른쪽의 다른 항은 조금 더 복잡하지만(**고계 도함수(higher order derivative)**입니다), 본질적으로 에너지가 금속 막대의 더 뜨거운 부분에서 더 차가운 부분으로 이동한다는 사실을 담고 있습니다.

> 이계 도함수 $\frac{\partial^{2} T}{\partial x^{2}}$는 온도의 **곡률(curvature)**을 측정합니다. 직관적으로 설명하면, 어떤 점의 온도가 주변보다 높으면 그 점에서 이계 도함수는 음수가 되고, 따라서 $\frac{\partial T}{\partial t}$도 음수가 되어 온도가 감소합니다. 반대로 어떤 점의 온도가 주변보다 낮으면 이계 도함수는 양수가 되고 온도가 증가합니다. 이것이 바로 "뜨거운 곳에서 차가운 곳으로" 에너지가 흐른다는 물리적 직관을 수학적으로 포착하는 방식입니다. 이계 도함수의 역할은 라플라시안(Laplacian) 연산자의 개념으로 일반화되며, 이는 고차원 확산 방정식의 핵심입니다.

푸리에의 방정식은 이제 **확산 방정식(diffusion equation)**으로 알려져 있으며, 단순히 열의 전파뿐만 아니라 어떤 기저의 무작위 과정으로 인해 무언가의 농도가 시간에 따라 변하는 모든 상황을 기술하는 데 사용됩니다. (여기서는 변수 $x$로 주어진 1차원에서의 확산만을 다루도록 방정식을 단순화했지만, 더 복잡한 상황을 기술하도록 다시 쓸 수 있습니다.)

> 확산 방정식의 놀라운 점은 그 보편성입니다. 열 전도, 물질의 확산, 인구 분포, 주식 가격 변동(블랙-숄즈 방정식), 이미지 처리(노이즈 제거), 심지어 기계학습의 일부 알고리즘까지 모두 같은 수학적 구조를 공유합니다. 이 방정식은 포물형 편미분방정식(parabolic PDE)의 원형으로, 비가역적 과정(시간을 거꾸로 돌릴 수 없는)을 기술합니다. 2차원이나 3차원으로 확장할 때는 $\frac{\partial^{2} T}{\partial x^{2}}$를 라플라시안 $\nabla^{2} T = \frac{\partial^{2} T}{\partial x^{2}} + \frac{\partial^{2} T}{\partial y^{2}} + \frac{\partial^{2} T}{\partial z^{2}}$로 대체하면 됩니다. 이 방정식의 해를 구하는 방법(분리 변수법, 그린 함수, 푸리에 변환 등)은 수리물리학의 기초를 이룹니다.

확산에 대한 재미있고 더 상세하지만 이해하기 쉬운 소개는 [좀비 침공에서 우리는 얼마나 오래 살아남을 수 있을까](https://plus.maths.org/content/how-long-can-we-survive)?에서 읽을 수 있습니다. 그리고 확산이 여러 놀라운 방식으로 활용되는 사례는 다음에서 더 읽을 수 있습니다:

*[경찰과 도둑](https://plus.maths.org/content/crime-1)*, *[표범이 어떻게 점무늬를 갖게 되었는가](https://plus.maths.org/content/how-leopard-got-its-spots)*, *[먹고 마시고 즐기자](https://plus.maths.org/content/eat-drink-and-be-merry-0)*

*이 확산 입문은 Carola Bibiane Schönlieb의 논문 **Restoring Profanity**와 Thomas Woolley, Ruth Baker, Eamonn Gaffney, Phillip Maini의 논문 **How long can we survive a zombie invasion**?을 바탕으로 합니다. 차 이미지는 Petr Kratochvil이 촬영했으며 퍼블릭 도메인입니다.*

*이 글은 **아이작 뉴턴 수학과학연구소(Isaac Newton Institute for Mathematical Sciences, INI)**와의 협업의 일부입니다. 협업에서 나온 모든 콘텐츠는 **여기**에서 찾을 수 있습니다.*

*INI는 국제 연구 센터이자 케임브리지 대학교 수학 캠퍼스에 있는 우리의 이웃입니다. 전 세계의 주요 수리과학자들을 끌어들이며 모두에게 열려 있습니다. 자세한 내용은 **www.newton.ac.uk**을 방문하세요.*

![INI 로고](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)