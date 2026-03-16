import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
lst = list(map(int, readline().split()))

answer = 0

def merge_sort(s, e):
    global lst, answer
    
    if e - s < 1:
        return
    
    if e - s == 1 and lst[s] > lst[e]:
        lst[s], lst[e] = lst[e], lst[s]
        answer += 1
    
    s1, e1 = s, s + (e - s) // 2
    s2, e2 = e1 + 1, e
    
    merge_sort(s1, e1)
    merge_sort(s2, e2)
    
    # 병합
    tmp = []
    k = s
    while s1 <= e1 and s2 <= e2:
        if lst[s1] > lst[s2]:
            tmp.append(lst[s2])
            answer += s2 - k
            s2 += 1
            k += 1
        else:
            tmp.append(lst[s1])
            s1 += 1
            k += 1
    
    while s1 <= e1:
        tmp.append(lst[s1])
        s1 += 1
        k += 1
    
    while s2 <= e2:
        tmp.append(lst[s2])
        s2 += 1
        k += 1
    
    j = 0
    for i in range(s, e + 1):
        lst[i] = tmp[j]
        j += 1

    return

merge_sort(0, len(lst) - 1)
write(str(answer))