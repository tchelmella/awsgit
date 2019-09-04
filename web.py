# Import pandas library
import pandas as pd

# Read the csv file using pandas.
df = pd.read_csv(
    'https://vincentarelbundock.github.io/Rdatasets/'
    'csv/datasets/OrchardSprays.csv')

# Write the csv file.
df.to_csv(r'/home/ubuntu/pandas/webscraping/webdata.csv',sep='\t',index=False)

# print the dataframe.
print(df)
