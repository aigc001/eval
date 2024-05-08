
# Generate an array of size 'size' with 'one_ratio' number of ones and the rest zeros
random_array = np.concatenate((np.ones(int(size*one_ratio)), np.zeros(int(size*(1-one_ratio)))))
# Shuffle the array to make the ones randomly distributed
np.random.shuffle(random_array)
