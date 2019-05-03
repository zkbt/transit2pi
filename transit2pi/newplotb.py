import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import batman
import planetplotlib as ppl



def make_transti_curve() :
	 




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
	fig , ax  = ppl.create_dome_plot()

	#ax = plt.axes(xlim=(-0.05, 0.05), ylim=(0.96, 1))
	line, = ax.plot(t, y, lw=2)
	ball, = ax.plot(t[0],y[0],marker= ".", markersize= 30)
	#t = np.arange(input(),input(),0.001)

	#save as pdf or png
	plt.savefig('Transit_Curve.png')

	#flux = m.light_curve(params)                    #calculates light curve


	# animation function.  This is called sequentially
	plt.show()

