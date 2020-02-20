#!/usr/bin/python

import sys

# Okay. First thought: this is a lot like eating_cookies.py!
# With some differences. Namely:
#  - The coin denominations aren't evenly spaced.
#  - The order of coins does not matter—i.e. 2 dimes and a nickel = a nickel and 2 dimes.

# Some further (rambly) thoughts:
#  - If one denomination divides into the amount, so do all of the denominations smaller than it.
#  - If one demonination divides into the amount _more than once_, dividingng only once leaves room for smaller denominations.
#  - How much room? Well... say amount = 20. 10 divides into 20 twice, so one way to make 20 up is with 10 + 10. But 10 + 5 + 5
#    would also work. Or, in other words: diviving 10 into 20 leaves 10, which can then itself be broken down. By how much?
#    Depends on the size of smaller denominations. Next smallest is 5, and 10 // 5 = 2, so we have either 5 + 5 = 10, or
#    5 + (1 * 5) = 10, as 1 is the next smallest denomination. And 1 will always divide into the amount, giving (1 * amount) = amount.
#  - So perhaps a first-pass at an alogorithm would look something like this:
#       1) Is amount smaller than any of the denominations? If yes, remove all denominations larger than it.
#       2) For the largest denomination, how many times does it divide into amount?
#       3) If 1, add one to the 'ways' count (or whatever), and ask the same of the next largest denomination.
#       4) Otherwise, how many times does it divide? For each of those times > 1, recurse on the remainder.

# Note: Coin denominations in play are:
#  - Pennies = 0.01$
#  - Nickels = 0.05$
#  - Dimes = 0.10$
#  - Half-dollars = 0.50$

# def making_change(amount, denominations):
#     # order denominations, smallest to largest
#     denominations.sort()

#     # Prune denominations larger than amount
#     prune_x_many = 0
#     for i in reversed(range(len(denominations))):
#         if amount / denominations[i] < 1:
#             prune_x_many += 1
#         else:
#             break
    
#     pruned_denominations = denominations[:-prune_x_many] if prune_x_many > 0 else denominations
#     print(pruned_denominations)

#     ways = 1
#     for i in range(1, len(pruned_denominations)):
#         divides = amount // pruned_denominations[i]
#         ways += pow(divides, i)

#         remainder = amount % pruned_denominations[i]
#         if remainder > 0:
#             x = pow((making_change(remainder, pruned_denominations) - 1), i)
#             print("yo", x)
#             ways += x

#     return ways

### Oh. I'm wayyyyyy ovethinking this! (Should have read the hints, dammit... :D )
def making_change(amount, denominations):
    # initialise a cache as a list of 0s with length = amount + 1 (to include 0)
    # each value at index i will represent the ways of making i cents
    # initialise cache[0] = 1
    cache = [1] + [0]*amount
    
    # for each coin in denominations
    for coin in denominations:
        # loop through higher_amount in range(coin, amount + 1)
        for higher_amount in range(coin, amount + 1):
            # find the difference b/w higher_amount and coin
            difference = higher_amount - coin
            # add cached result for difference to cached result for higher amount
            cache[higher_amount] += cache[difference]
    
    return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")