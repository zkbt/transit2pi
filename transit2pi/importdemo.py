'''
Here's a quick demo how to link modules together with imports.
'''

# these are normal things we import from our standard python directories
import matplotlib.pyplot as plt
import numpy as np

# we can also import our newly written file!
import planetplotlib as ppl

# let's use that function we defined in the other file
domefig, domeax = ppl.create_dome_plot()

# let's make a plot (which will go into the dome axes)
N = 1000
x = np.random.uniform(0, 1, N)
y = np.random.normal(0, 1, N)
plt.scatter(x, y)
plt.show()
