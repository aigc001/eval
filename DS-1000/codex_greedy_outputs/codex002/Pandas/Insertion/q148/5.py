
# Group by 'l' and sum 'v'
grouped = df.groupby('l')['v'].sum()

# Replace 0's with np.nan where 'v' is np.nan
grouped[df['v'].isnull()] = np.nan

print(grouped)
