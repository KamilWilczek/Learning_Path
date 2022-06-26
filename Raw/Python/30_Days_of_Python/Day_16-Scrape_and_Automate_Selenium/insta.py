# import getpass

# my_password = getpass.getpass('What is your password?\n"')

# print(my_password)
# from requests import post
import os
import requests
from urllib.parse import urlparse

import selenium
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
time.sleep(5)
post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements(By.XPATH, post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)

time.sleep(2)
video_els = browser.find_elements(By.XPATH, "//video")
time.sleep(2)
image_els = browser.find_elements(By.XPATH, "//img")
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# TODO: PIL to verify the size of any given image.
def scrape_and_save(elements):
    for el in elements:
        url = el.get_attribute("src")
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        # TODO: adding to whom belongs posts
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)


# scrape_and_save(video_els)
# scrape_and_save(image_els)

"""
LONG TERM Goal:
Use machine learning to classify the post's
image or video
and then comment in a relevant fashion
"""

"""
<textarea aria-label="Dodaj komentarz..." placeholder="Dodaj komentarz..." class="_ablz _aaoc" autocomplete="off" autocorrect="off" style="height: 18px !important;"></textarea>
"""


def automate_comment(content="That is cool!"):
    time.sleep(5)
    comment_xpath_str = "//textarea[contains(@placeholder, 'Dodaj komentarz')]"
    comment_el = browser.find_element(By.XPATH, comment_xpath_str)
    # try except fixes "StaleElementReferenceException: Message: stale element reference: element is not attached to the page document"
    try:
        comment_el.send_keys(content)
    except:
        comment_el = browser.find_element(By.XPATH, comment_xpath_str)
        comment_el.send_keys(content)
    submit_btns_xpath = "button[type='submit']"
    submit_btns_els = browser.find_elements(By.CSS_SELECTOR, submit_btns_xpath)
    time.sleep(2)
    for btn in submit_btns_els:
        try:
            btn.click()
        except:
            pass


automate_comment(content="That is cool!")

print("KONIEC")
