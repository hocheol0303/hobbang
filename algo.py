import sys
n=int(sys.stdin.readline())

lst=[]
dp=[[0]*3 for _ in range(n)]
# min_dp=[[0]*3 for _ in range(n)]


for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    lst.append([a, b, c])

for i in range(3):
    dp[0][i] = lst[0][i]
for i in range(1,n):
    dp[i][0] = lst[i][0] + max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = lst[i][1] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][2] = lst[i][2] + max(dp[i-1][1], dp[i-1][2])

print(max(dp[-1]),end=' ')

for i in range(3):
    dp[0][i] = lst[0][i]
for i in range(1,n):
    dp[i][0] = lst[i][0] + min(dp[i-1][0], dp[i-1][1])
    dp[i][1] = lst[i][1] + min(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][2] = lst[i][2] + min(dp[i-1][1], dp[i-1][2])

print(min(dp[-1]))

# print(lst)
# print(min_dp)
# print(max_dp)
