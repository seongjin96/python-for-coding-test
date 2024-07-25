n, m = map(int, input().split())

# 방문한 위치를 저장 하기 위한 맵을 생성하여 0으로 초기화
visited = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X,Y 좌표, 방향 입력 받기
y, x, direction = map(int, input().split())
visited[y][x] = 1  # 현재 좌표 방문 처리

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visited[ny][nx] == 0 and maps[ny][nx] == 0:
        visited[ny][nx] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if maps[ny][nx] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 박혀있는 경우
        else:
            break
        turn_time = 0

print(count)
