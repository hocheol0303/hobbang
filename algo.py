'''
n: IOI의 'O' 개수
m: s의 길이
s: 문자열
'''

import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
s=sys.stdin.readline().rstrip()

p=list('IO'*n)
p.append('I')
p=''.join(p)

index=0
result=0
while index < m-1:
    if s[index:index+n*2+1]==p:
        index+=2
        result+=1
    else:
        index+=1
print(result)