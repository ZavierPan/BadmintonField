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

FIELD_ID = {}
XPATH_IDs = []

def get_filed_info():
    global FIELD_ID, XPATH_IDs

    if args.f == 0:
        print(cst.ZHONGZHENG_FIELD_INFO)
        basic_url = cst.ZHONGZHENG_URL
        login_alert_num = 1
        FIELD_ID = cst.ZHONGZHENG_FIELD_ID
        XPATH_IDs = cst.ZHONGZHENG_FIELD_XPATH_IDs
    elif args.f == 1:
        print(cst.XINYI_FIELD_INFO)
        basic_url = cst.XINYI_URL
        login_alert_num = 2
        FIELD_ID = cst.XINYI_FIELD_ID
        XPATH_IDs = cst.XINYI_FIELD_XPATH_IDs
    else:
        raise Exception("Please use -f arguments")

    return basic_url, login_alert_num

def get_target_date():

    # 執行日期
    target_time = "{}-00-00-00".format(args.td)
    target_time = datetime.strptime(target_time, "%Y/%m/%d-%H-%M-%S")

    return target_time

def get_play_date():

    # 打球日期
    play_time = int(input("輸入打球時間 (8~22): ")) #詢問時間
    play_date = args.pd
    print("Play Date: ", play_date)

    return play_date, play_time

def get_play_field():

    #詢問場地選擇
    play_field_char = input("輸入場地編號 A, B, C, ...: ")
    play_field_id, play_field_xpath_ids = FIELD_ID[play_field_char], XPATH_IDs[play_field_char]
    print(play_field_id, play_field_xpath_ids)
    
    return play_field_char, play_field_id, play_field_xpath_ids

def login(driver, basic_url, login_alert_num):

    # 跳至活動中心登入畫面
    driver.get(basic_url + "?module=login_page&files=login")

    # 關閉Alert視窗
    for i in range(login_alert_num):
        driver.switch_to_alert().accept()

    # 自動輸入帳密

    # 自動辨識認證碼並登入

    # 登入完成才跳出迴圈
    while len(driver.find_elements_by_id("ContentPlaceHolder1_Panellogin"))!=0:
        pass

    return

def get_booking_url(basic_url, play_date, play_time, play_field):
    booking_url = basic_url + "?module=net_booking&files=booking_place&StepFlag=25&" + "QPid={}&QTime={}&PT=1&D={}".format(play_field, play_time, play_date)
    return booking_url

def get_menu_url(basic_url, play_date):
    menu_url = basic_url + "?module=net_booking&files=booking_place&StepFlag=2&PT=1&D={}&D2=1".format(play_date)
    return menu_url

def jump_to_menu(driver, menu_url):
    driver.get(menu_url)
    return

def main():

    basic_url, login_alert_num = get_filed_info()

    target_time = get_target_date()

    play_date, play_time = get_play_date()

    play_field_char, play_field_id, play_field_xpath_ids = get_play_field()

    # 取得url
    booking_url = get_booking_url(basic_url, play_date, play_time, play_field_id)
    menu_url = get_menu_url(basic_url, play_date)
    print("Menu URL: ", menu_url)

    # 打開瀏覽器
    driver = webdriver.Chrome('./chromedriver.exe')

    # 登入
    login(driver, basic_url, login_alert_num)

    # 超過指定時間才跳出迴圈
    while datetime.now() < target_time:
        pass

    # 跳至預約畫面
    jump_to_menu(driver, menu_url)

    xpath_base = "//*[@id=\"ContentPlaceHolder1_Panel_Step2\"]/table/tbody/tr[2]/td/table/tbody/tr[{}]/td[4]/img"
    icon = driver.find_element_by_xpath(xpath_base.format(XPATH_IDs[play_field_char][play_time-8]))
    icon.click()
    driver.switch_to_alert().accept()

    # 轉移至訂單
    driver.get(basic_url + "?module=member&files=orderx_mt")

    time.sleep(600)


    return

if __name__ == '__main__':
    main()