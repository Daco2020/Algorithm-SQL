
'''
1. 인풋 숫자의 홀짝을 구한다.
2. 짝이면 2를 나누고 카운팅을 한다.
3. 홀이면 3을 곱하고 1을 더한 후 카운팅을 한다.
4. 결과가 1이 될 때까지 반복한다.
5. 결과가 1이 나오면 카운팅을 반환한다.
6. 카운팅이 500을 넘어서면 -1 을 반환한다.
'''

import time


def solution(num):
    cnt = 0

    while not num == 1:

        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1

        cnt += 1

    if cnt >= 500:
        cnt = -1

    return cnt


def solution(num):
    cnt = 0

    while not num == 1:

        num = num / 2 if num % 2 == 0 else num * 3 + 1

        cnt += 1

    return cnt if cnt < 500 else -1


# 일반 코드와 삼항연산자의 효율을 비교해보았지만 큰 차이가 없음..
start = time.time()
print(solution(500000)*10000000000000000)
end = time.time()
print(start, end)
print(f"걸린 시간 : {end-start}")
