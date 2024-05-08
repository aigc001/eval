
# Calculate the cumulative distribution function (CDF) for each Z-score
p_values = 1 - scipy.stats.norm.cdf(z_scores, mu, sigma)
