---
title: COVID-19의 불평등
date: 2022-06-13
---

> [!NOTE]
> https://plus.maths.org/content/inequalities-covid
>
> COVID-19 팬데믹은 우리 사이의 차이를 증폭시켰다. 이러한 불평등을 이해하는 것은 현재와 미래의 팬데믹에 대응하는 데 필수적이다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/unequal_frontpage.jpg?itok=KnC8J9Bu)

COVID-19 팬데믹이 시작되던 초기, 우리 대부분은 모두가 함께 힘을 합치고 있다고 느꼈다. 우리는 자신을 보호하는 만큼이나 타인을 보호하기 위해 집에 머물렀고, 취약한 친구와 이웃을 최선을 다해 도왔으며, 숨죽이며 함께 기다렸다.

하지만 이 질병이 우리 사이의 차이를 증폭시킨다는 것이 곧 명확해졌다. 덜 유리한 배경을 가진 사람들이 더 많은 감염을 기록했고 더 많이 사망했으며, 인종 집단 간에도 차이가 나타났다.

### 불평등한 감염

데이터는 이를 명백히 보여준다. 아래 그래프는 시간에 따라 보고된 양성 검사 결과를 보여주는데, [복합 박탈 지수(index of multiple deprivation)](https://en.wikipedia.org/wiki/Multiple_deprivation_index)를 사용하여 열 개 집단으로 나눈 것이다. 이는 소득부터 주택 및 서비스 접근성까지 여러 요인을 고려하여 사람이 얼마나 불리한 처지에 있는지를 측정하는 방법이다. 이 지수는 [주택·지역사회·지방정부부(Ministry of Housing, Communities and Local Government)](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)가 정의한다.

> 복합 박탈 지수는 단순히 소득만을 보는 것이 아니라 다차원적 불평등을 포착하는 도구다. 영국에서는 소득, 고용, 건강, 교육, 범죄, 주거 환경, 생활 환경 등 7개 영역의 지표를 종합하여 각 지역의 상대적 박탈 수준을 계산한다. 예를 들어 소득이 낮으면서 동시에 의료 서비스 접근이 어렵고 주거 환경이 열악한 지역은 높은 박탈 지수를 받는다. 이런 종합적 접근은 빈곤이 단일 차원이 아니라 여러 불리한 조건이 중첩되어 나타나는 현상임을 인정하는 것이다. 팬데믹 상황에서 이러한 다차원적 불평등은 질병 확산과 사망률에 복합적으로 영향을 미친다.

진한 파란색 선은 인구의 가장 박탈된 10분위에 해당하고, 연한 파란색 선은 가장 유리한 10분위에, 그리고 다른 색들은 그 사이의 계층을 나타낸다. 그래프 오른쪽의 범례를 참조하라. 데이터에 대한 자세한 정보는 캡션을 참고하라.

![시간에 따른 양성 2단계 검사](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2022/socio-economic/First_IMD_figure.png)

이 그래프는 복합 박탈 지수(IMD)를 사용하여 열 개 집단으로 나눈 인구 10만 명당 [2단계 검사(pillar 2 tests)](https://www.gov.uk/government/publications/nhs-test-and-trace-statistics-england-methodology/nhs-test-and-trace-statistics-england-methodology) 결과를 보여준다(2단계 검사는 병원이나 의료진이 아닌 지역사회의 사람들이 자발적으로 받은 검사다). 양성 검사는 검사 양성자의 집 주소가 속한 [하위층 슈퍼 아웃풋 지역(Lower level super output area)](https://www.datadictionary.nhs.uk/nhs_business_definitions/lower_layer_super_output_area.html#:~:text=Lower%20Layer%20Super%20Output%20Areas,statistics%20in%20England%20and%20Wales.)(작은 지리적 영역)을 기반으로 IMD 집단에 할당되었다. 데이터는 [로그 척도(log scale)](https://plus.maths.org/content/logistic-growth-mathematics-covid-variants)로 표시된다. 이 그래프는 Newton Gateway 행사에서 Alison Hale의 [발표](https://gateway.newton.ac.uk/presentation/2022-04-05/35305)에 등장했으며, 허가를 받아 사용했다. 기초 데이터는 영국 보건안보청(UK Health Security Agency)에서 나왔지만 공개되지 않았다.

> 로그 척도는 지수적 성장을 직선으로 변환하여 시각화하는 방법이다. 감염병의 초기 확산은 지수함수적으로 증가하는데, 일반 선형 척도로 그리면 초기의 작은 변화가 보이지 않고 후기의 급증만 두드러진다. 로그 척도에서는 $y = e^{kt}$와 같은 지수 성장이 $\ln y = kt$로 직선이 되므로, 성장률의 변화를 쉽게 파악할 수 있다. 이 그래프에서 로그 척도를 사용한 것은 팬데믹 전 기간에 걸쳐 각 집단의 상대적 감염 추세를 비교하기 위함이다. 만약 선형 척도를 사용했다면 초기의 중요한 불평등 패턴이 묻혀버렸을 것이다.

주목할 만한 점은 2020년 4월부터 2021년 7월까지 거의 모든 시점에서 곡선의 순서가 박탈 계층의 순서와 거의 정확히 일치한다는 것이다. 가장 박탈된 10분위(진한 파란색)가 가장 많은 양성 검사 결과를 보고했고, 그 다음이 두 번째로 박탈된 집단(주황색), 세 번째로 박탈된 집단(녹색) 순이었으며, 가장 덜 박탈된 10분위를 나타내는 맨 아래 곡선(연한 파란색)까지 이어진다.

### 불평등한 사망

사망자의 경우에도 차이는 극명하다. 아래 그래프는 잉글랜드에서 2020년 초부터 6월까지 위에서 설명한 열 개의 박탈 집단 각각에 대해 시간에 따라 총 사망자 수가 어떻게 증가했는지를 보여준다. 진한 분홍색은 가장 박탈된 10분위를, 진한 녹색은 가장 덜 박탈된 10분위를 나타낸다.

가장 진한 분홍색 두 선은 전체 기간 동안 확고하게 상단에 머물러 있고, 가장 진한 녹색 두 선은 하단 근처에 머물러 있다. 가장 박탈된 집단의 사람들 사이에서 가장 덜 박탈된 집단에 비해 더 많은 사망이 있었다. [기초 데이터](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/deathsduetocovid19bylocalareaanddeprivation)는 국가통계청(Office for National Statistics, ONS)에서 나왔다. 그림에 대한 자세한 정보는 캡션을 참조하라.

![잉글랜드 인구 10만 명당 누적 사망자 수](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2022/socio-economic/image1.png)

이 그래프는 잉글랜드 인구 10만 명당 누적 사망자 수를 나타내며, 인구는 거주 지역에 할당된 복합 박탈 지수(IMD)에 따라 열 개의 동등한 집단으로 나뉘었다. 진한 분홍색은 가장 박탈된 10분위에, 진한 녹색은 가장 덜 박탈된 10분위에 해당한다. 이 그림은 Newton Gateway 행사에서 Clare Bambra의 [발표](https://gateway.newton.ac.uk/presentation/2022-04-05/35316)에 등장했으며, 허가를 받아 사용했다. 그래프와 [기초 ONS 데이터](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/deathsduetocovid19bylocalareaanddeprivation)에 대해 더 알아보려면 Clare Bambra와 동료들의 [이 논문](https://www.medrxiv.org/content/10.1101/2021.10.23.21265415v1)을 참조하라.

인종 집단 간 차이에 관해서는, [ONS가 2021년 5월에 발표한 보고서](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/articles/updatingethniccontrastsindeathsinvolvingthecoronaviruscovid19englandandwales/24january2020to31march2021)가 충격적인 내용을 담고 있다. 2020년 1월부터 2021년 3월 사이에 COVID-19와 관련된 사망률은 흑인 아프리카계 집단에서 가장 높았다. 남성의 경우 백인 영국계 집단보다 무려 3.7배 높았고, 여성의 경우 2.6배 높았다.

그 다음은 방글라데시계 인종 집단(남성 3배, 여성 1.9배 높음), 흑인 카리브계 인종 집단(남성 2.7배, 여성 1.8배 높음), 파키스탄계 인종 집단(남성 2.2배, 여성 2배 높음) 순이었다.

> 이러한 인종 간 사망률 격차는 단순히 유전적 차이로 설명할 수 없다. 실제로는 인종과 사회경제적 지위, 직업, 주거 환경이 복잡하게 얽혀 있다. 예를 들어 영국에서 소수 인종 집단은 필수 노동자(essential workers) 비율이 높고, 다세대 가구에 거주하는 경우가 많으며, 의료 서비스 접근성이 낮은 경향이 있다. 또한 만성 질환 유병률도 높다. 따라서 이 수치들은 생물학적 취약성보다는 구조적 불평등의 지표로 봐야 한다. 흑인 아프리카계의 3.7배라는 수치는 같은 바이러스가 사회적 맥락에 따라 얼마나 다르게 작용하는지를 극명하게 보여준다.

### 불평등한 백신 접종

마지막으로, 백신을 맞으러 간 사람의 수에서도 뚜렷한 차이가 있다. 예를 들어, [잉글랜드의 ONS 데이터](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthinequalities/datasets/coronavirusandvaccinationratesinpeopleaged18yearsandoverbysociodemographiccharacteristicandregionengland)에 따르면 2022년 3월까지 인구의 가장 박탈된 5분위에 속하는 18세 이상 남성 중 약 57%만이 백신 3회 접종을 받았다. 이는 가장 덜 박탈된 5분위의 81.5%와 비교된다.

COVID-19 팬데믹에 대한 우리의 모든 보도는 [여기](https://plus.maths.org/content/tags/covid-19)에서 볼 수 있다.

인종적 측면에서, [잉글랜드의 ONS 데이터](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/articles/coronaviruscovid19latestinsights/vaccines)는 3회 백신 접종을 받은 사람의 비율이 백인 영국계에서 가장 높았고(76%), 흑인 카리브계(38%), 흑인 아프리카계(45%), 파키스탄계(45%) 인종 집단에서 가장 낮았다는 것을 보여준다.

### 원인은 무엇인가?

이 질문에 대해 모든 측면을 다루는 쉬운 답은 없다. 실제로 불평등을 유발하는 사회경제적 요인들은 최근 [Newton Gateway to Mathematics](https://gateway.newton.ac.uk/event/tgm119)가 [JUNIPER 모델링 컨소시엄](https://maths.org/juniper) 및 [RAMP 연속성 네트워크](https://gateway.newton.ac.uk/node/10377)와 협력하여 조직한 가상 연구 회의의 주제였다. 이 회의는 질병 모델러부터 보건사회복지부와 웨일스 정부 대표에 이르기까지 다양한 전문가들로 구성되었다. 위의 그래프들은 회의에서 발표된 프레젠테이션에 나온 것이다.

이 문제에 대해 생각해보면 비교적 명백해 보이는 원인들이 있다. "팬데믹 초기에 사무직 노동자들은 재택근무를 했기 때문에 평소보다 접촉이 적었습니다"라고 Lancaster 대학의 역학자이자 JUNIPER 회원으로 Newton Gateway 회의를 조직한 [Alison Hale](https://www.lancaster.ac.uk/health-and-medicine/about-us/people/alison-hale)은 말한다. "하지만 우리에게는 무급휴직을 하지 않은 저임금 직종의 많은 사람들이 있었습니다. 요양원 직원, 간호사, 병원의 관리 보조원, 슈퍼마켓 직원, 일을 계속 유지하던 사람들, 여전히 많은 접촉이 있던 사람들 말입니다. 그리고 COVID-19 같은 감염병은 물론 접촉을 통해 퍼지죠."

> 접촉 패턴의 불평등은 감염병 역학에서 핵심적이다. 수리 역학 모델에서 기본재생산수(basic reproduction number) $R_{0}$는 평균 접촉률과 전파 확률의 곱에 비례한다. 즉, $R_{0} \propto \beta c$인데, 여기서 $\beta$는 접촉당 전파 확률이고 $c$는 평균 접촉 수다. 재택근무가 가능한 집단에서 $c$가 급격히 감소하면 그 집단의 유효 재생산수가 1 이하로 떨어져 전파가 억제된다. 반면 필수 노동자 집단에서는 $c$가 높게 유지되어 계속 전파가 일어난다. 이는 같은 바이러스가 사회 계층에 따라 전혀 다른 역학적 궤적을 보이는 이유를 설명한다.

데이터를 더 깊이 들여다보면 직업이 결정적인 것으로 보인다는 것을 확인할 수 있다. 다음 차트는 남성과 여성 모두에 대해 직업별로 분류된 잉글랜드와 웨일스에서 등록된 사망을 측정한다. 가장 오른쪽으로 뻗은 막대들, 즉 사망률이 가장 높은 직업 유형에 해당하는 것들은 낮은 임금을 받을 가능성이 있는 직업, 예를 들어 돌봄 및 여가 부문의 직업들이다.

![직업 유형별 사망](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2022/socio-economic/jobs_chart.jpg)

이 그래프는 2020년 3월 9일부터 2020년 12월 28일까지 남성과 여성에 대한 직업 유형별로 분류된 잉글랜드와 웨일스에서 COVID-19와 관련된 인구 10만 명당 사망 수를 나타낸다. 이 수치는 2021년 2월 과학자문그룹(Scientific Advisory Group for Emergencies, SAGE)의 소그룹이 발표한 [보고서](https://www.gov.uk/government/publications/emg-covid-19-risk-by-occupation-and-workplace-11-february-2021)에서 가져왔다. 그래프와 데이터에 대한 자세한 내용은 [보고서](https://www.gov.uk/government/publications/emg-covid-19-risk-by-occupation-and-workplace-11-february-2021)를 참조하라.

생활 조건 역시 중요한 역할을 할 가능성이 크다. 더 불리한 집단에서 더 흔한 과밀 주택은 질병에 걸린 사람이 다른 사람에게 전염시킬 가능성을 높인다. 붐비는 가구, 심지어 붐비는 이웃에 대한 위험은 구성원 중 한 명 이상이 더 높은 위험에 처하게 하는 직업에서 일하는 경우 증폭된다.

이 모든 것에 더하여, [COPD(만성 폐쇄성 폐질환)](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/)로 알려진 호흡 곤란을 일으키는 폐 질환 그룹과 같은 만성 건강 상태가 더 불리한 집단에서 더 만연해 있다는 사실이 있다. 예를 들어 2013년에 발표된 [이 연구](https://journals.sagepub.com/doi/10.1177/1355819613493772)를 참조하라. 이러한 기저 질환은 사람이 COVID-19로 매우 아프거나 심지어 사망할 가능성을 높인다.

> COPD는 여기서 구조적 불평등의 생물학적 각인(biological embodiment)을 보여주는 예다. COPD는 주로 장기간의 흡연, 직업적 먼지 노출, 대기 오염과 관련이 있는데, 이 모든 것이 사회경제적 지위와 강하게 연관되어 있다. 저소득층은 흡연율이 높고, 유해한 작업 환경에 노출될 가능성이 크며, 대기 오염이 심한 지역에 거주하는 경향이 있다. 따라서 COPD 유병률의 차이는 수십 년에 걸친 누적된 불평등의 결과다. COVID-19 팬데믹은 이러한 기존의 건강 불평등을 드러내고 악화시킨 것이다. 수학적으로 표현하면, 기저 질환이 있는 경우 중증 진행률과 사망률이 곱셈적으로(multiplicatively) 증가하므로, 불평등의 효과가 기하급수적으로 커진다.

함께 고려하면, 이러한 요인들—직업, 생활 조건, 기저 건강 상태—은 위의 차트 중 일부에 대한 그럴듯한 설명을 제공한다. 다른 불평등은 설명하기 더 어렵다. 인종 집단 간 차이와 백신 접종률의 차이가 그중 하나다. 이들은 아마도 박탈부터 서비스와 의료에 접근하려 할 때 장벽을 만들 수 있는 문화적 차이에 이르기까지 복잡한 요인의 조합 때문일 것이다(예를 들어, 과학자문그룹이 발표한 인종 집단 간 사망률 차이에 관한 [이 문서](https://www.gov.uk/government/publications/covid-19-ethnicity-subgroup-interpreting-differential-health-outcomes-among-minority-ethnic-groups-in-wave-1-and-2-24-march-2021/covid-19-ethnicity-subgroup-interpreting-differential-health-outcomes-among-minority-ethnic-groups-in-wave-1-and-2-24-march-2021)를 참조하라).

### 신데믹 팬데믹

여기서 우리가 보게 되는 것은 *신데믹(syndemic)*의 그림이다. 이 용어는 1990년대에 인류학자이자 임상의인 [Merrill Singer](https://anthropology.uconn.edu/person/merrill-singer/)가 만들었다. "Singer는 미국 도시에서 도시 폭력, HIV, 약물 사용과 관련된 상호작용하는 위험 요인에 대해 이야기했습니다"라고 사회과학자 [Clare Bambra](https://sphr.nihr.ac.uk/staff/prof-clare-bambra/)는 [Newton Gateway 행사에서의 매혹적인 발표](https://gateway.newton.ac.uk/presentation/2022-04-05/35316)에서 말했다. "당시 그것들은 매우 분리된 이슈로 연구되고 있었고, Singer는 그것들이 상호작용하는 유행병으로 바라봐야 한다고 주장했습니다."

*신데믹(syndemic)*이라는 단어 뒤에 있는 아이디어의 일반적인 의미는, 질병이 인구 집단에 어떻게 영향을 미칠 수 있는지를 밝히기 위해서는 실제 질병보다 훨씬 더 많은 것을 이해해야 한다는 것이다. "기존 건강 상태, 사회경제적 요인, 그리고 관련이 있다면 환경 요인이 모두 감염병의 데이터와 추세를 분석하고 평가할 때 고려되어야 합니다"라고 Hale은 말한다.

> 신데믹 개념은 단순한 동시 발생(co-occurrence)을 넘어선다. 핵심은 '시너지적 상호작용(synergistic interaction)'이다. 예를 들어 A라는 질병과 B라는 사회적 조건이 있을 때, 신데믹에서는 그 영향이 $A + B$가 아니라 $A \times B$ 또는 그 이상으로 나타난다. COVID-19의 경우, 바이러스 자체의 병원성, 사회경제적 박탈로 인한 높은 노출, 만성 질환으로 인한 취약성, 의료 접근성 부족이 서로를 증폭시켜 특정 집단에서 불균형적으로 높은 사망률을 초래했다. 이는 감염병 대응이 순수하게 생물의학적 개입만으로는 불충분하며, 사회적 결정 요인(social determinants)을 동시에 다뤄야 함을 의미한다. 신데믹 관점은 팬데믹을 사회적 불의(social injustice)를 드러내는 렌즈로 보게 한다.

![신데믹의 개략도](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2022/socio-economic/syndemic.jpg)

신데믹의 개략도. 이 그림은 Clare Bambra가 공동 저자로 참여한 [The COVID-19 pandemic and health inequalities](https://jech.bmj.com/content/74/11/964)에서 가져왔다. 허가를 받아 사용했다.

이러한 더 큰 그림을 염두에 두면, 놀라운 추세조차도 덜 의아해질 수 있다. 한 예가 이 기사의 첫 번째 차트에서 나온다. 이 차트는 시간에 따라 기록된 양성 검사를 박탈 수준별로 분리하여 보여준다. 차트는 2021년 여름까지만 다뤘다. 그러나 2022년까지 계속 따라가면 놀라운 일이 일어난다. 곡선들이 자리를 바꾸는 것이다.

![시간에 따른 양성 2단계 검사](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2022/socio-economic/Second_IMD_figure.png)

이 그래프는 복합 박탈 지수(IMD)를 사용하여 열 개 집단으로 나눈 인구 10만 명당 [2단계 검사(pillar 2 tests)](https://www.gov.uk/government/publications/nhs-test-and-trace-statistics-england-methodology/nhs-test-and-trace-statistics-england-methodology) 결과를 보여준다(이 그래프는 기사 시작 부분에 나왔다 - 이 그림에 대한 전체 세부사항은 [여기](https://plus.maths.org/content/inequalities-covid#figure1)를 참조하라).

가장 덜 박탈된 집단을 나타내는 곡선이 2021년 여름 이후 상단으로 이동하고 가장 박탈된 집단을 나타내는 곡선이 하단으로 이동한다. 사실, 역전이 완전한 것처럼 보이며, 다른 모든 색깔의 선들도 이제 거의 역순으로 나타난다.

만약 이 데이터를 액면 그대로 받아들인다면, 가장 박탈된 집단의 사람들이 2021년 여름 이후 실제로 가장 덜 박탈된 집단보다 COVID를 덜 걸렸다고 추론하게 된다. 이에 대한 이유는 가장 박탈된 집단이 일찍 질병의 주된 타격을 받았고, 2021년 여름까지 그 이전 감염을 통해 충분한 자연 면역을 획득하여 더 적은 사례를 기록했을 수 있다는 것이다.

그러나 만약 사람들의 더 넓은 상황을 고려한다면, 다른 이유가 제시된다. 2021년 7월에 인구의 대부분이 다시 직장에 가기 시작했을 때, 출근하지 않으면 급여를 받지 못하는 직업을 가진 사람들은 질병에 걸렸다고 의심하더라도 검사를 하지 않을 강한 유인이 있었다. 그러나 편안하게 집에 머물 수 있는 사람들은 계속 성실할 수 있었다. 자가격리하는 사람들에 대한 지원이 거의 없을 때, 규칙 준수는 사치품이 될 수 있다.

> 이 역전 현상은 데이터 해석의 미묘함을 보여주는 탁월한 사례다. 측정된 감염률과 실제 감염률의 차이는 검사 행동(testing behavior)에 달려 있다. 만약 $p$가 검사를 받을 확률이고 $\lambda$가 실제 감염률이라면, 측정된 감염률은 대략 $p \cdot \lambda$에 비례한다. 2021년 여름 이전에는 모든 집단에서 $p$가 비슷하게 높았으므로 측정된 차이가 실제 차이를 반영했다. 그러나 자가격리 지원이 철회된 후, 저소득층에서 $p$가 급감했다($p_{\text{deprived}} \ll p_{\text{affluent}}$). 따라서 측정된 감염률 역전은 실제 감염률의 역전이 아니라 검사 접근성과 경제적 유인의 불평등을 반영한다. 이는 팬데믹 감시 시스템에서 사회경제적 요인을 고려하지 않으면 왜곡된 결론에 이를 수 있음을 경고한다.

### 왜 우리가 관심을 가져야 하는가?

정확히 무엇이 역전 뒤에 있었는지 알아내려면 데이터를 훨씬 더 많이 풀어야 할 것이고, 아마도 우리는 결코 확신할 수 없을 것이다. 그러나 일반적으로, 가능한 한 신데믹 그림을 많이 이해하려고 노력하는 것이 중요하다. COVID-19 팬데믹은 아직 끝나지 않았으며, 이것이 감염병으로 인한 마지막 공중 보건 비상사태일 가능성은 낮다. 불평등에 대한 좋은 이해는 시행할 개입을 알리는 데 도움이 될 수 있다. "사회에서 가장 취약한 부분이 어디인지 파악할 수 있다면, 더 나은 지원을 제공할 수 있을 것입니다"라고 Hale은 말한다.

최근 Newton Gateway to Mathematics에서 열린 행사는 COVID-19와 관련된 불평등의 원인을 밝히려는 일반적인 노력의 일부다. 이것이 수학 연구소에서 열린 이유는 추측을 확고한 결론으로 바꾸는 데 영리한 통계적 탐정 작업이 필요하기 때문이다.

이론적으로는, COVID-19에 대한 정책 정보를 제공하는 데 매우 중요했던 수학적 모델에 사회경제적 요인을 포함시키는 것도 가능하다. 개념적으로, 이러한 모델은 인구를 집단으로 나눈다. 예를 들어 연령, 지리적 위치, 또는 백신 접종 상태별로 나누고, 그런 다음 서로 다른 집단의 사람들이 다양한 질병 단계를 어떻게 흘러가는지 시뮬레이션한다. 건강하지만 감염되기 쉬운 상태에서, 감염되어 회복하는 상태로, 또는 악화되어 병원에 가는 상태로, 잠재적으로 사망하는 상태로 말이다(모델에 대해 더 알아보려면 [여기](https://plus.maths.org/content/how-can-maths-fight-pandemic)를 참조하라). 각 집단은 질병에 걸릴 위험, 매우 아플 정도로 취약한 정도 등에 따라 한 질병 상태에서 다른 상태로 넘어가는 고유한 비율을 가진다.

> 이러한 구획 모델(compartmental models)은 전형적으로 SIR(Susceptible-Infected-Recovered) 또는 SEIR(Susceptible-Exposed-Infected-Recovered) 프레임워크를 사용한다. 수학적으로, 이는 연립 미분방정식 시스템으로 표현된다. 예를 들어 기본 SIR 모델은:
> 
> $\frac{dS}{dt} = -\beta SI, \quad \frac{dI}{dt} = \beta SI - \gamma I, \quad \frac{dR}{dt} = \gamma I$
> 
> 여기서 $S$, $I$, $R$은 각각 감염 가능자(susceptible), 감염자(infected), 회복자(recovered)의 비율이고, $\beta$는 전파율, $\gamma$는 회복률이다. 사회경제적 이질성을 포함하려면 이를 다층 시스템으로 확장해야 한다. 각 사회경제적 집단 $i$에 대해 $S_{i}$, $I_{i}$, $R_{i}$를 정의하고, 집단 간 접촉 패턴을 나타내는 행렬 $\beta_{ij}$를 도입한다. 이렇게 하면 모델이 훨씬 복잡해지지만, 특정 집단에 대한 표적 개입의 효과를 평가할 수 있게 된다. 예를 들어 필수 노동자에게 우선적으로 백신을 접종하는 것의 효과를 정량화할 수 있다.

만약 우리가 서로 다른 사회경제적 집단에 대한 비율을 이해한다면, 이것들도 모델에 포함될 수 있다. 일반적인 청사진은 이론적으로 모든 감염병에 대해 작동할 것이다(물론 특정 매개변수는 다를 것이다). "감염병 모델은 매우 일반적입니다"라고 Hale은 말한다. "일반적인 수학적 모델은 당신이 다루는 질병이 무엇인지 상관하지 않습니다."

모델에 사회경제적 요인을 포함하는 요점은 모델의 예측이 어떤 집단이 질병에 의해 가장 크게 타격을 받을 수 있는지를 알려줄 것이라는 점이다. 관련된 집단에 대한 좋은 지역 지식과 결합하면, 이는 그들을 보호하기 위한 표적 개입을 개발하는 데 도움이 될 것이다. 보호 장비를 제공하든, 격리가 필요할 때 지원하든, 그들이 신뢰할 수 있다고 느끼는 채널을 통해 정보를 제공하든 말이다.

우리는 여전히 COVID-19의 모든 사회적 불평등, 또는 실제로 과거에 발생한 다른 팬데믹의 불평등을 이해하는 초기 단계에 있다. 예를 들어 1918년 스페인 독감 팬데믹과 2009년 돼지독감 발생은 사회경제적 집단 간에 유사한 차이를 보였다.

명확한 것은 이 노력이 다양한 분야의 사람들의 전문 지식을 필요로 할 것이라는 점이다. "우리는 역학, 수학적 모델링, 사회과학을 함께 결합해야 합니다"라고 Hale은 말한다. "그것들이 정책에 효과적으로 정보를 제공하기 위해서는 잘 함께 작동해야 합니다." 이러한 불평등을 해결하기 위해 우리는 정말로 함께 힘을 합쳐야 한다.

> 이 마지막 문장은 기사의 시작으로 돌아간다. "우리 모두가 함께 힘을 합치고 있다"는 초기의 감정은 환상이었음이 드러났다. 팬데믹은 우리가 같은 배를 타고 있는 것이 아니라 같은 폭풍 속에 있을 뿐이며, 누구는 호화 유람선에, 누구는 구명보트에 타고 있음을 폭로했다. 진정한 연대는 이러한 불평등을 인정하고 측정하고 해결하려는 노력에서 나온다. 수학과 데이터 과학은 여기서 단순히 기술적 도구가 아니라 사회 정의를 위한 도구가 된다. 불평등을 정량화하고 그 원인을 규명하며 개입의 효과를 예측함으로써, 수학은 더 공평한 팬데믹 대응을 설계하는 기초를 제공한다. 이것이 바로 응용수학의 사회적 책임이다.

### 이 기사에 대하여

[Alison Hale](https://www.lancaster.ac.uk/health-and-medicine/about-us/people/alison-hale)은 Lancaster 대학의 역학자다. 그녀는 2022년 5월 *Plus*의 편집자인 [Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)와 인터뷰했다.

이 기사는 [Newton Gateway to Mathematics](https://gateway.newton.ac.uk/)가 [JUNIPER 모델링 컨소시엄](https://maths.org/juniper) 및 [RAMP 연속성 네트워크](https://gateway.newton.ac.uk/node/10377)와 협력하여 조직한 행사인 [영국의 코로나바이러스 사회경제적 결정요인(Socio-Economic Determinants of Coronavirus in the UK)](https://gateway.newton.ac.uk/event/tgm119)에서 발표된 프레젠테이션에서 영감을 받았다.

*이 기사는 JUNIPER(Joint UNIversity Pandemic and Epidemic Response 모델링 컨소시엄) 및 수리과학을 위한 아이작 뉴턴 연구소(Isaac Newton Institute for Mathematical Sciences, INI)와의 협력의 일환으로 제작되었습니다.*

*JUNIPER는 Cambridge, Warwick, Bristol, Exeter, Oxford, Manchester, Lancaster 대학의 학자들로 구성되어 있으며, COVID-19 통제에 관한 긴급한 질문을 다루기 위해 다양한 수학적 및 통계적 기법을 사용하고 있습니다. JUNIPER와 함께 제작된 더 많은 콘텐츠는 여기에서 볼 수 있습니다.*

*INI는 국제 연구 센터이자 Cambridge 대학 수학 캠퍼스의 우리 이웃입니다. 전 세계의 선도적인 수학 과학자들을 끌어들이며 모두에게 열려 있습니다. 더 알아보려면 www.newton.ac.uk를 방문하세요.*

![Juniper 로고](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)

![INI 로고](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)