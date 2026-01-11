---
title: 프랙탈의 기원
date: 1998-09-01
tags:
  - 함수
  - Hilbert
  - 곡선
  - Weierstrass
  - Benoit
  - Fractal
  - Karl
  - 프랙탈
---

> [!NOTE]
> https://plus.maths.org/content/origins-fractals
>
> 1970년대 중반 Benoit Mandelbrot가 도입한 프랙탈(fractal)이라는 용어는 이제 미분 불가능하며 무한한 길이를 가진 이 함수군을 묘사하는 데 일반적으로 사용된다. 이들의 기원과 역사에 대해 알아보자.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/issue6/turner1/icon.jpg?itok=JAJIw-uV)

### Karl Weierstrass

세기의 전환기에 일부 수학자 집단들 사이에서 적대감이 증가하고 있었다. 이러한 반목의 원인은 특정 해석학자들이 다른 해석학자들이 함수가 *당연히 가져야 한다*고 생각했던 속성들을 함수가 반드시 가질 필요는 없다는 것을 보여주었기 때문이었다. Karl Weierstrass와 같은 수학자들은 수학계의 많은 이들을 충격에 빠뜨릴 만큼 기괴한 새로운 함수들을 발명하고 있었다. 특히 Hermite와 그의 제자 Poincaré는 Weierstrass의 새로운 창조물을 "개탄스러운 악(deplorable evil)"이라고 묘사했다!

> 19세기 후반 수학계는 함수의 본질에 대한 근본적인 인식의 변화를 겪고 있었다. 그 이전까지 수학자들은 함수를 물리적 현상을 기술하는 "자연스러운" 대상으로 여겼고, 따라서 모든 함수는 미분 가능하고 부드러운 곡선이어야 한다고 믿었다. 그러나 Weierstrass는 이러한 직관에 정면으로 도전하는 함수를 구성함으로써, 수학적 대상이 우리의 물리적 직관을 초월할 수 있음을 보여주었다. 이는 단순한 호기심의 대상이 아니라 수학의 논리적 기초를 재정립하는 혁명적 사건이었다. Hermite와 Poincaré의 격렬한 반응은 이것이 단지 새로운 함수의 발견이 아니라 수학의 본질에 대한 패러다임 전환이었음을 보여준다.

도입부로서, 우선 함수 $F(x) = |x|$를 살펴보자. 이 함수는 $x > 0$일 때 $F(x) = x$이고, 그렇지 않으면 $F(x) = -x$인 속성을 가진다.

이제 아래 그래프에서 보이는 것처럼 $x = 0$에서 무슨 일이 일어나는지 살펴보자:

![](https://plus.maths.org/issue6/turner1/f.gif)

$F(x)$는 *연속(continuous)*이다. 이는 곡선에 틈이 없다는 의미이다. 우리는 모든 연속 함수를 펜을 종이에서 떼지 않고 그릴 수 있는 함수로 생각할 수 있다. 위치 $F(0)$에는 곡선에 "꺾임"이 있는 것처럼 보이며, 이것은 아무리 가까이 확대해도 매끄럽게 보이지 않는다. 이것은 곡선의 기울기(또는 *경사(gradient)*)의 *불연속(discontinuity)*이며, 기울기가 갑자기 한 각도에서 다른 각도로 변한다. 이 위치에서 곡선은 *미분 불가능(not differentiable)*한데, 기울기를 계산할 방법이 없기 때문이다. 점 $x$에서 미분 가능하다는 것은 일반적으로 그 점에서 매끄럽게 보인다는 것으로 정의된다.

> 미분 가능성(differentiability)은 함수의 국소적 선형성을 의미한다. 어떤 점에서 미분 가능하다는 것은 그 점 근처에서 함수를 직선으로 충분히 잘 근사할 수 있다는 뜻이다. 절댓값 함수 $|x|$의 경우, $x = 0$ 근처에서 왼쪽에서는 기울기가 $-1$이고 오른쪽에서는 $+1$이므로, 어떤 단일한 직선으로도 이 점 근처의 함수를 근사할 수 없다. 이것이 바로 원점에서 미분 불가능한 이유이다. 19세기 이전에는 이런 "모서리"를 가진 함수들도 예외적인 경우로만 여겨졌고, "진짜" 함수들은 모두 매끄럽다고 생각했다.

19세기 후반에는 모든 연속 함수가 적어도 한 지점에서는 미분 가능(매끄러운) 해야 한다고 믿어졌다. Karl Weierstrass는 어디에서도 미분 불가능하지만 여전히 연속인 함수를 만들어냄으로써 이를 뒤집었다. 이것은 곡선의 기울기를 결코 찾을 수 없다는 것을 의미한다. 여기에 제시된 Weierstrass 함수의 한 버전은 코사인 곡선의 무한 급수를 기반으로 하며, 일반적인 경우는 다음과 같다:

$$
C(x) = \sum_{n=0}^{\infty} b^{n} \cos(a^{n}x)
$$

여기서 $a$는 홀수 정수이고, $0 < b < 1$이며, $ab > 1 + \frac{3\pi}{2}$를 만족한다.

![x에 대한 C(x)의 그래프, 여기서 a=8, b=0.9인 경우](https://plus.maths.org/issue6/turner1/cgraph.gif)

$x$에 대한 $C(x)$의 그래프, 여기서 $a = 8$, $b = 0.9$인 경우

> Weierstrass 함수의 핵심 아이디어는 점점 더 빠르게 진동하는 코사인 함수들을 겹쳐 쌓는 것이다. 각 항 $b^{n}\cos(a^{n}x)$에서 $n$이 증가하면 진폭은 $b^{n}$으로 감소하지만 진동수는 $a^{n}$으로 증가한다. 조건 $ab > 1 + \frac{3\pi}{2}$는 진동수의 증가 속도가 진폭의 감소 속도를 충분히 빠르게 압도하여, 작은 스케일에서도 항상 "거칠기"가 남아있도록 보장한다. 이것이 모든 점에서 미분 불가능한 이유이다. 아무리 확대해도 함수는 여전히 울퉁불퉁하게 보인다. 이는 자기유사성(self-similarity)의 초기 형태로, 나중에 프랙탈의 핵심 특성이 된다.

다음 순서는 증가하는 수의 코사인 항들이 더해질 때 곡선이 어떻게 변하는지 보여준다:

![첫 번째 항 n=1](https://plus.maths.org/issue6/turner1/n1.gif)

첫 번째 항 $n = 1$

![처음 두 항 n=1과 n=2의 합](https://plus.maths.org/issue6/turner1/n12.gif)

처음 두 항 $n = 1$과 $n = 2$의 합

![처음 세 항 n=1, n=2, n=3의 합](https://plus.maths.org/issue6/turner1/n123.gif)

처음 세 항 $n = 1$, $n = 2$, $n = 3$의 합

![처음 네 항 n=1, n=2, n=3, n=4의 합](https://plus.maths.org/issue6/turner1/n1234.gif)

처음 네 항 $n = 1$, $n = 2$, $n = 3$, $n = 4$의 합

당시에는 이러한 함수들에 대한 구상된 용도가 없었고, 많은 수학자들은 미분 가능성을 상수로서 잃는 것에 경악했다. Hermite는 이 새로운 함수들을 "무서운 재앙(dreadful plague)"이라고 묘사했고, Poincaré는 다음과 같이 썼다:

"과거에는 새로운 함수가 발명되면 그것은 어떤 실용적 목적을 위한 것이었다. 오늘날 그것들은 오직 우리 선배들의 주장을 반박하기 위해 특별히 발명되며, 결코 다른 용도를 가지지 않을 것이다."

> Poincaré의 이 비판은 아이러니하게도 완전히 틀렸다. 오늘날 Weierstrass형 함수들은 브라운 운동(Brownian motion), 난류(turbulence), 금융 시장의 가격 변동, 해안선의 형태 등 자연 현상을 모델링하는 데 필수적이다. 이들 현상은 모두 모든 스케일에서 불규칙성을 보이는 공통점을 가진다. Poincaré가 "실용적 목적"이 없다고 비난했던 바로 그 속성-모든 점에서의 미분 불가능성-이 실제로는 자연의 복잡성을 포착하는 핵심 도구가 되었다. 이는 순수 수학적 탐구가 예상치 못한 응용으로 이어지는 대표적 사례이다.

### David Hilbert

이러한 발언에도 불구하고 많은 수학자들은 이러한 "병리학적 괴물(pathological monster)" 함수들을 계속 만들어냈고, 가장 유명하고 널리 사용되는 함수 중 하나는 David Hilbert에 의해 만들어졌다. Hilbert는 세기의 전환기에 매우 존경받는 수학자였지만, Gordan과 같은 그의 동시대인들은 종종 Hilbert의 문제 해결에 대한 혁명적 접근을 제대로 인정하지 못했다. 이는 특히 Hilbert가 *Mathematische Annalen*에 제출한 유한 기저 정리(finite basis theorem) 증명의 경우에 해당하는데, 이 정리는 Gordan이 20년 전에 훨씬 더 계산적인 접근을 사용하여 증명한 것이었다. 오늘날 Hilbert는 특히 그의 유명한 23개의 파리 문제들(여기에는 Goldbach의 추측이 포함되어 있다 - Issue No 2의 "[Mathematical mysteries: the Goldbach conjecture](https://plus.maths.org/issue2/xfile/index.html)" 참조)과 양자 이론의 필수 도구인 Hilbert 공간 개념을 통해 기억되고 있다.

> Hilbert의 유한 기저 정리 증명은 수학사에서 중요한 전환점을 나타낸다. Gordan의 증명은 구성적(constructive)이었다-실제로 기저를 찾는 알고리즘을 제공했다. 반면 Hilbert의 증명은 비구성적(non-constructive)이었다-기저가 존재한다는 것을 증명했지만 실제로 찾는 방법은 제시하지 않았다. Gordan은 유명하게 "이것은 신학이지 수학이 아니다"라고 반응했다. 그러나 Hilbert의 접근은 더 강력하고 일반적이었으며, 현대 수학의 존재 증명(existence proof) 패러다임을 확립했다. 이는 "어떻게 만드는가"보다 "존재하는가"가 더 근본적 질문이라는 인식의 변화를 나타낸다.

"병리학적 괴물" 함수들에 대한 Hilbert의 특별한 기여는 연속적일 뿐만 아니라 *전사적(surjective)*이기도 한, 공간을 채우는 곡선(space filling curve)이라는 속성을 가진다.

### 공간 채우는 곡선 (Space Filling Curves)

Hilbert 공간 채우는 곡선은 *스테이플(호치키스 침)*처럼 보이는 초기 형태에서 시작하여 만들어진다. 이 형태는 정사각형 영역을 채우기 위해 연결선이 삽입된 채로 네 번 복사되고 회전된다. 그것의 단순함과 아름다움은 정사각형 배열을 점진적으로 무한한 하위 정사각형 배열로 세분화한다는 사실에서 비롯된다. 최종 곡선은 복사 과정을 무한히 많이 반복함으로써 만들어진다. 처음 몇 단계는 아래에 나와 있다.

![](https://plus.maths.org/issue6/turner1/hilb1.gif) | ![](https://plus.maths.org/issue6/turner1/hilb2.gif)
![](https://plus.maths.org/issue6/turner1/hilb3.gif) | ![](https://plus.maths.org/issue6/turner1/hilb4.gif)

이 곡선은 1차원이지만 2차원 공간을 완전히 채우는 속성을 가진다. 우리가 정의할 대응하는 함수 $H$는 단일 실수 $x$를 받아서 실수 쌍 $(u, v)$를 반환하며, $H(x) = (u, v)$로 쓴다. 이것은 곡선에 대한 *매개변수 표현(parametric representation)*이라고 한다. 이것은 다음과 같은 속성들을 가진다:

- $H(x)$는 *일대일 대응(one-to-one mapping)*(또는 *단사(injective)*라고도 함)이므로, $H(x) = H(y)$이면 $x = y$이다. 이것은 선이 자기 자신과 겹치지 않는다는 것을 의미한다.
- $H(x)$는 *전사(onto)*(또는 *전사적(surjective)*이라고도 함)이므로, 정사각형 내의 모든 2차원 점 $(u, v)$는 어떤 $x$에 대해 $H(x)$로 표현될 수 있다. 이것은 선이 정사각형 내의 모든 가능한 점을 덮는다는 것을 의미한다.
- $H(x)$는 *연속* 함수이다. 이것은 선에 틈이 없다는 것을 의미한다.

> Hilbert 곡선의 구성은 놀라운 역설을 보여준다. 직관적으로 1차원 선은 2차원 평면을 "채울" 수 없어야 한다-차원이 다르기 때문이다. 그러나 무한 과정을 통해 이것이 가능해진다. 각 단계에서 곡선은 정사각형의 더 많은 부분을 방문하며, 극한에서는 모든 점을 방문한다. 이는 "차원"의 개념이 위상학적 관점(경로 연결성)과 측도론적 관점(공간 채우기) 사이에서 미묘한 차이를 가진다는 것을 보여준다. Hilbert 곡선은 위상학적으로는 1차원이지만(각 점이 국소적으로 선분처럼 보임), 측도론적으로는 2차원 영역을 "커버"한다.

$H$가 단사이므로, 우리는 *역 대응(inverse mapping)* $H^{-1}$을 찾을 수 있다. 그러한 역 대응은 정사각형 위의 점 $(u, v)$를 선 위의 값 $H(x)$로 변환할 것이다. 그러나 이 역 대응은 연속적이지 *않다*. 정사각형 위의 두 이웃 점, 예를 들어 $H(x)$와 $H(y)$는 곡선 위의 두 점 $x$와 $y$로 대응되지만, 이 점들은 서로 거의 임의의 거리만큼 떨어져 있을 수 있다. 우리의 원래 함수 $H$는 연속적이었으므로, 이것은 모든 연속 함수가 연속적인 역함수를 가지는 것은 아니라는 중요한 사실을 보여준다.

> 이 관찰은 위상수학에서 근본적으로 중요하다. 연속 함수의 역함수가 연속적이지 않을 수 있다는 사실은, 연속성이 쌍방향 속성이 아님을 의미한다. Hilbert 곡선의 경우, 선 위에서 가까운 두 점은 평면에서도 가까울 수 있지만(연속성), 평면에서 가까운 두 점이 선 위에서도 가까운 것은 아니다(역함수의 불연속성). 이는 곡선이 공간을 채우기 위해 끊임없이 "접히고" "되돌아가야" 하기 때문이다. 이 현상은 위상적 동형사상(homeomorphism)과 단순 연속 전단사(continuous bijection)의 차이를 명확히 보여준다. 위상적 동형사상이 되려면 함수와 그 역함수가 모두 연속이어야 하는데, Hilbert 곡선은 이 조건을 만족하지 않는다.

### 프랙탈 (Fractals)

미분 불가능하고 무한한 길이를 가진 이 함수군을 정의하는 데 현재 일반적으로 사용되는 *프랙탈(fractal)*이라는 용어는 1970년대 중반 Benoit Mandelbrot에 의해 도입되었다. 프랙탈이라는 용어는 라틴어 형용사 FRACTUS에서 파생되었으며, 이에 대응하는 동사 FRANGERE는 "부수다"를 의미한다. 이는 이러한 곡선들의 모습을 잘 묘사하는 설명이다.

> Mandelbrot의 천재성은 19세기의 "병리학적 괴물"들이 실제로는 자연 현상의 핵심을 포착한다는 것을 인식한 데 있다. 그는 해안선, 산맥, 구름, 나무 등 자연의 많은 구조들이 프랙탈 기하학을 따른다는 것을 보여주었다. 프랙탈의 핵심 특성은 **자기유사성(self-similarity)**-구조가 다른 스케일에서 비슷하게 반복된다-과 **비정수 차원(non-integer dimension)**이다. 예를 들어, 해안선은 1차원 선도 2차원 평면도 아닌 약 1.25차원을 가진다. 이것은 유클리드 기하학으로는 포착할 수 없는 자연의 "거칠기(roughness)"를 수학적으로 정량화하는 방법이다. Weierstrass와 Hilbert가 만든 "괴물"들은 이제 현실 세계를 모델링하는 강력한 도구가 되었다.

프랙탈에 대해 더 알아보려면, 이번 Issue의 다른 곳에 있는 "[Modelling nature with fractals](https://plus.maths.org/content/os/issue6/turner2/index)"를 참조하라.

### 더 읽어볼 자료

프랙탈의 수학은 몇몇 재미있는 웹사이트에서 논의되고 있다:

그리고 다음을 포함한 많은 책들에서:

- Fractals Everywhere, second edition, by Michael F Barnsley revised with the assistance of Hawley Rising III. Boston; London: Academic Press Professional, c1993
- Computers, Pattern, Chaos and Beauty: graphics from an unseen world by Clifford A Pickover. Stroud: Sutton 1990
- The Fractal Geometry of Nature by Benoit B Mandelbrot. San Francisco: W H Freeman, c1982

이 글의 일부 이미지와 텍스트는 다음 책에서 가져온 것이다:

- Fractal Geometry in Digital Imaging by Martin J Turner, Jonathan M Blackledge and Patrick R Andrews

[MacTutor history of mathematics archive](http://www-groups.dcs.st-and.ac.uk/~history/):

[Charles Hermite](http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Hermite.html)
[David Hilbert](http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Hilbert.html)
[Benoit B Mandelbrot](http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Mandelbrot.html)
[J Henri Poincaré](http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Poincare.html)
[Karl T W Weierstrass](http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Weierstrass.html)
[Paul Albert Gordan](http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Gordan.html)

### 저자

*Dr Martin J Turner*, Imaging Research Centre, SERC, De Montfort University, Leicester LE1 9BH

## 댓글

## Sean Siegel

Turner 박사님께,

저는 워싱턴 D.C. 외곽에서 온 학부생입니다. 프랙탈에 대한 박사님의 놀라운 작업에 감사드리고 싶습니다. 저는 스스로를 수학에 매우 능숙하다고 생각하지는 않지만, 이것은 제가 매우 이해하고 삶의 여러 측면에 적용하고 싶은 개념입니다. 저는 지난 몇 달 동안 무한에 대해 공부해 왔으며, 프랙탈의 수학이 우리가 그것을 이해하는 데 결정적이라고 믿습니다. 저는 이 주제에 대해 가능한 한 모든 것을 배우고 싶습니다.