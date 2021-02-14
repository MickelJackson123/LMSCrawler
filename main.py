from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from os.path import expanduser
from selenium.webdriver.common.keys import Keys
import time
import re

username = ""
password = ""

info = open("info.txt", "r")
for index, line in enumerate(info.readlines()):
    if index == 0:
        username = line
    if index == 1:
        password = line
        break
info.close()
username = username.strip()
password = password.strip()
print("Username:{}, pass:{}".format(username, password))

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.notifications": 1
})
opt.add_argument("--mute-audio")

# If you don't have compatible version of Chrome selenium, you can uncomment below and comment the next
# browser = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
browser = webdriver.Chrome(expanduser('~') + '/Downloads/chromedriver', options=opt)
browser.get('http://lms.ui.ac.ir/login/')

username_btn = browser.find_element_by_id("username")
username_btn.send_keys(username)

password_btn = browser.find_element_by_id("password")
password_btn.send_keys(password)

submit = browser.find_element_by_id("submit")
submit.send_keys(Keys.ENTER)

ss = re.findall("/jaam.*?\"", browser.page_source)
for index, link in enumerate(ss):
    link = "http://lms.ui.ac.ir" + link[:-1]
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[index + 1])
    print(link)
    browser.get(link)
    time.sleep(5)
    try:
        browser.find_element_by_xpath(xpath="//span/button[2]/span/i").click()
    except:
        browser.close()
