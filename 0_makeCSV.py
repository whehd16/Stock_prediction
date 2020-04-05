import os
import pandas as pd
import sys
#Read file from dir
#각각 다운로드한 csv 파일을 하나로 합침
file_list = os.listdir("../data/stockData/")
#기준이 될 csv 파일
kospiCSV = pd.read_csv('../data/stockData/코스피지수 내역.csv', thousands=',')
kospiCSV = kospiCSV.drop('오픈', axis=1)
kospiCSV = kospiCSV.drop('고가', axis=1)
kospiCSV = kospiCSV.drop('저가', axis=1)
kospiCSV = kospiCSV.drop('변동 %', axis=1)
kospiCSV = kospiCSV.drop('거래량', axis=1)

print(kospiCSV)
for file in file_list:
    if file == '코스피지수 내역.csv':
        continue
    try:
        csv = pd.read_csv("../data/stockData/" + file, thousands=',')
        csv = csv.drop('변동 %', axis=1)
        if len(csv.columns) == 6:
            csv = csv.drop('거래량', axis=1)

        for i in range(1, len(csv.columns)):
            target = csv.columns[i]
            if target == "현재가":
                target = "Now"
            elif target == "오픈":
                target = "Open"
            elif target == "고가":
                target = "High"
            elif target == "저가":
                target = "Low"
            csv.rename(columns={csv.columns[i]: file.split(' ')[0] + '_' + target}, inplace=True)
        kospiCSV = pd.merge(kospiCSV, csv, on='날짜', how='left')

    except:
        print(file)
        continue

for i in range(len(kospiCSV['날짜'])):
    kospiCSV['날짜'][i] = kospiCSV['날짜'][i].split(' ')[0][:-1] + '-' +\
                        kospiCSV['날짜'][i].split(' ')[1][:-1] + '-' +\
                        kospiCSV['날짜'][i].split(' ')[2][:-1]

kospiCSV.rename(columns={kospiCSV.columns[0]: 'Date'}, inplace=True)
kospiCSV.rename(columns={kospiCSV.columns[1]: 'KOSPI_Now'}, inplace=True)
# kospiCSV.rename(columns={kospiCSV.columns[2]: 'KOSPI_Open'}, inplace=True)
# kospiCSV.rename(columns={kospiCSV.columns[3]: 'KOSPI_High'}, inplace=True)
# kospiCSV.rename(columns={kospiCSV.columns[4]: 'KOSPI_Low'}, inplace=True)

index = len(kospiCSV)-1

#2007년 1월 9일 부터 사용하기 위함
while True:
    if kospiCSV['Date'][index] == "2007-01-09":
        break
    kospiCSV = kospiCSV.drop([index])
    index -= 1

# i = 0
# while True:
#     if kospiCSV['Date'][i] == "2018-12-28":
#         break
#     kospiCSV = kospiCSV.drop([i])
#     i += 1

#역순으로
kospiCSV = kospiCSV.reindex(index=kospiCSV.index[::-1])
kospiCSV.to_csv("../data/mergedData/코스피병합본.csv", index=False)

# for i in range(kospiCSV.count()[0] - 1, 0, -1):
#     for j in range(len(kospiCSV.columns)):
#         if kospiCSV.loc[i][j] == 'nan':
#             break
#         if j == len(kospiCSV.columns) - 1:
#             end = kospiCSV.count()[0]
#             for k in range(end-1, i, -1):
#                 kospiCSV = kospiCSV.drop([k])
#             sys.exit(0)