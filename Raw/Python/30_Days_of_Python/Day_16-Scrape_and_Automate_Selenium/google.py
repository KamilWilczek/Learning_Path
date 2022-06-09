import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()  # Firefox()

url = "https://google.com"
browser.get(url)

# google consent
search_el = browser.find_element(By.ID, "L2AGLb").click()
# print(search_el)

"""
<input type='text' class='' id='' name='???' />
<textarea name='???' ></textarea>

<input name="q" type="text"> # from google search inspect
<button id="L2AGLb" class="tHlp8d" data-ved="0ahUKEwj_1cbg3Z_4AhXwtYsKHcH3AxQQiZAHCB8"><div class="QS5gu sy4vM" role="none">Zgadzam się</div></button>
"""

time.sleep(3)
name = "q"
search_el = browser.find_element(By.NAME, "q")
# print(search_el)

search_el.send_keys("selenium python")

"""
# submitting forms
<input type='submit' />
<button type='submit' />
<form></form>

<input class="gNO89b" value="Szukaj w Google" aria-label="Szukaj w Google" name="btnK" role="button" tabindex="0" type="submit" data-ved="0ahUKEwi9lef04p_4AhVl-yoKHfmiDKsQ4dUDCAs">
"""
submit_btn_el = browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
print(submit_btn_el.get_attribute("name"))
time.sleep(2)
submit_btn_el.click()
