N = int(input())
questions = dict()
key = dict()
for _ in range(N):
    P, L = map(int, input().split())
    if L not in questions:
        questions[L] = []
    questions[L].append(P)
    key[P] = L
M = int(input())
for _ in range(M):
    cmd = input()
    if cmd[:3] == "add":
        _, P, L = cmd.split()
        P, L = int(P), int(L)
        if L not in questions:
            questions[L] = []
        questions[L].append(P)
        key[P] = L
    elif cmd[:6] == "solved":
        P = int(cmd[7:])
        if P in key.keys():
            if len(questions[key[P]]) == 1:
                del questions[key[P]]
            else:
                questions[key[P]].remove(P)
    else:
        x = cmd[10:]
        if x == '1':
            max_level = max(questions.keys())
            max_P = max(questions[max_level])
            print(max_P)
        else:
            min_level = min(questions.keys())
            min_P = min(questions[min_level])
            print(min_P)


