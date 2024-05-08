
# Create an array of the same shape as 'a' with zeros
new_a = np.zeros_like(a)

# Insert the elements at the given indices
new_a[pos] = element

# Create a boolean mask where the inserted elements are True
mask = np.zeros_like(a, dtype=bool)
mask[pos] = True

# Combine the original array 'a' and the new array 'new_a'
# where 'new_a' is True
result = np.where(mask, new_a, a)
