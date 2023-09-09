import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Data
LLL_players = ['Robo', 'Croc', 'tinOwns', 'Route', 'Ceos']
LLL_gs = [21.1, 18.9, 22, 24.4, 12.6]
LLL_dmg_share = [22.3, 13.4, 29.1, 29, 6.2]

PNG_players = ['Wizer', 'CarioK', 'dyNquedo', 'Bvoy', 'ProDelta']
PNG_gs = [21.5, 17.3, 22, 25.8, 13.5]
PNG_dmg_share = [22.1, 12.1, 25.7, 35.2, 4.9]

#Plotting
fig, ax = plt.subplots()

ax.scatter(LLL_gs, LLL_dmg_share,
            edgecolors='black', s=100, linewidths=1, alpha=0.75, color='#6EE049', label='LLL')

ax.scatter(PNG_gs, PNG_dmg_share,
            edgecolors='black', s=100, linewidths=1, alpha=0.75, color='#E04949', label='PNG')

ax.set_axisbelow(True)

for index, player in enumerate(LLL_players):
    ax.annotate(player, (LLL_gs[index], LLL_dmg_share[index]), xytext=(LLL_gs[index], LLL_dmg_share[index] + 0.5))

for index, player in enumerate(PNG_players):
    ax.annotate(player, (PNG_gs[index], PNG_dmg_share[index]), xytext=(PNG_gs[index], PNG_dmg_share[index] - 1))

plt.title('DMG% / GS% por Rota')
plt.xlabel('Gold Share (%)')
plt.ylabel('Damage Share (%)')
plt.legend(loc='lower right')
plt.tight_layout()
plt.grid()
plt.show()