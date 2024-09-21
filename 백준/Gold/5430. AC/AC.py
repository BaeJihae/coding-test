import sys
import re

input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):  # 테스트 케이스만큼 반복
    p = input()  # 명령어
    n = int(input())
    lst = list(re.split(r'[\[\],]', input()))
    lst = [x for x in lst if x]  # 빈 문자열 제거

    reverse = False  # 앞에서 삭제해야하는지 뒤에서 삭제해야하는지를 파악
    is_error = False
    l, r = 0, n  # 왼쪽의 인덱스 번호, 오른쪽의 인덱스 번호
    for s in p:
        if s == 'R':  # R: 뒤집기(배열에 있는 수의 순서 뒤집기)
            reverse = not reverse
        elif reverse:  # D : 버리기(마지막 수 버리기)
            r -= 1
        elif not reverse:  # D : 버리기(첫 번째 수 버리기)
            l += 1

        if r < l:  # 에러
            is_error = True
            break

    if is_error:
        print('error')
    else:
        answer = lst[l:r]

        if not answer:
            print('[]')
        else:
            if reverse:
                answer.reverse()

            print('[', end='')
            for string in answer[:-1]:
                print(string, end=',')
            print(answer[-1], end='')
            print(']')
