
# Group by 'Sp' and 'Mt', and for each group, get the row with the maximum 'count'
max_rows = df.loc[df.groupby(['Sp', 'Mt'])['count'].idxmax()]

print(max_rows)
