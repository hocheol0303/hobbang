import time
# 선택정렬 : 처리되지 않은 데이터 중 가장 작은 데이터를 앞으로 가져오기 반복
def selection_sort(lst):
    # 정렬하다보면 마지막 하나는 자기자신과 비교하게 됨 -> 빼
    for i in range(len(lst)-1):
        min_idx=i
        # min_idx를 i로 두고 시작하므로 j는 i+1부터
        for j in range(i+1,len(lst)):
            # index만 담아놨다가 j 반복문 끝나고 스왑
            if lst[j]<lst[min_idx]:
                min_idx=j
        lst[i],lst[min_idx] = lst[min_idx], lst[i]

    print(f'selection sort:{lst}')

# 삽입정렬 : 처리되지 않은 데이터를 처리된 배열의 알맞은 위치에 삽입
# 데이터 하나 가지고 자신보다 작은 데이터가 나올 때까지 앞쪽으로 스왑하면서 내려감 (버블정렬?)
# 배열의 insert : 뒤로 밀면서 앞의 공간 만들어내기
def insertion_sort(lst):
    for i in range(1,len(lst)):
        for j in range(i,0,-1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    print(f'insertion_sort:{lst}')

# 퀵정렬 : pivot 설정 후 pivot보다 큰 데이터와 작은 데이터의 위치 교환
# 병합정렬과 함께 일반적으로 많이 쓰이는 정렬
# 일반적으로 첫 번째 데이터를 기준으로 함. 이 때 최악의 경우 O(N^2). 라이브러리에서 제공하는 퀵정렬은 최악도 O(NlogN) 보장해줌
def quick_sort(lst, start, end):
    # 재귀함수 쓰기 때문에 종료조건 줌
    if start >= end:
        return 
    pivot=start
    left=start+1
    right=end
    # left와 right 엇갈리면 스답
    while left <= right:
        # left: 피벗보다 큰값 찾기 : while문 조건에는 작을 경우 반복
        while left <= end and lst[left] <= lst[pivot]:
            left+=1
        # right: pivot보다 작은값 찾기 : while문 조건에는 클 경우 반복
        while right > start and lst[pivot] <= lst[right]:
            right-=1
        # 엇갈렸으면 right와 pivot 교체
        if left > right:
            lst[pivot], lst[right] = lst[right], lst[pivot]
        # 안엇갈렸으면 left와 right 교체
        else:
            lst[left], lst[right] = lst[right], lst[left]
        # print(lst)
    
    # 매개변수 조건없이 right-1, right+1 >> 언젠가 종료조건 만족
    quick_sort(lst, start, right-1)
    quick_sort(lst, right+1, end)
    print(lst)

# 파이썬 퀵정렬
def quick_sort_py(lst):
    if len(lst) <= 1 :
        return lst
    pivot = lst[0]
    tail = lst[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


# 계수정렬: 특정 조건(양의정수)에 부합하면 빠름
# 최소값부터 최대값 사이의 모든 정수의 개수 크기의 리스트 만들어서 개수 올리는 방식
def count_sort(lst):
    print('count_sort:',end='')
    min_value=min(lst)
    if min_value < 0 :
        return
    for i in lst:
        if type(i) != int:
            return
        
    tmp = [0 for i in range(max(lst)-min_value+1)]
    for i in lst:
        tmp[i-min_value]+=1
    for i in range(len(tmp)):
        print((str(i+min_value)+' ')*tmp[i],end='')
    print()
        

lst=[7,5,9,0,3,1,6,2,4,8,]
print(f'lst:{lst}')
selection_sort(lst[:])
insertion_sort(lst[:])
print('quick_sort:'), quick_sort(lst[:], 0, len(lst)-1)
print('quick_sort_py:',quick_sort_py(lst[:]))
lst2=[ i + 0 for i in [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]]
count_sort(lst2[:])