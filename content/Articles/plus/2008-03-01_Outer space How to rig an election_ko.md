---
title: "아웃터 스페이스: 선거를 조작하는 방법"
date: 2008-03-01
---

> [!NOTE]
> https://plus.maths.org/content/outer-space-how-rig-election
>
> 당신이 생각하는 것보다 훨씬 쉽습니다

![](https://plus.maths.org/content/sites/default/files/styles/small_square/public/issue46/outerspace/icon.jpg?itok=Y-ZPqVYu)

당신은 얼마나 자주 투표에 참여하는지 알면 놀랄 것입니다. 어떤 영화를 보러 갈까요? 어떤 TV 채널을 볼까요? 휴가는 어디로 갈까요? 어떤 브랜드의 냉장고를 사는 게 좋을까요? 만약 당신이 여러 가지 가능한 답이 있는 질문들에 대해 다른 사람들과 논의한다면, 당신은 실제로 "투표"를 하고 있는 것입니다. 즉, 당신의 선호를 표현하는 것이고, 성공한 후보는 최종적으로 선택된 것입니다. 이러한 결정들은 모든 당사자가 투표권을 행사하는 방식으로 이루어지지 않습니다. 그 과정은 보통 훨씬 더 우연적입니다. 누군가 비디오를 빌리자고 제안합니다. 그러면 누군가 더 새로운 것이라며 다른 것을 제안합니다. 그러면 누군가 새로운 것은 너무 폭력적이니 세 번째 것을 골라야 한다고 말합니다. 누군가 이미 그것을 봤다는 것이 밝혀져서 첫 번째 선택으로 돌아갑니다. 누군가 그것은 아이들에게 지루하다는 것을 깨닫고 다른 것을 제안합니다. 사람들은 이제 지쳐서 그 제안에 동의합니다.

> 여기서 설명하는 과정은 사회 선택 이론(social choice theory)의 핵심 개념인 "경로 의존성(path dependence)"을 보여줍니다. 경로 의존성이란 최종 결과가 선택 과정에서 거친 경로에 따라 달라지는 현상을 의미합니다. 수학적으로 말하면, 선택 함수(choice function)가 선택지들의 순서에 대해 불변하지 않다는 것입니다. 이는 우리가 직관적으로 "합리적"이라고 생각하는 선택 과정이 실제로는 비가역적이고 맥락 의존적임을 보여줍니다. 이러한 현상은 Kenneth Arrow의 불가능성 정리(Arrow's Impossibility Theorem)와도 깊은 관련이 있으며, 완벽하게 공정한 투표 시스템이 존재하지 않는다는 것을 시사합니다.

![Hands exchanging money](https://plus.maths.org/issue46/outerspace/corrupt.jpg)

선거를 조작하고 싶으신가요? 올바른 투표 시스템을 선택한다면 부정행위가 필요 없습니다.

여기서 일어나는 일은 흥미롭습니다. 한 가능성이 다른 가능성과 비교되고, 이 과정이 반복됩니다. 당신은 모든 가능한 영화의 모든 속성을 고려하여 전체적으로 투표하지 않습니다. 따라서 숙고의 결과는 당신이 어느 영화를 다른 영화와 비교하는 순서에 매우 강하게 의존합니다. 당신이 영화를 고려하는 순서와 비교에 사용하는 속성을 변경하면, 매우 다른 승자로 끝날 수 있습니다.

선거도 마찬가지입니다. 8명의 가능한 후보자(Ali, Bill, Cath, Dave, Edith, Fred, Gill, Hal) 중에서 리더를 선택해야 하는 30명이 있다고 가정해봅시다. "투표자들"은 세 그룹으로 나뉘어 후보자들 사이의 선호도를 다음과 같이 정합니다:

그룹 1: Ali Bill Cath Dave Edith Fred Gill Hal

그룹 2: Bill Cath Dave Edith Fred Gill Hal Ali

그룹 3: Cath Dave Edith Fred Gill Hal Ali Bill

첫눈에 보기에 Cath가 전체적으로 선호되는 후보자로 보이며, 세 순위 목록에서 1위, 2위, 3위를 차지합니다. 그러나 Hal의 어머니는 Hal이 리더 자리를 얻기를 매우 원하며, Hal이 투표에서 이길 수 있도록 할 수 있는지 물어보러 왔습니다. 그는 선호 목록에서 꼴찌, 꼴찌에서 두 번째, 꼴찌에서 세 번째에 있기 때문에 희망이 없어 보입니다. Hal이 리더로 선출될 가능성이 전혀 없어 보입니다. 우리는 그의 어머니에게 모든 것이 규칙을 따라야 하며 어떠한 부정행위도 허용되지 않는다는 것을 분명히 합니다. 따라서 과제는 Hal을 승자로 만드는 투표 시스템을 찾는 것입니다. 다음은 그녀가 제안한 것입니다.

> 이제 소개될 방법은 "토너먼트 방식(tournament-style voting)" 또는 "순차적 쌍대 비교(sequential pairwise comparison)"입니다. 이 방식의 핵심 취약점은 대진표를 어떻게 구성하느냐에 따라 결과가 완전히 달라질 수 있다는 것입니다. 이는 투표 이론에서 "의제 설정 효과(agenda-setting effect)"로 알려진 현상입니다. 수학적으로 보면, 이는 선호 관계가 이행성(transitivity)을 만족하지 않을 때 발생합니다. 즉, $A > B$이고 $B > C$라고 해서 반드시 $A > C$인 것은 아닙니다. 이러한 비이행적 선호는 "콘도르세의 역설(Condorcet paradox)"의 한 형태로, 집단의 선호가 개인의 합리적 선호로부터 비합리적인 순환 구조를 만들어낼 수 있음을 보여줍니다.

당신이 해야 할 일은 토너먼트 방식의 선거를 설정하고 세 그룹의 선호도를 사용하여 각 2인 경쟁의 승자를 선택하는 것입니다. 먼저 Gill과 Fred를 맞붙이면, Fred가 3-0으로 이깁니다. 그런 다음 Fred가 Edith와 경쟁하고, 3-0으로 집니다. Edith는 Dave와 경쟁하고 3-0으로 집니다. Dave는 Cath와 경쟁하고 3-0으로 집니다. Cath는 Bill과 경쟁하고 2-1로 집니다. Bill은 Ali와 경쟁하고 2-1로 집니다. 그러면 Ali가 최종 대결에서 Hal과 경쟁하게 됩니다. Hal이 Ali를 2-1로 이깁니다. 따라서 Hal이 새로운 리더를 결정하는 이 토너먼트의 승리 선택입니다.

> 이 결과를 좀 더 자세히 분석해봅시다. 각 대결에서 승자가 결정되는 방식을 보면, 예를 들어 Fred vs Gill에서 Fred가 3-0으로 이긴다는 것은 세 그룹 모두 자신들의 선호 순위에서 Fred를 Gill보다 앞에 두었다는 의미입니다. 실제로 확인해보면: 그룹 1에서 Fred는 6번째, Gill은 7번째; 그룹 2에서 Fred는 5번째, Gill은 6번째; 그룹 3에서 Fred는 4번째, Gill은 5번째입니다. 모든 그룹에서 Fred가 Gill보다 앞서므로 3-0 승리입니다. 마지막 대결인 Hal vs Ali에서는 그룹 1(Ali가 1위, Hal이 8위)만 Ali를 선호하고, 그룹 2와 3(Ali가 각각 8위와 7위, Hal이 각각 7위와 6위)은 Hal을 선호하여 Hal이 2-1로 승리합니다. 핵심은 강력한 후보들(Cath, Dave 등)이 서로를 일찍 제거하도록 대진표를 구성했다는 점입니다.

트릭이 무엇이었을까요? 단순히 더 강한 후보자들이 초기 단계에서 하나씩 서로를 제거하도록 하고, 당신의 "보호받는" 후보자를 마지막 순간에만 투입하여 그들이 이길 수 있는 유일한 다른 후보자와 비교되도록 하는 것입니다. 그러니 영국 남자 테니스 선수도 결국 윔블던에서 우승할 수 있습니다.

> 이 예시는 투표 시스템 설계의 근본적인 문제를 드러냅니다. 수학적으로 "공정한" 투표 시스템이란 무엇일까요? Kenneth Arrow는 1951년 그의 불가능성 정리에서, 세 명 이상의 유권자와 세 개 이상의 선택지가 있을 때 몇 가지 합리적으로 보이는 조건들을 모두 만족하는 투표 시스템은 존재하지 않는다는 것을 증명했습니다. 이러한 조건들은: (1) 파레토 효율성(Pareto efficiency): 모두가 A를 B보다 선호하면 시스템도 A를 선택해야 함, (2) 무관한 대안으로부터의 독립성(Independence of Irrelevant Alternatives, IIA): A와 B 사이의 선택은 C의 존재에 영향받지 않아야 함, (3) 비독재성(non-dictatorship): 한 사람의 선호가 항상 결과를 결정해서는 안 됨 등입니다. 위 예시는 특히 IIA 조건이 위배되는 경우로, 대진표 순서(무관한 대안의 배치)가 최종 결과에 결정적 영향을 미칩니다. 이는 민주주의 시스템의 수학적 한계를 보여주는 심오한 결과입니다.

### 더 읽어볼 자료

[Chaotic elections! A mathematician looks at voting](http://www.amazon.co.uk/Chaotic-Elections-Mathematician-Looks-Voting/dp/0821828479/ref=sr_1_1?ie=UTF8&s=books&qid=1204205746&sr=8-1) Donald G. Saari 저;[Decisions and elections: Explaining the unexpected](http://www.amazon.co.uk/Decisions-Elections-Explaining-Donald-Saari/dp/0521004047/ref=sr_1_1?ie=UTF8&s=books&qid=1204284827&sr=8-1) Donald G. Saari 저;- [For all practical purposes](http://www.amazon.co.uk/All-Practical-Purposes-COMAP/dp/0716769018/ref=sr_1_1?ie=UTF8&s=books&qid=1204284985&sr=1-1) 7판의 12장, *대통령 선출하기*

[Outer space: Blowin' in the wind](https://plus.maths.org/issue45/outerspace/index.html)에 제시된 퍼즐을 풀었나요? 만약 아니라면, [여기서 답을 찾을 수 있습니다](https://plus.maths.org/issue46/outerspace/solution-gifd.html)!

> Donald G. Saari는 투표 이론의 세계적 권위자로, 특히 보르다 점수(Borda count) 방식의 수학적 특성을 연구했습니다. 그의 연구는 기하학적 방법을 사용하여 다양한 투표 시스템의 속성을 분석하는 것으로 유명합니다. 투표 시스템은 단순히 정치적 문제가 아니라 깊은 수학적 구조를 가진 주제입니다. 위상수학, 게임 이론, 확률론 등 다양한 수학 분야가 투표 이론과 연결되어 있으며, 이는 현대 민주주의의 이론적 기반을 이해하는 데 필수적입니다.