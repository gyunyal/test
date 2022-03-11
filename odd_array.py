# Extract all odd numbers from array of 1-10
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
var = arr[arr % 2 == 1]
print(var)
