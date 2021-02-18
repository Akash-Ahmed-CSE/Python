import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("tips.csv")
print(df.head())
sns.relplot(x="total_bill",y="tip",data=df,kind="scatter",col="day",col_wrap=3,
            col_order=["Thu","Sun","Mon","wed","Fri","Tue","Sat"])
plt.show()