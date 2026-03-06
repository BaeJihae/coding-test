# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
readline = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, readline().split())

# stack은 현재 순열 리스트
stack = []
# 현재 순열 리스트에 들어간 여부
remember = [0] * (n+1)

def bfs():
    if len(stack) == m:
        write(' '.join(map(str, stack)) + '\n')
    
    for i in range(1, n+1):
        if remember[i] == 0:
            remember[i] = 1
            stack.append(i)

            bfs()
            
            stack.pop()
            remember[i] = 0

bfs()