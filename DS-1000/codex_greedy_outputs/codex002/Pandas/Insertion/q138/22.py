
# Group by 'Sp' and 'Value', and for each group, get the row(s) where 'count' is maximum
max_rows = df.loc[df.groupby(['Sp','Value'])['count'].idxmax()]

print(max_rows)
