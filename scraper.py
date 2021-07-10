#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 23:26:08 2021

@author: rufus
"""

import requests,bs4,re,time

# Date and Time
nowDate = time.strftime('%d/%m/%y' , time.localtime())
nowTime = time.strftime('%H.%M' , time.localtime())

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

# Copy percentage change text from html
elemsChange = parser.select('#export-chart-element > div > section > div.coin-info-list.price-list > div:nth-child(2) > div.data-definition > div > span > span.percent-value-text')

# Extract the percent change
string2 = str(elemsChange)
PercentRegex = re.compile(r'((-)*\d+.\d+)')
percent = PercentRegex.findall(string2)
print('The percent-change of Bitcoin price on {} at {} is {}%'.format(nowDate , nowTime, percent[0][0]))