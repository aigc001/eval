
def split_name(name):
    parts = name.split(' ')
    if len(parts) == 2:
        return parts[0], None, parts[1]
    elif len(parts) == 3:
        return parts[0], parts[1], parts[2]
    else:
        return None, None, None

df[['first_name', 'middle_name', 'last_name']] = df['name'].apply(lambda x: pd.Series(split_name(x)))
