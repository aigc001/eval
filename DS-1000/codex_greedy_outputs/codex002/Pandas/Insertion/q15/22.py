
def extract_message_data(row):
    # Remove brackets and split string into list of key-value pairs
    pairs = row['message'].replace('[', '').replace(']', '').split(', ')
    
    # Convert list of key-value pairs into dictionary
    pairs = {pair.split(': ')[0]: pair.split(': ')[1] for pair in pairs}
    
    # Return dictionary
    return pairs

# Apply function to each row in dataframe
df_expanded = df.apply(extract_message_data, axis=1, result_type='expand')

# Rename columns to match keys in message
df_expanded.columns = df_expanded.columns.str.replace('[\[\]:]', '')

# Concatenate original dataframe with expanded dataframe
result = pd.concat([df, df_expanded], axis=1)

# Fill NaN values with 'none'
result.fillna('none', inplace=True)

print(result)
