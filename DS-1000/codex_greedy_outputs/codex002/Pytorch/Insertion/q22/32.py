
    max_len = max(lens)
    mask = np.zeros((len(lens), max_len))
    for i, l in enumerate(lens):
        mask[i, :l] = 1
    return torch.LongTensor(mask)
