
# Fit the data
params, params_covariance = sp.optimize.curve_fit(bekkers, sample_data, range(range_start,range_end), p0=[estimated_a, estimated_m, estimated_d])

# Create a continuous distribution function from the fitted parameters
def continuous_bekkers(x):
    return bekkers(x, params[0], params[1], params[2])

# Calculate the KS test
ks_statistic, ks_pvalue = sp.stats.kstest(sample_data, continuous_bekkers)

print("KS Statistic: ", ks_statistic)
print("KS p-value: ", ks_pvalue)
