---
title: 1분 수학- Lean을 이용한 코딩
date: 2025-08-12
---

> [!NOTE]
> https://plus.maths.org/content/maths-minute-coding-lean
>
> 매우 간단한 결과에 대해 증명 보조 프로그램을 사용하는 방법에 대한 안내.

![파란 배경의 코드](https://plus.maths.org/content/sites/default/files/styles/small_square/public/2025-08/Coding-CreditPeach_iStock%20%281%29.jpg?h=66899fbd&itok=HG1X1qtG)

**증명 보조 프로그램(proof assistant)**은 수학적 증명을 엄밀하게 만들어 오류가 없음을 보장하는 도구입니다. 이제 증명 보조 프로그램이 실제로 어떻게 작동하는지 살펴보겠습니다. 우리는 두 정수 $a$와 $b$에 대해 $(a+b)^{2} = a^{2} + 2ab + b^{2}$가 성립함을 증명할 것입니다. (안타깝게도 이것은 가끔 [신입생의 꿈(Freshman's dream)](https://en.wikipedia.org/wiki/Freshman%27s_dream)이라고 불리는 $a^{2}+b^{2}$와는 같지 않습니다.)

> 증명 보조 프로그램은 수학 증명의 각 단계를 형식 논리의 규칙에 따라 검증하는 소프트웨어입니다. 인간이 작성한 증명은 때로 직관에 의존하거나 "자명하다"는 표현으로 건너뛰는 부분이 있지만, 증명 보조 프로그램은 모든 단계를 명시적으로 확인합니다. 이는 특히 복잡한 증명에서 인간이 놓칠 수 있는 미묘한 오류를 잡아내는 데 유용합니다. 또한 증명의 각 단계가 어떤 공리와 정리에 의존하는지 명확히 추적할 수 있어, 수학적 지식의 의존 관계를 체계적으로 관리할 수 있습니다.

펜과 종이로 증명한다면 다음과 같을 것입니다:

$$
(a+b)^{2} = (a+b)(a+b)=a(a+b)+b(a+b)=aa+ab+ba+bb=aa+ab+ab+bb=aa+2ab+bb=a^{2}+2ab+b^{2}
$$

Isabelle, Rocq, Agda 등 다양한 증명 보조 프로그램이 있지만, 우리의 예제에서는 **Lean**이라는 증명 보조 프로그램을 사용할 것입니다.

> Lean은 Microsoft Research에서 개발한 증명 보조 프로그램으로, 종속 타입 이론(dependent type theory)을 기반으로 합니다. Lean의 특징은 상대적으로 현대적인 문법과 강력한 tactics 시스템, 그리고 활발한 수학 커뮤니티입니다. 특히 Mathlib이라는 방대한 수학 라이브러리 프로젝트가 진행 중이며, 학부 수학부터 고급 연구 수학까지 형식화되고 있습니다. Lean은 또한 교육적 목적으로도 널리 사용되는데, 이는 상대적으로 읽기 쉬운 문법과 즉각적인 피드백 시스템 덕분입니다.

Lean에서 이 기초적인 결과를 증명하기 위해, 우리는 먼저 증명에 필요한 관련 정리들을 포함하는 라이브러리를 가져옵니다(import). 우리의 경우, 관련 정리들이 Mathlib.Data.Int.Basic과 Mathlib.Algebra.Ring.Basic이라는 패키지에 있습니다. 우리가 사용할 정리들은 다음과 같습니다:

| 정리의 이름 | 의미 |
| --- | --- |
| pow_two | $x^{2} = x \times x$ |
| mul_add | $x \times (y+z)=x \times y+x \times z$ |
| add_mul | $(y+z) \times x=y \times x+z \times x$ |
| mul_comm | $x \times y=y \times x$ |
| add_assoc | $(x+y)+z=x+(y+z)$ |
| two_mul | $2 \times x=x+x$ |

이들은 모두 페아노 공리(Peano axioms)로부터 정수에 대해 유도된 매우 기본적인 결과들이며, Lean에서 완료된 모든 작업을 포함하는 GitHub 프로젝트인 Mathlib에 저장되어 있습니다.

> 페아노 공리는 자연수를 엄밀하게 정의하는 다섯 개의 공리 체계입니다. 0이 자연수이고, 모든 자연수는 후속자(successor)를 가지며, 귀납법이 성립한다는 등의 내용을 담고 있습니다. Mathlib에서는 이러한 기초 공리로부터 시작하여 덧셈, 곱셈의 성질, 그리고 더 고급 수학 개념들을 순차적으로 구축합니다. 위 표의 정리들은 우리가 학교에서 "당연하다"고 여기는 성질들이지만, 형식 증명 체계에서는 이들조차 명시적으로 증명되고 이름이 붙여진 정리로 취급됩니다. 이는 모든 수학적 추론의 근거를 추적 가능하게 만들기 위함입니다.

따라서, 우리는 다음과 같이 시작합니다:

```lean
import Mathlib.Data.Int.Basic
import Mathlib.Algebra.Ring.Basic

theorem int_square_expansion (a b : ℤ):
  (a+b)^{2} = a^{2} + 2*a*b + b^{2} := by
```

지금까지 우리가 한 일은 관련 라이브러리를 가져오고 증명하고자 하는 정리를 진술한 것뿐입니다. 이제 우리는 **재작성(rewriting)**이라는 **전술(tactic)**을 반복적으로 사용할 것입니다. 본질적으로 우리가 할 일은 가져온 정리들을 사용하여 정리의 좌변 `(a+b)^{2}`를 재작성하는 것입니다. 재작성 전술을 사용하려면 `rw[관련 정리]`라고 쓰면 됩니다. 각 코드 줄 아래에는 방정식 좌변의 현재 상태가 표시됩니다.

> Lean에서 tactics는 증명을 구성하는 작은 명령어들입니다. 각 tactic은 증명 상태(proof state)를 변환합니다. 증명 상태는 현재 증명해야 할 목표(goal)와 사용 가능한 가정(hypotheses)으로 구성됩니다. `rw` (rewrite) tactic은 등식을 사용하여 목표나 가정의 일부를 다른 형태로 바꿉니다. 예를 들어 $x^{2} = x \times x$라는 정리가 있다면, `rw [pow_two]`는 증명 상태의 모든 $x^{2}$를 $x \times x$로 치환합니다. 이는 마치 대수적 조작을 단계별로 명시적으로 수행하는 것과 같습니다.

```lean
rw [pow_two]
```
현재 상태: `(a+b)*(a+b)`

```lean
rw [mul_add]
```
현재 상태: `(a+b)*a + (a+b)*b`

```lean
rw [add_mul]
```
현재 상태: `a*a + b*a + a*b + b*b`

```lean
rw[mul_comm b a]
```
현재 상태: `a*a + a*b + a*b + b*b`

여기서 우리는 코드에서 `b`와 `a`를 바꾸도록 명시적으로 선택했는데, 이는 예를 들어 `a`와 `a`가 바뀌는 것을 방지하기 위함입니다. 그렇게 되면 별로 의미가 없을 것입니다.

> `mul_comm b a`처럼 인자를 명시하는 것은 Lean에서 매우 중요한 기법입니다. `mul_comm`은 일반적으로 $x \times y = y \times x$를 의미하지만, 증명 상태에는 여러 곱셈이 있을 수 있습니다. 만약 단순히 `rw [mul_comm]`이라고만 쓰면 Lean은 첫 번째로 발견되는 곱셈을 바꾸려 할 것입니다. 그러나 우리는 정확히 $b \times a$를 $a \times b$로 바꾸고 싶으므로, `mul_comm b a`로 명시합니다. 이는 형식 증명에서 정확성과 의도의 명시성이 얼마나 중요한지 보여줍니다.

```lean
rw[pow_two, pow_two]
```
현재 상태: `a^{2} + a*b + a*b + b^{2}`

이제 Lean이 이것을 읽는 방식이 `(((a^{2} + a*b) + a*b) + b^{2})`라는 것이 밝혀집니다. 즉, 우리는 중첩된 괄호를 가지고 있습니다. 따라서 `two_mul` 규칙을 적용하려면 다음을 사용하여 괄호를 약간 재배열해야 합니다:

> Lean을 포함한 대부분의 형식 시스템에서 연산자는 왼쪽 결합(left-associative)입니다. 즉, $a + b + c + d$는 자동으로 $(((a + b) + c) + d)$로 해석됩니다. 이것이 문제가 되는 이유는 `two_mul` 정리가 $2 \times x = x + x$ 형태이므로, 이를 적용하려면 $a \times b + a \times b$가 하나의 단위로 묶여 있어야 하기 때문입니다. 현재는 `((a^{2} + a*b) + a*b)`로 되어 있어서 직접 적용할 수 없습니다. 따라서 결합 법칙(associativity)을 사용하여 괄호를 재배열해야 합니다.

```lean
rw[add_assoc (a^{2}) (a*b) (a*b)]
```
현재 상태: `a^{2} + (a*b + a*b) + b^{2}`

다시 한번, 우리는 재작성을 적용하고 싶은 방정식의 특정 요소들을 선택했습니다.

```lean
rw[← two_mul]
```
현재 상태: `a^{2} + 2*a*b + b^{2}`

역방향 화살표(←)의 사용은 단순히 $2 \times a \times b$를 $a \times b + a \times b$로 바꾸는 것이 아니라, $a \times b + a \times b$를 $2 \times a \times b$로 바꾸고 있다는 것을 의미합니다.

> 형식 증명 시스템에서는 등식의 방향이 중요합니다. `rw [theorem]`은 정리를 왼쪽에서 오른쪽으로 적용하지만, `rw [← theorem]`은 오른쪽에서 왼쪽으로 적용합니다. 예를 들어 `two_mul`은 원래 $2 \times x = x + x$를 의미하므로, `rw [two_mul]`은 $2 \times x$를 $x + x$로 바꿉니다. 그러나 우리는 반대로 $x + x$를 $2 \times x$로 바꾸고 싶으므로 역방향 화살표를 사용합니다. 이러한 양방향 적용 가능성은 등식의 대칭성을 반영하며, 증명 작성의 유연성을 높여줍니다.

```lean
rfl
```

마지막으로, 우리는 `rfl`(reflexive의 줄임말)을 작성하여 코드를 마무리합니다. 이는 단순히 '이제 좌변이 우변과 같으므로, 증명이 완료되었다'는 것을 의미합니다.

> `rfl`은 반사성(reflexivity) tactic으로, $x = x$라는 자명한 사실을 사용합니다. Lean이 증명 상태를 확인했을 때 좌변과 우변이 정확히 같은 형태라면, `rfl` 하나로 증명이 완료됩니다. 이는 우리의 모든 재작성 단계가 성공적으로 좌변을 목표 형태로 변환했음을 의미합니다. 형식 증명 시스템의 미학 중 하나는 이렇게 복잡한 변환 과정 끝에 `rfl` 하나로 간결하게 마무리된다는 점입니다. 이는 모든 수학적 조작이 궁극적으로는 동일성(identity)의 인식에 도달한다는 철학적 통찰을 담고 있습니다.

Lean 코딩을 이해하기 어려울 수 있습니다. 제가 이해하려고 노력했을 때 가장 좋았던 자료는 [Kevin Buzzard](https://xenaproject.wordpress.com/)가 만든 [자연수 게임(Natural Number Game)](https://adam.math.hhu.de/)이었습니다. 여러분도 직접 시도해볼 수 있습니다. 첫 번째 세계(world)에서는 Lean에서 2+2=4를 엄밀하게 증명하는 방법을 보여줍니다.

> 자연수 게임은 게임화된 형태로 Lean을 배울 수 있는 인터랙티브 튜토리얼입니다. 플레이어는 각 레벨에서 점점 더 복잡한 정리들을 증명하면서 Lean의 문법과 tactics를 자연스럽게 익히게 됩니다. 첫 세계에서는 덧셈의 기본 성질들을, 이후 세계에서는 곱셈, 거듭제곱, 부등식 등을 다룹니다. 이 프로젝트는 형식 수학을 대중화하는 데 크게 기여했으며, 많은 수학자와 학생들이 증명 보조 프로그램에 입문하는 관문이 되었습니다. 특히 즉각적인 피드백 시스템 덕분에 자신의 증명이 어디서 막혔는지, 어떤 정리를 사용해야 하는지 실시간으로 배울 수 있습니다.

### 저자 소개:

Ben Watkins는 2025년에 케임브리지 대학교에서 수학 4학년 과정을 마쳤습니다. 그의 관심사는 이론 물리학, 양자 계산, 그리고 수학적 소통, 즉 더 넓은 청중과 수학의 즐거움을 공유하는 것을 포함합니다!

![](https://plus.maths.org/content/sites/default/files/styles/large/public/2025-08/image.png?itok=-_yGjYwa)

*이 콘텐츠는 **아이작 뉴턴 수리과학 연구소(Isaac Newton Institute for Mathematical Sciences, INI)**와의 협업의 일부입니다. 협업에서 나온 모든 콘텐츠는 **여기**에서 찾을 수 있습니다.*

*INI는 국제 연구 센터이자 케임브리지 대학교 수학 캠퍼스에 있는 우리의 이웃입니다. 전 세계의 저명한 수리과학자들을 끌어들이며, 모두에게 개방되어 있습니다. 자세한 내용은 **www.newton.ac.uk**를 방문하세요.*

![INI 로고](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/representation/ini_logo_green.jpg)