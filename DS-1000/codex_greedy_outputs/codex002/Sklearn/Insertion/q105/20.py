
# Assuming 'date' is the column with the dates
# Sort the dataframe by date
features_dataframe = features_dataframe.sort_values('date')

# Get the index of the row where we should split the data
split_index = int(len(features_dataframe) * train_size)

# Split the data into train and test sets
train_dataframe = features_dataframe.iloc[:split_index]
test_dataframe = features_dataframe.iloc[split_index:]
