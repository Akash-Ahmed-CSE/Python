import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ('chart_work.csv')

product_data = df["Product Name;"]
bug_data = df["Number Of Bugs"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]

plt.pie(bug_data , labels=product_data , colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.show()


