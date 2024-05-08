
    # Split the data into features and target
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # Split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
