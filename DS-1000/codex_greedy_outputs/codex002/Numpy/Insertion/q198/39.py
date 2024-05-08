
# Create a copy of the array to avoid modifying the original one
arr_temp = arr.copy()

# Create the masks for the different conditions
mask1 = arr_temp < -10  # values lower than -10
mask2 = arr_temp >= 15  # values greater or equal to 15
mask3 = np.logical_and(~mask1, ~mask2)  # values that are neither lower than -10 nor greater or equal to 15

# Apply the changes to the array
arr[mask1] = 0
arr[mask2] = 30
arr[mask3] = arr_temp[mask3] + 5

