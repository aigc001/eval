
# Compute the ECDF
ecdf = np.cumsum(np.bincount(grades.astype(int)))
ecdf = ecdf / ecdf[-1]

# Find the longest interval
longest_interval = (0, 0)
for i in range(len(grades)):
    for j in range(i, len(grades)):
        if all(ecdf[grades[i]:grades[j]+1] < threshold):
            if j - i > longest_interval[1] - longest_interval[0]:
                longest_interval = (i, j)
