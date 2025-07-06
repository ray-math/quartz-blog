---
title: 복소수(Complex number)
date: 2025-02-21
tags:
---
대수학에서는 실수체 만으로 이론을 전개하기 어려울 때가 많다. 예를 들어, $x^2 + 1 = 0$처럼 실수 계수를 갖는 다항식 중에서 실수 범위에서 해를 갖지 않는 경우가 있기 때문이다. 이러한 이유로, 모든 비영(非零)차수의 다항식이 그 계수를 가진 집합에서 해를 갖도록 하는 확장이 필요하다. 즉, 실수의 집합을 확장하여 이러한 조건을 만족하는 새로운 수 체계를 구축할 수 있다.

## 복소수(Complex number) 
복소수(Complex number)는 다음과 같은 꼴의 표현을 갖는 수이다. 

$$
z = a + bi
$$

여기서 $a, b$는 실수이며, 각각 실수 부분(real part)과 허수 부분(imaginary part)이라고 부른다.

### 복소수의 덧셈과 곱셈
복소수 $z = a + bi$와 $w = c + di$에 대해, 두 복소수의 합(Sum)과 곱(Product)은 각각 다음과 같이 정의된다. 

- 덧셈 (Addition)

$$
z + w = (a + bi)+ (c + di)= (a + c)+ (b + d)i
$$

- 곱셈 (Multiplication)

$$
zw = (a + bi)(c + di)= (ac - bd)+ (bc + ad)i
$$
## 실수를 복소수로 확장하기 
어떤 실수 $c$도 복소수로 간주할 수 있다. 즉, $c$를 복소수 $c + 0i$와 동일한 것으로 보면, 실수의 연산이 복소수의 연산과 자연스럽게 일치함을 확인할 수 있다. 
$$
\begin{gather*}
(c + 0i)+ (d + 0i)= (c + d)+ 0i \\\\
(c + 0i)(d + 0i)= cd + 0i
\end{gather*}
$$
따라서, 실수의 덧셈과 곱셈은 복소수의 덧셈과 곱셈의 특수한 경우로 볼 수 있다.

### 허수의 정의
$bi = 0 + bi$ 형태의 복소수를 허수(imaginary number)라고 한다. 이때, $b$는 $0$이 아닌 실수이다. 두 허수의 곱은 실수가 됨을 보이자. 

$$
(bi)(di)= (0 + bi)(0 + di)= (0 - bd)+ (b\cdot 0 + 0\cdot d)i = -bd
$$

특히, 허수 단위 $i$에 대해 

$$
i \cdot i = -1
$$

이는 복소수 곱셈의 정의를 기억하는 중요한 성질이 된다. 
즉, 복소수를 곱할 때 일반적인 다항식 전개처럼 계산하고, 
$i^2 = -1$로 대체하면 된다.

### 덧셈과 곱셈에 대한 항등원 
- 덧셈 항등원 : 복소수에서 $0$은 덧셈 항등원(identity)역할을 한다.
 $$
 (a + bi)+ 0 = (a + bi)+ (0 + 0i)= (a+0)+ (b+0)i = a + bi.
 $$

- 곱셈 항등원 : 복소수에서 $1$은 곱셈 항등원 역할을 한다.
 $$
 (a + bi)\cdot 1 = (a + bi)(1 + 0i)= (a\cdot1 - b\cdot0)+ (b\cdot1 + a\cdot0)i = a + bi.
 $$

### 복소수의 덧셈 역원과 곱셈 역원 
- 덧셈 역원 : 복소수 $a + bi$의 덧셈 역원은 $-a - bi$이다. 

$$
(a + bi)+ (-a - bi)= 0.
$$

- 곱셈 역원 : $0$이 아닌 복소수 $a + bi$의 곱셈 역원은 다음과 같이 주어진다.
 $$
 (a + bi)^{-1} = \frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2} i.
 $$

복소수의 역수를 구하려면 켤레 복소수를 이용하여 분모를 실수로 만들면 된다.

결국 복소수는 덧셈, 곱셈, 뺄셈, 나눗셈에 대해 닫혀 있으며, 교환법칙, 결합법칙, 분배법칙이 성립하므로 체(Field)를 만족한다.

## 복소수의 켤레 (Complex Conjugate) 
복소수 $a + bi$의 켤레 복소수(complex conjugate)는 $a - bi$이다. 복소수 $z$의 켤레는 $\overline{z}$로 표기한다.

### 켤레 복소수의 성질
복소수 $z, w$에 대해 다음 성질들이 성립한다.

1. 켤레 연산의 자기역성(Self-involution) 
  $$
  \overline{\overline{z}} = z
  $$

2. 덧셈에 대한 성질[^1]
  $$
  \overline{z + w} = \overline{z} + \overline{w}
  $$

3. 곱셈에 대한 성질[^2]
  $$
  \overline{zw} = \overline{z} \cdot \overline{w}
  $$

4. 나눗셈에 대한 성질 (단, $w \neq 0$)[^3]
  $$
  \overline{\left(\frac{z}{w}\right)} = \frac{\overline{z}}{\overline{w}}
  $$

5. $z$가 실수일 필요충분 조건 
  $$
  z \text{가 실수} \iff \overline{z} = z
  $$

### 켤레 복소수와 절댓값 
어떤 복소수 $z = a + bi$에 대해, $z \overline{z}$는 항상 실수이고 $0$이상이다. 
$$
\begin{align*}
z \overline{z} &= (a + bi)(a - bi)\\
&= a^2 - abi + abi - b^2i^2\\
&= a^2 + b^2
\end{align*}
$$
### 복소수의 절댓값 (Absolute Value) 
복소수 $z = a + bi$의 절댓값(absolute value)또는 법(modulus)은 다음과 같이 정의된다. 
$$
|z| = \sqrt{a^2 + b^2}
$$

$z$의 절댓값을 $\vert z \vert$라 표기한다. $z\overline{z} = \vert z \vert^2$임을 기억하자. 복소수와 켤레복소수이 곱이 실수임을 이용하면 복소수의 나눗셈을 쉽게할 수 있다. 복소수 $z = a + bi$, $w = c + di$에 대해 $w \neq 0$일 때, 복소수의 나눗셈은 다음과 같이 정의된다.

$$
\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac+bd) + (bc -ad)i}{c^2 + d^2} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2} i

$$
### 복소수 절댓값의 성질
1. 곱셈에 대한 성질[^4]
  $$
  |zw| = |z| \cdot |w|
  $$

2. 나눗셈에 대한 성질 (단, $w \neq 0$)[^5]
  $$
  \left| \frac{z}{w} \right| = \frac{|z|}{|w|}
  $$

3. 삼각 부등식 (Triangle Inequality)[^6]
  $$
  |z + w| \leq |z| + |w|
  $$

4. 절댓값 차에 대한 부등식[^7]
  $$
  ||z| - |w|| \leq |z + w|
  $$

## 복소수의 기하학적 표현 (Geometric Representation of Complex Numbers) 
복소수는 대수적 표현뿐만 아니라 기하학적 표현도 가질 수 있다. 즉, 복소수 $z = a + bi$는 복소수 평면(complex plane)에서 한 점으로 표현할 수 있다.

![[CleanShot 2025-02-21 at 17.53.51@2x.png]]

- 복소수의 실수부(real part)$a$는 실수 축(real axis)에서의 좌표이다.
- 복소수의 허수부(imaginary part)$b$는 허수 축(imaginary axis)에서의 좌표이다.
- 절댓값 $|z|$는 원점에서 해당 점까지의 벡터의 길이를 나타낸다.
- 복소수 덧셈은 평행사변형 법칙(parallelogram law)을 이용해 해석할 수 있다.

### 오일러 공식과 극형식 (Euler’s Formula and Polar Form) 
복소수를 극좌표계에서 표현할 수도 있다. 특히, 오일러 공식(Euler's formula)은 다음과 같이 주어진다.

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

이로 인해, 복소수 $z$를 다음과 같은 극형식으로 나타낼 수 있다.

$$
z = |z| e^{i\phi}
$$

여기서 $\phi$는 복소수 $z$가 양의 실수 축(positive real axis)과 이루는 각도이다.

### 복소수 곱셈의 기하학적 의미 
두 복소수 $z$와 $w$를 극형식으로 표현하면,

$$
z = |z| e^{i\theta}, \quad w = |w| e^{i\omega}
$$

이제, 곱셈을 수행하면

$$
zw = (|z| e^{i\theta})(|w| e^{i\omega})
$$

곱셈 성질을 이용하여 정리하면,

$$
zw = |z| |w| e^{i(\theta + \omega)}
$$

즉, 복소수의 곱셈은 길이의 곱과 각도의 합으로 해석된다.

- 길이(절댓값): $|zw| = |z| |w|$.
- 각도(위상): $zw$는 $z$와 $w$의 각도를 더한 방향을 가진다.

이 기하학적 해석은 회전 변환(rotation transformation)을 설명하는 데 유용하며, 신호 처리, 양자 역학, 공학 등 다양한 분야에서 중요한 역할을 한다.

[^1]: $z + w = (a + bi)+ (c + di)= (a + c)+ (b + d)i$이므로, $\overline{z + w} = (a + c)- (b + d)i = (a - bi)+ (c - di) =  \overline{z} + \overline{w}$
[^2]: $zw = (a + bi)(c + di)= ac - bd + (ad + bc)i$이므로, $\overline{zw} = (ac - bd)- (ad + bc)i$이다. $\overline{z} \cdot \overline{w} = (a - bi)(c - di)= ac - bd - (ad + bc)i$이다. 따라서 $\overline{zw} = \overline{z} \cdot \overline{w}$
[^3]: $\overline{\frac{1}{z}} = \frac{1}{\overline{z}}$임을 보이면 충분하다. $\overline{\frac{1}{z}} = \overline{\frac{1}{a+bi}} = \overline{\frac{a-bi}{a^2 + b^2}} = {\frac{a+bi}{a^2 + b^2}}$이고, $\frac{1}{\overline{z}} = \frac{1}{\overline{a+bi}} = \frac{1}{a-bi} = {\frac{a+bi}{a^2 + b^2}}$이다. 따라서 $\overline{\frac{1}{z}} = \frac{1}{\overline{z}}$이다.(또는 $z\overline{z} = \vert z \vert^2$이므로, $\overline{\frac{1}{z}} = \overline{\frac{\overline{z}}{\vert z \vert^2}} = {\frac{{z}}{\vert z \vert^2}} =\frac{1}{\overline{z}}$) 켤레 곱셈의 성질에 의해 $\overline{\left(\frac{z}{w}\right)} = \frac{\overline{z}}{\overline{w}}$이다.
[^4]: $|zw|^2 = (zw)(\overline{zw})= (zw)(\overline{z} \cdot \overline{w})= (z\overline{z})(w\overline{w})= |z|^2 |w|^2$ 이므로, $|zw| = |z| \cdot |w|$이다.
[^5]: $\left| \frac{z}{w} \right|^2 = \left| z w^{-1} \right|^2 = |z|^2 |w^{-1}|^2$이므로, $\left|\frac{z}{w} \right| = \frac{|z|}{|w|}$
[^6]: 먼저 임의의 복소수 $x = a + bi$에 대해, $x + \overline{x} = (a+bi)+ (a-bi)= 2a \leq 2\sqrt{a^2 + b^2} = 2|x|$이다. 이제 $x = w\overline{z}$로 두면, $w\overline{z} + \overline{w}z \leq 2|w|\cdot|z|$이다. 따라서, $|z + w|^2 = (z + w)(\overline{z} + \overline{w})= z\overline{z} + w\overline{z} + \overline{w}z + w\overline{w}\leq |z|^2 + 2|z||w| + |w|^2 = (|z| + |w|)^2$이므로, $|z + w| \leq |z| + |w|$이다.
[^7]: $|z| = |(z + w)- w| \leq |z + w| + |-w| = |z + w| + |w|$이므로, $|z| - |w| \leq |z + w|$이다.