'''
들고 있다가 3번째 나오면 정답후보 업데이트
'''
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

front = 0
other=0
rear = 1
species=[]
cnt=0

while rear < n:
    if lst[rear-1] != lst[rear]:
        if lst[rear] not in species:
            if len(species) < 2:
                species.append(lst[rear])