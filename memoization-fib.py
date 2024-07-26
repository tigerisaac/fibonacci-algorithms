"""

This is the memoization method. By storing previously calculated numbers in a  dictionary, we can speed up the process
tremendously by avoiding needless calculations. 
From here, the only limiting factor is space, as calculation time is near-zero.
Start by creating a dictionary with 0 and 1, then work your way up the sequence.

"""

import time

prev_calc = {0:0, 1:1}

def fib(n):
    if n in prev_calc: # 0 and 1
        return n
    prev_calc[n] = prev_calc[n-1] + prev_calc[n-2] # add the new value to the dictionary
    return prev_calc[n]

for i in range(50):
    start = time.time()
    print(f"{i}, {fib(i)}")
    stop = time.time()
    print(f"{stop-start}s")

# RUNTIME O(N)
# AX. SPACE O(N)