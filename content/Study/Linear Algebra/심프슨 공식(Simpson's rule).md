---
title: 심프슨 공식(Simpson's rule)
date: 2025-02-15
---
## 라그랑주 다항식의 적분
주어진 다항식 $p(x)$를 라그랑주 기저 다항식 $p_i(x)$로 전개한 후
$$
p(x) = \sum_{i=0}^{n} p(c_i) p_i(x)
$$

양변을 $a$부터 $b$까지 적분하면

$$
\int_a^b p(t) dt = \int_a^b \sum_{i=0}^{n} p(c_i) p_i(t) dt
$$

선형성을 이용하여 적분 기호를 분리할 수 있습니다.

$$
\int_a^b p(t) dt = \sum_{i=0}^{n} p(c_i) \int_a^b p_i(t) dt
$$

여기서 $d_i$를 다음과 같이 정의하면

$$
d_i = \int_a^b p_i(t) dt
$$

정적분을 라그랑주 다항식의 적분으로 표현한 결과는 다음과 같이 정리됩니다.

$$
\int_a^b p(t) dt = \sum_{i=0}^{n} p(c_i) d_i
$$
---
이때, $d_i$는 라그랑주 다항식 $p_i(x)$의 적분 값으로 각 점 $c_i$에서의 함수 값 $p(c_i)$에 대한 가중치 역할을 하며, 적절한 $c_i$ 선택에 따라 적분 공식이 다르게 유도됩니다.

## 특정한 $c_i$ 선택에 따른 적분 공식
구간 $[a, b]$를 $n$개의 등간격으로 나누어 $c_i$를 설정하면 다음과 같습니다.

$$
c_i = a + \frac{i(b-a)}{n} \quad (i = 0, 1, \cdots, n)
$$

### $n=1$

1. 주어진 식에서 $n=1$이면 $c_0 = a, c_1 = b$입니다.  
  $$
  \int_a^b p(t) dt = p(c_0) d_0 + p(c_1) d_1
  $$

2. $d_0, d_1$ 값 찾기
임의의 다항식 $p(x)$**에 대해 적분 공식이 항상 성립해야 하므로, 기저 함수 $p(x)$를 적절히 선택**하여 $d_0, d_1$을 결정할 수 있습니다.

**(1) $p(x) = 1$을 대입**
$$
\int_a^b 1 \,dx = b-a
$$
이므로,
$$
p(a) d_0 + p(b) d_1 = 1 \cdot d_0 + 1 \cdot d_1 = b-a
$$

즉,

$$
d_0 + d_1 = b-a.
$$

---

**(2) $p(x) = x$을 대입**
$$
\int_a^b x \,dx = \frac{b^2 - a^2}{2}
$$

이므로,

$$
a d_0 + b d_1 = \frac{b^2 - a^2}{2}.
$$

이를 연립방정식으로 정리하면

$$
\begin{cases}
d_0 + d_1 = b-a \\
a d_0 + b d_1 = \frac{b^2 - a^2}{2}
\end{cases}
$$

입니다.

3. 연립방정식 풀이
식을 정리하면,
$$
d_0 = \frac{(b-a)^2}{2(a-b)} = \frac{b-a}{2}
$$

이고, 마찬가지로,

$$
d_1 = b-a - d_0 = b-a - \frac{b-a}{2} = \frac{b-a}{2}.
$$

입니다.

4. 적분 공식에 대입
$$
d_0 = \frac{b-a}{2}, \quad d_1 = \frac{b-a}{2}
$$

를 적분 공식에 대입하면

$$
\begin{align*}
\int_a^b p(t) dt &= \frac{b-a}{2} p(a) + \frac{b-a}{2} p(b)\\
&= \frac{b-a}{2} \left( p(a) + p(b) \right)
\end{align*}
$$
이며, 이것은 사다리꼴의 넓이 공식(Trapezoidal Rule)과 일치합니다.

### $n=2$
1. 등간격 분할
$n=2$일 때의 경우도 살펴보겠습니다.  앞선 방법과 마찬가지로,  
$$
  c_0 = a, \quad c_1 = a + \frac{b-a}{2}, \quad c_2 = b.
  $$

세 개의 점을 사용하여 적분을 근사하겠습니다. 
  
$$
  \int_a^b p(t) dt = p(c_0) d_0 + p(c_1) d_1 + p(c_2) d_2
  $$



2. $d_0, d_1, d_2$ 찾기
**(1) $p(x) = 1$을 대입**
$$
\int_a^b 1 \,dx = b-a.
$$

즉,

$$
d_0 + d_1 + d_2 = b-a.
$$

**(2) $p(x) = x$을 대입**
$$
\int_a^b x \,dx = \frac{b^2 - a^2}{2}
$$

즉,

$$
a d_0 + \left(a + \frac{b-a}{2} \right) d_1 + b d_2 = \frac{b^2 - a^2}{2}
$$

**(3) $p(x) = x^2$을 대입**
$$
\int_a^b x^2 \,dx = \frac{b^3 - a^3}{3}
$$

즉,

$$
a^2 d_0 + \left( a + \frac{b-a}{2} \right)^2 d_1 + b^2 d_2 = \frac{b^3 - a^3}{3}
$$

이며, 위 세 개의 식을 풀면, 다음과 같은 가중치가 나옵니다.

$$
d_0 = \frac{b-a}{6}, \quad d_1 = \frac{4(b-a)}{6}, \quad d_2 = \frac{b-a}{6}
$$

3. 최종 적분 공식
이제 $d_0, d_1, d_2$를 원래 식에 대입하면

$$
\begin{align*}
\int_a^b p(t) dt &= \frac{b-a}{6} p(a) + \frac{4(b-a)}{6} p \left( \frac{a+b}{2} \right) + \frac{b-a}{6} p(b)\\
&= \frac{b-a}{6} \left[ p(a) + 4p \left( \frac{a+b}{2} \right) + p(b) \right]
\end{align*}
$$

입니다. 이 식은 흔히 심프슨 1/3 공식(Simpson's 1/3 Rule)이라 불립니다!

### 더 많은 점으로 분할하면
같은 방법으로, $n=3$일 때는,

$$
\int_a^b p(x) dx \approx \frac{3h}{8} \left[ p(a) + 3p(a+h) + 3p(a+2h) + p(b) \right]
$$

와 같습니다.

$p(x)$의 차수가 $n$과 같으면 이 식은 등식이 성립하지만, $p(x)$의 차수가 $n$보다 크다면 오차가 발생합니다. 물론 $n$이 증가할 수록 정확도가 증가하지만, 너무 높은 차수를 사용하면 오차가 커질 수(Runge's phenomenon) 있습니다.[^1] 

## 가중치의 대칭성
눈치가 빠르신 분들은 가중치 $d_i$가 **좌우 대칭**이 된다는 것을 아셨을 것입니다. 이러한 대칭성은 라그랑주 다항식의 적분을 통해 유도할 수 있습니다.

가중치 $d_i$는 **보간 다항식 $p_i(x)$의 적분 값**으로 정의됩니다:

$$
w_i = \int_a^b p_i(x) dx.
$$

여기서 $p_i(x)$는 **라그랑주 다항식**(Lagrange basis polynomial)이고,

$$
p_i(x) = \prod_{\substack{j=0 \\ j\neq i}}^n \frac{x - x_j}{x_i - x_j}.
$$
보간 다항식은 **등간격으로 나눠진 점 $x_0, x_1, \dots, x_n$에서 구성되므로, 항상 대칭성을 가집니다.

$$
\begin{array}{c|ccccccccccc}
n & w_0 & w_1 & w_2 & w_3 & w_4 & w_5 & w_6 & w_7 & w_8 & w_9 & w_{10} \\
\hline
1 & \frac{1}{2} & \frac{1}{2} & & & & & & & & & \\
2 & \frac{1}{6} & \frac{4}{6} & \frac{1}{6} & & & & & & & & \\
3 & \frac{3}{8} & \frac{9}{8} & \frac{9}{8} & \frac{3}{8} & & & & & & & \\
4 & \frac{7}{90} & \frac{32}{90} & \frac{12}{90} & \frac{32}{90} & \frac{7}{90} & & & & & & \\
5 & \frac{19}{288} & \frac{75}{288} & \frac{50}{288} & \frac{50}{288} & \frac{75}{288} & \frac{19}{288} & & & & & \\
6 & \frac{41}{840} & \frac{216}{840} & \frac{27}{840} & \frac{272}{840} & \frac{27}{840} & \frac{216}{840} & \frac{41}{840} & & & & \\
7 & \frac{751}{17280} & \frac{3577}{17280} & \frac{1323}{17280} & \frac{2989}{17280} & \frac{2989}{17280} & \frac{1323}{17280} & \frac{3577}{17280} & \frac{751}{17280} & & & \\
8 & \frac{989}{28350} & \frac{5888}{28350} & -\frac{928}{28350} & \frac{10496}{28350} & -\frac{4540}{28350} & \frac{10496}{28350} & -\frac{928}{28350} & \frac{5888}{28350} & \frac{989}{28350} & & \\
9 & \frac{2857}{89600} & \frac{15741}{89600} & \frac{1080}{89600} & \frac{19344}{89600} & \frac{5778}{89600} & \frac{5778}{89600} & \frac{19344}{89600} & \frac{1080}{89600} & \frac{15741}{89600} & \frac{2857}{89600} & \\
10 & \frac{16067}{598752} & \frac{106300}{598752} & -\frac{48525}{598752} & \frac{272400}{598752} & -\frac{260550}{598752} & \frac{427368}{598752} & -\frac{260550}{598752} & \frac{272400}{598752} & -\frac{48525}{598752} & \frac{106300}{598752} & \frac{16067}{598752} \\
\end{array}
$$

[^1]: Runge, C. (1901). "Über empirische Funktionen und die Interpolation zwischen äquidistanten Ordinaten". Zeitschrift für Mathematik und Physik. 46: 224–243.