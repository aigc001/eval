
# Get the column names that contain 'val'
value_columns = [col for col in df.columns if 'val' in col]

# Group by 'group' and take the sum of the value columns
grouped_df = df.groupby('group').agg({"group_color": "first", **{col: "sum" for col in value_columns}})

print(grouped_df)
