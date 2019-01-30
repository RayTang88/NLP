import numpy as np
x = np.array([[3.0,4.0],[1, 2]])
demon = np.apply_along_axis(lambda x: np.sqrt(x.T.dot(x)), 1, x)
print 'demon', demon, demon[:]
print demon[:,None]