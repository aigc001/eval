
# replace NaNs with zero
s1[np.isnan(s1)] = 0
s2[np.isnan(s2)] = 0

# compare the two arrays
diff = np.abs(s1 - s2)

# find the indices where the difference is larger than the machine precision
indices = np.where(diff > np.finfo(float).eps)

# print the number of different elements
print(indices[0].shape[0])
