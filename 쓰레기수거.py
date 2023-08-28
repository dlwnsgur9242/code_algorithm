from collections import deque

def bfs(start, n, m, grid):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start, 0)])
    visited[start[0]][start[1]] = True

    while queue:
        current, distance = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append(((nx, ny), distance + 1))
    
    return distance

def find_safest_distance(n, m, grid):
    max_safest_distance = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                safest_distance = bfs((i, j), n, m, grid)
                max_safest_distance = max(max_safest_distance, safest_distance)
    
    return max_safest_distance

# 입력 받기
n, m = map(int, input().split())
grid = []

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 안전 거리 최댓값 계산 및 출력
result = find_safest_distance(n, m, grid)
print(result)