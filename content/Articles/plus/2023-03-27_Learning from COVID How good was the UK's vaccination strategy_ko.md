---
title: "COVID-19에서 배우다: 영국의 백신 접종 전략은 얼마나 효과적이었는가?"
date: 2023-03-27
---

> [!NOTE]
> https://plus.maths.org/content/learning-covid-did-we-get-vaccination-strategy-right
>
> 취약 계층을 먼저 백신 접종하는 것이 좋은 선택이었을까? 사후 분석을 통해 이 질문을 평가한다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/vaccine_frontpage_0_0.jpg?itok=Atibwhjf)

마치 평생 전 일처럼 느껴질 수 있지만, 우리 대부분이 첫 COVID-19 백신 접종을 간절히 기다렸던 때로부터 이제 겨우 2년밖에 지나지 않았다. 그것은 우리가 견뎌왔던 제약에서 벗어나는 중요한 한 걸음이었다.

다행히도 영국의 백신 접종 순서는 명확했기에 우리 모두 자신이 어디에 속하는지 알 수 있었다. 요양원 거주자와 직원이 첫 번째 우선순위 그룹을 형성했다. 그 후에는 연령대별로 진행되었으며, 가장 고령자부터 아래로 내려가는 방식이었고, 임상적으로 취약한 사람들과 최전선 보건 및 사회복지 종사자도 초기 우선순위 그룹에 포함되었다. 이 접근법의 기본 아이디어는 가장 취약한 사람들을 신속하게 보호하고 의료 시스템을 유지하는 것이었다.

![Vaccine](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2020/vaccine/vaccine_normal.jpg)

사후 평가를 통해 영국의 백신 접종 전략을 검토할 수 있다.

이 접근법은 2020년 12월 [백신접종 및 면역 합동위원회](https://www.gov.uk/government/groups/joint-committee-on-vaccination-and-immunisation) (JCVI)에 의해 잉글랜드에 권고되었지만, JCVI가 선택할 수 있었던 유일한 방법은 아니었다. 다른 접근법은 가장 취약한 사람들이 아니라 질병을 전파할 가능성이 가장 높은 사람들에게 먼저 백신을 제공하는 것이었다.

이것은 당시 전파를 주도하고 있던 젊은 사람들이 먼저 백신을 맞는다는 것을 의미했을 것이다. 전파가 감소하면 취약한 사람들도 보호될 것이다. 일반적으로 백신이 있는 감염병을 다룰 때, 두 전략 중 어느 것 — 취약 계층 우선 접종과 고전파자 우선 접종 — 이 병원 입원과 사망을 최소화하는 데 더 나은지는 즉시 명확하지 않다.

> 전염병 수리모형에서는 이것을 '직접 보호(direct protection)' 대 '간접 보호(indirect protection)' 전략이라고 부른다. 직접 보호는 취약 계층에게 백신을 접종하여 그들이 감염되어도 중증으로 발전할 확률을 낮추는 것이고, 간접 보호는 전파력이 높은 집단(예: 사회활동이 활발한 젊은층)에게 먼저 접종하여 지역사회 전체의 감염 전파를 억제함으로써 결과적으로 취약 계층이 바이러스에 노출될 기회 자체를 줄이는 것이다. 이 두 전략의 최적 균형점은 질병의 특성(전파율, 치명률), 백신의 효능, 인구 구조, 그리고 유행의 단계에 따라 달라진다. 수리적으로는 기초재생산수($R_{0}$), 백신 효능(vaccine efficacy), 연령별 접촉 행렬(contact matrix) 등의 매개변수를 이용한 최적화 문제로 정식화할 수 있다.

백신 우선순위 결정과 관련하여 영국은 백신 접종 프로그램을 제공하는 대부분의 다른 국가들과 대체로 일치했지만, 2021년 초에 내린 또 다른 결정이 영국을 두드러지게 만들었다. 처음에는 캐나다만이 유사하게 행동했는데, 그것은 1차와 2차 백신 접종 사이의 간격을 3주에서 12주로 늘리는 것이었다.

이것은 부분적으로는 영국 백신 프로그램의 주요 초기 구성 요소였던 AstraZeneca 백신이 더 긴 간격으로 더 잘 작동한다는 새로운 증거 때문이었다. 그러나 이것은 또한 우선순위의 문제이기도 했다. 제한된 백신 용량과 배포 수단, 그리고 Alpha 변이가 우리를 위협하고 있는 상황에서 사용 가능한 자원의 최적 사용이 핵심이었다. 1차와 2차 접종 사이의 간격을 늘리는 것은 더 많은 사람들이 단일 접종의 부분적 보호를 빠르게 제공받을 수 있다는 것을 의미했다. 간격을 짧게 유지하는 것은 더 적은 수의 사람들이 이중 접종의 완전한 보호를 빠르게 제공받을 수 있다는 것을 의미했을 것이다. 어느 옵션을 선택할지에 대한 결정은 명확하지 않았다. (나중에 5월에 병원 입원이 증가하고 Delta 변이에 대해 단일 접종만으로 제공되는 보호 수준에 대한 우려가 있을 때, 간격은 다시 8주로 줄어들었다.)

> 이 결정의 수학적 핵심은 제한된 자원 하에서의 최적화 문제였다. $N$명의 접종 가능 인구와 시간 $t$까지 $V(t)$개의 백신 용량이 있을 때, 각 개인 $i$에게 시간 $t_{i,1}$에 1차 접종, $t_{i,2}$에 2차 접종을 할당하는 문제를 생각해보자. 목적 함수는 전체 사망자 수 또는 입원 환자 수 최소화이고, 제약 조건은 $\sum_{i} \mathbb{1}(t_{i,1} \leq t) + \mathbb{1}(t_{i,2} \leq t) \leq V(t)$ 이다. 1차 접종은 부분적 면역(예: 70% 효능)을, 2차 접종은 완전한 면역(예: 95% 효능)을 제공한다. 간격을 늘리면 더 많은 사람이 부분 면역을 얻지만, 완전 면역을 얻는 시점이 늦어진다. 이 트레이드오프의 최적점은 유행 곡선의 형태와 백신 공급 속도에 따라 달라진다. 영국의 결정은 유행이 급증하는 시기에 "부분 보호라도 빨리 많은 사람에게"라는 원칙이 합리적이라는 판단이었다.

당시 JCVI는 이러한 결정들을 신속하게, 그리고 제한된 데이터를 기반으로 내려야 했다. 이제 사후 판단의 이점을 가지고, 우리는 그들이 올바른 선택을 했는지 말할 수 있을까?

COVID-19 팬데믹에 대한 우리의 모든 보도는 [여기](https://plus.maths.org/content/tags/covid-19)에서 볼 수 있다.

이것은 [JUNIPER 모델링 컨소시엄](https://maths.org/juniper/)의 역학자 팀이 최근 [Nature Communications](https://www.nature.com/articles/s41467-023-35943-0.epdf?sharing_token=lqm7Rx1jkFLUOc0AriUpZ9RgN0jAjWel9jnR3ZoTv0NRRPM87_h_pV33kghFM_gy4pDjwBs96zyq_NE3pmdXlv_UDIiXePKJbW-tOPL1rgBCQR7TJAwmC9kNxZZsR7WAViMfp5wXDkRWyoYevVmBQMrDIXGh3PzlWLkTxu92cSk%3D)에서 다룬 질문이다. 그들이 내놓은 답은 "그렇다"이다. 그들의 연구는 가장 취약한 그룹에게 먼저 백신을 제공하는 것이 다른 전략들과 비교하여 가장 큰 즉각적인 영향을 미쳤다는 것을 보여준다. 12주 간격도 유익했다. 팀은 이것이 백신 캠페인의 첫 10개월 동안 32,000에서 72,000건의 병원 입원과 4,000에서 9,000건의 사망을 예방했다고 추정했다.

이 최신 연구를 수행한 팀은 University of Warwick의 [연구 그룹](https://warwick.ac.uk/fac/cross_fac/zeeman_institute/)의 일부를 형성하며, 그들의 결과는 팬데믹 동안 영국 정책을 알리는 데 중요한 역할을 했다. 무엇보다도 그들은 2021년에 우리를 봉쇄에서 벗어나게 한 [로드맵](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/965011/COVID-19_Response_-_Spring_2021___Summary_-_Easy_Read_.pdf)을 지시하는 데 도움을 준 여러 그룹 중 하나였으며, [과학적 자문 그룹](https://www.gov.uk/government/organisations/scientific-advisory-group-for-emergencies) (SAGE)에 결과를 제공한 모델링 그룹 [SPI-M-O](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)에 기여했다.

그룹의 수학적 모형은 주어진 시작 조건에서 팬데믹이 어떻게 전개될 수 있는지에 대한 감각을 제공하도록 설계되었으며, 놀라울 정도로 정확한 것으로 입증되었다(자세한 내용은 [여기](https://plus.maths.org/content/shining-light-covid-modelling)를 참조). 그룹의 디렉터인 [Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/)은 JCVI의 회원이었으며 당시 그 조언에 기여했다. 이 최신 노력은 수학적 모델링이 제공할 수 있는 비판적 렌즈를 통해 이러한 권고사항들을 평가하는 것을 의미했다.

### 다양한 시나리오

*Nature Communications*에 게재된 연구의 핵심에는 일련의 가정들을 기반으로 유행병이 어떻게 진화할 수 있는지 — 또는 이 경우에는 어떻게 진화했을 수 있는지 — 를 시뮬레이션할 수 있는 복잡한 수학적 모형이 있다. 이 모형은 인구의 연령 구조(사회적 접촉 및 중증 질환의 위험 측면에서)와 백신 접종 및 바이러스의 다양한 변이의 영향을 포착한다 — 모형에 대한 자세한 내용은 [이 기사](https://plus.maths.org/content/learning-covid-did-we-get-vaccination-strategy-right#model)의 끝에서 찾을 수 있다.

이 모형을 갖춘 팀은 백신 접종 전략이 달랐다면 무엇이 일어났을 수 있는지 탐구하기 시작했다. 그들은 네 가지 다른 시나리오를 고려했다:

- **실제 실행된 전략:** 실제로 일어난 것을 반영하는 시나리오.
- **백신 접종 순서 역전:** 백신 접종 순서가 역전되어 전파에 가장 책임이 있는 가장 젊은 성인들이 먼저 접종을 받지만, 1차와 2차 접종 사이의 간격은 12주로 고정된 시나리오.
- **짧은 간격 - 동일한 효과:** 사람들이 실제로 실행된 것과 동일한 순서로 1차 접종을 받지만, 2차 접종은 3주 간격 후에 제공되는 시나리오. 이 시나리오에서는 백신이 12주 간격에서와 마찬가지로 효과적으로 작동한다고 가정한다.
- **짧은 간격 - 덜 효과적:** 위의 시나리오 3과 동일하지만, 간격이 짧을 때 백신 효능의 잠재적 차이도 포착하는 시나리오.

> 이 네 가지 시나리오는 정책 공간의 주요 축들을 탐색한다. 시나리오 1(기준선)과 시나리오 2(순서 역전)는 "누구에게 먼저 접종할 것인가"라는 targeting 문제를 다루고, 시나리오 1과 시나리오 3, 4는 "언제 2차 접종을 할 것인가"라는 timing 문제를 다룬다. 시나리오 3과 4의 차이는 용량-반응 관계(dose-response relationship)의 불확실성을 반영한다. 실제 정책 결정에서는 이러한 불확실성이 매우 중요한데, 백신의 작동 메커니즘이 완전히 밝혀지기 전에 결정을 내려야 하기 때문이다. 수학적으로 이것은 매개변수 공간의 sensitivity analysis와 robustness 분석의 문제이다.

### 결과

아래 차트는 2020년 10월부터 2021년 10월까지의 기간 동안 모델링 작업의 결과를 보여준다. 위 차트는 추정된 일일 사망자를 보여주고 아래 차트는 추정된 병원 입원을 보여준다.

![model projections of daily deaths](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2023/vaccination_strategy/deaths_projections.png)

![model projections of hospital admissions](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2023/vaccination_strategy/admissions_projections.png)

이 차트들은 위에서 언급한 네 가지 시나리오에 대한 관찰된 사망 수준(위)과 병원 입원(아래)을 비교한다. 그림 출처: [Keeling 등의 The impacts of SARS-CoV-2 vaccine dose separation and targeting on the COVID-19 epidemic in England](https://www.nature.com/articles/s41467-023-35943-0)

파란 점은 관찰된 데이터, 즉 실제로 발생한 사망과 병원 입원을 나타낸다. 검은 선은 첫 번째 시나리오에 대한 모형 출력을 나타내며, 실제로 실행된 백신 접종 전략을 반영한다 — 이것이 파란 점을 밀접하게 따라가는 것을 볼 수 있다. 녹색 점선은 백신 접종 순서가 역전된 시나리오 2를 나타낸다. 빨간 선과 보라색 파선은 1차와 2차 백신 접종 사이의 간격이 단지 3주인 시나리오 3과 4를 나타낸다.

사망자 수(위 차트)에 관해서는, 실제로 실행된 전략을 반영하는 시나리오 1이 시나리오 2, 3, 4보다 명백히 더 나은 성과를 보였다. 병원 입원(아래 차트)에 대해서는, 시나리오 2(백신 접종 순서 역전)만이 다른 것들보다 더 나은 성과를 보이지만, 이것도 Delta 변이가 새로운 유행을 일으킨 약 2021년 6월 이후부터만 그렇다.

우리는 또한 기본 시나리오 1과 비교하여 시나리오 2, 3, 4에서 발생했을 총 추가 사망자와 병원 입원이 무엇을 의미하는지 살펴볼 수 있다. 이것은 아래 차트에 나와 있다. 실제 선 주변의 음영 영역은 추정치를 둘러싼 불확실성을 나타낸다.

![model projections of total additional deaths](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2023/vaccination_strategy/cumulative_deaths_projections.png)

![model projections of total additional hospital admissions](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2023/vaccination_strategy/cumulative_admissions_projections.png)

대안적 가정들로부터 예측된 누적 추가 사망자(위)와 병원 입원(아래). 이전과 마찬가지로 녹색 점선은 백신 접종 순서가 역전된 시나리오 2를 나타낸다. 빨간 선과 보라색 파선은 1차와 2차 접종 사이의 간격이 단지 3주인 시나리오 3과 4를 나타낸다. 음영 영역은 95% 예측 구간이다: 실제 값이 이 영역 어딘가에 있을 것이라는 95% 신뢰를 나타낸다. 그림 출처: [Keeling 등의 The impacts of SARS-CoV-2 vaccine dose separation and targeting on the COVID-19 epidemic in England](https://www.nature.com/articles/s41467-023-35943-0)

> 95% 예측 구간(prediction interval)은 신뢰구간(confidence interval)과는 다른 개념이다. 신뢰구간은 매개변수의 불확실성을 나타내지만, 예측 구간은 매개변수 불확실성과 모형의 확률적 변동(stochastic variation) 모두를 포함한다. 전염병 모형에서는 초기 조건의 작은 차이나 무작위 사건들이 큰 차이를 만들 수 있기 때문에 예측 구간이 넓어진다. 수학적으로 예측 구간은 $\text{Var}(\hat{Y}) = \text{Var}(\hat{\theta}) + \text{Var}(\epsilon)$ 형태로 표현되는데, 여기서 첫 번째 항은 매개변수 추정의 불확실성, 두 번째 항은 모형의 내재적 변동성이다. 이 연구에서 음영 영역이 비교적 넓은 것은 모형이 많은 불확실한 매개변수를 가지고 있으며, 전염병의 미래 경로가 본질적으로 예측하기 어렵다는 것을 정직하게 반영한다.

모든 종류의 백신 접종 순서를 탐색하는 추가 모델링 작업은 이 차트들이 시사하는 바를 뒷받침한다: 실제로 채택된 전략은 사망자에 관한 한 최적에 가까운 것으로 보인다. 장기적으로(Alpha로 인한 유행 이후와 Delta 유행 포함) 총 병원 입원 수를 살펴볼 때만 이 단순한 전략이 차선이 된다: 그 후기 단계들에서 우리는 전체 인구에 걸쳐 광범위한 수준의 면역을 생성하는 전략으로 전환했다면 더 적은 병원 입원을 보았을 것이다.

이 모든 것은 당신의 직관이 이미 당신에게 제안했을 수 있는 것을 확인해준다. 2020년 말과 2021년 초에 그랬던 것처럼 인구에 많은 감염이 있을 때, 취약한 사람들은 신속하게 보호되어야 하며, 전파를 주도하는 사람들을 우선시하는 백신 접종 전략이 효과적이 될 때까지 기다릴 시간이 없다. 그러나 인구의 감염 수준이 낮다면, 고전파자에게 먼저 백신을 제공하는 것이 성과를 거둘 수 있다.

> 이것은 전염병 동역학의 기본 원리를 반영한다. 유행 초기나 급증기($R_{t} > 1$인 시기)에는 감염이 지수적으로 증가하므로, 취약 계층이 감염될 위험이 매우 높고 임박해 있다. 이때는 직접 보호 전략이 효과적이다. 반면 유행이 통제되고 있는 시기($R_{t} \approx 1$인 시기)에는 전파 사슬을 끊는 것이 더 중요해진다. 수학적으로 이것은 최적 제어 이론(optimal control theory)의 시간 의존적 문제로 볼 수 있다. 목적 함수는 시간에 따라 가중치가 달라지는데, 초기에는 취약 계층의 즉각적 보호가 높은 가중치를, 후기에는 집단 면역 형성이 높은 가중치를 받는다. 이것은 정책이 유행의 단계에 따라 적응적으로 변해야 한다는 것을 의미한다.

더 일반적으로, 모든 질병과 모든 상황에서 최적인 단일 백신 접종 전략은 없다. 많은 것이 질병과 백신의 특성, 인구의 구성과 개인들이 감염에 반응하는 다양한 방식, 그리고 당신이 유행병의 어느 단계에 있는지에 달려 있다.

다른 요인들도 중요하다. 예를 들어, JCVI가 권고한 전략은 이해하기 쉽다는 장점이 있었다. 만약 우리가 누가 언제 백신을 접종받아야 하는지에 대한 혼란스러운 일련의 지시사항을 제시받았다면, 더 적은 사람들이 접종을 받으러 갔을 것이다.

### 현실은 어떤 모형보다도 복잡하다

모든 수학적 모형과 마찬가지로, JUNIPER 연구자들이 사용한 모형은 실제 사건에 대한 근사치일 수 있는 일련의 가정들에 기반한 현실의 단순화이다. 예를 들어, 팀은 그들이 조사한 네 가지 시나리오 모두에 대해 사람들의 행동이 현실에서와 동일할 것이라고 가정했다: 사람들은 현실에서와 동일한 수준의 질병 감염에 대한 주의를 보일 것이고, 각 연령 그룹의 백신 접종률도 동일할 것이다.

그것은 아마도 일이 전개되었을 방식이 아니었을 것이다. 예를 들어, 젊은 사람들이 먼저 백신을 접종받았고, 취약한 사람들을 보호하지 않은 결과로 사망자와 병원 입원이 높게 유지되었다면, 사람들은 예방 행동을 바꿨을 수 있고, 백신을 제공받은 연령 그룹의 백신 접종률도 달랐을 수 있다.

![Road sign for vaccination centre](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2023/vaccination_strategy/640px-Covid-19_Vaccination_Centre_sign_in_Newbury%2CUK_1.jpg)

영국에서 채택된 백신 접종 전략의 좋은 점은 이해하기 쉬웠다는 것이다. 사진: [KY Chow](https://commons.wikimedia.org/wiki/File:Covid-19_Vaccination_Centre_sign_in_Newbury,UK_1.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en).

> 이것은 모델링에서 "행동 피드백(behavioral feedback)" 또는 "적응적 행동(adaptive behavior)"이라고 불리는 현상이다. 사람들은 유행 상황을 관찰하고 그에 따라 행동을 조정한다. 만약 사망자가 많으면 자발적으로 사회적 거리두기를 강화하고, 상황이 나아지면 완화한다. 수학적으로 이것은 모형에 피드백 루프를 추가하는 것을 의미한다. 예를 들어, 접촉률 매개변수 $\beta(t)$가 현재 감염자 수 $I(t)$의 함수가 되도록 $\beta(t) = \beta_{0} f(I(t))$로 모델링할 수 있다. 이러한 모형은 "행동-질병 결합 모형(behavior-disease coupled models)"이라고 불리며, 게임 이론이나 경제학의 개념을 통합한다. 이 연구에서는 이러한 피드백을 명시적으로 모델링하지 않았는데, 이것이 모형의 한계이지만, 동시에 정책 효과를 분리해서 평가하기 위해서는 다른 요인들을 통제해야 한다는 방법론적 선택이기도 하다.

모형의 한계와 그 출력 내의 불확실성을 인식하는 것이 중요하다. 이러한 출력은 무엇이 일어날 것인지, 또는 이 경우 무엇이 일어났을 것인지에 대한 확실한 예측이 결코 아니다. 그러나 그것들은 매우 넓고 복잡한 요인들의 그물망과 다양한 정보를 고려하는 극도로 정교한 추측으로 볼 수 있으며, 이는 수학적 접근만이 가능하게 하는 것이다.

모든 것을 고려할 때, JUNIPER 팀은 그들의 모델링 작업이 JCVI가 내린 결정들이 당시에 내릴 수 있었던 최선이었고, 견고하고 실행 가능하며 단순한 우선순위 테스트였다는 좋은 증거를 제공한다고 믿는다. "공중 보건 결정은 종종 제한된 데이터를 기반으로 내려져야 하므로 과학적 이해의 잠재적 변화에 가능한 한 견고해야 한다"고 그들은 [논문](https://www.nature.com/articles/s41467-023-35943-0.epdf?sharing_token=lqm7Rx1jkFLUOc0AriUpZ9RgN0jAjWel9jnR3ZoTv0NRRPM87_h_pV33kghFM_gy4pDjwBs96zyq_NE3pmdXlv_UDIiXePKJbW-tOPL1rgBCQR7TJAwmC9kNxZZsR7WAViMfp5wXDkRWyoYevVmBQMrDIXGh3PzlWLkTxu92cSk%3D)에서 쓴다.

"2020년 말과 2021년 초에 JCVI가 제공한 조언은 새로 출현한 Alpha 변이에 대한 백신 효능에 관한 매우 제한된 데이터를 기반으로 했으며, 앞으로의 감염 유행이나 [백신이 제공하는] 보호의 약화에 대한 지식이 없는 상태였다. 그러한 조건 하에서 단순하면서도 예방적인 전략이 최적이며, 가장 필요로 하는 개인들에게 신속하게 광범위한 보호를 제공한다."

> 이것은 의사결정 이론에서 "견고성(robustness)" 또는 "강인성(resilience)"의 개념을 반영한다. 불확실성이 큰 상황에서는 특정 시나리오에 최적화된 복잡한 전략보다, 다양한 시나리오에서 "충분히 좋은" 성과를 내는 단순한 전략이 더 바람직할 수 있다. 이것은 "min-max regret" 원칙이나 "satisficing" 개념과 연결된다. 수학적으로는, 미래 상태에 대한 확률 분포 $P(\omega)$가 불확실할 때, $\max_{\text{strategy}} \min_{\omega} U(\text{strategy}, \omega)$ 형태의 최악의 경우 최적화(worst-case optimization)를 고려할 수 있다. 영국의 "연령별 우선순위" 전략은 이런 의미에서 견고했다: 바이러스가 어떻게 진화하든, 백신 효능이 정확히 어느 정도든, 고령자가 더 취약하다는 기본 사실은 변하지 않았기 때문이다.

### 모형

*Nature Communications*에 게재된 연구의 핵심에는 소위 SEIR 모형이 있다. 역학에서 널리 사용되는 SEIR 모형은 인구를 질병 상태에 따라 그룹으로 나눈다: 질병에 감염될 수 있는 사람(S, susceptible), 질병에 노출되었지만 아직 감염성이 없는 사람(E, exposed), 감염성이 있는 사람(I, infectious), 그리고 회복했거나 슬프게도 사망한 사람(R, recovered).

사람들이 한 클래스에서 다른 클래스로 이동하는 속도는 수학 방정식([미분방정식](https://plus.maths.org/content/maths-minute-differential-equations)을 정확히 말하면)을 사용하여 설명할 수 있다. 이 방정식들은 질병의 특수성과 그것이 퍼지는 세계를 포착하는 매개변수들에 의존한다: 사람들이 얼마나 쉽게 감염되는지, 감염성을 갖게 되고 회복하기까지 얼마나 걸리는지, 사망할 확률 등. 이러한 매개변수의 값은 실제 세계에서 수집된 데이터로부터 추정할 수 있다. (이 유형의 모형에 대한 자세한 내용은 Matt Keeling의 *Plus* 기사 [The mathematics of diseases](https://plus.maths.org/content/mathematics-diseases)에서 찾을 수 있다.)

매개변수 값을 추정하고 나면 컴퓨터를 사용하여 한 그룹에서 다른 그룹으로의 사람들의 이동을 시뮬레이션하여 유행병이 어떻게 전개될 수 있는지에 대한 감각을 얻을 수 있다. 그것이 일반적인 아이디어이지만, JUNIPER 팀이 탐구하고자 했던 현실이 훨씬 더 복잡했기 때문에, 그들은 추가 그룹을 추가하여 단순한 SEIR 설정을 크게 확장했다.

예를 들어, 감수성 그룹 S는 백신 접종 상태에 따라 여러 하위 그룹으로 분할되었다. 노출 그룹 E는 사람들이 노출에 다르게 반응한다는 사실을 반영하는 하위 그룹으로 나뉘었다. 감염성 그룹 I는 증상이 있는 사람과 없는 사람으로 나뉘었고, 또한 사람이 감염된 변이에 따라 나뉘었다. 아래 다이어그램은 이 접근법에 대한 감각을 제공한다.

![schematic of SEIR model](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2023/vaccination_strategy/SEIR.png)

이 다이어그램은 모형의 다양한 구획들과 그들 사이의 흐름을 보여준다. 감염은 빨간 화살표로 표시되고(크기가 위험에 대한 어느 정도의 표시를 제공함), 회복은 검은 화살표로 표시되며, 2회 접종 백신은 녹색으로, 보호 약화는 연한 파란색으로 표시된다. "감염(Infection)" 구획 자체는 추가 하위 그룹으로 더 분할되었다. 그림 출처: [Keeling 등의 The impacts of SARS-CoV-2 vaccine dose separation and targeting on the COVID-19 epidemic in England](https://www.nature.com/articles/s41467-023-35943-0)

> 이 다이어그램은 구획 모형(compartmental model)의 전형적인 구조를 보여준다. 각 상자는 상태(state)를, 화살표는 전이(transition)를 나타낸다. 수학적으로 각 화살표는 미분방정식의 항에 대응한다. 예를 들어, S에서 E로의 전이는 $\frac{dS}{dt} = -\beta S I / N$ 형태의 항을 만들고, E에서 I로의 전이는 $\frac{dE}{dt} = \beta S I / N - \sigma E$ 항을 만든다. 여기서 $\beta$는 전파율, $\sigma$는 잠복기의 역수이다. 이 모형에서는 백신 접종을 모델링하기 위해 S가 여러 하위 구획($S_{0}, S_{1}, S_{2}$ 등, 접종 횟수별)으로 나뉘고, 각각 다른 감수성을 갖는다. 변이를 모델링하기 위해 I도 여러 하위 구획($I_{\text{Alpha}}, I_{\text{Delta}}$ 등)으로 나뉜다. 전체 모형은 이러한 모든 구획에 대한 결합 미분방정식 시스템이 되며, 수백 개의 방정식으로 구성될 수 있다.

또한 연령이 COVID-19 감염의 심각성을 결정하는 핵심이었기 때문에, 모형 청사진은 21개의 5년 연령 그룹(0-4세, 5-9세, 그리고 95-99세를 거쳐, 마지막으로 100세 이상)을 반영하기 위해 21번 복제되었고, 잉글랜드의 7개 다른 지리적(NHS) 지역의 유행 역학을 반영하기 위해 추가로 7번 복제되었다. 결정적으로, 모형은 또한 사람들이 얼마나 신중했는지 — 예를 들어, 다른 사람들과 얼마나 섞였는지, 그리고 그들이 검사를 받고 격리했는지 등 — 를 반영하는 매개변수를 포함한다.

모형의 모든 매개변수 — 주어진 변이의 감염성, 백신이 감염에 대해 제공하는 보호, 예방 매개변수 등 — 의 값은 당시에 수집된 이용 가능한 데이터로부터 신중하게 추정되었다. (모형의 다양한 구성 요소와 그것들이 어떻게 결합하여 전체 모형을 형성하는지에 대해 더 알아보려면, 팀의 [논문](https://www.nature.com/articles/s41467-023-35943-0.epdf?sharing_token=lqm7Rx1jkFLUOc0AriUpZ9RgN0jAjWel9jnR3ZoTv0NRRPM87_h_pV33kghFM_gy4pDjwBs96zyq_NE3pmdXlv_UDIiXePKJbW-tOPL1rgBCQR7TJAwmC9kNxZZsR7WAViMfp5wXDkRWyoYevVmBQMrDIXGh3PzlWLkTxu92cSk%3D)을 참조하라.)

모형을 사용하여 다양한 시나리오를 시뮬레이션하기 위해서는, 연령 그룹이 모형의 백신 접종 관련 클래스를 통과하는 순서와, 그들이 그렇게 하는 시간 프레임을 변경한다.

> 시뮬레이션의 실제 구현은 상당히 복잡하다. 21개 연령 그룹 × 7개 지역 × (여러 질병 상태 구획)으로, 시스템은 수천 개의 결합된 미분방정식으로 구성될 수 있다. 이러한 시스템을 수치적으로 풀기 위해서는 Runge-Kutta 방법이나 다른 ODE 솔버를 사용한다. 백신 접종 정책을 변경하는 것은 시간 의존적 제어 함수를 바꾸는 것에 해당한다. 예를 들어, $u_{i}(t)$를 연령 그룹 $i$의 시간 $t$에서의 접종률이라고 하면, 다른 시나리오는 다른 함수 $u_{i}(t)$에 대응한다. 계산적으로 이것은 매우 까다로운데, 특히 확률적 변동을 포함시키기 위해 모델을 여러 번(예: 수백 또는 수천 번) 실행해야 할 때 그렇다. 이것이 이러한 연구에 고성능 컴퓨팅 자원이 필요한 이유이다.

### 이 기사에 대하여

이 기사는 2023년 2월 *Nature communications*에 게재된 Keeling 등의 논문 [The impacts of SARS-CoV-2 vaccine dose separation and targeting on the COVID-19 epidemic in England](https://www.nature.com/articles/s41467-023-35943-0)를 기반으로 한다.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)는 *Plus*의 편집자이다. 그녀는 이 기사에 대한 도움을 준 [Ed Hill](https://warwick.ac.uk/fac/sci/maths/people/staff/ed_hill/)과 [Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/)에게 감사한다.

*이 기사는 JUNIPER, Joint UNIversity Pandemic and Epidemic Response 모델링 컨소시엄과의 협력의 일부이다. JUNIPER는 Cambridge, Warwick, Bristol, Exeter, Oxford, Manchester 및 Lancaster 대학의 학자들로 구성되어 있으며, COVID-19의 통제에 관한 시급한 질문들을 다루기 위해 다양한 수학적 및 통계적 기법을 사용하고 있다. JUNIPER와 함께 제작된 더 많은 콘텐츠를 여기에서 볼 수 있다.*

![Juniper logo](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)