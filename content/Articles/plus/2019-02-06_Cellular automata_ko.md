---
title: 셀룰러 오토마타
date: 2019-02-06
---

> [!NOTE]
> https://plus.maths.org/content/cellular-automata
>
> 정사각형 격자와 몇 가지 간단한 규칙이 어떻게 복잡한 패턴과 생명과 유사한 행동을 만들어내는지 알아봅니다.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/640px-textile_cone_frontpage.jpg?h=1c7b55f3&itok=wvHyHEth)

*이 기사는 Chris Budd의 진행 중인 **Gresham College 강연 시리즈** 중 한 강연에 기반합니다. 강연 영상은 **아래**에서, 그리고 이 강연에 기반한 다른 기사들은 **여기**에서 보실 수 있습니다.*

셀룰러 오토마타(cellular automata)는 물리학, 화학, 생물학 분야에서 많은 유형의 자연 현상을 모델링하는 데 널리 사용됩니다. 동물 털의 무늬부터 세균 감염까지 다양한 현상을 다룹니다. 또한 [뜨개질](https://nadiacw.github.io/softwear/2020/06/08/cellular-automata.html)을 포함한 수학적 여가 활동에도 흥미로운 응용을 가지고 있습니다. 셀룰러 오토마타는 [이전 기사](https://plus.maths.org/content/selfish-herd)에서 설명한 놀라운 동적 행동의 다양한 형태를 보여줄 수 있습니다.

> 셀룰러 오토마타는 "세포 자동기계"라고 직역할 수 있지만, 생물학적 세포와는 구별되는 개념입니다. 여기서 "셀"은 격자(grid)상의 각 칸을 의미하며, "오토마타"는 정해진 규칙에 따라 자동으로 상태가 변하는 시스템을 뜻합니다. 이는 복잡한 전체 행동이 단순한 지역 규칙의 반복적 적용으로부터 어떻게 창발(emergence)할 수 있는지를 보여주는 핵심 도구입니다. 물리학에서의 상전이(phase transition), 생물학에서의 패턴 형성(pattern formation), 컴퓨터 과학에서의 병렬 계산 등 다양한 분야에서 기본적인 모델링 도구로 사용됩니다.

셀룰러 오토마타의 개념은 1940년대에 [Stanislaw Ulam](http://www-history.mcs.st-and.ac.uk/Biographies/Ulam.html)과 [John von Neumann](http://www-history.mcs.st-andrews.ac.uk/Biographies/Von_Neumann.html)이 Los Alamos 국립연구소에 있을 때 개발되었습니다. 1970년대에 Conway의 [Game of Life](https://plus.maths.org/content/games-life-and-game-life), 즉 2차원 셀룰러 오토마타가 *Scientific American*을 통해 대중화되면서 학계를 넘어 수학적 여가 활동으로까지 관심이 확대되었습니다. 1980년대에는 [Stephen Wolfram](https://en.wikipedia.org/wiki/Stephen_Wolfram)이 1차원 셀룰러 오토마타에 대한 체계적 연구를 수행했습니다. Wolfram은 2002년에 [*A new kind of science*](https://en.wikipedia.org/wiki/A_New_Kind_of_Science)를 출판하여 셀룰러 오토마타가 과학의 많은 분야에 응용될 수 있다고 주장했습니다.

> John von Neumann은 컴퓨터 아키텍처, 게임 이론, 양자역학 등 20세기 과학의 여러 분야에 근본적인 기여를 한 천재 수학자입니다. 그가 셀룰러 오토마타를 연구한 동기는 자기복제(self-replication) 시스템을 이해하기 위함이었습니다. 생명체가 어떻게 자신의 복제본을 만들 수 있는지를 순수하게 수학적·논리적으로 설명할 수 있을까? 이 질문에 답하기 위해 그는 충분히 복잡한 셀룰러 오토마타가 자기복제 패턴을 생성할 수 있음을 보였습니다. 이는 생명 현상을 계산 가능한(computable) 과정으로 이해할 수 있다는 가능성을 처음으로 제시한 것입니다.

### 1차원

1차원 셀룰러 오토마타는 한 줄의 셀들로 구성되며, 각 셀은 숫자를 포함합니다. 규칙적인 시간 간격마다 각 셀의 숫자는 주어진 규칙에 따라 변합니다(이 규칙은 보통 이웃 셀들의 숫자에 의존합니다). 예를 들어, 다음과 같은 0과 1의 행으로 시작할 수 있습니다:

| 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 |

이것을 제1세대 행으로 간주합니다. 이제 다음의 간단한 규칙에 따라 제2세대 행을 만듭니다:

- 첫 번째 숫자는 1로, 마지막 숫자는 0으로 유지합니다
- 다른 모든 셀의 숫자는 다음과 같이 대체합니다:
  - 양쪽의 두 셀에 있는 숫자가 같으면 0으로
  - 그렇지 않으면 1로

제2세대 셀은 다음과 같습니다:

| 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |

규칙을 반복해서 적용하여 제3, 제4, 제5세대 등의 행을 만들 수 있습니다. 다음 표는 처음 다섯 세대를 보여줍니다:

| 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |

(용어에 익숙한 분들을 위해 덧붙이자면, 셀의 새로운 숫자는 이전 세대의 이웃들의 XOR입니다.)

> XOR(exclusive OR, 배타적 논리합)는 두 비트가 서로 다를 때 1, 같을 때 0을 출력하는 논리 연산입니다. 예를 들어 $0 \oplus 0 = 0$, $0 \oplus 1 = 1$, $1 \oplus 0 = 1$, $1 \oplus 1 = 0$입니다. 위의 규칙 "양쪽이 같으면 0, 다르면 1"은 정확히 XOR 연산과 동일합니다. XOR은 컴퓨터 과학과 암호학에서 매우 중요한 연산으로, 가역적(reversible)이며 자기 역원(self-inverse)이라는 특성($a \oplus b \oplus b = a$)을 가집니다. 이 단순한 연산이 놀랍도록 복잡한 패턴을 만들어낼 수 있다는 것이 셀룰러 오토마타의 핵심 통찰입니다.

이 예제에서 간단한 규칙이 복잡한 패턴을 만들어낼 수 있다는 것이 분명합니다. 0을 포함한 각 셀을 흰색으로, 1을 포함한 각 셀을 검은색으로 칠하면 패턴을 더 잘 시각화할 수 있습니다. 위의 예와 달리, 첫 번째 행이 정중앙에 단 하나의 검은 셀(단일 1)만 포함하는 경우, 위 규칙의 처음 15세대는 다음과 같이 보입니다:

![규칙 90.](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2019/budd/rule_90.png)

규칙 90. 맨 위 행은 각 셀의 색이 이전 세대에서 자신의 색과 이웃의 색에 따라 어떻게 변하는지를 보여줍니다. 이 그림은 Wolfram Demonstrations Project의 Daniel de Souza Carvalho가 만든 [Representing Elementary Cellular Automaton Rules](http://demonstrations.wolfram.com/RepresentingElementaryCellularAutomatonRules/)를 사용하여 만들었습니다.

규칙을 계속 적용하면 다음과 같은 패턴이 나타납니다. 이것은 정확히 [파스칼의 삼각형(Pascal's triangle)](https://en.wikipedia.org/wiki/Pascal%27s_triangle)의 홀수 값을 검은색으로, 짝수 값을 흰색으로 칠한 것과 같습니다. 이 패턴은 매우 풍부한 구조를 가지고 있습니다. 실제로 이것은 [프랙탈(fractal)](https://plus.maths.org/content/fantastic-fractals)로, [시어핀스키 개스킷(Sierpinski gasket)](https://plus.maths.org/content/os/issue55/features/kormann/index)이라고 불리며, 점점 더 작은 스케일에서 동일한 구조가 반복됩니다.

> 파스칼의 삼각형과 셀룰러 오토마타의 연결은 수학의 아름다운 통일성을 보여줍니다. 파스칼의 삼각형은 조합론(combinatorics)의 기본 대상으로, $n$번째 행 $k$번째 위치의 수는 이항계수(binomial coefficient) $\binom{n}{k} = \frac{n!}{k!(n-k)!}$입니다. 이 계수들은 $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$라는 재귀 관계를 만족합니다. 놀랍게도, 이항계수를 2로 나눈 나머지(mod 2)를 취하면, 이 재귀 관계가 정확히 XOR 연산과 동치가 됩니다. 즉, 대수학(조합론), 기하학(프랙탈 구조), 그리고 계산 이론(셀룰러 오토마타)이 모두 하나의 대상으로 수렴하는 것입니다. 이는 수학의 서로 다른 분야들이 깊은 수준에서 연결되어 있음을 보여주는 아름다운 예시입니다.

![256세대까지의 규칙 90.](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2019/budd/r090_pulse_wide.png)

256세대까지의 규칙 90. 이미지: [eouw0o83hf](https://commons.wikimedia.org/wiki/File:R090_pulse_wide.png), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Wolfram은 1차원 셀룰러 오토마타에 대한 일련의 서로 다른 규칙들을 제시했으며, 이들 중 많은 것들이 놀라울 정도로 복잡한 패턴을 생성했습니다. 위의 것이 Wolfram의 규칙 90입니다. 아래는 규칙 30의 처음 15세대입니다:

![규칙 30.](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2019/budd/rule_30.png)

규칙 30. 맨 위 행은 각 셀의 색이 이전 세대에서 자신의 색과 이웃의 색에 따라 어떻게 변하는지를 보여줍니다. 이 그림은 Wolfram Demonstrations Project의 Daniel de Souza Carvalho가 만든 [Representing Elementary Cellular Automaton Rules](http://demonstrations.wolfram.com/RepresentingElementaryCellularAutomatonRules/)를 사용하여 만들었습니다.

규칙 30을 계속 적용하면 다음과 같은 패턴을 얻게 되는데, 이는 복잡한 구조로 주목할 만합니다. 왼쪽에서는 상당히 규칙적으로 보이지만, 오른쪽으로 이동하면서 이 규칙성이 사라지고, 무질서하고 혼돈적인 패턴을 볼 수 있다는 점에 주목하세요.

![256세대까지의 규칙 30.](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2019/budd/rule30-256-rows.png)

256세대까지의 규칙 30.

> 규칙 30은 결정론적 혼돈(deterministic chaos)의 놀라운 예입니다. 규칙은 완전히 결정론적이고 단순하지만, 결과는 무작위처럼 보입니다. 실제로 Wolfram은 규칙 30의 중앙 열이 생성하는 수열이 통계적으로 무작위 수열과 구별할 수 없을 정도로 무작위적이라고 주장했습니다. 이는 암호학적으로도 중요한 의미를 가집니다—단순한 결정론적 규칙으로부터 예측 불가능한 출력을 생성할 수 있다는 것입니다. 더 깊이 들어가면, 이는 계산 복잡도 이론과도 연결됩니다. 규칙 자체는 단순하지만(O(1) 복잡도), 미래의 특정 상태를 예측하는 것은 본질적으로 모든 중간 단계를 계산해야 하므로 "계산적으로 비가역적(computationally irreducible)"합니다.

Wolfram은 1차원 셀룰러 오토마타를 분류했습니다. 그는 패턴이 일반적으로 균질성으로 안정화되는 오토마타, 패턴이 진동 구조로 진화하는 오토마타, 패턴이 겉보기에 혼돈적인 방식으로 진화하는 오토마타, 그리고 패턴이 극도로 복잡해지고 안정적인 국소 구조를 가지며 오랫동안 지속될 수 있는 오토마타를 설명했습니다.

놀랍게도, 우리는 자연에서 매우 유사한 패턴을 볼 수 있습니다. 예를 들어 조개껍질에서 말이죠. 다음은 Wolfram의 규칙 30과 매우 유사한 패턴을 가진 *conus textile* 조개껍질의 예입니다. 아마도 이 패턴의 성장은 유사한 규칙에 의해 구동되는 것으로 보입니다.

![256세대까지의 규칙 90.](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2019/budd/640px-textile_cone.jpg)

*Conus textile* 조개껍질. 사진: [Richard Ling](https://commons.wikimedia.org/wiki/File:Textile_cone.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

> 조개껍질의 패턴 형성은 발생생물학(developmental biology)의 중요한 연구 주제입니다. 조개가 성장할 때, 껍질의 가장자리(mantle edge)에 있는 세포들이 탄산칼슘을 분비하여 새로운 껍질 층을 만듭니다. 이 세포들의 색소 생성 활동이 국소적 화학 신호에 따라 조절되는데, 이것이 셀룰러 오토마타의 지역 규칙과 유사합니다. 흥미롭게도, 이러한 패턴 형성은 반응-확산 시스템(reaction-diffusion system)으로도 모델링할 수 있습니다. Alan Turing이 1952년에 제안한 반응-확산 이론은 두 화학물질의 상호작용만으로도 복잡한 공간 패턴이 자발적으로 형성될 수 있음을 보였습니다. 셀룰러 오토마타와 반응-확산 시스템은 수학적으로 다르지만, 둘 다 "단순한 지역 규칙 → 복잡한 전역 패턴"이라는 동일한 원리를 구현합니다.

### 2차원

위의 아이디어를 2차원으로 확장할 수 있습니다. 숫자를 포함하는 2차원 셀 격자를 제1세대로 시작한 다음, 주어진 규칙에 따라 셀의 숫자를 대체합니다. 2차원 셀룰러 오토마타는 1940년대에 Von Neumann이 연구한 것으로 거슬러 올라가며, 종종 질병과 감염 과정을 모델링하는 데 사용됩니다.

2차원 셀룰러 오토마타의 유명한 예는 John Conway의 *Game of Life*입니다. 이것은 살아있는 유기체를 닮은 패턴을 생성한다고 알려져 있습니다. Game of Life는 무한한 2차원 정사각형 셀 격자에서 진행됩니다. 위에서와 마찬가지로, 숫자를 색상으로 대체할 수 있습니다. 초록색인 셀은 살아있는 것으로, 회색인 셀은 죽은 것으로 간주됩니다. 모든 셀은 수평, 수직 또는 대각선으로 인접한 여덟 개의 이웃 셀과 상호작용합니다. 각 시간 단계마다 다음과 같은 전이가 발생합니다:

- 살아있는 이웃이 두 개 미만인 살아있는 셀은 죽습니다 (과소 인구로 인한 것처럼).
- 살아있는 이웃이 두 개 또는 세 개인 살아있는 셀은 다음 세대로 살아남습니다.
- 살아있는 이웃이 세 개를 초과하는 살아있는 셀은 죽습니다 (과밀로 인한 것처럼).
- 정확히 세 개의 살아있는 이웃을 가진 죽은 셀은 살아있는 셀이 됩니다 (번식으로 인한 것처럼).

초기 패턴이 시스템의 씨앗(seed)을 구성합니다. 제1세대는 위의 규칙들을 씨앗의 모든 셀에 동시에 적용하여 만들어집니다. 1차원 셀룰러 오토마타에서처럼, 규칙들은 계속해서 반복적으로 적용되어 다음 세대를 만듭니다. 씨앗에 따라 매우 이국적인 패턴이 나타날 수 있습니다.

> Conway의 Game of Life는 1970년 *Scientific American*의 Martin Gardner 칼럼을 통해 소개되어 전 세계적인 현상이 되었습니다. 이 게임이 특별한 이유는 단순성과 복잡성의 놀라운 균형 때문입니다. Conway는 다음 세 가지 기준을 만족하는 규칙을 찾았습니다: (1) 대부분의 초기 패턴이 결국 소멸하거나 안정화되어야 한다, (2) 일부 초기 패턴은 무한히 성장해야 한다, (3) 시뮬레이션이 간단해야 한다. 이 세 조건의 균형점을 찾는 것이 중요했습니다. 너무 생동감이 없으면 모든 것이 곧 죽고, 너무 생동감이 넘치면 모든 것이 폭발적으로 성장하여 흥미로운 구조가 형성되지 않기 때문입니다.

우리의 놀라운 동료 Oscar Gillespie가 만든 아래의 인터랙티브 도구에서 Game of Life를 탐험할 수 있습니다. 이것은 살아있는 셀들의 무작위 패턴으로 시작합니다. 대신 자신만의 살아있는 셀의 시작 배치를 선택하고 싶다면, *Clear the grid*를 클릭한 다음 살아있게 하고 싶은 개별 셀을 클릭하세요. Game of Life의 단 한 단계만 실행하려면 *Run a generation*을 클릭하세요. 여러 단계를 실행하려면 *Run*을 클릭하세요. 그리고 다시 시작하려면 *Stop*을 클릭한 다음 *Reset*을 클릭하세요.

다음은 나타나는 흥미로운 패턴의 몇 가지 예입니다. *클로버리프(cloverleaf)*는 주기적으로 반복되는 진동 패턴입니다. 아래 비디오에서 재생을 눌러 패턴이 진화하는 것을 보세요. (우리는 Edwin Martin의 [온라인 버전 Game of Life](https://playgameoflife.com/)를 사용하여 이러한 동영상을 만들었습니다.)

연습 삼아, 완전히 고정된 상태로 남아있는 패턴을 찾아보세요.

> 완전히 고정된 패턴을 "정지 생명(still life)"이라고 부릅니다. 가장 간단한 예는 2×2 정사각형(블록)입니다. 각 살아있는 셀이 정확히 3개의 살아있는 이웃을 가지므로 규칙에 따라 계속 살아남습니다. 다른 예로는 "벌집(beehive)", "빵(loaf)", "배(boat)" 등이 있습니다. 이러한 정지 생명들은 안정적인 구조물로, 더 복잡한 패턴의 구성 요소가 되기도 합니다. 흥미롭게도, 주어진 $n$개의 살아있는 셀로 만들 수 있는 정지 생명의 개수를 세는 것은 비자명한 조합론 문제입니다.

*해머헤드 우주선(hammerhead spaceship)*의 모양도 시간상 주기적으로 반복되지만, 마치 어딘가 갈 곳이 있는 것처럼 격자를 따라 이동합니다.

유명한 패턴은 *글라이더(glider)*로, 이름에서 알 수 있듯이 격자를 가로질러 미끄러지듯 이동합니다.

> 글라이더는 Game of Life에서 가장 작은 우주선(spaceship)으로, 5개의 살아있는 셀로 구성되며 4세대마다 한 칸 대각선으로 이동합니다. 글라이더의 발견은 Game of Life가 단순한 장난감이 아니라는 것을 보여주었습니다. 정보를 한 위치에서 다른 위치로 전달할 수 있다는 것은 계산을 수행할 수 있다는 것을 의미합니다. 실제로 Game of Life는 튜링 완전(Turing complete)하다는 것이 증명되었습니다. 즉, 충분히 큰 격자와 적절한 초기 구성이 주어지면, 어떤 계산 가능한 함수든 Game of Life 패턴으로 시뮬레이션할 수 있습니다. 이는 범용 컴퓨터를 Game of Life 안에서 구현할 수 있다는 놀라운 사실입니다.

*고스퍼 글라이더 총(Gosper glider gun)*은 마치 설계된 것처럼 끝없이 글라이더 스트림을 생성합니다.

> 고스퍼 글라이더 총은 Bill Gosper가 1970년에 발견한 것으로, Game of Life 역사에서 중요한 이정표입니다. Conway는 무한히 성장하는 패턴이 존재하는지 몰랐고, 이에 대해 50달러 상금을 걸었습니다. Gosper는 36개의 살아있는 셀로 구성된 패턴을 발견했는데, 이것은 30세대마다 글라이더를 하나씩 발사합니다. 이 글라이더들이 무한히 멀리 날아가므로, 살아있는 셀의 총 개수는 무한히 증가합니다. 이 발견은 Game of Life가 단순히 안정화되거나 소멸하는 것이 아니라, 진정으로 성장하고 진화할 수 있음을 보여주었습니다. 더 나아가, 글라이더 총은 논리 회로의 구성 요소로 사용될 수 있어, Game of Life의 계산 능력을 실제로 활용하는 길을 열었습니다.

Game of Life가 실제 생명 과정을 모방한다는 주장들이 있었습니다 (심지어 인류 전체가 외계 존재들이 진행하는 어떤 셀룰러 오토마타의 에이전트일 뿐이라는 주장도!). 이것이 이론적으로는 가능하지만 극도로 억지스럽습니다. 실제로 John Conway는 복잡하고 진화하는 패턴을 만들어낼 가능한 가장 간단한 규칙 집합을 찾기 위해 Game of Life를 설계했습니다. Game of Life에 대한 자세한 내용은 [Conway와의 인터뷰](https://plus.maths.org/content/games-life-and-game-life)에서 확인할 수 있습니다.

> Game of Life와 실제 생명의 유사성은 제한적입니다. 실제 생명 시스템은 열역학 법칙을 따르며, 에너지와 물질의 흐름이 필요하고, 화학적 과정에 의존하며, 확률적 요소가 있습니다. 반면 Game of Life는 완전히 결정론적이고, 에너지 개념이 없으며, 순수하게 정보적입니다. 그러나 Game of Life가 중요한 이유는 실제 생명을 정확히 모델링하기 때문이 아니라, 생명의 핵심 특성들—자기조직화(self-organization), 창발적 복잡성(emergent complexity), 정보 처리—이 단순한 규칙으로부터 어떻게 나타날 수 있는지를 보여주기 때문입니다. 이는 환원주의(reductionism)의 한계를 보여주는 동시에, 복잡한 현상을 이해하는 새로운 방법론을 제시합니다.

그러나 2차원 (그리고 실제로 3차원) 셀룰러 오토마타가 박테리아, 질병, 감염의 작용을 모델링하는 데 매우 효과적으로 사용되는 것은 확실히 사실입니다. 특히 격자의 셀로 생물학적 세포를 모델링할 수 있고, 다른 셀로 박테리아를 모델링할 수도 있습니다. Game of Life에서처럼 생물학적 세포와 박테리아를 살아있거나 죽은 것으로 볼 수 있습니다. 이러한 모델은 Von Neumann의 작업에 대한 원래 동기였으며 많은 유형의 질병 전파를 연구하는 데 예측적으로 사용됩니다.

> 전염병 모델링에서 셀룰러 오토마타는 SIR(Susceptible-Infected-Recovered) 모델과 같은 미분방정식 기반 모델을 보완합니다. 셀룰러 오토마타의 장점은 공간적 이질성(spatial heterogeneity)과 개별 에이전트의 행동을 자연스럽게 포함할 수 있다는 점입니다. 예를 들어, COVID-19 확산을 모델링할 때, 각 셀은 지리적 위치를 나타낼 수 있고, 상태는 감염되지 않음/잠복기/감염성/회복됨/사망 등으로 세분화될 수 있습니다. 이웃 셀과의 상호작용 확률은 사회적 거리두기, 마스크 착용 등의 개입을 반영할 수 있습니다. 이러한 모델들은 정책 결정에 실제로 사용되며, 다양한 시나리오("만약 학교를 폐쇄하면?", "백신 접종률이 70%에 도달하면?")를 시뮬레이션하여 비교할 수 있게 해줍니다.

셀룰러 오토마타는 질서있고 목적이 있어 보이는 행동이 단순한 규칙에 따라 상호작용하는 무의식적 존재들—셀들—로부터 어떻게 나타날 수 있는지를 보여줍니다. 그리고 이 기사의 시작 부분에서 이미 언급했듯이, 이들은 자연에서 발생하는 많은 시스템을 시뮬레이션하는 데 사용될 수 있습니다. [다음 기사](https://plus.maths.org/content/agm)에서는 개별 존재들이 이동할 수 있도록 하는 시스템 유형을 살펴보겠습니다. 이것들은 *에이전트 기반 모델(agent based models)*이라고 불립니다.

> 에이전트 기반 모델(ABM)은 셀룰러 오토마타의 자연스러운 확장입니다. 셀룰러 오토마타에서는 에이전트(셀)가 고정된 격자에 묶여 있지만, ABM에서는 에이전트가 공간을 자유롭게 이동할 수 있습니다. 각 에이전트는 자신만의 상태와 행동 규칙을 가지며, 환경 및 다른 에이전트와 상호작용합니다. ABM은 경제학(시장 동역학), 사회학(여론 형성), 생태학(포식자-피식자 관계), 도시계획(교통 흐름) 등 다양한 분야에서 사용됩니다. 핵심 아이디어는 동일합니다: 미시적 수준(개별 에이전트)의 단순한 규칙이 거시적 수준(전체 시스템)에서 복잡한 창발적 행동을 만들어낸다는 것입니다. 이는 하향식(top-down) 접근과 대조되는 상향식(bottom-up) 모델링 패러다임의 핵심입니다.

### 저자 소개

이 기사는 Budd의 진행 중인 [Gresham College 강연 시리즈](https://www.gresham.ac.uk/series/mathematics-and-the-making-of-the-modern-and-future-world/) 중 한 강연에 기반합니다 (위의 비디오 참조). 이 강연에 기반한 다른 기사들은 [여기](https://plus.maths.org/content/maths-crowd)에서 볼 수 있습니다.

![Chris Budd](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2015/Mornington/chris.jpg)

Chris Budd.

Chris Budd OBE는 University of Bath의 응용수학 교수이며, [Institute of Mathematics and its Applications](http://www.ima.org.uk/)의 부회장, [Royal Institution](http://www.rigb.org/registrationControl?action=home)의 수학 의장, 그리고 [British Science Association](http://www.britishscienceassociation.org/)의 명예 펠로우입니다. 그는 특히 수학을 실제 세계에 적용하고 수학의 대중적 이해를 증진하는 데 관심이 있습니다.

그는 Oxford University Press에서 출판된 대중 수학 책 [*Mathematics Galore!*](https://plus.maths.org/content/mathematics-galore)를 C. Sangwin과 공저했으며, Sam Parc가 편집한 책 [*50 Visions of Mathematics*](https://global.oup.com/academic/product/50-visions-of-mathematics-9780198701811?cc=gb&lang=en&)에 등장합니다.