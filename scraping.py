import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# create a variable to hold the url I want to scrape
url = 'https://www.marketwatch.com/investing/stock/AAPL'
# check the request status, to ensure we can collect data
page = requests.get(url) 
# create a variable that pulls the HTML doc
soup = BeautifulSoup(page.text, 'lxml')

current_price = soup.find('bg-quote', class_ = 'value').text
print("Current Price: $", current_price)
settle_price = soup.find('td', class_ = 'table__cell u-semi').text

annual_range = soup.find('mw-rangebar', class_ = 'element element--range range--yearly')
lowest_price = annual_range.find_all('span', class_ = 'primary')[0].text
highest_price = annual_range.find_all('span', class_ = 'primary')[1].text
print("52-week range: $", lowest_price, '-', '$',highest_price)

# Or to start adding the data above into a table, you can use this template below 
# price_range_list = []
# i in price_range:
    #prices = i.text
    #price_range_list.append(prices)
    
# print(price_range_list)

#  *** STOCKS ONLY ***
analyst_rating = soup.find('li', class_ = 'analyst__option active').text
print("Analyst Say it is: ", analyst_rating)
