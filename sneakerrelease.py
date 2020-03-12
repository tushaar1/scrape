from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://sneakernews.com/release-dates/'
driver = webdriver.Chrome()
driver.get(url)
elem = driver.find_element_by_tag_name("body")
# no_of_pagedowns = 350, to go to the bottom
no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1
url = 'https://sneakernews.com/release-dates/'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')

results = soup.find_all("div", attrs={'class': 'content-box'})
print(len(results))

records = []
for result in results:
    date = result.find(class_='release-date').text.strip()
    price = result.find(class_='release-price').text.strip()
    hype = result.find(class_='release-rating').text.strip()
    name = result.find('h2',{'a': ''}).text.strip()
    records.append((name, price, date, hype))
print(len(records))

df = pd.DataFrame(records, columns=['name', 'price', 'release date', 'popularity'])
print(df.head())
print(df.tail())
df.to_csv('sneaker_releases.csv', index=False, encoding='utf-8')

'''see if scrapy will help with ajax '''
