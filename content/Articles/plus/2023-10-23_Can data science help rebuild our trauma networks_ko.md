---
title: 데이터 과학이 외상 네트워크 재구축을 도울 수 있을까?
date: 2023-10-23
---

> [!NOTE]
> https://plus.maths.org/content/can-data-science-help-rebuild-our-trauma-networks
>
> 수학이 병원 네트워크를 재편하는 데 도움을 줄 수 있을까?

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/front_icon_63.jpg?itok=FHRJVZrK)

구급차와 응급실 대기 시간이 최근 언론에서 많이 다뤄지고 있다. 많은 지역에서 의료 수용 능력(capacity) 증대가 필요해 보이는데, 바로 이 지점에서 수학이 도움을 줄 수 있다.

> 여기서 '수용 능력'이란 병원이 동시에 처리할 수 있는 환자 수, 병상 수, 의료진 규모 등을 포괄하는 개념이다. 단순히 물리적 공간만이 아니라, 적시에 적절한 치료를 제공할 수 있는 시스템 전체의 역량을 의미한다. 이는 대기열 이론(queueing theory)과 자원 배분 최적화 문제로 모델링할 수 있는데, 환자 도착률, 치료 시간 분포, 자원 제약 조건 등을 고려하여 시스템의 성능을 분석하고 개선하는 운영 연구(operations research)의 핵심 주제이다.

만약 우리가 케임브리지에서 심각한 부상을 당한다면, [East of England Trauma Network](https://www.eoetraumanetwork.nhs.uk/about-us)가 즉시 작동하여 구급차가 우리를 케임브리지의 Addenbrooke's Hospital로 이송할 것이다. 하지만 만약 우리가 이 지역의 다른 곳, Addenbrooke's에서 구급차로 45분 이상 떨어진 곳에 있다면, 네트워크를 구성하는 다른 12개 병원 중 한 곳으로 급히 이송될 것이다.

![A map showing the East of England Trauma Network](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2023/CMIH/EoETN_600.png)

East of England Trauma Network ([이미지](https://www.eoetraumanetwork.nhs.uk/about-us) 사용 허가를 받음)

Addenbrooke's는 이 지역에서 유일한 주요 외상 센터(Major Trauma Centre)로, 필요할 수 있는 모든 서비스를 제공할 수 있는 유일한 병원이다. 이는 다른 병원에서 초기 치료와 평가를 받은 환자들이 필요한 경우 추가 치료를 위해 Addenbrooke's로 이송되어야 할 수 있음을 의미한다. 그런데 East of England Trauma Network가 처음 설립된 이후 10년 동안 많은 것이 변했다. "Addenbrooke's의 주요 외상 환자를 위한 병상 수는 동일하지만, 환자 수는 증가했습니다"라고 Judge Business School의 경영과학 교수인 [Houyuan Jiang](https://www.cmih.maths.cam.ac.uk/about-us/people/houyuan-jiang)은 말한다. "인구 규모가 커지고 인구가 고령화되고 있어서 수요가 증가하고 있습니다. 이제 서비스 필요와 공급을 재평가할 때입니다."

> 외상 네트워크(trauma network)는 계층적 구조로 설계된다. 최상위 계층인 주요 외상 센터는 신경외과, 심장흉부외과 등 모든 전문 분야의 24시간 진료가 가능하고, 하위 계층인 외상 유닛(Trauma Unit)은 초기 안정화와 평가를 담당한다. 이러한 계층 구조는 희소한 고급 의료 자원을 효율적으로 배치하면서도 지리적 접근성을 확보하려는 전략이다. 그래프 이론의 관점에서 보면, 이는 중심 노드(hub)와 주변 노드(spoke)로 구성된 네트워크로, 최소 비용으로 최대 커버리지를 달성하는 시설 입지 문제(facility location problem)의 실제 사례라고 할 수 있다.

### 외상 네트워크 개선하기

Jiang은 Judge Business School의 운영 및 기술 경영 교수인 동료 Feryal Erhun과 함께 [Cambridge Mathematics of Information in Healthcare Hub](https://www.cmih.maths.cam.ac.uk/) (CMIH)의 멤버이다. CMIH는 케임브리지 대학교의 여러 학문 분야에서 온 19명의 공동 연구자들이 모든 유형의 의료 치료에서 데이터 문제를 해결하기 위해 수학을 사용하는 협업 프로젝트다. (CMIH에 대한 더 자세한 내용은 [여기](https://plus.maths.org/content/healthcare-AI)에서 읽을 수 있다.) Jiang은 [Newton Gateway to Mathematics](https://gateway.newton.ac.uk/)가 주관한 [2023년 6월 CMIH 행사](https://gateway.newton.ac.uk/event/tgm134)에서 지역 주민들의 미래 의료 수요를 충족시키기 위한 East of England Trauma Network 개발을 지원하는 자신의 연구에 대해 발표했다.

제안된 계획은 지역 내 다른 병원의 외상 유닛 중 하나를 업그레이드하여 두 번째 주요 외상 센터를 건설하는 것이다. 그런데 어디에 세워야 할까? 주요 외상 환자를 위한 병상은 몇 개가 있어야 할까? 그리고 이것이 네트워크 전체의 수요를 충족시킬 수 있을까? CMIH의 많은 연구자들처럼, Jiang은 [기계 학습](https://plus.maths.org/content/index.php/maths-minute-machine-learning-and-neural-networks) 접근법을 사용하여 이러한 질문들에 대한 가능한 답을 도출하기 위해 이용 가능한 방대한 양의 데이터를 활용했다. (기계 학습에 대한 쉬운 소개는 [여기](https://plus.maths.org/content/index.php/maths-minute-machine-learning-and-neural-networks)에서 읽을 수 있다.) Jiang과 그의 동료들은 지역 내 외상 병원 사용과 관련된 지난 10년간의 데이터뿐만 아니라, 미래 인구 변화와 그것이 수요에 미칠 영향에 대한 (통계청의) 예측도 사용했다. 그들은 또한 잠재적 환자들과 병원 사이의 거리를 판단하기 위해 Google Maps의 정보도 활용했다.

> 기계 학습 모델에서 데이터는 모델의 성능을 좌우하는 핵심 요소다. 여기서 사용된 데이터는 크게 세 가지 유형으로 분류된다: (1) 역사적 데이터 - 과거 10년간의 환자 이송 기록, 치료 시간, 병상 점유율 등 실제 운영 데이터, (2) 인구 통계 데이터 - 연령별, 지역별 인구 분포와 그 변화 예측치, (3) 지리 공간 데이터 - 각 지역에서 병원까지의 실제 이동 시간. 이러한 다차원 데이터를 통합하여 모델을 훈련시키면, 단순한 거리 계산보다 훨씬 정확한 수요 예측과 최적 입지 선정이 가능해진다. 이는 빅데이터 분석과 공간 최적화가 결합된 좋은 예시다.

Jiang과 그의 동료들이 이러한 광범위한 데이터 세트를 기반으로 기계 학습 모델을 구축한 후, 그들은 [반사실적 분석](https://towardsdatascience.com/counterfactual-explanations-in-model-interpretations-a73caec5b74b)(counterfactual analysis)을 사용하여 모델의 출력(예: 네트워크가 요구되는 시간 내에 수요를 충족할 수 있는지)에 영향을 미치기 위해 모델에 대한 입력(예: 주요 외상 센터의 위치 또는 주요 외상 병상 수)을 얼마나 변경해야 하는지 탐구했다. 기계 학습 모델은 종종 신비로운 블랙박스처럼 보일 수 있는데, 반사실적 분석은 연구자들이 자신의 모델이 무엇을 하고 있는지 설명하고 해석하는 데 도움을 줄 수 있다.

> 반사실적 분석은 "만약 X가 달랐다면 Y는 어떻게 되었을까?"라는 질문에 답하는 방법론이다. 예를 들어, "만약 두 번째 주요 외상 센터를 A 지역이 아닌 B 지역에 세웠다면, 45분 이내에 도달할 수 있는 인구 비율은 어떻게 달라졌을까?"와 같은 질문을 다룬다. 이는 인과 추론(causal inference)의 핵심 개념으로, 단순한 상관관계를 넘어 변수 간의 인과 관계를 이해하려는 시도다. 기계 학습의 예측 능력과 결합하면, 정책 결정자들에게 다양한 시나리오의 예상 결과를 정량적으로 제시할 수 있어, 근거 기반 의사결정(evidence-based decision making)을 가능하게 한다. 수학적으로는 민감도 분석(sensitivity analysis)과 최적화 이론이 결합된 형태로 볼 수 있다.

### CMIH 가족을 한데 모으기

의료 인프라와 계획 결정에 수학적 데이터 기반 접근법을 사용하는 Jiang의 연구는 [행사](https://gateway.newton.ac.uk/event/tgm134)에서 CMIH 구성원들이 수행한 광범위한 연구 중 한 가지 예에 불과했다. 신경외과 의사 [Chao Li](https://www.neurosurg.cam.ac.uk/research-groups/brain-tumour-imaging-lab/2988-2/dr-chao-li/)도 연사로 참여하여, 이미지 분석 알고리즘이 뇌종양의 진단과 치료에 어떻게 도움을 줄 수 있는지 설명했다. 그리고 생물의학 물리학자 [Sarah Bohndiek](https://www.cmih.maths.cam.ac.uk/about-us/people/sarah-bohndiek)은 다중 스펙트럼 영상(multispectral imaging)을 사용하는 유망한 의학적 응용에 대해 논의했는데, 이는 다양한 파장의 빛을 사용하여 물체를 촬영하는 기술이다. 한 가지 잠재적 응용은 식도의 전암 병변(precancerous region)을 발견하고 치료하여 암으로 발전하는 것을 막을 수 있는 새로운 의료 장비가 될 수 있다.

> 다중 스펙트럼 영상은 기존의 RGB(빨강, 초록, 파랑) 3채널 영상을 넘어 수십 개 이상의 서로 다른 파장 대역에서 이미지를 획득하는 기술이다. 각 파장은 조직의 서로 다른 화학적, 생물학적 특성에 반응하므로, 훨씬 풍부한 정보를 얻을 수 있다. 예를 들어, 정상 조직과 암 조직은 혈관 분포, 대사 활성, 세포 구조가 다르기 때문에 빛의 흡수와 반사 패턴이 다르게 나타난다. 이러한 고차원 데이터를 분석하려면 차원 축소(dimensionality reduction) 기법과 패턴 인식 알고리즘이 필요하며, 여기에 주성분 분석(PCA), 독립 성분 분석(ICA) 등의 수학적 도구가 활용된다. 이는 신호 처리와 통계적 학습의 융합 분야라고 할 수 있다.

다중 스펙트럼 영상의 아름다운 예

이 행사의 연사들의 폭넓은 분야와 그들의 연구 간의 연결은 CMIH가 지원하는 다학제 협업의 범위와 강점을 진정으로 보여주었다. "CMIH는 연구 주제 측면에서 매우 다양하며, 초기 경력 연구자들과 다양한 학문 분야 및 산업계에서 온 사람들로 구성되어 있습니다"라고 케임브리지 대학교의 응용수학 교수이자 CMIH의 공동 책임자인 [Carola-Bibiane Schönlieb](https://www.bloodcounts.org/people/carola-bibiane-sch%C3%B6nlieb)은 말한다. "우리 모두는 데이터 분석을 임상 연구에 도입하고자 하는 열정을 공통으로 가지고 있습니다."

CMIH의 임상 책임자이자 심혈관 의학 교수인 [James Rudd](https://www.cmih.maths.cam.ac.uk/about-us/people/james-rudd)는 CMIH가 생산한 연구가 이미 환자들이 받는 의료에 실질적인 영향을 미쳤다고 말했다: "[CMIH가 지금까지 생산한 거의 100편의 논문 중] 상당수가 정책에 영향을 미쳤습니다. 예를 들어, [CMIH가 개발한] 심혈관 질환 대기 명단 모델은 현재 NHS England에서 사용되고 있습니다."

> NHS(National Health Service)는 영국의 공공 의료 서비스 체계로, 세금으로 운영되어 무료 진료를 제공한다. 이러한 공공 시스템에서는 자원 배분의 효율성과 형평성이 특히 중요하며, 수학적 모델링이 정책 결정에 직접적으로 활용될 수 있다. 대기 명단 모델은 대기열 이론과 확률 과정을 기반으로, 환자 도착률, 치료 용량, 우선순위 규칙 등을 고려하여 최적의 자원 배분과 우선순위 설정을 제안한다. 이는 단순히 학술적 연구가 아니라 수백만 명의 실제 환자 치료에 영향을 미치는 공공 정책으로 전환된 사례로, 응용수학의 사회적 가치를 보여주는 좋은 예다.

그리고 이 행사가 CMIH의 현 단계를 마무리하는 것이지만, Schönlieb은 이 연구자 그룹이 중요한 역할을 할 수 있는 의료 분석의 주요 발전이 있다고 말한다. 그녀가 CMIH3이 될 수 있다고 제안한 미래 연구의 한 분야는 인구 건강 뒤의 수학 및 데이터 과학을 환경 건강 뒤의 것과 연결하는 것이다. 이 두 가지 사회적 과제를 통합된 방식으로 바라보는 것이 다음 개척지가 될 수 있다.

> 인구 건강(population health)과 환경 건강(environmental health)의 연결은 21세기 공중 보건의 핵심 과제다. 대기 오염, 기후 변화, 생태계 파괴는 직접적으로 심혈관 질환, 호흡기 질환, 감염병 발생에 영향을 미친다. 이를 수학적으로 모델링하려면 역학 모델(epidemiological model), 환경 시스템 모델, 기후 모델을 결합해야 한다. 예를 들어, 미세먼지 농도 변화가 천식 발작 빈도에 미치는 영향을 예측하는 모델은 대기 확산 방정식(편미분 방정식)과 질병 발생률 모델(통계적 모델)을 결합한 형태가 된다. 이는 복잡계(complex systems) 이론의 관점에서 접근해야 하는 대규모 다층 네트워크 문제로, 단일 학문으로는 해결할 수 없는 진정한 학제간 연구 영역이다.

### 이 글에 대하여

이 글은 2023년 6월 21일 Newton Gateway to Mathematics가 주최한 [CMIH Academic Engagement Event](https://gateway.newton.ac.uk/event/tgm134)에서 Houyuan Jiang의 강연을 기반으로 한다.

Jiang이 발표한 연구는 NHS England의 의료팀 전문 위탁 공중보건 컨설턴트인 Dr Esther Kwong이 주도했다. 케임브리지 대학교 Judge Business School과의 협업은 수용 능력 모델링과 예측을 위해 구축되었다. Esther Kwong, Lauren Rixen, Zidong Liu, Feryal Erhun, Houyuan Jiang은 이 연구에 대한 보고서인 *주요 외상에 대한 공중 보건 필요 평가*(Public Health Needs Assessment for Major Trauma)를 작성했으며, 이는 올해 말에 공개될 예정이다.

[Rachel Thomas](https://plus.maths.org/content/people/index.html#rachel)는 Plus의 편집자이다.

*이 글은 Cambridge Mathematics of Information in Healthcare Hub (CMIH), Newton Gateway to Mathematics, Isaac Newton Institute for Mathematical Sciences (INI)와의 협업의 일환으로 제작되었다.*

*INI는 케임브리지에 있는 국제 연구 센터로 전 세계의 저명한 수학자들을 끌어들인다. Newton Gateway는 INI의 영향력 확대 이니셔티브로, 수학 사용자들과 소통한다. 이 협업에서 나온 모든 콘텐츠는 여기에서 찾을 수 있다.*

![INI logo](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)

![Gateway logo](https://plus.maths.org/content/sites/plus.maths.org/files/Gateway%20logo/ngm%20logotype%20purple%20rgb%5B86%5D.png)