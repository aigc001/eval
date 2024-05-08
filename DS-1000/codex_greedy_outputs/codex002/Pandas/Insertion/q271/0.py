
# Replace pd.NA with np.nan
df.fillna(value=pd.np.nan, inplace=True)

# Round the 'dogs' column to 2 decimal places
df['dogs'] = df['dogs'].round(2)
