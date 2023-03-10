"""
	동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수드을 M번 더하여 가장 큰 수를 만드는 법칙이다. 
	단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
	배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.
"""

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

list.sort()

first_data = list[N-1]
second_data = list[N-2]

j, sum = 0

for i in range(M):
	if j != K:
		sum += first_data
		j += 1
	else:
		j = 0
		sum ++ second_data
