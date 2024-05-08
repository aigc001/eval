
    # Create a DataFrame from the list of lists
    df = pd.DataFrame(features)

    # Fill missing values with 0
    df.fillna(0, inplace=True)

    # Convert the DataFrame to a NumPy array
    array = df.values

    # Create a feature selector object
    selector = sklearn.feature_selection.SelectKBest(k=5)

    # Fit the selector to the data
    selector.fit(array, None)

    # Get the mask of selected features
    mask = selector.get_support()

    # Apply the mask to the array
    selected_features = array[:, mask]

    return selected_features
