import sys

readline = sys.stdin.readline
write = sys.stdout.write

N, K = map(int, readline().split())
A = list(map(int, readline().split()))

def quick_sort(start, end, K):
    global A
    if start < end:
        pivot = search_pivot(start, end)
        if pivot == K:
            return
        elif K < pivot:
            quick_sort(start, pivot - 1, K)
        else:
            quick_sort(pivot + 1, end, K)

def search_pivot(start, end):
    global A
    
    if start + 1 == end:
        if A[start] > A[end]:
            A[start], A[end] = A[end], A[start]
        return end
    
    M = (start + end) // 2
    A[start], A[M] = A[M], A[start]
    
    pivot = A[start]
    i, j = start + 1, end
    
    while i <= j:
        while A[i] < pivot and i < len(A)-1:
            i += 1
        while A[j] >= pivot and j > 0:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    
    A[start] = A[j]
    A[j] = pivot
    return j

quick_sort(0, N - 1, K - 1)
print(A[K - 1])