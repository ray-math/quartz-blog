---
title: 딥러닝이란 무엇인가?
date: 2024-03-01
---

> [!NOTE]
> https://plus.maths.org/content/what-deep-learning
>
> 놀라운 성공을 거둔 이 기계학습 기법에 대해 알아봅니다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/front_icon_50_0.jpg?itok=idavvJFL)

**딥러닝(deep learning)**은 기계학습(machine learning)의 특정한 한 유형입니다. 기계학습 알고리즘은 특정 작업을 반복적으로 수행하면서 직접 경험을 통해 학습함으로써 그 작업을 해결하도록 설계됩니다. 이러한 알고리즘은 입력(inputs)-알고리즘에 공급되는 현실 세계의 데이터-을 받아서 출력(outputs)-진행 중인 상황을 어떻게 해석할지에 대한 예측-을 제공합니다.

> 기계학습의 핵심은 "명시적 프로그래밍 없이 학습하는 능력"입니다. 전통적인 프로그램은 "입력 A가 들어오면 규칙 B를 따라 출력 C를 내놓으라"는 명령을 직접 작성하는 반면, 기계학습은 많은 (입력, 출력) 쌍의 예시를 보여주면 알고리즘이 스스로 패턴을 찾아내고 규칙을 추론합니다. 이는 인간이 경험을 통해 배우는 방식과 유사하며, 복잡하고 규칙을 명시하기 어려운 문제들-이미지 인식, 음성 이해, 자연어 번역 등-을 해결하는 데 매우 효과적입니다.

전체 인공지능 FAQ를 보려면 [여기](https://plus.maths.org/content/artificial-intelligence-and-deep-learning-your-questions-answered)를 클릭하세요.

딥러닝 알고리즘은 현대 알고리즘 중 가장 효과적인 것들에 속합니다. 단순히 입력을 출력으로 변환하는 대신, 입력을 "가짜 입력(fake inputs)"으로 변환하고, 이것을 유사한 과정을 통해-잠재적으로 여러 번-다시 처리한 후, 마지막 단계에서 얻은 것들을 실제 출력으로 제공합니다. 이름에 들어있는 "deep(깊은)"이라는 단어는 바로 이 반복적인 절차를 가리킵니다. 물론 최종적으로 얻는 것은 결국 입력을 출력으로 변환하는 방법일 뿐이지만, 이렇게 깊게 층을 쌓아서 처리하는 방식이 많은 문제에서 놀랍도록 잘 작동하는 것으로 밝혀졌습니다.

> "가짜 입력"이라는 표현은 중간 단계의 표현(intermediate representation)을 의미합니다. 예를 들어 고양이 사진을 분류하는 문제를 생각해보면, 원본 입력은 수백만 개의 픽셀 값들입니다. 첫 번째 층은 이를 "선분과 곡선의 모음"으로 변환하고, 두 번째 층은 이를 "눈, 귀, 수염 같은 부분들"로 변환하며, 세 번째 층은 이를 "고양이의 얼굴 구조"로 변환합니다. 각 단계의 출력이 다음 단계의 입력이 되는데, 이것이 원본 이미지는 아니지만 그로부터 파생된 것이기에 "가짜 입력"이라 부를 수 있습니다. 이러한 계층적 표현 학습(hierarchical representation learning)이 딥러닝의 핵심 아이디어입니다.

1980년대부터 **신경망(neural networks)**이 기계학습의 수학적 모델로 사용되어 왔습니다. 초기의 신경망은 단지 한두 개의 층으로 구성되었지만, 2000년대 초반부터 딥러닝 알고리즘이 많은 층으로 구성된 깊은 신경망(deep neural networks)을 사용하여 설계되기 시작했습니다. 딥러닝은 현재 입사 지원서 사전 심사부터 의료 분야의 혁명적인 접근법에 이르기까지 다양한 작업에 사용되고 있습니다.

> 신경망이라는 이름은 생물학적 뇌의 뉴런 구조에서 영감을 받았습니다. 뇌에서 각 뉴런은 여러 입력 신호를 받아 가중합을 계산하고, 특정 임계값을 넘으면 활성화되어 다음 뉴런으로 신호를 전달합니다. 수학적 신경망도 유사하게 작동합니다: 각 "인공 뉴런"은 여러 입력 $x_{1}, x_{2}, \ldots, x_{n}$을 받아 가중합 $\sum_{i} w_{i} x_{i} + b$를 계산하고, 이를 활성화 함수(activation function) $\sigma$에 통과시켜 출력 $\sigma(\sum_{i} w_{i} x_{i} + b)$을 생성합니다. 1980년대에는 계산 능력의 한계와 이론적 도구의 부족으로 얕은 신경망만 실용적이었지만, 컴퓨터 성능의 발전, 빅데이터의 출현, 그리고 역전파 알고리즘(backpropagation)의 개선으로 2000년대 이후 깊은 신경망이 현실화되었습니다.

![신경망](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/machibe_learning/neural_net.png)

신경망의 전형적인 구조 - 층이 많을수록 더 "깊은" 네트워크입니다. 깊은 신경망은 원래의 입력을 다음 층으로 공급되는 "가짜 입력"으로 변환하며, 이를 반복하다가 결국 출력을 생성합니다.

> 위 그림에서 왼쪽 열은 입력층(input layer), 가운데 열들은 은닉층(hidden layers), 오른쪽 열은 출력층(output layer)입니다. 각 원은 하나의 뉴런을 나타내며, 선은 연결 가중치(weight)를 나타냅니다. "은닉층"이라는 이름은 이 층들이 외부에서 직접 관찰되지 않고 네트워크 내부에 숨겨져 있기 때문입니다. 깊은 신경망의 "깊이"는 바로 이 은닉층의 개수를 의미합니다. 2012년 AlexNet이 ImageNet 대회에서 우승한 이후 네트워크는 점점 더 깊어졌고, 2015년 ResNet은 152개 층을 사용하여 인간의 이미지 인식 성능을 넘어섰습니다.

딥러닝 알고리즘의 이러한 계층적 구조는 원시 입력 데이터에서 구조를 인식하고 그 데이터를 매우 유용한 방식으로 표현할 수 있게 합니다. 예를 들어, 알고리즘이 많은 이미지 집합에서 특정 인물의 사진을 찾도록 설계되었다고 가정해봅시다. 그러면 알고리즘에 대한 원시 입력은 각 이미지의 픽셀들의 색상 값으로 표현된 이미지들이 될 것입니다. 그런 다음 네트워크의 첫 번째 층은 이미지에서 특징을 식별하도록 설계됩니다. 예를 들어 이미지의 어떤 픽셀들이 얼굴의 일부인지를 찾아냅니다. 이제 네트워크의 다음 층은 원본 이미지의 구조 없는 픽셀 덩어리를 처리해야 하는 것이 아니라, 얼굴의 형태가 이미 식별된 이미지를 처리하면 되므로 더 쉬운 작업을 수행하게 됩니다. 이런 방식으로 알고리즘은 층별로 최종 답(지정된 인물이 이미지에 있는지 여부)을 향해 나아가며, 진행하면서 점점 더 많은 특징을 추출해냅니다.

> 이것이 바로 **특징 학습(feature learning)** 또는 **표현 학습(representation learning)**의 핵심입니다. 전통적인 기계학습에서는 인간 전문가가 수작업으로 "유용한 특징"을 설계해야 했습니다. 얼굴 인식이라면 "두 눈 사이의 거리", "코의 길이", "입의 폭" 같은 특징들을 미리 정의해야 했죠. 하지만 딥러닝은 이러한 특징들을 데이터로부터 자동으로 학습합니다. 더 놀라운 것은, 하위 층에서 학습된 특징들(선분, 곡선)은 다른 문제에도 재사용될 수 있다는 점입니다. 이를 **전이 학습(transfer learning)**이라 하며, 이는 적은 데이터로도 좋은 성능을 내는 비결 중 하나입니다. 실제로 ImageNet으로 사전 학습된 네트워크는 의료 영상, 위성 이미지 분석 등 다양한 분야에서 출발점으로 활용됩니다.

*딥러닝에 대한 더 자세한 내용은 우리의 입문 기사 [Maths in a minute: Deep learning](https://plus.maths.org/content/maths-minute-deep-learning)에서 읽을 수 있습니다.*

### 이 기사에 대하여

이 기사는 Kweku Abraham, Chris Budd, Marianne Freiberger, Yury Korolev, Rachel Thomas가 작성했습니다.

[Kweku Abraham](https://maths4dl.ac.uk/team-member/kweku-abraham)은 University of Cambridge의 통계학 박사후연구원으로, 딥러닝의 수학을 연구하고 있습니다.

[Chris Budd](https://maths4dl.ac.uk/team-member/chris-budd-obe)는 University of Bath에서 응용수학 교수로 재직 중입니다. 그는 또한 Royal Institution의 수학 교수이자 Gresham College의 기하학 교수이기도 합니다. 그는 London Mathematical Society의 교육 담당관과 Institute of Mathematics and its Applications의 부회장을 역임했습니다.

[Yury Korolev](https://maths4dl.ac.uk/team-member/yury-korolev)는 University of Bath 수학과학부의 수학 및 데이터과학 강사이자 EPSRC 박사후연구원이며, University of Cambridge Hughes Hall의 Quondam Fellow입니다.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)와 [Rachel Thomas](https://plus.maths.org/content/people/index.html#rachel)는 *Plus*의 편집자입니다.

*이 기사는 Mathematics for Deep Learning (Maths4DL) 연구 프로그램과의 협력의 일환으로 제작되었습니다.* Maths4DL은 Bath, Cambridge, University College London의 연구자들을 모아 이론, 모델링, 데이터, 계산을 결합하여 차세대 딥러닝을 실현하는 것을 목표로 합니다. Maths4DL과 함께 제작된 더 많은 콘텐츠는 [여기](https://plus.maths.org/content/tags/maths4dl)에서 볼 수 있습니다.

> Maths4DL 프로그램은 딥러닝의 성공에도 불구하고 여전히 많은 부분이 이론적으로 이해되지 않고 있다는 문제의식에서 출발했습니다. 왜 이렇게 많은 매개변수를 가진 네트워크가 과적합(overfitting)되지 않는가? 왜 경사하강법(gradient descent) 같은 단순한 최적화 방법이 비볼록(non-convex) 문제에서도 좋은 해를 찾는가? 네트워크의 깊이는 정확히 무엇을 가능하게 하는가? 이러한 근본적인 수학적 질문들에 답하는 것이 단순히 학문적 호기심을 넘어, 더 효율적이고 신뢰할 수 있으며 설명 가능한 딥러닝 시스템을 설계하는 데 필수적입니다.

![Maths4DL logo](https://plus.maths.org/content/sites/plus.maths.org/files/Maths4DL/Logo.png)