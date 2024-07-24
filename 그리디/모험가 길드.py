n = int(input())
scared = list(map(int, input().split()))
result = 0

idx = 0
max_scared = 0
count = 1

scared.sort()

while idx < len(scared):
    max_scared = max(max_scared, scared[idx])

    if count == max_scared:
        result += 1
        count = 0

    idx += 1
    count += 1

print(result)
