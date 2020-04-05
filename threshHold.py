import pandas as pd
#양 끝의 중간 +-1%가 임계값.
#열고 하나하나 인덱스 마다 임계값 안에 있으면 나두고 없으면 None 으로

def cut(year, CSV, interCSV):
    for index in CSV.columns:
        if index == 'Date':
            continue
        for time in range(3):
            nonList = []
            var = [0.02, 0.015, 0.01]
            for num in range(4, len(CSV[index])-6):
                if abs(CSV[index][num] - CSV[index][num-1]) > CSV[index][num] * var[time]:
                    # print(abs(CSV[index][num] - CSV[index][num-1]))
                    # print(CSV[index][num] * 0.005)
                    # print('------------------------')
                # if abs(CSV[index][num] - interCSV[index][num]) > delta:
                    # CSV[index][num] = None
                    nonList.append(num)
            for num in range(len(nonList)):
                for i in range(0,2):
                    CSV[index][nonList[num] + i] = None
                    CSV[index][nonList[num] - i] = None
            print(nonList)
            CSV[index] = CSV[index].interpolate(method='polynomial', order=3)

        # delta = interCSV[index][len(interCSV[index])//2] * 0.01
        # for num in range(1, len(CSV[index] - 1)):
        #     if abs(CSV[index][num] - interCSV[index][num]) > delta:
        #         CSV[index][num] = None
        # CSV[index] = CSV[index].interpolate(method='polynomial', order=2)
        # CSV.to_csv('./cut/test'+str(year)+'.csv')

        CSV.to_csv('./data/' + str(year)+'.csv')
        print('-------------------------------')

def cutOtherFeature(CSV):
    for i in range(1,len(CSV.columns)):
        CSV = CSV.drop(CSV.columns[1], axis=1)
    return CSV

for i in range(2007, 2019):
    df = pd.read_csv('../data/mergedData/코스피병합본.csv')


# kokkokd