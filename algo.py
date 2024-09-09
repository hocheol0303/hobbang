'''
n명의 학생의 키 모두 다름

a가 b보다 작으면 a->b로 표시
'''

import sys
from collections import deque

def bfs(start):
    global grp, count
    visited= [False]*(n+1)
    q=deque()
    q.append(start)

    while q:
        n_start = q.popleft()

        for end in grp[n_start]:
            q.append(end)
            if visited[end]:
                continue
            else:
                count[end] += 1
                count[start]+=1
                visited[end]=True

n, m = map(int,sys.stdin.readline().split())

grp={i:[] for i in range(1,n+1)}
count=[0]*(n+1)

for i in range(m):
    start,end = map(int,sys.stdin.readline().split())
    grp[start].append(end)

# 모든 노드를 출발지로써 보고 출발지 - 도착지 관계만 볼거여
# 최종 도착지로 도달할 때의 중간 노드들은 카운트 안들어가
for i in range(1,n+1):
    bfs(i)

print(count.count(n-1))