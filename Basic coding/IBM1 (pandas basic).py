import pandas as pd
import folium
df = pd.read_excel(r'F:\python programs\project2\Canada.xlsx',
                       skiprows=range(20),
                       skipfooter=2)
#print(df.head())
#print(df.head())
#print(df.tail())
#print(df.info())
#print(df.columns.values)

#print(type(df.columns))
#print(type(df.index))

df.columns.tolist()
df.index.tolist()

#print (type(df.columns.tolist()))
#print (type(df.index.tolist()))

#print(df.shape)





