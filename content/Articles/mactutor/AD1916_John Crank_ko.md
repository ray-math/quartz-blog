---
title: John Crank
---

> [!NOTE]
> https://mathshistory.st-andrews.ac.uk/Biographies/Crank/
>
> John Crank는 열방정식을 연구한 영국의 수치해석학자였다.

![Thumbnail of John Crank](https://mathshistory.st-andrews.ac.uk/Biographies/Crank/thumbnail.jpg)

**출생**: 1916년 2월 6일 영국 Lancashire, Hindley

**사망**: 2006년 10월 3일 영국 London, Ruislip

---

**요약**: John Crank는 열방정식을 연구한 영국의 수치해석학자였다.

London, Ruislip, 영국

**John Crank**는 열방정식을 연구한 영국의 수치해석학자였다.

### 전기

**John Crank**는 Manchester 대학교(1934-38)에서 Lawrence Bragg와 Douglas [Hartree](https://mathshistory.st-andrews.ac.uk/Hartree/)의 제자였으며, 그곳에서 학사(B.Sc.)와 석사(M.Sc.) 학위를 받았고 이후(1953년) 박사(D.Sc.) 학위를 받았다. 탄도학 분야의 전쟁 연구를 수행한 후, 그는 1945년부터 1957년까지 Courtaulds 기초연구소에서 수리물리학자로 일했으며, 1957년부터 1981년까지 Brunel 대학교(초기에는 Acton에 위치한 Brunel College)에서 수학 교수로 재직했다. 그의 주요 연구는 [편미분방정식](https://mathshistory.st-andrews.ac.uk/Glossary/#partial_diff_equation)의 수치해법, 특히 열전도 문제의 해법에 관한 것이었다. 1940년대에 그러한 계산들은 단순한 기계식 탁상 계산기로 수행되었다. Crank는 당시 나무 조각 하나를 "태우는" 수치계산에 일주일이 걸릴 수 있었다고 말한 것으로 알려져 있다.

John Crank는 열방정식에 관한 [Phyllis Nicolson](https://mathshistory.st-andrews.ac.uk/Nicolson/)과의 공동 연구로 가장 잘 알려져 있다. 이 연구에서는 다음의 2계 편미분방정식을 만족하는 연속 해가 필요했다:

$x > 0$, $t > 0$에 대해

$$
\frac{\partial u}{\partial t} = \frac{\partial^{2} u}{\partial x^{2}}
$$

이는 모든 실수 $x$에 대해 $u(x, 0) = f(x)$ 형태의 초기 조건을 만족해야 한다. 그들은 $x$와 $t$의 격자점에서 근사해를 구하는 수치적 방법을 고려했으며, $\frac{\partial u}{\partial t}$와 $\frac{\partial^{2} u}{\partial x^{2}}$를 유한차분 근사로 대체했다. 이러한 대체 방법 중 가장 단순한 것 중 하나는 1910년 [L F Richardson](https://mathshistory.st-andrews.ac.uk/Richardson/)에 의해 제안되었다.

[Richardson](https://mathshistory.st-andrews.ac.uk/Richardson/)의 방법은 계산이 매우 쉬운 수치해를 제공했지만, 안타깝게도 수치적으로 불안정하여 쓸모가 없었다. 이 불안정성은 Crank, [Nicolson](https://mathshistory.st-andrews.ac.uk/Nicolson/) 등이 긴 수치 계산을 수행하기 전까지는 인식되지 않았다. 수치적으로 안정한 Crank와 [Nicolson](https://mathshistory.st-andrews.ac.uk/Nicolson/)의 방법은 각 시간 단계에서 매우 단순한 선형방정식계(삼중대각 시스템 tridiagonal system)의 해를 요구한다.

> Crank-Nicolson 방법은 현재 열방정식과 확산 방정식의 수치해법에서 가장 널리 사용되는 기법 중 하나로, 무조건 안정적(unconditionally stable)이면서도 계산 효율성이 뛰어나다는 장점이 있다.

### References ([show](https://mathshistory.st-andrews.ac.uk))

- J Crank,
*Free and moving boundary problems*(Oxford, 1987).

 - J Crank,
*Mathematics and industry*(Oxford, 1962).

 - J Crank,
*The mathematics of diffusion*(Oxford, 1956).

 - J Crank,
*The Differential Analyser*(London, 1947).

 - J Crank and P Nicolson. A practical method for numerical evaluation of solutions of partial differential equations of the heat-conduction type,
*Proc. Cambridge Philos. Soc.***43**(1947). 50-67. [Re-published in: John Crank 80th birthday special issue*Adv. Comput. Math.***6**(1997) 207-226]
