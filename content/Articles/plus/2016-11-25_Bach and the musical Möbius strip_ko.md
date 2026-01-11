---
title: 바흐와 음악적 뫼비우스 띠
date: 2016-11-25
tags:
  - 카논
  - Tony
  - 성부
  - Phill
  - Bach
  - 악보
  - Eric
  - 바흐
---

> [!NOTE]
> https://plus.maths.org/content/topology-music-m-bius-strip
>
> 바흐의 유명한 카논 속에 숨어 있는 뫼비우스 띠를 발견하고 들어보세요.

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/mobius_frontpage.jpg?itok=3UlkFC1x)

*이 글은 미국 수학회(American Mathematical Society) Feature Column에 실린 Tony Phillips의 "Surface Topology in Bach Canons, I: The Möbius Strip"을 재게재한 것입니다. 이 연구는 Eric Altschuler와 함께 진행되어 2015년 Musical Times에 발표되었습니다.*

악보는 기본적으로 두 가지 차원을 갖습니다: 음높이(pitch)와 시간(time)입니다. 예를 들어, 단성 음악 텍스트(one-voice musical text)에서 음표의 음높이(주파수에 해당)는 수직으로 표현되고, 연주 시간은 왼쪽에서 오른쪽으로 진행됩니다.

![Score](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/pic1.jpg)

14-15세기 성가집의 *Kyrie eleison*에서 발췌한 이 악보에서는 시간이 왼쪽에서 오른쪽으로 흐르고 음높이는 높이에 해당합니다. 음악 기보법의 많은 세부사항이 변했지만, 기본 원리는 정확히 동일합니다. Image used by permission of the University of Missouri-Kansas City Libraries, Dr. Kenneth J. LaBudde Department of Special Collections.

> 단성 음악(one-voice music)은 하나의 선율만으로 구성된 음악을 말합니다. 이는 서양 음악사의 가장 초기 형태로, 그레고리오 성가가 대표적입니다. 이러한 음악을 기록한 악보는 본질적으로 2차원 평면에서 하나의 곡선을 그리는 것과 같습니다. 가로축은 시간의 진행을, 세로축은 음의 높낮이를 나타내므로, 수학적으로는 직사각형 영역 내의 연속적인 경로로 볼 수 있습니다. 오선지(staff) 위의 음표들은 이 2차원 공간에서의 점들이며, 이들을 순서대로 연결하면 하나의 연속적인 선율을 형성합니다.

따라서 위상수학적으로 단성 악보는 2차원 띠(strip)입니다. 수평(시간) 좌표는 시작부터 끝까지 진행되고, 수직 좌표는 낮은 음높이에서 높은 음높이까지 이어집니다. 위 성가집 악보에서 시작 부분의 음자리표(clef)는 보표의 두 번째 선이 음계에서 "파(fa)"에 해당함을 나타냅니다.

![Score](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-strip-small.jpg)

직사각형 띠로서의 단성 악보. Image: Tony Phillips.

악보가 대칭성을 가질 때, 위상구조는 더욱 흥미로워집니다. 악보가 반복된다고 가정해 봅시다: 같은 음표 시퀀스가 계속해서 반복되는 경우입니다. 이는 예를 들어 *뱀프(vamp)*에서 발생합니다. 뱀프는 반주로 반복적으로 연주되거나 무언가가 시작되기를 기다리는 동안 시간을 채우기 위해 반복되는 음표나 화음의 시퀀스입니다. 음악 기보법에서 반복 기호(repeat bars)는 시퀀스의 끝을 처음과 동일시합니다. 이러한 동일시는 악보를 위상수학적으로 원기둥(cylinder)으로 만듭니다.

> 위상수학에서 두 공간의 "동일시(identification)"는 특정 점들이나 부분들을 같은 것으로 간주하여 붙이는 것을 의미합니다. 직사각형 띠의 양 끝을 동일시하면 원기둥이 됩니다. 이는 띠의 왼쪽 끝과 오른쪽 끝을 물리적으로 붙이는 것과 같습니다. 음악적으로는 마지막 마디의 끝이 첫 마디의 시작으로 매끄럽게 연결되어 무한히 반복될 수 있음을 의미합니다. 이러한 위상적 구조는 음악의 순환적 특성을 수학적으로 표현한 것입니다.

![Vamp](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-vamp-1.jpg)

기초적인 뱀프 악보는 위상수학적으로 원기둥입니다. Image: Tony Phillips. 아래를 클릭하여 들어보세요.

### 카논(Canons)

(2성부) 카논(canon)은 두 번째 성부가 첫 번째 성부를 지연시킨 후 모방하는 악보입니다. 가장 잘 알려진 것 중 하나는 *프레르 자크(Frère Jacques)*입니다. 이 곡의 선율은 8마디 길이입니다. 3번째 마디에서 두 번째 성부가 첫 번째 성부가 부른 것을 반복하기 시작합니다. 두 성부는 음악적으로 잘 어울립니다(화성을 이룹니다, harmonise). 화성은 9번째와 10번째 마디까지 계속되며, 이때 첫 번째 성부가 다시 시작하고 두 번째 성부는 마무리됩니다. 그런 다음 두 번째 성부가 다시 들어오고, 3번째부터 10번째 마디까지의 시퀀스는 자연스럽게 계속 반복되는 *정상 상태(steady state)*를 형성합니다.

> 카논은 대위법(counterpoint)의 한 형태로, 동일한 선율이 시간차를 두고 여러 성부에서 반복되는 작곡 기법입니다. "카논(canon)"이라는 용어는 그리스어로 "규칙" 또는 "법칙"을 의미하는데, 이는 엄격한 모방 규칙을 따르기 때문입니다. 카논에서 "정상 상태"란 모든 성부가 들어온 후 안정적으로 반복되는 부분을 말합니다. 이 부분에서는 각 성부가 동일한 선율을 시간차를 두고 연주하면서도 조화로운 화성을 이루게 됩니다. 프레르 자크와 같은 돌림노래(round)도 카논의 한 종류입니다.

![Frere Jacques](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-frere-jacques.jpg)

프레르 자크. 첫 번째 성부가 두 번째 성부가 끝나는 동안 다시 시작하므로 자연스러운 종료 지점이 없습니다: 정상 상태(파란색 상자)는 원하는 만큼 반복될 수 있습니다. Image: Tony Phillips. 아래를 클릭하여 들어보세요.

카논은 위대한 바로크 작곡가 [요한 제바스티안 바흐(Johann Sebastian Bach)](https://en.wikipedia.org/wiki/Johann_Sebastian_Bach) (1685-1750)의 전문 분야였습니다. 사실 우리가 가진 그의 가장 좋은 초상화는 그가 카논 악보를 들고 있는 모습을 보여주는데, 이는 그가 *[골드베르크 변주곡의] 아리아의 처음 여덟 개 기본 음에 기초한 14개의 카논(Fourteen Canons on the first eight fundamental notes of the aria)* 이라는 제목을 붙인 [14개 카논 세트](http://www.bach-cantatas.com/NVD/BWV1087.htm) 중 13번째 카논입니다.

![Bach](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-Johann_Sebastian_Bach.jpg)

1746년 Elias Gottlob Haussmann의 초상화에서 바흐는 골드베르크 변주곡 바소 오스티나토의 처음 여덟 음에 기초한 14개의 카논 세트(BWV 1087) 중 카논 13번의 사본을 들고 있습니다.

> 골드베르크 변주곡(Goldberg Variations, BWV 988)은 바흐의 가장 유명한 건반악기 작품 중 하나로, 하나의 아리아와 30개의 변주, 그리고 아리아의 재현으로 구성됩니다. 이 작품의 기초가 되는 "바소 오스티나토(ground bass)" 또는 "그라운드(ground)"는 아리아의 저음 선율로, 처음 여덟 개 음이 특히 중요합니다. BWV 1087 카논 세트는 바로 이 여덟 개 음을 기반으로 작곡된 것입니다. 흥미롭게도 바흐는 자신의 초상화에 이 카논을 포함시킬 만큼 이 작품을 중요하게 여겼습니다.

이 카논 세트에는 나름의 이야기가 있습니다. 그림 속의 카논과 바흐가 친구의 사인첩에 쓴 또 다른 카논을 제외하고는, 그 존재가 1974년까지 알려지지 않았습니다. 그해 파리 *국립도서관(Bibliothèque Nationale)*에서 바흐 자신의 골드베르크 변주곡 사본의 [뒷부분에](http://gallica.bnf.fr/ark:/12148/btv1b550059626/f39.item.r=Bach%20Variations.zoom) 쓰여진 것으로 발견되었습니다. 우리는 이 세트에서 두 개의 다른 카논, 즉 카논 3번과 5번을 분석할 것입니다.

### 카논 3번

카논 3, 4, 5번은 모두 한 성부와 그것의 *전위(inversion)*를 포함하는데, 전위에서는 모든 음정이 반전되어 원곡이 올라갈 때 내려가고 그 반대도 마찬가지입니다(바흐는 이것을 *motu recto et contrario*, 즉 "정행과 반행"이라고 표현했습니다). 카논 3번에서 선행 성부는 골드베르크 그라운드의 처음 여덟 음을 연주하고, 3번째 마디에서 시작하는 추종 성부는 같은 선율을 거꾸로 연주합니다.

> 음악에서 "전위(inversion)"는 선율의 음정 관계를 반대로 뒤집는 것을 의미합니다. 예를 들어 원래 선율이 3도 위로 올라가면, 전위에서는 3도 아래로 내려갑니다. 이는 선율을 수평축을 기준으로 대칭 이동시키는 것과 같습니다. 바흐는 이러한 대위법적 기법을 탁월하게 사용했는데, 전위된 선율이 원래 선율과 동시에 연주될 때도 조화로운 화성을 이루도록 작곡했습니다. 이는 수학적 대칭성과 음악적 아름다움이 만나는 지점입니다.

![Canon 3](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-canon3-small-x-1.jpg)

아래를 클릭하여 들어보세요.

![Canon 3](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-canon3-inversion-small.jpg)

아래를 클릭하여 들어보세요.

![Canon 3](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-canon3-small.jpg)

맨 위: 골드베르크 변주곡 주제의 처음 여덟 음. 중간: 같은 악보를 위로 반사시킨 것; 대칭축은 B와 가온 C 사이에 있습니다. 맨 아래: 두 성부를 함께 표시. 첫 번째 성부가 두 번째 성부가 절반만 끝났을 때 다시 시작하므로, 카논의 정상 상태는 자연스럽게 반복됩니다. 아래를 클릭하여 들어보세요.

위상수학적으로 프레르 자크와 카논 3번은 동일한 구조를 가지고 있습니다: 도입 마디 이후, 카논은 *원기둥 모양(cylindrical)*의 정상 상태로 안정화됩니다. 바흐의 모든 카논은 이런 방식으로 조직되어 있습니다.

![Cylinder](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-cylinder-solo-with-tail-small.jpg)

바흐 카논의 일반적인 위상구조. Image: Tony Phillips.

### 카논 5번

카논 5번은 바흐가 *duplex, a 4*(이중, 4성부)라고 설명한 것으로: 두 개의 카논이 평행하게 노래하는 4개의 성부가 있습니다. 카논 중 하나는 카논 3번의 두 성부를 사용하되, 추종 성부가 한 옥타브 아래로 이동되었습니다. 그 위에 같은 구조의 또 다른 카논이 겹쳐져 있습니다: 추종 성부가 2마디 후에 선행 성부를 거꾸로 모방합니다.

![Canon 5](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-1087canon5.jpg)

골드베르크 그라운드에 기초한 카논 5번. 두 카논 모두에서 추종 성부는 선행 성부의 진술이 절반 진행되었을 때 들어옵니다. 파란색 상자는 정상 상태를 보여줍니다. Image: Tony Phillips. 아래를 클릭하여 들어보세요.

> 4성부 이중 카논은 바흐의 대위법적 숙련도를 보여주는 복잡한 구조입니다. 두 개의 독립적인 카논이 동시에 진행되면서도 전체적으로 조화로운 화성을 이루어야 합니다. 이는 마치 두 개의 수학적 패턴이 서로 간섭하지 않으면서 동시에 존재하는 것과 같습니다. 각 카논은 자체의 선행-추종 관계를 가지면서도, 네 성부 전체가 하나의 통일된 음악적 텍스처를 만들어냅니다.

위쪽 두 성부에 초점을 맞추어 정상 상태에서 악보를 그것의 거울 이미지(아래로 뒤집은 것)와 비교해 봅시다. 악보의 마지막 두 마디는 처음 두 마디를 거꾸로 뒤집은 것과 동일하며(이미지의 주황색 상자), 그 반대도 마찬가지입니다. 악보는 *미끄럼-반사 대칭(glide-reflection symmetry)*을 갖습니다: 악보를 따라 이동시킨 다음 뒤집으면 동일하게 보입니다. 그리고 같은 방향으로 다시 이동시키고 다시 뒤집으면 원래 위치로 돌아옵니다.

> 미끄럼-반사 대칭(glide-reflection symmetry)은 평행이동(glide)과 반사(reflection)를 결합한 대칭입니다. 구체적으로, 어떤 도형을 일정 거리만큼 평행이동시킨 후 특정 축에 대해 반사시켰을 때 원래 도형과 일치하면 미끄럼-반사 대칭을 갖는다고 말합니다. 발자국이 남긴 패턴이 대표적인 예입니다. 카논 5번의 경우, 악보를 시간축을 따라 반만큼 이동시킨 후 음높이 축에 대해 반사(전위)시키면 자기 자신과 일치합니다. 이러한 대칭성은 뫼비우스 띠의 수학적 구조와 정확히 대응됩니다.

![Canon 5](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-1087canon5mirror.jpg)

카논 5번의 위쪽 성부 악보(정상 상태)는 미끄럼-반사 대칭을 갖습니다. (음표의 꼬리는 오른쪽에서는 위로, 왼쪽에서는 아래로 향합니다; 이 속성은 거울에서 반전됩니다). Image: Tony Phillips.

미끄럼-반사 대칭을 가진 주기적 텍스트는 뫼비우스 띠에 인코딩될 수 있습니다: 종이 띠를 가져와서 한 번 비틀어준 다음 양 끝을 붙여서 얻는 형태입니다.

- 주기성은 원기둥에 인코딩될 수 있음을 의미합니다(위 참조)
- 미끄럼-반사 대칭은 원기둥을 비틀어서 두 겹으로 감싸면 두 세트의 기호가 정확히 일치함을 의미합니다.

결과로 나오는 객체가 뫼비우스 띠입니다. 기호들은 띠의 표면에만 있는 것이 아니라 띠 *안에(in)* 존재한다는 점에 주목하세요: 기호들은 띠의 양쪽 면에서 읽을 수 있습니다.

> 뫼비우스 띠는 1858년 독일 수학자 아우구스트 페르디난트 뫼비우스(August Ferdinand Möbius)가 발견한 위상수학적 표면입니다. 이 띠의 가장 놀라운 성질은 한쪽 면만 가진다는 것입니다. 띠 위의 한 점에서 출발하여 띠를 따라 계속 가다 보면, 가장자리를 넘지 않고도 띠의 "반대편"에 도달할 수 있습니다. 수학적으로 이는 "비가향성(non-orientable)" 표면이라고 불립니다. 미끄럼-반사 대칭을 가진 주기적 패턴을 뫼비우스 띠에 배치하면, 띠를 한 바퀴 돌았을 때 패턴이 정확히 자기 자신과 일치하게 됩니다. 이는 대칭성의 기하학적 구현입니다.

![Canon 5](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-moebius-1.jpg)

미끄럼-반사 대칭을 가진 주기적 텍스트를 뫼비우스 띠에 인코딩한 것. 띠는 위와 아래에서 보여집니다. Image: Tony Phillips.

카논 5번의 위쪽 두 성부 악보가 미끄럼-반사 대칭을 가지므로, 우리는 이 과정을 적용할 수 있습니다:

![Canon 5](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-canon5-cylinder-500.jpg)

원기둥에 인쇄된 카논 5번의 위쪽 두 성부 악보. Image: Tony Phillips.

![Canon 5](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-canon5-moebius-350.jpg)

원기둥을 비틀어서 그 자체에 두 번 감싸 뫼비우스 띠를 형성한 것. 각 음표의 두 사본이 이제 정확히 일치함에 주목하세요(꼬리를 제외하고). Image: Tony Phillips. 아래를 클릭하여 뫼비우스 띠의 소리를 들어보세요.

아래쪽 두 성부의 악보도 미끄럼-반사 대칭을 갖습니다: 이것도 뫼비우스 띠에 인코딩될 수 있지만, 대칭축이 다르기 때문에 다른 뫼비우스 띠에 인코딩됩니다.

> 카논 5번은 실제로 두 개의 독립적인 뫼비우스 띠 구조를 포함하고 있습니다. 위쪽 두 성부가 하나의 뫼비우스 띠를 형성하고, 아래쪽 두 성부가 또 다른 뫼비우스 띠를 형성합니다. 각각의 카논은 자체의 대칭축을 가지고 있으며, 이는 서로 다른 음높이 중심에 해당합니다. 이는 바흐가 동일한 위상수학적 원리를 다른 음역대에서 동시에 구현했음을 보여줍니다. 두 뫼비우스 띠가 함께 작동하여 4성부의 조화로운 전체를 만들어내는 것입니다.

반행 카논(canon in contrary motion)의 악보가 반드시 미끄럼-반사 대칭을 가지는 것은 아니라는 점에 주목하세요. 미끄럼-반사 대칭이 반복되면 원래 상태로 돌아갑니다. 반행 카논이 이 속성을 갖는 것은 두 번째 성부가 정확히 중간 지점에 들어올 때뿐입니다.

![Periodic strip](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/fcarc-october2016-moebius-2.jpg)

이 주기적인 "2성부" 텍스트는 반행 모방을 보여주지만 미끄럼-반사 대칭을 갖지 않습니다. Image: Tony Phillips.

> 뫼비우스 띠 구조를 갖기 위한 핵심 조건은 추종 성부가 정확히 선행 성부 길이의 절반 지점에서 시작해야 한다는 것입니다. 이것이 "절반(halfway point)" 조건입니다. 만약 추종 성부가 다른 시점에 들어오면, 미끄럼-반사 작용을 두 번 적용했을 때 원래 위치로 정확히 돌아오지 않습니다. 수학적으로, 미끄럼 거리가 전체 주기의 절반이어야 미끄럼-반사가 2차 대칭(order-2 symmetry)이 되어 두 번 적용하면 항등원소가 됩니다. 카논 3번과 5번이 뫼비우스 띠 구조를 갖는 이유는 바로 이 조건을 만족하기 때문입니다.

우리의 카논 3번과 5번은 이 속성을 가지고 있습니다: 그들의 정상 상태는 뫼비우스 띠에서 읽을 수 있습니다. 다른 바흐의 반행 카논들, 예를 들어 *음악의 헌정(Musical Offering)*의 카논 3번과 9번, 또는 골드베르크 세트의 변주 12번과 15번은 이 속성을 갖지 않습니다. 이는 우리의 *Musical Times* 논문에서 이들이 그런 속성을 가진다고 잘못 언급한 것을 바로잡는 것입니다.

YouTube에 게시된 아름다운 [동영상](https://www.youtube.com/watch?v=xUHQ2ybTejU&feature=youtu.be)은 바흐의 *게 카논(Crab Canon)* (*음악의 헌정*의 카논 1번)이 뫼비우스 띠에서 읽을 수 있다는 것을 보여줍니다. 게 카논에서 추종자는 선행자를 끝에서 시작으로 거꾸로 연주합니다. 이것은 놀라운 음악 작품이지만, 실제로는 뫼비우스 띠와 아무 관련이 없습니다. 이 구성의 결함은 악보가 뫼비우스 띠의 양쪽 면에 쓰여지게 되어, 실제로는 뫼비우스 띠의 연결된 이중 덮개(connected double cover), 즉 원기둥에 쓰여지게 된다는 것입니다. 반복되는 텍스트는 모두 그렇게 표현될 수 있습니다.

> 게 카논(Crab Canon)은 역행 카논(retrograde canon)으로, 추종 성부가 선행 성부를 시간적으로 거꾸로 연주합니다. 마치 게가 뒤로 걷듯이 음악이 거꾸로 진행되어 "게 카논"이라는 이름이 붙었습니다. 이 카논은 팰린드롬(palindrome) 구조를 가지는데, 앞에서 읽으나 뒤에서 읽으나 같은 성질입니다. 그러나 이것이 뫼비우스 띠 구조를 만드는 것은 아닙니다. 뫼비우스 띠는 악보가 띠 안에 하나의 연속적인 경로로 존재해야 하는데, 게 카논을 뫼비우스 띠로 표현하려 하면 악보를 띠의 양면에 따로 써야 합니다. 이는 본질적으로 두 개의 독립적인 표면을 사용하는 것으로, 위상수학적으로는 원기둥과 동등합니다. 따라서 게 카논의 팰린드롬 구조는 뫼비우스 띠와 시각적으로 연관지을 수는 있지만, 수학적으로 엄밀한 의미에서 뫼비우스 띠 구조는 아닙니다.

### 이 글에 대하여

이 글은 미국 수학회 Feature Column *Surface Topology in Bach Canons, I: The Möbius Strip*의 Tony Phillips의 글을 재게재한 것입니다. 이 연구는 Eric Altschuler와 함께 진행되어 2015년 *Musical Times*에 발표되었습니다.

![Tony Phillips](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/tony-photo.jpg)

Tony Phillips.

[Tony Phillips](http://www.math.stonybrook.edu/~tony/)는 Stony Brook University의 John S. Toll 수학 교수이며 위상수학을 전공합니다. 그는 예술에서의 수학적 현현에 대한 평생의 관심을 가지고 있습니다.

![Eric Altschuler](https://plus.maths.org/content/sites/plus.maths.org/files/articles/2016/music/altschuler_e_profile.png)

Eric Altschuler.

[Eric Altschuler](https://medicine.temple.edu/eric-altschuler), MD, PhD는 Temple University의 Lewis Katz School of Medicine에서 물리의학 및 재활의학 부교수입니다. 그는 J.S. 바흐의 음악을 매우 사랑하며 바흐의 음악적 음조 및 조직 체계 탐구를 연구합니다.

## 댓글

## H. Celine

괴델, 에셔, 바흐(Gödel, Escher, Bach)를 읽어보셨나요?

> 더글러스 호프스태터(Douglas Hofstadter)의 1979년 저서 『괴델, 에셔, 바흐: 영원한 황금 노끈(Gödel, Escher, Bach: An Eternal Golden Braid)』은 수학, 예술, 음악에서 나타나는 자기참조와 재귀적 구조를 탐구합니다. 이 책은 논리학자 쿠르트 괴델, 화가 M.C. 에셔, 작곡가 J.S. 바흐의 작품에서 공통적으로 나타나는 패턴과 대칭성을 분석합니다. 특히 바흐의 카논과 푸가에서의 수학적 구조를 상세히 다루며, 본 글에서 다룬 뫼비우스 띠와 같은 위상수학적 개념이 음악에 어떻게 구현되는지를 탐구합니다.

## Andrew Pettit

또 다른 링크가 있습니다:

http://strangepaths.com/canon-1-a-2/2009/01/18/en/#footnote-1-295

## Prabhakar Rajasingham

Maths Plus에서 본 것 중 가장 잘 쓰여지고 잘 설명된 게시물 중 하나입니다. 정말 보석 같은 글입니다! 계속 이런 글들을 부탁드립니다.