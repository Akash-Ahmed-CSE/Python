import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Demo-for-Depression-Level.csv')
#print(df.head())
g = sns.countplot(x='If you answered "yes" to the previous question, did you take someone with you?', data=df, hue="Gender")
#print(df2)

#df3 = df2[[]]
#print(df3)
plt.show()
