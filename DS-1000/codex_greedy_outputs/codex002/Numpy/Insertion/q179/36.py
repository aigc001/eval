
    # replace inf with nan
    a[np.isinf(a)] = np.nan
    # calculate mean
    mean = np.nanmean(a)
    return mean
