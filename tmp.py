from collections import deque

l = [0 for x in range(100002)]
s,e = map(int,input().split())

queue = deque()
queue.append(s)

while queue:
    now = queue.popleft()
    if now-1 > 0 and l[now-1] == 0:
        l[now-1] = l[now]+1
        queue.append(now-1)
    if now+1 <= 100001 and l[now+1] == 0:
        l[now+1] = l[now]+1
        queue.append(now+1)
    if now*2 <= 100001 and l[now*2] == 0:
        l[now*2] = l[now]+1
        queue.append(now*2)
    
l[s] = 0
print(l[e])