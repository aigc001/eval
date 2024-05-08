
    # parse date index using pd.to_datetime
    df.index = pd.to_datetime(df.index)
    # swap the two levels
    df.swaplevel(0, 1, axis=0, inplace=True)
    return df
