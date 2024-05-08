
# Split the duration column into two new columns: 'time' and 'number'
df[['time', 'number']] = df['duration'].str.split(expand=True)

# Create a new column 'time_day' based on the values of 'time' column
df['time_day'] = df['time'].map({'year': 365, 'month': 30, 'week': 7, 'day': 1})

# Multiply 'time_day' with 'number'
df['time_day'] *= df['number'].astype(int)
