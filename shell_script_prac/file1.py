import time

start = time.time()
print('hi')
time.sleep(5)
print('bye')
end = time.time()
print(f'{end-start:.2f} second passed')