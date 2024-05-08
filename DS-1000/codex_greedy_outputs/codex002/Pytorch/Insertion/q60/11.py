
    # Get the sign of each element
    sign_x = torch.sign(x)
    sign_y = torch.sign(y)

    # Get the minimum absolute value for each element
    min_abs = torch.min(torch.abs(x), torch.abs(y))

    # Multiply the sign with the minimum absolute value
    result_x = min_abs * sign_x
    result_y = min_abs * sign_y

    return result_x, result_y
