
# Assuming 'date' is the column with the dates
# Sort the dataframe by date
features_dataframe = features_dataframe.sort_values('date')

# Get the index of the row where we should split the data
split_index = int(len(features_dataframe) * (1 - train_size))

# Split the dataframe into train and test sets
train_dataframe = features_dataframe[:split_index]
test_dataframe = features_dataframe[split_index:]
