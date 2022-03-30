import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

out = np.vstack((a,b))
print(out)


# a = np.arange(1,10).reshape(3,3)
# b = np.arange(10,19).reshape(3,3)
# c = np.dot(a, b)
# print(c)
# e = np.sum(c, axis = 0)
# print(e)