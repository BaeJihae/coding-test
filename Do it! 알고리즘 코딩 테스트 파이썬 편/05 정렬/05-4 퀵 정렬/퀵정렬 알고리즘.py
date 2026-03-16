from collections import deque

lst = [4, 2, 6, 3, 9, 1, 8, 10, 13, 41]

def quick_sort(s, e):
    global lst
    
    if e <= s:
        return
    elif e - s == 1 and lst[s] > lst[e]:
        lst[s], lst[e] = lst[e], lst[s]
        return
    
    # 중간값 찾기
    m = s + (e - s) // 2
    div = lst[m]
    
    # div 값과 젤 앞값 변경하기
    lst[s], lst[m] = lst[m], lst[s]
    
    tmp = deque()
    tmp.append(div)
    
    # 비교하여 값 넣기
    i, j, k = s + 1, e, s
    while i <= j:
        if lst[i] < div:
            tmp.appendleft(lst[i])
            k += 1
        else:
            tmp.append(lst[i])
        i += 1
    
    for i in range(s, e + 1):
        lst[i] = tmp.popleft()
    
    print(f's: {s}, e: {e}, lst: {lst}')
    
    quick_sort(s, k - 1)
    quick_sort(k + 1, e)
    
    return

quick_sort(0, len(lst) - 1)
print(lst)