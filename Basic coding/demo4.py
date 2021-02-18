import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv ('Demo-for-Depression-Level.csv')
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]

plt.title("All the tasks you have performed,\n are taking much more time than usual.")

sums = df.groupby(df["All the tasks you have performed, are taking much more time than usual."])["All the tasks you have performed, are taking much more time than usual."].count()




plt.pie(sums, labels=sums.index,autopct='%1.1f%%', colors=colors)

plt.show()


