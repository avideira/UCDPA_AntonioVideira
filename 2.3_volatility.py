import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

#take the csv file and converting it to a DataFrame object
#index_col = 0 will set the first column up as the row index
bitcoin_data = pd.read_csv('Data/btc-usdt.csv', usecols=['Open Time', 'Close'])
ethereum_data = pd.read_csv('Data/eth-usdt.csv', usecols=['Open Time', 'Close'])
binance_data = pd.read_csv('Data/bnb-usdt.csv', usecols=['Open Time', 'Close'])
solana_data = pd.read_csv('Data/sol-usdt.csv', usecols=['Open Time', 'Close'])

#let's merge the data into one dataframe, based on the date
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

start_date = pd.to_datetime('2020-01-01 00:00:00.000000000')
end_date = pd.to_datetime('2022-01-01 00:00:00.000000000')                         
df_coins['Open Time'] = pd.to_datetime(df_coins['Open Time']) 

df_condition = (df_coins['Open Time']>= start_date) & (df_coins['Open Time']<= end_date)

crypto_lasttwoyear = df_coins.loc[df_condition]

crypto_data = crypto_lasttwoyear.set_index('Open Time')

#print(crypto_data.head())
#print(crypto_data.shape)

# Returns i.e. percentage change in the closing price and drop the first row with NA's
returns = crypto_data[['Close_btc', 'Close_eth', 'Close_bnb']].pct_change(fill_method="bfill").dropna(axis=0)

#volatility, standard deviation of the returns
returns.std()

print(returns.head())
print(returns.shape)

#to format the x ticks
months = mdates.MonthLocator(interval=1)
monthsFmt = mdates.DateFormatter('%Y-%m')

#ploting the histogram
fig, axs = plt.subplots(3,1,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
axs[0].hist(returns['Close_btc'], bins=20, range=(-0.2, 0.2))
axs[0].set_title('BTC')
axs[1].hist(returns['Close_eth'], bins=20, range=(-0.2, 0.2))
axs[1].set_title('ETG')
axs[2].hist(returns['Close_bnb'], bins=20, range=(-0.2, 0.2))
axs[2].set_title('BNB')

#fig.savefig(volatility_2_years.png')

plt.show()