"""

The recursive approach is the most popular and is known to be the standard approach.
It works very well to teach people about recursive functions, but it fails to completely solve the problem.
It gets painfully slow at around the 40th Fibonacci number, and breaks soon after.

"""

import time

def fib(n):
    if n == 0 or n == 1:
        return n # Base case of recursions
    else:
        return (fib(n-1) + fib(n-2))

for i in range(50):
    start = time.time()
    print(fib(i), i)
    stop = time.time()
    print(f"{stop-start}s")