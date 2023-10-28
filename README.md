# transit2pi-experiments
This is a set of experiments for developing a set of tools for visualizing transit light curves in a planetarium dome, to take advantage of a very big, 360 degree display! It is a collaboration between Taylor Washington and Zach Berta-Thompson.

## Installation
If you want to be able to modify the code yourself, please fork/clone this repository onto your own computer and install directly from that editable package. For example, this might look like:
```
git clone https://github.com/zkbt/transit2pi-experiments.git
cd transit2pi-experiments/
pip install -e .
```
This will link the installed version of the `transit2pi` package to your local repository. Changes you make to the code in the repository should be reflected in the version Python sees when it tries to `import transit2pi`.

## Usage 

Try this!
```python
import transit2pi as t2p
import lightkurve as lk 
import numpy as np 
import matplotlib.pyplot as plt 

# download a light curve
lcf = lk.search_lightcurve('HD 209458')
lc = lcf[1].download()

# make an array of fluxes
time = lc.time.jd
flux = lc.normalize().flux

# animate the light curve
speed = 1e5
t2p.make_tess_transit_dots(time, 
                           flux, 
                           period=3.5247499, 
                           t0=2455015.49844,
                           speed=speed, 
                           dpi=300, 
                           filename=f'hd209458b-{speed}x-tess.mp4',)
```

## Contributors

This package was written by [Zach Berta-Thompson](https://github.com/zkbt) and [Taylor J. Washington](https://github.com/Tejorwa).
