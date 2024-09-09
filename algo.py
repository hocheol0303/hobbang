'''
(N,K)-요세푸스 순열
N명이 원형으로 앉아있음
K번 사람 지우기 시작해서 그 사람의 오른쪽 K번째 사람 지움
모든 사람 제거되었을 때 제거된 사람의 순서

반전 요세푸스: M번 지울 때마다 반대 방향으로 돌림

(7,3): [1,2,3,4,5,6,7]: 3,6,2,7,5,1,4
'''

import sys

n,k,m = map(int,sys.stdin.readline().split())

lst = [0 for i in range(n+1)]
result=[]
# True == 우, False == 좌
direction=True
loc=0
cnt=0

# # 1씩 올리는거 너무 느릴 것 같음
# while True:
#     # k칸 옮김
#     for i in range(k):
#         # 한 칸씩 옮겨감 index 넘어갔을 때 처리
#         while True:
#             if direction:
#                 loc += 1
#                 if loc > n:
#                     loc = 1
#             else:
#                 loc -= 1
#                 if loc < 1:
#                     loc = n
#             if lst[loc] == 0:
#                 break
#     lst[loc] = 1
#     result.append(loc)
#     cnt+=1
#     if cnt == m:
#         direction = False
#         cnt=0
#     if len(result) == n : break

