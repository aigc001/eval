
# Group by 'Sp' and 'Mt', and for each group, get the row(s) where 'count' is minimum
min_rows = df.loc[df.groupby(['Sp', 'Mt'])['count'].idxmin()]

print(min_rows)
