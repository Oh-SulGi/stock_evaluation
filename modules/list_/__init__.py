def stock():
    import pandas as pd

    amex = pd.read_csv('toy/nasdaq/amex.csv')
    nasdaq = pd.read_csv('toy/nasdaq/nasdaq.csv')
    nyse = pd.read_csv('toy/nasdaq/nyse.csv')

    amex_list = amex.loc[:,'Symbol'].to_list()
    nasdaq_list = nasdaq.loc[:,'Symbol'].to_list()
    nyse_list = nyse.loc[:,'Symbol'].to_list()

    return amex_list, nasdaq_list, nyse_list