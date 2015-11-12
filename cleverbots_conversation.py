import time 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
browser = webdriver.Firefox() 
browser2 = webdriver.Firefox() 
browser.get("http://cleverbot.com") 
browser2.get("http://cleverbot.com") 
time.sleep(15) 
input_for_bot = browser.find_element_by_name("stimulus") 
input_for_bot2 = browser2.find_element_by_name("stimulus") 
output_from_bot = "" 
output_from_bot2 = "Hey, friend, what's up" 
for i in range(0, 200): 
    input_for_bot.send_keys(output_from_bot2) 
    input_for_bot.send_keys(Keys.RETURN) 
    output_from_bot = "" 
    time.sleep(5) 
    for elem in browser.find_elements_by_xpath('.//span[@class="bot"]'): 
        output_from_bot = elem.text 
    input_for_bot2.send_keys(output_from_bot) 
    input_for_bot2.send_keys(Keys.RETURN) 
    output_from_bot2 = "" 
    time.sleep(5) 
    for elem in browser2.find_elements_by_xpath('.//span[@class="bot"]'): 
        output_from_bot2 = elem.text

