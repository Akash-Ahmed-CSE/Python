import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("tips.csv")
print(df.head(30))
sns.catplot(x="smokers",y="total_boll",data=df,kind="point")

plt.show()








