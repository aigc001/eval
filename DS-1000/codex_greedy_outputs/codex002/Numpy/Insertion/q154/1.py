
# First, we need to get the rankdata for the array
rank = rankdata(a)

# Then, we subtract the rank from the length of the array plus one
# to get the highest rank for the smallest value and vice versa
rank = (len(a)+1) - rank

# Finally, we convert the rank to integer
rank = rank.astype(int)

print(rank)
