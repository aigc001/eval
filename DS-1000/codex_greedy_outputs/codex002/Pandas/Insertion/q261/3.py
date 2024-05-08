
# Convert the TIME column to datetime
df['TIME'] = pd.to_datetime(df['TIME'])

# Add a new column 'RANK' which ranks the TIME column for each ID in descending order
df['RANK'] = df.groupby('ID')['TIME'].rank(ascending=False, method='dense')

# Format the TIME column to the desired format
df['TIME'] = df['TIME'].dt.strftime('%d-%b-%Y %a %H:%M:%S')
