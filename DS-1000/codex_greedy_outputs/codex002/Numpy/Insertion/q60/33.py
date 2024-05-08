
# Combine the two datasets
ab = np.concatenate([a, b])

# Calculate the weights for each dataset
weights = np.concatenate([np.ones(len(a))/len(a), np.ones(len(b))/len(b)])

# Calculate the weighted mean and standard deviation
mean = np.average(ab, weights=weights)
std_dev = np.sqrt(np.average((ab-mean)**2, weights=weights))

# Calculate the t-statistic and p-value
t_statistic, p_value = scipy.stats.ttest_1samp(ab, 0, weights=weights)

print("t-statistic:", t_statistic)
print("p-value:", p_value)
