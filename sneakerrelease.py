from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://sneakernews.com/release-dates/'
driver = webdriver.Chrome()
driver.get(url)

uClient = uReq(url)  # open up a connection and grabs the webpage
page_html = uClient.read()  # puts the content into a variable
uClient.close()  # closes the file

results = []
page_soup = soup(page_html, 'html.parser')  # parses the html into a new variable

'''release date'''
for shoe in page_soup.find_all('span', {'class': 'release-date'}):
    print(shoe.text)

'''shoe name'''
for shoe in page_soup.find_all('h2', {'a': ''}):
    print(shoe.text)
'''release price'''
for shoe in page_soup.find_all('span', {'class': 'release-price'}):
    print(shoe.text)

'''release rating'''
for shoe in page_soup.find_all('div', {'class': 'release-rating'}):
    print(shoe.text)

