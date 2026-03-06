# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 카드의 행 중 가장 작은 숫자를 넣을 리스트
card = []
for i in range(n):
    # 한 줄씩 입력받기
    tmp = list(map(int, input().split()))
    # 가장 작은 원소 추가하기
    card.append(min(tmp))

# 가장 큰 원소 출력하기
print(max(card))