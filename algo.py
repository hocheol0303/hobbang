import sys
n=int(sys.stdin.readline())

lst=[]
max_dp=[[0]*3 for _ in range(n)]
min_dp=[[0]*3 for _ in range(n)]

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    lst.append([a, b, c])

for i in range(3):
    max_dp[0][i] = min_dp[0][i] = lst[0][i]

for i in range(1,n):
    max_dp[i][0] = lst[i][0] + max(max_dp[i-1][0], max_dp[i-1][1])
    max_dp[i][1] = lst[i][1] + max(max_dp[i-1][0], max_dp[i-1][1], max_dp[i-1][2])
    max_dp[i][2] = lst[i][2] + max(max_dp[i-1][1], max_dp[i-1][2])

    min_dp[i][0] = lst[i][0] + min(min_dp[i-1][0], min_dp[i-1][1])
    min_dp[i][1] = lst[i][1] + min(min_dp[i-1][0], min_dp[i-1][1], min_dp[i-1][2])
    min_dp[i][2] = lst[i][2] + min(min_dp[i-1][1], min_dp[i-1][2])

# print(lst)
# print(min_dp)
# print(max_dp)

print(max(max_dp[-1]), min(min_dp[-1]))