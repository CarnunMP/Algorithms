#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # loop over prices, starting from the second price
    # for each price, find min before
    # keep track of current_min_price_so_far (min before) and max_profit_so_far

    max_profit_so_far = None

    for i in range(1, len(prices)):
        current_min_price_so_far = None

        for j in range(0, i):
            if current_min_price_so_far == None or prices[j] < current_min_price_so_far:
                current_min_price_so_far = prices[j]

        if max_profit_so_far == None or prices[i] - current_min_price_so_far > max_profit_so_far:
            max_profit_so_far = prices[i] - current_min_price_so_far

    return max_profit_so_far
            

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))