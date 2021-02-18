import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
tips = pd.read_csv("tips.csv")
print(tips.head())
sns.relplot(x="total_bill",y="tip",data=tips,kind="scatter",size="size",hue="size")

plt.show()