
# scale the data
scaled_data = preprocessing.scale(data)

# create a new DataFrame using the scaled data and the original DataFrame's index and columns
scaled_dataframe = pd.DataFrame(scaled_data, index=data.index, columns=data.columns)
