### $\mathbb{R}^n$에서의 연속성 (Continuity in $\mathbb{R}^n$)

#### 열린 공과 근방 (Open Ball and Neighborhood)
점 $p_0 \in \mathbb{R}^n$을 중심으로 하고 반지름이 $\epsilon > 0$인 열린 공(open ball)은 집합 $B_\epsilon(p_0) = \{p \in \mathbb{R}^n; |p - p_0| < \epsilon\}$이다.  점 $p$를 포함하는 열린 집합을 $p$의 근방(neighborhood)이라 한다. 

#### 연속 함수 (Continuous Map)
사상 $F: U \subset \mathbb{R}^n \to \mathbb{R}^m$이 점 $p \in U$에서 연속이라는 것은, 임의의 $\epsilon > 0$에 대해 $F(B_\delta(p)) \subset B_\epsilon(F(p))$를 만족하는 $\delta > 0$가 존재함을 의미한다.

- $F$가 연속일 필요충분조건은 그 성분 함수들 $f_i: U \to \mathbb{R}$이 모두 연속인 것이다  
- $F$가 연속일 필요충분조건은 모든 열린 집합 $V \subset \mathbb{R}^m$의 역상 $F^{-1}(V)$가 열린 집합인 것이다. 
- 연속 함수의 합성은 연속 함수이다.

### 닫힌 집합 (Closed Set)
집합 $F \subset \mathbb{R}^n$이 자신의 모든 집적점(limit point)을 포함할 때 닫혀있다고 한다.  집합 $F$가 닫혀있는 것과 그 여집합 $\mathbb{R}^n - F$가 열려있는 것은 동치이다. 

#### 코시 수열 (Cauchy Sequence)
$\mathbb{R}^n$ 안의 수열 $\{p_i\}$가 수렴할 필요충분조건은 코시 수열인 것이다.

#### 중간값 정리 (Intermediate Value Theorem)
닫힌 구간 $[a,b]$에서 연속인 함수 $f$에 대하여 $f(a)$와 $f(b)$의 부호가 다르면, $f(c)=0$인 $c \in (a,b)$가 존재한다.

#### 최대-최소 정리 (Extreme Value Theorem)
닫힌 구간 $[a,b]$에서 연속인 함수는 그 구간 내에서 최댓값과 최솟값을 갖는다. 

### $\mathbb{R}^n$에서의 미분가능성 (Differentiability in $\mathbb{R}^n$)

#### 미분가능한 함수 (Differentiable Function)
함수가 미분가능하다는 것은 모든 차수의 편도함수가 존재하고 연속임을 의미한다 ($C^\infty$ 등급). 미분가능한 함수에 대하여 혼합 편도함수는 미분 순서에 무관하다(예: $f_{xy} = f_{yx}$). 

#### 미분가능한 사상 (Differentiable Map)
사상 $F: U \subset \mathbb{R}^n \to \mathbb{R}^m$의 모든 성분 함수가 미분가능할 때, $F$를 미분가능하다고 한다. 

#### 사상의 미분 (Differential of a Map)
미분가능한 사상 $F: U \subset \mathbb{R}^n \to \mathbb{R}^m$의 점 $p \in U$에서의 미분(differential)은 선형사상 $dF_p: \mathbb{R}^n \to \mathbb{R}^m$으로 정의된다.  이는 $p$를 지나는 곡선 $\alpha(t)$ (단, $\alpha(0)=p, \alpha'(0)=w$)의 접선벡터 $w$를 곡선 $(F \circ \alpha)(t)$의 $F(p)$에서의 접선벡터 $(F \circ \alpha)'(0)$으로 보낸다.

* $dF_p$의 표준기저에 대한 행렬은 야코비 행렬(Jacobian matrix)이다. 

#### 연쇄 법칙 (Chain Rule for Maps)
미분가능한 사상 $F$와 $G$의 합성에 대하여 $d(G \circ F)_p = dG_{F(p)} \circ dF_p$가 성립한다. 

#### 역함수 정리 (Inverse Function Theorem)
미분가능한 사상 $F: U \subset \mathbb{R}^n \to \mathbb{R}^n$에 대하여, 만약 점 $p \in U$에서 미분 $dF_p$가 동형사상(isomorphism)이면, $F$는 $p$의 어떤 근방에서 미분동형사상(diffeomorphism)이다.[^1]

$\mathbb{R}^n$의 열린 집합 $U$에서 $\mathbb{R}^n$으로 가는 함수 $F: U \to \mathbb{R}^n$가 $C^1$ 이고, 야코비 행렬식이 $0$이 아니면, 점 $p_0$와 그 상 $F(p_0)$를 각각 포함하는 적절한 열린 근방 $V$와 $W$가 존재하여, 함수 $F$는 $V$에서 $W$로 가는 미분동형사상(diffeomorphism)이 된다. 즉, $F$를 $V$에 국한시키면 이 함수는 전단사 함수이며, 그 역함수 $F^{-1}: W \to V$ 또한 존재하고 $C^1$ 함수가 된다.

[^1]: 역함수 정리는 어떤 함수가 복잡한 비선형 함수라도 국소적으로 미분가능하고, 역함수를 가지면, 그 지점 근방에서는 함수를 마치 일대일 대응처럼 다룰 수 있고 그 역함수 또한 매끄럽다는 것을 보장해준다.