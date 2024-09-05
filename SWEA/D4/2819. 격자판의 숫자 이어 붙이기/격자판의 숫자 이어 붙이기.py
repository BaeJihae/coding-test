N = 4

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(idx, row, col, result):
    global answer, record
    
    # 기저조건
    if idx == 7:
        answer.add(result)
        return
    
    for k in range(4):
        next_x, next_y = row + dx[k], col + dy[k]
        
        # 인덱스 범위 체크
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
            continue
            
        # 다음 결과
        new_result = result + lst[next_x][next_y]
        
        # 가지치기
        # -> 현재의 좌표값과 결과값이 이미 있는 경우를 제외하고 재귀호출
        if (next_x, next_y, new_result) not in record:
            dfs(idx + 1, next_x, next_y, new_result)
            record.add((next_x, next_y, new_result))


for tc in range(1, int(input()) + 1):
    # 출력
    lst = [list(input().split()) for _ in range(N)]
    
    # 좌표와 결과값을 저장
    record = set()
    # 7자리의 수를 저장
    answer = set()
    
    for row in range(N):
        for col in range(N):
            dfs(0, row, col, '')
            
    # 출력
    print(f'#{tc}', len(answer))
