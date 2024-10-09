def solution(edges):
    # 0: 생성한 정점의 번호, 1: 도넛 모양, 2: 막대 모양, 3: 8자 모양
    answer = [0, 0, 0, 0]
    
    # 각 노드의 들어오는 노드의 개수와 나가는 노드의 개수를 저장할 배열
    node_info = {}
    for u, v in edges:
        if not node_info.get(u):
            node_info[u] = [0, 0]
        if not node_info.get(v):
            node_info[v] = [0, 0]
        
        node_info[v][1] += 1
        node_info[u][0] += 1
    
            
    for i, counts in node_info.items():
        out_cnt, in_cnt = counts
        # 나가는 노드의 개수가 0일 경우 -> 막대 모양 그래프
        if out_cnt == 0 and in_cnt != 0:
            answer[2] += 1
        # 나가는 노드의 개수가 2초과 일 경우 -> 생성자 노드
        elif out_cnt >= 2 and in_cnt == 0:
            answer[0] = i
        # 나가는 노드의 개수가 2일 경우 -> 8자 모양 그래프
        elif out_cnt >= 2 and in_cnt >= 2:
            # 그 중 들어오는 노드의 개수가 0인 경우 -> 생성자의 나가는 노드가 2개일 경우의 생성자 노드
            answer[3] += 1 
            
    answer[1] = node_info[answer[0]][0] - answer[2] - answer[3]
            
    return answer