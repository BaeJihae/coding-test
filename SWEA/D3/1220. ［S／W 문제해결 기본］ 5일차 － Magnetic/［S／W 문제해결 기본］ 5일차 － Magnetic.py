# 1220. Magnetic
for tc in range(1, 11):

   N = int(input())
   arr = [ list(map(int, input().split())) for _ in range(N)]
   answer = 0

   for lst in list(zip(*arr)):
      stack = []
      cnt = 0
      for k in lst:
         if k == 1:
            stack.append(1)
         elif stack and stack[-1] == 1:
            if k == 2:
               stack.append(k)
               answer += 1
            elif k == 1:
               stack.append(k)
         cnt += 1
      if cnt == 1:
         answer = 0

   print(f'#{tc} {answer}')