"""

The memoization method was an easy way to do it. But is it really necessary to hold 
EVERY single variable? Really, all we needed to access was the last two computed Fibonacci numbers!
Therefore, it should be possible (and much more efficient) to compute the numbers with only two variables.
With that, the best conditions of this method would force the output to occur inside the function, as it is a linear process.
Additionally, we'd have to calculate the total runtime of the calculation, the calculations themselves are almost instant.

"""

import time

def fib(n):
    f1 = 0
    f2 = 1 # initialize 0 and 1
    start = time.time()
    for i in range(n):
        print(f"{i}, {f1}")
        f1, f2 = f2, f1 + f2 # python allows for multiple 
    stop = time.time()
    print(f"{stop-start}s") 
fib(50)

# RUNTIME O(N)
# AX. SPACE O(1)