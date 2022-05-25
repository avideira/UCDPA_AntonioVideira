import pandas as pd
import numpy as np

#take the csv file and converting it to a DataFrame object
#index_col = 0 will set the first column up as the row index
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
#no empty values in this dataset 
#no need for drop or fill missing values

#understand the data
#print(df_coins.head())
#print(df_coins.shape)

#let's get the data for the last two year: 2020 and 2021
start_date = pd.to_datetime('2020-01-01 00:00:00.000000000')
end_date = pd.to_datetime('2022-01-01 00:00:00.000000000')                         
df_coins['Open Time'] = pd.to_datetime(df_coins['Open Time']) 
df_condition = (df_coins['Open Time']>= start_date) & (df_coins['Open Time']<= end_date)

crypto_lastyears = df_coins.loc[df_condition]

# saving the dataframe to a csv
crypto_lastyears.to_csv('Data\Crypto_Data_Merged.csv')