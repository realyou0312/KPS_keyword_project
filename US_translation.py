from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from tqdm import tqdm

header = {
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

df = pd.read_csv('C:/Users/kakaopaysec/PycharmProjects/KPS_keyword_project/US_merge.csv', encoding='utf-8')
datas = df.values.tolist()
datas = datas[:300]
i = 0
print(datas[0])
result = dict()

for data in tqdm(datas):
    i += 1

    new_data = []
    new_data.append(data[0])
    new_data.append(data[1])
    new_data.append(data[2])
    new_data.append(data[3])

    brands = data[4:]
    for brand in brands:

        try:
            if pd.isna(brand):
                new_data.append("")
                continue


            if brand == "":
                new_data.append(brand)
                continue

            print("----", brand, "----")

            driver = webdriver.Chrome(executable_path=r"C:/Users/kakaopaysec/chromedriver.exe")

            driver.get(f'https://translate.google.co.kr/?hl=ko&sl=en&tl=ko&text={brand}&op=translate')

            WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CLASS_NAME, "zEswK")))

            src = driver.page_source
            soup = BeautifulSoup(src, 'html.parser')
            trans_data = soup.select('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb > div.dePhmb > div > div.J0lOec > span.VIiyi > span > span')
            # yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb.as3dlc > div.dePhmb > div > div.J0lOec > a
            new_data.append(brand)
            if trans_data:
                new_data.append(trans_data[0].text)
                print("----", trans_data[0].text, "----")
            driver.quit()
        except Exception as e:
            print("error : ", e)
            new_data.append(brand)

    result[data[0]] = new_data


result_df = pd.DataFrame.from_dict(result, orient='index')
result_df.to_csv('C:/Users/kakaopaysec/PycharmProjects/KPS_keyword_project/US_transliteration.csv', encoding='utf-8-sig', index=False)