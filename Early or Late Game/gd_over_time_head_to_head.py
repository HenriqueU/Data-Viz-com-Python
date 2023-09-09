import pandas as pd
from matplotlib import pyplot as plt

index = ['GD@15', 'GD@20', 'GD@25', 'GD@30', 'GD@35']
loud_gd_vs_pain = {
    "Rodada 1": [-2145, -3860, -3946, -6673, '-'],
    "Rodada 10": [-641, -1982, 1660, 2331, 5895],
    "Playoffs UF - Jogo 1":[-898, -1163, -325, 290, -3160],
    "Playoffs UF - Jogo 2":[1949, 2878, 1992, 2883, '-'],
    "Playoffs UF - Jogo 3":[3833, 5644, 7422, 9845, '-']
}

pain_gd_vs_loud = {
    "Rodada 1": [2145, 3860, 3946, 6673, '-'],
    "Rodada 10": [641, 1982, -1660, -2331, -5895],
    "Playoffs UF - Jogo 1":[898, 1163, 325, -290, 3160],
    "Playoffs UF - Jogo 2":[-1949, -2878, -1992, -2883, '-'],
    "Playoffs UF - Jogo 3":[-3833, -5644, -7422, -9845, '-']
}

df_loud = pd.DataFrame(loud_gd_vs_pain, index=index)
df_loud['Média'] = df_loud.mean(axis=1, numeric_only=True)

df_pain = pd.DataFrame(pain_gd_vs_loud, index=index)
df_pain['Média'] = df_pain.mean(axis=1, numeric_only=True)

fig, ax = plt.subplots()
ax.plot()

game_time = ['15 min', '20 min', '25 min', '30 min', '35 min']
ax.plot(game_time, df_loud['Média'], marker='o', color='#6EE049', label='LLL')
ax.plot(game_time, df_pain['Média'], marker='o', color='#E04949', label='PNG')

for i, value in enumerate(df_loud['Média']):
    if i in (0, 3, 4):
        ax.annotate(round(value), (game_time[i], df_loud['Média'][i]), xytext=(game_time[i], df_loud['Média'][i] + 50))
    else:
        ax.annotate(round(value), (game_time[i], df_loud['Média'][i]), xytext=(game_time[i], df_loud['Média'][i] - 110))

for i, value in enumerate(df_pain['Média']):
    if i == 0:
        ax.annotate(round(value), (game_time[i], df_pain['Média'][i]), xytext=(game_time[i], df_pain['Média'][i] - 110))
    else: 
        ax.annotate(round(value), (game_time[i], df_pain['Média'][i]), xytext=(game_time[i], df_pain['Média'][i] + 50))

plt.title('Diferença de Ouro por tempo de partida - Confronto Direto')
plt.xlabel('Tempo de Partida')
plt.ylabel('Diferença de Ouro')
plt.legend(loc='lower right')
plt.tight_layout()
plt.grid()
plt.show()