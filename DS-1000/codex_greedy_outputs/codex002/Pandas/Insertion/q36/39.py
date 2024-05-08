
# Select rows from the dataframe based on the row_list
df_selected = df.iloc[row_list]

# Select columns from the dataframe based on the column_list
df_selected = df_selected[column_list]

# Calculate the mean of the selected rows and columns
mean_values = df_selected.mean()

print(mean_values)
