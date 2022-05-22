import pandas as pd

#take the csv file and converting it to a DataFrame object
#index_col = 0 will set the first column up as the row index
bitcoin_data = pd.read_csv('Data/coin_Bitcoin.csv', index_col=0)

#understand the data
print(bitcoin_data.head())
print(bitcoin_data.shape)

#check for missing data
#missing_values_count = bitcoin_data.isnull().sum()
#print(missing_values_count[0:8])

#no empty values in this dataset 
#no need for drop or fill missing values

