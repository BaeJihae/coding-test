# 어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 
# 당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서, 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다. 
# 이때, 사용하는 자연수는 N이하여야 한다.
# 예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지가 있다.
# N을 입력받아 가지수를 출력하는 프로그램을 작성하시오.

import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # N

answer = 1  # 연속된 자연수의 합으로 N을 만들 가짓수 (자기자신포함)

# # n // 2 + 1 만큼의 누적합 생성
# S = [0]
# m = n // 2 + 1
# for i in range(1, m + 1):
#     S.append(S[i-1] + i)

# # i, j 투 포인터 움직이면서 n 값 찾기
# i, j = 0, 1
# while(i <= j):
#     if S[j] - S[i] < n: 
#         j += 1
#     elif S[j] - S[i] == n:
#         answer += 1
#         j += 1
#         i += 1
#     else:
#         i += 1
    
#     if j > m:
#         break

# write(str(answer))

# 메모리 초과 엔딩 / 메모리 제한이 32MB
# 파이썬에서 정수 리스트 10,000,000 개를 만들면 360MB의 메모리를 차지함.

i, j = 0, 1
sumI = 0
sumJ = 1
while(i <= j):
    if sumJ - sumI < n: 
        j += 1
        sumJ += j
    elif sumJ - sumI == n:
        answer += 1
        j += 1
        i += 1
        sumJ += j
        sumI += i
    else:
        i += 1
        sumI += i
    
    if j > n // 2 + 1:
        break

write(str(answer))