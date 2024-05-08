
def subtract_func(row, arr):
    return row - arr[row.name]

df_result = df.apply(subtract_func, arr=a, axis=1)
