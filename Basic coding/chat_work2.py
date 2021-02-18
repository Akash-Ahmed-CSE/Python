import pandas as pd
from matplotlib.pyplot import pie, axis, show


df = pd.read_csv ('chart_work.csv')
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
sums = df.groupby(df["Product Name;"])["Number Of Bugs"].sum()
axis('equal')
pie(sums, labels=sums.index)
show()