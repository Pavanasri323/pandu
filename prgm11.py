import pandas as pd

df = pd.read_csv('online-retail.csv')
df.head()

print(df)

df['LinePrice'] = df['Quality'] * df['UnitPrice']
df.head()

print(df)
