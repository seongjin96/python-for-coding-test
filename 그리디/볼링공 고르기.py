n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0
cnt = 0     # 같은 무게의 볼링공 개수 체크

for i in range(len(data) - 1):
    cnt += 1
    # (같은 무게의 볼링공 개수 * 남은 볼링공 개수)를 더해준다.
    if data[i] != data[i+1]:
        result += (cnt * (n - i - 1))
        cnt = 0

print(result)
