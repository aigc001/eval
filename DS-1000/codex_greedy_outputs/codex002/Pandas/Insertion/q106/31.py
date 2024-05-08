
def split_name(name):
    if ' ' in name:
        first, last = name.split(' ', 1)
        return first, last
    else:
        return name, None

df['1_name'], df['2_name'] = zip(*df['name'].apply(split_name))
