
    # Convert numpy array to list
    a_list = a.tolist()
    # Convert list to torch tensor
    a_tensor = torch.tensor(a_list)
    return a_tensor
