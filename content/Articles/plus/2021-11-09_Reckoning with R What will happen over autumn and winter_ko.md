---
title: R값으로 계산하기 - 가을과 겨울에 무슨 일이 일어날까?
date: 2021-11-09
---

> [!NOTE]
> https://plus.maths.org/content/reckoning-r-what-will-happen-over-autumn-and-winter
>
> 다시 사회적 접촉을 줄여야 할까? 12세에서 15세까지 백신 접종이 효과적일까? 부스터 샷은? 레디 레커너가 답을 제공한다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/frontpage_8.jpg?itok=BkcWBkv3)

12세에서 15세 사이의 청소년들에게 백신을 접종하는 것이 올 가을과 겨울 COVID-19의 확산에 실제로 영향을 미칠까? 백신 부스터 프로그램은 어떨까? 혹은 재택근무나 마스크 착용 의무화 같은 영국 정부의 Plan B에서 구상된 조치들은?

이러한 질문들이 모델링 전문 과학 패널인 [SPI-M](https://www.gov.uk/government/groups/scientific-pandemic-influenza-subgroup-on-modelling)(Scientific Pandemic Influenza Group on Modelling)에 제기되었고, 그들은 지난주 최신 연구 결과 요약을 발표했다. 답은 부분적으로 Bristol 대학의 두 역학자 [Ellen Brooks-Pollock](https://www.bristol.ac.uk/people/person/Ellen-Brooks%20Pollock-9ffd9ff9-0949-49c4-97f7-bae51aa23d51/)과 [Leon Danon](https://research-information.bris.ac.uk/en/persons/leon-danon)로부터 나왔다. 이들은 SPI-M의 구성원이면서 동시에 [JUNIPER 모델링 컨소시엄](https://maths.org/juniper/)의 일원이기도 하다. (다른 보고서들은 [Imperial College](https://www.imperial.ac.uk/stories/coronavirus-modelling/), [LSHTM](https://cmmid.github.io/topics/covid19/), [University of Warwick](https://plus.maths.org/content/winter-coming-where-are-we-going)의 그룹들이 제출했다.)

아래 그래프는 Bristol 팀이 가을과 겨울 동안 [R값](https://plus.maths.org/content/maths-minute-r0-and-herd-immunity)이 어떻게 변할지에 대한 예측을 보여준다. 이제 우리 대부분이 알고 있듯이, $R$값은 한 감염자가 평균적으로 감염시키는 사람의 수를 의미한다. $R$값이 1보다 크면 감염이 지수적으로 증가하고, $R$값이 1보다 작으면 감염이 감소한다.

> $R$값은 '재생산지수(reproduction number)'라고도 불리며, 전염병 확산의 속도를 이해하는 핵심 지표다. 수학적으로 이것은 감염병 동역학의 기본방정식에서 나오는 고유값(eigenvalue)과 관련이 깊다. 만약 한 감염자가 평균 2명을 감염시킨다면($R = 2$), 다음 세대에는 $2^{n}$명의 감염자가 생기는 기하급수적 증가가 일어난다. 따라서 $R = 1$이 일종의 '임계점(critical threshold)'이 되는데, 이는 물리학의 상전이 현상과 비슷한 개념이다. 집단면역의 수학적 조건도 이 $R$값으로부터 도출되는데, 감수성 있는 개체의 비율이 $1 - 1/R_{0}$ 이하로 떨어지면 전염병이 사라지기 시작한다.

![A schematic of the Warwick model](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/ready_reckoner/r_estimates.jpg)

그림 1: 활동 접촉 비율의 함수로서 $R$값의 추정치. 패널 A는 COVID 완화 조치나 접촉 추적이 없다고 가정하고, 패널 B는 이 두 가지가 모두 시행되며 감염 예방에 25% 효과적이라고 가정한다.

(그림은 Bristol 팀의 [보고서](https://www.gov.uk/government/publications/university-of-bristol-trade-off-between-population-immunity-and-return-to-work-for-covid-19-control-autumn-and-winter-2021-scenarios-12-october-202)에서 가져왔으며, 허가를 받아 사용했다.)

이 그래프는 인구에서 활동하는 직장 및 여가 접촉의 비율에 따라 $R$이 어떻게 변할 것으로 추정되는지를 보여준다. 0%는 극단적인 봉쇄 상태에 해당하고, 100%는 COVID 이전의 정상적인 행동에 해당한다.

왼쪽 패널은 COVID 방역 조치(예: 마스크 착용과 사회적 거리두기)와 접촉 추적이 없다고 가정한다. 오른쪽 패널은 COVID 방역 조치와 접촉 추적이 있고, 이 두 조치가 함께 감염 예방에 25% 효과적이라고 가정한다.

색깔들은 다양한 시나리오를 나타낸다. 노란색은 기준 시나리오로, 부스터 샷이 없고 12세에서 15세까지의 백신 접종이 없으며, 기본 재생산지수(어떠한 개입이나 백신도 없을 때의 $R$값)가 7이라고 가정한다. 이것은 인구에 면역이 전혀 없는 상태에서 델타 변이의 전파 잠재력에 대한 현재의 최선의 추정치다. 초록색은 기준 시나리오에 부스터 백신 접종이 추가된 경우를 나타낸다. 파란색은 12세에서 15세까지의 백신 접종이 추가된 시나리오로, 접종률 65%를 가정한다. 분홍색은 앞의 두 조치가 모두 있는 상황에서, 인구 내 보호 면역이 20% 감소하는 우려 변이(variant of concern)가 나타나는 시나리오를 나타낸다.

> 기본 재생산지수 $R_{0} = 7$이라는 값은 델타 변이가 얼마나 전염성이 강한지를 보여준다. 비교하자면, 초기 우한 변이의 $R_{0}$는 약 2.5~3 정도였고, 홍역의 $R_{0}$는 12~18 정도다. 델타 변이는 홍역에 가까운 전염성을 가지고 있어서, 집단면역 달성이 매우 어렵다는 것을 의미한다. 우려 변이의 20% 면역 감소는 수학적으로 유효 $R$값을 $R_{eff} = R_{0}(1 - p_{immune})$에서 면역 비율 $p_{immune}$이 감소하는 것으로 모델링할 수 있다.

당신은 COVID 방역 조치와 접촉 추적이 없는 상태에서, 직장과 여가 접촉에 제한이 없다면, 우려 변이가 없는 경우에도 $R$이 1 이상으로 추정된다는 것을 볼 수 있다. 부스터 백신 접종과 12세에서 15세 백신 접종이 도움이 되지만, COVID 방역 조치와 접촉 추적(오른쪽 패널)이 큰 차이를 만든다. 그리고 직장과 여가 접촉을 제한하는 것(가로축의 왼쪽)도 마찬가지다. 하지만 우려 변이는 상당한 문제를 일으킬 수 있다.

### 레디 레커너(Ready Reckoner)

팀은 소위 **레디 레커너(ready reckoner)**라는 독창적이고 즉시 사용 가능한 수학적 방법을 사용하여 이러한 추정치를 산출했다. 레디 레커너는 인구 전체에 질병의 확산을 시뮬레이션하는 표준 역학 모델링 기법과는 상당히 다르며, 매우 영리한 방법이다.

> '레디 레커너(ready reckoner)'는 원래 복잡한 계산을 빠르게 수행하기 위한 참조표나 계산 도구를 의미하는 용어다. 여기서는 표준 역학 시뮬레이션 대신, 해석적(analytic) 접근으로 빠르게 $R$값을 추정하는 방법을 가리킨다. 이는 컴퓨터 집약적 시뮬레이션보다 훨씬 빠르면서도 정책적 질문에 답할 수 있는 유연성을 제공한다.

대략적으로 말하면, 레디 레커너 뒤에 있는 일반적 아이디어는 인구 전체의 $R$값을 인구 내 모든 사람들의 개별 $R$값에 대한 가중평균으로 생각하는 것이다. 이 개별 $R$값은 해당 인구가 감염되었을 경우 예상되는, 그들이 감염시킬 다른 사람들의 수를 나타낸다. 어떤 사람의 개별 $R$값은 그들의 나이(이것은 그들이 증상이 있고 감염성이 있을 가능성을 결정한다), 접촉 패턴(사회적 접촉의 수, 맥락, 길이), 그리고 주어진 시간 동안의 접촉이 감염 전파로 이어질 확률로부터 추정할 수 있다.

> 이 접근법의 핵심 통찰은 '이질적 혼합(heterogeneous mixing)' 개념이다. 전통적인 SIR 모델은 인구가 균질하다고 가정하지만, 실제로 사람들의 접촉 패턴은 매우 다양하다. 예를 들어, 교사나 의료 종사자는 학생이나 환자와 많은 접촉을 하고, 재택근무자는 접촉이 적다. 네트워크 이론의 관점에서 보면, 이는 각 노드(개인)가 다른 차수(degree, 연결 수)를 가진 이질적 네트워크다. 수학적으로, 이질적 네트워크에서의 전염병 확산은 차수 분포(degree distribution)에 크게 의존하며, 허브(hub) 역할을 하는 고접촉자들이 전파에 불균형적으로 큰 영향을 미친다.

![Network of people](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/rumours/network.jpg)

레디 레커너의 아이디어는 인구 전체의 $R$값을 인구 내 모든 사람들의 개별 $R$값에 대한 가중평균으로 생각하는 것이다.

이러한 방식으로 인구 전체의 $R$값을 나타내면 개입 조치의 효과를 테스트할 수 있다. 예를 들어, 학교 폐쇄가 $R$에 어떻게 영향을 미칠지 알고 싶다면, 개별 $R$값을 추정할 때 학교 연령대 사람이 학교에서 가진 모든 접촉을 세지 않으면 된다. 재택근무가 $R$에 어떻게 영향을 미치는지 알고 싶다면, 직장에서 발생한 접촉을 세지 않으면 된다. 사람들의 일정 비율이 여전히 학교나 직장에 간다면, 개별 $R$값 추정에서 해당 비율만큼의 학교나 직장 접촉을 끄면 된다.

백신이나 부스터, 그리고 마스크 착용이나 사회적 거리두기 같은 조치들의 효과도 이 아이디어를 사용하여 테스트할 수 있다. 이 둘 모두 한 개인에서 다른 개인으로 감염이 전파될 확률에 영향을 미치며, 이것은 개인의 $R$값 계산에 반영된다. 따라서 계산에서 매개변수를 적절히 조정함으로써 이러한 조치들을 고려할 수 있다.

### 사회적 접촉 데이터

여기서 명백한 반론은 우리가 나라 전체의 모든 개인의 사회적 접촉 패턴을 알 방법이 전혀 없다는 것이다. 하지만 2010년에 [JUNIPER 컨소시엄](https://maths.org/juniper/)의 [Matt Keeling](https://warwick.ac.uk/fac/sci/maths/people/staff/matt_keeling/), [Jon Read](https://www.lancaster.ac.uk/people-profiles/jonathan-read), [Leon Danon](https://research-information.bris.ac.uk/en/persons/leon-danon)을 포함한 역학자 팀이 사람들의 사회적 행동에 대한 깊은 통찰을 제공하는 연구를 수행했다. 그들은 거의 6,000명에게 전날 가졌던 접촉, 이 접촉들이 얼마나 오래 지속되었는지, 접촉에 신체 접촉이 포함되었는지, 그리고 어떤 맥락에서 일어났는지(학교나 직장, 가정, 여가 및 기타 활동) 묻는 [설문조사](https://royalsocietypublishing.org/doi/pdf/10.1098/rspb.2013.1037)를 실시했다.

> 이 사회적 접촉 설문조사는 전염병 모델링의 이정표가 된 연구다. 전통적으로 역학 모델은 인구를 몇 개의 연령 그룹으로 나누고 그룹 간 접촉률을 가정했지만, 이 연구는 실제 개인 수준의 접촉 데이터를 수집했다. 특히 접촉의 '지속 시간'을 기록한 것이 중요한데, 짧은 스쳐지나가는 접촉과 긴 대화는 전파 확률이 매우 다르기 때문이다. 또한 '접촉 행렬(contact matrix)'이라는 개념을 도입하여, 각 연령대가 다른 연령대와 얼마나 접촉하는지를 행렬 형태로 표현했다. 이는 선형대수의 관점에서 전염병 동역학을 이해하는 강력한 도구가 되었다.

개별 $R$값들의 평균을 계산할 때, 이것이 인구 전체의 $R$값 추정치로 사용될 것이기 때문에, 이 방법은 우리가 익숙한 일반적인 평균 개념과 비교하여 몇 가지 조정을 한다. 예를 들어, 많은 접촉을 가진 사람들은 감염을 전파할 가능성이 더 높을 뿐만 아니라 감염에 걸릴 가능성도 더 높기 때문에, 평균은 많은 접촉을 가진 사람들이 적은 접촉을 가진 사람들보다 그 값에 더 많이 기여하도록 구성된다.

![You may have many friends, but in real-life, be very alone.](https://plus.maths.org/latestnews/may-aug08/friends/piccy.jpg)

사회적 접촉 설문조사는 거의 6,000명의 개인에게 전날의 사회적 접촉을 기록하도록 요청했다.

레디 레커너는 이 정보를 사용하여 설문조사에 참여한 각 사람에 대한 개인별 $R$값을 계산한다. 이를 위해서는 정상적인 상황(즉, 마스크나 사회적 거리두기나 백신 접종이 없는 상태)에서 특정 기간의 접촉이 감염 전파로 이어질 확률을 추정해야 한다. 이것은 사회적 제한이 없고 COVID 유행이 지수적으로 증가하던 2020년 3월의 영국 데이터로부터 추정되었다. (이 데이터의 전파율은 당신이 고려하는 기간에 지배적인 변이를 반영하도록 조정된다는 점에 주목하라.)

또한 우리가 원하는 것은 6,000명의 표본이 아니라 전체 인구에 대한 $R$값 추정치이기 때문에, 평균 계산에는 연령과 관련된 조정이 있는데, 이를 통해 설문조사의 각 사람이 일반 인구에서 약 10,000명의 "유사한" 사람들을 대표하게 된다. 여기서 연령이 초점이 되는 이유는 연령이 접촉 패턴과 관련하여 매우 중요한 지표이기 때문이다. 어린이는 학교에 가는 경향이 있고, 20대는 활발한 사회생활을 하는 경향이 있으며, 노인은 집에서 더 많은 시간을 보내는 경향이 있다. 인구 전체의 $R$값이 전체 인구를 대표하도록 하기 위해, 평균은 표본에서 과소 대표된 연령 그룹(전체 인구와 비교하여)의 사람들이 과다 대표된 연령 그룹의 사람들보다 그 값에 더 많이 기여하도록 구성된다.

> 이것은 '가중 평균(weighted average)'의 정교한 응용이다. 단순 평균 $\bar{R} = \frac{1}{N}\sum_{i}R_{i}$가 아니라, 각 개인의 접촉 수와 연령에 따른 가중치 $w_{i}$를 적용하여 $\bar{R} = \frac{\sum_{i}w_{i}R_{i}}{\sum_{i}w_{i}}$ 형태로 계산한다. 특히 '접촉 수에 비례한 가중치'를 사용하는 것은 네트워크 이론의 '친구 역설(friendship paradox)'과 관련이 있다. 평균적으로 당신의 친구들은 당신보다 더 많은 친구를 가지고 있으며, 이는 고접촉자들이 전염병 전파 네트워크에서 더 중요한 역할을 한다는 것을 의미한다. 또한 연령별 가중치는 '층화 표본(stratified sampling)'의 역가중(inverse weighting) 원리를 사용하여, 인구 구조를 정확히 반영하도록 한다.

이러한 계산의 수학적 세부사항을 보려면, Ellen Brooks-Pollock, Jonathan Read, Angela McLean, Matt Keeling, Leon Danon의 [이 논문](https://royalsocietypublishing.org/doi/pdf/10.1098/rstb.2020.0276)을 참조하라.

조정된 평균은 이제 실제 인구 전체의 $R$값에 대한 추정치를 제공하며, 위에서 설명한 대로 개입 조치의 영향을 측정할 수 있다. 예를 들어, 레디 레커너에서 가구 외 사회적 접촉의 80%를 차단했을 때 2020년 4월 봉쇄 기간 동안 $R$이 약 0.7이라는 추정치를 도출했는데, 이는 직접 추정치와 놀랍도록 유사하며 이 접근법이 유용하다는 증거를 제공한다.

이 설명은 레디 레커너의 아이디어의 핵심을 제공하지만, 단순화된 것이다. 실제 수학은 더 복잡하며, 당연히 이용 가능한 데이터로부터 중요한 매개변수들의 좋은 추정치를 갖는 것이 매우 중요하다. 예를 들어, 백신, 부스터, 자연 면역의 효과에 대한 좋은 추정치가 필요하고, 또한 이 면역이 약화될 수 있다는 사실도 고려해야 한다.

최신 보고서를 위해, Bristol 팀은 인구 내 면역의 양에 대한 정보를 얻기 위해 Office of National Statistics의 인구 내 항체 존재에 관한 [연구](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/articles/coronaviruscovid19latestinsights/antibodies)의 데이터를 사용했다. 그들은 또한 여러 다른 가정들을 했으며, 이에 대해서는 그들의 [보고서](https://www.gov.uk/government/publications/university-of-bristol-trade-off-between-population-immunity-and-return-to-work-for-covid-19-control-autumn-and-winter-2021-scenarios-12-october-202)에서 읽을 수 있다.

### 감염자 수와 사망자 수

$R$값이 유행병이 증가할지 감소할지를 설명하는 데 유용하지만, 실제로 필요한 것은 감염자 수와 사망자 수다. 이것들은 $R$을 사용하여 근사할 수 있다.

위에서 설명한 것처럼, 유행병의 초기에 아무도 면역이 없고 사람들이 정상적으로 행동할 때, $R$값은 [기본 재생산지수](https://plus.maths.org/content/maths-minute-r0-and-herd-immunity)로 주어진다. 그러나 사람들이 면역을 갖게 되면 질병에 걸릴 수 있는 사람이 줄어들기 때문에 $R$값은 떨어진다. $R$이 1이 되면 감염자 수가 정점에 도달하고 유행병이 전환점을 맞는다. 그 이후 $R$은 0을 향해 계속 감소한다. 총 감염자 수를 추정하려면 이 모든 감염자들을 합산하면 된다.

> 이것은 전염병 동역학의 기본 원리다. $R_{eff} = R_{0}(1 - p)$로 쓸 수 있는데, 여기서 $p$는 면역을 가진 인구의 비율이다. 유행이 진행됨에 따라 $p$가 증가하고 $R_{eff}$가 감소한다. $R_{eff} = 1$일 때가 정점이며, 이때 $p = 1 - 1/R_{0}$가 된다. 이것이 '집단면역 임계값(herd immunity threshold)'이다. 예를 들어 $R_{0} = 7$이면 집단면역 임계값은 약 85.7%다. 하지만 실제로는 접촉 패턴의 이질성, 공간적 구조, 행동 변화 등으로 인해 이보다 복잡하다.

### 감염되지 않은 사람의 수

유행병 동안 감염을 피한 사람들의 수는 보통 $S_{\infty}$로 표기된다. 이것은 다음 방정식으로 계산할 수 있다.
$$
S_{\infty} = \exp\left(-R_{0}\left(1-S_{\infty}\right)\right).
$$

> 이 방정식은 고전적인 SIR 모델의 '최종 크기 방정식(final size equation)'이다. $S_{\infty}$는 유행이 끝났을 때 여전히 감수성이 있는(즉, 감염되지 않은) 개인의 비율이다. 이 방정식은 초월방정식(transcendental equation)이므로 명시적 해가 없고 수치적으로 풀어야 한다. 수학적으로 이것은 유행 초기의 감수성 개체 비율 $S_{0}$와 최종 비율 $S_{\infty}$ 사이의 관계를 나타내며, 전체 유행 과정에서 제거된(회복 또는 사망) 개체의 비율은 $S_{0} - S_{\infty}$가 된다. 이 방정식의 도출은 SIR 모델의 미분방정식을 적분하여 얻을 수 있다.

불행히도 총 감염자 수에 대한 공식은 없지만, 그 **반대**, 즉 유행병 동안 감염되지 **않은** 사람의 수를 박스의 방정식을 사용하여 수치적으로 계산할 수 있다.

역시 [JUNIPER](https://maths.org/juniper/)의 [Lorenzo Pellis](https://www.research.manchester.ac.uk/portal/lorenzo.pellis.html)와의 밤늦은 수학 작업을 거쳐, Bristol 팀은 레디 레커너 프레임워크에서 사용할 수 있도록 사회적 접촉 설문조사 데이터를 사용하는 동등한 계산 방법을 고안했다. 그런 다음 감염자 수와 사망률에 대한 정보를 함께 사용하여 사망자 수를 추정했다.

이를 통해 Bristol 팀은 가을과 겨울에 대한 다음과 같은 추정치를 얻었다. 모든 사람이 팬데믹 이전의 행동 패턴으로 돌아가고 어떠한 제한도 가해지지 않는다면, 이 기간 동안 총 감염자 수는 570만 명에서 630만 명 사이이고, 사망자 수는 7,500명에서 9,100명 사이로 추정된다.

부스터 프로그램을 포함하면 추정 감염자 수는 490만 명에서 540만 명 사이로 줄어들고, 사망자 수는 5,200명에서 6,300명 사이로 줄어든다. 그리고 12세에서 15세까지의 백신 접종을 추가하면 추정 감염자 수는 340만 명에서 380만 명 사이로 줄어들고, 사망자 수는 3,200명에서 3,800명 사이로 줄어든다.

마지막으로, 팀은 보호 면역을 20% 감소시키는 우려 변이가 엄청난 영향을 미칠 수 있다는 것을 발견했다. 이는 감염자 수를 2,100만 명에서 2,200만 명 사이로, 사망자 수를 91,000명에서 106,000명 사이로 끌어올릴 것이다.

> 이 수치들은 모든 개입 조치가 없을 때의 '최악의 시나리오'를 보여준다. 우려 변이의 경우 사망자가 10만 명을 넘는 것은 영국 인구 약 6,700만 명의 0.15%에 해당하며, 이는 의료 시스템에 감당할 수 없는 부담이 될 것이다. 이러한 추정의 불확실성은 여러 요인에서 나온다: 면역 지속 기간, 변이의 면역 회피 정도, 백신 접종률, 그리고 무엇보다도 사람들의 행동 변화. 이것이 바로 여러 시나리오를 제시하는 이유다.

![A schematic of the Warwick model](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/ready_reckoner/cases_estimates.jpg)

그림 2: 활동 접촉 비율의 함수로서 가을과 겨울 동안 총 감염자 수의 추정치. 색깔들은 그림 1과 같은 의미를 갖는다. 왼쪽 패널은 COVID 방역 조치와 접촉 추적이 전혀 없다고 가정하고, 오른쪽 패널은 감염 예방에 25% 효과적인 COVID 방역 조치와 접촉 추적을 가정한다. 그림은 Bristol 팀의 [보고서](https://www.gov.uk/government/publications/university-of-bristol-trade-off-between-population-immunity-and-return-to-work-for-covid-19-control-autumn-and-winter-2021-scenarios-12-october-202)에서 가져왔으며, 허가를 받아 사용했다.

계산된 추정치들이 이번 가을과 겨울 동안의 총 감염자 수와 사망자 수라는 것을 기억하는 것이 중요하다. 레디 레커너 접근법은 이러한 감염자들의 대부분이 집중된 기간에 발생하는지, 아니면 몇 달에 걸쳐 고르게 분포하는지를 말할 수 없다. 이것은 중요한데, 전자의 상황은 전체 감염자 수가 상대적으로 낮게 유지되더라도 의료 시스템에 상당한 압력을 가할 수 있기 때문이다. 따라서 이러한 총 감염자 수 추정치를 University of Warwick의 유행병 궤적 시나리오 모델링 같은 다른 예측들과 함께 고려하는 것이 중요하다. 이에 대해서는 [여기](https://plus.maths.org/content/winter-coming-where-are-we-going)에서 읽을 수 있다.

> 이것은 '시간 해상도(temporal resolution)'의 문제다. 레디 레커너는 적분된(integrated) 값, 즉 전체 기간의 누적 감염자를 제공한다. 하지만 공중보건 관점에서는 '피크 높이(peak height)'와 '피크 시점(peak timing)'이 중요하다. 같은 총 감염자 수라도 짧은 기간에 집중되면 의료 자원 부족으로 치명률이 높아질 수 있다. 이를 '곡선 펴기(flattening the curve)'라고 하며, 이는 팬데믹 초기의 핵심 전략이었다. 시간에 따른 동역학을 보려면 미분방정식 기반 시뮬레이션이나 에이전트 기반 모델(agent-based model)이 필요하다.

팬데믹을 이해하기 위해 설계된 모든 수학적 방법들과 마찬가지로, 레디 레커너는 무슨 일이 일어날지에 대한 확실성을 주지는 않는다. 하지만 그것은 우리가 가진 사람들의 접촉에 대한 정보를 최대한 활용하여 앞으로 무엇이 기다리고 있을지에 대한 감각을 제공하는 독창적인 방법이다.

### 이 글에 대하여

![Ellen Brooks Pollock and Leon Danon.](https://plus.maths.org/content/sites/plus.maths.org/files/podcast/2021/Ellen_Leon/ellen_leon.jpg)

Ellen Brooks Pollock과 Leon Danon.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)는 *Plus*의 편집자다. 그녀는 이 글을 작성하는 데 도움을 준 [Ellen Brooks-Pollock](https://www.bristol.ac.uk/people/person/Ellen-Brooks%20Pollock-9ffd9ff9-0949-49c4-97f7-bae51aa23d51/), [Leon Danon](https://research-information.bris.ac.uk/en/persons/leon-danon), [Ciara Dangerfield](https://maths.org/juniper/people)에게 감사한다.

*이 글은 JUNIPER, 즉 Joint UNIversity Pandemic and Epidemic Response 모델링 컨소시엄과의 협력의 일부다. JUNIPER는 Cambridge, Warwick, Bristol, Exeter, Oxford, Manchester, Lancaster 대학의 학자들로 구성되어 있으며, 이들은 다양한 수학적, 통계적 기법을 사용하여 COVID-19 통제에 관한 긴급한 질문들을 다루고 있다. JUNIPER와 함께 제작된 더 많은 콘텐츠를 여기에서 볼 수 있다.*

![Juniper logo](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)