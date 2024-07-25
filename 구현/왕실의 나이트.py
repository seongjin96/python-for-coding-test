data = input()
row = int(data[1])
col = int(ord(data[0]) - ord('a')) + 1
n = 8
result = 0

# 나이트가 이동할 수 있는 8가지 방향 정의
roads = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]


# 이동한 방향이 이동 가능한 영역인지 확인
def check_possible(y, x):
    if 0 < y <= n and 0 < x <= n:
        return True
    return False


for road in roads:
    # 해당 위치로 이동이 가능할 경우 카운트 증가
    if check_possible(row + road[0], col + road[1]):
        result += 1

print(result)
