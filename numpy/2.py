# To create an element-wise comparison using greater than (>), g
# reater than or equal to (>=), less than (<), and less than or equal to (<=).

import numpy as np

x=np.array([1,2,3,4])
y=np.array([1,4,6,4])

print("Greater")
print(np.greater(x,y))

print(">=")
print(np.greater_equal(x,y))

print("<")
print(np.less(x,y))

print("<=")
print(np.less_equal(x,y))



# import numpy as np
# x=np.array([3,4,5,6])
# y=np.array([5,4,3,6])
# print(np.greater(x,y))
# print(np.greater_equal(x,y))
# print(np.less(x,y))
# print(np.less_equal(x,y))