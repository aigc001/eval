
from scipy.stats import yeojohnson

# Apply the Yeo-Johnson transformation to each value in the array
transformed_data = np.array([yeojohnson(val).ppf(0.5) for val in data.flatten()])

# Reshape the transformed data back into its original shape
transformed_data = transformed_data.reshape(data.shape)
