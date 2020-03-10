from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

urllib3.disable_warnings()


driver = webdriver.Chrome()
driver.get('https://sneakernews.com/release-dates/')
heights = []
counter = 0
records = []
for i in range(1, 300):
    bg = driver.find_element_by_css_selector('body')
    time.sleep(0.1)
    bg.send_keys(Keys.END)
    heights.append(driver.execute_script("return document.body.scrollHeight"))
    try:
        bottom = heights[i - 16]
    except:
        pass
    if i % 16 == 0:
        new_bottom = heights[i - 1]
        if bottom == new_bottom:
            url = 'https://sneakernews.com/release-dates/'
            http = urllib3.PoolManager()
            response = http.request('GET', url)

            for shoe in url:
                http = urllib3.PoolManager()
                response = http.request('GET', url)
                soup = BeautifulSoup(response.data.decode('utf-8'), features="lxml")
                results = soup.find_all('span', attrs={'class': 'release-date'})
                records.append(results)
            print(records)
