import sys
sys.setrecursionlimit(100000)

def solution(numbers, target):
    answer = 0
    
    def dfs(i, result):
        nonlocal answer
        if i == len(numbers) and result == target:
            answer += 1
            return
        
        if i < len(numbers):
            dfs(i + 1, result + numbers[i])
            dfs(i + 1, result - numbers[i])

    dfs(0, 0)
    
    return answer