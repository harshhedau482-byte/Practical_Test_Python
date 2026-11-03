# Q.7

import numpy as np

# 1. Create a = np.arange(10, 51, 5) and print it[cite: 2]
a = np.arange(10, 51, 5)
print(a)

# 2. Array of zeros (3, 4) and ones (2, 5, dtype=float). Print shapes and sum of ones array on one line[cite: 2]
zeros_arr = np.zeros((3, 4))
ones_arr = np.ones((2, 5), dtype=float)
print(zeros_arr.shape, ones_arr.shape, ones_arr.sum())

# 3. Print np.eye(3) multiplied by 4[cite: 2]
print(np.eye(3) * 4)

# 4. Create lin = np.linspace(0, 10, 50) and print its length, lin[1] rounded to 4 decimals, and last value[cite: 2]
lin = np.linspace(0, 10, 50)
print(len(lin), round(float(lin[1]), 4), float(lin[-1]))

# 5. Call np.random.seed(7), create r, print r, replace first row with 100, print row, and print bottom-right 2x2 block[cite: 2]
np.random.seed(7)
r = np.random.randint(1, 21, size=(4, 4))
print(r)

r[0] = 100
print(r[0])

print(r[-2:, -2:])


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

# Q.8


import numpy as np

# 1. Boolean masks for ages
ages = np.array([25, 30, 18, 35, 22, 40, 17])
print(ages[ages >= 18])                                    # 18 or more
print(ages[(ages > 20) & (ages < 35)])                     # strictly between 20 and 35
print(ages[~(ages >= 18)])                                   # not 18 or more

# 2. Using np.where for scores
scores = np.array([65, 80, 72, 90, 55, 78])
print(np.where(scores >= 75, "Pass", "Fail"))

# 3. Boolean mask and modification on temps
temps = np.array([28, 32, 25, 35, 30, 22, 38])
mask = temps > 30
temps[mask] = 31
print(temps, int(mask.sum()))

# 4. Slicing a 2D array (matrix)
mat = np.arange(1, 26).reshape(5, 5)
print(mat[1:4, 2:5])  # Rows 1-3 (index 1 to 4) and columns 2-4 (index 2 to 5)

# 5. View vs Copy demonstration
view = mat[0]
view[0] = 99
print(mat[0, 0])  # Prints 99 because 'view' shares memory with 'mat'

copy = mat[1].copy()
copy[0] = -1
print(mat[1, 0])  # Prints 6 because 'copy' is independent and doesn't affect 'mat'

print("-------------------------------------------------------------------------------------------------------------------------------------")

# Q.9
import numpy as np

# 1. Element-wise operations, rounding, and matrix product
A = np.arange(1, 10).reshape(3, 3)
B = np.arange(11, 20).reshape(3, 3)
print(A * B)
print(np.round(A / B, 2))
print(A @ B)

# 2. Z-score calculation, rounding, and mean of z-scores
arr = np.array([10, 20, 30, 40, 50], dtype=float)
z_scores = np.round((arr - arr.mean()) / arr.std(), 2)
print(z_scores, float(np.round(z_scores.mean(), 6)))

# 3. Euclidean distance between points p and q
p = np.array([0, 0, 0])
q = np.array([3, 4, 12])
print(float(np.sqrt(np.sum((p - q) ** 2))))

# 4. Statistical operations on array v
v = np.array([4, 9, 2, 15, 7, 1])
print(np.argmax(v), np.argmin(v), v.max(), v.min())
print(float(v.mean()), float(np.median(v)), float(round(v.var(), 2)), float(round(v.std(), 2)))

# 5. Sorting a 2D array along different axes
m = np.array([[9, 3, 1], [6, 8, 2], [5, 7, 4]])
print(np.sort(m, axis=0))
print(np.sort(m, axis=1))

# 6. Count positive, negative, and zero values
pn = np.array([-3, 0, 5, -1, 0, 8, 2, -7, 0])
print(int((pn > 0).sum()), int((pn < 0).sum()), int((pn == 0).sum()))

print("------------------------------------------------------------------------------------------------------------------------------------------------------")

# Q.10

import numpy as np

# 1. Reshape and flatten comparison
vals = np.arange(1, 16)
print(vals.reshape(5, -1).shape)
print(vals.reshape(3, 5).flatten().tolist() == vals.tolist())

# 2. Broadcasting with sales, bonus, and rates
sales = np.array([[10, 20], [15, 25], [12, 18]])
bonus = np.array([2, 3, 1])[:, np.newaxis]
print(sales + bonus)
rates = np.array([0.1, 0.05])
print(np.round(sales * rates, 2))

# 3. Splitting arrays with try/except
arr = np.arange(1, 10 + 1)
try:
    np.split(arr, 3)
except ValueError:
    print("ValueError")
print([part.tolist() for part in np.array_split(arr, 3)])