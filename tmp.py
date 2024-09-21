lst = [(2,1), (0,5), (4,4), (5,3), (0,3), (2,5)]
lst.sort(key=lambda x:(x[0], -x[1]))
print(lst)