n = int(input())

answer = 0

for i in range(n):
    word = input()

    check = False

    char_list = []
    for char in word:
        if char_list == [] or char_list[-1] != char:
            if char in char_list:
                check = True
                break
            char_list.append(char)

    if check == True:
        continue

    answer += 1

print(answer)