# import getpass

# my_password = getpass.getpass('What is your password?\n"')

# print(my_password)
from requests import post
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.instagram.com"
browser.get(url)

# instagram cookie
# <button class="aOOlW   HoLwm " tabindex="0">Zezwól tylko na niezbędne pliki cookie</button>
# body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm
cookies_el = browser.find_element(By.CSS_SELECTOR, "button.aOOlW.HoLwm").click()

time.sleep(2)
username_el = browser.find_element(By.NAME, "username")
username_el.send_keys(INSTA_USERNAME)

password_el = browser.find_element(By.NAME, "password")
password_el.send_keys(INSTA_PASSWORD)

time.sleep(1.5)
submit_btn_el = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_btn_el.click()

# logging data save pop up
# react-root > section > main > div > div > div > div > button
# <button class="sqdOP yWX7d    y3zKF     " type="button">Nie teraz</button>
# //*[@id="react-root"]/section/main/div/div/div/div/button
# active the iframe and click the agree button
time.sleep(5)
logging_data_save_el = browser.find_element(By.CLASS_NAME, "sqdOP.yWX7d.y3zKF")
logging_data_save_el.click()


# notifications
# mount_0_0_f4 > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div._a9-z > button._a9--._a9_1
# <button class="_a9-- _a9_1" tabindex="0">Nie teraz</button>
time.sleep(3)
notifications_el = browser.find_element(By.CLASS_NAME, "_a9--._a9_1")
notifications_el.click()

body_el = browser.find_element(By.CSS_SELECTOR, "body")
html_text = body_el.get_attribute("innerHTML")
# print(html_text)

"""
<button class="_abn9 _abng _abni _abnn"><div class="_aacl _aaco _aacw _aad6 _aade">Obserwuj</div></button>
"""
# browser.find_elements(By.CSS_SELECTOR, 'button')

# xpath
# my_button_xpath = "//button"
# browser.find_element(By.XPATH, my_button_xpath)

# to follow all use recursive function
def click_to_follow(browser):
    # my_follow_xpath = (
    #     "//button[contains(text(), 'Obserwuj')][not(contains(text(), 'Obserwujesz'))]"
    # )

    my_follow_xpath = "//*[contains(text(), 'Obserwuj')][not(contains(text(), 'Obserwujesz'))][not(contains(text(), 'obserwujących'))][not(contains(text(), 'Obserwujący'))]"
    follow_btn_elements = browser.find_elements(By.XPATH, my_follow_xpath)
    for btn in follow_btn_elements:
        time.sleep(2)  # self-throttle
        try:
            btn.click()
        except:
            pass


# new_user_url = "https://www.instagram.com/ted/"
# browser.get(new_user_url)

time.sleep(2)
the_rock_url = "https://www.instagram.com/therock/"
browser.get(the_rock_url)

# post_url_pattern = "https://www.instagram.com/p/<post-slug-id>"
post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements(By.XPATH, post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)
