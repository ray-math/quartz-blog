---
title: "백신 접종: 현재 우리는 어디에 있고, 어디로 가고 있는가?"
date: 2021-04-01
---

> [!NOTE]
> https://plus.maths.org/content/vaccination-where-do-we-stand-and-where-are-we-going
>
> COVID-19 백신이 지금까지 우리를 어디까지 데려왔고, 백신 접종이 완료되면 우리가 어디에 있게 될 것인가?

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/vaccines_frontpage.jpg?itok=wgnEULdE)

영국의 COVID-19 백신 접종이 순조롭게 진행되고 있어 낙관할 만한 근거가 있는 것처럼 보입니다. 그러나 백신이 지금까지 우리를 어디까지 데려왔고, 접종이 완료되면 어디에 있게 될지 실제로 무엇을 말할 수 있을까요?

COVID-19 팬데믹에 대한 모든 보도는 [여기](https://plus.maths.org/content/tags/covid-19)에서 볼 수 있습니다.

[JUNIPER 모델링 컨소시엄](https://maths.org/juniper/)의 팀이 최근 수행한 [연구](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(21)00143-2/fulltext)는 몇 가지 통찰을 제공합니다. 이 연구는 백신 접종만으로는 COVID-19를 근절할 가능성이 매우 낮다고 제안합니다. 그러나 백신은 봉쇄에서 벗어나는 데 핵심적인 역할을 합니다. 이 연구는 여기서 신중함이 중요하다고 제안합니다. 규제 완화의 속도가 느릴수록 미래 감염 파동의 곡선이 더 평탄해집니다.

> 이 연구가 강조하는 핵심은 백신 접종이 단순히 "있으면 모든 것이 해결되는" 만능 해결책이 아니라는 점입니다. 수학적 모델링은 여러 변수들(백신 효능, 접종률, 규제 완화 속도 등)이 복합적으로 상호작용하여 결과를 만들어낸다는 것을 보여줍니다. 이는 역학(epidemiology)의 본질적인 특성으로, 질병 확산은 선형적이지 않고 비선형 동역학(nonlinear dynamics)을 따릅니다. 따라서 작은 정책 변화도 장기적으로 큰 차이를 만들 수 있으며, 이것이 바로 수학적 모델링이 정책 결정에 필수적인 이유입니다.

이 팀은 워릭 대학교(University of Warwick)의 역학자들로 구성되어 있습니다: Sam Moore, [Edward Hill](https://warwick.ac.uk/fac/sci/maths/people/staff/ed_hill/), [Michael Tildesley](https://warwick.ac.uk/fac/sci/lifesci/people/mtildesley/), [Louise Dyson](https://warwick.ac.uk/fac/sci/maths/people/staff/dyson/), 그리고 [Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/)입니다. 팀의 대부분은 [과학적 팬데믹 인플루엔자 모델링 그룹](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)(SPI-M)에 기여하고 있으며, Keeling은 [예방접종 및 면역 공동위원회](https://www.gov.uk/government/groups/joint-committee-on-vaccination-and-immunisation)의 위원이기도 합니다.

## 영국에서 배치된 백신은 얼마나 효과적인 것으로 입증되고 있는가?

팬데믹의 거의 모든 측면에는 많은 불확실성이 존재하며, 이는 백신에도 적용됩니다. 백신이 처음 승인되었을 때, [임상 시험](https://plus.maths.org/content/how-were-vaccines-tested)은 화이자/바이오엔텍(Pfizer/BioNTech)과 옥스퍼드/아스트라제네카(Oxford/AstraZeneca) 백신이 사용하기에 충분히 [안전](https://plus.maths.org/content/are-vaccines-safe)하고 효과적이라는 것을 보여주었지만, 백신이 얼마나 잘 작동하는지에 대한 정확한 수치는 많은 수의 사람들이 백신을 접종한 후에만 얻을 수 있습니다.

![Vaccine](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2020/vaccine/vaccine_normal.jpg)

접종이 시작된 이후 수집된 데이터는 더 명확한 그림을 제공했습니다. Keeling이 지난 주 아이작 뉴턴 연구소(Isaac Newton Institute)에서 주최한 [연구 발표](https://plus.maths.org/content/vaccination-where-do-we-stand-and-where-are-we-going#video)에서 보고한 바와 같이, 최신 추정치는 백신이 감염의 다른 측면에 대해 서로 다른 수준의 보호를 제공한다고 말합니다.

이상적으로는 백신이 사람들이 감염되는 것 자체를 막아야 하지만, 백신이 단지 증상 발현만 막을 수도 있습니다. 여기서 중요한 차이점은 증상만 막는 백신은 질병의 전파를 차단하지 못한다는 것입니다. 감염은 여전히 인구 내에서 순환할 수 있고, 백신을 접종할 수 없거나 접종하지 않으려는 사람들은 보호받지 못할 것입니다.

> 이 구분은 역학에서 매우 중요한 개념입니다. 백신의 효과를 측정할 때 우리는 여러 수준의 보호를 구분해야 합니다: (1) 감염 차단(sterilizing immunity) - 바이러스가 체내에 들어와도 증식하지 못함, (2) 질병 예방 - 감염되지만 증상이 없음, (3) 중증 질환 예방 - 증상은 있지만 입원이나 사망은 없음. 첫 번째가 가장 강력한 보호이며, 이것만이 집단 면역(herd immunity)에 기여할 수 있습니다. 만약 백신이 증상만 막는다면, 접종자는 무증상 전파자가 되어 다른 사람들에게 바이러스를 퍼뜨릴 수 있습니다. 이는 백신 효능을 단일 숫자로 표현하는 것이 오해를 불러일으킬 수 있는 이유입니다.

아직 확실할 만큼 충분한 데이터가 없지만, Keeling이 발표에서 보고한 수치는 낙관할 근거를 제공합니다. 백신은 사람들이 COVID-19에 감염되는 것 자체를 막는 데 50%에서 80% 사이의 효과가 있는 것으로 보이며, 따라서 전파를 차단하는 데도 그만큼의 효과가 있고, 중증 증상 발현을 막는 데는 약 90%의 효과가 있습니다.

백신의 효과는 1차 접종에서 2차 접종으로 갈수록 증가합니다. Keeling의 발표에서 그는 질병에 대한 보호 수준이 1차 접종 후 2주에 70%, 2차 접종 후 2주에 88%로 상승한다고 가정했습니다.

이 비율들은 높지만 최대치는 아니며, 이것이 백신 접종만으로는 COVID-19를 근절하지 못할 가능성이 높은 이유 중 하나입니다. "백신이 개인에게 제공하는 방패가 부분적이기 때문에, 일반 인구의 감염 수준 증가로 극복될 수 있습니다"라고 Keeling은 말합니다. 다시 말해, 일부 사람들은 백신을 접종했음에도 불구하고 COVID-19에 감염될 것이며, 일반 인구에 감염이 많을수록 이러한 백신 실패를 더 많이 보게 될 가능성이 높습니다.

> 이는 기초적인 확률 개념으로 이해할 수 있습니다. 백신의 효능이 80%라면, 백신 접종자가 바이러스에 노출될 때마다 20%의 확률로 감염됩니다. 만약 지역사회 내 바이러스 유행이 낮아서 백신 접종자가 1년에 바이러스에 10번만 노출된다면, 감염 확률은 $1 - (0.8)^{10} \approx 0.893$, 즉 약 10.7%입니다. 그러나 유행이 심해서 100번 노출된다면, 감염 확률은 $1 - (0.8)^{100}$로 거의 100%에 가까워집니다. 이것이 백신 접종률이 높더라도 지역사회 내 감염 수준이 높으면 "돌파 감염(breakthrough infection)"이 많이 발생하는 수학적 이유입니다. 따라서 백신 접종과 함께 감염 수준 자체를 낮게 유지하는 것이 중요합니다.

백신이 배포되기 전에 우리가 알 수 없었던 또 다른 것은 얼마나 많은 사람들이 백신 접종에 동의할 것인가 하는 점입니다. 그리고 여기서 숫자는 좋은 방향으로 기대를 초과합니다: 지금까지 60세 이상의 접종률은 95%입니다.

## 우리는 올바르게 하고 있는가?

JUNIPER 팀의 연구는 인구 집단의 어떤 그룹이 어떤 순서로 백신을 접종받을지, 그리고 두 번의 접종 사이에 얼마나 긴 간격을 둘지 모두에 있어서 백신이 어떻게 배포되어야 하는지를 알리는 데 도움이 되었습니다. 두 측면 모두에서 취할 수 있는 다양한 접근 방식이 있었습니다. 예를 들어, 노인과 취약 계층보다 사회적 접촉이 많은 사람들을 우선시하거나, 더 적은 사람들이 두 번의 접종을 빠르게 받도록 하는 대신 더 많은 사람들이 1차 접종을 빠르게 받도록 하는 것입니다.

JUNIPER 팀은 지난 여름부터 백신 전략을 살펴보기 시작했으며([여기](https://plus.maths.org/content/who-should-be-vaccinated-first) 참조), 다양한 가정 하에서 우리가 보게 될 가능성이 있는 확진자, 입원 및 사망자 수를 예측하는 수학적 모델을 사용했습니다. 물론 항상 불확실성이 있으므로, 이러한 모델의 결과를 확실한 예측으로 간주할 수는 없습니다. 대신 이러한 모델을 통해 "만약 이것이면 저것이다(if-this-then-that)" 방식으로 가능한 시나리오를 탐색할 수 있습니다. 백신 접종의 경우, 노인과 취약 계층을 우선시하는 것이 기본 가정이 달라지더라도 모델링에서 지속적으로 최적 전략으로 나타났습니다. 이것이 기본적으로 영국에서 채택된 전략입니다. (역학에서 사용되는 수학적 모델에 대해 더 알아보려면 [여기](https://plus.maths.org/content/how-can-maths-fight-pandemic)를 참조하세요.)

> 백신 접종 우선순위 결정은 복잡한 최적화 문제입니다. 목적 함수(objective function)를 무엇으로 설정하느냐에 따라 - 사망자 최소화, 감염자 최소화, 의료 시스템 부담 최소화 등 - 최적 전략이 달라질 수 있습니다. 노인 우선 접종은 치명률(case fatality rate, CFR)이 나이에 따라 기하급수적으로 증가한다는 사실에 기반합니다. 예를 들어, 80대의 CFR은 20대보다 약 100배 이상 높습니다. 반면, 사회적 접촉이 많은 젊은 층을 우선 접종하면 전체 감염 확산을 더 빠르게 억제할 수 있습니다. 이는 네트워크 이론(network theory)에서 높은 연결성을 가진 노드(hub)를 제거하는 것이 네트워크 붕괴에 더 효과적이라는 원리와 유사합니다. JUNIPER 팀의 모델링은 다양한 목적 함수와 제약 조건 하에서 노인 우선 접종이 가장 강건한(robust) 전략임을 보여주었습니다.

접종 간격에 관해서는, Hill과 Keeling의 [최근 연구](https://www.medrxiv.org/content/10.1101/2021.03.15.21253542v1.full.pdf)는 1차 접종을 우선시하는 것 - 더 적은 사람들에게 두 번의 접종을 모두 하는 것보다 가능한 한 많은 사람들에게 한 번의 접종을 하는 것 - 이 일반적으로 우리가 가진 백신과 백신 접종 능력에 대해 최선의 전략임을 제안합니다. 영국에서 채택된 정책은 여러 실용적 고려사항에 달려 있었습니다. 특히 옥스퍼드/아스트라제네카 백신이 12주 간격으로 접종했을 때 더 효과적이라는 사실이 중요했습니다. Hill과 Keeling의 연구는 이 전략이 사망자 수를 줄이는 측면에서도 이점이 있음을 보여줍니다.

> 접종 간격 최적화는 자원 할당(resource allocation) 문제의 한 형태입니다. 수학적으로 표현하면: 시간 $t$에서 총 $N(t)$개의 백신 용량이 있을 때, 이를 어떻게 분배해야 사망자 $D(T)$를 최소화할 것인가? 1차 접종 후 보호 효과가 $e_1$, 2차 접종 후 $e_2$일 때 ($e_1 < e_2$), 그리고 백신 생산이 제한적일 때, $e_1 \cdot n_1 + e_2 \cdot n_2$를 최대화하는 것이 단순한 목표가 될 수 있습니다. 여기서 $n_1$은 1차 접종자 수, $n_2$는 2차 접종 완료자 수입니다. 그러나 실제로는 시간 지연, 면역 형성 시간, 집단 면역 효과 등을 고려해야 하므로 동적 최적화(dynamic optimization) 문제가 됩니다. Hill과 Keeling의 연구는 영국의 12주 간격 전략이 이 복잡한 최적화 문제에 대한 좋은 해법임을 보여주었습니다.

## 우리는 어디로 가고 있는가?

수학적 모델은 미래에 일어날 수 있는 일을 탐색하는 데에도 사용될 수 있습니다. JUNIPER 팀이 사용한 모델은 상세하며, 예를 들어 인구의 연령 구조, 지리, B1.1.7 변이, 그리고 현재까지 누가 백신을 접종받았는지를 고려합니다. 이것은 과학자들이 매주 유명한 [재생산 지수 R](https://plus.maths.org/content/maths-minute-r0-and-herd-immunity)의 값을 계산하는 데 도움을 주는 모델 중 하나이기도 합니다. "전반적으로 [이 모델은] 현재까지 무슨 일이 일어나고 있는지에 대한 상당히 완전한 그림을 제공하도록 되어 있으며, 따라서 우리는 앞으로 시간이 흐르면서 무슨 일이 일어날지에 대한 합리적인 예측을 할 수 있기를 바랍니다. 물론 인간 행동에는 항상 불확실성이 있습니다"라고 Keeling은 말합니다.

> 재생산 지수 $R$은 감염된 한 사람이 평균적으로 몇 명을 감염시키는지를 나타내는 핵심 지표입니다. $R < 1$이면 유행이 소멸하고, $R > 1$이면 유행이 확산됩니다. $R = 1$은 유행이 일정 수준을 유지하는 임계점입니다. $R$의 값은 여러 요인에 의해 결정됩니다: $R = \beta \cdot c \cdot d \cdot s$로 표현할 수 있는데, 여기서 $\beta$는 접촉당 전파 확률, $c$는 일일 접촉 횟수, $d$는 감염 기간, $s$는 감수성 인구 비율입니다. 백신 접종은 주로 $s$를 감소시키고(사람들이 더 이상 감염에 취약하지 않음), 부분적으로 $\beta$도 감소시킵니다(백신이 전파를 차단하는 경우). 그러나 백신만으로 $R$을 1 이하로 낮추기 어렵다는 것은 다른 요인들($c$를 줄이는 사회적 거리두기 등)도 여전히 필요함을 의미합니다.

당신이 물어볼 수 있는 첫 번째 질문은 백신 접종이 $R$에 무엇을 하는가 하는 것입니다. 그리고 모델에 따르면, 그 답은 백신 접종 자체만으로는 $R$을 1 이하로 낮출 수 없다는 것입니다. "우리는 백신 접종이 $R$에 상당한 영향을 미칠 수 있는 상황에 있지만, 이 시뮬레이션에서 그것은 R을 1 이하로 낮추기에 충분하지 않습니다. 이것은 백신이 질병을 통제하는 데 잘 작동하고 있지만, 다른 통제 수단 없이는 질병을 근절할 수 있는 상황에 놓이게 하지 못한다는 것을 말하는 것입니다"라고 Keeling은 말합니다.

![백신 접종량이 증가함에 따른 R의 변화](https://plus.maths.org/content/sites/plus.maths.org/files/news/2021/vaccines/keeling_r.jpg)

이 그림은 어떠한 제한도 없는 상태에서 인구에서 더 많은 백신 용량이 투여됨에 따라 $R$의 값이 어떻게 변화할 것으로 추정되는지 보여줍니다. 네 개의 다른 선은 백신이 감염을 얼마나 예방하는지에 대한 네 가지 다른 가정에 해당하며, 범례에 표시되어 있습니다. JUNIPER 팀의 [논문](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(21)00143-2/fulltext)의 그림으로, *The Lancet*에 게재되었습니다.

팀은 또한 다양한 가정 하에서 규제를 완화하는 효과를 시뮬레이션했습니다. "우리가 [물어본] 첫 번째 것은, 만약 4월에 모든 것을 완전히 완화하면 어떻게 될까요?"라고 Keeling은 말합니다. "우리는 많은 수의 사망자와 입원으로 이어지는 절대적으로 거대한 발병으로 끝납니다. 4개월의 백신 접종 후에도 모든 통제를 중단하면 재앙적인 결과를 얻습니다."

![4월에 제한이 갑자기 해제된다면 COVID-19 일일 사망자 수](https://plus.maths.org/content/sites/plus.maths.org/files/news/2021/vaccines/keeling_april.jpg)

이 그림은 4월에 제한이 갑자기 해제된다면 COVID-19 일일 사망자 수에 무슨 일이 일어날지 탐색합니다. 다른 곡선들은 범례에 표시된 대로 백신이 감염을 예방하는 효능에 대한 다른 가정에 해당합니다. 이 시뮬레이션은 주당 250만 회의 백신 접종이 이루어지고, 효능이 1차 접종 후 70%, 2차 접종 후 88%이며, 접종률이 80세 이상에서 95%, 50~79세 연령대에서 85%, 18~49세 연령대에서 75%라고 가정합니다. JUNIPER 팀의 [논문](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(21)00143-2/fulltext)의 그림으로, *The Lancet*에 게재되었습니다.

12월까지 기다렸다가 모든 조치를 해제하더라도, 백신이 감염 예방에 매우 효과적이지 않는 한, 모델은 여전히 크고 지속적인 발병으로 끝날 수 있다고 제안합니다. "어떤 갑작스러운 변화든 항상 어떤 형태의 미래 발병을 촉발할 가능성이 있습니다"라고 Keeling은 말합니다.

![12월에 제한이 갑자기 해제된다면 COVID-19 일일 사망자 수](https://plus.maths.org/content/sites/plus.maths.org/files/news/2021/vaccines/keeling_december.jpg)

이 그림은 12월에 제한이 갑자기 해제된다면 COVID-19 일일 사망자 수에 무슨 일이 일어날지 탐색합니다. 다른 곡선들은 범례에 표시된 대로 백신이 감염을 예방하는 효능에 대한 다른 가정에 해당합니다. 이 시뮬레이션은 주당 250만 회의 백신 접종이 이루어지고, 효능이 1차 접종 후 70%, 2차 접종 후 88%이며, 접종률이 80세 이상에서 95%, 50~79세 연령대에서 85%, 18~49세 연령대에서 75%라고 가정합니다. JUNIPER 팀의 [논문](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(21)00143-2/fulltext)의 그림으로, *The Lancet*에 게재되었습니다.

> 이 결과들은 비선형 동역학의 중요한 특성을 보여줍니다. 시스템이 "임계점(tipping point)" 근처에 있을 때, 작은 교란이 큰 변화를 일으킬 수 있습니다. 4월이나 12월에 갑자기 제한을 해제하는 것은 시스템에 큰 교란을 주는 것입니다. 이는 수학적으로 비선형 미분방정식 시스템에서 평형점(equilibrium point)의 안정성과 관련이 있습니다. 백신 접종으로 $R$이 감소하지만 여전히 1보다 크면, 시스템은 불안정한 상태에 있습니다. 이때 사회적 거리두기 해제는 시스템을 새로운 평형점으로 빠르게 이동시키는데, 그 평형점은 높은 감염 수준을 의미합니다. 이것이 "갑작스러운 변화"가 위험한 수학적 이유입니다.

물론 정부의 봉쇄 해제 로드맵은 규제의 갑작스러운 완화를 포함하지 않고, 단계별로 진행됩니다. JUNIPER 팀은 또한 이러한 점진적 완화 전략을 살펴보았고, 그들의 모델에 따르면 속도가 느릴수록 발병이 작아진다는 것을 발견했습니다. "5개월 완화는 백신이 감염에 대해 85%의 보호를 제공하더라도 사망자의 눈에 띄는 정점을 여전히 제공합니다"라고 Keeling은 말합니다. 점점 더 느린 완화로 이동함에 따라, 발병은 덜 위협적이 됩니다.

![5개월, 10개월, 14개월에 걸쳐 제한이 완화되는 경우 COVID-19 일일 사망자 수](https://plus.maths.org/content/sites/plus.maths.org/files/news/2021/vaccines/keeling_months.jpg)

이 그림은 5개월(왼쪽 위), 10개월(오른쪽 위) 및 14개월(아래)에 걸쳐 제한이 완화되는 경우 COVID-19 일일 사망자 수에 무슨 일이 일어날지 탐색합니다. 다른 곡선들은 범례에 표시된 대로 백신이 감염을 예방하는 효능에 대한 다른 가정에 해당합니다. 이 시뮬레이션은 주당 250만 회의 백신 접종이 이루어지고, 효능이 1차 접종 후 70%, 2차 접종 후 88%이며, 접종률이 80세 이상에서 95%, 50~79세 연령대에서 85%, 18~49세 연령대에서 75%라고 가정합니다. JUNIPER 팀의 [논문](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(21)00143-2/fulltext)의 그림으로, *The Lancet*에 게재되었습니다.

> 완화 속도와 발병 규모 사이의 관계는 제어 이론(control theory)의 관점에서 이해할 수 있습니다. 빠른 완화는 시스템에 강한 "입력(input)"을 주는 것이고, 느린 완화는 약한 입력을 주는 것입니다. 비선형 시스템에서는 입력의 크기와 시스템 응답이 비례하지 않습니다. 특히 시스템이 임계점 근처에 있을 때는 더욱 그렇습니다. 점진적 완화는 본질적으로 "되먹임 제어(feedback control)" 전략입니다. 각 단계에서 감염 수준을 관찰하고, 그에 따라 다음 완화 단계를 조정할 수 있습니다. 이는 자동 조종 장치가 비행기를 안정적으로 유지하는 방식과 유사합니다. 갑작스러운 완화는 되먹임 없이 큰 조정을 하는 것과 같아서 시스템을 불안정하게 만듭니다.

"이 모든 것으로부터의 메시지는 우리가 신중해야 한다는 것입니다"라고 Keeling은 말합니다. "느린 완화가 항상 더 잘 작동하며, 발병을 통제하기 위해서는 더 높은 수준의 감염 차단이 필요합니다."

위의 수치들은 그때 이용 가능한 정보로 1월과 2월에 작성되었습니다. 백신의 효능에 대한 새로운 데이터가 항상 제공되면서 상황이 매우 빠르게 진전되고 있다는 것을 기억하는 것이 중요합니다. "내가 이번 주에 말하는 모든 것은 다음 주에 조정되고 수정될 가능성이 있습니다"라고 Keeling은 말합니다. 그러나 최신 정보로 모델을 실행할 때 시뮬레이션의 일반적인 메시지는 동일하게 유지됩니다. 다만 백신이 감염을 예방하는 데 얼마나 잘 작동하는지에 대해서는 더 낙관적입니다.

요약하자면, 모델링은 백신 접종이 만능 해결책은 아니지만, 봉쇄에서 벗어나는 데 핵심적인 역할을 한다는 것을 보여줍니다. 정확히 무슨 일이 일어날지는, 모델이 제안하는 바에 따르면, 백신이 감염을 차단하는 데 정확히 얼마나 효과적인지, 제한이 얼마나 천천히 해제되는지, 그리고 얼마나 많은 사람들이 백신 접종에 동의하는지에 결정적으로 달려 있습니다. 장기적으로는, 면역력 약화와 백신을 회피할 수 있는 새로운 변이가 이 단순한 그림을 바꿀 것입니다. 반복적인 부스터 백신 프로그램이 없다면 추가적인 미래 파동을 허용할 것입니다.

> 이 마지막 부분은 역학의 시간적 역학(temporal dynamics)을 강조합니다. 전염병은 정적인 현상이 아니라 끊임없이 진화하는 동적 시스템입니다. 바이러스는 돌연변이를 통해 백신 회피 능력을 발달시킬 수 있고(이는 진화적 압력의 결과), 인체의 면역 반응은 시간이 지남에 따라 약해집니다. 이는 수학적으로 시간 의존적 파라미터를 가진 모델로 표현됩니다. 예를 들어, 백신 효능 $e(t)$는 시간의 감소 함수일 수 있습니다. 또한 바이러스의 변이는 확률적 과정(stochastic process)으로, 각 감염 사건이 새로운 변이를 만들 기회를 제공합니다. 따라서 장기적 전략은 단순히 "한 번 백신 접종하고 끝"이 아니라, 지속적인 감시, 부스터 접종, 그리고 필요시 백신 업데이트를 포함해야 합니다. 이는 인플루엔자 백신이 매년 업데이트되는 것과 유사한 접근입니다.

## 이 글에 대하여

이 글은 [아이작 뉴턴 연구소](https://www.newton.ac.uk/)가 주최한 [Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/)의 [연구 발표](https://www.newton.ac.uk/seminar/29964/)와 Keeling, Sam Moore, [Edward Hill](https://warwick.ac.uk/fac/sci/maths/people/staff/ed_hill/), [Michael Tildesley](https://warwick.ac.uk/fac/sci/lifesci/people/mtildesley/), [Louise Dyson](https://warwick.ac.uk/fac/sci/maths/people/staff/dyson/)의 최근 논문을 기반으로 합니다.

Sam Moore는 작년 팬데믹 시작과 함께 워릭 대학교의 [SBIDER](https://warwick.ac.uk/fac/cross_fac/zeeman_institute/) 그룹에 합류한 후 Covid-19에 대한 백신 접종 모델링 작업을 해온 박사후 연구원입니다.

[Edward Hill](https://warwick.ac.uk/fac/sci/maths/people/staff/ed_hill/)은 워릭 대학교의 [SBIDER](https://warwick.ac.uk/fac/cross_fac/zeeman_institute/) 그룹의 박사후 연구원입니다. 그는 2020년 4월부터 [과학적 팬데믹 인플루엔자 모델링 그룹](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)(SPI-M)에 참여해 왔습니다.

[Michael Tildesley](https://warwick.ac.uk/fac/sci/lifesci/people/mtildesley/)는 워릭 대학교의 리더(Reader)입니다. 그는 2020년 4월부터 [SPI-M 모델링 그룹](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)에 참여해 왔습니다.

[Louise Dyson](https://warwick.ac.uk/fac/sci/maths/people/staff/dyson/)은 워릭 대학교의 역학 부교수입니다. 그녀는 2020년 4월부터 [SPI-M 모델링 그룹](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)에 참여해 왔습니다.

[Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/)은 워릭 대학교의 교수이며, 수학과 생명과학에서 공동 직위를 맡고 있습니다. 그는 현재 [시스템 생물학 및 감염병 역학 연구를 위한 Zeeman 연구소(SBIDER)](https://warwick.ac.uk/fac/cross_fac/zeeman_institute/)의 소장입니다. 그는 2009년부터 [SPI-M 모델링 그룹](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)의 일원이었으며, [예방접종 및 면역 공동위원회](https://www.gov.uk/government/groups/joint-committee-on-vaccination-and-immunisation)의 위원입니다.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)는 *Plus*의 편집자입니다.

*이 글은 공동 대학 팬데믹 및 유행병 대응 모델링 컨소시엄인 JUNIPER, 그리고 수학 과학을 위한 아이작 뉴턴 연구소(INI)와의 협력의 일환으로 제작되었습니다.*

*JUNIPER는 케임브리지, 워릭, 브리스톨, 엑서터, 옥스퍼드, 맨체스터, 랭커스터 대학교의 학자들로 구성되어 있으며, COVID-19의 통제에 관한 긴급한 질문을 다루기 위해 다양한 수학적 및 통계적 기법을 사용하고 있습니다. JUNIPER와 함께 제작된 더 많은 콘텐츠는 여기에서 볼 수 있습니다.*

*INI는 국제 연구 센터이며 케임브리지 대학교 수학 캠퍼스의 우리 이웃입니다. 전 세계의 주요 수학 과학자들을 끌어들이며, 모두에게 열려 있습니다. 자세한 내용은 www.newton.ac.uk를 방문하십시오.*

![Juniper logo](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)

![INI logo](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)