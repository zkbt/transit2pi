import henrietta as hsl
from somefile import taylors_awesome_function
lc = hsl.simulate_transit_data(period=1.2, t0=0.5)
# this function makes a (flattened, folded, binned) planetarium light curve plot
taylors_awesome_function(lc, period=1.2, t0=0.5)
