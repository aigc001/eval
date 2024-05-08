
df['date'] = pd.to_datetime(df['date'])
df.sort_values(by='date', inplace=True)
df.reset_index(drop=True, inplace=True)

filter_dates = []
for index, row in df.iterrows():
    if index == 0:
        continue
    if (row['date'] - df.at[index - 1, 'date']).days <= X:
        filter_dates.append(index)

df.drop(df.index[filter_dates], inplace=True)
df['date'] = df['date'].dt.strftime('%d-%b-%Y')
