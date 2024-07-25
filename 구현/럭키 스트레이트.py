n = input()

left_sum, right_sum = 0, 0
mid = len(n) // 2   # 점수 값의 중간 자릿수 

# 왼쪽 부분의 자릿수 합 더하기
for i in range(0, mid):
    left_sum += int(n[i])

# 오른쪽 부분의 자릿수 합 더하기
for i in range(mid, len(n)):
    right_sum += int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
