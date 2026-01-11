---
title: COVID-19의 세대 시간 이해하기
date: 2021-12-21
---

> [!NOTE]
> https://plus.maths.org/content/understanding-generation-time-covid-19
>
> 한 사람이 다른 사람을 감염시키는 데 걸리는 시간은 얼마나 될까?

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/clock_frontpage_3.jpg?itok=H353nYw1)

바이러스에 감염된 사람이 다른 사람을 감염시키는 데 얼마나 걸릴까? 한 번의 감염이 다음 감염을 일으키는 데 걸리는 시간은 얼마나 될까? 이 질문에 답하려면 바이러스가 작동하는 모든 수준에 대한 지식이 필요하다. 우리 몸 안에서 바이러스가 어떻게 행동하는지, 한 사람에서 다른 사람으로 어떻게 전파되는지, 그리고 질병이 전체 집단에 걸쳐 어떻게 행동하는지에 대한 이해가 모두 필요하다. 이러한 복합성 때문에 바이러스의 세대 시간은 매혹적이면서도 도전적인 연구 분야가 된다.

> 세대 시간(generation time)은 역학(epidemiology)에서 핵심적인 개념 중 하나다. 이는 단순히 "감염 후 며칠이 지나면 다른 사람을 감염시킬 수 있는가"라는 질문을 넘어서, 질병의 전파 동역학을 정량적으로 이해하는 데 필수적인 매개변수다. 예를 들어, 세대 시간이 짧을수록 질병은 더 빠르게 확산되며, 이는 공중보건 개입 전략의 시간적 여유를 결정짓는다. 또한 세대 시간은 재생산지수 $R$의 계산에 직접적으로 영향을 미치므로, 잘못 추정된 세대 시간은 방역 정책의 오판으로 이어질 수 있다. 이처럼 세대 시간은 생물학적, 행동학적, 역학적 요소가 모두 얽혀 있는 복합적인 양이다.

![Julia Gog](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2017/Women/Julia_small.jpg)

Julia Gog. 사진: [Henry Kenyon](http://henrykenyonphotography.com).

COVID-19의 세대 시간을 이해하는 것은 올해 여름 [Newton Gateway to Mathematics](https://gateway.newton.ac.uk/event/tgm100)가 [RAMP Continuity Network](https://gateway.newton.ac.uk/news/2021-02-10/10378)의 일환으로 개최한 가상 행사의 주제였다. 이 행사는 [JUNIPER 모델링 컨소시엄](https://maths.org/juniper/)의 창립 멤버인 [Julia Gog](https://www.infectiousdisease.cam.ac.uk/directory/jrg20@cam.ac.uk)의 발상이었다. Gog는 현재 진행 중인 팬데믹 상황에서 바이러스의 세대 시간을 이해하는 것의 도전과 기회에 대한 훌륭한 개요로 무대를 열었다. (그녀의 강연은 [여기](https://gateway.newton.ac.uk/presentation/2021-07-28/33247)에서 온라인으로 볼 수 있다.)

이 행사는 세대 시간을 이해하는 데 관련된 다양한 분야에서 일하는 사람들을 한자리에 모았다. 개인 내에서 감염이 어떻게 행동하는지 연구하는 임상의와 연구자들(소위 *숙주 내(within-host)* 수준), 우리의 행동과 물리적 환경이 질병의 확산에 어떻게 영향을 미치는지 이해하려는 과학자들(*숙주 간(between-host)* 수준), 그리고 전체 집단에 걸쳐 질병의 동역학을 모델링하는 연구자들이 참석했다. "저는 이 회의가 매우 기대됩니다"라고 Gog는 말했다. "우리는 각자 일부 분야의 전문가들이지만, 여기서 교차하는 모든 분야의 전문가는 아무도 없습니다. 그리고 [이러한 전문성을] 하나로 모으는 것이 마법이 일어나는 곳입니다!"

### 세대 시간이란 무엇이며 왜 중요한가?

세대 시간은 특정 바이러스에 대한 단일한 숫자가 아니다. 대신 이것은 사람들의 쌍, 즉 감염시킨 사람(infector)과 그들이 감염시킨 피감염자(infectee)에 대해 정의된다. 한 사람이 감염된 시점(감염자)과 그들이 다른 사람을 감염시킨 시점(피감염자) 사이의 세대 시간은 다른 쌍의 사람들에 대해 다를 것이다.

![Generation time](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/generation_time/stick-people2.png)

감염자(파란색)와 피감염자(보라색). 빨간색 구간은 세대 시간을 나타내고 주황색 구간은 직렬 시간(serial time)을 나타낸다.

> 직렬 시간(serial interval 또는 serial time)은 세대 시간과 혼동하기 쉬운 개념이다. 직렬 시간은 감염자가 증상을 보인 시점과 피감염자가 증상을 보인 시점 사이의 시간 간격이다. 반면 세대 시간은 감염자가 감염된 시점과 피감염자가 감염된 시점 사이의 간격이다. 두 개념의 차이는 미묘하지만 중요하다. 증상 발현 시점은 관찰 가능하지만, 정확한 감염 시점은 대부분 알 수 없기 때문에 실제로는 직렬 시간을 측정하고 이로부터 세대 시간을 추론해야 한다. 잠복기(incubation period)가 존재하는 질병의 경우, 직렬 시간과 세대 시간은 체계적으로 다를 수 있으며, 특히 COVID-19처럼 증상 전 전파(presymptomatic transmission)가 가능한 경우 직렬 시간이 세대 시간보다 짧을 수도 있다.

또한 세대 시간을 직접 측정하는 것은 어렵다. 대신 감염자와 피감염자가 증상을 나타내는 시간 간격(만약 증상이 나타난다면 — 많은 감염은 무증상이다)과 같이 직접 관찰할 수 있는 것들로부터 추론해야 한다. 따라서 어떤 질병을 모델링할 때 세대 시간에 대한 가정을 하는 것은 불가피하다.

COVID-19 팬데믹에 대한 모든 기사는 [여기](https://plus.maths.org/content/tags/covid-19)에서 볼 수 있다.

역학자들은 평균 세대 시간과 같은 통계적 측도를 바이러스가 어떻게 행동할 것인지에 대한 모델 내의 매개변수로 사용한다. 특히 이러한 매개변수들은 재생산지수 $R$의 값을 계산하는 데 사용되며, 세대 시간에 대한 잘못된 가정은 $R$ 값을 과소평가하거나 과대평가하는 결과를 초래할 수 있다.

> 재생산지수 $R$은 한 감염자가 평균적으로 몇 명을 감염시키는지를 나타내는 지표다. $R > 1$이면 감염이 확산되고, $R < 1$이면 감염이 줄어든다. $R$을 계산하는 공식은 여러 가지가 있지만, 가장 단순한 형태에서 $R$은 세대 시간과 감염 기간, 그리고 전파 확률에 의존한다. 예를 들어, 초기 성장률 $r$로부터 $R$을 추정할 때는 $R \approx 1 + rT_g$ (여기서 $T_g$는 평균 세대 시간)와 같은 근사식을 사용할 수 있다. 따라서 $T_g$를 잘못 추정하면 $R$도 잘못 계산되어, 방역 조치의 강도를 잘못 설정하게 된다. 예를 들어, 실제 세대 시간이 5일인데 7일로 잘못 가정하면, $R$을 실제보다 낮게 추정하여 필요한 개입의 강도를 과소평가할 수 있다.

COVID-19의 세대 시간, 그것이 어떻게 추정되는지, 그리고 $R$ 계산에 미치는 영향에 대한 모든 것은 우리의 설명 기사 [COVID-19의 세대 시간이 중요한 이유](https://plus.maths.org/content/why-generation-time-covid-19-important)에서 찾을 수 있다.

### 우리 안에서, 우리 사이에서, 우리 모두에게

세대 시간의 가능한 값들은 바이러스의 숙주 내, 숙주 간, 그리고 집단 전체 행동에 의해 결정된다. Newton Gateway에서 열린 행사에서의 강연에서 Gog는 이 모든 수준에서 수행된 작업들을 강조했다. "실제로 이 세 가지 모두를 생각하지 않고서는 세대 시간을 이해할 수 없다고 생각합니다."

질병이 어떻게 행동하는지에 대한 숙주 내 모델은 집단 전체 모델만큼 발전하지 않았지만, HIV와 다른 만성 질환에 대해서는 일부가 더 발전되어 있다. [전체 집단에 사용되는 것](https://plus.maths.org/content/mathematics-diseases)과 유사한 모델을 사용하여 일부 간단한 모델링이 수행되었는데, 예를 들어 말에서의 인플루엔자 동역학을 이해하기 위한 것이다. 그러나 숙주 내 모델링을 매우 어렵게 만드는 것 중 하나는 질병의 진행을 측정하는 것이 매우 어렵다는 점이다. "이런 종류의 실험을 수행하는 것은 매우 어렵고 드뭅니다"라고 Gog는 말한다. "수학은 집단 수준 모델과 같은 수학일 수 있지만, 이러한 모델을 관찰에 맞게 보정하고 적응시키는 것은 극도로 도전적이며 그것이 이 분야가 그렇게 발전하지 못한 이유 중 하나입니다." (Isaac Newton Institute의 [Infectious Disease Dynamics 2015 프로그램](https://www.newton.ac.uk/event/idd/)에서 나온 Gog의 [논문](https://www.sciencedirect.com/science/article/pii/S1755436514000589)에서 더 읽을 수 있다.)

> 숙주 내 모델링이 어려운 이유는 여러 가지가 있다. 첫째, 바이러스의 농도, 면역 반응의 강도, 세포 손상의 정도 등을 시간에 따라 추적하려면 반복적인 침습적 검사가 필요한데, 이는 윤리적으로나 실용적으로 제한된다. 둘째, 개인 간 변이가 크다. 같은 바이러스라도 사람마다 면역 체계, 기저 질환, 유전적 요인이 다르기 때문에 반응이 천차만별이다. 셋째, 숙주 내에서 일어나는 과정은 매우 복잡하다. 바이러스 복제, 선천 면역 반응, 적응 면역 반응, 조직 손상과 회복 등 수많은 과정이 상호작용하며, 이들 각각이 비선형적인 동역학을 보인다. 이러한 복잡성 때문에 숙주 내 모델은 종종 많은 매개변수를 가지며, 이 매개변수들을 추정하기 위한 데이터는 부족한 경우가 많다.

숙주 간 동역학을 이해하는 주요 요인 중 하나는 질병의 전파 경로를 이해하는 것에서 나온다. COVID-19의 경우 이는 COVID-19의 공기 전파 특성과 우리의 건물과 공공 공간이 질병의 확산에 어떻게 영향을 미칠 수 있는지를 이해하는 것을 의미한다. 이는 [Catherine Noakes](https://eps.leeds.ac.uk/civil-engineering/staff/169/professor-catherine-noakes)와 같은 유체역학자들의 전문성을 필요로 하는데, 그녀는 [과학자문비상그룹](https://www.gov.uk/government/groups/scientific-advisory-group-for-emergencies-sage-coronavirus-covid-19-response) (SAGE)의 참여자로서 영국의 COVID-19 대응 노력에서 주도적인 역할을 해왔으며, Gateway 행사에서도 연사로 참여했다. (Noakes의 COVID-19 작업에 대한 더 자세한 내용은 [신선한 공기 한 숨](https://plus.maths.org/content/breath-fresh-air)에서 읽을 수 있다.)

![마스크 없이 숨쉬기, 말하기, 웃기](https://plus.maths.org/content/sites/plus.maths.org/files/news/2020/ventilation/no_mask.jpg)

마스크 없이 숨쉬기, 말하기, 웃기. 이미지 출처: Bhagat, Davies Wykes, Dalziel, Linden의 [실내 COVID-19 확산에 대한 환기의 영향](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/effects-of-ventilation-on-the-indoor-spread-of-covid19/CF272DAD7C27DC44F6A9393B0519CAE3), Journal of Fluid Mechanics, 903, F1.

> 공기 중 전파는 COVID-19 팬데믹 초기에는 과소평가되었지만, 이제는 주요 전파 경로로 인정받고 있다. 사람들이 숨을 쉬거나 말하거나 기침할 때, 다양한 크기의 비말(droplet)과 에어로졸(aerosol)이 방출된다. 큰 비말은 빠르게 떨어지지만, 작은 에어로졸 입자(일반적으로 직경 5μm 이하)는 공기 중에 오랫동안 부유하며 멀리까지 이동할 수 있다. 실내 환경에서는 환기가 불충분하면 이러한 에어로졸이 축적되어 감염 위험이 증가한다. 유체역학 모델은 공기 흐름, 환기율, 입자 크기 분포, 증발과 침강 등을 고려하여 실내 공간에서 바이러스 입자가 어떻게 확산되는지 예측한다. 이러한 이해는 마스크 착용, 환기 개선, 공기 정화 같은 개입 조치의 효과를 정량적으로 평가하는 데 필수적이다.

이러한 다양한 수준에서의 질병 행동에 대한 우리의 이해를 연결할 수 있다면, 이 지식을 집단 전체의 역학 모델에 내장할 수 있을 것이다. "제게 이 회의는 세대 시간을 더 잘 이해한다는 점에서 그 자체로 중요합니다. 왜냐하면 그것이 우리가 하고 있는 일에서 매우 중요하기 때문입니다"라고 Gog는 말한다. 그녀는 [과학적 팬데믹 인플루엔자 모델링 소그룹](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling) (SPI-M)과 SAGE에서의 역할을 통해 COVID-19 모델링 작업에 참여하고 있다. Gog는 또한 이러한 연결이 면역력 감소와 바이러스 진화를 이해하는 데 도움이 될 것이라고 믿는다.

> 면역력 감소(waning immunity)와 바이러스 진화는 팬데믹의 장기적 동역학을 결정하는 중요한 요인들이다. 감염이나 백신 접종 후 시간이 지나면서 항체 수준이 감소하고 면역 반응이 약해지는데, 이 감소 속도는 세대 시간과 상호작용하여 재감염의 패턴을 결정한다. 만약 면역력이 빠르게 감소하고 세대 시간이 짧다면, 감염 파동이 더 자주 일어날 수 있다. 또한 바이러스는 돌연변이를 통해 진화하는데, 새로운 변이는 전파력이나 면역 회피 능력에서 차이를 보일 수 있다. 예를 들어, 오미크론 변이는 이전 변이들보다 짧은 세대 시간을 가지는 것으로 추정되어, 더 빠른 확산을 설명하는 데 도움이 된다. 숙주 내 바이러스 동역학, 숙주 간 전파, 그리고 집단 수준의 면역 풍경을 통합적으로 이해해야만 이러한 복잡한 현상들을 예측할 수 있다.

"하지만 더욱 흥미로운 것은 이 세 가지 수준을 함께 연결하고, 이러한 다른 분야의 전문성을 가진 우리가 함께 대화하는 것입니다. 각 수준만으로는 전체 이야기가 아닙니다. 우리는 속담의 코끼리의 다른 부분들을 보고 있는 것입니다." 이와 같은 행사와 그것이 영감을 주는 작업과 협력은, 현재의 COVID-19 코끼리와 우리의 길을 가로지르는 미래의 팬데믹 후생동물들에 대한 더 나은 그림을 우리에게 제공하기를 바란다.

> "장님 코끼리 만지기(blind men and an elephant)"는 각자가 코끼리의 다른 부분(코, 다리, 꼬리 등)만 만져보고 전체를 다르게 이해하는 우화다. Gog는 이 비유를 통해 세대 시간을 이해하기 위해서는 다양한 학문적 관점이 필요함을 강조한다. 숙주 내 면역학자는 바이러스 복제 동역학을 보고, 유체역학자는 공기 중 입자의 움직임을 보고, 역학자는 집단 수준의 확산 패턴을 본다. 각 관점은 진실의 일부이지만, 전체 그림을 그리기 위해서는 이들을 통합해야 한다. 이것이 바로 학제간(interdisciplinary) 연구가 중요한 이유이며, 특히 COVID-19와 같은 복잡한 문제에서는 더욱 그렇다.

### 이 기사에 대하여

이 기사는 2021년 7월 Newton Gateway for Mathematics에서 열린 [COVID-19의 세대 시간 이해하기 행사](https://gateway.newton.ac.uk/event/tgm100)에서의 Julia Gog의 강연을 기반으로 한다.

Gog는 [JUNIPER](https://maths.org/juniper/) 모델링 컨소시엄의 창립 멤버이며, 결과를 [과학자문비상그룹](https://www.gov.uk/government/groups/scientific-advisory-group-for-emergencies-sage-coronavirus-covid-19-response) (SAGE)에 제공하는 모델링 그룹인 SPI-M의 멤버이자, COVID-19 팬데믹에 대응하기 위해 Royal Society가 주도하는 [국가 컨소시엄](https://epcced.github.io/ramp/)의 운영위원회 멤버이다.

[Rachel Thomas](https://plus.maths.org/content/people/index.html#rachel)는 *Plus*의 편집자다.

*이 기사는 JUNIPER(Joint UNIversity Pandemic and Epidemic Response 모델링 컨소시엄) 및 Isaac Newton Institute for Mathematical Sciences (INI)와의 협력의 일환으로 제작되었다.*

*JUNIPER는 Cambridge, Warwick, Bristol, Exeter, Oxford, Manchester, Lancaster 대학의 학자들로 구성되어 있으며, COVID-19의 통제에 관한 긴급한 질문들을 다루기 위해 다양한 수학적 및 통계적 기법을 사용하고 있다. JUNIPER와 함께 제작된 더 많은 콘텐츠는 여기에서 볼 수 있다.*

*INI는 국제 연구 센터이자 Cambridge 대학의 수학 캠퍼스에 있는 우리의 이웃이다. 전 세계의 선도적인 수학 과학자들을 유치하며, 모두에게 개방되어 있다. 더 자세한 정보는 www.newton.ac.uk에서 확인할 수 있다.*

![Juniper logo](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)

![INI logo](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)