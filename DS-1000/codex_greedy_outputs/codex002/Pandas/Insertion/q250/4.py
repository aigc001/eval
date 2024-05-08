
# Find columns that contain the string 'spike'
cols = [col for col in df.columns if s in col]

# Rename the columns
for i, col in enumerate(cols):
    df.rename(columns={col: s + str(i+1)}, inplace=True)
