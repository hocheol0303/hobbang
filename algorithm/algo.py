import sys

# dfs 문제로 들어왔지만 bfs로 풀어보려했는데 리스트 관리를 못하겠음 백트래킹으로 전환

def dfs(row, col):
    global r, c, lst, record, max_, q, d_row, d_col

    for i in range(4):
        n_row, n_col = row+d_row[i], col+d_col[i]
        if 0 <= n_row < r and 0 <= n_col < c:
            if lst[n_row][n_col] in record:
                max_ = max(max_, len(record))
                continue
            else:
                record.append(lst[n_row][n_col])
                dfs(n_row, n_col)
                record.pop()


r, c = map(int, sys.stdin.readline().split())
lst = []
record = []
max_ = 0
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


for _ in range(r):
    lst.append(list(map(str, sys.stdin.readline().rstrip())))

record.append(lst[0][0])
max_ = max(max_, len(record))
dfs(0, 0)
record.pop()

print(max_)