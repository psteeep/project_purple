import matplotlib.pyplot as plt
import seaborn as sns  # Optional for data visualization
import pandas as pd
from datetime import datetime as dt
from pandas import isna  # Import isna function from pandas

# Assuming the data file path
data_path = 'C:/git/project_purple/data_loader/data sets/BTC-Daily.csv'

data = pd.read_csv(data_path)

print(data.head())


def calculate_time(timestamp):
    """
    This function turns the timestamp to the date, handling missing values.
    :param timestamp: given timestamp
    :return: date according to given timestamp (or None for missing values)
    """
    if isna(timestamp):  # Check if timestamp is missing (using isna)
        return None
    else:
        return dt.fromtimestamp(timestamp / 1000)


open_date = []
for i in data["open"]:
    open_date.append(calculate_time(i))
data["open"] = open_date

close_date = []
for i in data["close"]:
    close_date.append(calculate_time(i))
data["close"] = close_date


plt.figure(figsize=(16, 8))
plt.title("Bitcoin Price History")
plt.plot(data["date"], data["close"])
plt.xlabel("Time", fontsize=14,)
plt.ylabel("USDT", fontsize=14)
plt.show()