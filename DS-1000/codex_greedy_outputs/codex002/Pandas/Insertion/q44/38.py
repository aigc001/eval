
def shift_values(row):
    row_values = row.values
    shifted_values = row_values[~np.isnan(row_values)]
    shifted_values = np.roll(shifted_values, 1)
    shifted_values[0] = np.nan
    return shifted_values

df_shifted = df.apply(shift_values, axis=1)
