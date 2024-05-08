
    # First, we get the rankdata for the array
    rank = rankdata(a)
    # Then, we subtract the rank from the length of the array plus one
    # to get the highest rank for the smallest value and vice versa
    return (len(a)+1) - rank.astype(int)
