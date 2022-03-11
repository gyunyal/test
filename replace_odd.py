# Replace all odd numbers in an array of 1-10 with the value -1import numpy as np
import numpy as np

numbers = np.arange(1, 10, dtype=int)
for i in range(len(numbers)):
    if (i % 2 == 1):
        numbers[i] = -1
print(numbers)