
# Fit the data to the function
def fit_func(x, a, m, d):
    return bekkers(x, a, m, d)

# Estimated parameters
params = [estimated_a, estimated_m, estimated_d]

# Calculate the PDF of the fitted function
pdf_values = fit_func(sample_data, *params)

# Calculate the CDF of the fitted function
cdf_values = integrate.cumtrapz(pdf_values, sample_data, initial=0)

# Calculate the CDF of the fitted function for the entire range
full_cdf_values = integrate.cumtrapz(fit_func(np.linspace(range_start, range_end, 1000), *params), np.linspace(range_start, range_end, 1000), initial=0)

# Perform the KS test
ks_result = stats.kstest(cdf_values, 'cdf', full_cdf_values)

# Print the result
print(ks_result)
