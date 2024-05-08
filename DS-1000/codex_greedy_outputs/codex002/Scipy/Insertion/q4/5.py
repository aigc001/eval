
test_stat, p_value = stats.ks_2samp(x, y)
if p_value < alpha:
    print("We can reject the null hypothesis that the two distributions are identical")
else:
    print("We cannot reject the null hypothesis that the two distributions are identical")
