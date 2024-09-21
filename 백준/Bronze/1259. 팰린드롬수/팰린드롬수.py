while True:
    string = input()
    if string == '0':
        break
    l, r = 0, len(string) - 1
    is_pal = True
    while l < r:
        if string[l] == string[r]:
            l += 1
            r -= 1
            continue
        else:
            is_pal = False
            break

    print('yes' if is_pal else 'no')