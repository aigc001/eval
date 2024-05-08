
# Convert the datetime column to a string, specifying the desired format
df['datetime'] = df['datetime'].dt.strftime('%d-%b-%Y %H:%M:%S')
