---
title: 머신러닝이란 무엇인가?
date: 2024-03-01
---

> [!NOTE]
> https://plus.maths.org/content/what-machine-learning-0
>
> 인공지능 분야에서 가장 중요한 발전 중 하나인 머신러닝에 대해 알아보세요!

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/chess_frontpage_0.jpg?itok=wGgmolct)

인공지능 분야에서 가장 중요한 발전 중 하나는 바로 **머신러닝(machine learning)**입니다. 머신러닝은 기계에게 복잡한 과제를 수행하는 방법을 전통적인 컴퓨터 프로그램처럼 명시적으로 가르치는 대신, 기계가 그 과제를 반복적으로 수행하는 경험을 통해 직접 학습하도록 합니다. 이 접근법에서 기계는 명확히 정의된 과제에 접근하는 방법에 있어 많은 유연성을 부여받고, 자신이 얼마나 성공적인지를 측정하는 방법과 어떻게 개선할 것인지에 대한 알고리즘을 제공받습니다.

> 전통적인 프로그래밍과 머신러닝의 근본적인 차이는 지식의 표현 방식에 있습니다. 전통적 프로그래밍에서는 프로그래머가 모든 규칙을 명시적으로 코딩합니다(예: "if 조건 then 행동"). 반면 머신러닝에서는 이러한 규칙이 데이터로부터 자동으로 추출됩니다. 이는 특히 규칙을 명시적으로 작성하기 어렵거나 불가능한 복잡한 패턴 인식 문제(이미지 인식, 자연어 처리 등)에서 혁명적입니다. 머신러닝은 본질적으로 "프로그램을 작성하는 프로그램"을 만드는 것이라고 볼 수 있습니다.

![chess board](https://plus.maths.org/content/sites/plus.maths.org/files/chess_frontpage.jpg)

게임을 플레이하는 맥락에서 생각하면 가장 이해하기 쉬울 것입니다. 컴퓨터에게 "이 상황에서는 이 수를 두어라"와 같은 명시적 지침을 제공하는 대신, 컴퓨터가 수많은 게임을 플레이하게 하고 패배로 끝난 수보다 승리로 끝난 수를 더 자주 선택하도록 유도하는 것입니다.

> 체스나 바둑 같은 게임은 머신러닝의 핵심 개념을 설명하는 이상적인 예시입니다. 체스에는 약 $10^{120}$개의 가능한 게임 상태가 있습니다(관측 가능한 우주의 원자 수 $10^{80}$보다 많습니다). 모든 가능한 상황에 대한 최선의 수를 수동으로 프로그래밍하는 것은 불가능합니다. 대신 머신러닝 시스템은 수백만 게임을 플레이하며 어떤 패턴이 승리로 이어지는지 스스로 발견합니다. 2016년 AlphaGo가 이세돌을 이긴 것은 바로 이러한 접근법의 위력을 보여준 역사적 사건이었습니다. AlphaGo는 수천 년간 축적된 바둑의 정석을 배운 것이 아니라, 자기 대국을 통해 인간이 발견하지 못한 새로운 전략까지 스스로 개발했습니다.

이 분야의 진보에는 공학과 컴퓨터 과학의 발전이 핵심적입니다. 그러나 머신러닝의 진정한 핵심 메커니즘은 수학으로 이루어집니다. 머신러닝 알고리즘이 특정 과제를 해결하도록 설계되었다고 말할 때, 그 의미는 알고리즘이 어떤 입력(예: 수학적으로 표현된 게임의 현재 상태)을 받아 원하는 출력(예: 게임에서의 최선의 다음 수)을 신뢰성 있게 제공하는 수학적 함수를 구성하도록 설계되었다는 뜻입니다.

> 머신러닝의 수학적 본질을 이해하는 것이 중요합니다. 머신러닝은 근본적으로 **함수 근사(function approximation)** 문제입니다. 우리에게는 알려지지 않은 "참" 함수 $f^{*}$가 있고(예: 체스 상태를 최적의 수로 매핑하는 함수), 머신러닝의 목표는 이 함수를 근사하는 함수 $\hat{f}$를 찾는 것입니다. 이 과정은 다음과 같이 형식화됩니다: 함수의 클래스 $\mathcal{F}$(예: 특정 구조의 신경망들)에서 손실 함수(loss function) $L(f)$를 최소화하는 함수 $\hat{f} = \arg\min_{f \in \mathcal{F}} L(f)$를 찾습니다. 이것이 바로 "학습(learning)"의 수학적 정의입니다. 고전적인 통계학에서 다루던 선형 회귀도 사실 이 관점에서 보면 매우 단순한 형태의 머신러닝입니다.

[여기](https://plus.maths.org/content/artificial-intelligence-and-deep-learning-your-questions-answered)를 클릭하면 전체 인공지능 FAQ를 볼 수 있습니다.

처음에 머신러닝 알고리즘은 이 작업을 신뢰성 있게 수행할 최선의 수학적 함수를 알지 못합니다. 대신 알고리즘은 초기 함수로 시작하도록 설계되어 있으며, 과제를 반복적으로 수행하면서 받는 피드백에 따라 이 함수를 조정합니다. 피드백은 컴퓨터가 과제를 얼마나 잘 수행하고 있는지에 대한 어떤 종류의 측정일 수 있습니다(예를 들어, 위의 예시에서 게임에서 이겼는지 졌는지, 그리고 얼마나 빨리 그렇게 되었는지) – 이러한 접근법을 **강화학습(reinforcement learning)**이라고 합니다. 또는 알고리즘이 사전에 얻은 문제별 데이터(**훈련 데이터(training data)**라고 함)를 참조로 사용하여 과제를 반복적으로 수행하고 적절한 조정을 하며, 이를 통해 새롭고 보지 못한 데이터에 대해서도 요구되는 과제를 신뢰성 있게 수행할 수 있는 수학적 함수를 만들어냅니다.

> 강화학습과 지도학습(supervised learning)의 차이는 학습 신호의 본질에 있습니다. 강화학습에서는 "보상(reward)"이라는 희소한(sparse) 신호만 받습니다. 체스 게임에서 승리는 +1, 패배는 -1처럼 게임 끝에만 신호가 옵니다. 시스템은 과거의 어떤 행동이 이 최종 결과에 기여했는지 스스로 파악해야 합니다(이를 **신용 할당 문제(credit assignment problem)**라고 합니다). 반면 지도학습에서는 각 입력에 대해 정확한 "정답"이 훈련 데이터에 포함되어 있습니다. 예를 들어 고양이 이미지 분류기를 훈련할 때, 각 이미지에는 "고양이" 또는 "고양이 아님"이라는 명시적 레이블이 붙어 있습니다. 강화학습은 정답을 명시하기 어려운 복잡한 의사결정 문제에 적합하고, 지도학습은 입출력 쌍의 예시를 많이 확보할 수 있는 패턴 인식 문제에 적합합니다. 최근의 많은 돌파구는 이 두 접근법을 결합한 데서 나왔습니다.

> 머신러닝의 핵심 도전 과제 중 하나는 **일반화(generalization)**입니다. 훈련 데이터에서 잘 작동하는 함수를 찾는 것은 비교적 쉽습니다(극단적으로는 모든 훈련 예시를 단순히 암기할 수도 있습니다). 진짜 어려운 문제는 훈련 중에 보지 못한 새로운 데이터에서도 잘 작동하는 함수를 찾는 것입니다. 이는 수학적으로 **편향-분산 트레이드오프(bias-variance tradeoff)**로 형식화됩니다. 너무 단순한 모델(높은 편향)은 데이터의 진짜 패턴을 포착하지 못하고(과소적합, underfitting), 너무 복잡한 모델(높은 분산)은 훈련 데이터의 잡음까지 학습합니다(과적합, overfitting). 최적의 모델은 이 둘 사이의 균형점에 있으며, 이것이 바로 통계적 학습 이론(statistical learning theory)의 핵심 주제입니다.

더 자세한 내용은 우리의 소개글 [Maths in a minute: Machine learning and neural networks](https://plus.maths.org/content/maths-minute-machine-learning-and-neural-networks)에서 읽을 수 있으며, Chris Budd의 글 [What is machine learning?](https://plus.maths.org/content/what-machine-learning)에서 더 많은 세부 사항을 찾을 수 있습니다.

### 이 글에 대하여

이 글은 Kweku Abraham, Chris Budd, Marianne Freiberger, Yury Korolev, Rachel Thomas가 작성했습니다.

[Kweku Abraham](https://maths4dl.ac.uk/team-member/kweku-abraham)은 University of Cambridge의 통계학 박사후연구원으로 딥러닝의 수학적 기초에 관한 연구를 하고 있습니다.

[Chris Budd](https://maths4dl.ac.uk/team-member/chris-budd-obe)는 University of Bath를 기반으로 활동하며 응용수학 교수입니다. 그는 또한 Royal Institution의 수학 교수이자 Gresham College의 기하학 교수입니다. London Mathematical Society의 교육 담당관과 Institute of Mathematics and its Applications의 부회장을 역임했습니다.

[Yury Korolev](https://maths4dl.ac.uk/team-member/yury-korolev)는 University of Bath 수리과학과의 수학 및 데이터 과학 강사이자 EPSRC 박사후연구원이며, University of Cambridge Hughes Hall의 Quondam Fellow입니다.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)와 [Rachel Thomas](https://plus.maths.org/content/people/index.html#rachel)는 *Plus*의 편집자입니다.

*이 글은 Mathematics for Deep Learning (Maths4DL) 연구 프로그램과의 협력의 일환으로 제작되었습니다.* Maths4DL은 Bath와 Cambridge 대학교, 그리고 University College London의 연구자들을 한데 모아 이론, 모델링, 데이터, 계산을 결합하여 차세대 딥러닝의 잠재력을 개방하는 것을 목표로 합니다. Maths4DL과 함께 제작된 더 많은 콘텐츠는 [여기](https://plus.maths.org/content/tags/maths4dl)에서 볼 수 있습니다.

![Maths4DL logo](https://plus.maths.org/content/sites/plus.maths.org/files/Maths4DL/Logo.png)