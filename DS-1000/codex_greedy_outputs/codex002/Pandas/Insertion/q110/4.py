
def get_state(row):
    if row['col2'] <= 50 and row['col3'] <= 50:
        return row['col1']
    else:
        return max(row['col1'], row['col2'], row['col3'])

df['state'] = df.apply(get_state, axis=1)
