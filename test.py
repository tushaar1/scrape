import requests

for shoe in page_soup:
    test = page_soup.find_all('div', {'class': 'content-box'}).text
    release_date = test
    results.append(release_date)
print(results)



put this after driver.get(url)
elem = driver.find_element_by_tag_name("body")
# no_of_pagedowns = 350
no_of_pagedowns = 3

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

    """the above code opens up the website and scrolls down """
    # for shoe in page_soup.find_all('div', {'class':'content-box'}):
    #    print(shoe.text).strip()

    """
    release-date, span
    release-price, span
    release-rating, div
    name - h2, a, id="", href="" text
    post-data, div 
    """


        for shoe in page_soup:
            date = page_soup.find('span', {'class': 'release-date'})
            name = page_soup.find('h2', {'a': ''})
            price = page_soup.find('span', {'class': 'release-price'})
            hype = page_soup.find('div', {'class': 'release-rating'})
            url = page_soup.find('a')['href']
            results.append((date, name, price, hype, url))
        print(results)

class="row"
# sneaker_singlepost

< div class =​"col lg-12" id=​"sneaker_singlepost" > ​
id = "sneaker_singlepost"

records = []
for result in results:
    date = result.find('release-date')

    df = pd.DataFrame(results, columns=['date', 'name', 'price', 'rating'])
    df.to_csv('sneakerrelease.csv', index=False, encoding='utf-8')

    for shoe in page_soup:
        for date in page_soup.find_all('span', {'class': 'release-date'}):
            release_date = shoe.text.strip()
            results.append((release_date))

            '''release date'''
            for shoe in soup.find_all('span', {'class': 'release-date'}):
                date = shoe.text.strip()
            '''shoe name'''
            for shoe in soup.find_all('h2', {'a': ''}):
                name = shoe.text.strip()
            '''release price'''
            for shoe in soup.find_all('span', {'class': 'release-price'}):
                price = shoe.text.strip()
            '''release rating'''
            for shoe in soup.find_all('div', {'class': 'release-rating'}):
                rating = shoe.text.strip()


https://stackoverflow.com/questions/46759563/accessing-nested-elements-with-beautifulsoup

    for item in soup.find_all(class_="release-rating")[:2]:
        print(item.text)

        dates = soup.find_all('span', {'class': 'release-date'})
        print(len(dates))
        name = soup.find_all('h2', {'a': ''})
        print(len(name))
        price = soup.find_all('span', {'class': 'release-price'})
        print(len(price))
        # rating = soup.find_all('span', {'class': 'release-rating'})
        for rating in soup.find_all(class_="release-rating"):
            hype = rating.text.strip()
            print(len(hype))

response = requests.post(request_url, data=payload, headers=request_headers)
        
response = requests.post('https://sneakernews.com/wp-admin/admin-ajax.php?action=release_date_load_more&nextpage=2&category_name=sneaker-release&start_from=0&page_id=225762&last_month_box=March%202020', data=payload, headers=request_headers)