
# First, we remove all the zero values
a = a[a != 0]

# Then, we remove the adjacent duplicates
a = a[np.concatenate(([True], np.diff(a) != 0))]

print(a)
