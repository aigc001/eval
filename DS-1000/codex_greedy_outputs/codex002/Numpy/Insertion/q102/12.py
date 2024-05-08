
# get the number of columns in the array
num_cols = a.shape[1]

# constrain the high index to be within the number of columns
high = min(high, num_cols)

# slice the array to get the desired columns
a = a[:, low:high]
