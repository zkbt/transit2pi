from __future__ import print_function

from .planetplotlib import *
import matplotlib.animation as ani
import batman

from astropy.time import Time

def get_writer(filename, fps=30, **kw):
	'''
	Try to get an appropriate animation writer,
	given the filename provided.

	Parameters
	----------

	filename : str
		The output filename string for the animation.

	fps : float
		Frames/second.

	kw : dict
		All other keywords will be passed to the initialization
		of the animation writer.
	'''
	if '.mp4' in filename:
		try:
			writer = ani.writers['ffmpeg'](fps=fps, **kw)
		except (RuntimeError, KeyError):
			raise RuntimeError('This computer seems unable to ffmpeg.')
	else:
		try:
			writer = ani.writers['pillow'](fps=fps, **kw)
		except (RuntimeError, KeyError):
			writer = ani.writers['imagemagick'](fps=fps, **kw)
			raise RuntimeError('This computer seem unable to animate?')
	return writer


def animate_lightcurve_dots(t0=0,per=6.266,rp=0.1,a=6.85,inc=90,ecc=0,w=0,
					sigma=0.001, ylim=[None, None],
					filename='transit-movie.mp4',
					showtimelabel=False,	fps = 30,	speed = 500000.0,
					minalpha=0.2, maxalpha=1.0, decay=0.2,
					minsize=10, maxsize=50,
					minphase = -0.5, maxphase = 2.5,
						cadence = 0.0034,
					) :

	'''

	This function is based heavilty on `make_transit_curve` written
	by Taylor Washginton.

	Here is how to use the function.

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
	sigma : float
		The noise to inject into the light curve.
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

 # 5 minutes in dayas
	t = np.arange(per*minphase,per*maxphase, cadence)#1)
	m = batman.TransitModel(params, t)    #initializes model
	y = m.light_curve(params)

	flux = np.random.normal(y, sigma)

	# set up the animation writer
	wri = get_writer(filename)

	# First set up the figure, the axis, and the plot element we want to animate
	fi , ax  = create_dome_plot()

	tstep = speed/fps/(86400) # tstep is in days

	def fold(t):
		o = np.atleast_1d((t - params.t0))/params.per % 1
		o[o > 0.5] -= 1
		return o

	start = np.min(t)
	stop = np.max(t)
	tobs = t[0]


	points = ax.scatter(fold(t), flux, marker='o', edgecolor='none')
	#line = ax.plot(fold(t), y)[0]

	# set the initial window to show
	ax.set_xlim(-0.5, 0.5)

	# make sure we have a good ylim
	if ylim[0] is None:
		ylim[0] = np.min(flux)
	if ylim[1] is None:
		ylim[1] = np.max(flux)
	ax.set_ylim(ylim[0], ylim[1])

	# write some text somewhere
	if showtimelabel:
		text = ax.text(0.0, 1.0, Time(tobs, format='jd').iso, ha='left', va='top', transform=ax.transAxes)

	print('Making a movie!')

	# set up the animation to write frames into a movie
	with wri.saving(fi, filename, 100):

		# create an array of window centers to loop through
		#centers = np.arange(start+window/2, stop-window/2, tstep)
		centers = np.arange(start, stop, tstep)

		# loop over those times (shifting the center of the window)
		for i, tobs in enumerate(centers):

			x = t - tobs
			past = x < 0

			points.set_offsets(np.c_[fold(t-tobs)[past], flux[past]])
			#line.set_xdata(fold(t-tobs))

			# define a coordinate that is 0 at current time, and then fades
			decaytime = params.per*decay
			N = len(x)
			weights = np.zeros_like(x).astype(np.float)
			weights[past] = np.maximum(maxalpha*np.exp(x[past]/decay), minalpha)

			# define the colors of the points (alpha-method)
			#colors = np.ones(N)[:,np.newaxis]*np.ones(4)
			#colors[:, -1] = weights

			# define the colors of the points (intensity-method)
			colors = weights[:,np.newaxis]*np.ones(3)

			# set the colors of the points
			points.set_facecolor(colors[past])

			# set the sizes of the points
			points.set_sizes(np.maximum((weights[past])*maxsize, minsize))

			if showtimelabel:
				text.set_text(Time(tobs, format='jd').iso)

			wri.grab_frame()

			# provide an update
			print('completed frame {}/{}'.format(i+1,len(centers), end='\r'))


if __name__ == '__main__':
	animate_lightcurve_dots()
