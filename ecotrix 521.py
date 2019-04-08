import pandas as pd
import statistics
import collections
import math
from functools import reduce

data_df=pd.read_excel("/Users/aneesh/Dropbox/SBU/SEMESTER 2/ECONOMetrics/project/temporary ecotrix data.xlsx")


full = []
common_country = []
for i in range(13, 27):
    list1 = []
    for index, row in data_df.iterrows():
        list1.append(row['Country_{0}'.format(i)])
    full.append(list1)

common_country = list(reduce(set.intersection, [set(item) for item in full]))
print(len(common_country))

data_df1 = pd.DataFrame()
for i in range(13, 27):
    data1 = []

    dic = collections.defaultdict()

    for index, row in data_df.iterrows():
        dic[row['Country_{0}'.format(i)]] = row['Pollution Index_{0}'.format(i)]

    common_data = []
    common_country1 = []
    for key, value in dic.items():
        if key in common_country:
            common_country1.append(key)
            common_data.append(value)

    data_df1['Country_{0}'.format(i)] = common_country1
    data_df1['Pollution Index_{0}'.format(i)] = common_data
    print(len(common_data))


data_df1.to_excel("/Users/aneesh/Dropbox/SBU/SEMESTER 2/ECONOMetrics/project/outputff_eco521.xlsx")

