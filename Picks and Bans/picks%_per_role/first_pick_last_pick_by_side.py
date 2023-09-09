import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Data
index = [['B1', 'B2', 'B3', 'B4', 'B5'], 
         ['R1', 'R2', 'R3', 'R4', 'R5']]

LLL_blue_side = {
    'TOP': [0, 1, 3, 3, 4],
    'JG': [1, 3, 1, 5, 1],
    'MID': [2, 1, 1, 2, 5],
    'BOT': [5, 5, 1, 0, 0],
    'SUP': [3, 1, 5, 1, 1]
}
df1 = pd.DataFrame(LLL_blue_side, index=index[0])

LLL_red_side = {
    'TOP': [3, 0, 2, 4, 5],
    'JG': [4, 5, 0, 1, 4],
    'MID': [2, 2, 2, 4, 4],
    'BOT': [3, 6, 4, 1, 0],
    'SUP': [2, 1, 6, 4, 1]
}
df2 = pd.DataFrame(LLL_red_side, index=index[1])

PNG_blue_side = {
    'TOP': [2, 1, 2, 1, 8],
    'JG': [4, 5, 2, 3, 0],
    'MID': [1, 4, 3, 5, 1],
    'BOT': [5, 2, 4, 3, 'zero'],
    'SUP': [2, 2, 3, 2, 5]
}
df3 = pd.DataFrame(PNG_blue_side, index=index[0])

PNG_red_side = {
    'TOP': [0, 0, 5, 3, 7],
    'JG': [3, 9, 1, 2, 0],
    'MID': [2, 2, 6, 4, 1],
    'BOT': [8, 2, 2, 2, 1],
    'SUP': [2, 2, 1, 4, 6]
}
df4 = pd.DataFrame(PNG_red_side, index=index[1])

#Plotting
fig1, ((ax1, ax2, ax3, ax4, ax5), 
       (ax6, ax7, ax8, ax9, ax10)) = plt.subplots(nrows=2, ncols=5)

fig2, ((ax11, ax12, ax13, ax14, ax15), 
       (ax16, ax17, ax18, ax19, ax20)) = plt.subplots(nrows=2, ncols=5)

lll_df_list = [df1, df2]
png_df_list = [df3, df4]
lll_axes = [[ax1, ax2, ax3, ax4, ax5], [ax6, ax7, ax8, ax9, ax10]]
png_axes = [[ax11, ax12, ax13, ax14, ax15], [ax16, ax17, ax18, ax19, ax20]]
labels = ['TOP', 'JG', 'MID', 'BOT', 'SUP']
colors = ['#2980b9', '#27ae60', '#f1c40f', '#c70039', '#9b59b6']

for ax_list, index_list, df in zip(lll_axes, index, lll_df_list):
    for ax, i in zip(ax_list, index_list):
        value_list = []
        for value in df.loc[i]:
            if value == 0:
                index_of_zero = pd.Index(df.loc[i]).get_loc(value)
                del labels[index_of_zero]
                del colors[index_of_zero]
            else:
                value_list.append(value)
        
        ax.pie(value_list,
                labels=labels,
                autopct='%1.1f%%',
                colors=colors,
                wedgeprops={'edgecolor': 'black'},
                textprops={'fontsize': 7})
        ax.set_title(i[0] + 'P' + i[1])
        labels = ['TOP', 'JG', 'MID', 'BOT', 'SUP']
        colors = ['#2980b9', '#27ae60', '#f1c40f', '#c70039', '#9b59b6']

for ax_list, index_list, df in zip(png_axes, index, png_df_list):
    for ax, i in zip(ax_list, index_list):
        value_list = []
        for value in df.loc[i]:
            if value == 0 or value == 'zero':
                index_of_zero = pd.Index(df.loc[i]).get_loc(value)
                del labels[index_of_zero]
                del colors[index_of_zero]
            else:
                value_list.append(value)
        ax.pie(value_list,
                labels=labels,
                autopct='%1.1f%%',
                colors=colors, 
                wedgeprops={'edgecolor': 'black'},
                textprops={'fontsize': 7})
        ax.set_title(i[0] + 'P' + i[1])
        labels = ['TOP', 'JG', 'MID', 'BOT', 'SUP']
        colors = ['#2980b9', '#27ae60', '#f1c40f', '#c70039', '#9b59b6']

fig1.suptitle('% de Picks de cada Role (LLL)', fontsize=18)
fig2.suptitle('% de Picks de cada Role (PNG)', fontsize=18)
plt.tight_layout()
plt.show()