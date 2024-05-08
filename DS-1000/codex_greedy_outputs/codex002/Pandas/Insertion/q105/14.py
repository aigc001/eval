
def split_name(name):
    if ' ' in name:
        first_name, last_name = name.split(' ', 1)
    else:
        first_name, last_name = name, None
    return first_name, last_name

df['first_name'], df['last_name'] = zip(*df['name'].apply(split_name))
