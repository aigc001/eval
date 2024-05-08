
# Generate n random numbers in the range [0,1)
random_numbers = np.random.uniform(0, 1, n)

# Take the logarithm of the random numbers
log_numbers = np.log(random_numbers)

# Scale the logarithms to the desired range
scaled_log_numbers = min + (max - min) * log_numbers

# Exponentiate the scaled logarithms to get the final numbers
final_numbers = np.exp(scaled_log_numbers)
