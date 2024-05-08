
# Create a new array with the same shape as the original array, filled with NaNs
result = np.full(a.shape, np.nan)

# For each row, assign the values from the original array to the new array,
# starting from the shifted index
for i, s in enumerate(shift):
    result[i, s:] = a[i, :a.shape[1]-s]

print(result)
