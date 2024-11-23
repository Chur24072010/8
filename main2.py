from bs4 import BeautifulSoup
import requests
import sqlite3

print('Lesson 10: Sqlite3')

# responce = requests.get('https://coinmarketcap.com/')
# coins_prices = []
#
# if responce.status_code == 200:
#
#     # print('before parser', responce.text)
#     item_site = BeautifulSoup(responce.text, features='html.parser')
#     coin_rates = item_site.find_all('div', {'class', 'sc-b3fc6b7-0 dzgUIj'})
#
#     for rate in coin_rates:
#         # print('rate object -> ', rate)
#         temp = rate.findNext().text[1:].replace(',', '')
#         price = float(temp)
#         # coin_rates.append(temp)
#         print('price -> ', price)
#
# print('coins prices', coins_prices)

# sqlite3 intarection via python

# temp_price = 25.123

connection = sqlite3.connect('main_raids.sl3', 10)
cur_db = connection.cursor()

cur_db.execute("CREATE TABLE main_raids (name TEXT, price FLOAT);")

# cur_db.execute("INSERT INTO coins_rates (price) VALUES (1.1);")
# cur_db.execute("INSERT INTO coins_rates (price) VALUES (@price);", {"price": temp_price})
#cur_db.execute("SELECT * FROM coins_rates;")
connection.commit()
result = cur_db.fetchall()
print(result)

connection.close()