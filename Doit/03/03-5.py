import sys
write = sys.stdout.write

# 튜플 기반 다중 조건 정렬
scores = [
    (80 , 100),
    (100, 50),
    (70, 100),
    (80, 90)
]

# 영어 내림차순, 수학 내림차순 순으로 정렬
scores.sort(key=lambda x : (-x[0], -x[1]))

for english, math in scores:
    write(f'영어성적 : {english}, 수학성적 : {math}\n')
    
# 딕셔너리 기반 다중 조건 정렬
scores = [
    {'english' : 80, 'math' : 100},
    {'english' : 100, 'math' : 50},    
    {'english' : 70, 'math' : 100},    
    {'english' : 80, 'math' : 90},
]

# 영어 내림차순, 수학 내림차순 순으로 정렬
scores.sort(key=lambda x: (-x['english'], -x['math']))

for a in scores:
    write(f'영어성적 : {a['english']}, 수학성적 : {a['math']}\n')