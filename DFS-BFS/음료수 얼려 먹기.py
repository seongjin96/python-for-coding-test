n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


visited = [[0] * m for _ in range(n)]   # 방문 확인 그래프
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0


def dfs(y, x):
    visited[y][x] = 1

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                dfs(ny, nx)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
