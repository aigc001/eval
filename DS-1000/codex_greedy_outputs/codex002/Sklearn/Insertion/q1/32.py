
# Create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)

# Add the target column
df['target'] = data.target

# Add the target names column
df['target_names'] = data.target_names[data.target]
