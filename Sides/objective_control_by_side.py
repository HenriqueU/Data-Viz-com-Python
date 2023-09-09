import pandas as pd
from matplotlib import pyplot as plt

#Data
LLL_dragons = [(3/2), (10/5)]
LLL_heralds = [(3/2), (3/5)]
LLL_barons = [(3/2), (7/5)]

PNG_dragons = [(12/5), (16/6)]
PNG_heralds = [(5/5), (3/6)]
PNG_barons = [(6/5), (8/6)]

data_loud = {
    "Blue Side": [(3/2), (3/2), (3/2)],
    "Red Side": [(10/5), (3/5), (7/5)]
}
df_loud = pd.DataFrame(data_loud, index=['Dragões', 'Arautos', 'Barões'])
df_loud = df_loud.round(1)

data_pain = {
    "Blue Side": [(12/5), (5/5), (6/5)],
    "Red Side": [(16/6), (3/6), (8/6)]
}
df_pain = pd.DataFrame(data_pain, index=['Dragões', 'Arautos', 'Barões'])
df_pain = df_pain.round(1)

#Plotting
fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

plot1 = df_loud.plot.bar(ax=ax1, color=['#405685', '#a80000'], rot=0)
plot2 = df_pain.plot.bar(ax=ax2, color=['#405685', '#a80000'], rot=0)

for value1, value2 in zip(plot1.containers, plot2.containers):
    plot1.bar_label(value1, padding=5)
    plot2.bar_label(value2, padding=5)

plot1.set_title('Média de Objetivos Por Jogo (LLL)')
plot1.set_ylim(0, 3.25)
plot2.set_title('Média de Objetivos Por Jogo (PNG)')
plot2.set_ylim(0, 3.25)
plt.tight_layout()
plt.show()