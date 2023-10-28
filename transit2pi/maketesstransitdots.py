from __future__ import print_function

from .planetplotlib import *
import batman

from astropy.time import Time

from .animatetools import get_writer


def make_tess_transit_dots(t, flux, period=1, t0=0, ylim=[None, None],
					filename='transit-movie.mp4',
					showtimelabel=False,	fps = 30,	speed = 500000.0,
					minalpha=0.2, maxalpha=1.0, decay=0.2,
					minsize=10, maxsize=50,
						cadence = 0.0034,
						dpi=300
					):
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

	
	# set up the animation writer
	wri = get_writer(filename)

	# First set up the figure, the axis, and the plot element we want to animate
	fi , ax  = create_dome_plot(dpi=dpi, height=3)

	tstep = speed/fps/(86400) # tstep is in days

	def fold(t):
		o = np.atleast_1d((t - t0))/period % 1
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
	with wri.saving(fi, filename, dpi):

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
			decaytime = period*decay
			N = len(x)
			weights = np.zeros_like(x).astype(float)
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
			print('completed frame {}/{}'.format(i+1,len(centers)), end='\r')


if __name__ == '__main__':
	make_transit_dots()
