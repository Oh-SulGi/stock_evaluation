from modules import list_

amex_list, nasdaq_list, nyse_list = list_.stock()

def extract(list):
    '''
    equity : 자기자본
    roe : 자본이익률
    excess_profit : 초과이익
    corporate_value : 기업가치
    shs_outstand : 발행주식수
    price : 전일종가
    '''
    import requests
    import re
    from bs4 import BeautifulSoup as bs
    import warnings
    warnings.filterwarnings('ignore')
    from modules import bbb_

    dict1 = {}
    for ticker in list:
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Whale/3.20.182.14 Safari/537.36'}

        stock = f'https://finviz.com/quote.ashx?t={ticker}&p=d'
        stock2 = f'https://finance.yahoo.com/quote/{ticker}/balance-sheet?p={ticker}'

        req_stock = requests.get(stock, headers=headers)
        html = req_stock.text
        soup = bs(html, 'lxml')

        req_stock2 = requests.get(stock2, headers=headers)
        html2 = req_stock2.text
        soup2 = bs(html2, 'lxml')

        a = soup.find(text='ROE')
        a1 = soup.find(text='Price')
        a2 = soup2.select_one('#Col1-1-Financials-Proxy > section > div.Pos\(r\) > div.W\(100\%\).Whs\(nw\).Ovx\(a\).BdT.Bdtc\(\$seperatorColor\) > div > div.D\(tbrg\) > div:nth-child(13) > div.D\(tbr\).fi-row.Bgc\(\$hoverBgColor\)\:h > div:nth-child(2) > span')
        a3 = soup2.select_one('#Col1-1-Financials-Proxy > section > div.Pos\(r\) > div.W\(100\%\).Whs\(nw\).Ovx\(a\).BdT.Bdtc\(\$seperatorColor\) > div > div.D\(tbrg\) > div:nth-child(5) > div.D\(tbr\).fi-row.Bgc\(\$hoverBgColor\)\:h > div:nth-child(2) > span')

        bbb = bbb_.today_bbb()
        roe = a.find_next(class_='snapshot-td2').text
        price = a1.find_next(class_='snapshot-td2').text
        shs_outstand = a2.text
        equity = a3.text

        if roe != '-':
            roe = float(roe[:-2])
            equity = int(re.sub('[^0-9]','',equity))*1000/100000000
            bbb = float(bbb)
            price = float(price)
            excess_profit = round((equity * ((roe - bbb) / 100)), 2)
            corporate_value = round((equity + (equity * ((roe - bbb) / bbb))), 2)
            shs_outstand = int(re.sub('[^0-9]','',shs_outstand))*1000
            target_price = round((((equity + (excess_profit * (1 / (1 + (bbb / 100) - 1)))) * 100000000) / shs_outstand), 2)
            price_per_target = round((target_price / price), 2)

            dict1[f'{ticker}'] = {
                'equity' : equity,
                'roe' : roe,
                'bbb' : bbb,
                'excess_profit' : excess_profit,
                'corporate_value' : corporate_value,
                'shs_outstand' : shs_outstand,
                'target_price' : target_price,
                'price_per_target' : price_per_target,
                'price' : price
            }
        else:
            pass
    return dict1

print(extract(nasdaq_list))