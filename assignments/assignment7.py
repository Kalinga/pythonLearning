#!/usr/bin/python
# coding=UTF-8
import pandas as pd

import matplotlib.pyplot as plt

from  testmodule.styleformat import heading

heading("Module 7 Assignments: 1 [Add Change column]")
df = pd.read_csv('data/ARVIND.NS.csv')
print df.columns
df['Change'] = df.Open - df.Close
print df.Change
print df.columns
print df.head()
print df.Change.head()

heading("Module 7 Assignments: 2 Rolling Mean of Adj.Close")
print df["Adj Close"].mean()
df['rolling_avg'] = pd.rolling_mean(df["Adj Close"], 100)
#print df.loc[df.index, ["Adj Close", "rolling_avg"]]
#print df[["Adj Close", "rolling_avg"]] Other Syntax
print df.tail(20)
print df['Adj Close'].max()
print df[df["Adj Close"] == 245.4]
#df['rolling_avg'].plot()
#df['Adj Close'].plot()

'''f, (ax, ay) = plt.subplots(1, 2, sharey=True)
ax.plot(df['rolling_avg'])
ax.set_title('rolling_avg')
ay.plot(df['Adj Close'])
ay.set_title('Adj Close')
plt.show()'''

print df['Date'].values
print type(df['Date'][0])



#plt.plot(df['Date'].values, df['rolling_avg'].values, 'y-', label='rolling_avg')
#plt.plot(df['Adj Close'], 'r-', label='Adj Close')
#plt.legend(loc='upper right')
#plt.show()

heading("Module 7 Assignments: 3 matrix using scipy")
