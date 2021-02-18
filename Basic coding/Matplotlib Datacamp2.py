import matplotlib.pyplot as plt
import pandas as pd
fig,ax = plt.subplots(3,2)
df = pd.read_csv("date.csv")

ax[0,0].plot(df["MONTH"],df["TEMP"])
ax[0,1].plot(df["MONTH"],df["TEMP"])
ax[1,0].plot(df["MONTH"],df["TEMP"])
ax[1,1].plot(df["MONTH"],df["TEMP"])
ax[2,0].plot(df["MONTH"],df["TEMP"])
ax[2,1].plot(df["MONTH"],df["TEMP"])

plt.show()