import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('masculinity.csv')
print(df.head())

sns.countplot(x='how_masculine',data=df)

plt.show()