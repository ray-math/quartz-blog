---
title: 구구단에 숨겨진 아름다움
date: 2017-04-07
tags:
  - 대칭
  - 수학
  - 시각
  - common
  - 독학
  - 배수
  - 합동
  - 블록
---

> [!NOTE]
> https://plus.maths.org/content/hidden-beauty-multiplication-tables
>
> 단순한 산술 안에 숨어있는 놀라운 패턴들

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/multi_frontpage.jpg?itok=bNy_vfFk)

이 글에서는 양의 정수 곱셈표 안에 숨어있는 놀라운 대칭성들을 탐구해보겠습니다.

> 대칭성(symmetry)은 수학에서 가장 근본적인 개념 중 하나입니다. 기하학적 대칭뿐 아니라 대수적, 조합론적 구조에서도 대칭성은 핵심적인 역할을 합니다. 이 글에서 다루는 구구단의 대칭성은 초등 정수론(elementary number theory)과 시각화가 만나는 지점으로, 추상적인 수론 개념들이 어떻게 아름다운 기하학적 패턴으로 드러날 수 있는지 보여줍니다.

표준 곱셈표부터 시작하겠습니다. 아래 표는 첫 번째 행과 첫 번째 열에 1부터 10까지의 수를 담고 있습니다. 다른 모든 칸은 해당 행의 첫 번째 수와 해당 열의 첫 번째 수의 곱을 담고 있습니다.

![Table 0](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table0.png)

![Table 1](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table1.png)

### 하나의 배수

$k = 2$부터 시작하겠습니다. 곱셈표에서 $2$의 배수인 모든 칸에 파란색을 칠합니다. (숫자 $0$은 $2$의 배수이므로, 모든 $0$이 들어간 칸도 파란색입니다.)

![Table 2](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table2.png)

여기서는 표를 가로 방향으로 15까지 확장했습니다. 실제로 양의 정수에 대한 완전한 곱셈표는 양쪽 방향으로 무한하기 때문에, 앞으로도 새롭게 나타나는 패턴을 더 명확하게 보여주기 위해 표의 크기를 계속 조정할 것입니다.

> 여기서 중요한 관찰은 곱셈표가 주기적(periodic) 구조를 갖는다는 점입니다. 수론에서 주기성은 합동식(congruence)과 밀접하게 연관되어 있습니다. $2$의 배수로 칠해진 패턴의 주기성은 본질적으로 "modulo 2" 연산, 즉 $2$로 나눈 나머지를 고려하는 것과 같습니다. 이러한 관점은 추후 나머지 연산을 다룰 때 더욱 명확해질 것입니다.

위의 전체 패턴은 다음의 기본 구성 블록(fundamental building block)을 사용하여 조립될 수 있습니다:

![Fundamental building block](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/block.png)

> 이 $2 \times 2$ 기본 블록은 타일링(tiling) 개념을 보여줍니다. 평면을 특정 도형으로 빈틈없이 채우는 타일링은 기하학과 조합론의 중요한 주제입니다. 여기서는 곱셈표의 주기적 구조가 이러한 타일링으로 나타나며, 각 기본 블록의 크기는 우리가 고려하는 배수(여기서는 $2$)에 의해 결정됩니다. $2$의 배수를 고려할 때 기본 블록이 $2 \times 2$인 이유는 곱셈표의 $(i, j)$ 위치의 값이 $ij$이고, $2 \mid ij$인 조건이 $2$ 단위로 반복되기 때문입니다.

![Table 3](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table3.png)

![Table 4](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table4.png)

### 연속된 수들의 여러 배수

여러 배수와 그에 대응하는 여러 색상을 사용하면 더 흥미로운 패턴이 나타납니다. 다음 그림에서는 $2$의 배수인 수들을 빨간색으로, $3$의 배수인 수들을 주황색으로 칠했습니다. (단, $2$와 $3$ 모두의 배수, 즉 $6$의 배수인 경우에는 주황색이 빨간색보다 우선합니다.) 이렇게 하면 다음과 같은 패턴이 나타납니다.

![Table 5](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table5.png)

> 이제 우리는 두 소수 $2$와 $3$의 배수를 동시에 고려하고 있습니다. 색상의 우선순위를 정하는 것은 벤 다이어그램(Venn diagram)에서 교집합을 처리하는 방식과 유사합니다. $6$의 배수(즉, $\text{lcm}(2, 3) = 6$의 배수)에 주황색을 부여함으로써, 우리는 본질적으로 수들의 계층 구조를 시각화하고 있습니다. 이러한 방식은 포함-배제 원리(inclusion-exclusion principle)의 시각적 표현으로 볼 수 있으며, 정수론에서 중요한 개념인 최소공배수(least common multiple, LCM)와 최대공약수(greatest common divisor, GCD)의 역할을 드러냅니다.

![Table 6](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table6.png)

이 게임을 무한히 계속할 수 있습니다. 다음 네 그림은 각각 4개, 5개, 6개, 7개의 연속된 수들의 배수를 사용하며, 그에 따라 4개, 5개, 6개, 7개의 색상을 사용합니다. 어떤 패턴을 발견할 수 있나요? (반사) 대칭축을 찾을 수 있나요? 각 경우에 대칭성의 기본(반복) 구성 블록의 크기는 얼마나 되어야 할까요? 답은 아래 댓글란에 게시할 수 있으며, 답을 찾지 못한 경우 몇 주 후에 답을 공개하겠습니다.

> 여기서 핵심적인 수학적 질문은 기본 블록의 크기가 어떻게 결정되는가입니다. $n$개의 연속된 정수 $1, 2, \ldots, n$의 배수를 고려할 때, 기본 블록의 크기는 $\text{lcm}(1, 2, \ldots, n) \times \text{lcm}(1, 2, \ldots, n)$이 됩니다. 예를 들어, $n = 4$일 때 $\text{lcm}(1, 2, 3, 4) = 12$이므로 기본 블록은 $12 \times 12 = 144$개의 작은 정사각형으로 구성됩니다. 이 최소공배수는 소인수분해를 통해 효율적으로 계산할 수 있으며, 각 소수의 최대 거듭제곱을 취하면 됩니다. 대칭축의 존재는 곱셈의 교환법칙 $ab = ba$에서 비롯되며, 이는 주대각선에 대한 대칭을 만듭니다.

(이미지를 클릭하면 더 큰 버전을 볼 수 있습니다.)

![Table 7](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table7.jpg)

![Table 8](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table8.jpg)

![Table 9](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table9.jpg)

![Table 10](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table10.jpg)

### 연속되지 않은 수들의 배수

이제 연속되지 않은 $k$ 값들을 사용해봅시다. 다음 그림은 $6$의 배수인 수들에는 파란색을, $9$의 배수인 수들에는 초록색을 사용합니다. (이미지를 클릭하면 더 큰 버전을 볼 수 있습니다.)

[기본 구성 블록은 이제 $18 \times 18 = 324$개의 작은 정사각형으로 구성됩니다. 왜냐하면 $18$이 $6$과 $9$의 최소공배수이기 때문입니다. 그럼에도 불구하고 반복되는 $17 \times 17$ 정사각형을 구성하는 아홉 개의 $5 \times 5$ 정사각형 내부의 추가적인 대칭성은 기분 좋은 놀라움으로 다가올 것입니다. 이것들에 대한 수학적 설명을 찾을 수 있나요?](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table11_large.jpg)

> 연속되지 않은 수를 선택하면 더욱 복잡하고 흥미로운 패턴이 나타납니다. $6 = 2 \times 3$과 $9 = 3^{2}$을 선택한 경우, 이 두 수는 공통 소인수 $3$을 공유합니다. 이는 $\text{gcd}(6, 9) = 3$이고 $\text{lcm}(6, 9) = 18$임을 의미합니다. 패턴 내부의 추가적인 대칭성은 이러한 수론적 관계에서 비롯됩니다. 구체적으로, $6$과 $9$의 배수 구조는 각각 $2 \times 3$과 $3 \times 3$의 인수 구조를 반영하며, 이들의 상호작용이 더 미세한 부대칭(subsymmetry)을 만들어냅니다. 이는 군론(group theory)의 부분군(subgroup) 구조와도 연결되는 깊은 개념입니다.

![Table 11](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table11.jpg)

다음은 여러분이 감상할 수 있는 몇 가지 패턴입니다. 각 경우에 연속되지 않은 수들의 배수에 색을 칠했습니다. 어떤 수들인지, 그리고 어떤 패턴이 나타나는지 설명할 수 있나요? 답은 아래 댓글란에 게시할 수 있으며, 답을 찾지 못한 경우 몇 주 후에 답을 공개하겠습니다.

> 이러한 시각화 연습은 단순한 미적 즐거움을 넘어 중요한 수학적 통찰을 제공합니다. 패턴을 관찰하고 그 배후의 수들을 역추적하는 과정은 귀납적 추론(inductive reasoning)의 훌륭한 예시입니다. 또한 시각적 패턴의 주기성, 대칭성, 복잡도를 분석함으로써 선택된 수들의 소인수분해, 최대공약수, 최소공배수 같은 수론적 성질을 추론할 수 있습니다. 이는 추상적 수학과 구체적 시각 사이의 강력한 연결을 보여줍니다.

(이미지를 클릭하면 더 큰 버전을 볼 수 있습니다.)

![Table 12](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table12.jpg)

![Table 13](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table13.jpg)

![Table 14](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table14.jpg)

![Table 15](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table15.jpg)

![Table 16](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table16.jpg)

### 나머지 연산

마지막으로, 어떤 수 $k$를 고정하고 $k$에 대한 나머지에 따라 칸에 색을 부여하면 모든 정사각형을 칠할 수 있습니다. 예를 들어, $5$의 배수는 검은색으로, $5$로 나눈 나머지가 $1$인 수는 초록색으로, 나머지가 $2$인 수는 빨간색으로, 나머지가 $3$인 수는 보라색으로, 나머지가 $4$인 수는 노란색으로 칠하면 다음과 같은 그림이 얻어집니다. (이미지를 클릭하면 더 큰 버전을 볼 수 있습니다.)

> 이것이 바로 합동 산술(modular arithmetic)의 시각화입니다. 합동 산술은 현대 암호학, 컴퓨터 과학, 정수론의 핵심 도구입니다. 수를 $k$로 나눈 나머지에 따라 분류하는 것은 정수들을 $k$개의 동치류(equivalence class)로 나누는 것과 같으며, 이는 $\mathbb{Z}/k\mathbb{Z}$(정수 modulo $k$)라는 수학적 구조를 형성합니다. 이 구조는 환(ring)의 성질을 갖습니다. 곱셈표에서 이를 시각화하면, $(a \bmod k) \cdot (b \bmod k) \equiv ab \bmod k$라는 합동의 곱셈 성질이 기하학적 패턴으로 드러납니다. 패턴의 주기성은 정확히 $k \times k$이며, 이는 나머지 체계의 완전성을 반영합니다.

![Table 17](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2017/multitables/table17.jpg)

> 특히 $k = 5$인 경우, 우리는 $\mathbb{Z}/5\mathbb{Z}$ 구조를 보고 있습니다. $5$가 소수이므로 이는 실제로 체(field)를 이룹니다. 즉, $0$이 아닌 모든 원소가 곱셈 역원을 갖습니다. 이러한 대수적 구조가 시각적 패턴에 어떻게 반영되는지 관찰하는 것은 매우 흥미롭습니다. 대칭성과 반복 패턴의 규칙성은 기저의 대수 구조의 규칙성을 직접적으로 반영합니다.

### 결론

우리는 양의 정수 곱셈표 안에 숨어있는 대칭성들을 발견했습니다. 이러한 패턴을 생성하는 것은 (예를 들어 Excel을 사용하여) 쉽고, 정수의 산술과 약수 판정법을 사용하여 큰 어려움 없이 설명할 수 있습니다. 색상을 사용하여 이러한 대칭성을 표현하는 것은 수학에 새로운 측면을 더합니다. 이러한 이미지들과 비슷한 방식으로 만들어진 다른 이미지들은 수학과 예술을 공부하는 학생들에게 어필할 수 있으며, 새로운 협업으로 이어질 수 있습니다. 적어도 이러한 이미지들이 사람들에게 흥미를 유발하고, 놀라움을 주며, 영감을 줄 수 있기를 바랍니다.

> 이 작업은 수학의 여러 분야가 어떻게 연결되는지 보여주는 훌륭한 예시입니다. 초등 정수론(배수, 약수, 나머지), 조합론(타일링, 패턴), 대수학(합동 산술, 군과 환), 그리고 기하학(대칭성, 변환)이 모두 하나의 단순한 곱셈표 안에서 만납니다. 더 나아가, 이는 수학적 아름다움이 추상적 기호 조작에만 있지 않고, 구체적이고 시각적인 형태로도 드러날 수 있음을 보여줍니다. 역사적으로도 시각화는 가우스(Gauss)의 정수론 연구에서부터 현대의 프랙탈 기하학에 이르기까지 중요한 역할을 해왔습니다. 이 글의 접근법은 복잡한 수학적 개념을 누구나 접근 가능한 시각적 경험으로 변환함으로써, 수학 교육과 대중화에 기여할 수 있습니다.

### 저자 소개

알제리 라그와트(Laghouat) 출신의 조헤이르 바르카(Zoheir Barka)는 독학한 아마추어 수학자입니다. 그는 라그와트 대학교에서 프랑스어로 석사 학위를 받았으며, 현재 초등학교에서 프랑스어 교사로 일하고 있습니다.

> 이 사례는 수학이 전문 연구자들만의 영역이 아님을 보여주는 영감적인 예입니다. 역사적으로도 많은 중요한 수학적 발견들이 아마추어 수학자들에 의해 이루어졌습니다. 페르마(Fermat)는 변호사였고, 람마누잔(Ramanujan)은 독학으로 수학을 공부했습니다. 현대에도 인터넷과 컴퓨팅 도구의 발달로 누구나 수학적 탐구를 할 수 있는 환경이 조성되었습니다. 바르카의 작업은 호기심과 열정만 있다면 누구나 수학의 아름다움을 발견하고 기여할 수 있음을 보여줍니다.

이 글의 원본은 *곱셈표의 숨겨진 대칭성(The hidden symmetries of the multiplication table)*이라는 제목으로 Journal of Humanistic Mathematics, Volume 7, Issue 1 (2017년 1월), 189-203페이지에 처음 게재되었습니다.

## 댓글

## James S.

"$5$로 나눈 나머지가 $4$인 수는 노란색"이라고 해야 맞습니다.

"$5$로 나눈 나머지가 $1$인 수는 빨간색"이라고 나와 있습니다.

## Marianne

실수를 지적해주셔서 감사합니다. 수정했습니다.

## Raúl A. Simón Eléxpuru

아름답습니다! 저자에게 축하를 보냅니다.

## Oli

정말 아름답네요. 패턴을 만드는 정수들이 변할 때 흥미로운 애니메이션을 만들 수 있을 것 같은데요. 분명히 있을 것 같습니다!

## Barka

안녕하세요! 이 링크를 확인해보시면 다양한 modulo를 표시할 수 있는 대화형 도구를 찾을 수 있습니다:

http://guzintamath.com/blog/2017/02/modulus-hidden-symmetries/

## Ken Wessen

이 글에 영감을 받아 패턴을 탐구할 수 있는 웹 앱을 만들었습니다. 여기서 찾을 수 있습니다: http://thewessens.net/ClassroomApps/Main/multiples.html?topic=number&id…

## Barka

이전 연구에서 우리는 자연수와 정수의 곱셈표에 숨겨진 대칭성들을 탐구했습니다. 이 글에서는 양의 정수와 음의 정수 분포 내의 숨겨진 대칭성을 더 깊이 탐구합니다. 또한 이러한 대칭성을 교실 환경에서 탐구할 수 있는 다양한 아이디어를 공유하여, 학생들의 적극적인 참여와 깊은 이해를 장려합니다.

https://scholarship.claremont.edu/jhm/vol15/iss1/17/