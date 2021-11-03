#step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#step2.검색시작 페이지 입력
query = input('검색을 시작할 페이지를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www3.wipo.int/branddb/en/'
driver = webdriver.Chrome('C:/Users/kakaopaysec/PycharmProjects/KPS_keyword_project/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
driver.find_element_by_xpath('//*[@oldtitle="United States Trademarks"]').click()
driver.find_element_by_xpath('//*[@id="tabFortrademarkType_filter"]').click()
driver.find_element_by_xpath('//*[@oldtitle="WORD"]').click()
driver.find_element_by_xpath('//*[@id="tabForstatus_filter"]').click()
driver.find_element_by_xpath('//*[@oldtitle="ACT"]').click()
# driver.find_element_by_xpath('//*[@id="tabForholder_country_filter"]').click()
# driver.find_element_by_xpath('//*[@oldtitle="United States of America"]').click()
driver.find_element_by_xpath('//*[@id="status_filter"]/a[1]/span[1]').click()
time.sleep(2)

search_box = driver.find_element_by_css_selector("input#skipValue0")
search_box.clear()
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

for i in range(0, 3):
    driver.find_element_by_xpath('//*[@id="results"]/div[5]/a[2]/div[1]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@oldtitle="next page"]').click()
    time.sleep(5)
    print(f'{query}페이지에서 시작하여 {int(query) + i}페이지까지 다운 완료')

    url = 'https://www3.wipo.int/branddb/en/'
    driver = webdriver.Chrome('C:/Users/kakaopaysec/PycharmProjects/KPS_keyword_project/chromedriver')
    driver.get(url)

# search_box.send_keys(query)
# search_box.send_keys(Keys.RETURN)

#step5.뉴스 탭 클릭
# driver.webdriver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
# time.sleep(2)