import sys
from collections import Counter

input = sys.stdin.readline

# 입력
n = int(input())

subways_dict = dict()  # 지하철 번호 기억하는 딕셔너리
features = dict()      # 특징 번호 기억하는 딕셔너리
subways_map = [0] * n
bitmask_counter = Counter()

# 지하철역 번호로 기억하는 딕셔너리
for i in range(n):
    subways_dict[input().strip()] = i

def update(subway, new_features):
    subway_idx = subways_dict[subway]
    old_mask = subways_map[subway_idx]
    if old_mask != 0:
        bitmask_counter[old_mask] -= 1

    bitmask = 0
    for ft in new_features:
        if ft not in features.keys():
            features[ft] = len(features)
        bitmask |= (1 << features[ft])

    subways_map[subway_idx] = bitmask
    bitmask_counter[bitmask] += 1

def answer(search_features):
    search_mask = 0

    for ft in search_features:
        if ft not in features.keys():
            return 0
        search_mask |= (1 << features[ft])

    cnt = 0
    for mask, num in bitmask_counter.items():
        if (mask & search_mask) == search_mask:
            cnt += num
    return cnt

# 출력
r = int(input())

for i in range(r):
    tmp = list(input().split())
    if tmp[0] == "U":
        # 업데이트 함수 호출
        update(tmp[1], list(tmp[2].split(",")))
    elif tmp[0] == "G":
        # 출력 함수 호출
        print(answer(tmp[1].split(",")))
