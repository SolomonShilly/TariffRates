import pandas as pd

data = pd.read_csv("HstDebt.csv")
data['Record Date'] = pd.to_datetime(data['Record Date'])

newData = pd.DataFrame()
newData['Year'] = data['Record Date'].dt.year
newData['Debt'] = data['Debt Outstanding Amount']
print(newData.head())

newData.to_csv('GovDebt.csv', index=False)