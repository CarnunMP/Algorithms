#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
    # base cases
    if n < 1:
        return 1
    if n <= 2 :
        return n
    if n == 3:
        return 4

    if cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i:0 for i in range(n + 1)}
        
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

        return cache[n]

### First attempt:
# def eating_cookies(n, cache=None):
#     if n == 0:
#         return 1
#     if n <= 2:
#         return n
#     if n == 3:
#         return 4
#     if n == 4:
#         return 6
    
#     sequence = fibonacci(n - 2, 2, 2)
#     print(sequence)
#     print(sequence[len(sequence) - 3] + sequence[len(sequence) - 2] + sequence[len(sequence) - 1])

#     return sequence[len(sequence) - 3] + sequence[len(sequence) - 2] + sequence[len(sequence) - 1]

# def fibonacci(n, n0 = 1, n1 = 1):
#     if n == 0:
#         return n0
#     if n == 1:
#         return n1

#     sequence = [n0, n1]

#     for i in range(2, n + 1):
#         sequence.append(sequence[i - 2] + sequence[i - 1])

#     return sequence

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')