lst = [4, 5, 6, 3, 2, 1, 7, 10, 8, 9]

# 가장 큰 단위 부터 아래로 내려가는 탑 다운 재귀함수를 사용해야함.
# 새로운 리스트를 만드는 것 보다 기존에 있던 리스트를 활용해 값을 변경하면서 내려가면 됨.

def merge_sort(s, e):
    global lst
    
    if e - s == 1 and lst[s] > lst[e]:
        lst[s], lst[e] = lst[e], lst[s]

    if e - s > 1:    
        s1, e1 = s, (e - s) // 2 + s
        s2, e2 = e1 + 1, e
        
        merge_sort(s1, e1)
        merge_sort(s2, e2)

        # 합칠때 필요한 임시 리스트
        tmp_lst = []
        while s1 <= e1 and s2 <= e2:
            if lst[s1] < lst[s2]:
                tmp_lst.append(lst[s1])
                s1 += 1
            else:
                tmp_lst.append(lst[s2])
                s2 += 1
        
        while s1 <= e1:
            tmp_lst.append(lst[s1])
            s1 += 1

        while s2 <= e2:
            tmp_lst.append(lst[s2])
            s2 += 1
        
        # 합친 후 리스트 교체
        j = 0
        for i in range(s, e + 1):
            lst[i] = tmp_lst[j]
            j += 1

    return 0

merge_sort(0, len(lst) - 1)

print(lst)