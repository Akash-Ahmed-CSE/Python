import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("Demo-for-Depression-Level.csv")
print(df.head())
sns.set_style("dark")
#sns.set_palette("RdBu")




sns.relplot(x="Age" , y="You have been feeling very fatigued." , hue="Gender" ,data=df, size="Age")







#plt.xticks(rotation=90)
plt.show()
















#sns.catplot(x="Age",data=df,kind='scatterplot',hue="Gender")

#sns.catplot(x="Age",y="All the tasks you have performed, are taking much more time than usual.",data=df,kind='bar',hue="Gender")

#product_labels = ["Completely agree","Neutral","Somewhat agree","Somewhat disagree"]