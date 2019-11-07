#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Find biggest difference of prices Buy comes before Sell
    # Idea 1:
    # Iterate with 2 points over prices array:
    # First pointer selects the first number and moves right after every completed for loop
    # Second pointer iterates over the prices that are to the right of it in the array and puts the highest difference in a variable
    # After going through, and recording the data, First pointer goes to the next value and process starts all over
    # All differences in the array get checked to see which one is largest
    # Return number
    profit = -99999

    for i in range(0, len(prices) - 2):
        for j in range(i+1, len(prices)-1):
            diff = prices[j] - prices[i]
            if diff > profit:
                profit = diff
    return profit


print(find_max_profit([100, 55, 4, 98, 10, 18,
                       90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
