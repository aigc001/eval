
errors = []

for index, row in df.iterrows():
    if not isinstance(row['Field1'], int):
        errors.append(row['Field1'])

print(errors)
