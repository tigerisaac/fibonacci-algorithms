"""

This one's going to be much more advanced.
To make the leap from O(N) to O(log(N)), we're going to need to do some complex math stuff.
Here's some background on matrix multiplication:
If we think about a function like the Fibonacci sequence, we can envision it as 
F(n) = F(n-1) + F(n-2)
this could be represented as a matrix, like so
[F(n)  ] = MATRIX * [F(n-1)]
[F(n-1)]            [f(n-2)]
It's a bit hard to show it, but that should do for now.
Following the rules of matrix multiplication:
[F(n)  ] = [1 1] * [F(n-1)]
[F(n-1)]   [1 0]   [f(n-2)]
Now, to get the next Fibonacci number (namely, F(n+1)) we can just multiply it by the matrix again.
So, the formula for the nth Fibonacci becomes:
[F(n)  ] = [1 1]^(n-2) * [1]
[F(n-1)]   [1 0]         [0]

"""

def multiply(m1, m2):
    r = [[0, 0], [0, 0]] # Store the result
    mod = 10**9 + 7

    r[0][0] = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % mod # does matrix multiplication for the first row and column of m1 and m2, respectively
    r[0][1] = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % mod # does matrix multiplication for the first row and second column of m1 and m2, respectively
    r[1][0] = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % mod # does matrix multiplication for the second row and first column of m1 and m2, respectively
    r[1][1] = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % mod # does matrix multiplication for the second row and column of m1 and m2, respectively

    # now we copy the results
    m1[0][0] = r[0][0]
    m1[0][1] = r[0][1]
    m1[1][0] = r[1][0]
    m1[1][1] = r[1][1]


def power(M, ex):
    # to raise matrix M to exponent ex
    ans = [[1, 0], [0, 1]] # identity matrix

    while ex:
        if ex & 1: # fancy way of saying if it's divisible by 2
            multiply(ans, M)
        multiply(M, M)
        ex >>= 1

    return ans

def f(n):
    if n == 0 or n == 1:
        return n

    M = [[1, 1], [1, 0]]
    F = [[1, 0], [0, 0]]

    res = power(M, n - 2)

    multiply(res, F)
    return (res[0][0] + res[1][0])

for i in range(50):
    print(f(i), i)