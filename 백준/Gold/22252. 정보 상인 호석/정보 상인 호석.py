from collections import defaultdict, deque

# 고릴라가 얻은 정보의 수
Q = int(input())

# 특정 고릴라가 얻은 정보의 가치를 가지는 키와 값
info_dict = defaultdict()

# 호석이가 가진 정보들의 가치 총합
answer = 0

for _ in range(Q):
    cmd = list(input().split())
    i, name, count = int(cmd[0]), cmd[1], int(cmd[2])
    
    # 고릴라가 정보를 얻음.
    if i == 1:
        array = list(map(int, cmd[3:]))
        if name not in info_dict:
            info_dict[name] = deque(sorted(array, reverse=True))
        else:
            info_dict[name] = deque(sorted(list(info_dict[name]) + array, reverse=True))
    # 호식이가 정보를 캘때.
    if i == 2 and name in info_dict:
        if len(info_dict[name]) <= count:
            answer += sum(list(info_dict[name]))
            info_dict[name] = deque()
        else:
            for i in range(count):
                answer += info_dict[name].popleft()
    
print(answer)