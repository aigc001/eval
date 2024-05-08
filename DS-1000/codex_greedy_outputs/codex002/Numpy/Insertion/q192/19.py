
# Create a matrix of powers of x
x_matrix = np.vander(x, degree+1)

# Use numpy's polyfit function to find the coefficients
coefficients = np.polyfit(x, y, degree)

# Reverse the coefficients to have them in highest to lowest order
coefficients = coefficients[::-1]

print(coefficients)
