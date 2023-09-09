import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#Data
LLL_img = [
    [plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Kaisa.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Poppy.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Xayah.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Alistar.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Renekton.png')],

    [plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Tristana.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Maokai.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Vi.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Jax.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Jayce.png')]
    ]

PNG_img = [
    [plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Ahri.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Gnar.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Sejuani.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Kaisa.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Maokai.png')],

    [plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Neeko.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Rell.png'), 
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Poppy.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Xayah.png'),
    plt.imread('CBLOL 2023 Split 2 Finals/Picks and Bans/img/Rakan.png')]
    ]

LLL_data = [
    {"Champion": ['K', 'P', 'X', 'A', 'R'],
    "Qtd of picks": [10, 10, 8, 6, 6]},
    {"Champion": ['T', 'M', 'V', 'J', 'J'],
    "Qtd of picks": [17, 13, 8, 7, 7]}
    ]

PNG_data = [
    {"Champion": ['Ahri', 'Gnar', 'Sejuani', 'Kaisa', 'Maokai'],
    "Qtd of picks": [11, 9, 7, 7, 7]},
    {"Champion": ['Neeko', 'Rell', 'Poppy', 'Xayah', 'Rakan'],
    "Qtd of picks": [14, 11, 11, 8, 7]}
    ]

df1 = pd.DataFrame(LLL_data[0]['Qtd of picks'], LLL_data[0]['Champion'])
df2 = pd.DataFrame(LLL_data[1]['Qtd of picks'], LLL_data[1]['Champion'])
df3 = pd.DataFrame(PNG_data[0]['Qtd of picks'], PNG_data[0]['Champion'])
df4 = pd.DataFrame(PNG_data[1]['Qtd of picks'], PNG_data[1]['Champion'])

#Plotting
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
fig2, (ax3, ax4) = plt.subplots(nrows=1, ncols=2)

plot1 = df1.plot.bar(ax=ax1, legend=False, color='#6EE049', rot=0)
plot2 = df2.plot.bar(ax=ax2, legend=False, color='#6EE049', rot=0)
plot3 = df3.plot.bar(ax=ax3, legend=False, color='#E04949', rot=0)
plot4 = df4.plot.bar(ax=ax4, legend=False, color='#E04949', rot=0)

axes = [[ax1, ax2], [ax3, ax4]]
l, p = 0, 0

for lll_img_list, png_img_list in zip(LLL_img, PNG_img):
    for i,im in enumerate(lll_img_list):
        tick_labels = axes[0][l].xaxis.get_ticklabels()
        ib = OffsetImage(im, zoom=.3)
        ib.image.axes = axes[0][l]
        ab = AnnotationBbox(ib,
                        tick_labels[i].get_position(),
                        frameon=False,
                        box_alignment=(0.5, 1.2)
                        )
        axes[0][l].add_artist(ab)
    l += 1

    for i,im in enumerate(png_img_list):
        tick_labels = axes[1][p].xaxis.get_ticklabels()
        ib = OffsetImage(im, zoom=.3)
        ib.image.axes = axes[1][p]
        ab = AnnotationBbox(ib,
                        tick_labels[i].get_position(),
                        frameon=False,
                        box_alignment=(0.5, 1.2)
                        )
        axes[1][p].add_artist(ab)
    p += 1

l, p = 0, 0
plots = [[plot1, plot2], [plot3, plot4]]
for lll_plot, png_plot in zip(plots[0], plots[1]):
    lll_plot.bar_label(lll_plot.containers[0], labels=LLL_data[l]['Qtd of picks'])
    l += 1

    png_plot.bar_label(png_plot.containers[0], labels=PNG_data[p]['Qtd of picks'])
    p += 1

plot1.set_title('Campeões mais escolhidos (LLL)')
plot2.set_title('Campeões mais banidos (LLL)')
plot3.set_title('Campeões mais escolhidos (PNG)')
plot4.set_title('Campeões mais banidos (PNG)')

fig.tight_layout()
fig2.tight_layout()
plt.show()