
# Convert list of lists to DataFrame
df = pd.DataFrame(f)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Convert DataFrame to 2D array
f_array = df.values

# Print the array
print(f_array)
