import pandas as pd


data = pd.read_csv('AllBirdsv4.csv')
data['amount_x_2'] = data['amount']*2
data.to_csv('AllBirdsv4_2.csv')
