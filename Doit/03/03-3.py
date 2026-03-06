# 1부터 100,000까지 곱한 값을 1,000,000,007로 나눈 나머지를 구하시오.

import sys, time
print = sys.stdout.write

MOD = 1000000007

# 나머지 연산을 사용하지 않을 때,
start = time.time()

answer = 1
for i in range(1, 100001):
    answer *= i

end = time.time()

print(f'결과 : {str(answer % MOD)}\n')
print(f'걸린 시간 : {end - start}\n')

# 나머지 연산을 사용할 때,
start = time.time()

answer = 1

for i in range(1, 100001):
    answer = (answer * i) % MOD

end = time.time()

print(f'결과 : {str(answer)}\n')
print(f'걸린 시간 : {end - start}\n')