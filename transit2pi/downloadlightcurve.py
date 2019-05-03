# let's import some common Python packages we like
import matplotlib.pyplot as plt, numpy as np

# let's also import our custom Python package for this class
import henrietta as hsl


lc = hsl.download_kepler_lc('Kepler-17')


lc.plot()

# this is the time, in something like Julian Date
time_in_days = lc.time

# this is the relative flux of the star, normalized to the star's median brightness
relative_flux = lc.flux

N = len(time_in_days)
print("Our light curve contains {} data points!".format(N))
