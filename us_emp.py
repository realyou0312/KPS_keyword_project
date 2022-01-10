from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm


df = pd.read_excel('C:/Users/kakaopaysec/Desktop/us_emp_220110.xlsx')
code_df = df[df['CEO'].isnull()]
code_list = code_df['code'].to_list()

print(code_list)

for i in tqdm(code_list[:500]):
    temp = 0
    if i == 'TRUE':
        pass
    if i.endswith('.B'):
        temp = i.replace('.B', '-B')

    if i.endswith('.C'):
        temp = i.replace('.C', '-C')

    if i.endswith('.V'):
        temp = i.replace('.V', '-V')


    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    url = f"https://finance.yahoo.com/quote/{i}/profile?p={i}"
    res = requests.get(url, headers=header)

    # html = urlopen("https://finance.yahoo.com/quote/i}/profile?p={i}")

    bsObject = BeautifulSoup(res.text, "html.parser")

    names = bsObject.select('#Col1-0-Profile-Proxy > section > section.Bxz\(bb\).quote-subsection.undefined > table > tbody > tr > td:nth-child(1) > span')
    positions = bsObject.select('#Col1-0-Profile-Proxy > section > section.Bxz\(bb\).quote-subsection.undefined > table > tbody > tr > td.Ta\(start\).W\(45\%\) > span')

    try:
        name = names[0].text
        position = positions[0].text

        df.loc[df['code']==i, 'CEO'] = name
        df.loc[df['code'] == i, 'position'] = position

        print(name)
    except:
        print(i)

df.to_csv('C:/Users/kakaopaysec/Desktop/us_emp.csv', encoding='utf-8-sig', index=False)