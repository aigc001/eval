
    # Find the index of the maximum value in each row
    max_values, max_indices = torch.max(softmax_output, dim=1)
    return max_indices
