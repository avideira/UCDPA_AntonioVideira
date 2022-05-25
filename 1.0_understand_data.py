import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#take the csv file and converting it to a DataFrame object
bitcoin_data = pd.read_csv('Data/btc-usdt.csv')

# See the keys
#print df.keys()
#understand the data
#print(bitcoin_data.head())
#print(bitcoin_data.shape)

#get row where bitcoin reached the hightest value
bitcoin_high = bitcoin_data.loc[bitcoin_data['High'] == bitcoin_data['High'].max()]
print(bitcoin_high[['Open Time','High','Low', 'Volume']])

#we can sorted the DF also and get the hightest value on the 1st row
bitcoin_sorted_high = bitcoin_data.sort_values(by='High', ascending=False)
#print(bitcoin_sorted_high.head())

#Date is not a Datetimelike value
#Error: Can only use .dt accessor with datetimelike value
#Convert to Date
bitcoin_data['Open Time'] = pd.to_datetime(bitcoin_data['Open Time'], format='%Y-%m-%d')

#############################################################################################

#check how many days BTC was bigger or equal than 60k
bitcoin_60 = bitcoin_data[bitcoin_data['High'] >= 60000]

#print(bitcoin_60)

unique_days = len(bitcoin_60['Open Time'].dt.normalize().unique())

print("Days that bitcoin was over or equal than 60k is " + str(unique_days) + " days.")
#############################################################################################

#group by Date and calculate some agg for each year
#sum(), mean(), median(), min(), and max()
bitcoin_by_year = bitcoin_data.groupby(bitcoin_data['Open Time'].dt.year).\
                                    agg({'High':[np.max], 
                                        'Low':[np.min]})

bitcoin_by_year.columns = bitcoin_by_year.columns.droplevel(0)
#print(bitcoin_by_year.head())
#Let's calculate how much bitcoin % growth/loss, If bought in the bottom and sell on the top each year 100 * (p2 - p1) / p1
bitcoin_by_year['Percentage_Change'] = 100 * (bitcoin_by_year['amax'] -  bitcoin_by_year['amin']) / bitcoin_by_year['amin']

print(bitcoin_by_year)

#lets calculate the median price per month of bitcoin and plot it
#bitcoin_data['Year'] = bitcoin_data['Date'].dt.year
#bitcoin_median_month = bitcoin_data.groupby([bitcoin_data['Year'], bitcoin_data['Date'].dt.month]).median().reset_index()

#bitcoin_median_month['Date'] = pd.to_datetime(bitcoin_median_month['Date'])
#bitcoin_median_month.set_index('Date', inplace=True)

print(bitcoin_data.head())
bitcoin_data.set_index('Open Time', inplace=True)
#cleaner graph if we just plotted the monthly averages
bitcoin_median_month = bitcoin_data.resample('M').mean()
#round the dates off to whatever period you specify. round of to months
bitcoin_median_month.index = bitcoin_median_month.index.to_period('M')

bitcoin_median_month['High'].plot()

plt.show()