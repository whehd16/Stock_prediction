import pandas as pd
import statistics
#중앙값 사용하기 위함

kospiCSV0 = pd.read_csv('C:/stock/data/kospi_origin.csv')
# kospiCSV0 = kospiCSV0.dropna()
columnsList = []
for i in range(2,len(kospiCSV0.columns)):
    kospiCSV0 = kospiCSV0.drop(kospiCSV0.columns[2], axis=1)

# kospiCSV0.drop([],axis=1)
def avg(list):
    average = sum(list) / len(list)
    return average

up = 0
down = 0
none = 0
gaps = []
gaps_data = []
# print(len(kospiCSV0['KOSPI_Now']))
for i in range(len(kospiCSV0['KOSPI_Now'])):
    if i == 0:
        gaps.append(2)
        continue

    gap = kospiCSV0['KOSPI_Now'][i] - kospiCSV0['KOSPI_Now'][i-1]
    gaps_data.append(abs(gap))
    # if gap == 0:
    #     print(i)

    if gap > kospiCSV0['KOSPI_Now'][i-1] * 0.005:
        gaps.append(1)
        up += 1
    elif gap < -kospiCSV0['KOSPI_Now'][i-1] * 0.005:
        gaps.append(-1)
        down += 1
    else:
        gaps.append(0)
        none += 1

kospiCSV0['isUp'] = gaps
# print(kospiCSV0.columns[2])

kospiCSV0.to_csv("C:/stock/data/updown.csv")

#중앙값으로 오르내림 판단함.
print(avg(gaps_data))
print(min(gaps_data))
print(max(gaps_data))

print(statistics.median(gaps_data))
print()
print(up)
print(down)
print(none)
