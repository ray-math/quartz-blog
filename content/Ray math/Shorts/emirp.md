---
title: emirp
date: 2025-01-11
tags:
  - 소수
  - shorts
---
Emirp는 이름과 같이 소수를 뒤집어서도 소수가 되는 수를 의미합니다.

예를 들어 $13$은 소수인데 이를 뒤집은 $31$도 소수이므로 $13$은 emirp입니다.

대충 python을 돌려보면 꽤 많은 소수가 emirp가 존재합니다.
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    return int(str(n)[::-1])

def find_emirps(limit):
    emirps = []
    for i in range(13, limit + 1):  # Starting from 13 as it's the first emirp
        if is_prime(i):
            reversed_i = reverse_number(i)
            if i != reversed_i and is_prime(reversed_i):
                emirps.append(i)
    return emirps

# Set a limit to search for emirps up to that number
limit = 1000
emirps_up_to_limit = find_emirps(limit)
print(emirps_up_to_limit)
```

현재까지 알려진 가장 큰 emirp는 다음과 같은데

$$
10^{10006} + 941992101 \times 10^{4999} + 1
$$

신기하게도 이 숫자의 자리수인 $10007$도 emirp입니다.