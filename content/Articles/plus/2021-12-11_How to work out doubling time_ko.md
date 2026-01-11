---
title: 배가 시간(doubling time)을 계산하는 방법
date: 2021-12-11
tags:
  - 성장
  - 시간
  - 복리
  - 배가
  - JUNIPER
  - growth
  - Gog
  - rate
---

> [!NOTE]
> https://plus.maths.org/content/calculating-doubling-time
>
> 오미크론 변이의 배가 시간은 놀라울 정도로 빠른 것 같습니다. 하지만 이것을 어떻게 계산할까요?

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/sars-cov-2_frontpage.png?itok=IbGAWx2I)

COVID-19 팬데믹에 대한 모든 콘텐츠는 [여기](https://plus.maths.org/content/tags/covid-19)에서 확인하실 수 있습니다.

오미크론 변이의 출현과 더불어 많은 유럽 국가들에서 COVID-19 확진자 수가 급격히 증가하면서, 우리는 더 이상 다루지 않아도 되기를 바랐던 개념들을 다시 마주하게 되었습니다. 지수적 성장(exponential growth), 빠른 성장률(growth rate), 그리고 급속한 배가 시간(doubling time) 같은 것들 말입니다.

질병의 배가 시간은 확진자 수가 두 배가 되는 데 걸리는 시간을 의미합니다. 배가 시간은 질병의 성장률로부터 계산할 수 있지만, 이들의 관계는 처음 생각하는 것보다 조금 더 미묘합니다.

![SARS-Cov-2 바이러스](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/doubling/sars-cov-2.png)

과학적으로 정확한 SARS-CoV-2 바이러스의 원자 모델. 이미지: [Alexey Solodovnikov and Valeria Arkhipova](https://commons.wikimedia.org/wiki/File:Coronavirus._SARS-CoV-2.png), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

예를 들어, 성장률이 0.33인 경우(현재 남아프리카에서 대략 관찰되는 수치)를 생각해봅시다. 이 경우 확진자 수가 100% 증가하려면, 즉 두 배가 되려면 3일이 걸릴 것이라고 생각할 수 있습니다. 하지만 이것은 옳지 않습니다. 실제로 배가 시간은 훨씬 짧아서, 겨우 2일을 조금 넘을 뿐입니다. 이것은 본질적으로 복리(compound interest) 때문에 빚이 대출을 받을 때 생각했던 것보다 훨씬 빠르게 늘어나는 것과 같은 이유입니다.

> 성장률 0.33을 "33% 증가"로 직관적으로 해석하는 것은 자연스러워 보이지만, 이것이 틀린 이유는 바로 **연속 복리(continuous compounding)** 때문입니다. 은행 대출에서 복리 계산을 연 단위에서 월 단위, 일 단위로 세분화할수록 실제 이자가 더 빨리 불어나는 것처럼, 질병 확산도 연속적으로 일어나기 때문에 단순한 선형 계산보다 실제 증가 속도가 더 빠릅니다. 성장률 $\lambda = 0.33$은 "순간적인 변화율"을 의미하며, 이것이 하루 동안 축적되면 실제로는 약 39%의 증가로 나타나게 됩니다. 이 차이는 성장률이 클수록 더욱 극적으로 벌어지며, 이것이 왜 팬데믹 초기 단계에서 확진자 수가 예상보다 훨씬 빠르게 증가하는지를 설명합니다.

### 성장률(growth rate)에 대한 이해

질병의 *성장률*은 감염자 수가 날마다 얼마나 빠르게 변화하는지를 포착합니다. 이것은 지수 곡선을 사용하여 모델링됩니다:

$$
N(t) = c e^{\lambda t}
$$

여기서 $N$은 확진자 수이고, 이는 일(days) 단위로 측정된 시간 $t$에 의존합니다. $\lambda$(람다로 발음)는 하루당 질병의 *성장률*입니다. 수 $c$는 시간 $t=0$일 때의 확진자 수, 즉 미래를 예측하려고 하는 그 시점의 확진자 수입니다.

수 $e$는 대략 2.719에 해당하는 수학적 상수입니다. 이것이 여기에 등장하는 이유는 $e$가 연속적으로 복리 계산되는 성장과 본질적으로 연결되어 있기 때문입니다. 이에 대한 수학적 설명은 [여기](https://plus.maths.org/content/compound-infections)를, 성장률 개념에 대한 일반적인 설명은 [여기](https://plus.maths.org/content/epidemic-growth-rate)를 참고하세요.

> 자연 상수 $e$가 성장 모델에 등장하는 것은 우연이 아닙니다. $e$는 "연속 복리의 극한"으로 정의되는데, 이는 다음과 같이 이해할 수 있습니다. 만약 초기 금액 1원을 연이율 100%로 복리 계산한다고 할 때, 1년에 한 번 계산하면 2원이 되고, 반년에 한 번 계산하면 $(1 + 1/2)^{2} = 2.25$원이 되며, 매일 계산하면 $(1 + 1/365)^{365} \approx 2.714$원이 됩니다. 이 복리 계산 주기를 무한히 짧게 만들면 극한값으로 $e \approx 2.71828...$이 나타납니다. 질병 확산에서 감염은 연속적으로 일어나므로, 이산적인 날짜가 아니라 연속적인 시간에 대해 모델링할 때 자연스럽게 $e$가 나타나게 됩니다. 이것이 바로 $e^{\lambda t}$ 형태가 자연 현상의 성장을 기술하는 가장 자연스러운 방법인 이유입니다.

"성장률"이라는 용어를 처음 들으면, $\lambda$가 하루당 증가한 확진자 수를 나타낸다고 생각할 수 있습니다. 특히 이것이 백분율로도 표현될 수 있기 때문입니다. 하지만 이것은 정확하지 않습니다. 위의 공식에 따르면, 날마다의 증가량은 다음과 같습니다:

$$
N(t+1)-N(t) = c e^{\lambda (t+1)}-c e^{\lambda t}
$$

이것은 다음과 같이 단순화됩니다:

$$
c e^{\lambda t}\left(e^{\lambda}-1\right)
$$

이것을 $N(t)$에 대한 백분율로 표현하면:

$$
\frac{c e^{\lambda t}\left(e^{\lambda}-1\right)}{c e^{\lambda t}}\times 100 = 100(e^{\lambda}-1)
$$

$\lambda=0.33$인 우리의 예제로 돌아가면, 하루당 백분율 증가는 33%가 아니라:

$$
100(e^{0.33}-1)=39\%
$$

로, 상당히 더 높습니다. $\lambda$가 작을 때만(예를 들어 $\lambda \approx 0.1$ 정도), $\lambda$의 값 자체를 날마다의 증가량에 대한 추정치로 사용할 수 있습니다. 이는 이러한 작은 값에 대해서는 $\lambda$가 $e^{\lambda}-1$의 좋은 근사이기 때문입니다.

> 왜 $\lambda$가 작을 때만 $\lambda \approx e^{\lambda}-1$이 성립할까요? 이것은 **테일러 급수(Taylor series)** 전개로 이해할 수 있습니다. $e^{x}$를 $x=0$ 근처에서 급수 전개하면 $e^{x} = 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + ...$이 됩니다. 따라서 $e^{\lambda}-1 = \lambda + \frac{\lambda^{2}}{2!} + \frac{\lambda^{3}}{3!} + ...$입니다. $\lambda$가 작으면, 예를 들어 $\lambda = 0.1$이면, $\lambda^{2} = 0.01$, $\lambda^{3} = 0.001$ 등으로 급격히 작아지므로, 첫 번째 항 $\lambda$만으로도 충분히 정확한 근사가 됩니다. 하지만 $\lambda = 0.33$처럼 값이 크면, $\lambda^{2} = 0.11$, $\lambda^{3} = 0.036$ 등 고차항들이 무시할 수 없게 되어, 단순히 $\lambda$만 사용하면 실제 증가율을 과소평가하게 됩니다. 구체적으로 $\lambda = 0.1$일 때 $e^{0.1}-1 \approx 0.105$로 약 5% 오차이지만, $\lambda = 0.33$일 때는 $e^{0.33}-1 \approx 0.39$로 약 18%의 오차가 발생합니다.

### 성장률로부터 배가 시간 계산하기

이제 우리의 성장률 모델로부터 배가 시간을 계산해봅시다. 우리는 확진자 수가 두 배가 되는 데 걸리는 시간의 길이 $d$를 구하고자 합니다. 수학적으로, 우리는 다음 식에서 $d$를 풀어야 합니다:

$$
N(t+d)=2N(t)
$$

위의 공식을 사용하면, 다음 식에서 $d$를 풀어야 합니다:

$$
c e^{\lambda (t+d)}=2 c e^{\lambda t}
$$

방정식의 양변에 자연로그를 취하면:

$$
\ln{c}+\lambda (t+d) = \ln{2}+\ln{c}+\lambda t
$$

$d$에 대해 정리하면:

$$
d=\frac{\ln{2}}{\lambda}
$$

이것은 배가 시간 $d$가 성장률 $\lambda$에 어떻게 의존하는지를 알려줍니다. 다음은 이 관계의 그래프입니다. 배가 시간이 성장률에 대해 선형적으로 증가하지 않고, 오히려 $\lambda$가 증가함에 따라 상당히 극적으로 급락한다는 것을 보여줍니다.

![성장률에 따른 배가 시간](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2021/doubling_time/doubling.png)

우리가 계산한 공식으로 주어지는, 성장률에 따른 배가 시간.

> 배가 시간 공식 $d = \frac{\ln{2}}{\lambda}$가 갖는 직관적 의미를 살펴봅시다. 먼저, 이 공식은 $d$와 $\lambda$가 **반비례 관계**라는 것을 보여줍니다. 성장률이 두 배가 되면 배가 시간은 절반이 됩니다. $\ln{2} \approx 0.693$은 고정된 상수로, "두 배"라는 목표를 나타냅니다. 만약 세 배가 되는 시간을 구하고 싶다면 $\ln{3}/\lambda$를 계산하면 됩니다. 이 공식의 우아함은 시간 $t$에 독립적이라는 점입니다. 즉, 지수 성장에서는 언제 측정을 시작하든 배가 시간은 항상 같습니다. 이것이 바로 지수 성장의 무서운 점입니다. 초기에는 느리게 보이지만, 배가 시간이 일정하게 유지되면서 결국 폭발적으로 증가하게 됩니다. 예를 들어, $\lambda = 0.1$이면 $d \approx 6.93$일로 약 일주일마다 두 배가 되지만, $\lambda = 0.5$이면 $d \approx 1.39$일로 하루 반마다 두 배가 되어, 일주일이면 약 $2^{5} = 32$배가 됩니다.

위의 예제로 돌아가서, 성장률 $\lambda=0.33$에 대해, 우리의 공식은 대응하는 배가 시간이 다음과 같다고 알려줍니다:

$$
d=\frac{\ln{2}}{0.33} = 2.1
$$

이는 우리가 주장했던 것처럼 2일을 조금 넘습니다.

> 이 결과가 얼마나 놀라운지 다시 한 번 강조해봅시다. 성장률 0.33, 즉 33%라는 수치를 들으면, 직관적으로 "3일 정도면 100% 증가, 즉 두 배가 되겠구나"라고 생각하기 쉽습니다. 하지만 실제로는 2.1일만에 두 배가 됩니다. 이 약 30%의 차이는 짧은 기간에는 작아 보이지만, 누적되면 엄청난 차이를 만듭니다. 예를 들어, 한 달(30일) 동안 배가 시간을 3일로 잘못 예측하면 약 $2^{10} = 1024$배 증가를 예상하게 되지만, 실제 배가 시간 2.1일로는 약 $2^{14} = 16384$배 증가하게 됩니다. 즉, 실제 증가량이 예측보다 약 16배나 더 많습니다. 이것이 바로 팬데믹 대응에서 정확한 수학적 모델링이 필수적인 이유입니다.

### 이 글에 관하여

[Marianne Freiberger](https://plus.maths.org/content/people/index.html#marianne)는 *Plus*의 편집자입니다. 이 글은 Cambridge 대학교의 수리생물학(Mathematical Biology) 교수인 [Julia Gog](https://www.infectiousdisease.cam.ac.uk/directory/jrg20@cam.ac.uk)와 함께, [JUNIPER](https://maths.org/juniper/)(Joint UNIversity Pandemic and Epidemic Response modelling consortium)와의 협업의 일환으로 제작되었습니다. JUNIPER는 Cambridge, Warwick, Bristol, Exeter, Oxford, Manchester, Lancaster 대학의 학자들로 구성되어 있으며, COVID-19 통제에 관한 긴급한 문제들을 다루기 위해 다양한 수학적 및 통계적 기법을 사용하고 있습니다. JUNIPER와 함께 제작된 더 많은 콘텐츠는 [여기](https://plus.maths.org/content/juniper)에서 볼 수 있습니다.

Gog는 또한 [과학자문그룹(SAGE, Scientific Advisory Group for Emergencies)](https://www.gov.uk/government/groups/scientific-advisory-group-for-emergencies-sage-coronavirus-covid-19-response)에 결과를 제공하는 모델링 그룹인 SPI-M의 회원이며, COVID-19 팬데믹에 대응하기 위해 Royal Society가 주도하는 [국가 컨소시엄](https://epcced.github.io/ramp/)의 운영위원회 회원이기도 합니다.

![Juniper 로고](https://plus.maths.org/content/sites/plus.maths.org/files/packages/2021/Juniper-logos/juniper-light-bg.png)