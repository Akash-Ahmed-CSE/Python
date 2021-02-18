import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_csv('countries.csv')

print(population.head(13))

sns.relplot('year','population',data=population)
plt.show()