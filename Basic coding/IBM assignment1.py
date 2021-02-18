import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

#mpl.style.use('ggplot') # optional: for ggplot-like style

df_surv = pd.read_csv('Topic_Survey_Assignment.csv',index_col = 0)
df_surv.sort_values(by='Very interested', ascending=False, inplace=True)

# Change this line to plot percentages instead of absolute values
ax = (df_surv.div(df_surv.sum(1), axis=0)).plot(kind='bar', figsize=(20, 8), width = 0.8, color = ['#5cb85c','#5bc0de','#d9534f'])
plt.legend(labels=df_surv.columns,fontsize= 14)
plt.title("Percentage of Respondents' Interest in Data Science Areas",fontsize= 16)

plt.xticks(fontsize=14)
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.yticks([])

# Add this loop to add the annotations
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.annotate('{:.0%}'.format(height), (x, y + height + 0.01))

plt.show()
