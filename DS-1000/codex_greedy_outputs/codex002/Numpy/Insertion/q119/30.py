
# The np.random.choice function requires a 1-dimensional array for the probabilities.
# We can create a 1-dimensional array from the list probabilit using np.array().
probabilit = np.array(probabilit)
# Now we can use np.random.choice to select samples from the list lista_elegir with the given probabilities.
samples = np.random.choice(lista_elegir, samples, p=probabilit)
