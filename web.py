import pandas as pd
df = pd.read_csv(
    'https://vincentarelbundock.github.io/Rdatasets/'
    'csv/datasets/OrchardSprays.csv')

df.to_csv(r'/home/ubuntu/pandas/webscraping/webdata.csv',sep='\t',index=False)
print(df)
