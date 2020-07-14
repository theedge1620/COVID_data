#! python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:40:54 2017

@author: JBC4

This program scrapes worldometers for the US and outputs two files, one for 
current data (today) and one for the previous day (yesterday)

"""

import requests
import pandas as pd

NRCproxies = { 
        'http': 'http://148.184.186.51:80',
        'https': 'http://148.184.186.51:80',
}


regwebAddress = 'https://www.worldometers.info/coronavirus/country/us/'

res = requests.get(regwebAddress,proxies=NRCproxies, verify=False)
res.raise_for_status()
df_list=pd.read_html(res.text)
table = df_list[0]
table.to_excel("coronavirus_US_today.xlsx")
table2 = df_list[1]
table2.to_excel("coronavirus_US_yesterday.xlsx")

