"""
https://school.programmers.co.kr/learn/courses/30/lessons/1829
파이썬 없저..

[
    [1,1,1,0],
    [1,2,2,0],
    [1,0,0,1],
    [0,0,0,1],
    [0,0,0,3],
    [0,0,0,3]
]

ans=[4,5]
"""

'''
0은 빈공간으로 취급(영역 셀 때 포함 안됨)
같은 색에 한해서 이어진 길로 취급 (색 다를 경우 빈공간)
최대 길이, 총 경로의 수 필요
'''

import sys
from collections import deque

def bfs(i, j):
    # 지도, 최대길이, 총 개수를 전역변수로 받는다.
    global lst, mx, cnt

    # 입력받은 지점이 0이 아닐 때 길 시작
    if lst[i][j] == 0:
        return
    else:
        cnt+=1
    
    q = deque()
    
    # 상,하,좌,우 순서대로 탐색
    drow=[-1, 1, 0, 0]
    dcol=[0, 0, -1, 1]

    q.append([i,j])

    # 최대 길이, 같은색 판별을 위한 변수 선언
    count = 0
    color = lst[i][j]
    

    while len(q):
        row, col = q.popleft()
        # print(row,col)
        
        # 꺼내고 보니 0인 경우, 다른색인 경우 막혔다고 판단
        if lst[row][col] == 0 or lst[row][col] != color:
            continue
        else:
        # 같은 색의 길인 경우 이어진 길의 길이와 색깔(지나감 표시) 업데이트
            count+=1
            lst[row][col] = 0

        # 상하좌우 탐색하면서 맵을 벗어난 경우는 건너뜀
        for k in range(4):
            if row+drow[k] < 0 or row+drow[k] >= m or col+dcol[k] < 0 or col+dcol[k] >= n:
                continue
            else:
                # 길이 있는 경우만 push
                if lst[row+drow[k]][col+dcol[k]] != 0 and lst[row+drow[k]][col+dcol[k]] == color:
                    q.append([row+drow[k], col+dcol[k]])
    
    # print()
    if count > mx:
        mx=count

mx=0
cnt=0

m,n = map(int, sys.stdin.readline().split())

lst=[list(map(int, sys.stdin.readline().split())) for _ in range(m)]

for i in range(m):
    for j in range(n):
        bfs(i,j)

print(cnt, mx)