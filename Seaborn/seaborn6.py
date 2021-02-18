import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("tips.csv")
print(df.head(30))

hue_colors = {"Yes": "black","No": "red"}

sns.scatterplot(x="total_bill",y="tip",
                data=df,hue="smoker" ,
                palette=hue_colors)
plt.show()