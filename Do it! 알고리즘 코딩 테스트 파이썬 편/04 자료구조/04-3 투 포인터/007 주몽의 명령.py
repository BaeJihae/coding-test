# 주몽은 철기군을 양성하기 위한 프로젝트에 나섰다. 
# 그래서 야철대장을 통해 철기군이 입을 갑옷을 만들게 하였다. 
# 야철대장은 주몽의 명에 따르기 위하여 연구에 착수하던 중 아래와 같은 사실을 발견하게 되었다.

# 갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다. 
# 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다.
# 야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다.
# 이러한 궁금증을 풀어 주기 위하여 N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.

import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # 재료의 개수 N
m = int(readline()) # 갑옷을 만드는데 필요한 수 M
# n개의 재료들이 가진 고유한 번호
numbers = list(map(int, readline().split()))
numbers.sort()

answer = 0

startIndex, endIndex = 0, n - 1
while(startIndex < endIndex):
    sumOfTwoNumber = numbers[startIndex] + numbers[endIndex]
    if sumOfTwoNumber == m:
        answer += 1
        startIndex += 1
        endIndex -= 1
    elif sumOfTwoNumber < m:
        startIndex += 1
    else:
        endIndex -= 1

write(str(answer))