---
title: 세상을 바꾼 방정식 5 -  허수 i
date: 2023-10-30
tags:
  - 대수학
  - 방정식
  - 근
  - 음수
  - 복소수
  - 해
  - 제곱근
  - 이용
  - 차
  - 곱
---
## 이차 방정식의 해법
오늘날 우리가 외우는 근의 공식은 언제부터 있던 것일까요? 

$$
x = \frac{{-b \pm \sqrt{{b^2-4ac}}}}{{2a}}
$$

YBC 6967라는 이름이 붙은 이 점토판은 기원 전 1900년경에 만들어진 것으로 추정됩니다. 이 점토판은 상호 역수인 'igi'와 'igi.bi'에 대한 문제와 그 해결책을 담고 있습니다. 바빌로니아인들은 60진법을 사용했기 때문에, 이 문제에서 'igi'와 'igi.bi'의 곱은 60이며, 두 수의 차이는 7을 의미하죠.[^1]

![YBC 6967 점토판 앞면](https://www.ams.org/images/fcarc-nov2020-YBC6967-obv.png)
![YBC 6967 점토판 뒷면](https://www.ams.org/images/fcarc-nov2020-YBC6967-rev.png)

> [A reciprocal] exceeds its reciprocal by 7. What are [the reciprocal] and its reciprocal? You: break in half the 7 by which the reciprocal exceeds its reciprocal, and 3;30 (will come up). Multiply 3;30 by 3;30 and 12;15 (will come up). Append [1 00, the area,] to the 12;15 which came up for you and 1 12;15 (will come up). What is [the square-side of 1] 12;15? 8;30. Put down [8;30 and] 8;30, its equivalent, and subtract 3;30, the takiltum-square, from one (of them); append (3;30) to one (of them). One is 12, the other is 5. The reciprocal is 12, its reciprocal 5
>
>이 문제는 상호 역수가 7만큼 차이가 난다고 설명하고 있습니다. 그렇다면 이 상호 역수는 무엇일까요? 먼저, 상호 역수가 7만큼 차이나는 것을 반으로 나누면 3.5가 됩니다. 이 3.5를 제곱하면 12.25가 나옵니다. 이 값에 원래의 면적 60을 더하면 72.25가 됩니다. 이 값의 제곱근은 8.5입니다. 이제 8.5에서 3.5를 빼고, 다시 8.5에 3.5를 더하면 두 상호 역수를 찾을 수 있습니다. 하나는 12이고, 다른 하나는 5입니다. 따라서 상호 역수는 12와 5입니다.

현대적인 표기법으로 YBC 6967 문제는 $xy = 60, x-y = 7$을 의미합니다. 다른 말로 $x^2-7x-60=0$이죠. 서판에는 그림이 하나도 그려져 있지 않지만 내용을 들여다 보면 제곱을 완성하기 위해 더해야 할 항이 $\frac{b^2}{4a^2}=\frac{49}{4}=12 \frac{1}{4}$로, 그림에서의 작은 정사각형의 면적과 정확히 일치하는 것을 볼 수 있습니다. 바빌로니아 서기관들은 이러한 기하학적인 방식으로 $2$차 방정식을 해결했으며, 이는 오늘날 우리가 외우는 근의 공식과 같은 내용입니다.[^2]

$$
\begin{align*}
x^2 + px = q\\
x = \sqrt{q + \frac{p^2}{4}} - \frac{p}{2}
\end{align*}
$$

바빌로니아의 수학자들은 매우 발전된 수학적 기술을 가지고 있었지만, 이 시기에는 $0$이라는 개념이 없었기 때문에, 음수나 $0$을 포함한 복잡한 계산을 수행할 수 없었습니다. 음수의 개념은 7세기에 인도의 수학자 브라마굽타(Brahmagupta)에 의해 처음으로 규칙이 정립되었죠. 유럽에서 음수의 문제는 19세기에 드 모르간(De Morgan)과 피콕(Peacock) 등의 수학자들이 논리적 정의를 통해 '산술의 법칙'을 조사할 때까지 완전히 해결되지 않았습니다.[^3] 결과적으로 이러한 근의 공식에서 근은 길이나 양을 나타낼 수 있는 양수에서 밖에 정의되지 않았습니다.

## 삼차 방정식의 해법
16세기 초, 볼로냐 대학의 교수였던 Scipione del Ferro는 흔히 depressed cubic이라 불리는 이차항이 없는 삼차 방정식$x^3 + ax +b = 0$의 한 해를 찾는 방법을 알고있었습니다. 

$$
x = \sqrt[3]{-\frac{b}{2} + \sqrt{\frac{b^2}{4} + \frac{a^3}{27}}} + \sqrt[3]{-\frac{b}{2} - \sqrt{\frac{b^2}{4} + \frac{a^3}{27}}}
$$

삼차 방정식의 한 해를 찾는다면 삼차 방정식은 일차 방정식과 이차방정식으로 인수분해되므로 결과적으로 삼차 방정식의 모든 근을 찾을 수 있게 된거죠. 훗날 타르탈리아(Tartaglia)와 카르다노(Cardano)는 일반적인 삼차방정식 $ax^3 + bx^2 + cx + d = 0$에 $x = t - \frac{b}{3a}$를 대입하여 이차항이 없는 삼차 방정식을 만든 후 다시 치환을 이용해 근을 찾는 방법으로 삼차 방정식의 일반적인 해법을 알게되었습니다. 

$$
\begin{align*}
& ax^3 + bx^2 + cx + d = 0 \vert_{x = t - \frac{b}{3a}} \\\\
\Rightarrow & \quad a\left(t - \frac{b}{3a}\right)^3 + b\left(t - \frac{b}{3a}\right)^2 + c\left(t - \frac{b}{3a}\right) + d = 0 \\\\
\Rightarrow & \quad a \left( t^3 - 3t^2\left(\frac{b}{3a}\right) + 3t\left(\frac{b}{3a}\right)^2 - \left(\frac{b}{3a}\right)^3 \right) + b \left( t^2 - 2t\left(\frac{b}{3a}\right) + \left(\frac{b}{3a}\right)^2 \right) + c \left(t - \frac{b}{3a} \right) + d = 0 \\\\
\Rightarrow &  \quad at^3 - bt^2 + \left(\frac{b^2}{a}\right)t - \frac{b^3}{27a^2} + bt^2 - \frac{2b^2t}{3a} + \frac{b^3}{9a^2} + ct - \frac{bc}{3a} + d = 0 \\\\
\Rightarrow &  \quad at^3 + \left(c- \frac{b^2}{3a}\right)t + \left( \frac{2b^3}{27a^2}- \frac{bc}{3a} + d \right)= 0
\end{align*}
$$

나아가 카르다노와 그의 제자 페라리(Ferrari)는 사차 방정식의 일반적인 해법까지 찾아냅니다. 이와 같은 근의 공식은 방정식의 해를 찾는 데 있어서 중요한 도구입니다. 

$$
ax^4+bx^3+cx^2+dx+e=0
$$

함수나 기하학적 도구 없이 오로지 방정식의 계수들과 사칙연산 그리고 제곱근만을 가지고 근을 찾아낼 수 있기 때문이죠. 다양한 분야에서 문제를 해결하기 위해 방정식의 근을 찾을 때 근의 공식은 시간과 노력을 크게 절약해주는 효율적인 도구가 되었습니다.

그러나 이러한 삼차 방정식의 해법에는 큰 문제가 하나 있었습니다. 예를 들어 간단한 형태의 삼차 방정식 $x^3-6x+4=0$의 근을 찾는다고 해보겠습니다. 먼저 이 방정식은 정수로 쉽게 인수분해 되므로 우리는 어렵지 않게 $x=2$가 근이 된다는 것을 알 수 있습니다.

$$
x^3-6x+4 =(x-2)(x^2+2x-2)
$$

반면에 근의 공식에 계수들 $a=-6$, $b=4$을 대입하면 다음과 같습니다. 

$$
\begin{align*}
x &= \sqrt[3]{-\frac{4}{2} + \sqrt{\frac{4^2}{4} + \frac{(-6)^3}{27}}} + \sqrt[3]{-\frac{4}{2} - \sqrt{\frac{4^2}{4} + \frac{(-6)^3}{27}}}\\
&= \sqrt[3]{-2 + \sqrt{-4}} + \sqrt[3]{-2 - \sqrt{-4}}
\end{align*}
$$

앞서 소개한 것과 같이 당시에는 음수에 대한 견해가 분명하지 않았습니다. 고대부터 음수의 문제를 실제로 다루지 않았죠. 방정식의 근이라는 것은 기하학적 아이디어에 기반을 두고 있었으므로 길이, 면적, 부피처럼 기하학적 구성의 결과로 반드시 양수여야 했습니다. 따라서 일부 학자들은 음수가 "방정식의 교리를 어둡게 하고, 그 자체가 명백하고 단순한 것을 불명확하게 한다"라고 말했습니다. 심지어 음수가 존재하지 않는다고 주장 하기까지 했죠.[^3] 음수는 존재하지 않는다고 생각했던 시기이기에 음수가 해가 되는 식들은 의미가 없다는 관점이 상당히 힘을 얻었습니다. 당연히 제곱근 안에 음수가 들어간다는 것은 상상도 할 수 없는 일이었습니다. 하지만 삼차 방정식의 해에 대한 논란이 일어나며 많은 사람들이 이해할 수 있는 독립적인 대수학 책이 필요하다고 느낀 봄벨리(Bombelli)는 자신의 책"L'algebra parte maggiore dell’aritmetica divisa in tre libri"을 통해 대수학에 대한 포괄적인 소개 뿐만 아니라 복소수의 산술을 처음으로 다루게 됩니다.[^4]

![[Pasted image 20250210122334.png|L'algebra parte maggiore dell’aritmetica divisa in tre libri p.169|300]]

169페이지 하단에서 볼 수 있듯이, Bombelli는 특정한 복소수를 곱할 때의 규칙을 제시했습니다. 이 규칙은 다음과 같이 해석됩니다.

>- 양수에 음수의 양의 제곱근을 곱하면 음수의 양의 제곱근이 됩니다.
>$1(\sqrt{-1}) = \sqrt{-1}$
>- 음수에 음수의 양의 제곱근을 곱하면 음수의 음의 제곱근이 됩니다. $(-1)(\sqrt{-1}) = -\sqrt{-1}$
>- 양수에 음수의 음의 제곱근을 곱하면 음수의 음의 제곱근이 됩니다. $1(-\sqrt{-1}) = -\sqrt{-1}$
>- 음수에 음수의 음의 제곱근을 곱하면 음수의 양의 제곱근이 됩니다. $(-1)(-\sqrt{-1}) = \sqrt{-1}$
>- 음수의 양의 제곱근에 음수의 양의 제곱근을 곱하면 음수가 됩니다. $(\sqrt{-1})(\sqrt{-1}) = -1$
>- 음수의 양의 제곱근에 음수의 음의 제곱근을 곱하면 양수가 됩니다. $(\sqrt{-1})(-\sqrt{-1}) = 1$
>- 음수의 음의 제곱근에 음수의 양의 제곱근을 곱하면 양수가 됩니다. $(-\sqrt{-1})(\sqrt{-1}) = 1$
>- 음수의 음의 제곱근에 음수의 음의 제곱근을 곱하면 음수가 됩니다. $(-\sqrt{-1})(-\sqrt{-1}) = -1$

이 책에서는 복소수를 곱하는 규칙도 상세히 설명되어 있는데, 예를 들면 양수에 음수의 양의 제곱근을 곱하면 음수의 양의 제곱근이 되고, 음수의 양의 제곱근에 음수의 양의 제곱근을 곱하면 음수가 된다는 식입니다. 봄벨리의 연산 방법에 따라 앞선 식을 다시 보도록 하겠습니다.

$$
\begin{align*}
(1-i)^3 = 1 - 3i + 3i^2 - i^3 = 1 - 3i - 3 + i = -2+2i\\
(1+i)^3 = 1 + 3i + 3i^2 + i^3 = 1 + 3i - 3 - i = -2-2i
\end{align*}
$$

$$
\begin{align*}
x &= \sqrt[3]{-2 + 2i} + \sqrt[3]{-2 - 2i}\\
&= (1-i) + (1+i)\\
&= 2
\end{align*}
$$

$1-i$와 $1+i$를 각각 세제곱하면 각각 $-2+2i$와 $-2-2i$가 됩니다. 삼차 방정식의 근의 공식에 따라 $x$의 각 제곱근 안에 이 결과를 대입하면 우리가 사용하는 연산의 결과를 유지한 채로 $x=2$라는 결과를 얻을 수 있습니다. 이렇게 봄벨리는 복소수를 곱할 때의 다양한 경우를 상세하게 규정했고, 이는 당시에는 상당히 혁신적인 접근이었습니다. 존재하지 않아 쓸모 없었던 것처럼 보이던 '가상의 수'를 이용해 의미 있는 결과를 도출해냈기 때문이죠.

일반적으로 복소수는 $a + bi$ 형태로 표현되며, 여기서 $a$는 실수 부분, $b$는 허수 부분, $i$는 $\sqrt{-1}$입니다. 중학교 때까지만 해도 모든 수는 제곱 하면 양수라고 했는데 제곱 하면 음수가 되는 $i$의 등장은 처음에 이해하기 어렵고 인위적으로 느껴질 수 있습니다. 하지만 앞서 본 내용과 같이 복소수는 방정식의 근을 매우 합리적이고 단순하게 찾을 수 있게 도와줍니다. 실수 범위에서는 불가능한 $\sqrt{-1}$과 같은 표현을 이용하면 근을 찾는 공식과 연산 방법을 유지한 채로 대수적으로 생길 수 있는 모든 문제를 해결하게 된거죠. 단순함을 추구하는 수학의 본질과 **대수적 일관성**을 유지할 수 있게 된 것입니다. 그리고 이러한 결과로부터 수학자들은 새로운 사실을 발견하게 됩니다.

## $x^n=1$(roots of unity)
$$
\begin{array}{|c|c|c|}
\hline
n & \text{equation}&\text{Real Roots} \\
\hline
1 & x-1 & 1 \\
\hline
2 & x^2-1 = (x-1)(x+1) &1, -1 \\
\hline
3 & x^3-1 =(x-1)(x^2+x+1) &1 \\
\hline
4 & x^4-1 = (x-1)(x+1)(x^2+1)&1, -1 \\
\hline
5 & x^5-1 = (x-1) (1 + x + x^2 + x^3 + x^4)&1 \\
\hline
6 & x^6-1 = (x - 1)(x + 1) (x^2 - x +1) (x^2 + x + 1)&1, -1 \\
\hline
\vdots & \vdots& \vdots \\
\hline
\end{array}
$$
실수에서 $x^n=1$을 만족하는 $x$의 값들을 정리해보면 다음과 같습니다. $x=1$일 때, 자명한 근을 포함하며  $n$이 홀수일 때는 $1$개, $n$이 짝수일 때는 $2$개로 규칙적으로 반복됩니다. 그런데 복소수의 등장과 함께 이 규칙에 조금 다른 점이 보이게 됩니다.

$$
\begin{align*}
x^3 - 1 &= (x - 1)(x^2 + x + 1) = 0\\
&\Rightarrow x = 1, \frac{-1 + i\sqrt{3}}{2}, \frac{-1 - i\sqrt{3}}{2}
\end{align*}
$$

$x^3-1=0$을 인수 분해 한 후 근의 공식을 이용하여 복소수까지 확장한 해를 찾아보면 근이 총 $3$개가 발견됩니다. 같은 방법으로 $x^4-1 = 0$도 복소수까지 확장하여 해를 찾아보면 근이 총 $4$개가 발견됩니다. 

$$
\begin{align*}
x^4 - 1 & = (x - 1)(x + 1)(x^2 + 1) = 0\\
& \Rightarrow x = 1, -1, i, -i
\end{align*}
$$

복소수까지 확장해 근을 찾으면 $n$차 방정식은 $n$개의 해를 갖는 것과 같이 보이죠. 이러한 특성을 더 잘 이해하기 위해 복소수를 좌표평면상에 표시해보겠습니다. 복소수를 좌표평면에 표시하는 방법은 매우 쉽고 직관적입니다. 복소수 $a+bi$는 좌표평면에서 점 $(a, b)$로 표현됩니다. $a$는 실수 부분이고 $b$는 허수 부분이죠. 이렇게 표현하면 두 복소수의 덧셈은 실수부는 실수부끼리 허수부는 허수부끼리 연산이 되므로 좌표평면상의 덧셈으로 표현할 수 있습니다.

$$
\begin{gather*}\\
(a + bi) + (c + di) = (a+c)+(b+d)i \\
(a, b) + (c, d) = (a+c, b+d)
\end{gather*}
$$

그리고 복소수의 곱셈은 실수부는 벡터의 내적꼴, 허수부는 분수 덧셈에서의 분자 꼴로 나오며 대수적 규칙을 유지합니다. 이는 벡터의 길이와 각도를 고려한 연산으로 표현되죠.

$$
(a+bi) \times (c+di) = (ac - bd) + (ad + bc)i
$$

예를 들어, $z_1 = 1 + i$와 $z_2 = \sqrt3 + i$라고 할때, 
$$
(1+i)(\sqrt3+i) = (\sqrt3 - 1) + (\sqrt3 +1)i
$$
로 계산할 수도 있지만, 극좌표를 이용해 나타내면 $z_1 = 1 + i = \sqrt{2} e^{\frac{i\pi}{4}}$, $z_2 = \sqrt{3} + i = 2 e^{\frac{i\pi}{6}}$이므로 두 수의 곱을

$$
\begin{align*}
z_1 \times z_2 &= \sqrt{2} \times 2 \times e^{i(\frac{\pi}{4} + \frac{\pi}{6})}\\
&= 2\sqrt{2} \times e^{i\frac{5\pi}{12}} 
\end{align*}
$$
로 원점으로부터의 길이와 동경을 이용해 간단히 표현할 수 있습니다.

이러한 방식으로 복소수의 대수적 연산을 좌표평면과 연관지어 정의하면, 복소수가 단순한 숫자 이상의 의미를 가지며 다양한 수학적 문제를 풀거나 이해하는 데 도움을 줍니다. 이제 오일러 공식을 이용해 $x^n=1$을 만족하는 점들을 좌표평면 위에 표시해보겠습니다.[^5] 오일러 공식은 다음과 같이 주어집니다.

$$
e^{i\theta} = \cos(\theta) + i\sin(\theta)
$$

 $\theta = 2\pi$를 대입하면 $e^{i 2\pi} = 1$이 되므로 $x^n = 1$을 만족하는 $x$는 다음과 같이 표현할 수 있습니다.
 
$$
\begin{align*}
x^n & = e^{i 2\pi k}\\
\Rightarrow x_k &= e^{\frac{2\pi i k}{n}}\\
\Rightarrow x_k &= \cos\left(\frac{2\pi k}{n}\right) + i \sin\left(\frac{2\pi k}{n}\right)
\end{align*}
$$

따라서 $x^n=1$의 근 들은 $(1,~0)$을 고정한 후 단위원을 $n$등분 한 점들 이라는 것을 알 수 있습니다. 

$$
\begin{array}{|c|c|}
\hline
n & \text{Complex Roots} \\
\hline
1 & 1 \\
\hline
2 & 1, -1 \\
\hline
3 & 1, -\frac{1}{2} + \frac{\sqrt{3}}{2}i, -\frac{1}{2} - \frac{\sqrt{3}}{2}i \\
\hline
4 & 1, i, -1, -i \\
\hline
5 & 1, \frac{\sqrt{5} + 1}{4} + \frac{\sqrt{10 - 2\sqrt{5}}}{4}i, \frac{\sqrt{5} - 1}{4} + \frac{\sqrt{10 + 2\sqrt{5}}}{4}i,
\frac{\sqrt{5} - 1}{4} - \frac{\sqrt{10 + 2\sqrt{5}}}{4}i, \frac{\sqrt{5} + 1}{4} - \frac{\sqrt{10 - 2\sqrt{5}}}{4}i \\
\hline
6 & 1, -1, \frac{1}{2} + \frac{\sqrt{3}}{2}i, -\frac{1}{2} + \frac{\sqrt{3}}{2}i, \frac{1}{2} - \frac{\sqrt{3}}{2}i, -\frac{1}{2} - \frac{\sqrt{3}}{2}i \\
\hline
\vdots & \vdots \\
\hline
\end{array}
$$

결과적으로 $x^n=1$을 만족하는 점들은 원을 $n$등분 하여 나오는 점들이므로 $n$개의 해를 가집니다. 그렇다면 이 성질은 $x^n=1$뿐만 아니라 더 복잡한 방정식으로 확장할 수 있을까요?  

## 대수학의 기본정리 (Fundamental Theorem of Algebra)
수학에서 **기본 정리**라는 용어는 세부 분야의 핵심적인 원칙이나 규칙을 의미합니다. 흔히 고등학교 교과서에 있는 미적분학의 기본정리가 미분과 적분이 본질적으로 '역연산' 관계에 있다는 것을 보여주는 것처럼 기본 정리는 해당 학문의 기초를 이루며, 다양한 문제 해결과 이론 개발에 있어 중추적인 역할을 합니다.

$$
\int_a^b f'(t)dt = f(b)-f(a)
$$

대수학은 산술의 일반화로 시작되었으며 오늘날에 있어서는 수와 수 사이의 관계, 구조, 변화, 그리고 이러한 개념들을 일반화하고 추상화하는 수학의 한 분야입니다. 고등학교 과정까지만 본다면 쉽게 말해 미지수를 이용해 방정식을 푸는 것을 의미하죠. 그리고 고등학교 1학년 때 어렴풋이 들었던 기억이 나는 정리가 있습니다. 바로 $n$차 방정식은 복소수 상에서 (중복을 허용하여) $n$개의 해를 갖는다는 거죠. 별거 아닌거 같지만 참 신기한 성질입니다.

$$
\begin{align*}
P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 ,~a_n \neq 0,~a_n \in \mathbb{C}
\end{align*}
$$

$n$차 방정식이라고 하지만 근이 $n$보다 많거나 적을 수도 있는데 그렇지 않고 정확하게 $n$개만 갖는다는 것이죠. 복소수는 이처럼 방정식의 해를 일관되게 만들어 주기 때문에 방정식의 근을 찾는 대수학이 한층 깔끔해집니다. 그렇다면 이 사실을 어떻게 알게 되었을까요?

## 증명의 아이디어
대수학의 기본정리는 대수학에서 중요한 위치를 차지하고 있지만, 아이러니하게도 이를 증명하기 위해서는 실수의 완비성과 같은 해석학적 개념이 필요합니다. 그래서 정말 신기하게도 이 증명은 복소해석학과 위상을 이용해 증명됩니다. 최초의 증명은 달랑베르(d'Alembert)에 의해 시도되었으나 완전하지 않았습니다. 이후 오일러, 라그랑주, 라플라스 등이 증명을 시도했으나, 그들의 증명도 불완전했습니다. 결국 가우스가 박사학위 논문에서 이전의 증명들에서 틀린점을 반박하고 이후 몇 가지 증명을 더 내놓으며 최초의 증명은 가우스가 증명했다고 알려져 있습니다.[^6] 

<iframe src="https://www.geogebra.org/classic/jhvc4nxt?embed" width="100%" height="450" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

가우스의 아이디어는 다음과 같습니다. 예를들어 삼차 방정식 $f(z) = 4z^3+3z^2+2z+1$이 있다고 해보겠습니다. 복소 함수는 $2$차원 복소평면에서 $2$차원 복소평면으로 가는 함수입니다. 따라서 함수가 $4$차원에 있어 한 눈에 보기 어려우므로 정의역을 제한하면서 관찰하겠습니다. 우선 정의역을 $e^{iz}$ 즉, 반지름의 길이가 $1$인 단위원의 모든 값의 함숫값을 보겠습니다. $\theta$가 $0 \le \theta \le 2\pi$일 때, 함숫값을 보면 좌측의 점이 단위원을 한 바퀴 돌 때, 우측의 함숫값은 다음과 같은 궤적을 그리면서 회전하는 것을 볼 수 있습니다. 이때 자세히 보시면 점이 복소함수의 궤적을 따라 움직이면서 원점을 기준으로 세바퀴 회전하는 것을 볼 수 있습니다.

$$
\because  z = R \cos \theta + i R \sin \theta \Rightarrow z^n = R^n \cos n\theta + i R^n \sin n\theta
$$

방정식의 해라는 것은 함숫값이 $\mathbb{0}$이되게 하는 정의역을 의미하는데 복소 함수에서 오른쪽 그래프가 $\mathbb{0}$ 즉, 원점$(0,~0)$을 지나지 않으므로 $r=1$에서는 해를 갖지 않는 것을 알 수 있습니다.

그렇다면 이 함수는 복소수에서 해를 갖지 않는 것일까요? 그렇지 않습니다. 저는 정의역인 복소 평면 전체 중 단지 $r=1$인 단위원에서 밖에 해를 조사하지 않았습니다. 모든 정의역 조사하기 위해서는 복소 평면 전체를 덮어야하므로 우리는 $r$의 값을 조정해나가면서 정의역 전체에 대해 함숫값이 어떻게 변하는지 관찰해보겠습니다.

$r$의 값이 $1$보다 크다면 앞서 본 원점을 둘러싸고 있는 함수의 궤적은 점점 커지며, 반대로 $r$의 값이 1보다 작다면 함수의 궤적은 점점 작아집니다. 만약 극단적으로 $r=0$이라면 $z=0$이므로 $f(0)=1$이 됩니다. 그런데 이러한 복소함수는 $r$의 값이 변함에 따라 연속적으로 변하게됩니다. 그렇다면 원점을 세 번 둘러쌓은 이 그래프는 $(1,0)$으로 수렴해감에 따라 적어도 $3$번은 반드시 원점을 지나쳐야할 것입니다. $n$차 방정식은 $n$보다 많은 해를 가질 수는 없으므로 결과적으로 삼차 방정식은 복소수 상에서 $3$개의 근을 갖는 것을 알 수 있습니다.(그리고 이 함수를 보면 $x$축에 대해 대칭이므로 근은 반드시 켤레로 생겨야한다는 것도 시각적으로 확인할 수 있습니다.)

그런데 삼차방정식이라고해서 세 번 지나치는 것을 모두 확인할 필요는 없습니다. 왜냐하면 대수학의 기본정리는 다음과 같이 적을 수도 있기때문이죠. 다른말로 한 점에서 영점을 갖는 것만 보여도 충분합니다.

> 모든 상수가 아닌 $\mathbb{C}[x]$의 다항식은 $\mathbb{C}$ 안에 해를 가진다.

왜냐하면 $n$차 방정식 $f(z)$가 $z_1$에서 영점 즉, 근을 갖는다면 다음과 같이 적을 수 있습니다.

$$
f(z)=(z-z_1)Q_1 (z)
$$

여기서 $Q_1(z)$는 $(n-1)$차 방정식이죠. 같은 논리를 $Q_1(z)$에 적용하면 적당한 복소수 $z_2$가 존재해서 $(n-2)$차 방정식 $Q_2(z)$에 대해 다음과 같이 적을 수 있습니다.

$$
f(z)=(z-z_1)(z-z_2)Q_2 (z)
$$

이런 방법으로 계속한다면 결과적으로 $n$차 방정식은 $n$개의 해를 가진다는 것을 보일 수 있습니다.

$$
f(z)=(z-z_1)(z-z_2)\cdots(z-z_n)
$$

## 가우스의 증명
가우스는 먼저 방정식에서 계수가 실수여도 충분하다는 것을 증명하였습니다. 왜냐하면 $f(z)$가 복소수 근을 갖고 있다는 것을 증명하면 모든 계수들을 복소수인 경우에도 여전히 복소수 근을 가지기 때문이죠. 

$$
f(z)=a_0 + a_1z + a_2z^2 + \cdots + a_n z^n
$$

만약 $f(z)$의 계수가 모두 복소수라고 가정해보겠습니다. 그리고 켤레 복소수를 이용해 함수를 다음과 같이 정의하면

$$
\bar f(z) = \overline {a_0} + \overline {a_1}z + \overline {a_2}z^2 + \cdots + \overline{a_n} z^n
$$

새로운 함수 $g(z)$는 다음 식을 만족합니다. 

$$
g(z)=f(z) \bar{f}(z)= f(z)\overline{{f}(\bar{z})}
$$

따라서 $g(z)$는 실수 계수를 갖고 있으며 이 방정식이 근 $z_0$를 갖는다면

$$
g(z_0)=f(z_0) \bar{f}(z_0)= f(z_0)\overline{{f}(\overline{z_0})} = 0
$$

$f$는 $z_0$ 또는 $\overline{z_0}$가 근이 됩니다. 그러므로 $f$를 간단하게 실수계수 다항식이라 하겠습니다. 가우스의 실제 증명은 실수부와 허수부를 따로 관찰하며 이 두함수가 모두 $0$이 되는 지점이 교차해야한다고 했습니다.  복소수의 절댓값을 $\vert z \vert =r$로 놓은 다음 $r$이 충분히 크면 각각의 곡선들은 원 $\vert z \vert =r$과 $2n$개의 점에서 만나고,  이 곡선들이 만나는 점들이 서로 교차함을 보였죠. 즉, 한 곡선이 원과 만나는 두 개의 점 사이에는 다른 곡선의 점이 원과 만남을 보인 것입니다.

<iframe src="https://www.geogebra.org/classic/v64y4s3j?embed" width="100%" height="450" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

그리고 원 $\vert z \vert  \le r$ 이면 반드시 다시 나온다는 것을 증명하지 않고 주장했죠. 가우스는 각주에서 "이에 대한 의심을 제기한 사람이 없다고 알고 있다. 그러나 만약 누군가 그렇게 요구한다면, 나중에 의심의 여지가 없는 증명을 제공하겠다"고 적었습니다. 하지만 실제로 이 부분까지 증명하지는 않았죠.(자세한 증명은 참고자료를 보시길 추천드립니다.) [^7]

### 리우빌의 정리(Liouville's theorem)를 이용한 증명
오늘날 대수학의 기본정리는 복소해석학을 이용해 조금 더 쉽게 증명할 수 있습니다. 리우빌의 정리란 복소함수가 전체 복소평면에서 유한한 값을 가지려면 그 함수는 상수 함수밖에 없다는 것을 알려주는 정리입니다. 이 내용으로 어떻게 대수학의 기본정리를 증명할 수 있을까요? 차근차근 보도록 하죠.

#### 증명
$f$가 전해석 함수이고 복소 평면에서 유계이면, $f(z)$는 복소 평면 전체에 상수이다.

우선 복소함수 $f$는 적당한 조건에서 코시부등식을 만족합니다.

 중심이 $z_0$이고 반지름의 길이가 $R$인 양의 방향의 원 $C_r$과 그 안에서 해석적이라 할때, $C_R$에서 $\vert f(z) \vert$의 최댓값을 $M_R$이라 하면  

$$
\begin{align*}
&f^{(n)}(z_0)=\frac{n!}{2\pi i} \int_{C_R} \frac{f(z)}{(z-z_0)^{n+1}}dz \quad (n=1, ~2, ~\cdots)\\
\Rightarrow & \lvert f^{(n)}(z_0) \rvert = \frac{n!}{2\pi} \cdot \frac{M_R}{R^{n+1}}2\pi R \quad (n=1, ~2, ~\cdots)\\
\Rightarrow &\lvert f^{(n)}(z_0) \rvert = \frac{n! M_R}{R^{n}} (n=1, ~2, ~\cdots)
\end{align*}
$$

이제 $f$가 전해석함수이고 유계라면 코시부등식에 의해 임의로 선택한 $z_0$와 $R$에 대하여 $n=1$일 때, 다음 식이 성립합니다.

$$
\lvert f^\prime(z_0) \rvert \le \frac{M_R}{R}
$$
게다가 $f$가 유계라는 조건에 의해 $R$에 의한 값이 아닌 상수 $M$이 존재하여 식을 더 간단하게 표현할 수 있습니다.

$$
\lvert f^\prime(z_0) \rvert \le \frac{M}{R}
$$

앞서 말했든 임의의 $R$에 대하여 이 식이 성립해야하는데 $R$은 충분히 커질 수 있으므로 결과적으로 $f'(z_0)=0$이어야 합니다. 또 $z_0$도 임의의 점이므로 복소 평면 어디서나 $f'(z)=0$임을 알 수 있습니다. 따라서  $f(z)$는 복소평면 전체에서 상수입니다.

이제 앞서 본 리우빌 정리의 성질을 이용해 대수학의 기본정리를 증명해보겠습니다. 앞서 설명했듯이 $n$차 방정식에 대하여 근 하나만 찾을 수 있다면 같은 방법으로 $n-1$차에도 근이 있음을 보일 수 있으므로 증명이 완료됩니다. 

$n(n \ge 1)$차 다항함수 $f(z)$에는 적어도 한 개의 영점이 있다. 즉 적어도 한 개의 점 $z_0$이 존재하여 $f(z_0)=0$이다. 
$$
f(z)=a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n \quad (a_n \not= 0)
$$

우선 $f(z)$가 근을 갖지 않는다고 가정해보겠습니다. 따라서 $f(z) \not= 0$이므로 몫함수 $\frac {1}{f(z)}$를 정의할 수 있으며 이 또한 전해석 함수가 됩니다. 그러면 복소함수의 성질에 의해 충분히 큰 양수 $R$에 대하여  $\vert z \vert > R$일 때, 다음이 성립합니다.
$$
\frac{1}{f(z)}< \frac{2}{ \vert a_n \vert R^n }
$$

따라서 $\frac{1}{f(z)}$은 $\vert z \vert  \le R$의 밖 구역에 갇혀있게 됩니다. 그런데 $\frac{1}{f(z)}$은 닫힌 원판에서 연속이므로, 그 곳에서 유계가 됩니다. (쉽게 생각해 $\lim_{|z| \rightarrow \infty} \vert f(z) \vert =  \infty$이므로 $\lim_{|z| \rightarrow \infty} \vert {\frac{1}{f(z)}} \vert =  0$이다.) 그러므로 $\frac{1}{f(z)}$은 평면 전체에서 유계가 되며 앞서 본 리우빌 정리에 의해 $\frac{1}{f(z)}$은 상수함수가 됩니다. 그 말은 $f(z)$도 상수 함수여야한다는 건데 이는 모순이므로 결과적으로 $f(z)$는 근을 갖게 됩니다.

사실 이 증명이 유일한 증명은 아닙니다. 코시-구르사 정리를 이용한 방법도 있고,[^8] 로쉐(Rouchè)의 정리를 이용해 직접적으로 $n$차 방정식에서 정확히 $n$개의 해를 가짐을 보이는 방법도 있죠.[^9] 오늘날에는 대수적 아이디어만을 사용하여 증명하는 방법[^10]도 있습니다만 굳이 쉬운 방법을 이용해도 충분한데 어려운 방법으로 돌아지는 않겠습니다.

## 에필로그
사실 전 처음 $i$에 대해 배웠을 때 별로 큰 생각이 없었습니다. 그냥 필요하니까 만들었겠지라는 생각으로 연산만 주구장창했었죠. 대학에서 크로네커 정리를 통해 근이 반드시 존재하는 체로 확장하는 방법이나 복소해석학에서 리우빌 정리를 배웠을때도 그 정리 하나의 함의만 보고 증명을 외우는데 급급했습니다. 학교에 다닐 때는 당장 배워야 할 내용이 너무나 많다는 핑계로 왜 그래야만 하는가에 대한 질문은 하지 않았던 것 같습니다. 오히려 이번 기회로 저도 역사적 맥락과학교에서 왜 이러한 순서대로 교육을 진행했는지 조금이나마 더 잘 알게 되었고 학생들에게 해주고 싶은 이야기들이 늘어난 것 같아 뿌듯합니다. 여러분들도 조금이나마 $i$를 도입하기 위한 수학자들의 논의가 친숙해지셨기를 바랍니다. 

---

Let $n$ denote the degree of $f$. Without losing generality, assume the leading coefficient of $f$ is $1$, thus $f(z) = z^n + \sum_{m=0}^{n-1} c_m z^m$.

Define $R = 1 + \sum_{m=0}^{n-1} |c_m|$. By this choice of $R$, when $|z| > R$, $f(z) \neq 0$. Assuming $|z| \geq R$ and since $R \geq 1$, $|z^a| \leq |z^b|$ whenever $0 < a < b$.

The chain of inequalities follows:
$$ \left|\sum_{m=0}^{n-1} c_m z^m \right| \leq 1 + \sum_{m=0}^{n-1} |c_m||z^m| \leq |z^{n-1}| + \sum_{m=0}^{n-1} |c_m||z^{n-1}| \leq R|z^{n-1}| \leq |z^n| $$

Polynomials in $z$ are entire, and hence, are analytic functions in the disk $|z| \leq R$. So, Rouché’s theorem can be applied here. Given that $\left|\sum_{m=0}^{n-1} c_m z^m \right| \leq |z^n|$ for $|z| \geq R$, Rouché’s theorem implies that $z^n$ and $f(z)$ have the same number of zeroes in the disk $|z| \leq R$.

Since $z^n$ has a single zero of multiplicity $n$ at $z = 0$, which counts as $n$ zeroes, $f(z)$ must also have $n$ zeroes counted with multiplicity in the disk $|z| \leq R$. By the choice of $R$, it’s concluded that $f$ has exactly $n$ zeroes in the complex plane.


---


In the given scenario, we begin with a polynomial $f(x) \in \mathbb{C}[x]$ and a root $a$ of $f(x)$ in some extension of $\mathbb{C}$. We then introduce $K$ as a Galois closure of $\mathbb{C}(a)$ over $\mathbb{R}$ and define $G$ as $\operatorname{Gal}(K/\mathbb{R})$. Further, $H$ is a Sylow 2-subgroup of $G$, and $L = K^{H}$ is the fixed field of $H$ in $K$.

By the Fundamental Theorem of Galois Theory, we establish the equality $[L:\mathbb{R}]=[G:H]$, which is an odd number. It follows that $L$ can be expressed as $\mathbb{R}(b)$ for some $b \in L$. Thus, the minimal polynomial $m_{b,\mathbb{R}}(x)$ is irreducible over $\mathbb{R}$ and of odd degree. This implies that the degree must be 1, leading to $L = \mathbb{R}$, and hence $G = H$, a 2-group.

Now, $G_{1} = \operatorname{Gal}(K/\mathbb{C})$ is also a 2-group. If $G_{1} \neq 1$, we choose $G_{2} \leq G_{1}$ such that $[G_{1}:G_{2}] = 2$, and set $M = K^{G_{2}}$, leading to $[M:\mathbb{C}] = [G_{1}:G_{2}] = 2$. However, by the quadratic formula, any polynomial of degree 2 over $\mathbb{C}$ has roots in $\mathbb{C}$, making the existence of such a field $M$ impossible. This contradiction implies $G_{1} = 1$, and therefore $K = \mathbb{C}$ and $a \in \mathbb{C}$, completing the proof.

---



This markdown content encapsulates the core aspects of the proof utilizing Rouché’s theorem to demonstrate the Fundamental Theorem of Algebra.

[^1]: [New Light on Plimpton 322](https://maa.org/sites/default/files/pdf/news/monthly105-120.pdf)
[^2]: [Babylonian Quadratics](https://www.jstor.org/stable/27963851?read-now=1)
[^3]: [The History of Negative Numbers](https://nrich.maths.org/5961)
[^4]: [Mathematical Treasure: Raphael Bombelli's L'algebra](https://maa.org/press/periodicals/convergence/mathematical-treasure-raphael-bombellis-lalgebra)
[^5]: https://www.geogebra.org/classic/e565uncb
[^6]: [Fundamental theorem of algebra - Wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra)
[^7]: [On Gauss’s First Proof of the Fundamental Theorem of Algebra](https://arxiv.org/pdf/1704.06585.pdf)
[^8]: [Yet Another Proof of the Fundamental Theorem of Algebra.](https://sci-hub.se/https://doi.org/10.2307/2311751)
[^9]: [proof of fundamental theorem of algebra (Rouché’s theorem) (planetmath.org)](https://planetmath.org/proofoffundamentaltheoremofalgebrarouchestheorem)
[^10]: [A PURELY ALGEBRAIC PROOF OF THE FUNDAMENTAL THEOREM OF ALGEBRA](https://browse.arxiv.org/pdf/1504.05609.pdf)