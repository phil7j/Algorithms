#!/usr/bin/python

import argparse


def find_max_profit(prices):
  # Find biggest difference of prices Buy comes before Sell
  # Idea 1:
  # Iterate with 2 points over prices array:
  # First pointer selects the first number
  # Second pointer iterates over the rest of the prices and pushes the differences to a new array
  # After going through, and recording the data, First pointer goes to the next value and process starts all over
  # All differences in the array get checked to see which one is largest
  # Return number


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
