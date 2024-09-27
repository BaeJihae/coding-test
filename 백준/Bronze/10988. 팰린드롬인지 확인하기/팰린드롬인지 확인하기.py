string = input()
n = len(string)

if string == string[::-1]:
    print(1)
else:
    print(0)