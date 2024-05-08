
# Get the sum of the rows specified in row_list for the columns specified in column_list
sum_df = df.loc[row_list, column_list].sum()

# Delete the largest value
sum_df = sum_df.drop(sum_df.idxmax())

print(sum_df)
