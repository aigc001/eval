
# sort by VIM in ascending order and keep the original order for the same VIM
df.sort_values(by='VIM', kind='mergesort', inplace=True)
