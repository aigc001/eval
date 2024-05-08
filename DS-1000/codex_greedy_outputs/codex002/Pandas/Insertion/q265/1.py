
def equal_or_both_nan(x, y):
    return (x == y) or (np.isnan(x) and np.isnan(y))


def equal_columns(df, row1, row2):
    return df.columns[df.loc[row1].apply(equal_or_both_nan, args=(df.loc[row2],))]


print(equal_columns(df, 0, 8))
