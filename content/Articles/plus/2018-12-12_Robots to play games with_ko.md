---
title: 게임을 두는 로봇들
date: 2018-12-12
tags:
  - 컴퓨터
  - 학습
  - 사용
  - Integrator
  - ELO
  - MANIAC
  - Turing
  - Stockfish
---

> [!NOTE]
> https://plus.maths.org/content/robots-play-games
>
> 체스 컴퓨터는 인공지능의 한 형태를 개발하기 위한 첫 걸음 중 하나였다. 여기 간략한 역사가 있다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/chess_frontpage.jpg?itok=P7mJbmM7)

*이 글은 Chris Budd의 Gresham College 강연 시리즈를 바탕으로 한다. 아래에서 강연 영상을 볼 수 있으며, 이 강연을 기반으로 한 다른 글들도 여기서 볼 수 있다.*

체스나 바둑과 같이 명확한 규칙 체계를 가지면서도 거의 무한에 가까운 수준의 다양한 수를 둘 수 있는 게임을 컴퓨터가 플레이하는 능력은 오랫동안 약한 인공지능(weak artificial intelligence) 개발의 시험대(이자 자극제)로 여겨져 왔다(정의는 [지난 글](https://plus.maths.org/content/what-robot)을 참조).

> 약한 인공지능은 특정한 제한된 영역에서 지능적 행동을 보이는 시스템을 의미한다. 체스나 바둑에서처럼 명확한 규칙과 목표가 있는 문제를 푸는 데 특화되어 있지만, 자의식이나 일반적인 추론 능력은 없다. 이는 인간과 같은 수준의 일반 지능을 목표로 하는 '강한 인공지능'과 대비된다. 게임은 성공을 객관적으로 측정할 수 있고 규칙이 명확하여 약한 AI 개발의 이상적인 실험장이었다.

![Alan Turing](https://plus.maths.org/issue47/features/kopieczek/Turing.jpg)

Alan Turing

더 이전으로 거슬러 올라가면, 아마도 약한 AI의 가장 초기 사례로, 전자 컴퓨터의 선구자 세 명인 [Alan Turing](https://plus.maths.org/content/alan-turing-ahead-his-time), [John Von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann), 그리고 [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon)이 기계가 사람처럼 생각할 수 있는지에 대한 질문을 던졌고, 이를 기계가 체스를 둘 수 있는지의 맥락에서 고찰했다. Turing은 종이와 연필로 작성된 시스템으로 체스를 두는 컴퓨터에 대한 연구를 시작했는데, 그 시스템에서는 그 자신이 기계의 역할을 수행했다. 1949년 Shannon은 Turing의 연구를 확장하면서 체스에 대한 자신의 관심을 이렇게 설명했다: "실용적 중요성은 없지만, 이 질문은 이론적으로 흥미로우며, [...] 이 문제가 더 중요한 의미를 가진 다른 문제들을 공략하는 데 쐐기 역할을 할 것으로 기대한다."

> Turing이 "인간 역할 체스 컴퓨터"를 만든 것은 단순한 사고 실험이 아니었다. 그는 실제로 종이에 알고리즘을 작성하고, 수를 둘 때마다 그 알고리즘을 따라가며 계산했다. 이는 컴퓨터가 아직 충분히 발전하지 않은 시대에 알고리즘의 타당성을 검증하는 방법이었다. Shannon의 언급에서 "쐐기(wedge)"라는 비유는 중요한데, 체스처럼 구조화된 문제를 푸는 방법론이 이미지 인식, 자연어 처리 등 더 복잡한 문제로 확장될 수 있다는 선견지명을 보여준다. 실제로 이후 AI 발전은 이 예측을 정확히 따라갔다.

Shannon과 그를 따른 연구자들이 사용한 접근법은 인간이 체스를 두는 방식과 관련된 전략을 사용하여 컴퓨터를 프로그래밍하려는 시도였다. Shannon은 컴퓨터 체스를 두기 위한 탐색 전략을 *타입-A(type-A)와 타입-B(type-B)*로 구분했다. 타입-A 탐색은 모든 수를 똑같이, 계산 가능한 한계까지 탐색하는 무차별 대입(brute-force) 알고리즘을 사용했다. Shannon은 당시 컴퓨터의 한계 때문에 타입-A 전략은 실용적이지 않다고 생각했다. 게다가 이들은 유망한 전략을 깊이 추구하기보다는 모든 선택지를 추적했기 때문에 너무 단순했다.

대신 Shannon은 타입-B 탐색 전략을 사용해야 한다고 제안했다. 이들은 두 가지 접근법 중 하나를 사용한다: 유망한 전략만을 추구하는 어떤 종류의 탐색을 사용하거나, 각 국면에서 알려진 좋은 수 몇 가지만을 평가하는 것이다. 후자의 경우 좋다고 판단되는 수를 제외한 모든 수를 무시하는 것을 포함한다(이를 *전진 가지치기(forward pruning)*라고도 한다). 그러나 실제로 현대의 체스를 두는 컴퓨터는 첫 번째 접근법을 사용한다-일부 수의 연속을 다른 것들보다 더 높게 가중치를 주고, 덜 유망한 연속에 대해서는 더 빠른 차단을 적용한다.

> 타입-A와 타입-B의 차이는 근본적으로 "모든 가능성을 보는가, 아니면 선택적으로 보는가"의 문제다. 타입-A는 완전하지만 비효율적이다. 체스에서 평균적으로 각 수마다 약 35개의 합법적인 수가 있고, 10수를 내다본다면 $35^{10} \approx 2.8 \times 10^{15}$개의 경우를 계산해야 한다. 타입-B는 인간 체스 선수가 "이 수는 명백히 나쁘니 고려하지 않겠다"고 판단하는 방식을 모방한다. 흥미롭게도 현대 엔진은 타입-A에 가까워졌다. 하드웨어가 발전하면서 "전부 보되, 중요한 것은 더 깊이 본다"는 전략이 가능해졌기 때문이다. 이는 Shannon의 예측과 달리, 때로는 단순한 방법이 영리한 방법을 이길 수 있음을 보여준다.

![Claude Shannon](https://plus.maths.org/issue15/features/shannon/shannon.jpg)

초기 인공지능 실험 중 하나인 전기기계식 쥐 Theseus와 함께 있는 Claude Shannon. (Image Copyright 2001 Lucent Technologies, Inc. All rights reserved.)

Shannon의 연구 이후 체스 프로그램들은 그가 제안한 방향을 따라 개발되었고 빠르게 인간만큼 실력이 좋아졌다. 주요 돌파구는 1996년 체스를 두는 코드 [Deep Blue](https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer))가 세계 챔피언 그랜드마스터 [Garry Kasparov](https://en.wikipedia.org/wiki/Garry_Kasparov)를 이겼을 때 찾아왔다. 주목할 만하게 Deep Blue는 초당 2억 개의 국면을 평가할 수 있었다.

> Deep Blue와 Kasparov의 대결은 단순한 게임 경기 이상의 의미를 가졌다. 이는 "기계가 인간의 지적 영역을 침범할 수 있는가"라는 철학적 질문의 상징이 되었다. Kasparov는 패배 후 Deep Blue가 특정 수에서 "너무 인간적인" 판단을 했다며 인간 개입을 의심했다(실제로는 버그였던 것으로 밝혀졌다). 초당 2억 국면 평가는 오늘날 기준으로는 느리지만, 1996년 당시로서는 경이로운 성능이었다. 이는 특수 제작된 체스 전용 칩을 사용한 결과였다.

더 최근에 Shannon의 아이디어를 기반으로 한 "궁극의" 체스 프로그램은 어떤 인간 플레이어도 이길 수 있는 코드 *Stockfish*였다. 완벽한 체스 프로그램이 도착했다... 아니면 그랬을까? 2017년 말 기계 학습의 돌파구와 함께 모든 것이 다시 변했다. Google Mind의 팀은 거대하고(매우 계산 집약적인) 심층 학습 신경망 기반 기계 학습 알고리즘인 [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero)를 개발했다. 그들은 체스의 규칙만을 주고 게임에 대한 다른 정보는 전혀 주지 않았다. AlphaZero는 그 후 여러 시간 동안 자기 자신과 대국하며, 순수하게 플레이로부터 직접적인 인간 입력 없이 체스 전략을 학습했다.

이후 AlphaZero는 Stockfish와 대결하여 28승, 72무, 0패의 점수로 결정적으로 이겼다! 이러한 프로그램의 품질을 측정하는 척도는 플레이 수준을 측정하는 [ELO 등급](https://en.wikipedia.org/wiki/Elo_rating_system)이다. Stockfish는 3226의 ELO를 가지고 있고, AlphaZero는 3500의 ELO에 접근하고 있으며, 인간의 최고 등급은 2800이다. 아래 그래프는 한 수에 짧은 시간만 허용되면 Stockfish가 이긴다는 것을 보여준다. 그러나 컴퓨터에게 수당 10초를 주면 AlphaZero가 매번 이긴다.

> ELO 등급은 체스 선수의 실력을 수치화한 시스템으로, 헝가리 물리학자 Arpad Elo가 개발했다. 두 선수의 ELO 차이가 400점이면 높은 쪽이 약 90% 확률로 이긴다. AlphaZero와 Stockfish의 약 300점 차이는 압도적이다. 더 흥미로운 점은 시간에 따른 성능 변화다. Stockfish는 빠른 평가에 최적화되어 있어 짧은 시간에는 우위를 보이지만, AlphaZero의 신경망 기반 평가는 더 많은 계산 시간을 받을수록 품질이 급격히 향상된다. 이는 "얼마나 빨리 계산하는가"보다 "얼마나 잘 평가하는가"가 중요함을 시사한다.

![ELO of AlphaGo versus ELO of Stockfish](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/machibe_learning/elo.jpg)

AlphaGo와 Stockfish의 ELO 등급 및 수를 두는 데 주어진 시간에 따른 의존성. 이 그래프는 D Silver 등의 논문 *Mastering chess and shogi by self-play with a general reinforcement learning algorithm*에서 가져왔다.

비슷한 접근법이 2016년 바둑을 두는 컴퓨터 [AlphaGo Zero](https://en.wikipedia.org/wiki/AlphaGo_Zero)를 개발하는 데 사용되었다. AlphaZero처럼, 이것은 바둑의 규칙과 판의 대칭 속성 외에는 아무런 입력도 받지 않았다. 24시간 자기 대국을 통해 곧 바둑 그랜드마스터 Lee Se-dol(이세돌)을 능가하는 능력을 획득했다. 우리는 이제 포커나 심지어 스크래블까지 할 수 있는 기계를 바라보고 있다.

> AlphaGo Zero의 "Zero"는 제로부터 시작한다는 의미다. 이전 버전인 AlphaGo는 수천 개의 인간 기보를 학습했지만, AlphaGo Zero는 규칙만 주어지고 스스로 게임을 수백만 번 두며 학습했다. 놀랍게도 인간 지식 없이 학습한 AlphaGo Zero가 인간 기보로 학습한 AlphaGo를 압도했다. 이는 인간의 오랜 경험과 지혜가 때로는 최적이 아닐 수 있고, 편견 없는 탐색이 더 나은 전략을 발견할 수 있음을 보여준다. 바둑은 체스보다 훨씬 복잡한데($19 \times 19$ 판에서 약 $10^{170}$개의 가능한 게임이 있다), 이를 정복한 것은 AI의 중요한 이정표였다.

### 일반 기계 학습

그렇다면 AlphaZero와 AlphaGo를 가능하게 만든 기술은 무엇이고, 어디에서 왔으며, 어디로 향하고 있는가? 특정 작업을 수행하도록 컴퓨터를 프로그래밍한다는 아이디어는 컴퓨팅 머신의 원래 개념으로 거슬러 올라간다. 이 분야의 초기 선구자 중 한 명은 Alan Turing으로, 1930년대에 *튜링 머신(Turing machine)*의 개념을 고안했다. 이 매우 단순한 장치는 원칙적으로 매우 복잡한 작업을 수행하도록 프로그래밍될 수 있었다.

> 튜링 머신은 무한히 긴 테이프, 테이프를 읽고 쓸 수 있는 헤드, 그리고 유한한 상태를 가진 제어 장치로 구성된 추상적 계산 모델이다. 놀랍도록 단순한 구조에도 불구하고, 이론적으로 어떤 알고리즘도 구현할 수 있다(계산 가능하다면). 이는 "계산이란 무엇인가?"라는 근본적 질문에 대한 수학적으로 엄밀한 답을 제공했다. 현대의 모든 컴퓨터는 본질적으로 튜링 머신의 물리적 구현이며, 튜링의 이 통찰은 컴퓨터 과학의 이론적 기초가 되었다. Church-Turing 논제는 모든 "효과적으로 계산 가능한" 함수는 튜링 머신으로 계산될 수 있다고 주장한다.

이 기본 아이디어로부터 Turing과 [Tommy Flowers](https://en.wikipedia.org/wiki/Tommy_Flowers)와 같은 영국의 다른 연구자들, 그리고 John Von Neumann이 최초의 프로그래밍 가능한 전자 컴퓨터를 만들었다. 이 모든 진전은 제2차 세계대전 중에 일어났다. Turing과 Flowers의 연구 뒤에 있던 동기는 독일인들이 사용하는 다양한 암호를 해독하는 매우 구체적인 작업이었고, 이는 [Colossus 컴퓨터](https://en.wikipedia.org/wiki/Colossus_computer)로 이어졌다. 마찬가지로 Von Neumann은 원자폭탄을 설계하는 구체적인 작업에 동기를 받았고, 이는 [ENIAC](https://en.wikipedia.org/wiki/ENIAC)과 [MANIAC 컴퓨터](https://en.wikipedia.org/wiki/MANIAC_I)로 이어졌다.

> Colossus는 1943-1945년 영국 Bletchley Park에서 개발된 세계 최초의 프로그래밍 가능한 전자 디지털 컴퓨터였다. 독일의 Lorenz 암호를 해독하기 위해 설계되었으며, 진공관 1,500개(나중에 2,400개)를 사용했다. ENIAC(Electronic Numerical Integrator and Computer)은 1945년 미국에서 완성되어 포탄 탄도 계산에 사용되었고, 18,000개의 진공관을 포함했다. MANIAC(Mathematical Analyzer Numerical Integrator and Computer)은 1952년 Los Alamos에서 완성되어 핵무기 설계에 중요한 역할을 했다. 전쟁이 컴퓨터 발전의 강력한 촉매였다는 점은 기술 발전의 역사에서 자주 보이는 아이러니다.

![The Colossus Mark 2 computer width=](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2018/machibe_learning/colossus.jpg)

Colossus Mark 2 컴퓨터는 제2차 세계대전 중 독일 암호를 해독하는 데 사용되었다.

전쟁 후 Turing과 다른 연구자들은 일반적인 작업을 수행하도록 프로그래밍될 수 있는 컴퓨터의 개발을 계속했다. 그 이후로 우리는 컴퓨터 기술과 컴퓨터를 프로그래밍하는 데 사용되는 알고리즘 및 언어의 폭발적인 성장을 보았다. (내 자신의 연구 분야는 이것과 밀접하게 관련되어 있다.) 이 성장은 기하급수적인 속도로 계속되고 있으며, [무어의 법칙(Moore's law)](https://en.wikipedia.org/wiki/Moore%27s_law)은 컴퓨터 성능이 2년마다 두 배가 된다고 예측한다.

> 무어의 법칙은 Intel의 공동 창업자 Gordon Moore가 1965년 제시한 경험적 관찰로, 집적회로의 트랜지스터 수가 약 2년마다 두 배로 증가한다는 것이다. 이는 단순한 관찰을 넘어 반도체 산업의 로드맵이 되었고, 기업들은 이 법칙을 유지하기 위해 막대한 투자를 했다. 1971년 Intel 4004 프로세서는 2,300개의 트랜지스터를 가졌지만, 2020년대의 프로세서는 수백억 개를 포함한다. 그러나 물리적 한계(원자 크기, 열 방출 등)로 인해 무어의 법칙은 최근 둔화되고 있으며, 이는 양자 컴퓨팅 같은 새로운 패러다임의 필요성을 제기한다.

최근까지 컴퓨터를 제어하는 데 사용되는 프로그램들은 일반적으로 인간 컴퓨터 프로그래머가 작성했다. 이들은 보통 [C](https://en.wikipedia.org/wiki/C_(programming_language))나 [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 또는 유사한 고급 언어로 작성되며, 그 다음 컴퓨터 아키텍처가 사용하는 기계어 명령어로 변환(컴파일되거나 인터프리트)된다. 이러한 코딩은 오류(컴퓨터 버그)가 발생하기 쉽고, 코드는 출시 전에 버그를 포함하지 않는다는 것을 보장하기 위해 종종 광범위하게 테스트되어야 한다. 우리 대부분이 너무나 잘 알고 있듯이, 이 테스트가 항상 완벽한 것은 아니다.

> 소프트웨어 버그의 역사는 컴퓨터 역사만큼이나 오래되었다. "버그(bug)"라는 용어는 1947년 Harvard Mark II 컴퓨터에서 실제 나방이 발견된 사건에서 유래했다고 알려져 있다(실제로는 그 이전부터 사용되던 용어였다). 역사상 가장 유명한 버그로는 1962년 Mariner 1 우주선을 파괴한 단일 하이픈 누락, 1996년 Ariane 5 로켓을 폭발시킨 정수 오버플로, 2000년 Y2K 문제 등이 있다. 현대 소프트웨어는 수백만 줄의 코드로 구성되어 있어 완전한 버그 제거는 사실상 불가능하며, 이는 형식 검증의 중요성을 부각시킨다.

더 최근에는 *검증 가능한 코드(provable codes)와 자동화된 추론(automated reasoning)*의 생성에서 중요한 발전이 있었다. 이러한 코드에서는 작업이 프로그래머에 의해 명시되지만, 코드는 오류를 포함하지 않는다는 것을 증명할 수 있는 방식으로 기계에 의해 작성된다. 검증 가능한 코드는 여객기의 제트 엔진 제어, 의료 기기, 사이버 보안 시스템과 같은 안전 필수 시스템의 소프트웨어 설계에서 매우 중요한 용도를 가진다.

> 형식 검증(formal verification)은 수학적 방법을 사용하여 소프트웨어나 하드웨어가 명세를 만족한다는 것을 증명하는 과정이다. 예를 들어, Hoare 논리를 사용하면 프로그램의 전후 조건(precondition과 postcondition)으로부터 정확성을 논리적으로 증명할 수 있다. CompCert는 형식적으로 검증된 C 컴파일러로, 컴파일러 자체가 버그를 도입하지 않음을 보장한다. Airbus A380의 비행 제어 소프트웨어 일부는 형식 검증을 거쳤다. 이러한 기법은 계산 비용이 높고 전문 지식이 필요하지만, 실패 비용이 매우 높은 시스템에서는 필수적이다.

그러나 컴퓨터 프로그래밍의 가장 최근 발전은 *기계 학습(machine learning)*의 개발이었다. 우리는 [다음 글](https://plus.maths.org/content/what-machine-learning)에서 이 혁명적인 기법을 살펴볼 것이다.

> 기계 학습은 프로그래밍 패러다임의 근본적 전환을 나타낸다. 전통적 프로그래밍에서는 규칙을 명시적으로 작성하지만, 기계 학습에서는 데이터로부터 규칙을 학습한다. 예를 들어, 고양이 사진을 인식하는 전통적 프로그램은 "뾰족한 귀, 수염, 특정 형태의 눈" 같은 규칙을 명시해야 하지만, 기계 학습 모델은 수천 장의 고양이 사진을 보고 스스로 특징을 추출한다. 이는 규칙을 명시하기 어려운 문제(음성 인식, 자연어 이해 등)에 특히 강력하다. AlphaZero의 성공은 체스 전략이라는 인간이 수백 년간 축적한 지식도 데이터 기반 학습으로 능가할 수 있음을 보여주었다.

### 이 글에 대하여

이 글은 Budd의 진행 중인 [Gresham College 강연 시리즈](https://www.gresham.ac.uk/series/mathematics-and-the-making-of-the-modern-and-future-world/)(위 영상 참조)의 한 강연을 기반으로 한다. 이 강연을 기반으로 한 다른 글들은 [여기](https://plus.maths.org/content/rise-machines)에서 볼 수 있다.

![Chris Budd](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2015/Mornington/chris.jpg)

Chris Budd.

Chris Budd OBE는 University of Bath의 응용수학 교수이며, [Institute of Mathematics and its Applications](http://www.ima.org.uk/)의 부회장, [Royal Institution](http://www.rigb.org/registrationControl?action=home)의 수학 의장, 그리고 [British Science Association](http://www.britishscienceassociation.org/)의 명예 펠로우이다. 그는 특히 수학을 현실 세계에 응용하고 대중의 수학 이해를 증진시키는 데 관심이 있다.

그는 Oxford University Press에서 출판된 대중 수학 책 *Mathematics Galore!*를 C. Sangwin과 공동 집필했으며, *50 Visions of Mathematics*(ed. Sam Parc.)에 등장한다.