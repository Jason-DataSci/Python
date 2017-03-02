import pandas as pd

# Series and DataFrame

# Reading a csv into Pandas.
df = pd.read_csv('/Users/zhengyichen/Downloads/uk_rain_2014.csv', header=0)
# Getting first x rows.
df.head(5)

# Getting last x rows.
df.tail(5)

# Change column labels
df.columns = ['water_year','rain_octsep', 'outflow_octsep',
            'rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']

# Finding out how many rows dataset has.
len(df)

# Limit output to 3 decimal places.
pd.options.display.float_format = '{:,.3f}'.format
# Finding out basic statistical information on your dataset.
df.describe()

# Getting a column by label
df['rain_octsep']

# 命名列标签的时候不用空格、破折号之类的符号，这样我们就可以像访问对象属性一样访问数据集的列——只用一个点号
# Getting a column by label using .
df.rain_octsep

# Creating a series of booleans based on a conditional
df.rain_octsep < 1000 # Or df['rain_octsep] < 1000

# Using a series of booleans to filter
df[df.rain_octsep < 1000]

# Filtering by multiple conditionals
df[(df.rain_octsep < 1000) & (df.outflow_octsep < 4000)]
# Can't use the keyword 'and'

# Filtering by string methods
df[df.water_year.str.startswith('199')]

# Getting a row via a numerical index
df.iloc[30].unstack

# Setting a new index from an existing column
df = df.set_index(['water_year'])
df.head(5)
# 如果你想设置多个索引，只需要在列表中加入列的名字即可

# Getting a row via a label-based index
df.loc['2000/01']

# Getting a row via a label-based or numerical index
df.ix['1999/00'] # Label based with numerical index fallback *Not recommended

# 对 dataframe 调用 sort_index 方法进行排序
df.sort_index(ascending=False).head(5)
#inplace=True to apple the sorting in place

# 当你将一列设置为索引的时候，它就不再是数据的一部分了。如果你想将索引恢复为数据，调用 set_index 相反的方法 reset_index 即可
# Returning an index to data
df = df.reset_index('water_year')
df.head(5)

# Applying a function to a column
def base_year(year):
    base_year = year[:4]
    # base_year= pd.to_datetime(base_year).year
    return base_year

# apply和applymap可以对数据集中的一列数据或整个数据集进行应用函数
df['year'] = df.water_year.apply(base_year)
df.head(5)

#Manipulating structure (groupby, unstack, pivot)
# Grouby
df.groupby(df.year // 10 *10).max() #there're some problems with "// 10 *10".

# Grouping by multiple columns
decade_rain = df.groupby([df.year, df.rain_octsep])[['outflow_octsep',                                                              'outflow_decfeb', 'outflow_junaug']].mean().head(5)
decade_rain

# Unstacking
decade_rain.unstack(1)
p = decade_rain.unstack(1)
p.stack()

# Create a new dataframe containing entries which
# has rain_octsep values of greater than 1250
high_rain = df[df.rain_octsep > 1250]
high_rain

# 轴旋转其实就是我们之前已经看到的那些操作的一个集合。首先，它会设置一个新的索引（set_index()），然后对索引排序（sort_index()），最后调用 unstack 。以上的步骤合在一起就是 pivot 。

#Pivoting
#does set_index, sort_index and unstack in a row
high_rain.pivot('year', 'rain_octsep')[['outflow_octsep', 'outflow_decfeb', 'outflow_junaug']].fillna('')

# Merging two datasets together
rain_jpn = pd.read_csv('jpn_rain.csv')
rain_jpn.columns = ['year', 'jpn_rainfall']

uk_jpn_rain = df.merge(rain_jpn, on='year')
uk_jpn_rain.head(5)

# Using pandas to quickly plot graphs
uk_jpn_rain.plot(x='year', y=['rain_octsep', 'jpn_rainfall'])

# Saving your data to a csv
df.to_csv('uk_rain.csv')
