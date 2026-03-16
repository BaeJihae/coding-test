# 내가 구현한 퀵 정렬
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
    
    quick_sort(s, k - 1)
    quick_sort(k + 1, e)
    
    return

quick_sort(0, len(lst) - 1)
print(lst)

# 문제점1. deque를 사용해서 appendleft 할 때 순서가 뒤집힘.
# 문제점2. 매번 deque를 생성하여 퀵 정렬의 장점인 리스트 내에서 swap 형태가 이루어 지지 않음.


# 해결한 코드
lst = [4, 2, 6, 3, 9, 1, 8, 10, 13, 41]

def quick_sort(s, e):
    global lst

    if s >= e:
        return

    # 중간 pivot 선택
    m = s + (e - s) // 2
    pivot = lst[m]

    # pivot을 맨 앞으로 이동
    lst[s], lst[m] = lst[m], lst[s]

    k = s  # pivot 위치

    # partition
    for i in range(s + 1, e + 1):
        if lst[i] < pivot:
            k += 1
            lst[i], lst[k] = lst[k], lst[i]

    # pivot을 제자리로 이동
    lst[s], lst[k] = lst[k], lst[s]

    quick_sort(s, k - 1)
    quick_sort(k + 1, e)


quick_sort(0, len(lst) - 1)
print(lst)