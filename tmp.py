import sys
import heapq

lst=[]
for i in [2,7,0,5,8]:
    heapq.heappush(lst, -i)
print(lst)

