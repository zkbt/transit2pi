import animatedots as ad
import numpy as np

'''
Here is the script that will help us test 3 cases in the Fiske Planetarium.
'''
#Case 1: rs = 1 Rsun, rp=0.10049, a=0.0465*212


for speed in [2e4]:
    for minalpha in [0, 0.1, 0.2, 0.3, 0.5, 1.0]:
        for decay in [0.1, 0.2, 0.3, 0.4, 0.5, 1.0]:
            for stellar in [0.5, 1.0]:
                filename = 'movies/{}Rsun-speed={:.0f}X-minalpha={:03.0f}-decay={:03.0f}.mp4'.format(stellar, speed, 100*minalpha, 100*decay)
                ad.animate_lightcurve_dots( a=0.0465*212/stellar,
                                            rp=0.10049/stellar,
                                            per=3.65/np.sqrt(stellar), #kludge
                                            speed=speed,
                                            minalpha=minalpha,
                                            decay=decay,
                                            cadence=10.0/24.0/60.0,
                                            ylim=[0.95, 1.01],
                                            filename=filename)
