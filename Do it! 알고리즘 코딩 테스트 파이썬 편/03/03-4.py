import sys

write = sys.stdout.write

# 오름차순 정렬
A = [3, 4, 1, 2, 6, 5]
write('리스트 A : ' + ' '.join(map(str, A)) + '\n')

B = sorted(A)
write('복사된 오름차순 리스트 B : ' + ' '.join(map(str, B)) + '\n')

A.sort()
write('오름차순 리스트 A : ' + ' '.join(map(str, A)) + '\n')

# 내림차순 정렬 1
B = sorted(A, reverse=True)
write('복사된 내림차순 리스트 B : ' + ' '.join(map(str, B)) + '\n')

A.sort(reverse=True)
write('내림차순 리스트 A : ' + ' '.join(map(str, A)) + '\n')

# 내림차순 정렬 2
A = [-a for a in A]

B = sorted(A)
B = [-b for b in B]
write('복사된 오름차순 리스트 B : ' + ' '.join(map(str, B)) + '\n')

A.sort()
A = [-a for a in A]
write('오름차순 리스트 A : ' + ' '.join(map(str, A)) + '\n')