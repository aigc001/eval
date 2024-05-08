
def rename_columns(df):
    df.columns = [f'{col}X' for col in df.columns]
    return df

df = rename_columns(df)
