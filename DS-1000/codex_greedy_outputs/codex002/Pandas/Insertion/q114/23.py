
    error_list = []
    for index, row in df.iterrows():
        if not isinstance(row['Field1'], int):
            error_list.append(row['Field1'])
    return error_list
