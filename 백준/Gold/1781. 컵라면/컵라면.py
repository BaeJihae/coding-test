import heapq

N = int(input())
lst = list()

for _ in range(N):
    d, c = map(int, input().split())
    lst.append((d, c))

lst.sort()

heap = []
for d, c in lst:
    heapq.heappush(heap, c)
    if len(heap) > d:        
        heapq.heappop(heap) 

print(sum(heap))