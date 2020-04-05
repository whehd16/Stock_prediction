import os
#csv 파일 시계열 데이터 선형 보간하는 데이터.
import pandas as pd

def interpolate(file):
    kospiCSV = pd.read_csv(file+'.csv', thousands=',')
    for column in kospiCSV.columns:
        kospiCSV[column] = kospiCSV[column].interpolate()
    kospiCSV.to_csv(file+'_interpolated.csv', index = False)
    return

def interpolate_origin(file):
    kospiCSV = pd.read_csv('../data/'+ file, thousands=',')
    for column in kospiCSV.columns:
        kospiCSV[column] = kospiCSV[column].interpolate()
    kospiCSV.to_csv('../data/original_interpolated/' + file, index=False)
    return

interpolate('../data/mergedData/코스피병합본')

#다시 1번으로 가서 file 이름 바꾸기