
# Define the multinomial log-likelihood function
def multinomial_log_likelihood(params, data):
    # Get the number of categories
    K = len(params)
    # Get the number of data points
    N = len(data)
    # Compute the log-likelihood
    ll = np.sum(np.log(params[data]))
    return ll

# Define the multinomial log-likelihood derivative
def multinomial_log_likelihood_derivative(params, data):
    # Get the number of categories
    K = len(params)
    # Get the number of data points
    N = len(data)
    # Compute the derivative of the log-likelihood
    derivative = np.zeros(K)
    for k in range(K):
        derivative[k] = -np.sum(np.log(params[data != k]))
    return derivative

# Compute the number of categories
K = len(np.unique(a['A1']))
# Set initial guess for parameters
params_init = np.ones(K) / K
# Compute the MLE
params_mle = sciopt.minimize(multinomial_log_likelihood, params_init, args=(a['A1'],), method='BFGS', jac=multinomial_log_likelihood_derivative).x
# Print the MLE
print(params_mle)
