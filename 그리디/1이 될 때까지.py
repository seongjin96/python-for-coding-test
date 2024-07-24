n, k = map(int, input().split())

result = 0

while True:
    # N이 1이 되면 탈출
    if n == 1:
        break

    # N이 K로 나누어 떨어질 경우
    if n % k == 0:
        n //= k
    # N이 K로 나눌 수 없을 때 1씩 빼기
    else:
        n -= 1

    result += 1

print(result)
