
# Create a mask of the indices in b
mask = np.zeros_like(a)
mask[np.arange(a.shape[0])[:,None,None],np.arange(a.shape[1])[None,:,None],b] = 1

# Use the mask to select the elements in a and sum them
result = np.sum(a*mask)

print(result)
