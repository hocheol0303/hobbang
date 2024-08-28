'''
다이나믹 프로그래밍 문제
퍼져나가면서 그자리에 적는거여



"넷, 혹은 그 이하"
최대로 놓고 min()으로 쭉쭉쭉
'''
import sys

lst= [4] * 50001
i=1
n=int(sys.stdin.readline())

lst[1]=1
lst[2]=2
lst[3]=3

# 26 : [5, 1]={25,1} / [4, 3, 1]={4^2,10}

while i < n:
    for j in range(1, i):
        # if (i==25 and j==1) or (i==5 and j==1) :
        #     print()

        if i**2+j**2 <= n:
            lst[i**2+j**2]=2
        if i**2 <= n:
            lst[i**2]=1
        if j**2 <= n:
            lst[j**2]=1
            
        # lst[j**2 + i] += 1
        # lst[i], j**2
        # lst[i+j**2]을 lst[i]+1
        if i+j**2 <= n:
            lst[i+j**2] = min(lst[i+j**2], lst[i]+1)
    i+=1

print(lst[n])