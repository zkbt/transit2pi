'''
This is a small set of tools that extends matplotlib to be a bit better
for making plots that look nice in a planetarium dome.
'''

import matplotlib.pyplot as plt
import numpy as np

def create_dome_plot(dpi=100, hideticks=True):
    '''
    This function creates a matplotlib figure that
    has a dark background and that is stretched out
    so it will span a full 360x10 degree strip on
    the dome.
    Parameters
    ----------
    dpi : int
        The number of dots per "inch".
        By default, a figure is 36x1 inches in
        size, so dpi=100 means you will create
        an image with 3600x100 pixels.
    hideticks : bool
        Should we hide the ticks and all the
        x and y labels?
    Returns
    -------
    ax : matplotlib.axes object
        This is a matplotlib axes, into which
        data can be plotted. By default, this function
        will set the current axes to this one, so
        "plt.plot", "plt.xlim" (...) commands will
        apply to it. You could also use "ax.plot",
        "ax.set_xlim", (...) to interact directly
        with the ax.
    '''

    # switch to a dark background for matplotlib
    plt.style.use('dark_background')
    
    # make room for x and y labels, unless we're hiding the ticks
    if hideticks:
        left = 0
        bottom = 0
    else:
        left = 0.01
        bottom = 0.1

    fi, ax = plt.subplots(1, 1, # create a 1x1 grid of ax objects,
                          figsize=(36,1), # make the figure really long
                          dpi=dpi, # set the dots per inch
                          gridspec_kw=dict(left=left, # set the borders
                                           right=1,
                                           bottom=bottom,
                                           top=1))

    # set current axes to this new ax
    plt.sca(ax)

    # get rid of the ticks and labels, if we want to hide ticks
    if hideticks:
        plt.axis('off')

    # return both the figure and the axes for this dome plot
    return fi, ax

if __name__ == '__main__':
    # code inside '__main__' will not be run if someone *imports* this module
    # the __main__ block runs only if this script is run on its own

    # create a space to plot into
    domefig, domeax = create_dome_plot()

    # plot a sine curve in our new dome plot
    x = np.linspace(0, 2*np.pi)
    plt.plot(x, np.sin(x))
    plt.xlim(0, 2*np.pi)
    plt.show()
