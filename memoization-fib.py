"""

This is the memoization method. By storing previously calculated numbers in an array, we can speed up the process
tremendously by avoiding needless calculations. 
From here, the only limiting factor is space, as calculation time is near-zero.
Start by creating an array with 0 and 1, then work your way up the sequence.

"""

import time

prev_calc = [0, 1] 

def fib(n):
    if n == 0 or n == 1:
        return n
    prev_calc.append(prev_calc[n-1] + prev_calc[n-2]) # append the new value to the array
    return prev_calc[n-1] # zero-based indexing

for i in range(50):
    start = time.time()
    print(fib(i), i)
    stop = time.time()
    print(f"{stop-start}s")

    

