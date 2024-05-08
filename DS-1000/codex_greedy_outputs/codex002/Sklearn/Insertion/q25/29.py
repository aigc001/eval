
    # Fit the model
    model.fit(data.drop('t', axis=1), data['t'])
    # Predict
    predictions = model.predict(scaled.drop('t', axis=1))
    # Inverse transform
    predictions = scaler.inverse_transform(predictions)
    # Check score
    score = model.score(data.drop('t', axis=1), data['t'])
    return predictions, score
