import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("tips.csv")

print(df.head(30))
sns.catplot(x="time",y="total_bill",data=df,kind="box",order=["Dinner","Lunch"])
sns.catplot(x="time",y="total_bill",data=df,kind="box",sym="",whis=[0,100])
plt.show()