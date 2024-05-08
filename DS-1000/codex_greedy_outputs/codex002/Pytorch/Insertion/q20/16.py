
# Create an array of zeros with the shape (len(lens), max(lens))
mask = np.zeros((len(lens), max(lens)))

# For each index and its corresponding length, set the first length elements to 1
for i, length in enumerate(lens):
    mask[i, :length] = 1

# Convert the numpy array to a PyTorch tensor
mask = torch.from_numpy(mask).long()
