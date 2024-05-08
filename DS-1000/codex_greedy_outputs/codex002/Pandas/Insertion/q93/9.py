
    # Convert the date string to datetime
    df.index = pd.to_datetime(df.index)

    # Convert the DataFrame to a numpy array
    arr = df.values

    # Add the converted date index to the numpy array
    arr = np.c_[df.index.values, arr]

    return arr
