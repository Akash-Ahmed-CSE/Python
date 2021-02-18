import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("tips.csv")
print(df.head(30))
sns.countplot(x="smoker",data=df,hue="sex",hue_order=["Male","Female"])
plt.show()