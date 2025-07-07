위상수학에서 [[근방(Neighborhood)]]의 뜻을 엄밀히 정의하면 다음과 같습니다.

정의. $(X,\tau)$를 위상 공간이라 하고, $x\in X$를 한 점이라 하자.  
집합 $N\subset X$이 $x$의 근방(neighborhood)이라고 부르려면,

$$
\exists\,U\in\tau\quad\text{such that}\quad x\in U\subset N
$$

즉, $N$ 내에 $x$를 포함하는 어떤 열린집합 $U$가 꼭 있어야 합니다.

- 이때 열린집합 $U$를 $x$의 열린 근방(open neighborhood)이라 합니다.  
- 만약 $N$ 자체가 이미 열린집합이라면, “$N$는 $x$의 근방”과 “$N$는 $x$의 열린 근방”이 동치입니다.

또한, 집합 $A\subset X$ 전체의 근방을 정의할 때는,

$$
N\subset X\quad\text{이 $A$의 근방}\quad\Longleftrightarrow\quad
\exists\,U\in\tau\;\bigl(A\subset U\subset N\bigr)
$$

즉 $N$ 안에 $A$를 포함하는 어떤 열린집합 $U$가 있으면 $N$을 $A$의 근방이라 합니다.

이 정의를 통해 “어떤 점이나 부분집합 주위의 충분히 작은 ‘열린’ 공간”을 가리켜 근방이라 부르며, 이를 바탕으로 연속성·국소연결성·경로연결성 등을 정의합니다.