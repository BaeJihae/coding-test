# 입력
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 한 줄 병합하기
def merge_block(lst):
    new_lst = []
    # 이미 병합이 된 곳인지 확인
    merged = [False] * N

    for i in range(N):
        # 0이 아니라면
        if lst[i] != 0:
            # 처음 0이 아닌 숫자 탐색이라면
            if not new_lst:
                new_lst.append(lst[i])
            else:
                # 병합할 번호
                if new_lst[-1] == lst[i] and not merged[len(new_lst) - 1]:
                    num = new_lst.pop()
                    new_lst.append(num * 2)
                    merged[len(new_lst) - 1] = True
                # 병합하지 않는 번호
                else:
                    new_lst.append(lst[i])

    # 0 채우기
    while len(new_lst) != N:
        new_lst.append(0)

    return new_lst


# 0:상, 1:하, 2:좌, 3:우
def game_progression(idx, lst):
    global answer
    
    # 5번의 이동 후에 최댓값 찾기
    if idx == 5:
        cnt = max(max(row) for row in lst)
        answer = max(answer, cnt)
        return
    
    # 상, 하, 좌, 우로 이동
    for k in range(4):
        new_lst = [[0] * N for _ in range(N)]
        # 상
        if k == 0:
            for i in range(N):
                tmp = [lst[j][i] for j in range(N)]
                merged = merge_block(tmp)

                for z in range(N):
                    new_lst[z][i] = merged[z]
        # 하
        elif k == 1:
            for i in range(N):
                tmp = [lst[j][i] for j in range(N - 1, -1, -1)]
                merged = merge_block(tmp)

                for z in range(N):
                    new_lst[N - 1 - z][i] = merged[z]
        # 좌
        elif k == 2:
            for i in range(N):
                merged = merge_block(lst[i])
                new_lst[i] = merged
        # 우
        elif k == 3:
            for i in range(N):
                merged = merge_block(lst[i][::-1])
                new_lst[i] = merged[::-1]

        # 재귀함수 실행
        game_progression(idx + 1, new_lst)

# 로직 실행
answer = 0
game_progression(0, lst)

# 출력 
print(answer)
