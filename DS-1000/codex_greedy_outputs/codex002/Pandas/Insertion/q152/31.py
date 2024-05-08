
def get_relationship(df):
    columns = df.columns
    relationships = []

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            col1 = df[columns[i]]
            col2 = df[columns[j]]

            if col1.nunique() == col2.nunique():
                relationships.append(f'{columns[i]} {columns[j]} one-2-one')
            elif col1.nunique() > col2.nunique():
                relationships.append(f'{columns[i]} {columns[j]} one-2-many')
            else:
                relationships.append(f'{columns[i]} {columns[j]} many-2-one')

    return relationships

relationships = get_relationship(df)
for relationship in relationships:
    print(relationship)
