from collections import defaultdict

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    start_x, start_y = map(int, f.readline().strip().split(','))
    end_x, end_y = map(int, f.readline().strip().split(','))


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N


def bfs(start_x, start_y, end_x, end_y, N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    start = (start_x, start_y)
    end = (end_x, end_y)
    queue = [start]
    visited[start_x][start_y] = 0

    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    while queue:
        current_x, current_y = queue.pop(0)

        if (current_x, current_y) == end:
            return visited[current_x][current_y]

        for k in range(8):
            new_x, new_y = current_x + row[k], current_y + col[k]
            if is_valid(new_x, new_y, N) and not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = visited[current_x][current_y] + 1

    return -1


graph = Graph()
shortest_path = bfs(start_x, start_y, end_x, end_y, N)
if shortest_path != -1:
    with open('result.txt', 'w') as f:
        f.write(f"Shortest path: {shortest_path} moves")
else:
    with open('result.txt', 'w') as f:
        f.write("No valid path found")
