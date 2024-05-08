
# First, we need to take the logarithm of x
log_x = np.log(x)

# Then, we can use polyfit to fit a line to the logarithm of y against x
log_y = np.log(y)
coefficients = np.polyfit(log_x, log_y, 1)

# The coefficients returned by polyfit are in the form of [B, A]
# So, we need to rearrange them to be in the form of [A, B]
A = np.exp(coefficients[1])
B = np.exp(coefficients[0])

