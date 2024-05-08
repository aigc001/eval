
# Calculate the weighted sample variances
weighted_var = (anobs * avar + bnobs * bvar) / (anobs + bnobs)

# Calculate the weighted sample means
weighted_mean = (amean * anobs + bmean * bnobs) / (anobs + bnobs)

# Calculate the standard deviation of the weighted sample
std_dev = np.sqrt(weighted_var)

# Calculate the standard error of the difference between the means
std_err = np.sqrt(weighted_var * (1/anobs + 1/bnobs))

# Calculate the t-statistic
t_stat = (weighted_mean - 0) / std_err

# Calculate the p-value
p_value = scipy.stats.t.sf(np.abs(t_stat), df=anobs + bnobs - 2) * 2

print("t-statistic:", t_stat)
print("p-value:", p_value)
