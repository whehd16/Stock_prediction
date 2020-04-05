import pandas as pd
import statistics

# error cal
kospiCSV0 = pd.read_csv('C:/stock/data/4/kospi_original_2007_2010.csv')
kospiCSV1 = pd.read_csv('C:/stock/data/4/kospi_original_2009_2012.csv')
kospiCSV2 = pd.read_csv('C:/stock/data/4/kospi_original_2011_2014.csv')
kospiCSV3 = pd.read_csv('C:/stock/data/4/kospi_original_2013_2016.csv')
kospiCSV4 = pd.read_csv('C:/stock/data/4/kospi_original_2015_2018.csv')

kospiCSV5 = pd.read_csv('C:/stock/data/6/kospi_original_2007_2012.csv')
kospiCSV6 = pd.read_csv('C:/stock/data/6/kospi_original_2010_2015.csv')
kospiCSV7 = pd.read_csv('C:/stock/data/6/kospi_original_2013_2018.csv')

kospiCSV8 = pd.read_csv('C:/stock/data/8/kospi_original_2007_2014.csv')
kospiCSV9 = pd.read_csv('C:/stock/data/8/kospi_original_2011_2018.csv')

kospiCSV0.to_csv('C:/stock/data/4/kospi_original_2007_2010.csv')
kospiCSV1.to_csv('C:/stock/data/4/kospi_original_2009_2012.csv')
kospiCSV2.to_csv('C:/stock/data/4/kospi_original_2011_2014.csv')
kospiCSV3.to_csv('C:/stock/data/4/kospi_original_2013_2016.csv')
kospiCSV4.to_csv('C:/stock/data/4/kospi_original_2015_2018.csv')

kospiCSV5.to_csv('C:/stock/data/6/kospi_original_2007_2012.csv')
kospiCSV6.to_csv('C:/stock/data/6/kospi_original_2010_2015.csv')
kospiCSV7.to_csv('C:/stock/data/6/kospi_original_2013_2018.csv')

kospiCSV8.to_csv('C:/stock/data/8/kospi_original_2007_2014.csv')
kospiCSV9.to_csv('C:/stock/data/8/kospi_original_2011_2018.csv')