
# create an array of NaNs with the same shape as the original array
shifted_a = np.full_like(a, np.nan)

# fill the shifted array with the shifted values
shifted_a[shift:] = a[:-shift]

print(shifted_a)
