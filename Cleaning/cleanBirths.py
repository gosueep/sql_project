import pandas as pd

df = pd.read_csv('NCHS_-_Teen_Birth_Rates_for_Age_Group_15-19_in_the_United_States_by_County.csv')
# print(df.columns)
df.drop(columns=['State FIPS Code','County FIPS Code'], inplace=True)
df.to_csv('../Birth_CleanCounty.csv', index=False)
