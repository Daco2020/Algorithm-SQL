'''
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.


제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.


해결 방법
1. 최종 리턴할 리스트를 생성한다
2. 내장함수 zip과 for를 이용하여 각 리스트의 요소를 분리한다
3. 반복 시 초기화되는 임시 리스트를 생성한다
4. 다시 각 리스트의 요소를 분리한다
5. 분리된 요소끼리 더한 값을 임시 리스트에 추가한다
6. 최종 리스트에 임시 리스트를 요소로 추가한다
7. 최종 리스트를 반환한다
'''


def solution(arr1, arr2):

    answer_list = []

    for i, j in zip(arr1, arr2):
        temp_list = []

        for a, b in zip(i, j):
            temp_list.append(a + b)

        answer_list.append(temp_list)

    return answer_list
