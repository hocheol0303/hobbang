tmp='''0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0'''.split('\n')
lst=[i.split() for i in tmp]
lst=[[int(i) for i in j] for j in lst]

tmp=[[0]*7 for i in range(7)]
tmp[0][3]=1
for i in tmp:
    print(i)