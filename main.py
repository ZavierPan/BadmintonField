import time
import argparse
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

import constant as cst

parser = argparse.ArgumentParser()
parser.add_argument("-f", type=int, choices=[0, 1], help="0:中正, 1:信義")
parser.add_argument("-td", type=str, help="Target date, eg. 2021/3/7")
parser.add_argument("-pd", type=str, help="Play date, eg. 2021/3/20")

args = parser.parse_args()


if args.f == 0:
    print(cst.ZHONGZHENG_FIELD_INFO)
    basic_url = cst.ZHONGZHENG_URL
    login_alert_num = 1
elif args.f == 1:
    print(cst.XINYI_FIELD_INFO)
    basic_url = cst.XINYI_URL
    login_alert_num = 2

# 執行日期
target_time = "{}-00-00-00".format(args.td)
target_time = datetime.strptime(target_time, "%Y/%m/%d-%H-%M-%S")

# 打球日期
play_field = int(input("輸入場地編號: ")) #詢問場地選擇
play_time = int(input("輸入打球時間 (8~22): ")) #詢問時間
play_date = args.pd
print("Play Date: ", play_date)

booking_url = basic_url + "?module=net_booking&files=booking_place&StepFlag=25&" + "QPid={}&QTime={}&PT=1&D={}".format(play_field, play_time, play_date)
print("URL: ", booking_url)

# 打開瀏覽器
driver = webdriver.Chrome('./chromedriver.exe')

# 跳至活動中心登入畫面
driver.get(basic_url + "?module=login_page&files=login",)
# 關閉Alert視窗
for i in range(login_alert_num):
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

# 每秒爬一次，共爬三次
driver.get(booking_url)


# 轉移至訂單
driver.get(basic_url + "?module=member&files=orderx_mt")

time.sleep(600)