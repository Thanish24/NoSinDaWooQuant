import matplotlib.pyplot as plt
import pandas as pd

# Create a pandas DataFrame from the data
crudeOilDf = pd.read_csv('NoSinDaWooQuant/CLF_data.csv')

deltaDf = pd.read_csv('NoSinDaWooQuant/DAL_data.csv')

# Convert 'Date' column to datetime type
crudeOilDf['Date'] = pd.to_datetime(crudeOilDf['Date'])
deltaDf['Date'] = pd.to_datetime(deltaDf['Date'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(crudeOilDf['Date'], crudeOilDf['Close'], marker='o', linestyle='-', label='crude oil')
plt.plot(deltaDf['Date'], deltaDf['Close'], marker='o', linestyle='-', label='delta')
plt.title('Crude Oil and Delta Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()

plt.show()