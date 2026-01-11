---
title: COVID-19 현황 파악하기
date: 2021-04-09
---

> [!NOTE]
> https://plus.maths.org/content/keeping-covid-19
>
> 팬데믹 한가운데서 질병의 실시간 발생률을 파악하는 것은 전례 없는 일이었지만, ONS COVID-19 감염 조사팀은 이를 실현할 방법을 개발했습니다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/covid19_test_frontpage.jpg?h=1c7b55f3&itok=ok-NBf-J)

우리 중 많은 이들은 팬데믹 상황을 알려주는 일일 통계를 기다립니다: 처음으로 양성 판정을 받은 사람 수, 입원 환자 수, 그리고 안타깝게도 지난 24시간 동안의 사망자 수. 하지만 [정부의 일일 통계](https://coronavirus.data.gov.uk/)에서 두 가지 수치가 빠져 있다는 것을 궁금하게 여긴 적이 있을 것입니다: 현재 COVID-19에 감염된 사람이 몇 명인지, 그리고 영국에서 새로운 COVID-19 감염이 얼마나 발생했는지.

> 여기서 언급되는 두 가지 누락된 수치는 역학(epidemiology)에서 가장 기본이 되는 측정값들입니다. 첫 번째는 '유병률(prevalence)'로, 특정 시점에서 질병을 가진 사람의 비율을 의미합니다. 두 번째는 '발생률(incidence)'로, 특정 기간 동안 새롭게 질병에 걸린 사람의 수를 나타냅니다. 이 두 개념을 구분하는 것이 중요한 이유는, 유병률은 현재 의료 시스템에 가해지는 부담을 알려주는 반면, 발생률은 질병의 확산 속도를 보여주기 때문입니다. 팬데믹 대응에서 이 두 수치는 각각 다른 정책적 의미를 갖습니다.

COVID-19 팬데믹에 대한 모든 기사는 [여기](https://plus.maths.org/content/tags/covid-19)를 참조하세요.

이 수치들, 즉 질병의 *유병률과 발생률*을 정확히 아는 것은 팬데믹 기간 동안 필수적으로 보이지만, 이 수치들은 다른 일일 통계와 함께 발표되지 않습니다. 우리가 모든 인구를 항상 검사할 수는 없기 때문에, 이 수치들을 얻기는 어렵습니다. 이것이 바로 영국 국가통계청(Office for National Statistics, ONS)이 2020년 4월에 [COVID-19 감염 조사](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/bulletins/coronaviruscovid19infectionsurveypilot/previousReleases)를 시작한 이유입니다. ONS 조사의 결과와 분석은 매주 정부와 대중에게 보고됩니다.

> 전수조사(census)가 불가능한 상황에서 표본조사(sample survey)는 모집단의 특성을 추정하는 핵심 방법입니다. 하지만 COVID-19와 같은 감염병의 경우, 단순한 횡단면 조사(cross-sectional survey)로는 질병의 동적 특성을 파악하기 어렵습니다. ONS가 채택한 종단 연구(longitudinal study) 설계는 같은 개인들을 반복적으로 추적함으로써, 질병의 시작과 끝, 그리고 지속 기간을 관찰할 수 있게 합니다. 이는 통계학에서 '패널 데이터(panel data)'로 불리며, 시간에 따른 변화를 추적하는 가장 강력한 도구 중 하나입니다.

### ONS 조사

ONS 조사는 다른 어떤 연구도 제공하지 못한 것을 제공했습니다: 시간이 지남에 따라 같은 가구를 추적하며, 조사 대상 가구들은 전체 인구를 근사적으로 대표하는 표본을 형성합니다. 처음에는 가구의 모든 구성원이 감독하에 매주 COVID-19 검사를 받으며, 처음 4주 후에는 월별 검사로 전환합니다. 이 연구는 증상 유무와 관계없이, 이러한 가구들에서 COVID-19의 유병률과 발생률을 거의 실시간으로 관찰할 기회를 제공합니다. 이러한 방식으로 ONS 조사는 주로 COVID-19 증상 발생에 대응하여 일회성으로 실시되는 NHS 검사 및 추적 프로그램의 데이터보다 지역사회에서의 팬데믹 상태를 훨씬 더 명확하게 보여줍니다.

![주간 검사 결과](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/prevalence/testresults_web.jpg)

ONS 조사 참가자의 일련의 COVID-19 검사 결과.

ONS 조사는 여론조사가 사람들의 투표 의향을 직접적으로 측정하는 것과 유사한 방식으로 유병률을 직접 측정합니다. 실제로 여론조사에 사용되는 것과 유사한 방법인 [다층 회귀 및 사후층화(multilevel regression and poststratification, MRP)](https://en.wikipedia.org/wiki/Multilevel_regression_with_poststratification)가 조사 표본에서 영국 전체 인구로 외삽하는 데 사용됩니다. (ONS 조사에서 사용된 방법에 대한 자세한 내용은 [여기](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/methodologies/covid19infectionsurveypilotmethodsandfurtherinformation#incidence)에서 확인할 수 있습니다.)

> MRP는 현대 통계학에서 가장 정교한 표본 가중치 조정 기법 중 하나입니다. 이 방법은 두 단계로 작동합니다. 첫째, 다층 회귀 모델(multilevel regression model)을 사용하여 다양한 인구통계학적 그룹(연령, 성별, 지역 등)별로 관심 변수(여기서는 COVID-19 양성률)를 예측합니다. 둘째, 사후층화(poststratification) 단계에서 실제 인구 구성에 맞춰 이러한 예측값들을 가중 평균합니다. 이는 표본이 모집단을 완벽하게 대표하지 못할 때 발생하는 편향(bias)을 교정하는 강력한 방법입니다. 예를 들어, 조사 표본에서 젊은 층이 과소 대표되었다면, MRP는 실제 인구에서 젊은 층이 차지하는 비율을 반영하여 이를 보정합니다.

연구자들은 또한 데이터를 사용하여 더 간접적인 경로를 통해 발생률과 감염 기간을 추정할 수 있습니다. 참가자가 1주차에 음성, 2주차에 COVID-19 양성, 3주차에 다시 양성, 4주차에 음성으로 검사되었다고 가정해 봅시다. 이러한 검사 결과의 순서는 ONS 조사가 포착하는 것으로, 다른 곳에서는 포착되지 않습니다: 이 조사는 1주차에 바이러스를 가지고 있지 않던 사람이 COVID-19 양성 판정을 받고 최소 2주 후에 회복하는 변화를 감지합니다.

맨체스터 대학의 수학자이자 [JUNIPER 컨소시엄](https://maths.org/juniper/)의 일원인 [Thomas House](https://www.research.manchester.ac.uk/portal/thomas.house.html)는 말합니다. "연구 설계를 고려하면, 우리는 그들이 정확히 언제 양성 판정을 시작하고 멈췄는지 알 수 없습니다." House는 이 진행 중인 프로젝트에서 ONS와 협력하는 학술 협력팀 중 한 명입니다. "실제로 할 수 있는 것은 이러한 사건들에 대한 가장 빠른 시간과 가장 늦은 시간을 계산하는 것뿐입니다." 이것은 통계학에서 [절단 문제(censoring problem)](https://en.wikipedia.org/wiki/Censoring_%28statistics%29#Epidemiology)의 예로, 데이터에 대해 알 수 있는 것은 관찰된 범위 내에 있다는 것뿐입니다.

> 절단(censoring)은 생존분석(survival analysis)과 역학 연구에서 흔히 마주치는 문제입니다. 데이터가 '우측 절단(right-censored)'되었다는 것은 사건이 일어났는지는 모르지만, 특정 시점까지는 일어나지 않았다는 것을 안다는 의미입니다. 반대로 '좌측 절단(left-censored)'은 사건이 특정 시점 이전에 일어났다는 것만 안다는 의미입니다. COVID-19 검사에서는 양방향 절단이 발생합니다: 1주차 음성과 2주차 양성 사이 어느 시점에 감염되었는지 정확히 알 수 없습니다. 이러한 불확실성을 다루는 것은 통계적 추론의 핵심 과제이며, 여러 방법론이 개발되어 왔습니다. 가장 간단한 접근법이 다음에 설명될 '중점 대체법(mid-point imputation)'입니다.

이러한 절단된 데이터를 관리하기 위해 여러 수학적 접근법이 사용될 수 있지만, ONS 조사의 경우 처음 사용된 접근법은 놀랍도록 간단했습니다. 본질적으로, 조사의 학술 협력팀은 *중점 대체(mid-point imputation)*라고 불리는 방법으로 그들의 추정을 분산시켰습니다. 그들은 참가자가 1주차에 검사받은 날짜에 음성이었고, 2주차에 검사받은 날짜에 양성이었다는 것을 알고 있습니다. 따라서 그들은 이러한 알려진 사실들 사이의 시간을 반으로 나누고, 사람이 이 구간의 중간에 감염되었다고 가정합니다.

![주간 검사 결과 - 중점 대체 적용](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/prevalence/midpoint3_web.jpg)

중점 대체는 참가자가 실제로 감염되거나 회복한 날짜가 관찰된 검사 결과의 변화 사이의 중간이었다고 가정합니다.

> 중점 대체법은 통계학에서 '대체법(imputation)'의 가장 단순한 형태입니다. 대체법은 결측 데이터(missing data)나 불확실한 데이터를 합리적인 값으로 채우는 기법입니다. 중점 대체는 구간 $[t_1, t_2]$ 내에서 사건이 발생했을 때, 그 중간점 $(t_1 + t_2)/2$에서 발생했다고 가정합니다. 이는 구간 내 모든 시점이 동일한 확률을 가진다는 균등분포(uniform distribution) 가정 하에서 기댓값을 사용하는 것과 같습니다. 더 정교한 방법으로는 베이지안 다중 대체(Bayesian multiple imputation)가 있지만, 중점 대체의 단순성은 계산 효율성과 해석 용이성이라는 장점을 제공합니다. 특히 표본 크기가 크고 관측 구간이 상대적으로 짧을 때, 중점 대체는 더 복잡한 방법과 비교하여 편향이 크지 않습니다.

### 지속 기간

ONS 조사의 초기 주간 단계는 영국 팬데믹 상황에 대한 정보만 제공한 것이 아니라, 질병 자체에 대한 중요한 증거를 제공했습니다. 특히, 주간 추적조사는 증상 유무와 관계없이 사람들이 질병을 얼마나 오래 가지고 있었는지에 대한 데이터를 수집할 기회를 제공했습니다.

예상할 수 있듯이, 이 지속 기간은 고정된 숫자가 아닙니다 - 어떤 사람들은 며칠 동안만 양성 판정을 받는 반면, 어떤 사람들은 몇 주 동안 양성 판정을 받을 것입니다. House는 질병의 지속 기간을 수학적으로 설명하는 가장 좋은 방법은 누군가가 처음 감염된 후 어느 시점에 여전히 양성 판정을 받을 확률로 표현하는 것이라고 설명합니다. 수학적으로 우리는 이것을 시간에 대한 함수(변수 이름 $T$ 사용)로 쓸 수 있으며, 조건부 확률을 제공합니다: 

$$
Dur(T) = P(\text{여전히 양성} \mid \text{시간 } T=0 \text{에 양성이 됨})
$$

> 이 지속 기간 함수 $Dur(T)$는 생존함수(survival function)의 한 형태입니다. 생존분석에서 생존함수 $S(t)$는 시간 $t$까지 사건(여기서는 회복 또는 음성 전환)이 발생하지 않을 확률을 나타냅니다. 일반적으로 $S(0) = 1$ (모든 사람이 처음에는 양성)이고, 시간이 지남에 따라 단조감소하며(사람들이 점진적으로 회복), $t \to \infty$일 때 $S(t) \to 0$에 접근합니다. 이 함수의 형태는 질병의 자연사(natural history)를 이해하는 데 핵심적입니다. 예를 들어, 함수가 급격히 감소한다면 대부분의 사람들이 빠르게 회복한다는 의미이고, 긴 꼬리(long tail)를 가진다면 일부 사람들은 매우 오랫동안 양성 상태를 유지한다는 의미입니다.

![지속 기간 함수](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/prevalence/duration_web.jpg)

지속 기간 함수의 대략적인 스케치로, 감염 후 시간이 지남에 따라 누군가가 여전히 COVID-19 양성일 확률을 보여줍니다.

ONS 조사는 $Dur(T)$를 가능한 한 실시간에 가깝게 직접 추정할 기회를 제공했습니다. 연구자들은 이제 COVID-19 감염 기간에 대한 훨씬 더 명확한 수학적 설명을 가지고 있습니다.

> 지속 기간 함수를 추정하는 것은 공중보건 정책에 직접적인 영향을 미칩니다. 예를 들어, 격리 기간을 얼마나 설정해야 하는지는 대부분의 사람들이 더 이상 전염성이 없는 시점, 즉 $Dur(T)$가 충분히 작아지는 시점에 기반해야 합니다. 초기 팬데믹 때는 이 정보가 없어서 다른 코로나바이러스(SARS, MERS)의 데이터나 보수적인 추정에 의존했습니다. ONS 조사가 제공한 실증적 데이터는 이러한 정책을 과학적 근거에 기반하여 조정할 수 있게 했습니다.

### 유병률에서 발생률로

![Covid-19 검사](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2020/UnlockingHE/covid19_test.jpg)

새로운 양성 검사 수는 일일 COVID-19 통계의 일부로 보고됩니다. 이것은 새로운 양성 검사 수의 증가와 감소를 모니터링하면서 질병의 성장과 쇠퇴에 대한 합리적으로 좋은 그림을 제공하는 견고한 데이터입니다. 그러나 보고된 새로운 양성 검사 수에는 질병을 가지고 있지만 검사받지 않은 사람들이 포함되지 않습니다: 아마도 증상이 없기 때문에; 검사에 접근할 수 없기 때문에; 또는 검사를 받지 않을 다른 이유가 있기 때문입니다. 게다가, 누군가가 검사를 받은 날과 그 검사 결과가 보고되는 날은 그들이 COVID-19를 가진 첫날과 거의 확실히 같지 않을 것입니다. 매일 보고되는 새로운 양성 검사 수는 그 시점의 질병의 진정한 발생률과 같지 않습니다.

> 여기서 강조되는 것은 관찰된 데이터와 진정한 역학적 과정 사이의 차이입니다. 보고된 양성 검사는 '감시 데이터(surveillance data)'로, 질병 활동의 대리 지표(proxy indicator)일 뿐입니다. 진정한 발생률을 가리는 여러 요인이 있습니다: (1) 검사 접근성의 변화 - 검사소가 더 많이 열리면 양성 사례도 더 많이 발견됩니다. (2) 검사 행동의 변화 - 사람들이 더 조심스러워지면 경미한 증상에도 검사를 받습니다. (3) 보고 지연(reporting delay) - 감염, 증상 발현, 검사, 결과 보고 사이에 각각 시차가 있습니다. (4) 무증상 감염자 - 증상이 없으면 검사받을 가능성이 낮습니다. 이러한 편향(bias)들을 이해하고 보정하는 것이 역학 연구의 핵심 과제입니다.

"우리가 여전히 대부분의 참가자들을 주간으로 추적조사하고 있을 때, 우리는 발생률과 유병률을 직접 파악하려고 노력했습니다"라고 House는 말합니다. "하지만 너무 많은 사람들이 월간 추적조사로 이동했기 때문에 그것은 이제 중단되었습니다." 사람들을 월별로만 검사하면 정확한 발생률 측정을 위해 너무 많은 사람들의 초기 양성 검사를 놓치게 됩니다. 하지만 인구 표본에서 양성 검사 수에 대한 지속적인 스냅샷은 여전히 진정한 유병률에 대한 좋은 측정값을 제공하며, 월 15만 명을 무작위로 검사하는 다른 중요한 COVID-19 연구인 [REACT 연구](https://www.imperial.ac.uk/medicine/research-and-impact/groups/react-study/)도 마찬가지입니다.

"대신 우리는 유병률로부터 발생률을 계산하는 방향으로 이동하고 있습니다. 월간 추적조사에 의존하게 되면 이것이 유일한 방법이기 때문입니다"라고 House는 말합니다. 이것은 질병의 유병률, 발생률, 지속 기간 사이의 수학적 관계 덕분에 가능합니다.

질병의 유병률은 오늘 COVID-19에 걸린 사람들을 포함합니다: 우리는 이것을 시간의 함수 $Inc(t)$로 쓸 것이며, 여기서 오늘은 시간 $t$입니다.

유병률은 또한 어제 질병에 걸렸지만(시간을 일 단위로 측정한다면 $Inc(t-1)$로 주어짐) 오늘 여전히 질병을 가지고 있는 사람들을 포함합니다. 위에서 질병의 지속 기간에 대한 논의에서, 1일 전에 질병에 걸린 사람들이 여전히 양성 판정을 받을 확률은 $Dur(1)$이라는 것을 알고 있으므로, 오늘 여전히 양성 판정을 받는 그들의 수는 $Inc(t-1) \times Dur(1)$입니다.

오늘 질병의 유병률은 또한 이틀 전에 질병에 걸렸지만 오늘 여전히 양성 판정을 받는 사람들을 포함합니다: $Inc(t-2) \times Dur(2)$로 주어집니다. 그리고 우리는 이 사고의 흐름을 계속해서 질병의 유병률을 다음과 같이 나타낼 수 있습니다: 

$$
Prev(t) = Inc(t) + Inc(t-1) \times Dur(1) + Inc(t-2) \times Dur(2) + Inc(t-3) \times Dur(3) + \dots
$$

> 이 식은 역학에서 근본적으로 중요한 관계를 보여줍니다. 유병률은 '저량(stock)' 변수이고, 발생률은 '유량(flow)' 변수입니다. 경제학의 비유를 들자면, 은행 계좌의 잔고(유병률)는 매일의 입금(발생률)에서 출금(회복률)을 뺀 것의 누적입니다. 여기서 핵심 통찰은 유병률이 과거 모든 발생률의 가중합(weighted sum)이라는 것입니다. 가중치는 지속 기간 함수 $Dur(k)$로 주어지며, 이는 $k$일 전에 감염된 사람이 여전히 감염 상태일 확률을 나타냅니다. 이 관계는 '갱신 방정식(renewal equation)'의 한 형태로, 인구 동태(population dynamics) 모델링에서 널리 사용됩니다.

![오늘 질병의 유병률 계산](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/prevalence/prevalencetoday_web.jpg)

오늘 질병의 유병률은 오늘 질병에 걸린 사람들과, 어제 걸렸지만 오늘 여전히 감염된 사람들, 그리고 이틀 전에 걸렸지만 오늘 여전히 감염된 사람들... 등등의 합입니다. 연한 파란색 직사각형은 이전 날짜의 발생률을 나타내고, 진한 파란색 직사각형은 그 중 오늘 여전히 감염된 비율(*Inc(t-k) × Dur(k)*, 여기서 $k$는 며칠 전인지를 나타냄)을 나타냅니다.

통계는 매일 발표되지만, 이렇게 시간을 일 단위로 나누는 것은 상당히 자의적입니다. 수학적으로는 점점 더 작은 시간 간격으로 작업하는 것이 더 쉬울 수 있으며, 이를 극한으로 가져가면 미적분학의 모든 힘을 활용할 수 있습니다. 이 시점에서, 일별 또는 시간별 계산보다는, 임의의 시점 $t$에 대한 유병률을 사람들이 질병에 걸린 이후의 시간 $T$에 대한 적분으로 설명할 수 있습니다: 

$$
Prev(t) = \int_{T=0}^{\infty} Inc(t-T) \, Dur(T) \, dT
$$

이것은 아름다운 수학적 결과이지만, 또한 매우 유용합니다. House는 ONS 조사의 주간 단계에서 그들이 발생률, 지속 기간, 유병률 이 세 가지를 각각 별도로 측정하려고 노력했다고 설명합니다. 그리고 이제 그들은 월간 추적조사를 사용하여 유병률을 측정하고 있으며, 여전히 이 수학적 관계를 사용하여 질병의 발생률을 계산할 수 있습니다.

> 이 적분 방정식은 수학적으로 합성곱(convolution)입니다: $Prev = Inc * Dur$. 합성곱은 신호처리, 확률론, 그리고 여기서처럼 역학에서 핵심적인 연산입니다. 직관적으로, 이는 "과거의 모든 발생들이 현재의 유병률에 얼마나 기여하는가"를 합산하는 것입니다. 수학적으로 흥미로운 점은 푸리에 변환(Fourier transform) 하에서 합성곱이 곱셈으로 바뀐다는 것입니다: $\mathcal{F}\{Prev\} = \mathcal{F}\{Inc\} \cdot \mathcal{F}\{Dur\}$. 이는 주파수 영역(frequency domain)에서 작업할 때 계산을 크게 단순화할 수 있습니다. 또한 이 방정식은 역문제(inverse problem)를 제기합니다: $Prev$와 $Dur$를 알 때 $Inc$를 구하는 것은 '디컨볼루션(deconvolution)'으로, 일반적으로 불안정(ill-posed)한 문제입니다. 이는 작은 측정 오차가 큰 추정 오차로 증폭될 수 있음을 의미하며, 정규화(regularization) 기법이 필요합니다.

House는 이 접근법이 완전한 과거 질병 데이터 세트를 다루는 일반적인 경험에서, 실시간으로 진행되는 질병의 실시간 데이터 스트림을 다루는 것으로 이동하면서 수학자들이 해야 했던 혁신의 일부를 보여준다고 설명합니다. "실시간으로 질병의 발생률을 직접 파악하려는 시도는 이전에 한 번도 이루어진 적이 없습니다. 그것은 정말 도전적입니다." 다행히도 Thomas House와 팀에서 일하는 나머지 연구자들 같은 사람들이 이 도전에 맞서고 있습니다.

> 실시간 역학 추론(real-time epidemiological inference)은 21세기 공중보건의 새로운 frontier입니다. 전통적으로 역학 연구는 회고적(retrospective)이었습니다: 유행이 끝난 후 데이터를 수집하고 분석하여 무슨 일이 있었는지 이해했습니다. 하지만 COVID-19 팬데믹은 '지금 무슨 일이 일어나고 있는가'를 실시간으로 알아야 하는 절박한 필요성을 만들었습니다. 이는 여러 새로운 과제를 제기합니다: 불완전하고 잡음이 많은 데이터로 작업해야 하고, 모델 가정이 시간에 따라 변할 수 있으며(예: 새로운 변이), 분석 결과가 즉각적인 정책 결정에 영향을 미칩니다. 이는 통계적 방법론뿐만 아니라 계산 효율성, 불확실성 정량화(uncertainty quantification), 그리고 결과의 효과적인 전달에 대한 새로운 요구를 만들어냅니다.

### 이 글에 대하여

![Thomas House](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/prevalence/house_web.jpg)

Thomas House

[Thomas House](https://www.research.manchester.ac.uk/portal/thomas.house.html)는 맨체스터 대학 수학과의 수리통계학 Reader이며 [JUNIPER 모델링 컨소시엄](https://maths.org/juniper/) 및 모델링 그룹 [SPI-M](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)의 일원이고, [과학자문그룹 긴급상황대응(Scientific Advisory Group for Emergencies, SAGE)](https://www.gov.uk/government/organisations/scientific-advisory-group-for-emergencies)에 기여하고 있습니다.

[Rachel Thomas](https://plus.maths.org/content/people/index.html#Rachel)는 *Plus*의 편집자입니다.

이 글에 도움을 주신 옥스퍼드 대학의 의료통계학 및 역학 교수 [Sarah Walker](https://www.ndm.ox.ac.uk/team/ann-sarah-walker)에게 감사드립니다. 그녀는 ONS 조사의 학술 협력팀 중 한 명입니다.

*이 글은 **JUNIPER**와의 협력의 일환으로 제작되었습니다. JUNIPER는 Cambridge, Warwick, Bristol, Exeter, Oxford, Manchester, Lancaster 대학의 학자들로 구성된 Joint UNIversity Pandemic and Epidemic Response 모델링 컨소시엄입니다. 이들은 다양한 수학적 및 통계적 기법을 사용하여 COVID-19 통제에 관한 긴급한 질문들을 다루고 있습니다. JUNIPER와 함께 제작한 더 많은 콘텐츠는 **여기**에서 확인할 수 있습니다.*

![Juniper logo](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)