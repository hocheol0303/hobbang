import sys

def dfs(start):
    global n, m, lst
    if len(result) == m:
        print(*result)
        result.pop()
    else:
        for i in range(start, n):
            result.append(lst[i])
            dfs(i)


n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
result=[]

dfs(0)