#How many events do we have?
#How many events do we have for each activity name?
#How many cases do we have?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv('data.txt', delimiter="\t") #read dataset
data.head(50)

data["ActivityName"].count() #How many events do we have

data["ActivityName"].value_counts() # How many events do we have for each activity nam

data["eLetter_ID"].value_counts().count() # How many cases do we have

data["eLetter_Type"].value_counts() # How often eLetter_Type they occur?

#Transforming the data into an event log

#1. Calculating the timestamps for each row.
#2. Combining two subsequent rows for the same activity into one with start and complete timestamp. 
#3. Removing all rows for which we do not have a matching second row. 

start_time = pd.Timestamp('2016-1-1 10:00')
data['concant_time'] = [start_time + timedelta(seconds=s) for s in data['Time']]
data['concant_time'] # Calculating the timestamps for each row.

idx = 0
delIndex = [];

while idx < data["ActivityName"].count() - 1:
    if data["ActivityName"][idx] == data["ActivityName"][idx+1]:
        idx += 2
        continue
    delIndex.append(idx)
    idx += 1

transformed_data = data.drop(delIndex) #Removing all rows for which we do not have a matching second row
transformed_data.head(50)

Checking the transformed data 

#Calculate the difference between start and complete time for each event and show the distribution 

transformed_data["ActivityName"].count() # How many transformed events do we have
transformed_data["ActivityName"].value_counts() # How many transformed events do we have for each activity name
transformed_data["eLetter_ID"].value_counts().count() # How many transformed cases do we have
transformed_data["eLetter_Type"].value_counts() # How often transformed eLetter_Type they occur?
for idx in range(0,len(modify)-1,2):
    print(modify.iloc[idx]['ActivityName'], " : ", modify.iloc[idx+1]['Time'] - modify.iloc[idx]['Time']) # difference between start and complete time for each event 

#Forward the starting date of your events and use the standard Twitter search API to get the number of tweets about your event for each day. This you could add as an extra column to each event so we exactly know how much people talked about your event while our process was running 

import datetime

startDate = datetime.datetime(2016, 1, 1, 0, 0, 0)
endDate =   datetime.datetime(2020, 2, 20, 0, 0, 0)

from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['activity name', 'penguin']) # defining name of activity and of coursen our penguins we would like to have a look for
    tso.set_language('de') # if we want to see German tweets only

    # TwitterSearch with tokens
    ts = TwitterSearch(
        consumer_key = '?',
        consumer_secret = '?',
        access_token = '?',
        access_token_secret = '?'
     )

     # this process will show results of udername of person and what he tweeted related to activity and penguins.
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as error: 
    print(error)
