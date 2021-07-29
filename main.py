from selenium import webdriver
import json
import pyautogui
from threading import Thread
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()


PROXY = "134.202.250.38:45785"
with open('Cookie/Paula Maxwell.json', 'r', newline='') as inputdata:
    cookies = json.load(inputdata)
options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument("user-data-dir=C:\\Users\\phant\\AppData\Local\\Google\\Chrome\\User Data\\Profile 6")
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)


def enter_proxy_auth(proxy_username, proxy_password):
    sleep(1.5)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')


driver.get("https://www.etsy.com/")
Thread(target=enter_proxy_auth, args=('Selphantridungdz', 'N7a8PfA')).start()
sleep(3)
driver.delete_all_cookies()
i = 0
while i < len(cookies):
    cookies[i].pop('sameSite')
    cookies[i].pop('domain')

    driver.add_cookie(cookies[i])
    i+=1

driver.get("https://www.etsy.com/")

f = open("searchtext.txt", "r")

ListSearchText = []

for x in f:
    ListSearchText.append(x)

i = 0
sleep(1)
e =0
while e < 3:
    if e >0:
        driver.get("https://www.etsy.com/")
    input = driver.find_element_by_id("global-enhancements-search-query")
    input.send_keys(ListSearchText[randint(0,len(ListSearchText)-1)])

    input = driver.find_element_by_css_selector(".wt-input-btn-group__btn")
    input.click()
    try:
        driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")
        sleep(3)
        driver.execute_script("window.scrollTo({ top: "+str(randint(0,1080))+", behavior: 'smooth' })")
        sleep(2)
        driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")
        sleep(3)
        driver.execute_script("window.scrollTo({ top: "+str(randint(1080,3080))+", behavior: 'smooth' })")
        sleep(2)
    except:
        sleep(3)

    links = driver.find_elements_by_class_name("wt-mb-xs-0")
    l = links[randint(0, len(links)-1)]
    l.click()

    driver.switch_to.window(driver.window_handles[1])

    sleep(2)

    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")
    sleep(3)
    driver.execute_script("window.scrollTo({ top: "+str(randint(0,1080))+", behavior: 'smooth' })")
    sleep(2)

    input = driver.find_element_by_css_selector(".wt-btn--fixed-floating .wt-display-block > svg")
    input.click()

    sleep(randint(0, 2))

    while i < randint(2, 6):
        links = driver.find_elements_by_class_name("wt-btn")
        l = links[10]
        l.click()
        sleep(3)
        i+=1

    try:
        select = Select(driver.find_element_by_id("inventory-variation-select"))
        select.select_by_index(randint(1, len(select.options) - 1))
    except:
        print("Khong co lua chon nao")
    sleep(2)
    try:
        select = Select(driver.find_element_by_id("inventory-variation-select-0"))
        select.select_by_index(randint(1, len(select.options) - 1))
    except:
        print("Khong co lua chon nao")
    sleep(2)
    try:
        select = Select(driver.find_element_by_id("inventory-variation-select-1"))
        select.select_by_index(randint(1, len(select.options) - 1))
    except:
        print("Khong co lua chon nao")
    sleep(2)
    try:
        textarea = driver.find_element_by_id("personalization-input")
        textarea.send_keys("hello")
    except:
        print("Khong viet gi ca")
    sleep(2)
    try:
        input = driver.find_element_by_css_selector(".wt-btn:nth-child(7) > div")
        input.click()
    except:
        print("Khong tim thay nut 7")

    try:
        input = driver.find_element_by_css_selector(".wt-btn:nth-child(8) > div")
        input.click()
    except:
        print("Khong tim thay nut 8")
    sleep(3)
    try:
        links = driver.find_elements_by_link_text('Contact shop')
        l = links[randint(0, len(links)-1)]
        l.click()
        sleep(1)
        message = driver.find_element_by_id(".cheact-text-input")
        message.send_keys("Hello")
    except:
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

    # driver.quit()
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])



    # input = driver.find_element_by_css_selector(".wt-tooltip__trigger > .etsy-icon:nth-child(3) > svg")
    # input.click()
    e+=1

