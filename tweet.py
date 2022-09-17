from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os

options = Options()
options.add_argument(f"user-data-dir={os.getcwd()}cookies")
options.add_argument("start-maximize")
driver = webdriver.Chrome(options=options)
driver.get("https://twitter.com")
time.sleep(2)
sendmessage = driver.find_element_by_xpath("*//*[@contenteditable='true']")
sendmessage.send_keys("test")
time.sleep(2)
kliktweet = driver.find_element_by_xpath("//div[@data-testid='tweetButtonInline']")
kliktweet.click()
time.sleep(60)
driver.quit()