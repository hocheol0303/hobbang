import sys
n=int(sys.stdin.readline())

# 이전 단계의 값들 저장하는거
dp_max=[0,0,0]
dp_min=[0,0,0]
min_ = max_ = None

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if i == 0:
        dp_max=[a,b,c]
        dp_min=[a,b,c]
    else:
        new_max_a = a + max(dp_max[0], dp_max[1])
        new_max_b = b + max(dp_max[0], dp_max[1], dp_max[2])
        new_max_c = c + max(dp_max[1], dp_max[2])
        dp_max = [new_max_a, new_max_b, new_max_c]

        new_min_a = a + min(dp_min[0], dp_min[1])
        new_min_b = b + min(dp_min[0], dp_min[1], dp_min[2])
        new_min_c = c + min(dp_min[1], dp_min[2])
        dp_min = [new_min_a, new_min_b, new_min_c]

print(max(dp_max), min(dp_min))

########################################################################
# for _ in range(n):
#     a, b, c = map(int, sys.stdin.readline().split())
#     lst.append([a, b, c])

# for i in range(3):
#     dp[0][i] = lst[0][i]
# for i in range(1,n):
#     dp[i][0] = lst[i][0] + max(dp[i-1][0], dp[i-1][1])
#     dp[i][1] = lst[i][1] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
#     dp[i][2] = lst[i][2] + max(dp[i-1][1], dp[i-1][2])

# print(max(dp[-1]),end=' ')

# for i in range(3):
#     dp[0][i] = lst[0][i]
# for i in range(1,n):
#     dp[i][0] = lst[i][0] + min(dp[i-1][0], dp[i-1][1])
#     dp[i][1] = lst[i][1] + min(dp[i-1][0], dp[i-1][1], dp[i-1][2])
#     dp[i][2] = lst[i][2] + min(dp[i-1][1], dp[i-1][2])

# print(min(dp[-1]))

# print(lst)
# print(min_dp)
# print(max_dp)
