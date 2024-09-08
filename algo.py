'''
가중치 그래프
'''

import sys

t = int(sys.stdin.readline())

n, m = map(int, sys.stdin.readline().split())

# 1부터 n까지의 정점 저장
dct={i:{} for i in range(1,n+1)}

for i in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())

    # 경로 이미 존재하면 비교
    if end in dct[start].keys():
        if dct[start][end] > weight:
            dct[start][end] = weight
            dct[end][start] = weight
    else: 
        dct[start][end]=weight
        dct[end][start]=weight

print(dct)


# 모르겠쪄