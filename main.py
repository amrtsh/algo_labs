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
    start = (start_x, start_y)
    end = (end_x, end_y)
    visited = set()
    visited.add(start)
    queue = [(start, 0)]
    counter = 0
    coordinates = {}

    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    while queue:
        (current_x, current_y), move = queue.pop(0)
        counter += 1

        if (current_x, current_y) == end:
            path = [(end_x, end_y)]
            while (end_x, end_y) != start:
                end_x, end_y = coordinates[(end_x, end_y)]
                path.append((end_x, end_y))
            path.reverse()
            return move, counter, path

        for k in range(8):
            new_x, new_y = current_x + row[k], current_y + col[k]
            if is_valid(new_x, new_y, N) and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), move + 1))
                visited.add((new_x, new_y))
                coordinates[(new_x, new_y)] = (current_x, current_y)

    return -1, counter, []


graph = Graph()
shortest_path, counter, path = bfs(start_x, start_y, end_x, end_y, N)
if shortest_path != -1:
    with open('result.txt', 'w') as f:
        f.write(f"Shortest path: {shortest_path} moves\n")
        f.write(f"Number of iterations (counter): {counter}\n")
        f.write(f"Path: {path}\n")
else:
    with open('result.txt', 'w') as f:
        f.write("No valid path found")
