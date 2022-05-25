import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

#take the csv file and converting it to a DataFrame object
bitcoin_data = pd.read_csv('Data/btc-usdt.csv', usecols=['Open Time', 'Close'])
ethereum_data = pd.read_csv('Data/eth-usdt.csv', usecols=['Open Time', 'Close'])
binance_data = pd.read_csv('Data/bnb-usdt.csv', usecols=['Open Time', 'Close'])
solana_data = pd.read_csv('Data/sol-usdt.csv', usecols=['Open Time', 'Close'])

#let's merge the data into one dataframe, based on the Open Time
df_coins = bitcoin_data.merge(ethereum_data, on='Open Time', how='left', suffixes=['_btc','_eth'])\
    .merge(binance_data, on='Open Time', how='left')\
        .merge(solana_data, on='Open Time', how='left', suffixes=['_bnb','_sol'])

#check for missing data
missing_values_count = df_coins.isnull().sum()
print(missing_values_count[0:8])
#replace NaN with zeros
df_coins['Close_sol'] = pd.to_numeric(df_coins['Close_sol'], errors='coerce').fillna(0)

#understand the data
#print(df_coins.head())
#print(df_coins.shape)

#let's get the data for the last two years: 2020 and 2021
start_date = pd.to_datetime('2020-01-01 00:00:00.000000000')
end_date = pd.to_datetime('2022-01-01 00:00:00.000000000')                         
df_coins['Open Time'] = pd.to_datetime(df_coins['Open Time']) 
df_condition = (df_coins['Open Time']>= start_date) & (df_coins['Open Time']<= end_date)
crypto_lastyears = df_coins.loc[df_condition]

#print(crypto_data.head())
#print(crypto_data.shape)

#function to get min and max for each coin
def MinMax(df):
    return pd.Series(index=['min', 'max'], data=[df.min(), df.max()])

crypto_values = crypto_lastyears.apply(MinMax)
crypto_values.drop(crypto_values.columns[[0,4]], axis = 1, inplace = True)

for (colName, colData) in crypto_values.iteritems():
    num = colData.values[1]
    div = colData.values[0]
    if div <= 0: div == 1
    print('Percentage return from min value till max value for  ' + colName + ' : ', ((num - div)//div)*100 )

print(crypto_values)