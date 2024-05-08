
# Calculate Pearson correlation coefficient
correlation_coefficient = np.corrcoef(post, distance)[0, 1]
print("Pearson correlation coefficient: ", correlation_coefficient)
