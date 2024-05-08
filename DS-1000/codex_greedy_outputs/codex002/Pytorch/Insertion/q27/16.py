
    # Convert tensors to numpy
    a_np = a.detach().numpy()
    b_np = b.detach().numpy()

    # Use np.vstack to stack vertically
    ab_np = np.vstack((a_np, b_np))

    # Convert back to tensor
    ab = torch.from_numpy(ab_np)

    return ab
