import sys

readline = sys.stdin.readline
write = sys.stdout.write

S, P = map(int, readline().split()) # DNA 문자열의 길이, 부분 문자열의 길이
dnaStr = list(readline()) # DNA 문자열
condition = list(map(int, readline().split())) # A, C, G, T 의 최소 개수
current = [0, 0, 0, 0]  # A, C, G, T의 현재 개수

def addStr(char):
    match char:
        case 'A':
            current[0] += 1
        case 'C':
            current[1] += 1
        case 'G':
            current[2] += 1
        case 'T':
            current[3] += 1

def deleteStr(char):
    match char:
        case 'A':
            current[0] -= 1
        case 'C':
            current[1] -= 1
        case 'G':
            current[2] -= 1
        case 'T':
            current[3] -= 1

def check():
    for i in range(4):
        if current[i] < condition[i]:
            return False
    return True

s, e = 0, P - 1
# 처음 s~e까지의 문자열 저장
for i in range(s, e + 1):
    addStr(dnaStr[i])

answer = 0
while(e < S):
    if check():
        answer += 1
    
    deleteStr(dnaStr[s])
    s += 1
    e += 1
    addStr(dnaStr[e])

write(str(answer))