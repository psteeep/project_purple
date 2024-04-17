import matplotlib.pyplot as plt
import pandas as pd

data_path = 'C:/git/project_purple/data_loader/data sets/BTC-Daily.csv'

df = pd.read_csv(data_path)

df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(16, 8))
plt.plot(df['date'], df['close'], color='blue', linestyle='-')
plt.title('BTC/USD Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('USD')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
