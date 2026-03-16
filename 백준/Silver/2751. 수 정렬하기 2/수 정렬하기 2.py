import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
numbers = [int(readline()) for _ in range(N)]

# 두 개의 배열 병합하기
def merge(s, e):
    global numbers
    
    if e - s == 1 and numbers[s] > numbers[e]:
        numbers[s], numbers[e] = numbers[e], numbers[s]
    
    if e - s > 1:
        s1, e1 = s, s + (e - s) // 2
        s2, e2 = e1 + 1, e
        
        merge(s1, e1)
        merge(s2, e2)
        
        tmp = []
        while s1 <= e1 and s2 <= e2:
            if numbers[s1] < numbers[s2]:
                tmp.append(numbers[s1])
                s1 += 1
            else:
                tmp.append(numbers[s2])
                s2 += 1
        
        while s1 <= e1:
            tmp.append(numbers[s1])
            s1 += 1

        while s2 <= e2:
            tmp.append(numbers[s2])
            s2 += 1

        # tmp를 리스트에 적용
        j = 0
        for i in range(s, e + 1):
            numbers[i] = tmp[j]
            j += 1

    return 0

merge(0, len(numbers) - 1)

for num in numbers:
    write(str(num) + "\n")