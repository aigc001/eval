
df['text'] = df['text'].apply(lambda x: ', '.join(df['text'].tolist()))
df = df.groupby(level=0).first()
