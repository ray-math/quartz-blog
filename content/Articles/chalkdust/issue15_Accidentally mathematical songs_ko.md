---
title: 우연히 수학적인 노래들
date: 2022-05-25
---

> [!NOTE]
> https://chalkdustmagazine.com/features/accidentally-mathematical-songs/
>
> Goran Newsum always should be someone you really love

## Blur의 Girls & Boys

![](https://i0.wp.com/chalkdustmagazine.com/wp-content/uploads/2022/05/blur-alt.png?resize=300%2C300&ssl=1)

브릿팝 밴드 Blur의 *Girls & Boys* 후렴구는 다음과 같다:

Girls who are boys

Who like boys to be girls

Who do boys like they're girls

Who do girls like they're boys.

Always should be someone you really love.

Girls who are boys

Who like boys to be girls

Who do boys like they're girls

Who do girls like they're boys.

Always should be someone you really love.

투에-모스 수열(Thue–Morse sequence)은 이진수 문자열로 표현된다. 이 수열을 확장하는 방법은 현재 문자열의 불 보수(Boolean complement, 각 위치의 반대값을 취함)를 구하여 문자열 끝에 추가하는 것이다. 0에서 시작하여 불 보수인 1을 추가하면 문자열 01을 얻는다. 이제 01이 있고, 불 보수인 10을 추가하면 0110을 얻는다. 이를 몇 번 반복하면 수열 0110100110010110…을 얻는다.

> 투에-모스 수열은 노르웨이 수학자 Axel Thue(1906)와 미국 수학자 Marston Morse(1921)가 독립적으로 발견한 수열이다. 이 수열의 핵심 성질은 '중첩 없음(overlap-free)'이다. 여기서 중첩이란 어떤 문자열 패턴이 자기 자신과 겹치면서 반복되는 것을 의미한다. 예를 들어 "ababa"에서 "aba"는 중첩되어 나타난다. 투에-모스 수열은 이런 중첩이 전혀 없는 놀라운 구조를 가진다. 이 수열은 조합론, 컴퓨터 과학, 프랙탈 이론 등 다양한 분야에서 나타나며, 특히 반복 패턴을 피하는 문자열 구성 문제에서 중요한 역할을 한다.

실제로 투에-모스 수열에서 임의의 0과 1로 이루어진 문자열을 가져오면, 그 문자열이 끝날 때까지 다시 나타나지 않는다. 예를 들어, 시작 부분 근처에 나타나는 문자열 1101을 생각해보자. 이 문자열이 다음으로 나타나는 위치는 14번째이며, 원래 문자열과 겹치지 않는다:

**1101**00110010

**1101**00101100…

이를 손을 흔들며(hand-wavy) 증명하자면*, 투에-모스 수열이 어떤 중첩을 포함하는 문자열 $A$가 나타날 때까지 중첩이 없다고 가정하자(예를 들어, $A$는 중첩되는 101들을 포함하므로 10101일 수 있다). 그러나 수열의 성질상, $A$의 불 보수(우리 예에서는 01010)가 이미 수열에 나타났어야 하며, 이는 더 이른 중첩이 있었음을 의미한다. 이것은 모순이므로, 투에-모스 수열은 반드시 중첩이 없어야 한다. 증명 끝.

> 이 증명은 "손을 흔드는" 증명, 즉 엄밀하지 않지만 직관적으로 설득력 있는 논증이다. 엄밀한 증명은 귀납법을 사용한다. 핵심 아이디어는 다음과 같다: 만약 어떤 단계에서 중첩이 발생한다면, 그것은 새로 추가된 부분(불 보수)에서 발생해야 한다. 그런데 불 보수 부분의 중첩은 원래 부분의 중첩에 대응되므로, 원래 부분에 이미 중첩이 있었어야 한다. 이것은 귀납 가정에 모순이다. 이런 재귀적 구조를 통해 중첩이 절대 생기지 않음을 보일 수 있다. 이 성질은 투에-모스 수열이 가장 단순한 무한 중첩 없는 수열임을 보여준다.

0과 1을 G와 B로 바꾸면, 투에-모스 수열의 시작이 Girls & Boys 수열과 같다는 것을 알 수 있다. 따라서 후렴구를 다음과 같이 확장할 수 있다:

Girls who are boys

Who like boys to be girls

Who do boys like they're girls

Who do girls like they're boys

Who need boys like they're girls

Who need girls like they're boys

Who have girls who are boys

Who have boys who are girls

Who choose boys who see girls

Who choose girls who see boys

Who meet girls who like boys

Who meet boys who like girls

Who verb girls who verb boys

Who verb boys who verb girls

…

Always should be someone you really love.

Girls who are boys

Who like boys to be girls

Who do boys like they're girls

Who do girls like they're boys

Who need boys like they're girls

Who need girls like they're boys

Who have girls who are boys

Who have boys who are girls

Who choose boys who see girls

Who choose girls who see boys

Who meet girls who like boys

Who meet boys who like girls

Who verb girls who verb boys

Who verb boys who verb girls

…

Always should be someone you really love.

> 이 확장이 가능한 이유는 투에-모스 수열의 재귀적 구조 때문이다. 각 단계에서 이전 패턴을 복제하고 반전시키므로, 가사도 G(Girls)와 B(Boys)의 패턴을 따라 무한히 확장될 수 있다. 흥미롭게도, 이렇게 확장된 가사는 어떤 젠더 정체성의 조합도 자기 자신과 "겹치지" 않고 나타난다. 이는 원곡이 의도했든 아니든, 젠더 유동성과 다양성을 수학적으로 표현한 셈이다. 투에-모스 수열이 음악에서도 실제로 사용되는데, 특히 현대 음악 작곡가들이 반복을 피하면서도 구조적인 멜로디를 만들 때 활용한다.

## Faith No More의 Falling to Pieces

![](https://i0.wp.com/chalkdustmagazine.com/wp-content/uploads/2022/05/faith-no-more.png?resize=295%2C300&ssl=1)

1990년, 미국 록 밴드 Faith No More는 앨범 *The Real Thing*에서 싱글 *Falling to Pieces*를 발매했다. 노래 안에는 다음과 같은 구절이 있다:

From the bottom, it looks like a steep incline,

From the top, another downhill slope of mine,

But I know, the equilibrium's there.

From the bottom, it looks like a steep incline,

From the top, another downhill slope of mine,

But I know, the equilibrium's there.

중간값 정리(intermediate value theorem)는 다음과 같이 말한다: '만약 $f$가 정의역에 구간 $[a,b]$를 포함하는 연속함수라면, $f(a)$와 $f(b)$ 사이의 임의의 값을 그 구간 내의 어떤 점에서 취한다.' 이 정리의 따름정리(corollary)는, 같은 조건에서 $f(c) = (f(a) + f(b))/2$를 만족하는 $c \in [a, b]$가 반드시 존재한다는 것이다.

> 중간값 정리는 직관적으로는 당연해 보이지만, 실수의 완비성(completeness)이라는 깊은 성질에 기반한다. 이 정리가 말하는 것은 연속함수의 그래프가 "점프"하지 않고 이어진다는 것이다. 예를 들어, 산을 오를 때 해발 100m에서 출발해 해발 500m에 도착한다면, 반드시 해발 300m 지점을 지나가야 한다. 여기서 언급된 따름정리는 더 구체적으로, 시작점과 끝점의 평균 높이에 해당하는 지점이 반드시 존재한다고 말한다. 이는 $f(a)$와 $f(b)$의 중간값인 $(f(a) + f(b))/2$를 중간값 정리에 적용한 것이다. 이 정리는 방정식의 근의 존재성을 증명하는 데 자주 사용되며, 수치해석에서 이분법(bisection method)의 이론적 근거가 된다.

![](https://i0.wp.com/chalkdustmagazine.com/wp-content/uploads/2022/05/graph.png?resize=654%2C313&ssl=1)

그런데 이것이 노래와 어떤 관련이 있을까? '바닥(the bottom)'을 $x = a$ 지점으로, '꼭대기(the top)'를 $x = b$ 지점으로 취하면, 그 사이에 함수를 정의할 수 있다. 앞서 언급했듯이, 중간값 정리를 사용하려면 함수가 연속이어야 한다. 경사면이므로, 표면이 거의 끊어지지 않는다고 말하는 것이 공정하다고 생각한다. 언덕을 올라가다가 갑자기 중간에 바닥에 거대한 틈이 있는 경우는 없다!

> 여기서 "연속성"이라는 수학적 조건이 물리적 현실과 연결된다. 언덕의 경사면은 실제로 연속적이다. 만약 불연속점이 있다면, 그것은 절벽이나 틈이 될 것이다. 일반적인 언덕이나 산의 경우, 이런 극단적인 불연속은 없고, 경사가 급하거나 완만할 수는 있어도 표면은 이어져 있다. 수학적으로 말하면, 고도 함수 $h(x)$는 수평 위치 $x$에 대해 연속함수가 된다. 이런 연속성 가정이 있어야만 중간값 정리를 적용할 수 있다.

중간값 정리의 따름정리는 수직 단면의 정확히 중간 지점이 반드시 존재한다고 말해준다. 다시 말해, '평형(the equilibrium)'이 거기 있다. 정확히 Faith No More의 추측이 말한 그대로다.

> 이 가사가 수학적으로 정확한 이유를 더 자세히 살펴보자. 바닥에서 보면 가파른 오르막(steep incline)이고, 꼭대기에서 보면 내리막 경사(downhill slope)다. 이는 관점의 차이를 표현하지만, 수학적으로는 $f(a) < f(c) < f(b)$라는 관계를 나타낸다. "equilibrium"이라는 단어는 물리학에서 힘의 균형을 의미하지만, 여기서는 기하학적으로 높이의 중간점을 의미한다. 중간값 정리의 따름정리는 이 중간점 $c$가 단순히 존재할 가능성이 있는 것이 아니라, 반드시 존재함을 보장한다. 이것이 "I know, the equilibrium's there"라는 확신 있는 가사와 완벽하게 일치한다. 수학적 필연성과 가사의 확신이 하나로 만난 순간이다.