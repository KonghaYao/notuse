import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./1.csv', dtype={
    "year": 'str',
    'month': 'str'
})
df.drop_duplicates(inplace=True)
df['scores'].fillna(df.scores.mean(), inplace=True)

df['date'] = pd.to_datetime(df['year']+'/'+df['month']+'/1')

df.set_index('date', inplace=True)
df.resample('4M').median().plot()
plt.show()
print(df.head())
