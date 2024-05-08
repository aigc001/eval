
# Step 1: Multiply the column by a number
a[:, col] *= multiply_number

# Step 2: Calculate the cumulative sum of the column
cumulative_sum = np.cumsum(a[:, col])

print(cumulative_sum)
