import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os
import datetime
# import xgboost as xgb
from sklearn import model_selection, preprocessing


def filtering(path):
    train_set = pd.read_csv(path)
    for f in train_set.columns:
        if train_set[f].dtype=='object':
            lbl = preprocessing.LabelEncoder()
            lbl.fit(list(train_set[f].values))
            train_set[f] = lbl.transform(list(train_set[f].values))
    dtype_df = train_set.dtypes.reset_index()
    dtype_df.columns=["Count", "Column Type"]
    dtype_df.groupby("Column Type").aggregate('count').reset_index()
    corrmat = train_set.drop(['Date'], axis = 1).corr(method='pearson', min_periods=1)
    # corrmat = np.abs(corrmat)
    sns.set(context="paper", font = "monospace")

    remain_num = 264
    corr_target = corrmat['KOSPI_Now'].reset_index()[:-2]
    corr_target.columns = ['feature', 'abs_corr']
    corr_target = corr_target.sort_values(by = 'abs_corr', ascending = True)[:remain_num].loc[corr_target['abs_corr'] >= 0.2]
    train_set_1=pd.read_csv(path)
    print(len(train_set_1.columns))
    remain_columns_list = []
    for a, b in corr_target.values:
        remain_columns_list.append(a)
    # print(remain_columns_list)

    for column in train_set_1.columns:
        if column == 'Date':
            continue
        elif column not in remain_columns_list:
                train_set_1 = train_set_1.drop(column, axis = 1)

    print(len(train_set_1.columns))
    print()
    train_set_1.to_csv(path, index = False)

filtering('../data/4/2007-2008.csv')
filtering('../data/4/2009-2010.csv')
filtering('../data/4/2011-2012.csv')
filtering('../data/4/2013-2014.csv')
filtering('../data/4/2015-2016.csv')

filtering('../data/4/2007-2009.csv')
filtering('../data/4/2009-2011.csv')
filtering('../data/4/2011-2013.csv')
filtering('../data/4/2013-2015.csv')
filtering('../data/4/2015-2017.csv')

filtering('../data/6/2007-2009.csv')
filtering('../data/6/2010-2012.csv')
filtering('../data/6/2013-2015.csv')

filtering('../data/6/2007-2010.csv')
filtering('../data/6/2010-2013.csv')
filtering('../data/6/2013-2016.csv')

filtering('../data/8/2007-2010.csv')
filtering('../data/8/2011-2014.csv')

filtering('../data/8/2007-2011.csv')
filtering('../data/8/2011-2015.csv')


