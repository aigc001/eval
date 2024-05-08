
# Calculate pairwise distances
distances = pd.DataFrame(index=df.index, columns=df.index)
for i in df.index:
    for j in df.index:
        distances.loc[i, j] = ((df.loc[i, 'x'] - df.loc[j, 'x'])**2 + (df.loc[i, 'y'] - df.loc[j, 'y'])**2)**0.5

# For each car and time, find the farmost neighbour and corresponding distance
df2 = pd.DataFrame(columns=['time', 'car', 'farmost_neighbour', 'euclidean_distance'])
for t in df['time'].unique():
    for c in df['car'].unique():
        max_distance = 0
        farmost_neighbour = None
        for n in df['car'].unique():
            if c != n:
                distance = distances.loc[df[df['car'] == c].index[0], df[df['car'] == n].index[0]]
                if distance > max_distance:
                    max_distance = distance
                    farmost_neighbour = n
        df2 = df2.append({'time': t, 'car': c, 'farmost_neighbour': farmost_neighbour, 'euclidean_distance': max_distance}, ignore_index=True)
