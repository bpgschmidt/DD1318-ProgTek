import yfinance as yf
import pandas as pd


# Part B:
def fundamental_analysis_yf(ticker):
    stock = yf.Ticker(ticker)

    # Get the p/e-value of the stock
    # Get the financial data for the stock
    # Get the info dictionary

    p_e = stock.info['forwardPE']

    # Get the p/s-value of the stock
    p_s = stock.info["priceToSalesTrailing12Months"]

    # Get the balance sheet data for the stock
    balance_sheet = stock.balance_sheet
    # Calculate the solidity (quick ratio)
    solidity = ((balance_sheet["Total Cash"] + balance_sheet["Total Marketable Securities"] +
                balance_sheet["Total Receivables"]) / balance_sheet["Total Current Liabilities"])

    return print(f'''Fundamental Analysis for {ticker}
—————————————————————————————————
Company solidity is {solidity}
Company p/e-number is {p_e}
Company p/s- number is {p_s}
''')


def technical_analysis_yf(ticker):
    stock = yf.Ticker(ticker)

    # Get the beta-value of the stock
    beta = stock.info["beta"]

    # Get historical prices of the stock
    hist = stock.history(period="90d")

    # Calculate growth
    # pct_change() and mean() are both from the pandas library
    # pct_change() is used to calculate the percentage change in the
    # closing price of the stock for each day over the last 90 days.

    # mean() is then used to calculate the average of this series of percentage changes.
    growth = hist["Close"].pct_change().mean()

    # Find the lowest and highest prices
    low = hist["Close"].min()
    high = hist["Close"].max()

    # Print the values
    return print(f'''
Technical Analysis for {ticker}
—————————————————————————————————
Growth(last 90 days) {growth}
Growth Beta Worth: {beta}
Lowest price (last 90 days): {low}
Highest price (last 90 days): {high}
''')
