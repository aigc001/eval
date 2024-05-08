
def binary_to_categorical(df):
    df['category'] = df.apply(lambda row: [col for col in df.columns if row[col] == 1], axis=1)
    return df

df = binary_to_categorical(df)
