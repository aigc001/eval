
# Fit the pipeline
pipe.fit(data, target)

# Get the feature selector from the pipeline
selector = pipe.named_steps['select']

# Get the selected features
selected_features = selector.get_support(indices=True)

# Create a new DataFrame with only the selected features
selected_data = data.iloc[:, selected_features]
