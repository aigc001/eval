
# Find the relative extrema
extrema = signal.argrelmin(arr, order=n)

# Get the indices of the extrema in the original order
indices = np.argsort(extrema[0])

print(extrema[0][indices])
