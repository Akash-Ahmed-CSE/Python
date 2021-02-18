import matplotlib.pyplot as plt
import pandas as pd
fig,ax = plt.subplots()

df = pd.read_csv("date.csv")

ax.plot(df["MONTH"],df["TEMP"],color="b",marker='o',linestyle='--')
ax.set_xlabel("Month")
ax.set_ylabel("Temp")
ax.set_title("month vs temp")

plt.show()