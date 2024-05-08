
# Test if c is in CNTS
print(c in CNTS)

# Remove c from CNTS
CNTS = [x for x in CNTS if not np.array_equal(x, c)]
