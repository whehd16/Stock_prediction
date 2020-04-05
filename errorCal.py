import pandas as pd
import statistics
#error cal
kospiCSV0 = pd.read_csv('C:/stock/data/error/4/31/31ERR.csv')
for k in range(10):
    for i in range(len(kospiCSV0['error'+str(k)])):
        try:
            list = kospiCSV0['error'+str(k)][i].split(' ')
            value = []
            for j in range(len(list)):
                if list[j] != '':
                    value.append(list[j])
            kospiCSV0['error'+str(k)][i] = float(value[2])
        except:
            continue
        # print(kospiCSV0['error'][i])

    gaps = []
    gaps_data_abs = []
    gaps_data = []
    for i in range(len(kospiCSV0['error'+str(k)])):
        try:
            if i == 0:
                gaps.append(2)
                continue

            gap = kospiCSV0['error'+str(k)][i] - kospiCSV0['error'+str(k)][i-1]

            if gap > kospiCSV0['error' + str(k)][i-1] * 0.005:
                gaps.append(1)
            elif gap < -kospiCSV0['error' + str(k)][i-1] * 0.005:
                gaps.append(-1)
            else:
                gaps.append(0)

            # gaps_data.append(gap)
            # gaps_data_abs.append(abs(gap))
        except:
            continue
        # if gap == 0:
        #     print(i)
    # med = statistics.median(gaps_data_abs)

    # for i in range(len(gaps_data)):
    #     med = kospiCSV0['error' + str(k)][i-1] * 0.005
    #     if gaps_data[i] > med:
    #         gaps.append(1)
    #     elif gaps_data[i] < -med:
    #         gaps.append(-1)
    #     else:
    #         gaps.append(0)
    print(k)
    kospiCSV0['isUp'+str(k)] = gaps
    kospiCSV0.to_csv("C:/stock/data/error/4/31/31UD.csv")