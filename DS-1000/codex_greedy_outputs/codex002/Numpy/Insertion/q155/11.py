
# First, we need to reverse the array
a = a[::-1]
# Then, we calculate the rankdata
rank = rankdata(a)
# Finally, we subtract the rank from the length of the array plus one
result = (len(a)+1) - rank.astype(int)
print(result)
