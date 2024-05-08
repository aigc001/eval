
z_scores = []
for p in p_values:
    z = scipy.stats.norm.ppf(p)
    z_scores.append(z)
print(z_scores)
