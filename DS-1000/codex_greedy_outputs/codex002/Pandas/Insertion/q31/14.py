
def rename_columns(df, prefix):
    df.columns = [prefix + col for col in df.columns]
    return df

df = rename_columns(df, 'X')
