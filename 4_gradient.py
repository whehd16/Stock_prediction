import pandas as pd
import sys
csv = pd.read_csv('../data/mergedData/코스피병합본_interpolated.csv')
length = csv.count()[0]

for ins in range(csv.count()[0]):
    if len(csv.loc[ins]['Date'].split(str(2019))) == 2:
        csv = csv.drop([ins])
    else:
        continue

for i in range(csv.count()[0]-2, -1, -1):
    for j in range(1, len(csv.columns)):
        if csv[csv.columns[j]][i] == 0:
            continue
        csv[csv.columns[j]][i+1] =100*(csv[csv.columns[j]][i+1] - csv[csv.columns[j]][i]) / csv[csv.columns[j]][i]

for column in csv.columns:
    csv[column] = csv[column].interpolate()

csv.to_csv('../data/mergedData/코스피병합본_interpolated_1.csv', index = False)