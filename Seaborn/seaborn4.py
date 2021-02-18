import seaborn as sns
import matplotlib.pyplot as plt

sections = ['PC-A','PC-B','PC-D','PC-A','PC-F','PC-A','PC-D','PC-A','PC-F','PC-A',
            'PC-D','PC-A','PC-F','PC-A','PC-D','PC-A','PC-F','PC-A','PC-A','PC-B',
            'PC-D','PC-A','PC-F','PC-A',]
sns.countplot(x=sections)
plt.show()