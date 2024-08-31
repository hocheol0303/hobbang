'''
가장 빠른 시간
선택지: +1 / -1 / *2
0 <= n,k <= 100,000
'''
import sys
from collections import deque

def bfs(x, y):
    global lst, cnt
    # dx = +1, -1, *2
    q = deque()
    q.append(x)

    while q:
        x=q.popleft()
        if x >= 100000 or x < 0:
            continue
            
        if cnt[x+1]<3:
            cnt[x+1]+=1
            q.append(x+1)
            lst[x+1]=min(lst[x+1], lst[x]+1)

        if cnt[x-1]<3:
            cnt[x-1]+=1
            q.append(x-1)
            lst[x-1]=min(lst[x-1], lst[x]+1)

        if x*2 < 100000 and cnt[x*2]<3:
            cnt[x*2]+=1
            q.append(x*2)
            lst[x*2]=min(lst[x*2],lst[x]+1)

        # 목적지 3번 정도 봤으면 최솟값 나왔을거라 믿어
        if cnt[y]>=3:
            return

n,k=map(int,sys.stdin.readline().split())
lst=[100000]*100001

# 한 2~3번 봤으면 제꺼야하나?
cnt=[0]*100001

lst[k]=abs(k-n)
lst[n]=0

bfs(n,k)
print(lst[k])