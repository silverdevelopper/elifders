calculated = {0:1,1:1}
import time

def fib(n:int):
    # base condition
    if n in calculated:
        return calculated[n]
    
    #print("fib({}) = fib({})+fib({})".format(n,n-1,n-2))
    fibn= fib(n-1) + fib(n-2)
    calculated[n] = fibn
    return fibn

def fib2(n:int):
    if n == 0 or n==1:
        return 1
    #print("fib({}) = fib({})+fib({})".format(n,n-1,n-2))
    fibn= fib2(n-1) + fib2(n-2)
    return fibn

# 1 1 2 3 5 8 13 ..... (10.)
# fib(10) = fib(9) + fib(8)
# fib(n) = fib(n-2) + fib(n-1)

'''
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(2) = fib(1) + fib(0)
fib(1) = 1
fib(0) = 1
'''
start_time = time.time()
print(fib(100))
t1 = time.time() - start_time
print("Fib1 ",t1)

start_time2 = time.time()
#print(fib2(20))
t2 = time.time() - start_time2
print("Fib2",t2)

print("t2 - t1 = ",t2-t1)
