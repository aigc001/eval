
# Melt the dataframe
melted_df = pd.melt(df, id_vars=['user', 'someBool'], var_name='date', value_name='value')

# Drop the rows where value is None
melted_df = melted_df[melted_df['value'].notnull()]

# Convert date column to datetime
melted_df['date'] = pd.to_datetime(melted_df['date'])

# Sort the dataframe by user and date
melted_df = melted_df.sort_values(['user', 'date'])

# Reset the index
melted_df = melted_df.reset_index(drop=True)

print(melted_df)
