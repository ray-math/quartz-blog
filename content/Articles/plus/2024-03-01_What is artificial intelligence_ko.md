---
title: 인공지능이란 무엇인가?
date: 2024-03-01
tags:
  - AI
  - 수학
  - Rachel
  - Yury
  - Intelligence
  - Artificial
  - DL
  - Korolev
---

> [!NOTE]
> https://plus.maths.org/content/what-artificial-intelligence
>
> SF에서 등장하던 AI가 이제 미디어, 정부 토론, 심지어 술집에서도 논의됩니다. 대화에 참여할 수 있도록 그 의미를 알아보세요.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/robot_frontpage_1.jpg?itok=Iktroeww)

*인공지능*(Artificial Intelligence, AI)은 컴퓨터와 같은 무생물 객체의 추론을 중심으로 하는 광범위한 개념들을 포괄하는 총칭입니다. 일반적으로 두 가지 유형으로 나뉩니다.

> 여기서 '추론(reasoning)'은 단순한 계산을 넘어서 정보를 분석하고 결론을 도출하는 인간의 사고 과정을 의미합니다. 전통적으로 추론 능력은 생명체, 특히 인간의 고유한 특성으로 여겨졌지만, AI는 이를 기계로 구현하려는 시도입니다. 이 정의가 '우산 용어(umbrella term)'라고 표현한 것은 AI가 단일한 기술이 아니라 기계 학습, 신경망, 자연어 처리 등 다양한 접근법과 기술들의 집합이기 때문입니다.

![A robot](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/machibe_learning/robot_fotolia.jpg)

강한 AI는 아직 먼 미래의 일이지만, 약한 AI는 이미 우리 곁에 있습니다.

*강한 인공지능*(Strong Artificial Intelligence, 때때로 *진정한 인공지능*이라고도 불림)은 기계가 일반 지능을 보여주는 능력을 의미합니다. 여기서 기계는 어떤 작업이든 학습할 수 있고 거의 모든 상황에 인간과 구별할 수 없을 정도로 반응할 수 있습니다. 이에 대한 표준 테스트는 1950년 [앨런 튜링(Alan Turing)](https://plus.maths.org/content/alan-turing-ahead-his-time)이 고안한 튜링 테스트입니다. 컴퓨터가 대화를 나누는 인간으로 하여금 그것이 컴퓨터인지 인간인지 구별할 수 없게 만든다면 튜링 테스트를 통과한 것입니다.

> 강한 AI의 핵심은 '일반성(generality)'입니다. 인간은 체스를 두다가 요리를 하고, 시를 쓰고, 새로운 언어를 배우는 등 한 영역에서 다른 영역으로 자유롭게 이동할 수 있습니다. 강한 AI는 이러한 영역 독립적 학습과 적응 능력을 목표로 합니다. 튜링 테스트는 1950년 튜링이 "Computing Machinery and Intelligence"라는 논문에서 제안했으며, 원래는 "모방 게임(imitation game)"이라고 불렀습니다. 이 테스트는 지능을 정의하려는 철학적 논쟁을 회피하고, 대신 행동적 관점에서 지능을 평가합니다. 즉, "기계가 생각할 수 있는가?"라는 질문을 "기계가 생각하는 것처럼 행동할 수 있는가?"로 전환한 것입니다. 이는 실용주의적 접근으로, 내부 메커니즘보다 외부 관찰 가능한 행동에 초점을 맞춥니다.

인공지능 FAQ 전체를 보려면 [여기](https://plus.maths.org/content/artificial-intelligence-and-deep-learning-your-questions-answered)를 클릭하세요.

대조적으로, *약한 인공지능*(Weak Artificial Intelligence)은 시스템이 특정한(비록 복잡하기는 하지만) 작업을 수행하도록 훈련될 수 있는 능력을 의미합니다. 강한 AI의 개념이 현재로서는 공상과학에서만 발견될 수 있는 반면, 우리는 일상생활에서 매일 약한 AI의 사례들에 둘러싸여 있습니다. 한 예는 음성 인식입니다. 이제 컴퓨터, Siri와 같은 휴대폰 기능, 심지어 자동차 보험 전화 시스템이 수학적 알고리즘을 사용하여 상당히 복잡한 음성을 인식하고 이해하며, 심지어 간단한 질문에 답하는 것이 일상적인 일이 되었습니다. 우리는 또한 ChatGPT와 생성형 AI가 놀라운 결과를 만들어내는 것에 익숙해지고 있으며, 이것들은 종종 [튜링 테스트를 통과할 수 있지만](https://www.nature.com/articles/d41586-023-02361-7), 특정 작업에 한정됩니다.

> 약한 AI의 핵심은 '특수성(specialization)'입니다. 체스를 두는 AI는 체스만 둘 수 있고, 얼굴 인식 AI는 얼굴만 인식할 수 있습니다. 이러한 시스템들은 자신이 훈련받은 영역 밖으로는 일반화할 수 없습니다. 음성 인식을 예로 들면, 이는 음향 신호를 텍스트로 변환하는 복잡한 과정으로, 푸리에 변환을 통한 주파수 분석, 은닉 마르코프 모델(Hidden Markov Models) 또는 최근의 심층 신경망을 활용합니다. 수학적으로는 고차원 확률 공간에서의 패턴 매칭 문제로 볼 수 있습니다. ChatGPT 같은 대규모 언어 모델(Large Language Models)은 흥미로운 경계 사례입니다. 특정 작업(텍스트 생성)을 위해 설계되었지만, 방대한 데이터로 훈련되어 다양한 하위 작업을 수행할 수 있습니다. 그러나 여전히 약한 AI입니다. 왜냐하면 진정으로 새로운 영역으로의 일반화, 자기 인식, 또는 목표 설정 능력이 없기 때문입니다. 튜링 테스트 통과 여부는 실제로는 미묘한 문제입니다. 제한된 대화에서는 통과할 수 있지만, 확장된 상호작용이나 다양한 맥락에서는 여전히 한계가 드러납니다.

*인공지능에 대해 더 알아보려면 Chris Budd의 글 "로봇이란 무엇인가?"를 참조하세요.*

> 약한 AI와 강한 AI의 구분은 철학자 존 설(John Searle)이 1980년 "중국어 방(Chinese Room)" 사고 실험에서 제시한 개념에서 유래했습니다. 설은 형식적 기호 조작(약한 AI)과 진정한 이해(강한 AI) 사이에는 근본적인 차이가 있다고 주장했습니다. 수학적 관점에서, 약한 AI는 특정 함수 $f: X \to Y$를 학습하는 것으로 볼 수 있습니다. 여기서 $X$는 입력 공간(예: 이미지, 음성), $Y$는 출력 공간(예: 라벨, 텍스트)입니다. 반면 강한 AI는 임의의 함수 공간에서 학습할 수 있는 메타-학습자로, 범용 근사기(universal approximator)를 넘어서는 개념입니다. 현재 AI 연구의 중심 과제는 이 간극을 어떻게 메울 것인가입니다.

### 이 글에 대하여

이 글은 Kweku Abraham, Chris Budd, Marianne Freiberger, Yury Korolev, Rachel Thomas가 작성했습니다.

[Kweku Abraham](https://maths4dl.ac.uk/team-member/kweku-abraham)은 케임브리지 대학교의 통계학 박사후 연구원으로, 딥러닝의 수학적 기초를 연구하고 있습니다.

[Chris Budd](https://maths4dl.ac.uk/team-member/chris-budd-obe)는 바스 대학교의 응용수학 교수이며, 왕립연구소(Royal Institution)의 수학 교수이자 그레샴 칼리지(Gresham College)의 기하학 교수이기도 합니다. 그는 런던 수학회(London Mathematical Society)의 교육 담당관과 수학 및 응용 연구소(Institute of Mathematics and its Applications)의 부회장을 역임했습니다.

[Yury Korolev](https://maths4dl.ac.uk/team-member/yury-korolev)는 바스 대학교 수리과학과의 수학 및 데이터 과학 강사이자 EPSRC 박사후 펠로우이며, 케임브리지 대학교 Hughes Hall의 명예 펠로우입니다.

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)와 [Rachel Thomas](https://plus.maths.org/content/people/index.html#rachel)는 *Plus*의 편집자입니다.

*이 글은 딥러닝을 위한 수학(Mathematics for Deep Learning, Maths4DL) 연구 프로그램과의 협력으로 제작되었습니다.* Maths4DL은 바스 대학교, 케임브리지 대학교, 유니버시티 칼리지 런던의 연구자들을 한데 모으며, 이론, 모델링, 데이터, 계산을 결합하여 차세대 딥러닝을 실현하는 것을 목표로 합니다. Maths4DL과 함께 제작된 더 많은 콘텐츠는 [여기](https://plus.maths.org/content/tags/maths4dl)에서 볼 수 있습니다.

> Maths4DL 프로그램은 AI의 현재 성공이 주로 경험적이고 공학적 접근에 기반한다는 인식에서 출발합니다. 예를 들어, 딥러닝 네트워크가 왜 그렇게 잘 작동하는지, 언제 실패할지, 어떻게 개선할 수 있는지에 대한 엄밀한 수학적 이해는 여전히 부족합니다. 이 프로그램은 함수 근사 이론, 최적화 이론, 통계적 학습 이론, 정보 이론 등을 활용하여 딥러닝의 이론적 토대를 구축하고자 합니다. 이는 단순히 학문적 호기심이 아니라, AI 시스템의 신뢰성, 안정성, 해석 가능성을 보장하기 위한 실용적 필요성에서 비롯된 것입니다.

![Maths4DL logo](https://plus.maths.org/content/sites/plus.maths.org/files/Maths4DL/Logo.png)