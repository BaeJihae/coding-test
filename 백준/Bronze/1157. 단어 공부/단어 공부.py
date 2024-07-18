word = input()

word_dict = {}

for i in word.lower():
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

values_list = list(word_dict.values())

if values_list.count(max(values_list)) > 1:
    print('?')
else:
    print(max(word_dict, key=word_dict.get).upper())