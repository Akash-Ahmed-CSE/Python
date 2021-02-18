import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('masculinity.csv')
print(df.head(30))
#sns.set_context("talk")
sns.set_style("dark")
sns.set_palette("RdBu")
category_order=[ "No answer",
                 "not very",
                 "Not at all",
                 "Very",
                 "Somewhat"]
sns.catplot(x='how_masculine',data=df,kind="count",order=category_order)
plt.show()