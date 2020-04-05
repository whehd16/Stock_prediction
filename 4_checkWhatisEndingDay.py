import pandas as pd

def showWhatisEndingDay(file):
    csv = pd.read_csv(file)
    print(csv['Date'][csv.count()[0]-1])
    return csv['Date'][csv.count()[0]-1]
    # print(file, csv['Date'][csv.count()[0]-1])

showWhatisEndingDay('../data/4/2007-2008.csv')
showWhatisEndingDay('../data/4/2009-2010.csv')
showWhatisEndingDay('../data/4/2011-2012.csv')
showWhatisEndingDay('../data/4/2013-2014.csv')
showWhatisEndingDay('../data/4/2015-2016.csv')
print()
showWhatisEndingDay('../data/4/2007-2009.csv')
showWhatisEndingDay('../data/4/2009-2011.csv')
showWhatisEndingDay('../data/4/2011-2013.csv')
showWhatisEndingDay('../data/4/2013-2015.csv')
showWhatisEndingDay('../data/4/2015-2017.csv')
print()
showWhatisEndingDay('../data/6/2007-2009.csv')
showWhatisEndingDay('../data/6/2010-2012.csv')
showWhatisEndingDay('../data/6/2013-2015.csv')
print()
showWhatisEndingDay('../data/6/2007-2010.csv')
showWhatisEndingDay('../data/6/2010-2013.csv')
showWhatisEndingDay('../data/6/2013-2016.csv')
print()
showWhatisEndingDay('../data/8/2007-2010.csv')
showWhatisEndingDay('../data/8/2011-2014.csv')
print()
showWhatisEndingDay('../data/8/2007-2011.csv')
showWhatisEndingDay('../data/8/2011-2015.csv')

############################################여기까지가 train test 섞이지 않게 확인하는거