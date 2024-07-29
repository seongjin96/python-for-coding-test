from collections import deque

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(y, x, cnt):
    queue = deque([(y, x, cnt)])
    visited[y][x] = 1

    while queue:
        y, x, cnt = queue.popleft()

        if y == n - 1 and x == m - 1:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx, cnt + 1))
    return -1


print(bfs(0, 0, 1))
