
def bin_data(df):
    df['group'] = df.index // 3
    df['group_mod'] = df.index % 3
    df['col1_sum'] = df.groupby('group')['col1'].transform('sum')
    df['col1_avg'] = df.groupby('group_mod')['col1'].transform('mean')
    df.loc[df['group_mod'] == 0, 'col1_avg'] = df['col1_sum']
    df.loc[df['group_mod'] == 1, 'col1_avg'] = df['col1_avg']
    df.loc[df['group_mod'] == 2, 'col1_avg'] = df['col1_avg']
    df = df.drop(['group', 'group_mod'], axis=1)
    return df

df = bin_data(df)
