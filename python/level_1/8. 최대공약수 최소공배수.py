'''
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.


제한 사항
두 수는 1 이상 1000000 이하의 자연수입니다.


입출력 예
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.


해결 방법
1. n과 m의 크기를 비교 및 재할당한다.
2. 최대공약수를 구하는 함수를 만든다.
3. 최소공배수를 구하는 함수를 만든다.
4. 최대공약수와 최소공배수를 리스트로 묶어 반환한다.

'''


def solution(n, m):
    if n > m:
        n, m = m, n

    def banana(n, m):
        for i in range(1, n+1):
            if not n % i:
                banana = n // i
            if m % banana == 0:
                return banana

    def tomato(n, m):
        for i in range(1, m+1):
            tomato = m * i
            if tomato % n == 0:
                return tomato

    return [banana(n, m), tomato(n, m)]


'''
banana함수는 최대공약수, tomato함수는 최소공배수를 구하는 함수이다.
이 두 함수를 활용해 최종적으로 최대공약수와 최소공배수를 리스트로 반환하였다.

수학을 잘하면 이를 쉽게구하는 공식을 알고 있겠지만
나는 수학을 잘 모르다보니(수포 미대생임..) 일단 머리를 굴려보면서 코드를 작성했다.
그래도 어찌저찌 답을 찾아 합격점을 맞을 수 있었다.

물론 처음에 짠 코드는 처참한 점수를 얻었다. 아래는 처음에 작성한 31.3점짜리 코드이다.


# 합계: 31.3 / 100.0

def solution(n, m):
    if n > m:
        n, m = m, n

        
    def banana(n, m):
        banana_set = set()
        
        for i in range(m):
            i = i+1
            
            banana_set.add(n // i if n % i == 0 else 1)
            banana = m // i if m % i == 0 else 1
            
            if banana in banana_set:
                return banana
        
        
    def tomato(n, m):
        tomato_list = []
        
        for i in range(m):
            i = i+1
            
            tomato_list.append(m * i)
            tomato = n * i
            
            if tomato in tomato_list:
                return tomato
    
    
    return [banana(n, m), tomato(n, m)]


list와 set을 활용하여 약수와 배수안에 해당 값이 있는지 확인하는 식으로 코드를 작성하였는데 이 코드는 좋은 점수를 받지 못했다. 
아무래도 로직에 허점이 있었던 것 같다. 

프로그래머스의 경우 왜 틀렸는지는 정확하게 나오지 않으므로 그냥 처음부터 새로 짜기로 했고 결국 맨 위와 같은 코드로 합격점을 받을 수 있었다.


추가로 최대공약수를 구하는 banana함수의 경우 할 말이 있다.



    def banana(n, m):
        for i in range(1, n+1):
            if not n % i:
                banana = n // i
            if m % banana == 0:
                return banana


banana = n // i 의 경우 나누기가 실행되고 나서 그 결과 값을 반올림을 하기 때문에 올바르지 않은 숫자가 변수에 할당되는 일이 발생했다. 
그렇기 때문에 if not n % i: 코드를 추가 함으로써 나머지가 없는 값(반올림 할 필요가 없는 값)에 한 해 나누기를 실행하였다. 
이렇게 하니 정상적으로 최대공약수를 구할 수 있었다.


이번 문제의 경우 다른 사람들의 풀이를 보니 정말 다들 각양각색으로 풀었더라. 
누구는 나보다 더 복잡하게, 누구는 나보다 더 간결하게 풀었다. 
다른 사람들의 코드를 보면서 다양한 방법을 간접적으로 익혀봐야겠다. 


참고할만한 코드


# while을 사용한 경우
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
    
    
# for와 if를 사용한 경우
def gcdlcm(a, b):
    for i in range(a):
        if a%(a-i)+b%(a-i) == 0:
            return [a-i, a*b/(a-i)]
            
            
# 람다를 사용한 경우
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]


출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

'''
