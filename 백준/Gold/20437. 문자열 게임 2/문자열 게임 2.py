from collections import defaultdict 

tc = int(input())

for _ in range(tc):
    word = input()
    k = int(input())
    
    alphabet_dict = defaultdict()
    checked_arr = [False]*len(word)

    tmp = []

    for i, w in enumerate(word):
        if alphabet_dict.get(w) == None :
            alphabet_dict[w] = [i]
        else:
            alphabet_dict[w].append(i)

    for (key, value) in alphabet_dict.items():
        if len(value) >= k:
            for i in range(0, len(value) - k + 1):
                tmp.append(value[i + k - 1] - value[i] + 1)

    if tmp == []:
        print(-1)
    else:
        print(min(tmp), max(tmp))