import pandas as pd
import math
import sys
#다시할때는 할 필요없음
def deleteNan(file):
    csv = pd.read_csv(file)
    for i in range(csv.count()[0] - 1, 0, -1):
        for j in range(1,len(csv.columns)):
            if math.isnan(csv.loc[i][j]):
                break
            if j == len(csv.columns) - 1:
                end = csv.count()[0]
                for k in range(end-1, i, -1):
                    csv = csv.drop([k])
                csv.to_csv(file, index = False)
                print(csv['Date'][i])
                return

deleteNan('../data/4/2007-2008.csv')
deleteNan('../data/4/2009-2010.csv')
deleteNan('../data/4/2011-2012.csv')
deleteNan('../data/4/2013-2014.csv')
deleteNan('../data/4/2015-2016.csv')

deleteNan('../data/4/2007-2009.csv')
deleteNan('../data/4/2009-2011.csv')
deleteNan('../data/4/2011-2013.csv')
deleteNan('../data/4/2013-2015.csv')
deleteNan('../data/4/2015-2017.csv')

deleteNan('../data/6/2007-2009.csv')
deleteNan('../data/6/2010-2012.csv')
deleteNan('../data/6/2013-2015.csv')

deleteNan('../data/6/2007-2010.csv')
deleteNan('../data/6/2010-2013.csv')
deleteNan('../data/6/2013-2016.csv')

deleteNan('../data/8/2007-2010.csv')
deleteNan('../data/8/2011-2014.csv')

deleteNan('../data/8/2007-2011.csv')
deleteNan('../data/8/2011-2015.csv')
