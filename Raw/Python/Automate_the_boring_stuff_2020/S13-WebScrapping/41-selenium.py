from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# browser = webdriver.Chrome()
# browser.get('https:\\automatetheboringstuff.com')
# browser.get('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')
# elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')
# print(elem)

# elem.click()
# elems = browser.find_elements_by_css_selector('p')
# print(len(elems))
# searchElem = browser.find_element_by_css_selector('#searchInput')
# searchElem.send_keys('zombie')
# searchElem.submit()
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()



browser = webdriver.Chrome()
browser.get('https:\\automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > p:nth-child(8)')
print(elem.text)
# elem = browser.find_element_by_css_selector('html')
# print(elem.text)