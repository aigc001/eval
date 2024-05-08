
def remove_after_last_underscore(s):
    split_str = s.split('_')
    if len(split_str) > 1:
        return '_'.join(split_str[:-1])
    else:
        return s

df['SOURCE_NAME'] = df['SOURCE_NAME'].apply(remove_after_last_underscore)
