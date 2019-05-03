#"""
#Matplotlib Animation Example

#author: Jake Vanderplas
#email: vanderplas@astro.washington.edu
#website: http://jakevdp.github.com
#license: BSD
#Please feel free to use and modify this, but keep the above information. Thanks!
#"""
#import params2 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import batman  


params = batman.TransitParams()       #object to store transit parameters
params.t0 = 0.                        #time of inferior conjunction
params.per = 1.                       #orbital period
params.rp = 0.2                       #planet radius (in units of stellar radii)
params.a = 15.                        #semi-major axis (in units of stellar radii)
params.inc = 87.                      #orbital inclination (in degrees)
params.ecc = 0.                       #eccentricity
params.w = 90.                        #longitude of periastron (in degrees)
params.limb_dark = "nonlinear"        #limb darkening model
params.u = [0.5, 0.1, 0.1, -0.1]      #limb darkening coefficients [u1, u2, u3, u4

t = np.arange(-0.05,0.05,0.001)
m = batman.TransitModel(params, t)    #initializes model
y = m.light_curve(params)
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-0.05, 0.05), ylim=(0.96, 1))
line, = ax.plot(t, y, lw=2)
ball, = plt.plot(t[0],y[0],marker= ".", markersize= 30)
#t = np.arange(input(),input(),0.001)



#flux = m.light_curve(params)                    #calculates light curve


# animation function.  This is called sequentially
def animate(i):
    print i
    ball.set_data(t[i], y[i])
    return ball,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate,
                               frames=100, interval=20, blit=True)   # To make transit go all the way around add 100 frames.previously 20.

# save the animation as an gif. This code previously saved this animation as mp4. Which required ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#extra_args=['-vcodec', 'libx264']
# gif instead of mp4 for this laptop
writer = animation.writers["imagemagick"]()
anim.save('basic_animation.gif',writer= writer )

plt.show()
