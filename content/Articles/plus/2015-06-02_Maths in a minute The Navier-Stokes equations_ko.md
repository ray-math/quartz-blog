---
title: "1분 수학: 나비에-스토크스 방정식"
date: 2015-06-02
tags:
  - 방정식
  - 유체
  - Institute
  - 점성
  - Stokes
  - 스토크
  - 나비
  - 액체
---

> [!NOTE]
> https://plus.maths.org/content/maths-minute-navier-stokes-equations
>
> 난류에 관한 수학적 난제

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/frontpage_3.jpg?itok=zFBlvwvB)

난류(turbulence)는 극적이고, 아름다우며, 잠재적으로 위험하다. 난류는 액체에서 일어나기도 하는데, 부서지는 파도나 격렬한 강물을 떠올려 보라. 기체에서도 일어나는데, 예를 들어 자동차나 비행기 주위를 흐르는 공기를 생각해 보면 된다. 본질적으로, 난류는 기술하기가 매우 어렵다. 난류 흐름에서 물의 속도와 방향을 측정하면, 서로 매우 가까운 점들에서도 완전히 다른 값을 얻을 수 있다.

![Waterfalls](https://plus.maths.org/issue48/features/markowich/Water2.jpg)

난류 상태의 물: 브라질과 아르헨티나 국경의 이과수 폭포. 사진: [Peter Markowich](http://homepage.univie.ac.at/peter.markowich/) (*Plus* 기사 [Universal pictures](https://plus.maths.org/content/universal-pictures) 참조).

> 난류는 유체 운동에서 가장 복잡한 현상 중 하나다. 층류(laminar flow)가 질서정연하게 평행한 층을 이루며 흐르는 것과 달리, 난류는 소용돌이(vortex)와 불규칙한 변동으로 가득 차 있다. 이러한 복잡성은 공간적으로 매우 작은 스케일에서도 나타나며, 이것이 난류를 수학적으로 다루기 어렵게 만드는 핵심 이유다. 흥미롭게도, 난류는 완전히 무작위한 것이 아니라 통계적 패턴을 보이는데, 이를 이해하는 것이 현대 유체역학의 주요 목표 중 하나다.

이러한 복잡성에도 불구하고, 과학자들은 유체 흐름이 **나비에-스토크스 방정식(Navier-Stokes equations)**에 의해 합리적인 수준의 정확도로 기술된다고 믿는다. 액체나 기체의 운동을 기술하려고 할 때, 우리가 구하고자 하는 것은 공간상의 점 $(x,y,z)$와 시각 $t$에서 액체의 속도 $v(x,y,z,t)$와 압력 $P(x,y,z,t)$이다. 물리학자 [클로드-루이 나비에(Claude-Louis Navier)](http://www-groups.dcs.st-and.ac.uk/~history/Biographies/Navier.html)와 [조지 가브리엘 스토크스(George Gabriel Stokes)](http://www-history.mcs.st-andrews.ac.uk/Biographies/Stokes.html)의 이름을 딴 나비에-스토크스 방정식은, 속도의 변화, 압력의 변화, 그리고 액체의 점성(viscosity)을 연결하는 **연립 편미분방정식(coupled partial differential equations)** 체계다. 함수 $v$와 $P$를 찾기 위해서는, 이 방정식들을 풀어야 한다.

> 편미분방정식(PDE)은 여러 변수를 가진 미지함수의 편미분을 포함하는 방정식이다. 나비에-스토크스 방정식이 '연립'이라는 것은 속도와 압력이 서로 독립적이지 않고 상호 의존적으로 결정된다는 의미다. 이는 한 방정식을 따로 떼어서 풀 수 없고, 전체 시스템을 동시에 고려해야 한다는 뜻이다. 점성은 유체의 '끈적임'을 나타내는 물리량으로, 꿀처럼 점성이 높은 유체는 천천히 흐르고, 물처럼 점성이 낮은 유체는 빠르게 흐른다. 방정식에서 점성은 유체 내부의 마찰력으로 작용하여 운동 에너지를 열로 소산시킨다.

하지만 그것은 결코 쉬운 일이 아니다. 방정식의 정확한 해(exact solutions) - 수학적 공식으로 명시적으로 쓸 수 있는 해 - 는 물리적으로 흥미롭지 않거나 실용성이 거의 없는 단순화된 문제들에 대해서만 존재한다. 대부분의 실용적 목적을 위해서는, 근사 해가 컴퓨터 시뮬레이션을 통해 - 본질적으로 교육받은 추측(educated guess-work)을 통해 - 구해지는데, 이는 엄청난 계산 능력을 요구한다.

> 현재까지 알려진 정확한 해석해(analytical solution)는 극히 제한적이다. 예를 들어, 두 평행한 평판 사이의 정상 유동(Poiseuille flow)이나 원통 주위의 특정 대칭 유동 같은 경우다. 이런 문제들은 기하학적으로 매우 단순하고 경계 조건이 특별해서, 실제 공학 문제와는 거리가 멀다. 현대의 컴퓨터 시뮬레이션은 유한요소법(finite element method)이나 유한차분법(finite difference method) 같은 수치해석 기법을 사용한다. 이들은 연속적인 유체를 이산적인 격자점들로 근사하고, 미분방정식을 대수방정식으로 변환하여 푼다. 슈퍼컴퓨터로도 며칠씩 걸리는 계산이 흔하다.

가장 일반적인 형태의 방정식에 대해 정확한 수학적 해가 존재하는지조차 아무도 모른다. 그리고 만약 해가 존재한다고 하더라도, 그 해가 불연속(discontinuities)이나 무한대(infinities) 같은 기이한 특성들을 포함하는지 - 액체가 어떻게 행동해야 하는지에 대한 우리의 직관과 맞지 않는 - 우리는 여전히 알지 못한다. 이 질문에 대한 답은 [클레이 수학연구소(Clay Mathematics Institute)](http://www.claymath.org/millenium-problems/navier-stokes-equation)로부터 백만 달러의 상금을 받을 수 있게 해 준다.

> 이것이 바로 유명한 '밀레니엄 문제(Millennium Prize Problems)' 중 하나다. 클레이 연구소는 2000년에 수학의 가장 중요하고 어려운 7개 문제를 선정하고, 각 문제당 100만 달러의 상금을 내걸었다. 나비에-스토크스 문제의 핵심은 두 가지다: (1) 매끄러운 초기 조건과 경계 조건이 주어졌을 때, 3차원 공간에서 모든 시간에 대해 매끄러운 해가 존재하는가? (2) 만약 존재한다면, 해가 물리적으로 합리적인가 (즉, 에너지가 유한한가)? 놀랍게도, 2차원의 경우 이 문제는 이미 증명되었지만, 3차원은 본질적으로 다른 수학적 구조를 가지고 있어 여전히 미해결 상태다. 이는 단순한 차원의 차이가 아니라, 3차원에서만 나타나는 소용돌이의 복잡한 상호작용 때문이다.

나비에-스토크스 방정식과 그 다양한 응용 - 공기역학적으로 안정적인 축구공 설계부터 날씨 예측까지 - 에 대해 더 알고 싶다면, [이곳의](https://plus.maths.org/content/taxonomy/term/13) *Plus* 기사들을 참조하라.

다음은 방정식의 완전한 형태다:

### 나비에-스토크스 방정식

공간상의 점 $(x,y,z)$에서, 속도 $\mathbf{v}(x,y,z)$는 세 개의 성분 $(u,v,w)$를 가지며, 각 좌표에 대해 하나씩이다. 액체의 압력은 $P(x,y,z)$이다. 깊게 숨을 들이쉬어 보라. 여기 방정식들이 있다:

![Navier-Stokes equations](https://plus.maths.org/issue48/features/markowich/navier2.gif)

방정식의 매개변수 $\text{Re}$는 **레이놀즈 수(Reynolds number)**라고 불리며, 액체의 점성을 측정한다.

> 레이놀즈 수는 유체역학에서 가장 중요한 무차원 수(dimensionless number) 중 하나다. 이는 관성력(inertial force)과 점성력(viscous force)의 비율을 나타낸다: $\text{Re} = \frac{\rho v L}{\mu}$, 여기서 $\rho$는 밀도, $v$는 특성 속도, $L$은 특성 길이, $\mu$는 동점성 계수다. 레이놀즈 수가 작으면 점성력이 지배적이어서 층류가 나타나고, 크면 관성력이 지배적이어서 난류가 발생한다. 임계값은 유동의 기하학적 형태에 따라 다르지만, 대략 $\text{Re} > 2000$이면 난류 전이(turbulent transition)가 시작된다. 흥미롭게도, 같은 유체라도 스케일이 달라지면 레이놀즈 수가 변하므로, 곤충이 보는 공기와 비행기가 보는 공기는 완전히 다른 유체처럼 행동한다. 이것이 바로 스케일 의존성(scale dependence)이며, 유체역학의 핵심 통찰이다.

> 위 이미지의 방정식을 자세히 살펴보면, 첫 번째 방정식은 **운동량 보존 방정식(momentum equation)**으로, 뉴턴의 제2법칙 $\mathbf{F} = m\mathbf{a}$의 유체역학 버전이다. 좌변은 유체 입자의 가속도를 나타내는데, 단순한 시간 미분이 아니라 이동하는 유체를 따라가며 보는 '물질 도함수(material derivative)' $\frac{D\mathbf{v}}{Dt} = \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla)\mathbf{v}$로 표현된다. 우변은 압력 구배에 의한 힘과 점성에 의한 마찰력을 나타낸다. 두 번째 방정식은 **연속 방정식(continuity equation)**으로, 질량 보존 법칙을 표현한다: $\nabla \cdot \mathbf{v} = 0$은 비압축성(incompressibility) 조건으로, 유체의 밀도가 일정함을 의미한다. 이 두 방정식이 결합되어 유체의 속도와 압력을 완전히 결정한다.

*이 기사는 현재 아이작 뉴턴 수리과학연구소(Isaac Newton Institute for Mathematical Sciences, INI)와의 협력의 일부를 이루고 있다 - 우리의 협력에서 나온 모든 콘텐츠는 여기서 찾을 수 있다. INI는 국제 연구 센터이며 케임브리지 대학교의 수학 캠퍼스에 있는 우리의 이웃이다. 전 세계의 저명한 수리과학자들을 끌어들이며, 모두에게 열려 있다. 더 알아보려면 www.newton.ac.uk을 방문하라.*

![INI logo](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)