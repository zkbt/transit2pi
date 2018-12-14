import maketransitcurve as mtc
import planetplotlib as ppl
import henrietta as hsl
from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive
import matplotlib.pyplot as plt
# The line above allows you as the user to import periods from the Kepler data
#table



def make_transit(EP='Kepler-20 b',exo='Kepler-20'):
    ''' Here is how to use the function.

    Parameters
	---------------------
    EP : string of the planet that you want to see the period

    lc : string of the planet you want to download and plot on the figure

    folden : float of the planet period from the KT function
    KT=NasaExoplanetArchive.query_planet(EP)
    You want to write your planet as Kepler -# b or Tess -#
    period = KT['pl_orbper'] # Planet's period from NasaExoplanetArchive

    '''

    KT=NasaExoplanetArchive.query_planet(EP,all_columns = True)
    # Need to update astroquery as dev ver
    #You want to write your planet as Kepler -# b or Tess -#
    period= KT['pl_orbper'].to('day').value # Planet's period from NasaExoplanetArchive
    t0 = KT['pl_tranmid']
    print(t0)
    print(period) #KT['pl_orbper']
    lc = hsl.download_kepler_lc(exo)  # Here import other Kepler planet data



    flattened = lc.flatten()

    folden= flattened.fold(period)
    folden.scatter()


    fig , ax  = ppl.create_dome_plot()
    binned = folden.bin(50)
    folden.scatter(ax=ax)
    binned.scatter(ax=ax)
    plt.savefig('Transit_CurveKepTest_2.png')
    return;
    plt.show()
