import pandas as pd
from matplotlib import pyplot as plt

index = ['GD@15', 'GD@20', 'GD@25', 'GD@30', 'GD@35']
loud_gd_over_time = {
    "Rodada 1": [-2145, -3860, -3946, -6673, '-'],
    "Rodada 2": [-569, 1125, 1161, -3981, '-'],
    "Rodada 3": [-446, -2238, -3853, -658, '-'],
    "Rodada 4": [46, -2631, -381, 3942, '-'],
    "Rodada 5": [493, 1476, 2071, 9170, '-'],
    "Rodada 6": [-3159, -1283, -131, 1600, '-'],
    "Rodada 7": [867, 3317, 3678, 9656, '-'],
    "Rodada 8": [3478, 3563, -7, 2558, '-'],
    "Rodada 9": [708, 467, 7852, 13338, '-'],
    "Rodada 10": [-641, -1982, 1660, 2331, 5895],
    "Rodada 11": [-3131, -3614, -7912, -13425, '-'],
    "Rodada 12": [1693, 1147, 2724, 4853, -5358],
    "Rodada 13": [2993, 7835, 13473, '-', '-'],
    "Rodada 14": [4242, 5108, 8006, '-', '-'],
    "Rodada 15": [2118, 4981, 10313, '-', '-'],
    "Rodada 16": [-44, -1208, 5615, '-', '-'],
    "Rodada 17": [1456, 5687, 11965, '-', '-'],
    "Rodada 18": [-1181, -2857, 1434, 1603, 9315],
    "Playoffs R1 - Jogo 1":[-1012, -2901, -8229, -7645, '-'],
    "Playoffs R1 - Jogo 2":[535, 2844, 10974, '-', '-'],
    "Playoffs R1 - Jogo 3":[-1071, -2382, 1082, 4035, '-'],
    "Playoffs R1 - Jogo 4":[-2622, -1133, 1944, 10831, '-'],
    "Playoffs UF - Jogo 1":[-898, -1163, -325, 290, -3160],
    "Playoffs UF - Jogo 2":[1949, 2878, 1992, 2883, '-'],
    "Playoffs UF - Jogo 3":[3833, 5644, 7422, 9845, '-']
}
pain_gd_over_time = {
    "Rodada 1": [2145, 3860, 3946, 6673, '-'],
    "Rodada 2": [-2679, -1394, -1577, -7617, '-'],
    "Rodada 3": [-212, 1291, 5957, '-', '-'],
    "Rodada 4": [104, -1043, 8079, '-', '-'],
    "Rodada 5": [422, 1838, 585, 3782, -1826],
    "Rodada 6": [-806, -1180, 3235, 5704, '-'],
    "Rodada 7": [-1355, -647, 470, -2096, 1127],
    "Rodada 8": [817, 3917, 12158, '-', '-'],
    "Rodada 9": [3554, 4028, 10725, '-', '-'],
    "Rodada 10": [641, 1982, -1660, -2331, -5895],
    "Rodada 11": [4768, 8478, 13628, '-', '-'],
    "Rodada 12": [3705, 7011, 15009, '-', '-'],
    "Rodada 13": [2164, 4572, 11075, '-', '-'],
    "Rodada 14": [6408, 10183, 13556, '-', '-'],
    "Rodada 15": [-1478, -2356, -3955, -7831, -4549],
    "Rodada 16": [4057, 3774, 3550, 7262, 3674],
    "Rodada 17": [1043, 5821, 12854, '-', '-'],
    "Rodada 18": [3261, 4059, 1562, 3294, 4281],
    "Playoffs R1 - Jogo 1":[471, 1544, 3120, 4167, 4724],
    "Playoffs R1 - Jogo 2":[792, 674, -2265, -2760, -2016],
    "Playoffs R1 - Jogo 3":[592, -413, -2774, 64, 907],
    "Playoffs UF - Jogo 1":[898, 1163, 325, -290, 3160],
    "Playoffs UF - Jogo 2":[-1949, -2878, -1992, -2883, '-'],
    "Playoffs UF - Jogo 3":[-3833, -5644, -7422, -9845, '-'],
    "Playoffs LF - Jogo 1":[2417, 4358, 9883, '-', '-'],
    "Playoffs LF - Jogo 2":[817, -194, -4303, -6345, -2662],
    "Playoffs LF - Jogo 3":[-2956, -3649, -10344, -11065, '-'],
    "Playoffs LF - Jogo 4":[562, -117, 770, -1962, -3114],
    "Playoffs LF - Jogo 5":[2266, 3093, 2901, 3891, '-'],
}

df_loud = pd.DataFrame(loud_gd_over_time, index=index)
df_loud['Média'] = df_loud.mean(axis=1, numeric_only=True)

df_pain = pd.DataFrame(pain_gd_over_time, index=index)
df_pain['Média'] = df_pain.mean(axis=1, numeric_only=True)

fig, ax = plt.subplots()
game_time = ['15 min', '20 min', '25 min', '30 min', '35 min']
ax.plot(game_time, df_loud['Média'], marker='o', color='#6EE049', label='LLL')
ax.plot(game_time, df_pain['Média'], marker='o', color='#E04949', label='PNG')

for i, value in enumerate(df_loud['Média']):
    if i in (0, 3):
        ax.annotate(round(value), (game_time[i], df_loud['Média'][i]), xytext=(game_time[i], df_loud['Média'][i] + 60))
    else:
        ax.annotate(round(value), (game_time[i], df_loud['Média'][i]), xytext=(game_time[i], df_loud['Média'][i] - 125))

for i, value in enumerate(df_pain['Média']):
    ax.annotate(round(value), (game_time[i], df_pain['Média'][i]), xytext=(game_time[i], df_pain['Média'][i] + 60))

plt.title('Diferença de Ouro por tempo de partida')
plt.xlabel('Tempo de Partida')
plt.ylabel('Diferença de Ouro')
plt.legend(loc='lower right')
plt.tight_layout()
plt.grid()
plt.show()