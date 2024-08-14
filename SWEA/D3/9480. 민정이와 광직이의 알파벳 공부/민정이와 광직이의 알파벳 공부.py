# 민정이와 광직이의 알파벳 공부
# 부분집합과 합집합을 이용한 풀이
for tc in range(1, int(input()) + 1):

    # 입력
    N = int(input())
    alphabet_set_lst = []
    for _ in range(N):
        alphabet_set_lst.append(set(list(input().strip())))

    # 알파벳 단어 세트 개수
    answer = 0

    # 부분집합 생성 후 단어 세트 확인
    def subset(idx, bits):
        if idx == N:
            # 부분집합의 알파벳의 합집합 생성
            word_set = set()
            for i in range(N):
                if bits[i] == 1:
                    word_set = word_set.union(alphabet_set_lst[i])
            # 알파벳 개수가 26개라면 알파벳 단어 세트 완성
            if len(word_set) == 26:
                return 1
            return 0

        return subset(idx + 1, bits + [1]) + subset(idx + 1, bits + [0])

    # 부분집합 함수 실행
    answer = subset(0, [])

    # 출력
    print(f'#{tc} {answer}')