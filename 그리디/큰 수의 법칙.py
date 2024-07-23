n, m, k = map(int, input().split())
data = list(map(int, input().split()))

answer = 0

data.sort()     # 입력 받은 수 정렬
first = data[-1]    # 가장 큰 수
second = data[-2]   # 두 번째로 큰 수

count = m // (k + 1)    # 두 번째로 큰 수가 더해지는 횟수

answer += second * count    # 두 번째로 큰 수 더하기
answer += first * (m - count)   # 첫 번째로 큰 수 더하기

print(answer)
