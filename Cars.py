
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

file = open('Vehicles.csv', 'w')
file.write('Name,'+'Price,'+'Fuel\n')

try:
    for page in range(1, 5):
        url = f'https://www.myauto.ge/ka/search/?vips=1&page={page}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/56.0.2924.87 Safari/537.36',
        }
        resp = requests.get(url, headers=headers)
        content = resp.text

        soup = BeautifulSoup(content, 'html.parser')
        car = soup.find('div', class_='search-lists-container')
        carName = car.find_all('div', {'itemprop': 'itemOffered'})

        for each in carName:
            title = each.find('a', {'itemprop': 'url'}).text.replace('იყიდება ', '').strip()
            print(title)
            try:
                price = 'GEL ' + each.find('span', class_='car-price').text
            except:
                price = 'ფასი შეთანხმებით'
            print(price)
            fuelType = each.find('div', {'data-info': 'ძრავი'}).text.strip()
            print(fuelType + '\n')
            file.write(title+','+price+','+fuelType+'\n')
        sleep(randint(4, 8))
except: pass
