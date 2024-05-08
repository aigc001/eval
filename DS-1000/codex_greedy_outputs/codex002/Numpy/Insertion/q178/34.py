
# Replace the infinite values with NaN
a[np.isinf(a)] = np.nan

# Compute the mean
mean = np.nanmean(a)
