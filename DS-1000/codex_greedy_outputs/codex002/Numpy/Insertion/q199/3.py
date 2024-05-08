
# Create a copy of the array
arr_temp = arr.copy()

# Create a boolean mask for values less than n1
mask = arr_temp < n1[:, np.newaxis]

# Create a boolean mask for values greater or equal to n2
mask2 = arr_temp >= n2[:, np.newaxis]

# Create a boolean mask for values between n1 and n2
mask3 = ~(mask | mask2)

# Set values less than n1 to 0
arr[mask] = 0

# Set values greater or equal to n2 to 30
arr[mask2] = 30

# Add 5 to the remaining values
arr[mask3] = arr_temp[mask3] + 5
