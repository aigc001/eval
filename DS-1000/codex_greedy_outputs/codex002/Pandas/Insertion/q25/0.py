
# Convert the list to a DataFrame
List = pd.DataFrame({'Date': List})
List['Date'] = pd.to_datetime(List['Date'])

# Merge the two DataFrames
df = pd.merge(df, List, on='Date', how='inner')

# Convert the date to the desired format
df['Date'] = df['Date'].dt.strftime('%d-%b-%Y %A')

print(df)
