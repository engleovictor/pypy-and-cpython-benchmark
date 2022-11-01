import sys
import time

def iterative_fibonacci(n):
    if n < 2:
        return n
    else:
        _1,_2= 0,1
        for i in range(n):
            _1,_2=_2,_1+_2
        return _2

def recursive_fibonacci(n):
    if n < 2:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

def main():
    n = int(sys.argv[1])
    t0 = time.perf_counter()
    iterative_fibonacci(n)
    print(time.perf_counter()-t0)
    t0 = time.perf_counter()
    recursive_fibonacci(n)
    print(time.perf_counter()-t0)

if __name__ == '__main__':
    main()