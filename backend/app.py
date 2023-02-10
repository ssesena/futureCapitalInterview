import json
import sys


INPUT_ARG_LENGTH = 3

def calculateStockPortfolioValue(stock_portfolio_input):
    """
    Calculates and returns the total value of a given stock portfolio

    :param stock_portfolio_input: str, stock portfolio input as a string
    :return: int, total portfolio value
    """
    portfolio = parseStockPortfolioQuantitiesIntoDictionary(stock_portfolio_input)

    # Opening JSON file
    json_file = open('stocks.json')

    # returns JSON object as a dictionary
    stocks_info = json.load(json_file)

    total_portfolio_value = 0

    # Bool to check if inputted ticker exists
    ticker_found = False
    for stock in portfolio:
        for entry in stocks_info:
            if entry["ticker"] == stock:
                ticker_found = True
                total_portfolio_value += entry["close"]*portfolio[stock]
                break

        # Raise error is ticker does not exist
        if not ticker_found:
            raise KeyError("Stock " + stock + " was not found. Please input an existing stock ticker")
        ticker_found = False

    # Closing file
    json_file.close()

    return total_portfolio_value

def parseStockPortfolioQuantitiesIntoDictionary(stock_portfolio_input):
    """
    Converts stock portfolio input into dictionary mapping tickers to their quantities

    :param stock_portfolio_input: str, stock portfolio input as a string (e.g "FB:12,PLTR:5000")
    :return: dict of {str : int}
    """
    try:
        stocks_as_strings = stock_portfolio_input.split(",")
        portfolio = {}
        for stock in stocks_as_strings:
            ticker_to_quant = stock.split(":")
            if len(ticker_to_quant) > 2 or len(ticker_to_quant) < 2:
                raise SyntaxError("Portfolio input was not formatted correctly")
            if float(ticker_to_quant[1]) < 0:
                raise ValueError("Portfolio cannot have negative quantities")
            portfolio[ticker_to_quant[0]] = float(ticker_to_quant[1])
        return portfolio
    except:
        print("--------------------------INPUT WAS NOT IN CORRECT FORMAT--------------------------")
        raise

def findMaximumProfits(projected_stock_prices_input):
    """
    Finds the max possible profit given an array of projected stock prices

    :param projected_stock_prices_input: str, stock price array as a string input
    :return: float, max profit possible given projected stock prices
    """

    projected_stock_prices = parseProjectedStockPricesIntoArray(projected_stock_prices_input)

    # Keep track of two different days (indices) of stock prices using left and right pointer
    left_pointer = 0
    right_pointer = 1
    max_profit = 0
    while right_pointer < len(projected_stock_prices):
        left_num = projected_stock_prices[left_pointer]
        right_num = projected_stock_prices[right_pointer]
        if left_num > right_num:
            # There cannot be a better profit between those two days so both pointers move onto
            # next section of array
            left_pointer = right_pointer
        else:
            # Keep track of max profit as pointers move
            if right_num - left_num > max_profit:
                max_profit = right_num - left_num
        right_pointer += 1
    return max_profit


def parseProjectedStockPricesIntoArray(projected_stock_prices_input):
    """
    Converts stock prices input string into an array of integers

    :param projected_stock_prices_input: str, stock price array as a string (e.g. "7,1,5,3,6,4")
    :return: List[int], stock prices as an array
    """
    try:
        values_as_strings = projected_stock_prices_input.split(",")
        values_as_float = []
        for value in values_as_strings:
            if float(value) < 0:
                raise ValueError("Stock price cannot be negative")
            values_as_float.append(float(value))
        return values_as_float
    except:
        print("--------------------------INPUT WAS NOT IN CORRECT FORMAT--------------------------")
        raise


def main():
    """
    Interprets arguments from command line.
    Calls functions if command is valid and prints result.

    :return: None
    """

    # sys.argv is the command line input as an array of strings
    # sys.argv[num] indexes the array (0 - filename, 1 - command, 2 - input)
    if len(sys.argv) < INPUT_ARG_LENGTH:
        print("Not enough arguments given")
        print("Need " + INPUT_ARG_LENGTH + " arguments")
    elif len(sys.argv) > INPUT_ARG_LENGTH:
        print("Too many arguments given")
        print("Need " + INPUT_ARG_LENGTH + " arguments")
    else:
        if sys.argv[1] == "-part1":
            print(calculateStockPortfolioValue(sys.argv[2]))
        elif sys.argv[1] == "-part2":
            print(findMaximumProfits(sys.argv[2]))
        else:
            print(sys.argv[1] + " is not a valid command")

if __name__ == "__main__":
    main()