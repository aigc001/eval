
# Generate n random numbers in the range 0 to 1
random_numbers = np.random.uniform(0, 1, n)

# Take the logarithm of the random numbers to get logarithmically distributed numbers
log_numbers = np.log(random_numbers)

# Scale the logarithmically distributed numbers to the desired range
scaled_log_numbers = min + (max - min) * log_numbers / np.log(max)

# Print the first 10 numbers
print(scaled_log_numbers[:10])
