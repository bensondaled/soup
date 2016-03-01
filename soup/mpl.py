from matplotlib import pyplot as pl
pl.interactive(True)
import numpy as np
mpl_plot = pl.plot
mpl_scatter = pl.scatter

pl.style.use('benson')

def plot(*args,**kwargs):
    ret = mpl_plot(*args,**kwargs)
    pretty()
    return ret
def scatter(*args,**kwargs):
    ret = mpl_scatter(*args,**kwargs)
    pretty()
    return ret
pl.plot = plot
pl.scatter = scatter

def ticf(both=None, x=None, y=None, ax=None):
    # show only every n ticks

    if ax is not None:
        axs = [ax]
        fig = ax.figure
    elif ax is None:
        fig = pl.gcf()
        axs = fig.get_axes()

    if both:
        x,y = both,both

    for ax in axs:
        
        if x: #it works fine without these if's, except in the case where certain axes in the fig had adjustments already made on one axis and you don't want to mess with them
            for label in ax.xaxis.get_ticklabels():
                label.set_visible(False)
            for label in ax.xaxis.get_ticklabels()[::x]:
                label.set_visible(True)

        if y:
            for label in ax.yaxis.get_ticklabels():
                label.set_visible(False)
            for label in ax.yaxis.get_ticklabels()[::y]:
                label.set_visible(True)

    fig.canvas.draw()

def pretty(fig=None, ax=None, tickin=True, lims=False, xlim=None, ylim=None):
    if ax:
        fig = ax.figure
    elif fig is None:
        fig = pl.gcf()
    if ax is None:
        ax = pl.gca()
    
    # ticks
    if not tickin:
        for tic in ax.xaxis.get_major_ticks():
            tic.tick1On = tic.tick2On = False
        for tic in ax.yaxis.get_major_ticks():
            tic.tick1On = tic.tick2On = False
        ax.tick_params(axis='both', which='both', bottom='off', top='off')

    elif tickin:
        ax.tick_params(axis='both', which='both', direction='in', bottom='on', top='off', left='on', right='off')

    # borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # lims
    if lims or xlim or ylim:
        lines=ax.get_lines()
        x,y = zip(*[[l.get_xdata(),l.get_ydata()] for l in lines])
        x,y = map(np.concatenate, [x,y])
        if xlim:
            ax.set_xlim(xlim)
        else:
            rang = np.max(x)-np.min(x)
            pad = 0.1*rang
            ax.set_xlim([np.min(x)-pad,np.max(x)+pad])
        if ylim:

            ax.set_ylim(ylim)
        else:
            rang = np.max(y)-np.min(y)
            pad = 0.1*rang
            ax.set_ylim([np.min(y)-pad,np.max(y)+pad])

    pl.margins(0.05)

    fig.canvas.draw()
