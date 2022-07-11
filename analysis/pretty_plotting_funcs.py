import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm 
from faceted import faceted as fc
import numpy as np


def make_pretty_plot(ax, xmin=-10, xmax=10, ymin=-10, ymax=10, xscalelog=False, yscalelog=False,
                    xlabel='', ylabel=''):
    ax.tick_params(axis='both', direction='in', length=3, top=True, right=True, 
                   left=True, bottom=True)
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)
#     ax.yaxis.set_ticks_position('left')
#     ax.xaxis.set_ticks_position('bottom')
    plt.xticks(fontsize='small')
    plt.yticks(fontsize='small')
    ax.set_xlim([xmin,xmax])
    if xscalelog==True:
        ax.set_xscale('log')
    ax.set_ylim([ymin,ymax])
    if yscalelog==True:
        ax.set_yscale('log')
    ax.set_xlabel(xlabel, fontsize='small')
    ax.set_ylabel(ylabel, fontsize='small')
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(0.4)
    ax.tick_params(width=0.4)
    ax.tick_params(axis='both', direction='in', length=1.5, top=True, right=True, left=True,
                   bottom=True, which='minor', width=0.4)



    return ax

# Ukrainian Color Scheme
from matplotlib.colors import ListedColormap

N = 256
blue = np.ones((N,4))
blue[:,0] = np.linspace(0/256, 1, N)
blue[:, 1] = np.linspace(87/256, 1, N)
blue[:, 2] = np.linspace(184/256, 1, N)
Blues = ListedColormap(blue)

yellow = np.ones((N,4))
yellow[:,0] = np.linspace(254/256, 1, N)
yellow[:, 1] = np.linspace(221/256, 1, N)
yellow[:, 2] = np.linspace(0/256, 1, N)
Yellows = ListedColormap(yellow)