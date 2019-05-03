#"""
#Matplotlib Animation Example

from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import batman
from .planetplotlib import create_dome_plot

from .animatetools import get_writer

def make_transit_movie(t0=0,per=6.266,rp=0.15,a=6.85,inc=90,ecc=0,w=0, ylim=[0.95, 1.01], filename='basic_animation.gif'):
    ''' Here is how to use the function.

    Parameters
    ---------------------
    t0 : float
    	#time of inferior conjunction
    per: float
    	#orbital period
    rp: float
    	#planet radius (in units of stellar radii)
    a: float
    	 #semi-major axis (in units of stellar radii)
    inc:float
    	#orbital inclination (in degrees)
    ecc:float
    	#eccentricity
    w:float
    	#longitude of periastron (in degrees)
    '''

    params = batman.TransitParams()       #object to store transit parameters
    params.t0 = t0                      #time of inferior conjunction
    params.per = per                       #orbital period
    params.rp = rp                     #planet radius (in units of stellar radii)
    params.a = a                       #semi-major axis (in units of stellar radii)
    params.inc = inc                      #orbital inclination (in degrees)
    params.ecc = ecc                       #eccentricity
    params.w = w                       #longitude of periastron (in degrees)
    params.limb_dark = "nonlinear"        #limb darkening model
    params.u = [0.5, 0.1, 0.1, -0.1]      #limb darkening coefficients [u1, u2, u3, u4

    dt = 0.002
    t = np.arange(-per/2,per/2,0.002)

    m = batman.TransitModel(params, t)    #initializes model
    y = m.light_curve(params)
    # First set up the figure, the axis, and the plot element we want to animate
    fig, ax = create_dome_plot()

    line, = ax.plot(t, y, lw=2)
    ball, = plt.plot(t[0],y[0],marker= ".", markersize= 30)
    #t = np.arange(input(),input(),0.001)

    # set the x and y limits of the plot
    plt.xlim(np.min(t), np.max(t))
    plt.ylim(ylim[0], ylim[1])

    #flux = m.light_curve(params)                    #calculates light curve

    timestep = 0.02
    skip = np.maximum(int(timestep/dt), 1)
    N = int(len(t)/skip)

    # animation function.  This is called sequentially
    def animate(i):
        print(i, '/', N, end='\r')
        ball.set_data(t[i*skip], y[i*skip])
        return ball,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate,
                                   frames=N, interval=20, blit=True)   # To make transit go all the way around add 100 frames.previously 20.

    # save the animation as an gif. This code previously saved this animation as mp4. Which required ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    #extra_args=['-vcodec', 'libx264']
    # gif instead of mp4 for this laptop
    writer = get_writer(filename)
    print("Saving movie to {}".format(filename))

    anim.save(filename, writer= writer )
