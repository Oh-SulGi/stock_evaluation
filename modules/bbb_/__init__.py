def today_bbb():
    import requests
    from bs4 import BeautifulSoup as bs
    
    ice = 'https://fred.stlouisfed.org/series/BAMLC0A4CBBBEY#0'

    req_ice = requests.get(ice)
    html = req_ice.text
    soup = bs(html, 'lxml')
    BBB = soup.select_one('#meta-left-col > div.float-start.meta-col.col-sm-5.col-5 > span.series-meta-observation-value')
    
    return BBB.text