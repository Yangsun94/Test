
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

options = Options()
options.add_argument("--start-maximized")
#화면 최대화
options.add_experimental_option("detach", True)
#화면 안꺼짐
driver = webdriver.Chrome(options=options)
#드라이버에 설정한 내용 적용
url = "https://www.google.com"
driver.get(url)
time.sleep(1)
action = ActionChains(driver)

driver.find_element(By.XPATH,'//*[@id="gb"]/div[3]/a').click()
#로그인 버튼을 찾아서 클릭
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[contains(@class,'whsOnd')]")))

action.send_keys('yangsunstudy').perform()
action.reset_actions()
#아이디 입력 후 액션 리셋
driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()

password = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//input[@type='password' and contains(@name,'Passwd')]")))
password.send_keys('study1234!@#$')

driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
#비밀번호 입력창 찾아 입력 후 클릭
time.sleep(2)

driver.get('https://mail.google.com/mail/u/0/#inbox')
#구글 메일 페이지로 이동
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.T-I.T-I-KE.L3').click()
#메일 보내기 버튼 찾아 클릭
time.sleep(2)
(
action.send_keys('yangsunstudy@gmail.com').key_down(Keys.TAB).key_down(Keys.TAB).pause(1)
.send_keys('제목입니다').key_down(Keys.TAB)
.send_keys('내용입니다').perform()
)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3').click()
#메일 내용 입력 후 보내기 버튼 클릭
time.sleep(3)
driver.quit()
#창 닫기













