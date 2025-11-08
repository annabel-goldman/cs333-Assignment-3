import pandas as pd

df = pd.read_csv('data.csv')

df = df.drop(['End_Lat', 'End_Lng'], axis=1)

new_df = df.dropna() #Removes all data with an empty cell

new_df.to_csv('cleandata.csv', index=False)

print('num rows after cleaning', len(new_df))