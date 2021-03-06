
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

regwebAddress = 'https://www.worldometers.info/coronavirus/country/us/'

res = requests.get(regwebAddress)
res.raise_for_status()
df_list=pd.read_html(res.text)
table = df_list[0]
table2 = df_list[1]

print('Deaths today:  ' + str(table.NewDeaths[0]) + '   Deaths yesterday:  ' + str(table2.NewDeaths[0]))

# print yesterday's results:
sorted_df = table2.sort_values(by='NewDeaths', ascending=False)
sorted_df.reset_index(inplace=True)
sorted_today=table.sort_values(by='NewDeaths', ascending=False)
sorted_today.reset_index(inplace=True)
print('Top States by New Deaths and Cases')
print('Rank  Deaths'+"\t"+'Cases'+"\t"+'State')
print('Today')
for i in range(2,12):
    print('Rank ' + str(i-1) + ':  ' + str(sorted_today.NewDeaths[i]) + "\t"+str(sorted_today.NewCases[i])+"\t"+sorted_today.USAState[i] )
print('Yesterday')
for i in range(2,12):
    print('Rank ' + str(i-1) + ':  ' + str(sorted_df.NewDeaths[i]) + "\t" + str(sorted_df.NewCases[i]) + "\t" + sorted_df.USAState[i])


