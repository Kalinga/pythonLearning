import pandas as pd
from pandas.core.frame import DataFrame
from pylab import *

from testmodule.styleformat import clear

series = pd.Series (list("abcde"))
print series

series = pd.Series (list("abcde"), index=[100, 200, 300, 400, 500])
print series

print series[500]
print series[400]
print series[300]
print series[200]
print series[100]

# print series[0] KeyError

series = pd.Series (list("abcde"), index=['a', 'e', 'a', 'c', 'a'])
print series
print series['a']
print series['a'][1:]

df = pd.read_csv("data/emp.csv")
print df.head(5)
print df.dtypes.index
print df.columns.values



import pandas as pd
import numpy as np

# Creating Series

s = pd.Series(list('abcdf'))
s = pd.Series([1,2,3,4], index=['*', '**', '***', '****'])

s[['*', '**']]       # Fetching multiples values

s = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd']) # specify values for each index

s = pd.Series(range(5), index=('a', 'b', 'c', 'd', 'e'))  # passing range

s = pd.Series(range(5), index=('a', 'b', 'c', 'b', 'e'))  # redundant indices

s = pd.Series({'a': 'Python', 'b': 'Hadoop', 'c': 'java'}) # Directly passing dictionary

s = pd.Series({'a': 'Python', 'b': 'Hadoop', 'c': 'java'}, index=list('abbc')) # passing redundant indices

s = pd.Series({'a': 'Python', 'b': 'Hadoop', 'c': 'java'}, index=list('sbbc')) # passing unknown indices

#Key: The column name and list is the values for the column
data = {'a': ['Python'], 'b': ['Hadoop'], 'c': ['java']}

print s*3  # arithmetic on series

# Creating DataFrame
# dataFrame = pd.DataFrame(data = d, index=index)
dataFrame = pd.DataFrame(data)
print dataFrame

data = {'Country':['US','US','INDIA','INDIA'],
         'year':[2012,2013,2012,2013],
         'Population':[20,27,30,35]
         }
dataFrame = pd.DataFrame(data)
print dataFrame

data = {'US':{2011:30,2013:35},
        'INDIA':{2012:20,2013:27,2014:28}
        }
dataFrame = pd.DataFrame(data)
print dataFrame

clear()

d = {'one' : pd.Series([1,2,3], index=list('abc')),
     'two' : pd.Series([2,4,6, 8], index=list('abcd'))}

df = pd.DataFrame(d)
print df

col_one = df['one']  # accessing values
print type(col_one)
print col_one

df['new_col'] = list('1234')
df['new_col'] = df['two'] * 2 # adding new column

# Something more interesting in series

clear()

obj = pd.Series(['python', 'hadoop', 'java'], index=[0,2,4])
print obj

print obj.reindex(range(5))

print obj.reindex(range(5), fill_value='empty')

print obj.reindex(range(5), method='ffill') # use of ffill
print obj.reindex(range(5), method='bfill') # use of bfill

clear()

# Some Interesting operations on DataFrames
d = {'one' : pd.Series([1,2,3], index=list('abc')),
     'two' : pd.Series([2,4,6,8], index=list('abcd'))}

df = pd.DataFrame(d)
print df
print df.one
print df.two

df['new_col'] = df['two'] * 2
print df.new_col

print df.sum()

print df.mean()

print df.describe()

clear()

# Loading Data in Pandas

data = pd.read_csv('data/emp.csv')  #Data created is a DataFrame

#print data
print len(data)
print data.columns
#data.head(7)
#data.tail(10)
#print data.irow(1)
#print data[data.Id == 12646303]
print data[data.Town == 'Lincoln']
print data.describe()

#Plotting Graph
data = pd.read_csv('data/emp.csv')
print "Total no# "
print len(data)

towns = data['Town'].unique()
town_count =  data['Town'].value_counts()
print type(town_count)
print town_count
top_five = town_count[:5]
top_five.plot(kind='barh', rot=30)
#show()

specific_town = data[data['Town'] == 'Lincoln']
print (specific_town)

clear()
# Merging Tables
import numpy as np
df1 = pd.DataFrame(dict(id=range(5), age=np.random.randint(18, 30, size=5)))
print df1

df2 = pd.DataFrame(dict(id=range(4), runs=np.random.randint(0, 100, size=4)))
print df2

print pd.merge(df1, df2)

clear()
# Usage of axis: By default axis is 0, meant along rows
df = pd.DataFrame([[1,2], [3,4]],columns=["col1", "col2"],index =['A', 'B'])
print df
print df.mean()
print df.mean(axis=1)

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df
print df[:3]
print df.loc[dates[0]]
print df.loc[dates[1:5],["C", "D"]]
print df.iloc[3:5, 0:2]
#Scalar value Fast access
print df.iat[1,1]

clear("Boolean Indexing")
#Boolean Indexing
print df[(df.A > 0)]
print df[df > 0]

print df.apply(np.square)
print df.apply(np.cumsum) #cumulative sum across rows
print df.apply(np.cumsum, axis=1) #cumulative sum across col

clear("Using lambdas")
print df
print df.apply(lambda x:np.cumsum(x),  axis=1) #cumulative sum across col
print df.apply(lambda x:np.cumsum(x),  axis=0) #cumulative sum across row
print df.apply(lambda x: x.max() - x.min(), axis=1) #across cols
print df.apply(lambda x: x.max() - x.min()) #across rows

