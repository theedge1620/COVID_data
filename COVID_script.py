#!/usr/bin/env python
# coding: utf-8

# ### JHU COVID-19 data - Daily and Weekly Confirmed and Deaths Calculation
# 
# This notebook calculates and appends the daily and weekly (last 7 days) totals for confirmed COVID-19 cases and deaths for the US data provided by the John's Hopkins University Center for Systems Science and Engineering (JHU CSSE).  JHU CSSE posts daily updates to its data to GitHub at:
# 
# https://github.com/CSSEGISandData/COVID-19
# 
# The following code assumes you have downloaded the JHU CSSE data and placed this file in a directory directly above the cloned or downloaded repository.

# In[8]:


# Import pandas and read in latest US confirmed and death time history data:

import pandas as pd
covid_US_confirmed = pd.read_csv("./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
covid_US_deaths = pd.read_csv("./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")

# drop all but the last two weeks of data:
covid_US_confirmed.drop(covid_US_confirmed.iloc[:, 11:-14], inplace = True, axis = 1)
covid_US_deaths.drop(covid_US_deaths.iloc[:, 11:-14], inplace = True, axis = 1)


# #### Calculate daily and weekly totals:
# 
# The following code calculates the daily and weekly totals for confirmed cases and deaths, since the JHU data always appends the current days date as the last column in their dataset.

# In[9]:


new_cases_US_daily = covid_US_confirmed[covid_US_confirmed.columns[-1]]-covid_US_confirmed[covid_US_confirmed.columns[-2]]
new_cases_US_weekly = covid_US_confirmed[covid_US_confirmed.columns[-1]]-covid_US_confirmed[covid_US_confirmed.columns[-8]]
new_deaths_US_daily = covid_US_deaths[covid_US_deaths.columns[-1]]-covid_US_deaths[covid_US_deaths.columns[-2]]
new_deaths_US_weekly = covid_US_deaths[covid_US_deaths.columns[-1]]-covid_US_deaths[covid_US_deaths.columns[-8]]


# In[10]:


# Print totals as a check:

print('Total new cases in US in last 24 hours:  ' + str(new_cases_US_daily.sum()))
print('Total new cases in US in last 7 days  :  ' + str(new_cases_US_weekly.sum()))
print('Total new cases in US in last 24 hours:  ' + str(new_deaths_US_daily.sum()))
print('Total new cases in US in last 7 days  :  ' + str(new_deaths_US_weekly.sum()))


# In[11]:


#  Append the new data to the dataframes for confirmed cases and deaths:
covid_US_confirmed['New Cases Daily']=new_cases_US_daily
covid_US_confirmed['New Cases Weekly']=new_cases_US_weekly
covid_US_deaths['New Deaths Daily']=new_deaths_US_daily
covid_US_deaths['New Deaths Weekly']=new_deaths_US_weekly


# In[12]:


# Write the new files to a .csv file that has the calculated fields as the last columns:
covid_US_confirmed.to_csv('current_confirmed.csv')
covid_US_deaths.to_csv('current_deaths.csv')

