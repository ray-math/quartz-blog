---
title: 표지 이야기 - 조립이 필요합니다
date: 2022-11-09
tags:
  - 사용
  - 수학
  - 코흐
  - Ness
  - Rock
  - Koch
  - BBC
  - 눈송이
---

> [!NOTE]
> https://chalkdustmagazine.com/regulars/on-the-cover/on-the-cover-some-assembly-required/
>
> 16호 표지에 실린 Sam Palmer의 작품에서 느껴지는 황홀한 뇌 마사지

Sam Palmer는 수학적 디지털 아트 작가로, 그의 작품을 [트위터](https://chalkdustmagazine.com/twitter.com/sjpalmer1994), [레딧](https://chalkdustmagazine.com/reddit.com/user/sjpalmer94), 그리고 자신의 [웹사이트](https://chalkdustmagazine.com/sjpalmer.art)를 통해 공유하고 있다. 그는 오픈소스 스케칭 소프트웨어인 [Processing](https://processing.org/)을 사용하여 아름다운 기하학적 주제를 담은 정적 이미지와 애니메이션 그래픽을 모두 생성한다. 많은 사람들이 그의 작품을 아름답다고 생각하지만, 일부 사람들은 그의 gif 애니메이션 중 몇몇이 다소 불안하게 느껴진다고 한다:

![레딧 댓글: "이거 완전 몽환적이야, 너무 좋아" 그리고 "마치 뇌 마사지 같아"](https://i0.wp.com/chalkdustmagazine.com/wp-content/uploads/2022/11/Screenshot1.png?resize=300%2C204&ssl=1)

![레딧 댓글: "실례지만, 제 눈에 그런 짓 좀 하지 마세요" 그리고 "옷장에 가서 토해야겠어"](https://i0.wp.com/chalkdustmagazine.com/wp-content/uploads/2022/11/Screenshot2.png?resize=300%2C210&ssl=1)

Chalkdust 16호의 표지 작품은 특히 떨어지는 코흐 눈송이(Koch snowflake)들의 전환 애니메이션에서 영감을 받아 제작되었으며, *Some assembly required(조립이 필요합니다)*라는 제목이 붙었다:

![](https://i0.wp.com/sjpalmer1994-art.s3.eu-west-2.amazonaws.com/some_assembly_required_thumbnail.gif?w=654&ssl=1)

> 코흐 눈송이는 스웨덴의 수학자 헬게 폰 코흐(Helge von Koch)가 1904년에 고안한 프랙탈 곡선이다. 이 도형이 특별한 이유는 우리의 직관에 완전히 반하는 성질을 가지고 있기 때문이다. 둘레는 무한히 길지만 넓이는 유한하다는 것이다. 이는 각 반복 단계에서 둘레가 $\frac{4}{3}$배씩 증가하여 무한대로 발산하는 반면, 넓이는 기하급수적으로 수렴하기 때문이다. 구체적으로, 초기 정삼각형의 넓이를 $A$라 할 때, 최종 눈송이의 넓이는 $\frac{8A}{5}$로 수렴한다. 이러한 역설적 성질은 19세기 말부터 20세기 초에 걸쳐 수학자들이 연속이지만 미분불가능한 함수의 존재를 증명하려 했던 노력의 일환으로 탄생했다.

코흐 눈송이는 특히 아름다운 유명한 도형이며, *프랙탈(fractal)*로 알려진 수학적 대상들의 한 예시다. 프랙탈은 자기유사성(self-similarity)을 가진 대상으로, 정수가 아닌 차원(non-integer dimension)을 포함한 정말 흥미로운 수학적 성질들을 갖는다. 코흐 눈송이라는 특정 예시의 경우, 이 도형은 무한한 둘레를 가지지만 유한한 넓이를 갖는다. 다른 유명한 프랙탈로는 시에르핀스키 삼각형(Sierpinski's triangle), 멩거 스펀지(Menger sponge), 그리고 망델브로 집합(Mandelbrot set) 등이 있다.

> 자기유사성이란 대상의 일부를 확대했을 때 전체와 동일하거나 매우 유사한 구조가 반복되는 성질을 말한다. 이는 프랙탈의 가장 핵심적인 특징으로, 어느 배율로 관찰하든 비슷한 패턴이 나타난다. 프랙탈 차원(fractal dimension)은 하우스도르프 차원(Hausdorff dimension)으로 정의되며, 코흐 눈송이의 경우 $\frac{\log 4}{\log 3} \approx 1.26186$이다. 이는 1차원(선)과 2차원(면) 사이의 값으로, 이 곡선이 선보다는 '두껍지만' 면만큼 공간을 채우지는 못한다는 직관적 의미를 담고 있다. 자연계에서도 해안선, 나뭇가지, 구름, 혈관 등이 프랙탈 구조를 보이는데, 이는 제한된 자원으로 표면적이나 접근성을 극대화하는 효율적인 구조이기 때문이다.

코흐 눈송이 도형은 정삼각형에서 시작하여, 도형의 각 변의 중간에 더 작은 정삼각형들(정확히 말하면 이전에 추가된 삼각형 넓이의 $\frac{1}{9}$)을 추가하는 방식으로 반복적으로 구성된다:

![코흐 눈송이 생성 과정](https://i0.wp.com/chalkdustmagazine.com/wp-content/uploads/2022/11/otc-5.png?resize=654%2C134&ssl=1)

> 코흐 눈송이의 구성 과정을 더 정확히 설명하면 다음과 같다. 각 변을 3등분한 후, 가운데 부분을 한 변으로 하는 정삼각형을 바깥쪽으로 돌출시키고 원래의 가운데 부분은 제거한다. 이렇게 하면 하나의 직선 변이 네 개의 더 짧은 변(각각 원래 길이의 $\frac{1}{3}$)으로 바뀐다. 따라서 각 반복 단계마다 변의 개수는 4배가 되고 각 변의 길이는 $\frac{1}{3}$이 되므로, 전체 둘레는 $\frac{4}{3}$배씩 증가한다. 초기 삼각형의 둘레를 $L$이라 하면, $n$번 반복 후 둘레는 $L \cdot (\frac{4}{3})^{n}$이 되어 $n \to \infty$일 때 무한대로 발산한다. 반면 넓이는 각 단계에서 이전에 추가된 삼각형들의 $\frac{1}{9}$ 크기의 삼각형들이 추가되는 기하급수로, 유한한 값으로 수렴한다.

이 소프트웨어를 직접 사용해보고 싶은가? Processing 프로그래밍 언어는 Java를 기반으로 하며, 처음 실행하면 훌륭한 [튜토리얼](https://necessarydisorder.wordpress.com/2018/07/02/getting-started-with-making-processing-gifs-and-using-the-beesandbombs-template/)과 템플릿으로 연결되는 링크들이 있다. [Windows, MacOS, Linux](https://processing.org/download) 모두에서 사용 가능하므로, 시도하지 않을 이유가 없다.

> Processing은 2001년 MIT 미디어 랩에서 벤 프라이(Ben Fry)와 케이시 리스(Casey Reas)에 의해 개발되었다. 원래는 비프로그래머들, 특히 디자이너와 예술가들이 코딩을 배우고 시각적 작품을 만들 수 있도록 돕기 위해 만들어진 교육용 도구였다. Java의 복잡성을 단순화하고 시각적 피드백을 즉각적으로 제공함으로써, 수학적 아이디어를 시각화하는 데 이상적인 환경을 제공한다. 특히 `setup()`과 `draw()` 함수의 구조는 초기 설정과 프레임별 애니메이션을 명확히 분리하여, 프랙탈과 같은 반복적 구조를 구현하는 데 매우 직관적이다. 생성 예술(generative art)과 크리에이티브 코딩(creative coding) 커뮤니티에서 널리 사용되며, 수많은 예제와 라이브러리가 공개되어 있어 초보자도 쉽게 시작할 수 있다.

당신의 작품에 제목이 필요한가? *The Koch Ness Monster(코흐 네스 몬스터)*, *Kochodile Rock(코코다일 록)* 또는 *BBC News at Ten O'Koch(BBC 10시 뉴스)*는 어떨까?

> 이 제목들은 모두 영어 발음의 유희를 활용한 말장난이다. "Koch"의 발음이 "Loch(호수)"나 "croc(악어)", "o'clock(시각)"과 유사하다는 점을 이용한 것이다. The Loch Ness Monster(네스호의 괴물), Crocodile Rock(엘튼 존의 유명한 노래), BBC News at Ten O'Clock(BBC의 대표적인 저녁 뉴스 프로그램)을 각각 패러디한 것으로, 수학적 개념에 친근하고 유머러스한 이름을 붙여 대중과의 거리를 좁히려는 시도다. 실제로 수학 커뮤니티에서는 이러한 말장난이 자주 사용되며, 딱딱한 수학적 개념을 기억하기 쉽고 재미있게 만드는 효과적인 방법으로 여겨진다.