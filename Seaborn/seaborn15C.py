import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('tips.csv')
print(df.head(30))
sns.catplot(x="day",y="total_bill",data=df,kind="bar",ci=None)
plt.show()
