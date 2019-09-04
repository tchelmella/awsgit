# Import pandas library
import pandas as pd

# Read the csv file using pandas.
df = pd.read_csv(
    'https://vincentarelbundock.github.io/Rdatasets/'
    'csv/datasets/OrchardSprays.csv')

# Write the csv file.
df.to_csv(r'C:/Users/slmsh/Documents/GitHub/awsgit/webdata1.csv',sep='\t',index=False)

# print the dataframe.
print(sorted(list(df.columns)))
