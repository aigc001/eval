
# Map the values in the dictionary to the 'Date' column where the 'Member' column matches the key in the dictionary
df['Date'] = df['Member'].map(dict)

# Fill NaN values with a default date
df['Date'].fillna('17/8/1926', inplace=True)

# Convert the date format to 'DD-MMM-YYYY'
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d-%b-%Y')
