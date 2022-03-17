'''
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.


제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.


해결 방법
1. 리스트의 각 요소들의 합계를 구한다
2. 리스트의 요소 수를 구한다
3. 합계와 요소 수를 나눈다

*sum과 for문 등으로 문제를 해결 할 수 있다.
'''


# sum의 경우
def solution(arr):
    return sum(arr)/len(arr)


# for의 경우
def solution(arr):
    a = 0

    for i in arr:
        a += i

    return a/len(arr)
