
from scipy.stats import boxcox

# Apply Box-Cox transformation
transformed_data, lam = boxcox(data)

# If lambda is less than 0.01, we assume that the data is approximately normal
if lam < 0.01:
    print("Data is approximately normal.")
else:
    print("Data is not normal, lambda: ", lam)
