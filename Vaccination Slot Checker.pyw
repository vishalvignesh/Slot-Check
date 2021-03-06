from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import os
import time
from pynotifier import Notification
import re
from notify_run import Notify
import pickle

phone_notif_count = 0
notif = None

if os.path.exists('notify_file'):
    with open('notify_file','rb') as n:
        notif = pickle.load(n)
    print(notif.endpoint)
else:
    notif = Notify()
    notif.register()
    with open('notify_file','wb') as n:
        pickle.dump(notif,n)
    print(notif.endpoint)

sleep_timer = 1
interval_timer = 5
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir="+os.getcwd()+'/chromeprofile') #Path to chrome profile
driver = webdriver.Chrome('./chromedriver',options=chrome_options)
driver.set_window_size(500,500)
driver.get("https://www.cowin.gov.in/home")
#chrome_options.add_argument("--headless") 
#chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#chrome_options.add_experimental_option('useAutomationExtension', False)

def login():
    driver.refresh()
    driver.get('https://selfregistration.cowin.gov.in')
    

def chennai():
    global phone_notif_count
    driver.refresh()
    get_by_dist = driver.find_element_by_class_name('custom-checkbox').click()
    time.sleep(sleep_timer)
    state_select = driver.find_element_by_id("mat-select-0").click()
    time.sleep(sleep_timer)
    selector = driver.find_element_by_id("mat-option-31").click()
    time.sleep(sleep_timer)
    district_selector = driver.find_element_by_id("mat-select-value-3").click()
    time.sleep(sleep_timer)
    selector = driver.find_element_by_id("mat-option-41").click()
    time.sleep(sleep_timer)

    driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[3]/button').click()

    time.sleep(sleep_timer)
    get_age = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[3]/div/div[1]/label").click() #18+
    #get_age = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[3]/div/div[2]/label").click() #45+ Test Purpose
    covaxin_only = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[3]/div/div[4]/label").click()
    time.sleep(sleep_timer)


    result = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]").get_attribute('innerHTML').replace('><','> <')
    #result = driver.page_source()
    #print(result)
    
    re_search = '<a _ngcontent-...-c68=""> [0-9]+ </a>'

    
    if re.search(re_search,result) is not None:
        Notification(
	        title='Vaccine Slot Possibly Available',
	        description='Vaccine Slot Possibly Available',
	        duration=5,
	        urgency='normal'
            ).send()
        if phone_notif_count == 0:
            notif.send('Vaccine Slot Possibly Available according to CoWin Website')
            phone_notif_count += 1
        else:
            phone_notif_count += 1
            print('New Notif Count: ',phone_notif_count)
            if phone_notif_count == 15:
                phone_notif_count = 0
    else:
        print('Vaccine Slot Not Available')
        phone_notif_count = 0


#login()
while(1):
    try:
        chennai()
        #login()
        None
    except:
        print('Error')
        driver.get("https://www.cowin.gov.in/home")
        driver.refresh()
    time.sleep(interval_timer)








