'''
버블 소트 알고리즘을 다음과 같이 C++로 작성했다.

bool changed = false;
for (int i=1; i<=N+1; i++) {
    changed = false;
    for (int j=1; j<=N-i; j++) {
        if (A[j] > A[j+1]) {
            changed = true;
            swap(A[j], A[j+1]);
        }
    }
    if (changed == false) {
        cout << i << '\n';
        break;
    }
}
위 소스에서 N은 배열의 크기이고, A는 정렬해야 하는 배열이다. 배열은 A[1]부터 사용한다.

위와 같은 소스를 실행시켰을 때, 어떤 값이 출력되는지 구해보자.
'''

import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) # n

L = list()
for i in range(N):
    L.append((int(readline()), i))

sortedL = sorted(L)
answer = 0

for j in range(N):
    if answer < sortedL[j][1] - j:
        answer = sortedL[j][1] - j

print(answer + 1)

# 첫번째 풀이했던 딕셔너리로 풀이를 한다면, 같은 값일 경우 값이 덮어씌어져서 틀림.