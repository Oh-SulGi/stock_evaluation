import requests
import re
from bs4 import BeautifulSoup as bs
import warnings
warnings.filterwarnings('ignore')
from modules import bbb_

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Whale/3.20.182.14 Safari/537.36'}

stock = f'https://finviz.com/quote.ashx?t=AADI&p=d'
stock2 = f'https://finance.yahoo.com/quote/AADI/balance-sheet?p=AADI'

req_stock = requests.get(stock, headers=headers)
html = req_stock.text
soup = bs(html, 'lxml')

req_stock2 = requests.get(stock2, headers=headers)
html2 = req_stock2.text
soup2 = bs(html2, 'lxml')

a = soup.find(text='ROE')
a1 = soup.find(text='Price')
a2 = soup2.select_one('#Col1-1-Financials-Proxy > section > div.Pos\(r\) > div.W\(100\%\).Whs\(nw\).Ovx\(a\).BdT.Bdtc\(\$seperatorColor\) > div > div.D\(tbrg\) > div:nth-child(14) > div.D\(tbr\).fi-row.Bgc\(\$hoverBgColor\)\:h > div:nth-child(2) > span')
a3 = soup2.select_one('#Col1-1-Financials-Proxy > section > div.Pos\(r\) > div.W\(100\%\).Whs\(nw\).Ovx\(a\).BdT.Bdtc\(\$seperatorColor\) > div > div.D\(tbrg\) > div:nth-child(6) > div.D\(tbr\).fi-row.Bgc\(\$hoverBgColor\)\:h > div:nth-child(2) > span')

bbb = bbb_.today_bbb()
roe = a.find_next(class_='snapshot-td2').text
price = a1.find_next(class_='snapshot-td2').text
shs_outstand = a2.text
equity = a3.text

print(shs_outstand)
print(equity)


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