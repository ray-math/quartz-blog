---
title: Madhava
---

> [!NOTE]
> https://mathshistory.st-andrews.ac.uk/Biographies/Madhava/
>
> Madhava는 남인도 출신의 수학자이다. 그는 삼각함수의 급수 전개를 발견하는 등 무한급수에서 중요한 발전을 이루었다.

**출생**: 1350년 인도 케랄라주 상가마그라마 (코친 인근)

**사망**: 1425년 인도

---

**요약**: Madhava는 남인도 출신의 수학자이다. 그는 삼각함수의 급수 전개를 발견하는 등 무한급수에서 중요한 발전을 이루었다.

인도

**Madhava**는 남인도 출신의 수학자이다. 그는 삼각함수의 급수 전개를 발견하는 등 무한급수에서 중요한 발전을 이루었다.

### 생애

**상가마그라마의 Madhava**는 인도 남서부 케랄라주의 해안 도시 코친 근처에서 태어났다. 지난 25년간 케랄라 수학에 대한 연구가 이루어진 덕분에 Madhava의 놀라운 업적이 비로소 세상에 알려지게 되었다. [10]에서 Rajagopal과 Rangachari는 그의 업적을 다음과 같이 평가한다:

> [Madhava는] 고대 수학의 유한한 절차에서 무한으로의 극한 과정을 다루는 결정적인 단계를 내딛었으며, 이것이 바로 현대 고전 해석학의 핵심이다.

Madhava의 수학 저작은 모두 소실되었지만, 천문학에 관한 일부 저작은 현존한다. 그러나 그의 뛰어난 수학 연구는 약 100년 후에 살았던 [Nilakantha](https://mathshistory.st-andrews.ac.uk/Nilakantha/)와 같은 케랄라의 다른 수학자들의 기록을 통해 대부분 밝혀졌다.

Madhava는 1400년경 sin(x), cos(x), arctan(x)의 [Maclaurin](https://mathshistory.st-andrews.ac.uk/Maclaurin/) 급수 전개와 동등한 급수를 발견했는데, 이는 유럽에서 재발견되기 200년 이상 앞선 것이다. 구체적인 내용은 그의 후학들이 쓴 여러 저작에 나타나는데, 그 중 하나가 *Mahajyanayana prakara*로 *대정현을 계산하는 방법*이라는 뜻이다. 사실 이 저작은 Sarma와 같은 일부 역사가들([2] 참조)에 의해 Madhava 본인의 것으로 주장되기도 했으나, 이는 매우 가능성이 낮으며 현재 대부분의 역사가들은 이를 16세기 Madhava의 후학이 쓴 것으로 받아들인다. 이에 대한 자세한 논의는 [4]에 나와 있다.

[Jyesthadeva](https://mathshistory.st-andrews.ac.uk/Jyesthadeva/)는 1550년경 케랄라의 지역 언어인 말라얄람어로 *Yukti-Bhasa*를 저술했다. [9]에서 Gupta는 이 문헌의 번역을 제공하며, 이는 [2]와 다른 여러 문헌에도 수록되어 있다.

[Jyesthadeva](https://mathshistory.st-andrews.ac.uk/Jyesthadeva/)는 Madhava의 급수를 다음과 같이 설명한다:

> 첫 번째 항은 주어진 정현과 원하는 호의 반지름의 곱을 호의 코사인으로 나눈 것이다. 이어지는 항들은 첫 번째 항에 정현의 제곱을 반복적으로 곱하고 코사인의 제곱으로 나누는 반복 과정을 통해 얻어진다. 모든 항들은 홀수 1, 3, 5, ...로 나누어진다. 호는 홀수 번째 항들을 더하고 짝수 번째 항들을 빼서 얻어진다. 여기서 주어진 정현으로는 호의 정현 또는 그 여각의 정현 중 더 작은 것을 취해야 한다고 규정되어 있다. 그렇지 않으면 위의 반복으로 얻어진 항들이 소멸하는 크기로 수렴하지 않을 것이다.

이것은 Madhava의 급수를 설명하는 놀라운 구절이지만, [Jyesthadeva](https://mathshistory.st-andrews.ac.uk/Jyesthadeva/)의 이 구절조차 [James Gregory](https://mathshistory.st-andrews.ac.uk/Gregory/)가 이 급수 전개를 재발견하기 100년 이상 전에 쓰여졌다는 점을 기억해야 한다. Madhava가 발견한 급수가 정확히 무엇인지 현대 기호로 표현해 보자. 먼저 주목할 점은 인도에서 θ의 정현(sine)은 우리의 표기법으로 $r\sin\theta$로 쓰일 것이고, θ의 코사인(cosine)은 우리의 표기법으로 $r\cos\theta$가 될 것이며, 여기서 $r$은 반지름이다. 따라서 이 급수는

$$
\theta = \frac{r\sin\theta}{r\cos\theta} - \frac{(r\sin\theta)^{3}}{3(r\cos\theta)^{3}} + \frac{(r\sin\theta)^{5}}{5(r\cos\theta)^{5}} - \cdots
$$

$r = 1$을 대입하고 정리하면

$$
\theta = \tan\theta - \frac{\tan^{3}\theta}{3} + \frac{\tan^{5}\theta}{5} - \cdots
$$

이는 [Gregory](https://mathshistory.st-andrews.ac.uk/Gregory/)의 급수

$$
\arctan x = x - \frac{x^{3}}{3} + \frac{x^{5}}{5} - \cdots
$$

와 동등하다.

이제 Madhava는 그의 급수에 $\theta = \frac{\pi}{4}$를 대입하여

$$
\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots
$$

를 얻었고, 또한 $\theta = \frac{\pi}{6}$을 대입하여

$$
\frac{\pi}{6} = \frac{1}{\sqrt{3}}\left(1 - \frac{1}{3 \cdot 3} + \frac{1}{5 \cdot 3^{2}} - \frac{1}{7 \cdot 3^{3}} + \cdots\right)
$$

를 얻었다.

Madhava가 소수점 이하 11자리까지 정확한 π의 근삿값을 구했다는 것을 알고 있는데, 그는

$$
\pi = 3.14159265359
$$

를 제시했으며, 이는 위의 Madhava 급수에서 21개 항을 취하여 얻을 수 있다. [5]에서 Gupta는 Madhava의 소수점 이하 11자리까지 정확한 π 근삿값을 제시한 산스크리트 문헌의 번역을 제공한다.

아마도 더욱 인상적인 것은 Madhava가 급수의 나머지 항을 제시하여 근삿값을 개선했다는 사실이다. 그는 보정항(correction term)을 더하여 $\frac{\pi}{4}$ 급수의 근삿값을 개선했다:

$$
\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \cdots \pm \frac{1}{n} + \frac{R_{n}}{n}
$$

Madhava는 근삿값을 개선하는 세 가지 형태의 $R_{n}$을 제시했는데, 즉

$$
R_{n} = \frac{1}{2}
$$

또는

$$
R_{n} = \frac{1}{2} - \frac{1}{4n}
$$

또는

$$
R_{n} = \frac{(n/2)^{2} + 1}{(n/2)^{2} + 2 + (n/4)}
$$

이다.

Madhava가 어떻게 보정항을 찾았는지 재구성하려는 많은 연구가 이루어졌다. 가장 설득력 있는 설명은 이들이 연분수(continued fraction)의 처음 세 수렴값(convergent)으로부터 나온다는 것이며, 이 연분수 자체는 표준적인 인도의 π 근삿값인 $\frac{355}{113}$로부터 유도될 수 있다.

Madhava는 또한 주어진 원의 사분원에서 같은 간격으로 그려진 24개의 호에 대한 거의 정확한 반정현현(half-sine chord) 값의 표를 제시했다. 그가 이러한 매우 정확한 표를 구한 방법은 다음의 급수 전개와 동등한 것을 사용했을 것으로 생각된다:

$$
\sin x = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \cdots
$$

$$
\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \cdots
$$

[Jyesthadeva](https://mathshistory.st-andrews.ac.uk/Jyesthadeva/)는 *Yukti-Bhasa*에서 Madhava가 1400년경 그의 급수 전개를 어떻게 찾았는지 설명했으며, 이는 1676년경 [Newton](https://mathshistory.st-andrews.ac.uk/Newton/)에 의해 재발견된 현대적 버전들과 동등하다. 역사가들은 Madhava가 사용한 방법이 항별 적분(term by term integration)에 해당한다고 주장해왔다.

Madhava가 현대 고전 해석학으로 나아가는 결정적인 단계를 내딛었다는 Rajagopal의 주장은 그의 놀라운 업적을 고려할 때 매우 타당해 보인다. 같은 맥락에서 Joseph은 [1]에서 다음과 같이 쓴다:

> 우리는 Madhava를 수리 해석학의 창시자로 간주할 수 있다. 이 분야에서의 그의 발견들 중 일부는 그가 비범한 직관력을 소유했음을 보여주며, 그를 Madhava의 출생지에서 멀지 않은 쿰바코남에서 어린 시절과 청년 시절을 보낸 더 최근의 직관적 천재 [Srinivasa Ramanujan](https://mathshistory.st-andrews.ac.uk/Ramanujan/)과 거의 동등한 수준으로 만든다.

### References ([show](https://mathshistory.st-andrews.ac.uk))

- G G Joseph,
*The crest of the peacock*(London, 1991).

 - K V Sarma,
*A History of the Kerala School of Hindu Astronomy*(Hoshiarpur, 1972).

 - A K Bag, Madhava's sine and cosine series,
*Indian J. History Sci.***11**(1) (1976), 54-57.

 - D Gold and D Pingree, A hitherto unknown Sanskrit work concerning Madhava's derivation of the power series for sine and cosine,
*Historia Sci. No.***42**(1991), 49-65.

 - R C Gupta, Madhava's and other medieval Indian values of pi,
*Math. Education***9**(3) (1975), B45-B48.

 - R C Gupta, Madhava's power series computation of the sine,
*Ganita***27**(1-2) (1976), 19-24.

 - R C Gupta, Madhava's rule for finding angle between the ecliptic and the horizon and Aryabhata's knowledge of it, in
*History of oriental astronomy, New Delhi, 1985*(Cambridge, 1987), 197-202.

 - R C Gupta, On the remainder term in the Madhava-Leibniz's series,
*Ganita Bharati***14**(1-4) (1992), 68-71.

 - R C Gupta, The Madhava-Gregory series,
*Math. Education***7**(1973), B67-B70.

 - T Hayashi, T Kusuba and M Yano, The correction of the Madhava series for the circumference of a circle,
*Centaurus***33**(2-3) (1990), 149-174.

 - C T Rajagopal and M S Rangachari, On an untapped source of medieval Keralese mathematics,
*Arch. History Exact Sci.***18**(1978), 89-102.

 - C T Rajagopal and M S Rangachari, On medieval Keralese mathematics,
*Arch. History Exact Sci.***35**(1986), 91-99.
