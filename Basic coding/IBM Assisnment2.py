import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd


df_incidents = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset read into a pandas dataframe!')

print(df_incidents.shape)
print(df_incidents.head())

print(df_incidents['PdDistrict'].value_counts())
print(df_incidents.groupby(['PdDistrict']).groups.keys())

df_crime_nh = df_incidents.groupby('PdDistrict')['PdId'].count().reset_index()
print(df_crime_nh)

df_crime_nh.rename(columns={'PdDistrict':'Neighborhood', 'PdId':'Count'}, inplace=True)
print(df_crime_nh)


