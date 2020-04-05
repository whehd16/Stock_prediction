#년도(행)을 분리하는 코드.
import pandas as pd
#2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018
#2년 단위로 끊기
##4년 단위 22
for i in range(5):
    kospiCSV = pd.read_csv('../data/' + str(2007+2*i) + '-' + str(2010+2*i) + '.csv', thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(2007 + 2 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2008 + 2 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/4/" + str(2007 + 2 * i) + "-" + str(2008 + 2 * i)+".csv", index = False)

#4년 단위 31
for i in range(5):
    kospiCSV = pd.read_csv('../data/' + str(2007+2*i) + '-' + str(2010+2*i) + '.csv', thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(2007 + 2 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2008 + 2 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2009 + 2 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/4/" + str(2007 + 2*i) + "-" + str(2009 + 2*i)+".csv", index = False)

#6년 단위 33
for i in range(3):
    kospiCSV = pd.read_csv('../data/' + str(2007+3*i) + '-' + str(2012+3*i) + '.csv', thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(2007 + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2008 + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2009 + 3 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/6/" + str(2007 + 3*i) + "-" + str(2009 + 3*i)+".csv", index = False)

#6년 단위 33
for i in range(3):
    kospiCSV = pd.read_csv('../data/' + str(2007+3*i) + '-' + str(2012+3*i) + '.csv', thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(2007 + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2008 + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2009 + 3 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2010 + 3 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/6/" + str(2007 + 3*i) + "-" + str(2010 + 3*i)+".csv", index = False)

#8년 단위 44
for i in range(2):
    kospiCSV = pd.read_csv('../data/' + str(2007+4*i) + '-' + str(2014+4*i) + '.csv', thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(2007 + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2008 + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2009 + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2010 + 4 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/8/" + str(2007 + 4 * i) + "-" + str(2010 + 4 * i) + ".csv", index = False)

#8년 단위 53
for i in range(2):
    kospiCSV = pd.read_csv('../data/' + str(2007+4*i) + '-' + str(2014+4*i) + '.csv', thousands=',')
    while kospiCSV.columns[0] != 'Date':
        kospiCSV = kospiCSV.drop(kospiCSV.columns[0], axis=1)
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(2007 + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2008 + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2009 + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2010 + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(2011 + 4 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("../data/8/" + str(2007 + 4 * i) + "-" + str(2011 + 4 * i) + ".csv", index = False)