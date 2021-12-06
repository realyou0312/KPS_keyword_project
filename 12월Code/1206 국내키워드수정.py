import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/kakaopaysec/Desktop/1206 국내 키워드추가.csv')

for i in range(df.shape[0]):
    df.loc[i, '종목코드'] = 'A' + df['종목코드'][i].zfill(6)

print(df)

df.to_csv('C:/Users/kakaopaysec/Desktop/1206 국내 키워드추가2.csv', index=False, encoding='utf-8-sig')