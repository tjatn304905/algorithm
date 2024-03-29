import sys
sys.stdin = open('sample_input.txt')

def dfs(matrix, x, y):
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]
    stack = [[x, y]]

    while stack:
        [x, y] = stack.pop()
        for idx in range(4):
            dx = dxs[idx]
            dy = dys[idx]
            if 0 <= x + dx < N and 0 <= y + dy < N and matrix[y + dy][x + dx] != 1:
                if matrix[y + dy][x + dx] == 3:
                    return 1
                matrix[y + dy][x + dx] = 1
                stack.append([x + dx, y + dy])

    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)

    print('#{} {}'.format(tc, dfs(matrix, *start)))