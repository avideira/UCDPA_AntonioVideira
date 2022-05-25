from requests import Request, Session
import json
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np


url = 'https://api.coingecko.com/api/v3/exchanges'
parameters = {
}
headers = {
    'Accepts': 'application/json',
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
#Loading the JSON File to a Python Dictionary
#returns a nested dictionary
data = json.loads(response.text)

df = pd.DataFrame(data)

# Sort the rows of dataframe by trust score and volume traded
rslt_df = df.sort_values(by = ['trust_score_rank','trade_volume_24h_btc'], ascending=[True,False])
df_top = rslt_df.iloc[0:11,:] #top 10 exchanges

print(df_top)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(9, 7))

sns.set_color_codes("pastel")
sns.barplot(x="trade_volume_24h_btc", y="name", data=df_top,
            label="Volume", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 500000), ylabel="",
       xlabel="Volume Traded last 24h in the top 10 Exchanges")
sns.despine(left=True, bottom=True)

plt.subplots_adjust(left=0.21)

Volume_top_exchanges.png

plt.show()