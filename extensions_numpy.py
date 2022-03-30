import numpy as np
a = np.array([1, 2, 3])
print(np.hstack((np.repeat(a, 3), np.tile(a, 3))))

# a = np.array([1,2,3,4,5])
# b = np.array([ 4,5,6,7,8,9])
# repeated=np.argwhere(np.isin(a,b))
# b=np.delete(b,repeated)
# print(a,b)