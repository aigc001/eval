
    # Convert the tensors to numpy arrays for easier manipulation
    a, b = a.numpy(), b.numpy()

    # Create a new array with the desired shape
    result = np.zeros((a.shape[0], a.shape[1] + b.shape[1] - 1))

    # Assign the values from a and b to the new array
    result[:, :a.shape[1]] = a
    result[:, a.shape[1]:] = b

    # Compute the average of the overlapping columns
    result[:, a.shape[1]-1] = (a[:, -1] + b[:, 0]) / 2

    # Convert the result back to a torch tensor
    result = torch.from_numpy(result)

    return result
