
def bin_data(df):
    df['group'] = df.index // 3  # Create groups of every 3 rows
    df['group_size'] = df.groupby('group').size()  # Get the size of each group

    # For every 3 rows, get the sum. For every 2 rows, get the average.
    df['col1'] = df.groupby('group')['col1'].transform(lambda x: x.sum() if x.size == 3 else x.mean())

    # Drop the group and group_size columns
    df.drop(['group', 'group_size'], axis=1, inplace=True)

    return df


df = bin_data(df)
