import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import batman
import planetplotlib as ppl



def make_transit_curve(t0=0,per=6.266,rp=0.017,a=6.85,inc=90,ecc=0,w=0) :
	 
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

	params = batman.TransitParams()    #object to store transit parameters
	params.t0 = t0                     #time of inferior conjunction
	params.per = per                   #orbital period
	params.rp = rp             #planet radius (in units of stellar radii)
	params.a = a              #semi-major axis (in units of stellar radii)
	params.inc = inc                      #orbital inclination (in degrees)
	params.ecc = ecc                       #eccentricity
	params.w = w                  #longitude of periastron (in degrees)
	params.limb_dark = "nonlinear"        #limb darkening model
	params.u = [0.5, 0.1, 0.1, -0.1]
	 #limb darkening coefficients [u1, u2, u3, u4

	#t = np.arange(-0.05,0.05,0.001)
	t = np.arange(-per/2,per/2,0.001)
	m = batman.TransitModel(params, t)    #initializes model
	y = m.light_curve(params)
	# First set up the figure, the axis, and the plot element we want to animate
	fig , ax  = ppl.create_dome_plot()

	#ax = plt.axes(xlim=(-0.05, 0.05), ylim=(0.96, 1))
	line, = ax.plot(t, y, lw=2)
	ball, = ax.plot(t[0],y[0],marker= ".", markersize= 30)
	#t = np.arange(input(),input(),0.001)

	#save as pdf or png
	plt.savefig('Transit_Curve1.png')

	#flux = m.light_curve(params)                    #calculates light curve


	return;

	# animation function.  This is called sequentially
	plt.show()

