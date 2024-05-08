
# Calculate the weighted t-statistic, p-value, and degrees of freedom
t_statistic, p_value, df = scipy.stats.ttest_ind(a, b, equal_var=False, nan_policy='omit')

print("t-statistic:", t_statistic)
print("p-value:", p_value)
print("degrees of freedom:", df)
