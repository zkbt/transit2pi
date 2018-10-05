import maketransitcurve as mtc
import planetplotlib as ppl
import henrietta as hsl

lc = hsl.download_kepler_lc(raw_input())  # Here import other Kepler planet data
flattened = lc.flatten()
folden= flattened.fold(period=9.28716)
folden.scatter()
binned = folden.bin(25)

fig , ax  = ppl.create_dome_plot()
binned = folden.bin(25)
binned.scatter(ax=ax)


