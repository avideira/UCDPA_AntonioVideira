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

#let's get the data for the last two year: 2020 and 2021
start_date = pd.to_datetime('2020-01-01 00:00:00.000000000')
end_date = pd.to_datetime('2022-01-01 00:00:00.000000000')                         
df_coins['Open Time'] = pd.to_datetime(df_coins['Open Time']) 
df_condition = (df_coins['Open Time']>= start_date) & (df_coins['Open Time']<= end_date)
crypto_lastyears = df_coins.loc[df_condition]

# saving the dataframe to a csv
crypto_lastyears.to_csv('Data\Crypto_Data_Merged.csv')

crypto_data = crypto_lastyears.set_index('Open Time')

#print(crypto_data.head())
#print(crypto_data.shape)
#print(crypto_data)

fig, axs = plt.subplots(4, 1, sharex=True, figsize=(12, 8))
fig.tight_layout(h_pad=1)

#to format the x ticks
months = mdates.MonthLocator(interval=1)
monthsFmt = mdates.DateFormatter('%Y-%m')

axs[0].set_title('BTC', fontsize = 8)
axs[0].plot(crypto_data.index, crypto_data['Close_btc'], 'r-.')

axs[1].set_title('ETH', fontsize = 8)
axs[1].plot(crypto_data.index, crypto_data['Close_eth'], 'g--')

axs[2].set_title('BNB', fontsize = 8)
axs[2].plot(crypto_data.index, crypto_data['Close_bnb'],  'y-')

axs[3].set_title('SOL', fontsize = 8)
axs[3].plot(crypto_data.index, crypto_data['Close_sol'],  'b-')
axs[3].set_xlabel('Date')

#define axis for all plots
for ax in axs:
    ax.tick_params(axis='both', which='major', labelsize=8)
    ax.set_xticks(crypto_data.index)
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(monthsFmt)
    ax.grid()
    ax.set_ylabel('Price')
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=20)

plt.subplots_adjust(top=0.9,bottom=0.08, left=0.08, right=0.92)

#fig.savefig('close_price_chart_2_years.png')
plt.show()
