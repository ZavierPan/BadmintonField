import time
import argparse
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException



parser = argparse.ArgumentParser()
parser.add_argument("-f", type=int, choices=[0,1,2], help="0:大安")
parser.add_argument("-td", type=str, help="Target date, eg. 2021/3/7")
parser.add_argument("-pd", type=str, help="Play date, eg. 2021/3/20")

args = parser.parse_args()
print("""
中正活動中心
已被長租之場地 (2021/3/7更新)
週六 8~10 ABC
週六 10~12 AB
週六 14~16 ABC
週日 8~10 ABC
週日 10-12 BC

每周日晚上必搶 周日8~10 D E

# A號場 1112
# B號場 1113
# C號場 1114
# D號場 1115
# E號場 1116
""")


target_time = "{}-00-00-00".format(args.td)
target_time = datetime.strptime(target_time, "%Y/%m/%d-%H-%M-%S")
# print(target_time)

basic_url = "https://www.cjcf.com.tw/jj01.aspx?module=net_booking&files=booking_place&StepFlag=25&"

play_field = int(input("輸入場地編號: ")) #詢問場地選擇
play_time = int(input("輸入打球時間: ")) #詢問時間
play_date = args.pd
print("Play Date: ", play_date)

target_url = basic_url + "QPid={}&QTime={}&PT=1&D={}".format(play_field, play_time, play_date)
print("URL: ", target_url)

# 打開瀏覽器
driver = webdriver.Chrome('./chromedriver.exe')

# 跳至活動中心登入畫面
driver.get("https://www.cjcf.com.tw/jj01.aspx?module=login_page&files=login",)
# 關閉Alert視窗
driver.switch_to_alert().accept()

# 自動輸入帳密

# 自動辨識認證碼並登入

# 登入完成才跳出迴圈
while len(driver.find_elements_by_id("ContentPlaceHolder1_Panellogin"))!=0:
    pass

# driver.set_page_load_timeout(0.5)

# 超過指定時間才跳出迴圈
while datetime.now() < target_time:
    pass

count = 0
while True:
    driver.get(target_url)
    time.sleep(1)
    count += 1
    if count == 3:
        break

    


driver.get("https://www.cjcf.com.tw/jj01.aspx?module=member&files=orderx_mt")