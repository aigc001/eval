
# Create a dataframe from the numpy arrays
df = pd.DataFrame({'lat': lat.flatten(), 'lon': lon.flatten(), 'val': val.flatten()})

# Add a column with the maximum value of each row
df['maximum'] = df[['lat', 'lon', 'val']].max(axis=1)

print(df)
