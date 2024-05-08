
# Create a new DataFrame where we apply the aggregation functions separately
df_new = pd.DataFrame({
    'D_max': df.groupby('B')['D'].max(),
    'E_min': df.groupby('B')['E'].min()
})

print(df_new)
