
def parse_str(s):
    if '_' in s:
        return s.split('_')[-1]
    else:
        return s

df['SOURCE_NAME'] = df['SOURCE_NAME'].apply(parse_str)
