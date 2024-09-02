'''
첫 줄: TC
시작마다: 입력 개수
I n: n을 q에 삽입하는 연산
D 1: Q에서 최댓값을 삭제하는 연산
D -1: Q에서 최솟값을 삭제하는 연산
'''
import sys
import heapq

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())
    min_heap=[]
    max_heap=[]
    cnt=0
    for __ in range(n):
        op, num = sys.stdin.readline().rstrip().split()
        num=int(num)

        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            cnt+=1
        else:
            if cnt==0:
                min_heap=[]
                max_heap=[]
                continue
            cnt-=1
            if num == 1:
                heapq.heappop(max_heap)
            else:
                heapq.heappop(min_heap)
    if cnt==0:
        print('EMPTY')
    else:
        for i in max_heap:
            max_=-heapq.heappop(max_heap)
            if max_ in min_heap:
                break
        for i in min_heap:
            min_=-heapq.heappop(min_heap)
            if min_ in max_heap:
                min_=-min_
                break
        print(max_, min_)