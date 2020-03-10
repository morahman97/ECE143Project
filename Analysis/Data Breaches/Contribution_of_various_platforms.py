#Contribution of various platforms to data breaches
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
# %matplotlib inline

def autopct_generator(limit):
    """Remove percent on small slices."""
    def inner_autopct(pct):
        return ('%.2f%%' % pct) if pct > limit else ''
    return inner_autopct

def generate_plot():
    data = pd.read_excel('cleaned_social_media.xlsx')
    labels = data['Entity']
    sizes = data['records lost']
    NUM_COLORS = len(sizes)

    fig1, ax1 = plt.subplots(figsize=(18,10))

    theme = plt.get_cmap('bwr')
    ax1.set_prop_cycle(color=[theme(
        1. * i / NUM_COLORS) for i in range(NUM_COLORS)])

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 1.3, box.height])

    _, _, autotexts = ax1.pie(
        sizes, autopct=autopct_generator(1.5),explode = (0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0), startangle=90)
    for autotext in autotexts:
        autotext.set_weight('bold')
    ax1.axis('equal')
    total = sum(sizes)
    plt.legend(
        loc='upper left',
        labels=['%s, %1.1f%%' % (
            l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
        prop={'size': 13},
        bbox_to_anchor=(0.0, 1),
        bbox_transform=fig1.transFigure
    )
    #defining fonts
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'heavy',
            'size': 28,
            }

    plt.title('Contribution of various platforms to data breaches',fontdict=font)