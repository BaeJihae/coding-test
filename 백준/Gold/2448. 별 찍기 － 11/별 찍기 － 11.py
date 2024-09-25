n = int(input())
STAR = ['  *  ', ' * * ', '*****']

def solution(star, num):
    nxt_star = []
    for s in star:
        nxt_star.append(' ' * num + s + ' ' * num)
    for s in star:
        nxt_star.append(s + ' ' + s)

    if num == n:
        for s in star:
            print(s)
        return
    else:
        num *= 2
        solution(nxt_star, num)


solution(STAR, 3)