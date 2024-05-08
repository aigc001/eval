
def compare_rows(df, i, j):
    diffs = []
    for col in df.columns:
        if df.iloc[i][col] != df.iloc[j][col]:
            if pd.isnull(df.iloc[i][col]) and pd.isnull(df.iloc[j][col]):
                continue
            diffs.append((df.iloc[i][col], df.iloc[j][col]))
    return diffs

print(compare_rows(df, 0, 8))
