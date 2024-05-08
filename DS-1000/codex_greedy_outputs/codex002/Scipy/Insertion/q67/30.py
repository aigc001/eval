
# Calculate the mean and standard deviation of each column
mean = df.mean(axis=0)
std = df.std(axis=0)

# Calculate the z-scores
z_scores = (df - mean) / std

# Print the z-scores
print(z_scores)
