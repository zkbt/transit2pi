# Tests the code from test_360movie but adds in Kepler curves.
#An attempt to run a ball on the full plot
#Maybe try to write a class that has two functions

import make2pitransit_2 as m2t
import planetplotlib as ppl
import henrietta as hsl
import numpy as np
from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive
import matplotlib.pyplot as plt
from matplotlib import animation
import downloadlightcurve as dtc

# The line above allows you as the user to import periods from the Kepler data
#table
p = 9.6
t = 0.5
hsl.download_kepler_lc
lc = hsl.simulate_transit_data(period=p,t0=t)

def make_transit_curve(lc,):

	''' Here is how to use the function.

	Parameters
	---------------------
	t0 : float
		#time of inferior conjunction
	per: float
		#orbital period
	rp: float
		#planet radius (in units of stellar radii)
 '''




t = lc.time
y = lc.flux
plt.ioff() # turn interactive plotting off

fig , ax  = ppl.create_dome_plot()
line, = ax.plot(t, y, lw=2)
ball, = ax.plot(t[0],y[0],marker= ".", markersize= 30)




def animate(i):
    print (i)
    ball.set_data(t[i], y[i])
    return ball,

# call the animator.  blit=True means only re-draw the parts that have changed.

anim = animation.FuncAnimation(fig, animate,
                               frames=1000, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#extra_args=['-vcodec', 'libx264']
# gif instead of mp4 for this laptop
writer = animation.writers["imagemagick"]()
anim.save('basic_animation.gif',writer= writer )
	#save as pdf or png
plt.savefig('Transit_Curve_Chi.png')
#put in black as background in above line




    #def animate(i):
        #print (i)
        #ball.set_data(t[i], y[i])
        #return ball,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    #anim = animation.FuncAnimation(fig, animate,
                                  # frames=100, interval=20, blit=True)

    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    #extra_args=['-vcodec', 'libx264']
    # gif instead of mp4 for this laptop
    #writer = animation.writers["imagemagick"]()
    #anim.save('360test_movie.gif',writer= writer )

plt.show()
