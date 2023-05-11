import requests
import re
from bs4 import BeautifulSoup as bs
import warnings
warnings.filterwarnings('ignore')
from modules import bbb_, list_

amex_list, nasdaq_list, nyse_list = list_.stock()

# def extract(list):
dict1 = {}
for ticker in nasdaq_list:
    print(ticker)
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Whale/3.20.182.14 Safari/537.36'}

    summary = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'
    balance_sheet = f'https://finance.yahoo.com/quote/{ticker}/balance-sheet?p={ticker}'
    statistics = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'

    req_summary = requests.get(summary, headers=headers)
    req_balance_sheet = requests.get(balance_sheet, headers=headers)
    req_statistics = requests.get(statistics, headers=headers)

    html_summary = req_summary.text
    html_balance_sheet = req_balance_sheet.text
    html_statistics = req_statistics.text

    soup_summary = bs(html_summary, 'lxml')
    soup_balance_sheet = bs(html_balance_sheet, 'lxml')
    soup_statistics = bs(html_statistics, 'lxml')

    price_ = soup_summary.find(text='Previous Close')
    roe_ = soup_statistics.find(text='Return on Equity')
    issued_shares_ = soup_balance_sheet.find(text='Share Issued')
    equity_ = soup_balance_sheet.find(text='Common Stock Equity')

    bbb = bbb_.today_bbb()
    #     price = price_.find_next(class_='Ta(end) Fw(600) Lh(14px)').text
    #     roe = roe_.find_next(class_='Fw(500) Ta(end) Pstart(10px) Miw(60px)').text
    #     issued_shares = issued_shares_.find_next(class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)').text
    #     equity = equity_.find_next(class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)').text

    dict1[f'{ticker}'] = {
        'equity' : equity_,
        'roe' : roe_,
        'bbb' : bbb,
        'issued_shares' : issued_shares_,
        'price' : price_
    }

    # return dict1


# equity = int(re.sub('[^0-9]','',equity))*1000/100000000
# roe = float(roe[:-2])
# bbb = float(bbb)
# price = float(price)
# excess_profit = round((equity * ((roe - bbb) / 100)), 2)
# corporate_value = round((equity + (equity * ((roe - bbb) / bbb))), 2)
# shs_outstand = int(re.sub('[^0-9]','',shs_outstand))*1000
# target_price = round((((equity + (excess_profit * (1 / (1 + (bbb / 100) - 1)))) * 100000000) / shs_outstand), 2)
# price_per_target = round((target_price / price), 2)

# dict1 = {}
# dict1['AADI'] = {
#     'equity' : equity,
#     'roe' : roe,
#     'bbb' : bbb,
#     'excess_profit' : excess_profit,
#     'corporate_value' : corporate_value,
#     'shs_outstand' : shs_outstand,
#     'target_price' : target_price,
#     'price_per_target' : price_per_target,
#     'price' : price
# }

# print(dict1)