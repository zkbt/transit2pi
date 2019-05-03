import transit2pi as t2p
import numpy as np

'''
Here is the script that will help us test 3 cases in the Fiske Planetarium.
'''

import os
try:
    os.mkdir('movies')
except FileExistsError:
    pass

# test different speeds
for speed in [2e4]:
    # test different levels of transparency
    for minalpha in [0, 0.1, 0.2, 0.3, 0.5, 1.0]:
        # test different decay timescales
        for decay in [0.1, 0.2, 0.3, 0.4, 0.5, 1.0]:
            # test different stellar raddi
            for stellar in [0.5, 1.0]:
                # create a custom filename for this particular set of parameters
                filename = 'movies/{}Rsun-speed={:.0f}X-minalpha={:03.0f}-decay={:03.0f}.mp4'.format(stellar, speed, 100*minalpha, 100*decay)

                # print the movie we're trying to write
                print(filename)

                # create an animation
                t2p.make_transit_dots( a=0.0465*212/stellar,
                                            rp=0.10049/stellar,
                                            per=3.65/np.sqrt(stellar), #kludge
                                            speed=speed,
                                            minalpha=minalpha,
                                            decay=decay,
                                            cadence=10.0/24.0/60.0,
                                            ylim=[0.95, 1.01],
                                            filename=filename)
