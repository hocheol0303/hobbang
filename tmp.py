import time

# recursion
def fib_re(n):
	if n <= 2:
		return 1
	else:
		return fib_re(n-1) + fib_re(n-2)

# memoization
d = [0] * 100
def fib_me(n):
	if n <= 2:
		return 1
	if d[n] != 0:
		return d[n]
	else:
		d[n] = fib_me(n-1) + fib_me(n-2)
		return d[n]
	
n=int(input())
# start=time.time()
# print(fib_re(n))
# end=time.time()
# print((end-start))


start=time.time()
print(fib_me(n))
end=time.time()
print((end-start))
