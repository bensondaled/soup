import pylab as pl

def pretty():
    fig = pl.gcf()
    ax = pl.gca()
    
    # ticks
    pl.tick_params(axis='x', which='both', bottom='off', top='off')
    pl.tick_params(axis='y', which='both', bottom='off', top='off')

    # borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.canvas.draw()
