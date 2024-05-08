
def expand_list(row):
    while len(row) < 3:
        row.append(None)
    return row

df['codes'] = df['codes'].apply(expand_list)

df[['code_1', 'code_2', 'code_3']] = pd.DataFrame(df['codes'].tolist(), index=df.index)
