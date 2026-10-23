import numpy as np
import matplotlib.pyplot as pll
x=np.array([22,43,65,87])
y=np.array([32,43,21,43])

pll.plot(
    x,y,
    mfc='g',
    mec='r',
    c='g',
    marker='s',
    linestyle='solid'

)
pll.show()