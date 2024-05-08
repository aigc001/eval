
def find_diff_columns(df, row1, row2):
    diff_cols = []
    for col in df.columns:
        if df.iloc[row1][col] != df.iloc[row2][col]:
            diff_cols.append(col)
    return diff_cols


diff_cols = find_diff_columns(df, 0, 8)
print(diff_cols)
