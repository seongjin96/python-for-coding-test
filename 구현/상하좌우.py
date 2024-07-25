n = int(input())
roads = list(map(str, input().split()))

x, y = 1, 1

for direction in roads:
    if direction == 'R' and x + 1 <= n:
        x += 1
    elif direction == 'L' and x - 1 > 0:
        x -= 1
    elif direction == 'U' and y - 1 > 0:
        y -= 1
    elif direction == 'D' and y + 1 <= n:
        y += 1
    else:
        continue

print(y, x)
