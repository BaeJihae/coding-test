n, m = map(int, input().split())
set1, set2 = set(), set()

for _ in range(n):
    set1.add(input())

for _ in range(m):
    set2.add(input())

intersection = list(set1.intersection(set2))
intersection.sort()

print(len(intersection))
[print(name) for name in intersection]