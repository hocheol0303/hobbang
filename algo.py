import sys
n = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n):
    for j in range(i+lst[i][0], n+1):
        dp[j] = max(dp[j], dp[i]+lst[i][1])

# print(lst)
print(dp[-1])