import math
import pandas as pd

# csv = pd.read_csv('../data/mergedData/코스피병합본.csv')
# for ins in range(csv.count()[0]):
#     for col in csv.columns:
#         if col == 'Date':
#             continue
#         if math.isnan(csv[col][ins]):
#             print('1')

def howMany(year):
    csv = pd.read_csv('../data/mergedData/코스피병합본.csv')

    for ins in range(csv.count()[0]):
        if len(csv.loc[ins]['Date'].split(str(year))) != 2:
            csv = csv.drop([ins])
        else:
            continue

    csv.to_csv('../data/temp/a.csv')
    csv = pd.read_csv('../data/temp/a.csv')

    for ins in range(csv.count()[0]):
        for col in csv.columns:
            if col == 'Date':
                continue
            if math.isnan(csv[col][ins]):
                print(csv['Date'][ins])
                break
howMany(2009)
print()
howMany(2010)
print()
howMany(2011)
print()
howMany(2012)
print()
howMany(2013)
print()
howMany(2014)
print()
howMany(2015)
print()
howMany(2016)
print()
howMany(2017)
print()
howMany(2018)