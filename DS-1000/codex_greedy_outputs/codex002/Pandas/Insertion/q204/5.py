
    df = df.set_index('Name')
    df = df.replace(0, np.nan)
    df = df.cumsum(axis=1) / df.count(axis=1)
    return df
