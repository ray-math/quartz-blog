---
title: 시간과 운동
date: 1999-01-01
---

> [!NOTE]
> https://plus.maths.org/content/time-and-motion
>
> A 지점의 모든 사람들이 B 지점으로 가고 싶어하게 만드는, B 지점의 그 놀라운 점은 무엇일까? Robert Hunt는 C 지점에 앉아 이 문제에 대해 사색한다.

![sunrise over earth](https://plus.maths.org/content/sites/default/files/styles/small_square/public/issue7/features/greatcircles/icon.jpg?itok=eRN0SatT)

![](https://plus.maths.org/issue7/features/greatcircles/concorde.jpg)

![그림 1: 파란색 경로?](https://plus.maths.org/issue7/features/greatcircles/merc.gif)

그림 1: 파란색 경로?

하지만 여행에서 속도만이 유일한 고려사항은 아니다. 선택한 경로가 최단 경로인지 확인하는 것도 중요하다. 당신이 콩코드 여객기를 조종해서 런던에서 샌프란시스코로 가야 하는데, 지도에서 경로를 선택해야 한다고 상상해보자. 파란색으로 표시된 직선 경로를 선택하겠는가, 아니면 노란색으로 표시된 긴 곡선 경로를 선택하겠는가? 놀랍게도 곡선 경로가 더 짧은 경로다!

![그림 2: 아니면 노란색?](https://plus.maths.org/issue7/features/greatcircles/ortho.gif)

그림 2: 아니면 노란색?

왜 그럴까? 지구는 평평하지 않지만 지도는 평평하기 때문에, 지도는 항상 왜곡되어 있다. 지구 위의 두 지점 사이의 최단 경로는 *대원(great circle)*의 일부를 따라간다. 대원이란 지구 전체를 한 바퀴 도는 큰 원으로, 지구의 중심이 이 원의 중심이 된다. 지구 그림을 보면 대원 경로(노란색)가 평면 지도에서 직선처럼 보였던 경로보다 왜 더 짧은지 알 수 있다. (노란색 선을 지구를 한 바퀴 도는 더 큰 원의 일부로 상상할 수 있다 - 또는 장난감 지구본을 보면서 스스로 확인할 수도 있다!)

일반적으로, 평평하지 않은 곡면 위에서 곡면 상의 두 점 사이를 있는 선 중 가능한 한 가장 짧은 선을 *측지선(geodesic)*이라고 부른다. 지구 위에서 모든 측지선은 대원의 일부다.

> 측지선은 곡면 기하학의 핵심 개념이다. 평면에서 두 점 사이의 최단 경로는 직선이지만, 곡면에서는 그 곡면의 고유한 기하학적 구조에 따라 최단 경로가 결정된다. 구면(sphere)에서는 대원이 측지선이 되고, 원기둥(cylinder)에서는 나선이 측지선이 될 수 있으며, 안장 모양의 쌍곡면(hyperboloid)에서는 더욱 복잡한 형태가 나타난다. 측지선의 개념은 미분기하학에서 리만 계량(Riemannian metric)을 통해 엄밀하게 정의되며, 일반상대성이론에서 시공간 내 물체의 운동 경로를 설명하는 데에도 사용된다. 지구 표면에서 비행기가 대원 경로를 따라 비행하는 것은, 곡면 위에서 자연스럽게 '직진'하는 것과 같은 의미다.

## 거리 계산하기

두 공항 사이의 대원 거리를 어떻게 계산할까? 항공사들이 비행기에 얼마나 많은 연료를 실어야 할지 알기 위해서는 거리를 아는 것이 중요하다! 경도와 위도 개념, 그리고 두 벡터의 스칼라곱(scalar product, 또는 내적 dot product이라고도 함)을 사용하면 쉽게 계산할 수 있다.

![그림 3: 위도와 경도](https://plus.maths.org/issue7/features/greatcircles/general.gif)

그림 3: 위도와 경도

지구 표면의 한 점 $P$를 생각해보자. 위도는 $\theta$(적도로부터 북쪽으로 측정)이고 경도는 $\phi$(그리니치 자오선으로부터 동쪽으로 측정)다. 지구가 반지름 $R$인 완전한 구라고 가정하자. 여기서 $R$은 약 6370 km다. (물론 지구가 정확히 구형이 아니라는 사실을 고려해서 계산하는 것도 가능하다.)

점 $P$의 $z$-좌표가 $R\sin\theta$라는 것은 쉽게 알 수 있다. 조금 더 생각해보면 $x$와 $y$ 좌표는 $(R\cos\theta)\cos\phi$와 $(R\cos\theta)\sin\phi$임을 알 수 있다. 따라서 지구 표면의 두 점에 대해, 지구 중심을 기준으로 한 위치 벡터는 다음과 같다:
$$
\mathbf{r}_{1} = \begin{pmatrix} R \cos \theta_{1} \cos \phi_{1} \\ R \cos \theta_{1} \sin \phi_{1} \\ R \sin \theta_{1} \end{pmatrix}
$$
그리고
$$
\mathbf{r}_{2} = \begin{pmatrix} R \cos \theta_{2} \cos \phi_{2} \\ R \cos \theta_{2} \sin \phi_{2} \\ R \sin \theta_{2} \end{pmatrix}
$$

> 구면좌표계(spherical coordinate system)에서 직교좌표계(Cartesian coordinate system)로의 변환을 이해하는 것이 중요하다. 위도 $\theta$는 적도면으로부터의 각도이므로, 높이 방향 성분은 $R\sin\theta$가 된다. 적도면에 투영된 점까지의 거리는 $R\cos\theta$가 되고, 이것을 다시 $x$-$y$ 평면에서 경도 $\phi$에 따라 분해하면 $x = (R\cos\theta)\cos\phi$, $y = (R\cos\theta)\sin\phi$가 된다. 이러한 좌표 변환은 지구과학, 천문학, 물리학 등 다양한 분야에서 구형 대칭성을 가진 문제를 다룰 때 기본이 되는 도구다.

따라서 내적을 계산할 수 있다:
$$
\mathbf{r}_{1} \cdot \mathbf{r}_{2} = R^{2}(\cos\theta_{1}\cos\theta_{2}(\cos\phi_{1}\cos\phi_{2}+\sin\phi_{1}\sin\phi_{2}) +\sin\theta_{1}\sin\theta_{2})
$$

하지만 내적에 대한 또 다른 공식이 있다:
$$
\mathbf{r}_{1} \cdot \mathbf{r}_{2} = |\mathbf{r}_{1}| |\mathbf{r}_{2}| \cos\alpha
$$
여기서 $\alpha$는 두 벡터 사이의 각이다. 따라서
$$
\alpha = \cos^{-1}\left(\frac{\mathbf{r}_{1} \cdot \mathbf{r}_{2}}{R^{2}}\right)
$$

이제 원의 호의 길이에 대한 잘 알려진 공식을 사용한다: 호의 길이는 $R\alpha$다. 단, $\alpha$를 라디안(radian)으로 측정해야 한다. 이제 우리는 대원 경로를 따른 거리를 알게 되었다!

> 이 계산의 핵심은 두 가지 내적 공식을 연결하는 것이다. 첫 번째 공식은 좌표 성분으로부터 직접 계산한 것이고, 두 번째 공식은 벡터의 기하학적 의미를 담고 있다. 두 위치 벡터가 모두 길이 $R$을 가지므로 $|\mathbf{r}_{1}| = |\mathbf{r}_{2}| = R$이고, 따라서 $\cos\alpha = \frac{\mathbf{r}_{1} \cdot \mathbf{r}_{2}}{R^{2}}$가 된다. 각 $\alpha$는 지구 중심에서 본 두 지점 사이의 중심각(central angle)이다. 구면 위의 호의 길이는 반지름에 중심각을 곱한 것이므로, 거리는 $d = R\alpha$가 된다. 이것이 바로 대원거리(great circle distance) 공식의 핵심이다. 삼각함수의 덧셈 공식을 사용하면 $\cos\alpha$를 더 간단하게 $\cos\theta_{1}\cos\theta_{2}\cos(\phi_{2}-\phi_{1}) + \sin\theta_{1}\sin\theta_{2}$로 표현할 수도 있는데, 이것이 흔히 사용되는 하버사인 공식(Haversine formula)의 기초가 된다.

![그림 4: 알파](https://plus.maths.org/issue7/features/greatcircles/vector-small.jpg)

그림 4: 알파

## 런던에서 샌프란시스코까지

![그림 5: LHR에서 SFO까지](https://plus.maths.org/issue7/features/greatcircles/polar.jpg)

그림 5: LHR에서 SFO까지

런던 히드로 공항의 위도는 북위 $51.3^{\circ}$이므로 $\theta_{1} = 51.3^{\circ}$이고, 경도는 서경 $0.3^{\circ}$이므로 $\phi_{1} = -0.3^{\circ}$이다. (히드로가 그리니치 자오선의 서쪽에 있기 때문에 음수다.) 샌프란시스코의 경우 $\theta_{2} = 37.5^{\circ}$이고 $\phi_{2} = -122.3^{\circ}$이다. 이 값들을 공식에 대입하면 $\alpha = 1.36$ 라디안이 나오고, 따라서 거리는 유효숫자 3자리로 8640 km다.

지도책에서 몇몇 장소들을 찾아보고 그들 사이의 거리를 계산해보라. 예를 들어, 당신의 고향에서 런던까지의 거리를 계산할 수 있다. 그냥 지도에서 측정한 거리와 많이 다른가? 모든 장소 쌍에 대해 같은 일이 일어날까?

실제로 비행기가 취하는 경로는 여러 가지 이유로 항상 대원 경로는 아니다. 다른 나라의 영공을 비행하는 것에 문제가 있을 수도 있다. 풍속과 풍향도 차이를 만든다: 유리한 뒷바람(tailwind)을 얻기 위해 대원 경로에서 벗어나는 것이 더 빠를 수 있다!

> 항공 내비게이션의 실제는 순수한 기하학적 최단 거리보다 훨씬 복잡하다. 제트 기류(jet stream)는 고도 약 10km에서 시속 200-400km로 흐르는 강한 바람인데, 이를 타면 연료 소비를 크게 줄일 수 있다. 예를 들어 태평양 횡단 노선에서 동쪽으로 가는 비행기는 제트 기류를 타기 위해 북쪽으로 우회하고, 서쪽으로 가는 비행기는 남쪽으로 우회한다. 또한 국제 항공 조약에 따라 일부 영공은 통과가 제한되거나 추가 비용이 발생하므로, 정치적 고려사항도 경로 선택에 영향을 미친다. 현대의 항공 교통 관제 시스템은 이 모든 요소들을 실시간으로 고려하여 최적의 경로를 계산한다.

당신만의 대원 경로를 그려보고 싶다면, [gc.kls2.com](http://gc.kls2.com/)에 멋진 페이지가 있다. 같은 사이트에는 이 주제에 대한 유용한 [도움말 파일](http://gc.kls2.com/faq.html)도 있다.

## 빛의 속도로 여행하기?

[아인슈타인(Einstein)](http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Einstein.html)의 상대성이론은 우리가 (또는 질량을 가진 다른 어떤 것이든!) 빛의 속도로 여행하는 것은 불가능하다고 말한다. 하지만 새 천년의 새벽에, 어떤 사람들은 - 어떤 방식으로든 - 시도하기로 결심했다!

2000년 1월 1일 새벽을 공식적으로 가장 먼저 볼 거주 지역은 태평양의 뉴질랜드 동쪽에 있는 핏 섬(Pitt Island)이다. 지구가 자전하면서, 태양은 서쪽으로 가면서 각 나라에서 차례로 떠오를 것이다. 일부 대담한 여행자들은 태평양에서 일출을 보고 나서 서쪽으로 딱 적절한 속도로 비행하여, 태양이 항상 그들 뒤의 지평선에서 막 떠오르도록 할 계획이다. 물론 그들은 실제로 빛의 속도로 여행하는 것은 아니지만, 그들이 있는 곳에서는 태양보다 앞서 가는 것처럼 보일 것이다! 그들에게는 24시간 동안 계속해서 밀레니엄의 새벽이 밝아오는 것이다.

![그림 6: 태평양 일출](https://plus.maths.org/issue7/features/greatcircles/fiji.jpg)

그림 6: 태평양 일출

이것을 달성하기 위해 얼마나 빨리 비행해야 할까? 다행히도 그것은 합리적인 속도로 밝혀진다! 만약 그들이 적도 주위를 비행한다면, 지구의 둘레인 $2\pi R$을 24시간 안에 여행해야 하는데, 이는 1670 km/hr (또는 464 m/s)의 속도가 된다. 이것은 음속보다 빠르지만, 콩코드라면 할 수 있다! 더 나은 아이디어는 둘레를 도는 것이 아니라 지구상의 더 작은 원을 따라, 일정한 위도를 유지하면서 여행하는 것이다. 그러면 초음속 비행기가 필요하지 않을 것이다. 그들에게 행운을 빈다!

> 이 문제는 각속도(angular velocity)와 선속도(linear velocity)의 관계를 보여주는 좋은 예다. 지구는 24시간에 $360^{\circ}$ 또는 $2\pi$ 라디안을 자전하므로, 각속도는 $\omega = \frac{2\pi}{24 \text{ hr}} = \frac{\pi}{12}$ rad/hr이다. 적도에서의 선속도는 $v = r\omega = R \cdot \frac{2\pi}{24}$가 된다. 하지만 위도 $\theta$에서는 회전 반지름이 $R\cos\theta$로 줄어들므로, 필요한 속도는 $v = R\cos\theta \cdot \frac{2\pi}{24}$가 된다. 예를 들어 위도 $60^{\circ}$에서는 $\cos 60^{\circ} = 0.5$이므로 필요한 속도가 절반으로 줄어들어 약 835 km/hr이 된다. 이는 보잉 747 같은 일반 여객기로도 충분히 달성 가능한 속도다. 실제로 2000년 새천년을 맞아 일부 항공사들은 이러한 '영구 일출' 비행 상품을 제공했다.

### 저자 소개

![](https://plus.maths.org/issue7/features/greatcircles/robert-credit.jpg)

[Dr. Robert Hunt](https://plus.maths.org/editorial/index.html#Robert)는 PASS Maths의 편집자다. 그는 [Cambridge University](http://www.cam.ac.uk)의 [Department of Applied Mathematics and Theoretical Physics](http://www.damtp.cam.ac.uk)에서 강사로 재직하고 있으며, [Christ's College](http://www.christs.cam.ac.uk)의 펠로우다.