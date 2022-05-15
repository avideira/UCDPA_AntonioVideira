import pandas as pd

#index_col = 0 will set the first column up as the row index
bitcoin_data = pd.read_csv('Data/coin_Bitcoin.csv', index_col=0)

print(bitcoin_data)