word = ['c=','c-','dz=','d-','lj','nj','s=','z=']

croatia = input()

answer = 0

while croatia != '':
    if croatia[:2] in word:
        answer += 1
        croatia = croatia[2:]
    elif croatia[:3] in word:
        answer += 1
        croatia = croatia[3:]
    else:
        answer += 1
        croatia = croatia[1:]

print(answer)