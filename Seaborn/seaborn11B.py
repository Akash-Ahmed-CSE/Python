import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("air_df_mean.csv")
print(df.head(30))
sns.relplot(x="hour",y="NO_2_mean",data=df,kind="line",ci="sd") #ci=None will remove all gray part
plt.show()