---
title: "1분 수학: 푸리에 급수"
date: 2016-11-28
---

> [!NOTE]
> https://plus.maths.org/content/maths-minute-fourier-series
>
> 열방정식이 어떻게 엔터테인먼트 산업을 뒷받침하는 수학을 탄생시켰는가

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/match_frontpage.jpg?itok=ljbCad7t)

[여기](http://www.gresham.ac.uk/series/mathematics-and-the-making-of-the-modern-and-future-world)에서 이 무료 공개 강연 시리즈에 대해 더 알아보실 수 있습니다.

수학의 한 분야가 어떤 문제를 해결하기 위해 고안되었다가 나중에 완전히 다른 수많은 문제들을 해결하게 되는 가장 아름다운 사례 중 하나가 바로 **푸리에 급수(Fourier series)**입니다. [Joseph Fourier](http://www-groups.dcs.st-and.ac.uk/~history/Biographies/Fourier.html)는 19세기 프랑스 수학자로, 열이 물체를 통해 어떻게 흐르는지에 관심을 가졌습니다. 그의 첫 번째 기여는 현재 **열방정식(heat equation)**으로 알려진 것입니다. 이것은 **편미분방정식(partial differential equation)**의 한 예로, 물체의 온도 $T$가 시간 $t$와 공간 $x$ 모두에 어떻게 의존하는지를 기술합니다. 현대적 표기법으로 열방정식은 다음과 같습니다:

$$
\frac{\partial T}{\partial t} = k \frac{\partial^{2} T}{\partial x^{2}}
$$

여기서 $k$는 물체의 **열전도도(thermal conductivity)**로, 물체가 열을 전도하는 능력을 측정하는 수입니다.

> 편미분방정식은 둘 이상의 독립변수(여기서는 시간 $t$와 위치 $x$)에 대한 미분을 포함하는 방정식입니다. 열방정식은 물리학에서 가장 중요한 편미분방정식 중 하나로, 확산 현상(diffusion)을 기술하는 기본 모델입니다. 이 방정식이 말하는 것은 직관적으로 다음과 같습니다: 어떤 지점에서 온도가 시간에 따라 변하는 속도($\partial T / \partial t$)는 그 지점 주변의 온도 분포가 얼마나 "굽어있는지"(곡률, $\partial^{2} T / \partial x^{2}$)에 비례합니다. 온도가 주변보다 높은 곳은 열을 잃고, 낮은 곳은 열을 얻어서 결국 평형 상태로 가려는 자연의 경향을 수학적으로 표현한 것입니다.

이 방정식의 해를 찾을 수 있다면, 각 지점 $x$와 시간 $t$에서의 물체 온도 $T(x,t)$를 알 수 있을 것입니다. 푸리에의 첫 번째 놀라운 통찰은 $T(x,t)$를 단순한 함수들의 합으로 표현한 다음, 이 함수들로 해를 찾을 수 있다는 것이었습니다. 이것을 생각하는 좋은 방법은, 집을 한 번에 짓는 것보다 벽돌 하나하나로 쌓아 올리는 것이 훨씬 쉽다는 것입니다. 그의 두 번째 놀라운 통찰은 온도를 구성하기 위해 어떤 함수들을 선택할 것인가에 있었습니다. 그는 삼각법(삼각형 연구)에서 나오는 [사인 함수와 코사인 함수](http://www.bbc.co.uk/education/guides/zq4w7ty/revision)를 사용하기로 선택했고, $T$를 다음과 같이 표현했습니다:

$$
T(x,t) = a_{0}(t) + \sum_{n=1}^{\infty} \left[ a_{n}(t) \cos\left(\frac{n\pi x}{L}\right) + b_{n}(t) \sin\left(\frac{n\pi x}{L}\right) \right]
$$

이것이 **푸리에 급수(Fourier series)**입니다.

> 푸리에의 핵심 아이디어는 "복잡한 함수를 단순한 파동들의 합으로 분해할 수 있다"는 것입니다. 이것은 음악에 비유하면 이해하기 쉽습니다. 오케스트라의 풍부한 소리도 결국 각 악기가 내는 단순한 음들의 합입니다. 마찬가지로, 아무리 복잡한 온도 분포도 서로 다른 주파수를 가진 사인파와 코사인파들의 합으로 표현할 수 있습니다. 여기서 $L$은 물체의 길이이고, $n$은 각 파동의 "주파수"를 결정합니다. $n=1$일 때는 물체 전체에 걸쳐 한 번 진동하는 기본파(fundamental wave), $n=2$일 때는 두 번 진동하는 제2조화파(second harmonic) 등입니다. 계수 $a_{n}(t)$와 $b_{n}(t)$는 각 주파수 성분이 얼마나 강하게 포함되어 있는지를 나타냅니다.

**계수들**

$a_{n}(t)$와 $b_{n}(t)$는 다음과 같이 정의됩니다:

$$
a_{n}(t) = A_{n}e^{-kn^{2}t}, \quad b_{n}(t) = B_{n}e^{-kn^{2}t}
$$

여기서 $A_{n}$과 $B_{n}$의 값은 초기 조건에 따라 결정됩니다.

> 이 시간 의존성이 매우 중요한 물리적 의미를 담고 있습니다. 지수함수 $e^{-kn^{2}t}$는 각 주파수 성분이 시간이 지남에 따라 어떻게 감쇠(decay)하는지를 보여줍니다. 특히 고주파 성분($n$이 큰 경우)은 $n^{2}$에 비례하여 훨씬 빠르게 사라집니다. 이것은 직관적으로도 타당합니다: 급격한 온도 변화(고주파)는 완만한 온도 변화(저주파)보다 빨리 평탄화됩니다. 뜨거운 물체를 만졌을 때 처음의 날카로운 통증이 빠르게 사라지지만, 전체적인 따뜻함은 오래 지속되는 것과 같은 이치입니다.

![Fourier](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/fourier/Fourier2.jpg)

Jean-Baptiste Joseph Fourier, 1768 - 1830.

푸리에의 위대한 발견 이후 많은 수학자들이 그의 아이디어를 확장하고 일반화하는 작업에 착수했고, 그 과정에서 많은 아름다운 결과들을 발견했습니다. 그중에는 (원래 [Leonhard Euler](http://www-groups.dcs.st-and.ac.uk/~history/Biographies/Euler.html)가 발견한) 놀라운 공식의 우아한 유도도 포함됩니다:

$$
\sum_{n=1}^{\infty} \frac{1}{n^{2}} = \frac{\pi^{2}}{6}
$$

> 이것은 수학사에서 가장 아름다운 항등식 중 하나인 바젤 문제(Basel problem)의 해입니다. 오일러가 1734년에 처음 증명했는데, 푸리에 급수를 이용하면 이 결과를 훨씬 간결하게 유도할 수 있습니다. $f(x) = x$를 구간 $[-\pi, \pi]$에서 푸리에 급수로 전개하고 파르스발 정리(Parseval's theorem)를 적용하면 이 공식이 자연스럽게 나타납니다. 이는 단순한 역수 제곱의 합이라는 대수적 대상이 원주율 $\pi$라는 기하학적 대상과 깊이 연결되어 있음을 보여줍니다. 더 일반적으로, 이런 유형의 급수들(리만 제타 함수의 특수값들)은 현대 정수론과 물리학에서 핵심적인 역할을 합니다.

푸리에 급수와 컴퓨터에서의 이산적 일반화는 현대 기술에서 근본적인 역할을 합니다. 특히 우리는 이것들을 사용하여 소리, 정보, 이미지를 만들고 처리하며, 음악, TV, 비디오 산업은 푸리에 급수 없이는 존재할 수 없습니다.

> 현대 디지털 신호 처리의 핵심은 이산 푸리에 변환(DFT, Discrete Fourier Transform)과 그것의 고속 계산 알고리즘인 고속 푸리에 변환(FFT, Fast Fourier Transform)입니다. MP3 음악 파일은 푸리에 변환을 사용하여 인간의 귀가 덜 민감한 주파수 성분을 제거함으로써 데이터를 압축합니다. JPEG 이미지 압축도 유사한 원리(이산 코사인 변환, DCT)를 사용합니다. 휴대폰 통신, 와이파이, 의료 영상(CT, MRI), 지진파 분석, 양자역학의 파동함수 분석까지, 푸리에의 아이디어는 21세기 기술 문명의 보이지 않는 기반입니다. 열의 흐름을 이해하려던 19세기 수학자의 순수한 지적 호기심이 200년 후 전 세계 사람들이 스마트폰으로 음악을 듣고 영상을 볼 수 있게 만든 것입니다.

### 더 읽고 듣기

Chris Budd가 출연한 이 [팟캐스트](https://plus.maths.org/content/podcast-11-june-2008-catching-waves)에서 푸리에 해석에 대해 더 알아보세요.

푸리에 급수에서 영감을 받은 수학의 응용에 대한 더 많은 정보는 다음을 참조하세요:

*생명 구하기: 단층촬영의 수학(Saving lives: The mathematics of tomography)*
*먹고, 마시고, 즐기기: 안전 확보하기(Eat, drink and be merry: Making sure it's safe)*
*아벨에서 아이팟까지(Abel to iPod)*
[직업 인터뷰: 오디오 소프트웨어 엔지니어](https://plus.maths.org/content/career-interview-audio-software-engineer)
[직업 인터뷰: 컴퓨터 음악 연구자](https://plus.maths.org/content/career-interview-computer-music-researcher-0)

### 이 글에 대하여

![Chris Budd](https://plus.maths.org/content/sites/plus.maths.org/files/blog/092016/budd.jpg)

Chris Budd.

이 글은 Chris Budd의 Gresham College 강연 중 하나에서 각색되었으며, *현대와 미래 세계를 만드는 수학(Mathematics and the making of the modern and future world)*이라는 시리즈의 일부입니다. 이 강연들은 런던에서 열리며, 일반 청중을 대상으로 하고 무료로 참석할 수 있습니다.

Chris Budd OBE는 University of Bath의 응용수학 교수이자, [수학 및 그 응용 연구소(Institute of Mathematics and its Applications)](http://www.ima.org.uk/)의 부회장, [Royal Institution](http://www.rigb.org/registrationControl?action=home)의 수학 의장, [Gresham 기하학 교수](http://www.gresham.ac.uk/professors-and-speakers/professor-chris-budd/), [영국 과학협회(British Science Association)](http://www.britishscienceassociation.org/)의 명예 펠로우입니다. 그는 특히 수학을 실세계에 적용하고 수학의 대중적 이해를 증진하는 데 관심이 있습니다.

그는 C. Sangwin과 함께 Oxford University Press에서 출판한 대중 수학책 *Mathematics Galore!*의 공동 저자이며, *50 Visions of Mathematics* (ed. Sam Parc)에도 등장합니다.

## 댓글

## Fred

Leonhard Euler는 이미 많은 주기 함수들이 사인과 코사인의 급수로 표현될 수 있다는 것을 발견했습니다. 그는 이미 실명한 상태에서도 계수에 대한 일반 공식까지 찾아냈습니다...

> Fred의 지적은 수학사의 중요한 측면을 강조합니다. 오일러는 1750년대에 이미 진동하는 현(vibrating string) 문제를 연구하면서 삼각함수 급수 표현을 사용했고, 현대 푸리에 계수 공식과 본질적으로 동일한 적분 공식을 유도했습니다. 그러나 푸리에의 독창성은 (1) 이 아이디어를 열방정식이라는 완전히 새로운 맥락에 체계적으로 적용했고, (2) 불연속 함수나 "임의의" 함수도 삼각급수로 표현할 수 있다고 과감하게 주장했다는 점입니다. 이 주장은 당대 수학자들에게 충격이었고, 함수 개념 자체를 재정의하게 만들었으며, 결국 리만 적분론과 집합론 같은 현대 해석학의 발전을 촉발했습니다. 오일러의 실명 후 업적들(70대에 이루어진)은 수학사의 경이로운 일화입니다. 그는 제자들에게 구술하여 놀라운 양의 논문을 생산했고, 시각 없이도 순수한 정신력으로 복잡한 계산을 수행했습니다.