
# Combine the two datasets into one array
x = np.concatenate((x1, x2))

# Create a label array that specifies which dataset each value comes from
labels = np.concatenate((np.zeros(len(x1)), np.ones(len(x2))))

# Use the anderson_ksamp function to test if the two datasets are drawn from the same population
result = ss.anderson_ksamp([x1, x2])

# The result is a statistic and a critical values. We can compare the statistic to the critical values to determine if the p-value is less than 0.05
statistic, critical_values, significance_level = result
p_value = critical_values[2]  # The critical value for a significance level of 0.05

# If the p-value is less than 0.05, we reject the null hypothesis and conclude that the two datasets are not drawn from the same population
if p_value < 0.05:
    print("The two datasets are not drawn from the same population.")
else:
    print("The two datasets are drawn from the same population.")
