
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 23:26:08 2021

@author: rufus
"""

import requests, bs4, re, time, sqlite3

# Creating Database
conn = sqlite3.connect("bitcoin.db")

# Creating Table
# conn.execute("DROP TABLE BITCOIN")
conn.execute('''CREATE TABLE IF NOT EXISTS BITCOIN
         (ID    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         NOWDATE    VARCHAR(8)  NOT NULL,
         NOWTIME    VARCHAR(5) NOT NULL,
         PRICE  FLOAT,
         TIMESTAMP  FLOAT);''')

# Date and Time
nowDate = time.strftime('%d/%m/%y' , time.localtime())
nowTime = time.strftime('%H.%M' , time.localtime())
timestamp = time.time()

# Go to Webpage
webpage = requests.get('https://www.coindesk.com/price/bitcoin')

# Raise exception if there is an error
if webpage.status_code != requests.codes.ok:
    raise Exception("Error while downloading webpage")

# Copy price text from html
parser = bs4.BeautifulSoup(webpage.text,'html.parser')
elemsPrice = parser.select('#export-chart-element > div > section > div.coin-info-list.price-list > div:nth-child(1) > div.data-definition > div')

# Extract the price
string1 = str(elemsPrice).replace(',','')  # Replace commas in price
NumRegex = re.compile(r'\d+.\d+')
num = NumRegex.findall(string1)
print('The price of Bitcoin on {} at {} is ${}'.format(nowDate , nowTime, num[0]))

# Adding Data to sql database
conn.execute("INSERT INTO BITCOIN (NOWDATE,NOWTIME,PRICE,TIMESTAMP) \
             VALUES ('{}','{}',{:.2f},{:.2f} \
            )".format(nowDate,nowTime,float(num[0]),timestamp));
conn.commit()
conn.close()
