import schedule
import time
import datetime

from selenium import webdriver
import csv
import time

def job():
    print("I'm working...")
    total = 0

    browser = webdriver.Firefox()

    browser.implicitly_wait(10)

    browser.get("https://valu.is/users/categories")

    web_data = browser.find_elements_by_xpath("//span[@class='va-list-item__count']")
    data2 = [x.text for x in web_data]
    #print(data2) # 文字列のデータ

    # 置換 ()なしに
    data_N = []
    for data in data2:
        after_data = data.replace("(", "")
        next_after_data = after_data.replace(")", "")
        data_N.append(next_after_data)
        #print(data_N)

    # Str →　Int
    Int_Data = [int(s) for s in data_N]
    #print(Int_Data)

    # このページの合計値
    #print(sum(Int_Data))
    total = sum(Int_Data) + total
    #合計値
    
    print(datetime.datetime.now())
    print(total)

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) 

