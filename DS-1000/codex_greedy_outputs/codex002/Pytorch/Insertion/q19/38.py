
max_len = max(lens)
mask = torch.zeros(len(lens), max_len)
for i, l in enumerate(lens):
    mask[i, :l] = 1
