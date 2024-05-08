
# Calculate the mean and standard deviation
mean = np.mean(a)
std = np.std(a)

# Calculate the 2nd standard deviation
two_std = 2 * std

# Calculate the start and end of the 2nd standard deviation interval
start = mean - two_std
end = mean + two_std

# Return the result as a tuple
result = (start, end)
