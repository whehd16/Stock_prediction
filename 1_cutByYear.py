#년도(행)을 분리하는 코드.
import pandas as pd
file = '../data/mergedData/코스피병합본.csv'
file = '../data/mergedData/코스피병합본_interpolated.csv'
file = '../data/mergedData/코스피병합본_interpolated_1.csv'
# file = '../data/kospiFiltered.csv'
#2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018
#2년 단위로 끊기
for i in range(5):
    kospiCSV = pd.read_csv(file, thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(int('2007') + 2 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2008') + 2 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2009') + 2 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2010') + 2 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/" + str(2007 + 2*i) + "-" + str(2010 + 2*i)+".csv",index = False)

for i in range(3):
    kospiCSV = pd.read_csv(file, thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(int('2007') + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2008') + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2009') + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2010') + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2011') + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2012') + 3 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/" + str(2007 + 3*i) + "-" + str(2012 + 3*i)+".csv", index = False)

for i in range(2):
    kospiCSV = pd.read_csv(file, thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(int('2007') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2008') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2009') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2010') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2011') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2012') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2013') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2014') + 4 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/" + str(2007 + 4 * i) + "-" + str(2014 + 4 * i) + ".csv", index = False)