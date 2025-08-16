from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

def search():
    url = "https://trends.google.co.kr/trending?geo=KR&hl=ko"
    driver.get(url)
    time.sleep(2)

##실시간 검색어들 keyword리스트에 담기
    keyword = []
    keywordlist = driver.find_elements(By.CLASS_NAME, "mZ3RIc")
    for keywordlist in keywordlist:
        keyword.append(keywordlist.text)

##검색량 number리스트에 담기
    number = []
    numberlist = driver.find_elements(By.CLASS_NAME, "lqv0Cb")
    for numberlist in numberlist:
        number.append(numberlist.text)

## 1~10위까지 리스트 노출
    for i in range(0,10):
        print(i+1,keyword[i],number[i])


## 확인한 리스트중에서 보고싶은 기사키워드 관련뉴스 보는 함수 만들기
def choice(keyword):

    element = driver.find_element(By.XPATH,f"//*[contains(text(), '{keyword}')]")
    element.click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"xZCHj").click()


search()
choice('우정잉')