---
title: 무지개에서 괴물파까지
date: 2022-11-30
tags:
  - 파도
  - 분산
  - 조직
  - Moro
  - Gateway
  - El
  - Hoefer
  - 행사
---

> [!NOTE]
> https://plus.maths.org/content/rainbows-rogue-waves-1
>
> 케임브리지 아이작 뉴턴 연구소(INI)에서 탐구되고 있는 무지개, 괴물파, 그리고 더 많은 응용 분야의 매혹적인 수학을 발견하세요

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/front_icon_53.jpg?itok=lD3757YI)

무지개를 보고 경탄한 적이 있다면, 당신은 *분산(dispersion)*이 작용하는 것을 목격한 것입니다. 분산은 파동의 이동 속도가 그 진동수(frequency)와 파장(wavelength)에 의존하는 현상입니다. (파동과 그 진동수 및 파장에 대한 기본 소개는 [Why sine (and cosine) make waves](https://plus.maths.org/content/why-sine-and-cosine-make-waves)와 [Give us a wave](https://plus.maths.org/content/give-us-wave)에서 읽을 수 있습니다.)

> 분산은 단순히 파동이 퍼지는 것이 아니라, 파동을 구성하는 서로 다른 진동수 성분들이 서로 다른 속도로 전파되는 현상을 의미합니다. 예를 들어, 물결을 던졌을 때 긴 파장의 파도와 짧은 파장의 물결이 서로 다른 속도로 움직이는 것을 관찰할 수 있습니다. 수학적으로는 파동의 위상 속도(phase velocity)가 진동수의 함수로 표현되며, 이는 $v = v(\omega)$ 형태로 나타납니다. 분산이 있는 매질에서는 파동 패킷(wave packet)이 전파되면서 그 형태가 변하는데, 이것이 무지개나 광섬유 통신에서 중요한 역할을 합니다. 분산 관계식(dispersion relation)은 각진동수 $\omega$와 파수 $k$ 사이의 관계를 나타내며, 이는 해당 매질에서 파동의 동역학을 완전히 결정하는 핵심 정보입니다.

![프리즘을 통과하는 빛의 분산](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2022/HYD2/Light_dispersion_conceptual_waves.gif)

프리즘에 의해 분산되는 백색광의 서로 다른 파장들을 보여주는 그림. (이미지: [Lucas Vieira](https://en.wikipedia.org/wiki/Dispersion_(optics)#/media/File:Light_dispersion_conceptual_waves.gif) - 퍼블릭 도메인)

### 무지개

가장 친숙한 예는 백색광을 구성하는 서로 다른 색깔들이 유리 프리즘을 통과하거나 물방울 내부에서 반사될 때 굴절되어 무지개를 만드는 것입니다. 태양에서 온 빛이 진공(그리고 아주 좋은 근사로는 공기)을 통과할 때, 모든 진동수는 같은 속도 $c$, 대략 초당 300,000 km로 이동합니다. 그러나 물이나 유리 프리즘 내부에서 빛의 속도는 빛의 진동수(따라서 색깔)에 의존합니다. 물 속에서 서로 다른 색깔의 빛들 사이의 속도 차이는 매우 작지만, 이 작은 양의 분산도 태양광을 우리가 무지개에서 보는 아름다운 색 스펙트럼으로 분리하기에 충분합니다. (더 자세한 내용은 [Maths behind the rainbow](https://plus.maths.org/content/rainbows)와 분산에 대한 입문 [Maths in a minute: Dispersion](https://plus.maths.org/content/maths-minute-dispersion)에서 읽을 수 있습니다.)

> 무지개의 색 분리는 스넬의 법칙(Snell's law)과 매질의 굴절률(refractive index)이 파장에 따라 달라지는 현상의 결합으로 설명됩니다. 물의 굴절률 $n(\lambda)$는 파장 $\lambda$의 함수로, 짧은 파장의 보라색 빛이 긴 파장의 빨간색 빛보다 더 크게 굴절됩니다. 이 차이는 약 1.33(빨강)에서 1.34(보라)로 매우 작지만, 물방울에서 빛이 한 번 굴절하고 반사된 후 다시 굴절하면서 이 작은 차이가 증폭되어 약 42도(빨강)에서 40도(보라)의 각도 차이를 만들어냅니다. 이것이 무지개가 원호를 이루며 색깔별로 분리되어 보이는 이유입니다. 역사적으로 데카르트(Descartes)가 기하광학으로 무지개의 각도를 설명했고, 뉴턴(Newton)이 백색광이 여러 색의 조합임을 밝혔으며, 영(Young)의 파동 이론이 빛의 진동수와 파장 개념을 확립했습니다.

분산을 설명하는 수학은 복잡하고 매우 활발한 연구 분야입니다. 또한 유체역학(fluid dynamics)을 포함하여 많은 응용 분야를 가진 영역이기도 합니다. [아이작 뉴턴 연구소](https://www.newton.ac.uk/)(INI)에서 진행되는 6개월간의 [연구 프로그램](https://www.newton.ac.uk/event/hyd2/)의 조직자 중 한 명인 Mark Hoefer는 이를 설명합니다. "사람들은 수면파에서 새로운 실험을 하고 있으며, 새로운 관찰과 그것들을 이해하고 이러한 기법들을 적용하는 것에 대한 질문들이 있습니다"라고 Hoefer는 말합니다. 또 다른 큰 분야는 [비선형 광학(nonlinear optics)](https://en.wikipedia.org/wiki/Nonlinear_optics)으로, 레이저, 통신, 정보 처리를 개선하는 응용이 있습니다.

> 비선형 광학은 빛의 세기가 매우 강할 때 나타나는 현상으로, 매질의 광학적 성질 자체가 빛의 세기에 의존하게 됩니다. 일반적인 선형 광학에서는 중첩의 원리(superposition principle)가 성립하여 두 빛이 간섭 없이 투과하지만, 비선형 광학에서는 빛들이 서로 상호작용하여 새로운 진동수의 빛을 생성하거나 자기 집속(self-focusing) 같은 현상이 발생합니다. 이는 매질의 분극(polarization) $P$가 전기장 $E$의 고차 항을 포함하는 $P = \epsilon_{0}(\chi^{(1)} E + \chi^{(2)} E^{2} + \chi^{(3)} E^{3} + \cdots)$로 표현되기 때문입니다. 레이저 통신에서는 광섬유의 비선형 효과와 분산을 동시에 고려해야 하며, 이 두 효과의 균형이 솔리톤(soliton)이라는 특별한 파동을 만들어내어 장거리 정보 전송을 가능하게 합니다.

"우리 프로그램은 매우 광범위하고 학제간 성격이 강하다는 점에서 상당히 주목할 만합니다"라고 프로그램의 또 다른 조직자인 Barbara Prinari는 말합니다. "이 프로그램은 일반적으로 대화하고 협력할 기회가 없는 서로 다른 커뮤니티의 사람들을 비교적 긴 기간 동안 함께 모을 것입니다. 그래서 우리는 분야 간 많은 교류를 확실히 기대하고 있습니다."

이에 대한 좋은 예가 최근 개최된 [From Dispersive Hydrodynamics to Forecasting, Machine Learning and Back](https://gateway.newton.ac.uk/event/ofbw54) 행사입니다. [Newton Gateway to Mathematics](https://gateway.newton.ac.uk/)가 조직한 이 *Open For Business* 행사는 수학 외부의 응용 분야에서 일하는 사람들을 INI 프로그램에 참여하는 연구자들과 함께 모으는 것을 목표로 합니다. 이 행사는 [과학 워크숍](https://www.newton.ac.uk/event/hy2w04/)에 직접 이어져 구축되었고, 기상학자들과 기후 모델러들을 함께 모아 이 수학 분야의 기상 및 기후 예측과 해양학에 대한 응용에 초점을 맞췄습니다.

> INI의 프로그램 구조는 순수 수학적 연구와 실제 응용을 연결하는 독특한 방식을 보여줍니다. 일반적으로 수학자들과 응용과학자들은 서로 다른 학회에 참석하고 다른 저널에 논문을 발표하지만, INI는 6개월이라는 긴 기간 동안 이들을 한 공간에 모아 지속적인 상호작용을 가능하게 합니다. 이는 단순한 학술대회가 아니라, 연구자들이 실제로 함께 거주하며 매일 비공식적으로도 교류할 수 있는 환경을 제공합니다. 역사적으로 많은 수학적 돌파구가 이러한 학제간 협력에서 나왔으며, 예를 들어 나비에-스토크스 방정식(Navier-Stokes equations)도 물리학자와 수학자의 협력으로 발전했습니다. Open For Business 행사는 이를 한 단계 더 나아가 산업계 실무자들까지 포함시키는 시도입니다.

### 괴물파

"자연의 파도는 반드시 단순하지 않습니다"라고 프로그램의 또 다른 조직자인 Gennady El은 *Open For Business* 행사의 도입부에서 말했습니다. "우리는 *괴물파(rogue waves)*와 같은 실제 파동 현상을 예측하기 위한 새로운 방법이 필요합니다."

괴물파는 파괴적인 힘을 가진 거대한 단일 파도입니다. 그것들은 순간적으로만 존재하며 - 아무데서도 나타나지 않는 것처럼 보이고 빠르게 사라집니다. "대부분의 시간 동안 우리는 [괴물]파에 대한 어떤 증거도 가지고 있지 않습니다"라고 연사 중 한 명인 [유럽 중기 기상 예보 센터](https://www.ecmwf.int/)의 Peter Janssen은 말했습니다. "매우 변덕스러운 사건입니다." 그것들은 기껏해야 몇 초에서 몇 분 동안만 지속되어, 데이터를 포착할 수 있는 매우 짧은 시간을 주고 그 데이터도 제한적일 것입니다. "도전 과제는 이러한 사건의 발생에 대해 무언가를 말하는 것입니다."

> 괴물파는 주변 파도 높이의 2배 이상, 유의파고(significant wave height, 가장 높은 1/3 파도들의 평균)의 2.2배 이상으로 정의됩니다. 해양학에서 유의파고는 파도의 통계적 성질을 나타내는 중요한 지표로, 일반적으로 4미터의 유의파고는 상당히 거친 바다를 의미합니다. 괴물파의 수수께끼는 단순히 크기만이 아니라 그 출현의 예측 불가능성에 있습니다. 전통적인 해양 모델은 파도 높이가 레일리 분포(Rayleigh distribution)를 따른다고 가정했는데, 이는 극단적으로 높은 파도의 확률을 심각하게 과소평가합니다. 괴물파는 이 분포의 '꼬리(tail)'를 훨씬 벗어나는 사건으로, 이는 비선형 효과가 중요함을 시사합니다.

선원들이 수세기 동안 그것들을 보고했지만, 괴물파는 1995년에야 처음으로 과학적으로 기록되었습니다. Draupner 석유 시추 플랫폼은 20미터 파도를 견디도록 건설되었고, 그러한 파도는 10,000년에 한 번만 발생할 것으로 예측되었습니다. 그러나 1995년, 시추 플랫폼은 26미터 높이의 단일 파도에 휩쓸렸습니다. 시추 플랫폼의 플랫폼과 기저부에 있는 센서들이 이 순간적인 현상을 포착하여, 마침내 괴물파의 존재를 확인했습니다.

> Draupner 파도의 기록은 해양학 역사에서 전환점이었습니다. 그 이전까지 괴물파는 선원들의 과장된 이야기나 신화로 여겨졌으며, 과학계는 이를 진지하게 받아들이지 않았습니다. 1995년 1월 1일, 북해의 Draupner 플랫폼에서 기록된 데이터는 11미터의 유의파고를 가진 바다에서 최대 25.6미터의 파도가 측정되었음을 보여주었습니다. 이는 유의파고의 2.3배로, 명백한 괴물파였습니다. 더욱 중요한 것은 이 측정이 여러 센서에서 동시에 이루어져 신뢰성이 높았다는 점입니다. 이 데이터는 시간에 따른 수면 높이의 변화를 정확히 기록했고, 파도의 형태가 매우 비대칭적(steep front, gentle back)이었음을 보여주었습니다. 이는 선형 이론으로는 설명할 수 없는 특징입니다.

Draupner 파도 데이터와 그 이후 수집된 다른 실제 데이터는 해양학자들이 수학적 모델을 재고하게 만들었고, 그들은 이제 괴물파가 흔하다고 믿습니다. 전 세계 바다에서 언제든지 약 10개의 괴물파가 발생하고 있는 것으로 생각되며, 이제 그것들은 과거와 최근 역사에서 많은 선박 침몰의 원인으로 생각되고 있습니다.

괴물파가 어떻게 발생할 수 있는지를 설명하는 많은 경쟁하는 수학 이론들이 있습니다. 기본 아이디어는 서로 다른 해수면 파도들이 상호작용하여 그들의 정점이 일치하고 서로를 강화하여 더 가파른 파도를 만드는 방식입니다, 라고 Janssen은 말했습니다. "파동 에너지의 이 집속을 야기하는 여러 비선형 과정들이 있습니다." 이러한 비선형 효과는 특정 분산 조건으로부터 발생할 수 있으며, 파도가 일시적으로 이웃으로부터 에너지를 빌려올 수 있게 합니다. 이 새로운 이론적 이해는 해양에서 관찰된 괴물파 현상을 재현한 새로운 실험실 실험으로 이어졌습니다.

> 괴물파 형성의 주요 메커니즘은 변조 불안정성(modulational instability)과 비선형 집속(nonlinear focusing)입니다. 변조 불안정성은 Benjamin-Feir 불안정성으로도 알려져 있으며, 거의 단색인(monochromatic) 파동이 작은 섭동에 의해 불안정해져 에너지가 특정 위치에 집중되는 현상입니다. 이는 비선형 슈뢰딩거 방정식(nonlinear Schrödinger equation, NLS) $i\frac{\partial A}{\partial t} + \alpha \frac{\partial^{2} A}{\partial x^{2}} + \beta |A|^{2} A = 0$으로 모델링되며, 여기서 $A$는 파동의 복소 진폭입니다. 이 방정식은 솔리톤 해를 가지며, 특정 조건에서는 Peregrine 솔리톤이라는 시공간적으로 국소화된 해가 존재합니다. 이것이 괴물파의 수학적 프로토타입으로 여겨지며, 실험에서 실제로 재현되었습니다. 또한 교차하는 파도들(crossing seas)의 상호작용도 중요한 메커니즘으로, 서로 다른 방향에서 오는 파도들이 만날 때 건설적 간섭이 발생하여 극단적으로 높은 파도를 만들 수 있습니다.

![실험에서 재현된 괴물파](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2022/HYD2/Rogue_waves_McAllister_2019_web.png)

[2019년 Draupner 파도 시뮬레이션](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/laboratory-recreation-of-the-draupner-wave-and-the-role-of-breaking-in-crossing-seas/65EA3294DAFD97A50C8046140B45F759)의 이미지들은 파도의 가파름이 어떻게 형성되는지 보여줍니다. (이미지: [McAllister et al 2019](https://commons.wikimedia.org/wiki/File:Rogue_waves_breaking_behavior_at_different_crossing_angles,_McAllister_2019.png) - [CC BY 4.0](https://creativecommons.org/licenses/by/4.0))

> 실험실에서 괴물파를 재현하는 것은 이론 검증의 핵심 단계입니다. 2019년 McAllister 등의 연구는 University of Oxford의 파동 수조에서 Draupner 파도를 성공적으로 재현했습니다. 이들은 파동 생성기를 사용하여 서로 다른 각도에서 교차하는 파도 군(wave trains)을 만들어냈고, 특정 각도와 위상 관계에서 실제 Draupner 파도와 유사한 형태의 극단적인 파도가 형성됨을 보였습니다. 중요한 발견은 파도의 깨짐(wave breaking)이 중요한 역할을 한다는 것입니다. 선형 이론은 무한히 높은 파도를 예측할 수 있지만, 실제로는 파도가 특정 가파름(steepness, $H/\lambda$ 비율)을 초과하면 깨지면서 에너지를 소산시킵니다. 이 실험들은 또한 위상 잠금(phase-locking) 현상을 관찰했는데, 이는 파동 성분들이 일시적으로 동기화되어 에너지를 한 곳에 집중시키는 메커니즘입니다.

분산 유체역학(dispersive hydrodynamics)은 해양학에서 보이는 이러한 복잡한 행동과 기상 및 기후 모델링의 다른 현상을 이해하는 데 핵심적입니다. 이 모든 분야는 또한 방대한 양의 데이터를 동반하여, [기계 학습(machine learning)](https://plus.maths.org/content/maths-minute-machine-learning-and-neural-networks)이라는 인공지능의 한 형태를 적용할 명백한 기회를 제공합니다. "기계 학습은 모델링에 정보를 제공하는 데 점점 더 도움이 되고 있으며, 비선형 수학의 기법들이 신경망과 이에 기반한 알고리즘의 근본적인 행동을 이해하는 데 사용되고 있습니다"라고 프로그램 조직자 중 한 명인 Antonio Moro는 말합니다. "새로운 연구가 이론과 응용 모두에서 발전하고 있습니다."

> 기계 학습과 분산 유체역학의 만남은 양방향 흐름을 보여줍니다. 한편으로, 해양 관측 데이터(위성 고도계, 부표 측정 등)는 엄청난 양이지만 시공간적으로 드물게 분포되어 있어, 기계 학습 알고리즘이 이 데이터로부터 패턴을 추출하고 예측 모델을 개선할 수 있습니다. 예를 들어, 딥러닝 네트워크를 훈련시켜 위성 이미지로부터 괴물파가 발생할 가능성이 높은 해역을 식별할 수 있습니다. 다른 한편으로, 분산 유체역학의 수학적 통찰은 신경망 자체의 동역학을 이해하는 데 기여합니다. 심층 신경망의 훈련 과정은 손실 함수(loss function)의 최적화 문제로, 이는 고차원 공간에서의 비선형 동역학 시스템으로 볼 수 있습니다. 비선형 파동 이론의 도구들, 특히 해밀토니안 구조(Hamiltonian structure)와 적분 가능성(integrability) 개념이 이러한 시스템의 분석에 적용되고 있습니다.

### 새로운 수학, 새로운 실험, 새로운 연구자

이러한 학제간 교류는 INI 프로그램의 주요 기회 중 하나이며, 순수 및 응용 수학자들과 실험 물리학자들 간의 협력이 이루어진다고 El은 말합니다. "새로운 수학적 결과는 새로운 물리 실험을 제안합니다. 그리고 이것이 실제로 이 프로그램 동안 일어나고 있는 일입니다 - 새로운 협력이 이미 여기서 확립되고 있습니다."

유체역학적 분산은 비교적 새로운 분야이며, 프로그램의 핵심 측면은 또한 초기 경력 연구자들이 이 분야를 발전시킬 수 있도록 격려하고 지원하는 것입니다. "이 분야에서 떠오르는 스타들 간에 상호작용이 있습니다, 그들은 서로 대화하고 있으며 또한 선배들과도 대화하고 있습니다"라고 Shearer는 말합니다. "이것은 어떤 면에서 초기 단계에 있는 분야이지만 이에 대한 많은 흥분이 있으며, 따라서 [다음] 세대를 고무시킬 수 있다는 것은 훌륭합니다. 그들이 이 주제를 앞으로 나아가게 할 것입니다."

> 분산 유체역학의 역사는 비교적 짧지만 풍부합니다. 이 분야는 1960년대 Korteweg-de Vries(KdV) 방정식의 재발견과 솔리톤의 발견으로 시작되었습니다. KdV 방정식 $\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + \frac{\partial^{3} u}{\partial x^{3}} = 0$은 분산과 비선형성이 균형을 이루는 전형적인 모델입니다. 1967년 Gardner, Greene, Kruskal, Miura가 발견한 역산란 변환(inverse scattering transform)은 이 비선형 편미분방정식을 정확히 풀 수 있게 해주었고, 이는 수학의 혁명적 발전이었습니다. 이후 Zakharov-Shabat, Ablowitz-Kaup-Newell-Segur(AKNS) 등이 이 방법을 확장하여 많은 물리적으로 중요한 방정식들이 적분 가능함을 보였습니다. 최근에는 분산 충격파(dispersive shock waves)라는 새로운 구조가 발견되어 연구되고 있으며, 이는 고전적인 충격파와 달리 진동하는 전이 영역을 가집니다. 이 분야는 여전히 활발히 발전하고 있으며, 특히 다차원 문제와 무작위성(randomness)이 포함된 경우는 아직 많은 미해결 문제를 가지고 있어, 젊은 연구자들에게 매력적인 기회를 제공합니다.

### 이 글에 대하여

이 글은 아이작 뉴턴 수학과학 연구소가 주최하는 [분산 유체역학: 수학, 시뮬레이션 및 실험, 비선형 파동의 응용](https://www.newton.ac.uk/event/hyd2/) 프로그램에 대한 우리의 보도 내용의 일부로 제작되었습니다. 프로그램에 대한 더 많은 콘텐츠는 [여기](https://plus.maths.org/content/rainbows-rogue-waves-0)에서 찾을 수 있습니다.

이 글은 부분적으로 INI의 Dan Aspel이 조직자들인 Antonio Moro, Michael Shearer, Mark Hoefer, Gennady El, Barbara Prinari와 진행한 [인터뷰](https://www.youtube.com/watch?v=bL_kdvm0WXY&t=1s)와, 2022년 10월 24일에 Newton Gateway to Mathematics가 조직한 프로그램의 첫 번째 [Open For Business 행사](https://gateway.newton.ac.uk/event/ofbw54)를 기반으로 합니다.

[Rachel Thomas](https://plus.maths.org/content/people/index.html#rachel)는 *Plus*의 편집자입니다.

*이 글은 아이작 뉴턴 수학과학 연구소(INI)와의 협력의 일환으로 제작되었습니다 - 우리의 협력으로부터 나온 모든 콘텐츠를 여기에서 찾을 수 있습니다.
INI는 국제 연구 센터이며 케임브리지 대학교의 수학 캠퍼스에 있는 우리의 이웃입니다. 전 세계의 저명한 수학자들을 끌어모으며, 모두에게 열려 있습니다. 더 자세한 내용은 www.newton.ac.uk을 방문하세요.*

![INI 로고](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)