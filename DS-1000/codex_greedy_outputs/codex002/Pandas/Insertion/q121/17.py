
# Calculate pairwise distances
distances = pd.DataFrame(index=df.car, columns=df.car)
for i in df.car:
    for j in df.car:
        if i != j:
            distances.loc[i, j] = ((df.loc[df.car == i, 'x'] - df.loc[df.car == j, 'x'])**2 + (df.loc[df.car == i, 'y'] - df.loc[df.car == j, 'y'])**2).apply(lambda x: x**0.5)

# Find nearest neighbour
nearest_neighbour = distances.idxmin(axis=1)

# Calculate euclidean distance to nearest neighbour
euclidean_distance = distances.min(axis=1)

# Create result dataframe
df2 = pd.DataFrame({'car': df.car, 'nearest_neighbour': nearest_neighbour, 'euclidean_distance': euclidean_distance})

# Set time as index
df2.set_index('car', inplace=True)

# Calculate average distance for each time point
average_distance = df2.groupby(df.time).euclidean_distance.mean()

# Print result
print(average_distance)
