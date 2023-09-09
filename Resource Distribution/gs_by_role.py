import pandas as pd
from matplotlib import pyplot as plt

#Modelling Data
data = {
    'LLL': [21.1, 18.9, 22, 24.4, 12.6],
    'PNG': [21.5, 17.3, 22, 25.8, 13.5]
    }

df = pd.DataFrame(data, index=['TOP', 'JG', 'MID', 'BOT', 'SUP'])

#Plotting
ax = df.plot.barh(color=['#6EE049', '#E04949'])

for value in ax.containers:
    ax.bar_label(value, padding=5)

ax.invert_yaxis()

plt.title('Gold Share por Rota')
plt.xlabel('Gold Share (%)')
plt.tight_layout()
plt.show()