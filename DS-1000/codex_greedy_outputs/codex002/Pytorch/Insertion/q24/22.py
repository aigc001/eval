
    # Convert 2D tensor to numpy array
    np_array = t.numpy()
    # Create an empty 3D tensor
    Tensor_3D = torch.zeros(t.size(0), t.size(0), t.size(1))
    # Fill the diagonal of each 2D slice with the values from the original tensor
    for i in range(t.size(0)):
        np_array_2D = np.diag(np_array[i])
        Tensor_3D[i] = torch.from_numpy(np_array_2D)
    return Tensor_3D
