from matplotlib import pyplot as pl
from matplotlib.pyplot import hist as hist_orig
from matplotlib.colors import LinearSegmentedColormap
pl.interactive(True)
from matplotlib import colors as mcolors
import numpy as np
from matplotlib.ticker import NullFormatter
from mpl_toolkits.mplot3d import Axes3D

pl.style.use('normal') # benson / normal / classic [normal is a custom one I made, classic is the builtin]

def hist(*args,**kwargs):
    kwargs['histtype'] = kwargs.pop('histtype','step')
    return hist_orig(*args,**kwargs)
pl.hist = hist

def share(axs, x=True, y=True, keep_labels=[0]):
    xlos,xhis = zip(*[ax.get_xlim() for ax in axs.ravel()])
    ylos,yhis = zip(*[ax.get_ylim() for ax in axs.ravel()])

    xlo = np.min(xlos)
    xhi = np.max(xhis)
    ylo = np.min(ylos)
    yhi = np.max(yhis)

    all_figs = []

    for idx,ax in enumerate(axs.ravel()):
        if x:
            ax.set_xlim([xlo,xhi])
            if not idx in keep_labels:
                ax.set_xticklabels([])
        if y:
            ax.set_ylim([ylo,yhi])
            if not idx in keep_labels:
                ax.set_yticklabels([])

        if ax.figure not in all_figs:
            all_figs.append(ax.figure)
    
    for fig in all_figs:
        fig.canvas.draw()

def ticf(both=None, x=None, y=None, ax=None, fig=None):
    # show only every n ticks

    if ax is not None:
        axs = [ax]
        fig = ax.figure
    elif ax is None:
        fig = fig or pl.gcf()
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

def despine(ax=None, which=['top','right']):
    if ax is None:
        ax = pl.gca()
    # spines
    if which == 'all':
        which = ['top','right','bottom','left']
    for w in which:
        ax.spines[w].set_visible(False)

def pretty(fig=None, ax=None, tickout=True, tickin=False, lims=False, xlim=None, ylim=None):
    if ax is not None:
        axs = [ax]
        fig = ax.figure
    elif ax is None:
        fig = fig or pl.gcf()
        axs = fig.get_axes()

    for ax in axs:

        # spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    
        # ticks
        if not tickin and not tickout:
            for tic in ax.xaxis.get_major_ticks():
                tic.tick1On = tic.tick2On = False
            for tic in ax.yaxis.get_major_ticks():
                tic.tick1On = tic.tick2On = False
            ax.tick_params(axis='both', which='both', bottom='off', top='off')

        elif tickin:
            ax.tick_params(axis='both', which='both', direction='in', bottom='on', top='off', left='on', right='off')
        elif tickout:
            ax.tick_params(axis='both', which='both', direction='out', bottom='on', top='off', left='on', right='off')

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

def nc():
    # named colours
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

    # Sort by hue, saturation, value and name.
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                    for name, color in colors.items())

    # Get the sorted color names.
    sorted_names = [name for hsv, name in by_hsv]

    n = len(sorted_names)
    ncols = 4
    nrows = int(np.ceil(1. * n / ncols))

    fig, ax = pl.subplots(figsize=(8, 5))

    X, Y = fig.get_dpi() * fig.get_size_inches()

    # row height
    h = Y / (nrows + 1)
    # col width
    w = X / ncols

    for i, name in enumerate(sorted_names):
        col = i % ncols
        row = int(i / ncols)
        y = Y - (row * h) - h

        xi_line = w * (col + 0.05)
        xf_line = w * (col + 0.25)
        xi_text = w * (col + 0.3)

        ax.text(xi_text, y, name, fontsize=(h * 0.8),
                horizontalalignment='left',
                verticalalignment='center')

        ax.hlines(
            y + h * 0.1, xi_line, xf_line, color=colors[name], linewidth=(h * 0.6))

    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    ax.set_axis_off()

    fig.subplots_adjust(left=0, right=1,
                        top=1, bottom=0,
                        hspace=0, wspace=0)

def cm():
    cmaps = [('Perceptually Uniform Sequential', [
                'viridis', 'plasma', 'inferno', 'magma']),
             ('Sequential', [
                'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
             ('Sequential (2)', [
                'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                'hot', 'afmhot', 'gist_heat', 'copper']),
             ('Diverging', [
                'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
             ('Qualitative', [
                'Pastel1', 'Pastel2', 'Paired', 'Accent',
                'Dark2', 'Set1', 'Set2', 'Set3',
                'tab10', 'tab20', 'tab20b', 'tab20c']),
             ('Miscellaneous', [
                'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
                'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]


    nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))


    def plot_color_gradients(cmap_category, cmap_list, nrows):
        fig, axes = pl.subplots(nrows=nrows)
        fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
        axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

        for ax, name in zip(axes, cmap_list):
            ax.imshow(gradient, aspect='auto', cmap=pl.get_cmap(name))
            pos = list(ax.get_position().bounds)
            x_text = pos[0] - 0.01
            y_text = pos[1] + pos[3]/2.
            fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

        # Turn off *all* ticks & spines, not just the ones with colormaps.
        for ax in axes:
            ax.set_axis_off()


    for cmap_category, cmap_list in cmaps:
        plot_color_gradients(cmap_category, cmap_list, nrows)

    pl.show()

def scatterhist(x, y, fig=None, bins=30, scatter_kw={}, hist_kw={}):
    if fig is None:
        fig = pl.figure()

    nullfmt = NullFormatter()

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    axScatter = fig.add_axes(rect_scatter)
    axHistx = fig.add_axes(rect_histx)
    axHisty = fig.add_axes(rect_histy)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # the scatter plot:
    axScatter.scatter(x, y, **scatter_kw)

    rangex = np.max(x) - np.min(x)
    minx = np.min(x) - rangex/20
    maxx = np.max(x) + rangex/20
    rangey = np.max(y) - np.min(y)
    miny = np.min(y) - rangey/20
    maxy = np.max(y) + rangey/20
    
    axScatter.set_xlim((minx,maxx))
    axScatter.set_ylim((miny,maxy))
    
    binwidth_x = rangex / bins
    binwidth_y = rangey / bins

    bins_x = np.arange(minx, maxx + binwidth_x, binwidth_x)
    bins_y = np.arange(miny, maxy + binwidth_y, binwidth_y)
    hist_kw['normed'] = hist_kw.pop('normed', True)
    axHistx.hist(x, bins=bins_x, **hist_kw)
    axHisty.hist(y, bins=bins_y, orientation='horizontal', **hist_kw)

    ylimx = axHistx.get_ylim()
    xlimy = axHisty.get_xlim()
    myx = np.max(ylimx)
    mxy = np.max(xlimy)
    maxx = np.max([myx,mxy])

    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())
    axHisty.set_xlim((0, maxx))
    axHistx.set_ylim((0, maxx))

    return axScatter,axHistx,axHisty


