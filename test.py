import pandas as pd

csv = pd.read_csv('../data/kospi_origin.csv')
print(csv.count()[0])