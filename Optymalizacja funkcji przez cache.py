import functools as ft
import time

@ft.lru_cache(100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()

for n in range (1, 39):
    print('{}\t'.format(n),fib(n)) 

stop = time.time()

print("Time:\t", stop - start)
print(fib.cache_info())