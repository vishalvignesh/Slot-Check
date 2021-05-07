from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import os
import time
from pynotifier import Notification
import re

chrome_options = Options()
#chrome_options.add_argument("--headless")


def chennai(driver):
    driver.get("https://www.cowin.gov.in/home")
    get_by_dist = driver.find_element_by_class_name('custom-checkbox').click()
    time.sleep(1)
    state_select = driver.find_element_by_id("mat-select-0").click()
    time.sleep(1)
    selector = driver.find_element_by_id("mat-option-31").click()
    time.sleep(1)
    district_selector = driver.find_element_by_id("mat-select-value-3").click()
    time.sleep(1)
    selector = driver.find_element_by_id("mat-option-41").click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[3]/button').click()

    time.sleep(1)
    get_age = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[3]/div/div[1]/label").click() #18+
    #get_age = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[3]/div/div[2]/label").click() #45+ Test Purpose
    time.sleep(1)

    result = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]/div/div/div").get_attribute('innerHTML').replace('><','> <')

    #print(result)
    
    re_search = '<a _ngcontent-...-c68=""> [0-9]+ </a>'

    
    if re.search(re_search,result) is not None:
        Notification(
	        title='Vaccine Slot Possibly Available',
	        description='Vaccine Slot Possibly Available',
	        duration=5,
	        urgency='normal'
            ).send()
    else:
        print('Vaccine Slot Not Available')



while(1):
    driver = webdriver.Chrome('./chromedriver',options=chrome_options)
    try:
        chennai(driver)
        driver.close()
    except:
        print()
        driver.close()
    time.sleep(2)








