
    # Convert the softmax output to a numpy array
    softmax_output = softmax_output.numpy()

    # Find the index of the maximum value in each row
    max_index = np.argmax(softmax_output, axis=1)

    # Create a new tensor with the class labels
    class_labels = torch.from_numpy(max_index).unsqueeze(1)

    return class_labels
