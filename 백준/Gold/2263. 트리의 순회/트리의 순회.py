import sys
sys.setrecursionlimit(10**6)

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

answer = []

in_order_idx = {value: idx for idx, value in enumerate(in_order)}

# 재귀함수
def tree_search(in_order_s, in_order_e, post_order_s, post_order_e):
    if in_order_s > in_order_e:
        return

    # 루트 노드의 번호
    root_node = post_order[post_order_e]
    # 루트 노드의 인덱스
    root_idx = in_order_idx[root_node]
    # 왼쪽 서브 노드의 원소 개수
    left_count = root_idx - in_order_s

    # 루트 노트를 정답에 추가
    answer.append(root_node)

    tree_search(in_order_s, root_idx - 1, post_order_s, post_order_s + left_count - 1)
    tree_search(root_idx + 1, in_order_e, post_order_s + left_count, post_order_e - 1)

# 재귀함수 실행
tree_search(0, N - 1, 0, N - 1)
print(*answer)