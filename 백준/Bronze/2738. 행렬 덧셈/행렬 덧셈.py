N, M = map(int,input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(N)]
matrix_2 = [list(map(int, input().split())) for _ in range(N)]

matrix_sum = [[x + y for x, y in zip(m_1, m_2)] for m_1, m_2 in zip(matrix_1, matrix_2)]

print('\n'.join(' '.join(map(str, mtrx)) for mtrx in matrix_sum))