# Draw a line connecting the points
# \((1,3)\), \((2,10)\), \((6,12)\), and \((18,20)\). Mark each point in green and make the line red and dotted.

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 6, 18])
y = np.array([3, 10, 12, 20])

plt.plot(
    x, y,
    marker='o',
    mfc='g',
    mec='g',
    c='r',
    linestyle='dotted'
)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,6,18])
y=np.array([3,10,12,20,])
plt.plot(
    x,y,
    marker='o',
    mec='g',
    mfc='r',
    c='r',
    linestyle='dotted'
)
