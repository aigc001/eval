
# expand W to match the batch size and reshape it to perform batch matrix multiplication
result = torch.bmm(data, W.expand(10, hid_dim, 1)).squeeze()
result = result.view(10, 2, 3)
