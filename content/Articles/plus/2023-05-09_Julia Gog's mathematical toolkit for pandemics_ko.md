---
title: 팬데믹을 위한 줄리아 고그의 수학적 도구상자
date: 2023-05-09
tags:
  - Pandemic
  - Epidemic
  - Joint
  - JUNIPER
  - Response
  - 고그
  - 해악
  - 팬데믹
---

> [!NOTE]
> https://plus.maths.org/content/julia-gogs-mathematical-toolkit-pandemics
>
> 바이러스와 그에 맞선 우리의 조치들이 초래한 서로 다른 해악들을 어떻게 균형 잡아야 했는지에 대한 수학적이고 개인적인 고찰

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/Julia_frontpage2_0.jpeg?itok=HATNYicM)

[줄리아 고그(Julia Gog)](https://www.infectiousdisease.cam.ac.uk/directory/jrg20@cam.ac.uk) - 수리생물학(Mathematical Biology) 교수이자 *Plus*의 아주 좋은 친구 - 는 지난달 아이작 뉴턴 연구소에서 [케임브리지 페스티벌(Cambridge Festival)](https://www.newton.ac.uk/outreach/ongoing-initiatives/cambridge-festival/)을 위해 탁월한 강연을 진행했다.

> 수리생물학은 생물학적 현상을 수학적 모델로 기술하고 분석하는 학문 분야다. 특히 전염병 확산, 생태계 역학, 진화 과정 등을 미분방정식, 확률 과정, 네트워크 이론 등의 수학적 도구를 사용해 연구한다. 줄리아 고그 교수는 특히 인플루엔ザ와 같은 호흡기 감염병의 수학적 모델링 전문가로, COVID-19 팬데믹 동안 영국 정부의 과학자문위원회(SAGE)에서 핵심적인 역할을 수행했다. 수리생물학자들은 단순히 질병의 확산을 예측하는 것을 넘어, 다양한 방역 정책의 효과를 정량적으로 비교하고, 불확실성 하에서의 의사결정을 지원하는 중요한 역할을 담당한다.

이 강연에서 고그는 COVID-19 팬데믹 동안 우리 모두가 어떻게 서로 다른 해악들 - 바이러스 자체로부터의 해악과 바이러스에 맞서 우리 모두가 취한 조치들로부터의 해악 - 을 균형 잡아야 했는지를 수학적이면서도 개인적인 관점에서 살펴보았다. 이 강연을 시청하면, 개인에게 "최적"인 해법과 집단에게 최적인 해법이 매우 다를 수 있다는 것을 발견하게 될 것이다. 수학만으로는 우리에게 무엇을 해야 할지 말해줄 수 없지만, 우리의 사고를 틀지워주는(frame) 강력한 도구가 될 수 있다.

> 여기서 "개인의 최적"과 "집단의 최적" 사이의 차이는 게임 이론의 핵심 개념 중 하나다. 예를 들어, 팬데믹 상황에서 한 개인의 관점에서는 다른 사람들이 모두 백신을 맞아 집단면역이 형성된다면, 자신은 백신의 부작용 위험을 피하면서 보호받을 수 있다. 하지만 모든 사람이 이렇게 생각하면 집단면역은 달성되지 않고 모두가 위험해진다. 이는 "공유지의 비극(tragedy of the commons)"이나 "죄수의 딜레마(prisoner's dilemma)"와 유사한 구조다. 수학적 모델링은 이러한 개인 합리성과 집단 합리성 사이의 간극을 정량화하고, 어떤 정책이 이 간극을 좁힐 수 있는지 탐구하는 데 필수적이다. 예를 들어, $R_{0}$(기초감염재생산수)가 3인 질병의 경우, 집단면역을 위해서는 인구의 최소 $1 - 1/R_{0} = 2/3$가 면역을 획득해야 하지만, 개인의 자발적 선택만으로는 이 수준에 도달하기 어려울 수 있다.

우리는 고그 교수와 [JUNIPER](https://maths.org/juniper/) 모델링 컨소시엄의 동료들과 긴밀히 협력해왔다 - 그들의 연구에 대해 더 자세히 알고 싶다면 [여기](https://plus.maths.org/content/juniper)를 참조하라. 그리고 우리는 이 강연을 주최한 [아이작 뉴턴 수리과학연구소(Isaac Newton Institute)](https://www.newton.ac.uk/)와 협력하게 된 것을 매우 자랑스럽게 생각한다. INI와의 협력을 통해 제작된 모든 콘텐츠는 [여기](https://plus.maths.org/content/ini)에서 읽을 수 있다.

> JUNIPER(Joint UNIversity Pandemic and Epidemic Response)는 영국의 주요 대학들이 팬데믹 대응을 위해 결성한 연구 컨소시엄이다. 이러한 다기관 협력체의 형성은 현대 과학 연구의 중요한 특징을 보여준다. 복잡한 전염병 현상을 이해하려면 수학적 모델링, 통계학, 전산학, 역학, 공중보건학 등 다양한 전문성이 필요하며, 단일 기관이나 개인이 모든 측면을 다루기는 불가능하다. JUNIPER는 각 대학의 강점을 결합하여 신속하고 견고한 과학적 증거를 생산하고, 이를 정책 결정자들에게 제공하는 역할을 수행했다. 또한 연구 결과의 재현성과 투명성을 높이기 위해 많은 모델과 데이터를 공개했다는 점에서도 의미가 크다.

*이 영상은 JUNIPER(Joint UNIversity Pandemic and Epidemic Response 모델링 컨소시엄)와 아이작 뉴턴 수리과학연구소(INI)와의 협력의 일부를 형성한다.*

*JUNIPER는 케임브리지, 워릭, 브리스톨, 엑서터, 옥스퍼드, 맨체스터, 랭커스터 대학의 학자들로 구성되어 있으며, COVID-19의 통제에 관한 긴급한 질문들을 다루기 위해 다양한 수학적 및 통계적 기법을 사용하고 있다. JUNIPER와 함께 제작된 더 많은 콘텐츠는 [여기](https://plus.maths.org/content/juniper)에서 볼 수 있다.*

*INI는 국제 연구센터이자 케임브리지 대학교 수학 캠퍼스에 있는 우리의 이웃이다. 전 세계의 선도적인 수학 과학자들을 끌어들이며, 모두에게 열려 있다. 더 자세한 정보는 www.newton.ac.uk를 방문하라.*

> 아이작 뉴턴 수리과학연구소는 1992년에 설립된 국제적인 수학 연구 센터로, 순수수학과 응용수학의 경계를 넘나드는 학제간 연구를 촉진한다. 특히 특정 주제에 대한 장기 프로그램(보통 6개월)을 운영하여 전 세계의 전문가들이 한곳에 모여 집중적으로 협력 연구를 수행할 수 있도록 한다. COVID-19 팬데믹 동안 INI는 전염병 모델링 관련 여러 워크숍과 세미나를 개최하여 연구자들 간의 신속한 지식 교환을 가능하게 했다. 이러한 물리적, 지적 공간의 제공은 수학 연구의 발전에 있어 매우 중요한데, 서로 다른 배경을 가진 연구자들이 우연히 만나 대화하는 과정에서 예상치 못한 통찰이 탄생하는 경우가 많기 때문이다.

![Juniper 로고](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)

![INI 로고](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)