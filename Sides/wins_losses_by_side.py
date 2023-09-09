import pandas as pd
from matplotlib import pyplot as plt

#Modelling Data
data = {
    'Vitórias Blue Side': [2, 2],
    'Derrotas Blue Side': [0, 3],
    'Vitórias Red Side': [4, 4],
    'Derrotas Red Side': [1, 2]
    }

df = pd.DataFrame(data, index=['LLL', 'PNG'])

#Plotting
ax = df.plot.bar(color=['#405685', '#70b0e0', '#a80000', '#eb5757'])

for value in ax.containers:
    ax.bar_label(value, padding=5)

plt.title('Vitórias e Derrotas por Side (Patch 13.15)')
plt.ylabel('Número de vitórias e derrotas')
plt.xticks(rotation=0, horizontalalignment='center')
plt.ylim(0, 4.25)
plt.tight_layout()
plt.show()