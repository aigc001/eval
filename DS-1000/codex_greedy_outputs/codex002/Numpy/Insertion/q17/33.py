
# Set the seed for the random number generator
np.random.seed(0)

# Generate the random array
r = np.random.randint(3, size=(100, 2000)) - 1

# Save the array
np.save('r.npy', r)

# Load the saved array
r_loaded = np.load('r.npy')

# Check if the loaded array is the same as the original
print(np.array_equal(r, r_loaded))
