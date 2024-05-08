
    # Reshape the arrays to be 1D
    lat = lat.reshape(-1)
    lon = lon.reshape(-1)
    val = val.reshape(-1)

    # Create a DataFrame from the 1D arrays
    df = pd.DataFrame({'lat': lat, 'lon': lon, 'val': val})

    return df
