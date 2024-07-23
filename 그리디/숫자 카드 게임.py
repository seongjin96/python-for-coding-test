n, m = map(int, input().split())

result = 0

for _ in range(n):
    data = list(map(int, input().split()))  # 한 줄씩 입력 받기
    result = max(result, min(data))     # 각 줄의 가장 작은 수들 중에 가장 큰 수 찾기

print(result)
