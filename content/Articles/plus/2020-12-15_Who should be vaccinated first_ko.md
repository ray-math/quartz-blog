---
title: 누구에게 먼저 백신을 접종해야 하는가?
date: 2020-12-15
tags:
  - 백신
  - 감염
  - 접종
  - Warwick
  - Keeling
  - Matt
  - Sam
  - rate
---

> [!NOTE]
> https://plus.maths.org/content/who-should-be-vaccinated-first
>
> 수학적 모델링이 보여주는 백신 접종 우선순위: 노인과 취약계층이 먼저다.

![icon](https://plus.maths.org/content/sites/default/files/styles/small_square/public/abstractpics/%5Buid%5D/%5Bsite-date%5D/icon_boy.jpg?itok=48rN1mAB)

*뉴스에서 쏟아지는 질문들 속에서 우리는 Warwick 대학교의 역학 모델링 전문가이자 JUNIPER 모델링 컨소시엄의 회원인 Matt Keeling과 Sam Moore에게 누가 백신을 먼저 맞아야 하는지 물었다. 다음은 우리가 배운 내용이다.*

모든 사람이 동시에 백신을 접종받을 수는 없기 때문에, 누가 먼저 백신을 맞을 것인지 결정해야 한다. 두 가지 명백한 전략이 있다. 하나는 사회적 접촉이 가장 많은 사람들을 우선시하는 것이다. 이들이 감염을 전파할 가능성이 가장 높기 때문이다. 이는 아마도 젊은 연령층에게 먼저 접종하는 것을 의미할 것이다. 이들은 직장과 여가 활동을 통해 더 많은 사람들을 만나는 경향이 있기 때문이다. 다른 전략은 가장 취약한 사람들을 우선시하는 것이다. 즉, 노인과 더 높은 위험에 처하게 하는 특정 건강 상태를 가진 사람들이다.

> 이 두 전략은 서로 다른 목표를 반영한다. 첫 번째 전략(젊은층 우선)은 감염병의 **전파 속도**(transmission rate)를 낮추는 데 초점을 맞춘다. 역학에서 기본재생산수(basic reproduction number) $R_{0}$는 한 감염자가 평균적으로 몇 명을 감염시키는지를 나타내는데, 사회적 접촉이 많은 집단을 먼저 백신 접종하면 이 $R_{0}$ 값을 빠르게 낮출 수 있다. 반면 두 번째 전략(노인 우선)은 **사망률**(mortality rate)과 **중증도**(severity)를 낮추는 데 초점을 맞춘다. COVID-19의 경우 나이가 들수록 치명률이 기하급수적으로 증가하므로, 어떤 전략이 더 많은 생명을 구할 수 있는지는 자명하지 않다. 이것이 바로 수학적 모델링이 필요한 이유다.

전체 COVID-19 백신 FAQ를 보려면 [여기](https://plus.maths.org/content/covid-19-vaccines-your-questions-answered)를 클릭하세요.

역학 모델러인 [Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/)과 Sam Moore는 [Ed Hill](https://warwick.ac.uk/fac/sci/maths/people/staff/ed_hill/), [Louise Dyson](https://warwick.ac.uk/fac/sci/maths/people/staff/dyson/), [Mike Tildesley](https://warwick.ac.uk/fac/sci/lifesci/people/mtildesley/)와 함께 어느 전략이 더 나은지를 수학 모델을 사용하여 탐구했다. 이 모델들은 특정 가정 하에서 질병이 어떻게 확산될지 시뮬레이션할 수 있다 (그들이 사용한 것은 정교한 *구획 모델*(compartmental model)이며, 자세한 내용은 [이 글](https://plus.maths.org/content/how-can-maths-fight-pandemic)을 참조하라).

> 구획 모델은 인구를 여러 '구획'으로 나누어 질병의 전파를 추적하는 수학적 틀이다. 가장 기본적인 형태는 SIR 모델로, 인구를 감수성(Susceptible), 감염(Infected), 회복(Recovered)의 세 구획으로 나눈다. 이를 미분방정식으로 표현하면:
> $\frac{dS}{dt} = -\beta SI, \quad \frac{dI}{dt} = \beta SI - \gamma I, \quad \frac{dR}{dt} = \gamma I$
> 여기서 $\beta$는 전파율, $\gamma$는 회복률이다. COVID-19 백신 접종 전략을 연구하기 위해서는 이보다 훨씬 복잡한 모델이 필요하다. 연령대별로 구획을 나누고(연령 구조 모델), 백신 접종자를 위한 별도의 구획을 추가하며, 백신의 효능, 사회적 거리두기, 무증상 감염 등의 요소를 포함해야 한다. 이러한 모델은 수십 개에서 수백 개의 연립 미분방정식으로 구성될 수 있으며, 컴퓨터 시뮬레이션을 통해 다양한 시나리오의 결과를 예측한다.

![A boy being vaccinated](https://plus.maths.org/latestnews/sep-dec09/vaccines/iStock_vaccine.jpg)

COVID-19 백신의 경우 노인을 우선시하는 것이 합리적이므로, 어린이들은 접종 순서에서 나중에 온다.

연구팀이 여름과 가을에 걸쳐 모델링을 수행했을 때, 어떤 유형의 백신이 등장할지, 얼마나 효과적일지는 아직 명확하지 않았다. 따라서 그들은 백신이 작동할 수 있는 다양한 방식(예: 전파를 억제하는가, 아니면 단지 증상만 억제하는가?)과 효과성(예: 50%, 70%, 또는 90%)에 대한 여러 가능성을 탐구했다. 또한 백신 접종 프로그램이 진행되는 동안 사회적 거리두기 조치가 시행되는지 여부, 백신 배포가 빠르게 이루어지는지 천천히 이루어지는지 등 다양한 가정에 대해서도 탐구했다 (탐구된 시나리오와 기본 가정에 대한 자세한 내용은 [논문](https://www.medrxiv.org/content/10.1101/2020.09.22.20194183v2.full.pdf)에서 확인할 수 있다).

> 백신의 작동 방식에 따라 결과는 크게 달라질 수 있다. 백신은 크게 세 가지 유형의 효과를 가질 수 있다: (1) **감염 차단**(sterilizing immunity) - 바이러스가 아예 몸에 침투하지 못하게 함, (2) **증상 완화**(symptom reduction) - 감염되더라도 증상이 경미하게 나타남, (3) **전파 억제**(transmission blocking) - 감염되더라도 다른 사람에게 전파할 가능성이 낮아짐. 완벽한 백신은 세 가지를 모두 달성하지만, 실제 백신은 이들 중 일부만 달성하는 경우가 많다. 예를 들어, 어떤 백신이 증상은 완벽하게 막지만 감염과 전파는 막지 못한다면, 백신을 맞은 사람은 무증상 감염자가 되어 여전히 바이러스를 퍼뜨릴 수 있다. 따라서 백신의 정확한 특성을 알지 못한 상태에서 접종 전략을 수립하려면, 모든 가능한 시나리오를 고려한 강건한(robust) 분석이 필요하다.

모델링의 결과는 놀랍도록 명확하다: 탐구된 모든 시나리오에서 취약계층을 우선시하는 것이 더 나은 것으로 나타났다. 이는 노인과 기저질환이 있는 사람들에 해당한다. 이 전략은 2021년 말까지 더 적은 수의 사망자를 낳을 것이며, 더 적은 수의 QALY 손실로도 이어질 것이다. QALY는 *질 보정 생존년수*(quality adjusted life year)를 의미하며, 삶의 질을 고려한 개인 수명의 기간을 측정하는 지표다 (자세한 내용은 [여기](https://plus.maths.org/content/os/latestnews/jan-apr10/qaly/index)를 참조하라).

> QALY는 보건경제학에서 의료 개입의 가치를 평가하기 위해 사용되는 핵심 지표다. 단순히 생존 기간만을 고려하는 것이 아니라, 그 기간 동안의 삶의 질도 함께 고려한다. 예를 들어, 완벽한 건강 상태로 1년을 사는 것은 1 QALY이고, 50%의 건강 상태로 1년을 사는 것은 0.5 QALY다. 여기서 건강 상태는 0(사망)부터 1(완벽한 건강)까지의 '효용 값'(utility value)으로 표현된다. COVID-19의 경우, 젊은 사람이 사망하면 더 많은 잠재적 생존년수가 손실되지만, 노인이 사망하면 더 높은 치명률과 중증도로 인해 더 큰 즉각적 영향이 있다. QALY 분석은 이 둘을 균형 있게 고려하여, 어느 전략이 전체 사회의 건강 부담을 최소화하는지 정량적으로 평가한다. 연구 결과, 노인 우선 전략이 생명 구조(사망자 수 감소)와 QALY 손실 최소화 두 측면 모두에서 우수했다는 것은 매우 강력한 결론이다.

이는 80세 이상부터 시작하여 연령대 순서대로 사람들에게 백신을 접종하는 것이 최선의 전략임을 의미한다. 기저질환으로 인해 취약한 사람들도 백신 접종 프로그램 초기에 접종받아야 한다. 의료 종사자들도 바이러스에 접촉할 위험이 더 크고, 의료 시스템을 보존해야 할 필요성이 있으며, 백신이 실제로 전파를 억제한다면 얻을 수 있는 잠재적 이득이 있기 때문에 우선순위에 포함된다. 이것은 본질적으로 영국 정부가 수학적 모델링의 안내를 부분적으로 받아 채택한 전략이다.

충분한 사람들이 백신을 맞지 않고 사회적 거리두기 조치가 지켜지지 않는다면, 최고의 백신도 이길 수 없다.

모델링은 또한 두 가지 다른 중요한 교훈을 제시한다. 첫째는, 상당히 엄격한 사회적 거리두기 조치가 시행되지 않는 한, 지수적으로 증가하는 전염병과 이를 따라잡으려는 백신 접종 프로그램 사이에 경주가 일어날 것이라는 점이다. 이 경주는 지수 성장의 속도 때문에 전염병이 이길 가능성이 높다. 실제로, 백신 접종이 진행되는 동안 모든 사회적 거리두기 조치가 해제된다면, 모델링은 전파뿐만 아니라 증상도 억제할 수 있는 매우 효과적인 백신만이 후속 파동을 통제할 수 있을 것이라고 제시한다.

> 이것은 지수 성장의 파괴적 힘을 보여주는 중요한 통찰이다. 감염병의 초기 단계에서 감염자 수는 $I(t) = I_{0}e^{rt}$ 형태로 증가하는데, 여기서 $r$은 성장률이다. 만약 $R_{0} = 3$이고 세대 시간(generation time)이 5일이라면, 감염자 수는 약 5일마다 3배씩 증가한다. 반면 백신 접종은 선형적으로(하루에 일정 수의 사람들에게) 진행된다. 지수 함수는 초기에는 천천히 증가하지만, 임계점을 넘으면 선형 성장을 압도적으로 추월한다. 따라서 백신 접종 속도가 충분히 빠르더라도, 사회적 거리두기 없이는 전염병이 백신 접종 속도를 추월하여 대규모 감염을 일으킬 수 있다. 이것이 "경주"라는 비유가 적절한 이유다. 수학적으로, 백신 접종이 전염병을 억제하려면 백신 접종률이 $\gamma + r$ (회복률 + 성장률)보다 커야 하는데, 지수 성장 단계에서는 이 조건을 만족시키기가 매우 어렵다.

둘째 교훈은 백신 접종률(uptake)이 결정적이라는 것이다. 모델링은 인구의 각 하위 그룹의 70%가 백신을 접종받을 것이라고 가정했다. 그러나 접종률이 이보다 상당히 낮다면, 최고의 백신이라도 이길 수 없다.

> 백신 접종률과 집단면역 임계값(herd immunity threshold) 사이에는 중요한 관계가 있다. 집단면역은 인구의 충분한 비율이 면역을 획득했을 때 달성되며, 이때 감염병의 확산이 자연스럽게 멈춘다. 이 임계값은 $1 - \frac{1}{R_{0}}$로 계산된다. 만약 $R_{0} = 3$이라면, 약 67%의 인구가 면역을 가져야 한다. 그러나 이는 백신이 100% 효과적이라는 가정 하의 값이다. 백신 효능이 90%라면, 실제로 필요한 백신 접종률은 $\frac{1 - 1/R_{0}}{\text{효능}} \approx 74\%$로 증가한다. 70% 접종률은 이 임계값 근처에 있어, 접종률이 이보다 낮아지면 집단면역 달성이 불가능해진다. 또한, 인구가 여러 하위 그룹으로 나뉘어 있고 그룹 간 접촉 패턴이 비균질적일 때는 분석이 더욱 복잡해진다. 어떤 그룹(예: 젊은층)의 접종률이 낮으면, 그 그룹에서 전파가 계속되어 전체 방역 효과가 크게 감소할 수 있다.

*COVID-19 백신 FAQ로 돌아가기*

### 이 글에 대하여

![Matt](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2020/vaccine/matt.jpg)

Matt Keeling

[Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/)은 University of Warwick의 교수이며, 수학과 생명과학 분야에서 공동 직책을 맡고 있다. 그는 현재 Zeeman Institute for Systems Biology and Infectious Disease Epidemiology Research (SBIDER)의 소장이다. 2009년부터 SPI-M 모델링 그룹의 일원으로 활동해 왔다.

Sam Moore는 박사후 연구원으로, 올해 초 팬데믹이 시작된 후 University of Warwick의 SBIDER에 합류하여 COVID-19에 대한 백신 접종 모델링 작업을 해왔다.

![Sam](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2020/vaccine/sam.jpg)

Sam Moore

두 사람 모두 JUNIPER(Joint UNIversity Pandemic and Epidemic Response 모델링 컨소시엄)의 회원이다. 이 컨소시엄은 영국 7개 대학의 학자들로 구성되어 있으며, 다양한 수학적·통계적 기법을 사용하여 COVID 통제에 관한 시급한 질문들을 다룬다. 참여 대학은 Cambridge, Warwick, Bristol, Exeter, Oxford, Manchester, Lancaster이다. JUNIPER와 함께 제작된 더 많은 콘텐츠는 [여기](https://plus.maths.org/content/juniper)에서 볼 수 있다.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)와 [Rachel Thomas](https://plus.maths.org/content/people/index.html#rachel)는 *Plus*의 편집자다.

![Juniper logo](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)