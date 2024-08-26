'''
이분탐색 구현하기
'''
import random
lst=sorted([random.randint(0,100) for i in range(20)])
# print(lst)

left_idx=0
right_idx=9

target = random.randint(0,100)

while left_idx<=right_idx:
    cur=(left_idx+right_idx) //2

    if lst[cur] == target:
        print(cur, lst[cur])
        break
    elif lst[cur] > target:
        right_idx = cur-1
    elif lst[cur] < target:
        left_idx = cur+1

if left_idx > right_idx:
    print('no', target, 'in', lst)
else:
    print(target, 'in', lst)